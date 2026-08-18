# Implementation Tasks: PoC 1 - Redis High-Concurrency Mutex & Atomic Stock Reservation

> **Change ID:** `poc01-redis-mutex-flashsale`  
> **Target Path:** `pocs/poc01-redis-mutex-flashsale/`

---

## Task Breakdown (TDD Pipeline)

- [ ] **Task 1: Setup PoC Boilerplate & Docker Environment**
  - Create directory `pocs/poc01-redis-mutex-flashsale/`
  - Initialize Node.js TypeScript project with Fastify & ioredis
  - Create `docker-compose.yml` with Redis v7 and PostgreSQL v16 services
- [ ] **Task 2: Write Unit & Integration Tests (TDD Red Phase)**
  - Write test: Concurrent stock reservation must never result in stock < 0
  - Write test: Duplicate request with same lock key within TTL must be rejected
- [ ] **Task 3: Implement Redis Lua Stock Script & Mutex Middleware**
  - Implement `reserve_stock.lua` script with `redis.eval`
  - Implement `RedisLockManager` class with `acquireLock` and `releaseLock` (UUID + TTL)
- [ ] **Task 4: Implement Reserve Endpoint & Async Worker**
  - Build `POST /api/v1/flash-sale/reserve` endpoint in Fastify
  - Build Redis Queue worker to flush confirmed claim tokens to PostgreSQL asynchronously
- [ ] **Task 5: Write k6 Load Testing Script (5,000 QPS)**
  - Create `k6/flashsale_stress_test.js` targeting 5,000 VUs / 5,000 QPS
  - Assert zero overselling: Total 200 OK responses MUST equal initial stock exactly
- [ ] **Task 6: Contabo VPS Deployment & SigNoz Verification**
  - Deploy PoC 1 stack to Contabo VPS using Docker Compose
  - Capture p99 latency chart and include metrics in CV milestone report
