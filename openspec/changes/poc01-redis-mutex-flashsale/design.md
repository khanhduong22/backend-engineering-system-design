# System Design: PoC 1 - Redis High-Concurrency Mutex & Atomic Stock Reservation

> **Change ID:** `poc01-redis-mutex-flashsale`  
> **Target Module:** `pocs/poc01-redis-mutex-flashsale`

---

## 1. Technical Components & Tech Stack

- **Runtime:** Node.js v20 / Fastify (for maximum HTTP QPS throughput) or NestJS Fastify Adapter.
- **Cache / In-Memory Storage:** Redis v7 (Dockerized).
- **Database (Async Persistence):** PostgreSQL 16 (Dockerized).
- **Load Testing Tool:** Grafana k6 (5,000 QPS test script).
- **Monitoring & Metrics:** SigNoz APM / Prometheus + Grafana (Containerized on VPS).

---

## 2. Core Implementation Details

### A. Redis Atomic Lua Script (`reserve_stock.lua`)
```lua
-- KEYS[1]: stock_key (e.g., 'flashsale:item:1001:stock')
-- ARGV[1]: requested_qty (e.g., 1)

local current_stock = tonumber(redis.call('GET', KEYS[1]))

if not current_stock or current_stock <= 0 then
    return -1 -- Sold Out
end

if current_stock < tonumber(ARGV[1]) then
    return -2 -- Insufficient Stock
end

local new_stock = redis.call('DECRBY', KEYS[1], ARGV[1])
return new_stock
```

### B. Distributed Mutex Lock (SET NX PX)
```typescript
async function acquireLock(redis: Redis, lockKey: string, lockValue: string, ttlMs: number): Promise<boolean> {
  const result = await redis.set(lockKey, lockValue, 'PX', ttlMs, 'NX');
  return result === 'OK';
}

async function releaseLock(redis: Redis, lockKey: string, lockValue: string): Promise<boolean> {
  const luaScript = `
    if redis.call("get", KEYS[1]) == ARGV[1] then
      return redis.call("del", KEYS[1])
    else
      return 0
    end
  `;
  const res = await redis.eval(luaScript, 1, lockKey, lockValue);
  return res === 1;
}
```

---

## 3. Comparative Trade-offs Table (Pros & Cons)

| Approach | Pros | Cons | Performance & Complexity | Recommendation |
|---|---|---|---|---|
| **Option A: Pure DB Row Lock (`SELECT FOR UPDATE`)** | Simple, ACID guarantees | DB bottleneck under high QPS, connection pool exhaustion | Poor (p99 > 500ms at 5k QPS) | ❌ Do NOT use for Flash Sale |
| **Option B: Redis Mutex + Lua Script + Async DB Sync** | Ultra-high QPS (5k-10k QPS), zero overselling, <5ms latency | Eventual DB consistency | Exceptional (p99 < 8ms) | ✅ **RECOMMENDED (PoC 1)** |
| **Option C: Optimistic Locking (`version` column in DB)** | No pessimistic locks | High retry rate under high contention | Moderate (High CPU retry overhead) | ❌ High retry overhead |
