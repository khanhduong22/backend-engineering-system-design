# Capability Specification: Flash Sale Distributed Mutex & High-Concurrency Stock Engine

## Overview
This specification governs high-concurrency stock reservation mechanics, preventing overselling (negative inventory) and cache stampedes under high request rates (5,000+ QPS) using Redis Distributed Mutex Locks and Atomic Lua Scripts.

---

## Capabilities & Scenarios

### Requirement: Atomic Inventory Decr (Anti-Overselling)
The system MUST ensure that inventory decrement operations are strictly atomic and non-blocking under extreme concurrency.

#### Scenario: Successful stock decrement when inventory is available
- **GIVEN** a flash sale item `item:1001` has a Redis inventory count of `10`
- **WHEN** 50 concurrent purchase requests hit the `/api/v1/flash-sale/reserve` endpoint simultaneously
- **THEN** exactly 10 requests MUST receive a `200 OK` reservation status with a valid claim token
- **AND** remaining 40 requests MUST receive a `409 Conflict` (Sold Out) status within <5ms latency
- **AND** the Redis key `item:1001:stock` MUST equal `0` (NEVER negative).

#### Scenario: Distributed Mutex Lock (Redlock / SET NX PX)
- **GIVEN** a user `user:88` is executing a checkout transaction for item `item:1001`
- **WHEN** a duplicate request for the same user and item arrives within 200ms
- **THEN** the system MUST acquire a Redis Mutex `lock:user:88:item:1001` using `SET key uuid NX PX 5000`
- **AND** the duplicate request MUST fail immediately with `429 Too Many Requests` (Lock Acquired by Concurrent Request).

#### Scenario: Async DB Persistence & Resilience
- **GIVEN** stock has been reserved in Redis atomically
- **WHEN** the reservation token is confirmed by the worker
- **THEN** the system MUST dispatch an async event to PostgreSQL using `INSERT INTO orders ... ON CONFLICT (order_id) DO NOTHING`
- **AND** if PostgreSQL is temporarily unavailable, the reservation MUST be backed up in a Redis Dead Letter Queue (DLQ).
