# 05_SystemDesign_Architecture - System Design & Distributed Architecture Study Guide

- **Total Cards**: 1439

---

## 📂 Category: API Design (10 cards)

### 🟢 Junior Level

#### 1. Describe the query API design for an ad click event aggregator.
**Answer:**
API 1: GET /v1/ads/{:ad_id}/aggregated_count - Retrieves the aggregated click count for a specific ad over a time window. Parameters include 'from' (start minute), 'to' (end minute), and 'filter' (filtering strategy, e.g., geographic filter). Returns 'ad_id' and 'count'.
API 2: GET /v1/ads/popular_ads - Returns the top N most clicked ads in a given time window. Parameters include 'count' (top N), 'window' (M minutes), and 'filter'. Returns an array of 'ad_ids'.

#### 2. What are the core API endpoints for a URL shortener system?
**Answer:**
1. URL shortening: POST api/v1/data/shorten taking a {longUrl} parameter and returning a short URL.
2. URL redirection: GET api/v1/shortUrl which resolves the short URL and returns a longURL for HTTP redirection.

#### 3. What are the primary benefits and use cases of implementing an API rate limiter?
**Answer:**
Prevents resource starvation and mitigates Denial of Service (DoS) attacks (intentional or accidental). Reduces infrastructure costs and third-party API expenses by capping billable or high-resource calls. Protects backend servers from being overloaded by bots or misbehaving client applications.

#### 4. What does a file revision API look like and what parameters does it typically take?
**Answer:**
Example API: https://api.example.com/files/list_revisions
Parameters:
• path: The path to the file to get the revision history for.
• limit: The maximum number of revisions to return.
Example payload: {"path": "/recipes/soup/best_soup.txt", "limit": 20}

#### 5. What is the API structure for downloading a file from cloud storage like Google Drive?
**Answer:**
The download API endpoint typically follows a RESTful structure, such as `https://api.example.com/files/download`, accepting parameters in a JSON payload where the `path` specifies the target file location (e.g., `{"path": "/recipes/soup/best_soup.txt"}`).

#### 6. What is the purpose of the HTTP response code 429?
**Answer:**
It indicates a user has sent too many requests (Too Many Requests), commonly used in rate limiting.

#### 7. What is the standard API design and execution status endpoint for a payment system order?
**Answer:**
The execution status of a single payment order is typically exposed via a RESTful endpoint using the HTTP GET method: `GET /v1/payments/{:id}`, which returns the status based on the `payment_order_id`.


### 🟡 Mid Level

#### 1. What are the core REST API endpoints required for a basic webmail service?
**Answer:**
1. POST /v1/messages: Sends a message to recipients in To, Cc, and Bcc headers.
2. GET /v1/folders: Returns all folders of an email account (e.g., All, Archive, Drafts, Flagged, Junk, Sent, Trash).
3. GET /v1/folders/{folder_id}/messages: Returns paginated messages under a folder.
4. GET /v1/messages/{message_id}: Retrieves metadata, sender/recipient info, subject, body, and read status of a specific message.

#### 2. What is idempotency in distributed systems?
**Answer:**
Idempotency is the property where an operation can be applied multiple times without changing the result beyond the initial application. From an API standpoint, it allows clients to make the same call repeatedly and produce the exact same outcome, serving as a key mechanism for achieving at-most-once delivery guarantees.

#### 3. Why should monetary amounts be transmitted and stored as strings rather than floating-point numbers in a payment system API?
**Answer:**
Doubles and floats suffer from precision inconsistencies across different hardware/software architectures, leading to rounding errors. Furthermore, values can be exceedingly large or small (e.g., Bitcoin satoshis). Striving to keep numbers in string format prevents unintended loss of precision during serialization/deserialization.


## 📂 Category: API Design & Concurrency (1 cards)

### 🟡 Mid Level

#### 1. How can an idempotent API be used to avoid double reservations?
**Answer:**
1. Generate a unique reservation_id via a globally unique ID generator. 2. Pass this reservation_id as part of the submission request as a primary key constraint in the database table. 3. If a user clicks complete/submits twice, the database's unique constraint on the primary key prevents duplicate record creation.


## 📂 Category: API Design & Concurrency Control (1 cards)

### 🟡 Mid Level

#### 1. How do you prevent duplicate actions (like double-clicking a 'book' or 'pay' button) from creating multiple resources?
**Answer:**
Use client-side mitigations (disabling buttons, though unreliable) combined with server-side Idempotent APIs. An idempotency key (such as a shopping cart ID or reservation UUID) is passed in the request header. If multiple concurrent requests arrive with the same key, only the first is processed; subsequent ones either return the cached previous result or a '429 Too Many Requests' status code.


## 📂 Category: API Design & Data Pipelines (1 cards)

### 🟡 Mid Level

#### 1. What are the primary functional requirements when designing a query API for an ad click event aggregator?
**Answer:**
The API must:
1. Aggregate the total number of clicks for a given `ad_id` over a rolling time window (e.g., the last M minutes).
2. Return the top N most clicked `ad_ids` in a given time frame.
3. Support aggregation filtering and querying by various categorical attributes for dashboards used by data scientists and advertisers.


## 📂 Category: API Design & E-Commerce (1 cards)

### 🟡 Mid Level

#### 1. Describe the RESTful API design and idempotency handling for a hotel reservation system.
**Answer:**
Exposes RESTful endpoints for hotels, rooms, and reservations (e.g., GET /v1/hotels/ID, POST /v1/reservations). The POST /v1/reservations endpoint requires a reservationID acting as an idempotency key to prevent double-booking (multiple reservations for the same room on the same day).


## 📂 Category: API Design & Gaming (1 cards)

### 🟢 Junior Level

#### 1. Describe the API design for a scalable gaming leaderboard.
**Answer:**
1. POST /v1/scores: Internal API called only by game servers to update user points when winning a game.
2. GET /v1/scores: Fetches the top 10 players.
3. GET /v1/scores/{:user_id}: Fetches the specific rank, score, and user info for a given user.


## 📂 Category: API Design & Gateway (1 cards)

### 🟢 Junior Level

#### 1. How does a client determine whether its requests are being rate-limited by a service?
**Answer:**
The client inspects HTTP response headers returned by the rate limiter: X-Ratelimit-Remaining (remaining allowed requests in the current window), X-Ratelimit-Limit (total calls allowed per window), and X-Ratelimit-Retry-After (seconds to wait before retrying). Exceeding the limit results in a '429 Too Many Requests' status along with the retry header.


## 📂 Category: API Design & Rate Limiting (3 cards)

### 🟢 Junior Level

#### 1. What is the most widely used rate limiting algorithm?
**Answer:**
The token bucket algorithm is widely used for rate limiting due to its simplicity and robust understanding. It is commonly used by internet companies like Amazon and Stripe to throttle API requests.


### 🟡 Mid Level

#### 1. How do you decide on the number of buckets when implementing the token bucket rate-limiting algorithm?
**Answer:**
Bucket allocation depends on the granularity of the rate limit: 1) Different endpoints require separate buckets per user (e.g., 1 post/sec, 150 friends/day require 3 separate buckets per user). 2) IP-based throttling requires a bucket per IP address. 3) System-wide limits (e.g., max 10,000 requests/sec globally) utilize a single shared global bucket.

#### 2. What is a token bucket algorithm?
**Answer:**
A rate-limiting mechanism using a container of fixed capacity where tokens are added at a constant preset rate. When a request arrives, tokens are consumed; if the bucket is empty, the request is throttled or dropped. Excess tokens generated beyond capacity overflow and are discarded.


## 📂 Category: API Design & Resiliency (3 cards)

### 🟢 Junior Level

#### 1. What is a rate limiter and how does it function in a network system?
**Answer:**
A rate limiter controls the rate of traffic sent by a client or service by tracking HTTP request counts over a specified period. If requests exceed the defined threshold, excess calls are blocked to protect downstream services.

#### 2. What is the standard HTTP response code and subsequent action when a client exceeds its rate limit?
**Answer:**
APIs return HTTP status code 429 (Too Many Requests). Depending on the use case, rate-limited requests (such as critical orders) can be enqueued into a message broker/queue to be processed asynchronously later during off-peak traffic.


### 🟡 Mid Level

#### 1. What are the most common rate-limiting algorithms?
**Answer:**
1. Token bucket
2. Leaking bucket
3. Fixed window counter
4. Sliding window log
5. Sliding window counter


## 📂 Category: API Design & Scalability (2 cards)

### 🟢 Junior Level

#### 1. What are the main benefits of using an API rate limiter?
**Answer:**
The key benefits include: preventing resource starvation caused by DoS attacks or misbehaving clients, reducing operational costs by limiting excessive calls, and preventing server overload to maintain system stability.


### 🟡 Mid Level

#### 1. What are the core parameters required for the token bucket rate-limiting algorithm?
**Answer:**
1. Bucket size: The maximum number of tokens allowed in the bucket at any given time.
2. Refill rate: The exact number of tokens added to the bucket per second.


## 📂 Category: API Design & Traffic Management (3 cards)

### 🟢 Junior Level

#### 1. What is the impact on request processing when a rate limiter is added?
**Answer:**
When a client exceeds the defined capacity (e.g., sending 3 requests when the limit is 2 requests per second), the rate limiter middleware throttles the excess request and returns an HTTP status code 429 (Too Many Requests).


### 🟡 Mid Level

#### 1. How do we monitor and tune rate limiters?
**Answer:**
Gather analytics data to verify if the rate-limiting algorithm and rules are effective. If rules are too strict, valid requests drop, requiring rule relaxation. If sudden traffic spikes (like flash sales) bypass limits or break effectiveness, switch to burst-friendly algorithms like the Token Bucket.

#### 2. What foundational requirements and parameters must be gathered when designing a rate limiter?
**Answer:**
1. Placement: Client-side vs. server-side API rate limiter.
2. Throttling Key: Throttling based on IP address, User ID, API key, or custom properties.
3. Scale: Startup scale vs. enterprise scale with massive user bases.
4. Distribution: Single-node vs. distributed environment synchronization.
5. Architecture: Dedicated standalone service vs. middleware embedded directly in application code.
6. User Feedback: Protocol and mechanism for notifying throttled users (e.g., HTTP 429 status code).


## 📂 Category: API Gateway & Rate Limiting (3 cards)

### 🟢 Junior Level

#### 1. How does a token bucket-based rate limiter work?
**Answer:**
Each request consumes one token. When a request arrives, the system checks if there are enough tokens in the bucket. If sufficient tokens exist, one token is removed per request and the request is allowed to proceed. If the bucket does not have enough tokens, the request is dropped or rate-limited.

#### 2. What are common examples of rate-limiting rules used in API gateways?
**Answer:**
Rate-limiting rules restrict traffic based on specific criteria defined in configuration files and stored on disk. Common examples include limiting a client to a maximum number of specific actions over a time window (e.g., maximum 5 marketing messages per day, or a login endpoint restricted to a maximum of 5 attempts in 1 minute).


### 🟡 Mid Level

#### 1. Should a rate-limiter be implemented on the API gateway or on the application server?
**Answer:**
There is no absolute answer; it depends on the tech stack, resources, and requirements. Guidelines: 1) Evaluate the programming language and cache service efficiency for server-side implementation. 2) Server-side gives full algorithm control, whereas third-party gateways limit customization. 3) If using a microservices architecture with an existing API gateway handling auth and IP filtering, adding rate-limiting there is convenient. 4) Building a custom rate limiter takes engineering resources; a commercial API gateway is preferred if resources are constrained.


## 📂 Category: API Gateway & Resiliency (1 cards)

### 🟡 Mid Level

#### 1. Describe the high-level request lifecycle and data flow of a Redis-backed rate limiter middleware.
**Answer:**
1. A client sends a request that passes through a rate-limiting middleware.
2. The middleware retrieves the current request counter from the corresponding bucket in Redis and evaluates it against defined limits.
3. If the limit is reached, the request is immediately rejected.
4. If the limit is not reached, the request is forwarded to downstream API servers, while the middleware asynchronously or synchronously increments the Redis counter.


## 📂 Category: API Gateway & Security (2 cards)

### 🟢 Junior Level

#### 1. What are some common examples of rate limiting rules in web applications?
**Answer:**
Examples include limiting posts per second, account creations per day from the same IP address, or reward claims per week from the same device.


### 🟡 Mid Level

#### 1. What are the core architectural characteristics required of a robust distributed rate limiter?
**Answer:**
- Accurately limit excessive requests.
- Low latency (must not impact HTTP response time).
- Minimal memory footprint.
- Distributed rate limiting shared across multiple nodes/processes.
- Clear user exception handling/throttling responses.
- High fault tolerance (cache failures must not crash the entire application).


## 📂 Category: API Gateway & Traffic Management (1 cards)

### 🟢 Junior Level

#### 1. What is an API rate limiter?
**Answer:**
An API rate limiter is a component or system that restricts the number of client requests allowed to be sent over a specified time period to protect backend services from overload and abuse.


## 📂 Category: APIs & Protocols (1 cards)

### 🟢 Junior Level

#### 1. What is a common API response format used to transfer data between clients and web servers?
**Answer:**
JSON (JavaScript Object Notation) is the most common lightweight data-interchange format used for API responses in modern web and mobile applications.


## 📂 Category: Algorithms (1 cards)

### 🟡 Mid Level

#### 1. What are practical applications of graph algorithms in system architecture?
**Answer:**
Car navigation systems use shortest-path algorithms (e.g., Dijkstra's/A*) over road network graphs, and search engines use PageRank over the web graph to determine document popularity and rankings.


## 📂 Category: Algorithms & Data Structures (2 cards)

### 🟡 Mid Level

#### 1. How do routing algorithms like Dijkstra’s and A* work in mapping systems like Google Maps?
**Answer:**
They operate on a graph data structure where intersections are nodes and roads are edges. Because performance is sensitive to graph size, the global road network must be partitioned into manageable units rather than represented as a single large graph.


### 🔴 Senior Level

#### 1. How are large-scale road networks broken down into manageable units for routing algorithms?
**Answer:**
Road networks are subdivided using tiling concepts similar to geohashing, dividing the world into small geographical grids called 'routing tiles'. Each tile contains a local graph of nodes (intersections) and edges (roads) and holds references to adjacent connected tiles. Routing algorithms load these tiles on-demand, minimizing memory footprint and boosting pathfinding performance.


## 📂 Category: Application Protocols (1 cards)

### 🟡 Mid Level

#### 1. How do email clients implement conversational threads using headers?
**Answer:**
Threads group email replies with original messages using three core email headers: `Message-Id` (unique ID generated by the sending client), `In-Reply-To` (parent message ID being replied to), and `References` (list of related message IDs in the thread chain).


## 📂 Category: Architecture (3 cards)

### 🟢 Junior Level

#### 1. Explain horizontal vs vertical scaling
**Answer:**
Vertical scaling (scale-up) adds more resources (CPU, RAM) to a single server, bounded by hardware limits and single-point-of-failure risks. Horizontal scaling (scale-out) adds more machines to a cluster, distributing load via load balancers for near-infinite scalability and high availability.

#### 2. What is a stateless web tier?
**Answer:**
An architectural pattern where user session data and persistent state are externalized to a shared persistent storage layer (such as a database or distributed cache) rather than being stored locally on the web servers.


### 🟡 Mid Level

#### 1. How do we convert a synchronous ad click processing design to an asynchronous one?
**Answer:**
Insert a message queue (such as Kafka) between producers and consumers. This decouples them, prevents consumer out-of-memory errors and sudden shutdowns during traffic spikes, and allows producers and consumers to scale independently.


## 📂 Category: Architecture Basics (1 cards)

### 🟢 Junior Level

#### 1. What components typically run on the same server in a basic single-server setup?
**Answer:**
The web application, database, and cache are all running on the same server.


## 📂 Category: Architecture Fundamentals (2 cards)

### 🟢 Junior Level

#### 1. What are the characteristics of a stateless system architecture?
**Answer:**
In a stateless architecture, HTTP requests can be routed to any web server because user session state is kept out of the servers and stored in a shared data store (like a database or distributed cache). This makes the system simpler, more robust, and horizontally scalable.

#### 2. What is software architecture and what are its main concerns?
**Answer:**
Software architecture refers to the fundamental structures of a software system, the discipline of creating them, and documentation of these structures. Main concerns include scalability, maintainability, fault tolerance, security, and performance.


## 📂 Category: Architecture Patterns (3 cards)

### 🔴 Senior Level

#### 1. Describe the static and dynamic models of event sourcing.
**Answer:**
In event sourcing, a state machine handles two primary functions: validating commands into events and applying events to update state. Architecturally, this can be modeled statically as dual state machines (command validation vs. event application). In the dynamic model over a time dimension, the system continuously ingests incoming commands, validates them, emits immutable events, and processes them sequentially to materialize current state.

#### 2. What is CQRS and how does it relate to Event Sourcing?
**Answer:**
Command-Query Responsibility Segregation (CQRS) separates read and write operations. In Event Sourcing, instead of publishing state updates, all state-changing events are published. There is one state machine responsible for writes, and multiple read-only state machines (projections/views) that consume events to build customized read views.

#### 3. Why is event data the only component requiring a high-reliability guarantee in event sourcing?
**Answer:**
State and snapshots can be rebuilt by replaying the event list. Commands cannot guarantee reproducibility because event generation is non-deterministic and can involve random factors or external I/O. Therefore, immutable historical events are the sole source of truth requiring strong durability.


## 📂 Category: Back-of-the-Envelope Estimation (4 cards)

### 🟡 Mid Level

#### 1. What are the back-of-the-envelope calculations for a URL shortener generating 100 million URLs per day over 10 years?
**Answer:**
Write QPS = 100,000,000 / (24 * 3600) = ~1,160 QPS. Assuming a 10:1 read-to-write ratio, Read QPS = 11,600 QPS. Over 10 years: 100 million * 365 * 10 = 365 billion records. Assuming an average URL length of 100 bytes, total storage requirement over 10 years = 365 billion * 100 bytes * 10 years = 365 TB.

#### 2. What are the back-of-the-envelope calculations for a proximity service?
**Answer:**
Seconds in a day = 24 * 60 * 60 = 86,400 (rounded up to 10^5 for easier calculation). Assuming a user makes 5 search queries per day with 100 million users: Search QPS = 100 million * 5 / 10^5 = 5,000 QPS.

#### 3. What are the back-of-the-envelope estimations for an ad click event aggregator supporting 1 billion DAU?
**Answer:**
1 billion DAU, assuming 1 ad click per user daily = 1 billion ad click events per day. Ad click QPS = 10^9 events / 10^5 seconds = 10,000 average QPS. Peak QPS (5x average) = 50,000 QPS. At 0.1 KB per ad click event, daily storage = 100 GB, and monthly storage = ~3 TB.


### 🔴 Senior Level

#### 1. What are the back-of-the-envelope estimations for a cloud storage service like Google Drive with 50 million signed up users and 10 million DAU?
**Answer:**
Users receive 10 GB free space (Total space allocated: 50 million * 10 GB = 500 Petabytes). Assuming 2 uploads per user/day with an average file size of 500 KB and a 1:1 read-to-write ratio: Upload API QPS = 10 million * 2 / 86,400 = ~240 QPS. Peak QPS = 480 QPS.


## 📂 Category: Big Data & Analytics (2 cards)

### 🟡 Mid Level

#### 1. What functional requirements, data scales, and edge cases must be defined when designing an ad click event aggregator?
**Answer:**
1. Input Data: Appended log files containing ad_id, click_timestamp, user_id, ip, and country.
2. Scale: 1 billion ad clicks/day, 2 million total ads, growing 30% YoY.
3. Core Queries: Return click count for an ad in the last M minutes; return top 100 most clicked ads in the past minute (configurable); support filtering by IP, user_id, or country.
4. Edge Cases: Late-arriving events, duplicate events, and partial system outages requiring recovery.
5. Latency: A few minutes of end-to-end latency is acceptable (unlike real-time bidding) since it serves billing and reporting pipelines.


### 🔴 Senior Level

#### 1. What are alternative data storage and aggregation designs for an ad click event aggregator?
**Answer:**
Instead of specialized big-data setups, a common generic pattern is storing raw ad click data in distributed storage (e.g., Hive) with an indexing layer (e.g., Elasticsearch) built for fast queries. Aggregation and analytical queries are typically handled by OLAP databases optimized for column-oriented storage, such as ClickHouse or Apache Druid.


## 📂 Category: Big Data & Batch Processing (2 cards)

### 🟡 Mid Level

#### 1. How do we compute the top N most clicked ads using a MapReduce architecture?
**Answer:**
Map input click events by `ad_id`. Each intermediate aggregate node maintains a localized heap data structure to efficiently compute the top N ads locally. Finally, a Reduce node merges the localized top results from all aggregate nodes to output the global top N most clicked ads.


### 🔴 Senior Level

#### 1. How do we scale a MapReduce-based aggregation service for high throughput?
**Answer:**
Scale horizontally by adding or removing compute nodes. To increase throughput per node, choose between multi-threading (`ad_id`-based thread allocation) or distributed cluster resource managers like Apache Hadoop YARN for multi-processing scale-out.


## 📂 Category: Big Data & Real-time Processing (1 cards)

### 🔴 Senior Level

#### 1. Describe the architecture and data flow for real-time ad click event aggregation.
**Answer:**
Ad click events flow as unbounded real-time data streams into and out of the aggregation service. The processing utilizes a MapReduce or Directed Acyclic Graph (DAG) model, breaking the system down into small computing units (Map/Aggregate/Reduce nodes) where each node performs a single task and passes results downstream.


## 📂 Category: Big Data Architecture (1 cards)

### 🔴 Senior Level

#### 1. What are the core functional requirements of a large-scale ad event aggregator?
**Answer:**
Aggregate click counts for any given ad_id over the last M minutes; return the top 100 most-clicked ads every minute; support aggregation filtering by arbitrary attributes; handle high-volume ingestions at Facebook or Google scale.


## 📂 Category: Caching (24 cards)

### 🟢 Junior Level

#### 1. Explain cache warming
**Answer:**
The process of proactively populating a cache with frequently accessed data (e.g., via background jobs or pre-computed queries) before serving production traffic. This prevents cold-start latency spikes and sudden database load surges.

#### 2. Explain the concept of cache-aside (look-aside) pattern
**Answer:**
In the cache-aside (or look-aside) pattern, the application code directly interacts with the cache and the primary database. When a read request occurs, the application checks the cache first; on a cache miss, it reads from the database, populates the cache with the retrieved data, and returns it to the client. On writes, the application updates the database directly and then either invalidates or updates the cache entry.

#### 3. How is load typically balanced across N cache servers using basic hashing?
**Answer:**
serverIndex = hash(key) % N, where N is the total size of the server pool.

#### 4. How is the location cache structured for a nearby friends application, and what data store is typically used?
**Answer:**
Redis is typically used for the location cache to store the real-time geographic positions of active users. The data model maps user_id (key) to a hash or JSON structure containing {latitude, longitude, timestamp} (value).

#### 5. What are the common cache eviction policies?
**Answer:**
When a cache is full, adding new items triggers eviction:
• LRU (Least Recently Used): Evicts items that haven't been accessed for the longest time.
• LFU (Least Frequently Used): Evicts items with the lowest access frequency.
• FIFO (First In, First Out): Evicts the oldest items added to the cache.

#### 6. What are the trade-offs when configuring cache expiry times?
**Answer:**
Cache expiry time should neither be too long (which risks serving stale content) nor too short (which causes excessive repeat reloading and load on origin servers).

#### 7. What is a cache and how does it improve application performance?
**Answer:**
A cache is a high-speed, temporary storage layer (typically in-memory) that holds the results of expensive computations or frequently accessed data so subsequent requests can be served rapidly. Caching reduces repetitive database queries and significantly lowers application latency.

#### 8. What is a common strategy to mitigate a Single Point of Failure (SPOF) in caching?
**Answer:**
A common strategy is to deploy and replicate multiple cache servers across different availability zones or data centers.

#### 9. What is a read-through caching strategy?
**Answer:**
A caching pattern where the application interacts directly with the cache. If a requested data item is missing from the cache, the cache itself queries the persistent database, stores the retrieved response internally, and returns it to the caller.

#### 10. What is cache eviction?
**Answer:**
Cache eviction is the process of removing existing items from a cache when it is full and new items need to be added.

#### 11. What is the most popular cache eviction policy?
**Answer:**
Least-Recently-Used (LRU).

#### 12. What is the purpose and benefit of a database/system cache tier?
**Answer:**
The cache tier is a temporary, high-throughput, low-latency data store layer placed in front of primary databases. Benefits include vastly improved read performance, reduced database workloads, and the ability to scale the caching tier independently from the persistence layer.

#### 13. What is the purpose of the Time-to-Live (TTL) header in the context of a CDN and caching?
**Answer:**
The TTL header or setting describes how long an asset, image, or cache entry is valid and stored before it expires or requires revalidation.

#### 14. What type of content is typically cached by Content Delivery Networks (CDNs)?
**Answer:**
Static content like images, videos, CSS, and JavaScript files.


### 🟡 Mid Level

#### 1. Explain cache sharding
**Answer:**
The practice of partitioning a caching layer across multiple physical or virtual nodes using a deterministic hashing algorithm (like consistent hashing). This scales out total cache capacity and throughput beyond the limits of a single machine.

#### 2. How do we cache reservations and inventory in a hotel booking system to handle high read volumes?
**Answer:**
Move inventory query operations to an in-memory cache (Redis) pre-populated with keys structured as hotelID_roomTypeID_{date} and values representing available rooms. The Inventory DB serves as the source of truth, while the cache handles read-heavy workloads (which outnumber writes by orders of magnitude).

#### 3. How is consistency maintained between a data store and a cache?
**Answer:**
Consistency involves keeping the data store and cache in sync. Inconsistency occurs because data-modifying operations on the data store and cache are typically not executed within a single distributed transaction. Maintaining consistency becomes especially challenging when scaling across multiple regions.

#### 4. What are the common cache consistency patterns?
**Answer:**
Common cache consistency patterns include Cache-Aside (Lazy Loading), Write-Through, Write-Behind (Write-Back), and Refresh-Ahead. Each balances read latency differently against the risk of serving stale data and write performance complexity.

#### 5. What is the role of a distributed cache in an email system?
**Answer:**
Since the most recent emails are repeatedly loaded by clients, caching recent emails in memory (e.g., using Redis for its rich data structures and scalability) significantly improves load times.

#### 6. What is the thundering herd problem in caching?
**Answer:**
The thundering herd problem occurs when a heavily requested cache key expires, or a popular item is missing, causing a massive concurrent influx of client requests to simultaneously bypass the cache and hit the underlying database, potentially overwhelming it.

#### 7. Why are raw location coordinates (latitude and longitude) poor cache keys for proximity services?
**Answer:**
GPS coordinates from mobile devices are prone to slight fluctuations and measurement noise even when stationary, and user movement causes continuous micro-changes. Using raw coordinates results in cache misses. Instead, solutions like Geohash or Quadtrees map nearby locations and businesses to a discrete grid cell, ensuring stable cache keys.


### 🔴 Senior Level

#### 1. Explain cache coherence
**Answer:**
The mechanism that ensures consistency of shared resource data stored in multiple local caches (or distributed cache nodes). When data is modified in one cache, invalidation or update signals must be propagated to other caches holding that data to prevent stale reads.

#### 2. What is the architectural pattern of a decentralized distributed cache?
**Answer:**
In a decentralized distributed cache architecture, nodes are peers rather than having a rigid master-slave hierarchy. Each node typically performs multiple roles independently, such as handling client requests, participating in consistent hashing ring routing, maintaining peer health checks (gossip protocol), and managing its own local memory/eviction policies.

#### 3. What is the multi-layer cache architecture typically used in a news feed service?
**Answer:**
1. News Feed: Stores IDs of news feeds.
2. Content: Stores post data, with popular content cached in a hot cache.
3. Social Graph: Stores user relationships and follow graphs.
4. Action: Stores metadata on user interactions (likes, replies, shares).
5. Counters: Stores aggregated metrics like like counts, reply counts, and follower counts.


## 📂 Category: Caching & Concurrency (1 cards)

### 🔴 Senior Level

#### 1. How are race conditions or cache-database inconsistencies handled in a hotel reservation system?
**Answer:**
If a cache indicates an empty room exists but the database shows none, the user attempts to reserve it. The database performs the authoritative validation and rejects the request if no rooms remain. The client receives an error stating the room was just booked. Subsequent refreshes sync the accurate database inventory back to the cache.


## 📂 Category: Caching & Content Delivery (4 cards)

### 🟢 Junior Level

#### 1. How are static assets like map tiles efficiently retrieved and cached?
**Answer:**
Static assets like map tiles are served via Content Delivery Networks (CDNs). A client requests a tile from the CDN; if missing, the CDN fetches it from the origin server, caches it locally, and serves it. Subsequent requests hit the nearest Point of Presence (POP), providing high scalability and performance.


### 🟡 Mid Level

#### 1. How can you optimize search autocomplete (Trie) response times and handle regional variances (e.g., top search queries differing by country)?
**Answer:**
Build separate tries localized for different countries and store these tries close to users by caching them in Content Delivery Networks (CDNs) at edge locations.

#### 2. What are the core considerations when designing a caching layer in a system architecture?
**Answer:**
Key considerations include deciding when to use cache, defining expiration policies, handling cache consistency, mitigating cascading failures (e.g., cache stampedes), and choosing appropriate eviction policies (e.g., LRU, LFU).

#### 3. What are the key considerations and trade-offs when setting an appropriate cache expiry and invalidation strategy for a CDN?
**Answer:**
Cache expiry should balance freshness and origin load. If too long, content is stale; if too short, it causes frequent cache misses and thrashes origin servers. For invalidation before expiry, methods include using CDN vendor APIs or object versioning (e.g., query strings like image.png?v=2). Cost is also a factor since CDNs charge for data transfer; caching infrequently accessed assets yields low benefit.


## 📂 Category: Caching & Data Consistency (1 cards)

### 🔴 Senior Level

#### 1. How can an asynchronous cache update mechanism (such as CDC) handle cache-database inconsistency in a hotel reservation system?
**Answer:**
1. Architecture: The inventory database is updated first; changes are subsequently propagated to the cache asynchronously via application logic or Change Data Capture (CDC) pipelines using tools like Debezium.
2. Consistency Window: A temporary state window exists where the cache may be out of sync with the primary database (e.g., indicating a room is available when sold out, or vice versa).
3. Resolution: This temporary inconsistency is acceptable because the transactional database acts as the strict final source of truth and performs the ultimate inventory validation check during booking.


## 📂 Category: Caching & Geospatial (1 cards)

### 🟡 Mid Level

#### 1. What is the role of Redis location cache in a nearby friends feature?
**Answer:**
Redis stores the most recent location data for each active user with a Time-to-Live (TTL) set on each entry. When the TTL expires due to lack of heartbeats, the user is considered inactive and location data is expunged.


## 📂 Category: Caching & In-Memory Data Stores (2 cards)

### 🟡 Mid Level

#### 1. How do you efficiently store and update scores in a monthly leaderboard using Redis?
**Answer:**
Maintain a separate Redis sorted set for each month (e.g., `leaderboard_feb_2021`), archiving previous months to historical storage. When a user scores points, invoke the `ZINCRBY` command, which automatically increments the user's score or adds them to the sorted set if they do not yet exist (e.g., `ZINCRBY leaderboard_feb_2021 1 'mary1934'`).


### 🔴 Senior Level

#### 1. How do you utilize caching and TTL mechanisms to optimize hotel reservation and inventory systems?
**Answer:**
Hotel inventory applies primarily to current and future dates. Use Redis to cache inventory with a Time-To-Live (TTL) expiration mechanism and Least Recently Used (LRU) eviction policy to manage memory efficiently. Place inventory checks and reservation logic in the cache layer to block invalid requests, but always fall back to the primary database as the ultimate source of truth before finalizing a booking.


## 📂 Category: Caching & In-Memory Databases (1 cards)

### 🟡 Mid Level

#### 1. What factors should be considered when sizing Redis nodes?
**Answer:**
Write-heavy applications require significantly more available memory to accommodate writes while creating snapshots during failures (allocate roughly twice the memory to be safe). Redis-benchmark can be used to simulate multiple clients and queries to test hardware throughput.


## 📂 Category: Caching & In-Memory Stores (1 cards)

### 🟡 Mid Level

#### 1. Which in-memory data store and data type provide predictable performance and easy access for leaderboards with millions of users?
**Answer:**
Redis using sorted sets. Because Redis operates entirely in-memory, it enables fast reads and writes, and its sorted set data type natively handles leaderboard ranking operations without complex database queries.


## 📂 Category: Caching & Performance (4 cards)

### 🟢 Junior Level

#### 1. What are the pros and cons of caching in a hotel reservation system?
**Answer:**
Pros:
- Reduced database load since read queries are answered by the cache layer.
- High performance because read queries are fetched directly from fast in-memory stores.
Cons:
- Maintaining data consistency between the database and the cache is difficult and requires careful design to avoid negatively impacting user experience.


### 🟡 Mid Level

#### 1. What Redis sorted set operations are commonly used to implement a high-performance leaderboard, and what are their time complexities?
**Answer:**
1. ZADD: Inserts a user or updates their score. Complexity: $O(\log(n))$.
2. ZINCRBY: Increments a user's score by a delta (defaults score to 0 if non-existent). Complexity: $O(\log(n))$.
3. ZRANGE / ZREVRANGE: Fetches a range of users sorted by score within specified indices. Complexity: $O(\log(n) + m)$ where $m$ is the number of elements fetched.
4. ZRANK / ZREVRANK: Retrieves a user's absolute ordinal position in ascending/descending order. Complexity: $O(\log(n))$.

#### 2. What additional caching optimizations can be implemented for a leaderboard system?
**Answer:**
As a small performance optimization, create an additional cache of user details, specifically targeting the top 10 players since they are retrieved most frequently. This minimizes load without consuming excessive memory.

#### 3. What optimizations can be applied to a query service to guarantee very quick responses in an autocomplete search system?
**Answer:**
1. AJAX requests: Fetch autocomplete suggestions asynchronously without refreshing the entire web page.
2. Browser caching: Cache suggestions locally (e.g., Cache-Control with `private` and `max-age=3600`) to eliminate round-trips for repeated typing.
3. Data sampling: For massive-scale systems, log only a fraction of queries (e.g., 1 out of every N requests) to reduce processing and storage overhead.


## 📂 Category: Caching & Search Systems (1 cards)

### 🟡 Mid Level

#### 1. Describe the high-level design and cache-aside query resolution mechanism for an autocomplete search query service.
**Answer:**
1. A search query hits a load balancer and routes to API servers.
2. API servers retrieve prefix data from a Trie Cache to construct autocomplete suggestions.
3. On a cache miss (caused by cache eviction or server restart), the system queries the primary database, replenishes the Trie Cache, and returns suggestions, ensuring subsequent requests for the same prefix are served directly from cache.


## 📂 Category: Caching & Storage (6 cards)

### 🟢 Junior Level

#### 1. How can caching be utilized in a metrics collection service?
**Answer:**
Cache servers are added in front of or alongside the time-series database to store frequent query results, thereby reducing database load and improving query service performance.

#### 2. How do we mitigate Single Points of Failure (SPOF) and memory exhaustion when using caching servers?
**Answer:**
Deploy multiple cache servers across distinct availability zones or data centers, and overprovision cache memory by a calculated percentage buffer to absorb unexpected spikes in memory consumption.


### 🟡 Mid Level

#### 1. How do we handle system failure recovery and data persistence for a Redis-backed leaderboard?
**Answer:**
Configure Redis with read replicas for automatic failover. Maintain supporting tables (user and point) in a relational database like MySQL to store game history and timestamps. In the event of a catastrophic failure, these historical entries can be re-run offline using ZINCRBY to completely reconstruct the Redis leaderboard.

#### 2. What is a Trie Cache and how is it used in persistent storage architectures?
**Answer:**
A Trie Cache is a distributed cache system that keeps a trie in memory for fast read operations, taking a weekly snapshot of the database. The persistent storage counterpart (Trie DB) can be stored using either a Document store (by periodically serializing the snapshot) or a Key-Value store (by mapping every prefix to a hash table key and node data to a hash table value).


### 🔴 Senior Level

#### 1. How do we scale and improve availability of a high-throughput location cache in a nearby friends service?
**Answer:**
Use Redis with TTLs renewed on every location update to cap memory usage. Because 10 million users updating every 30 seconds yields ~334K writes/sec, shard the Redis cache by user ID to distribute the load. Replicate each shard to a standby node with quick promotion to minimize downtime.

#### 2. How should one evaluate the necessity of a caching layer in a proximity service?
**Answer:**
Evaluate if the workload is read-heavy and if the dataset is small enough to fit into the working set of a modern database server. If queries are not I/O bound, they run fast without a cache. Read replicas can also improve read throughput. Careful benchmarking and cost analysis are required before implementation.


## 📂 Category: Caching & Storage Strategies (1 cards)

### 🟡 Mid Level

#### 1. How do you handle business info CRUD operations and caching in a proximity service?
**Answer:**
Separate business-related APIs from the Location Based Service (LBS). When fetching business details, check the Redis cache first; if missing, query the database cluster and populate the cache. For newly added or updated businesses, update cached data via a nightly synchronization job based on business agreements.


## 📂 Category: Caching Strategies (1 cards)

### 🟡 Mid Level

#### 1. What is the stale-while-revalidate caching strategy?
**Answer:**
A caching directive where a cache returns stale content immediately to a client request while asynchronously issuing a background request to fetch and update the cache with fresh data from the origin server.


## 📂 Category: Capacity Estimation (1 cards)

### 🔴 Senior Level

#### 1. What is the storage usage estimation for a global map tile service?
**Answer:**
At zoom level 21, there are approximately 4.3 trillion tiles. Assuming each tile is a 256x256 pixel compressed PNG image of about 100 KB, the raw storage required for the highest zoom level is roughly 440 PB. Factoring in that ~90% of the Earth's surface consists of natural/uninhabited areas (which are highly compressible), the estimate reduces by 80-90% to around 50 PB for the highest zoom level. Accounting for lower zoom levels using a geometric series where each lower level reduces tile count (and storage) by 4x (50 + 50/4 + 50/16 + ...), the total storage requirement across all zoom levels is roughly ~67 PB, rounding up to approximately 100 PB for a safe capacity margin.


## 📂 Category: Capacity Planning (11 cards)

### 🟢 Junior Level

#### 1. Provide a back-of-the-envelope estimation for a payment processing system.
**Answer:**
- Transaction volume: 1 million transactions per day.
- Average TPS: 1,000,000 transactions / 10^5 seconds = 10 TPS.
- Architectural takeaway: 10 TPS is trivial for standard relational databases; therefore, the system design interview focus should center on ACID consistency, idempotency, distributed locking, and fault tolerance rather than high throughput.

#### 2. What is a back-of-the-envelope estimation?
**Answer:**
According to Google Senior Fellow Jeff Dean, back-of-the-envelope calculations are rough estimates created using thought experiments and standard performance numbers to quickly evaluate whether a proposed system design will meet its scale and latency requirements.


### 🟡 Mid Level

#### 1. Provide a back-of-the-envelope estimation for a gaming leaderboard with 5 million DAU.
**Answer:**
- Average request rate: 5,000,000 DAU / 10^5 seconds = ~50 users/sec.
- Peak load multiplier: Assuming a 5x peak factor, peak load = 250 users/sec.
- Score-submitting QPS: 50 users/sec * 10 games/day = ~500 average QPS; Peak score QPS = 500 * 5 = 2,500 QPS.
- Top 10 leaderboard-fetching QPS: Assuming users fetch it once daily upon opening the game = ~50 QPS.

#### 2. Provide a back-of-the-envelope estimation for a hotel reservation system.
**Answer:**
- Inventory: 5,000 hotels and 1 million rooms total.
- Daily reservations: (1 million rooms * 70% occupancy) / 3-day average stay = ~233,333 (~240,000) reservations/day.
- Reservation TPS: 240,000 / 10^5 seconds = ~3 TPS.
- Funnel QPS (working backward assuming 10% conversion per step): Detail page QPS = 300, Booking confirmation page QPS = 30, Final reservation TPS = 3.

#### 3. Provide a back-of-the-envelope estimation for a search autocomplete system.
**Answer:**
- DAU: 10 million, with 10 searches per user per day.
- Request payload: 20 bytes per query string (4 words * 5 characters * 1 byte ASCII).
- Request amplification: ~20 requests sent per query (one per keystroke).
- Average QPS: (10M * 10 * 20 chars) / 86,400s = ~23,148 (~24,000) QPS.
- Peak QPS: 2 * Average QPS = ~48,000 QPS.
- Daily incremental storage: 10M users * 10 queries * 20 bytes * 20% new queries = 0.4 GB/day.

#### 4. Provide a back-of-the-envelope estimation for a video streaming service with 5 million DAU.
**Answer:**
- Daily uploads: 5 million DAU * 10% upload rate = 500,000 videos/day.
- Storage needed: 500,000 videos * 300 MB average size = 150 TB/day.
- CDN egress cost: 5 million DAU * 5 videos/day * 0.3 GB * $0.02/GB (CloudFront US pricing) = $150,000/day in bandwidth costs.

#### 5. Provide a back-of-the-envelope estimation for a web crawler handling 1 billion web pages per month.
**Answer:**
- Average QPS: 1,000,000,000 pages / (30 days * 24 hours * 3600 seconds) = ~400 pages/sec.
- Peak QPS: 2 * Average QPS = 800 pages/sec.
- Storage (1 month): 1 billion pages * 500 KB average size = 500 TB/month.
- Storage (5 years): 500 TB * 12 months * 5 years = 30 PB required for total content retention.


### 🔴 Senior Level

#### 1. How do you perform a back-of-the-envelope estimation for large-scale object storage capacity and IOPS?
**Answer:**
Object storage bottlenecks usually occur in disk capacity or IOPS. Assume an object distribution (e.g., 20% small <1MB, 60% medium 1-64MB, 20% large >64MB) and use median sizes (0.5MB, 32MB, 200MB) to calculate total storage needs given a storage usage ratio. For IOPS, estimate standard hard disk limits (e.g., a 7200 rpm SATA drive yields roughly 100-150 random seeks/second). Metadata sizing must also be factored in (e.g., ~1KB per object metadata).

#### 2. Provide a back-of-the-envelope estimation for a distributed email service with 1 billion users.
**Answer:**
- Email sending QPS: 10^9 users * 10 emails/day / 10^5 seconds = 100,000 QPS.
- Metadata storage (1 year): 1 billion users * 40 emails/day * 365 days * 50 KB = 730 PB.
- Attachment storage (1 year): 1 billion users * 40 emails/day * 365 days * 20% attachment rate * 500 KB = 1,460 PB.
- Conclusion: The massive scale necessitates a horizontally scalable distributed database and object storage tier.

#### 3. Provide a back-of-the-envelope estimation for a nearby friends feature.
**Answer:**
- Scale: 100 million DAU, 10% concurrent users (10 million).
- Frequency: Location updates reported every 30 seconds (accounting for human walking speeds of 3-4 mph).
- Location update QPS: 10 million concurrent users / 30 seconds = ~334,000 QPS.
- User connections: Average user has 400 friends, all assumed to utilize the feature.

#### 4. Provide a back-of-the-envelope estimation for a stock exchange system.
**Answer:**
- Scale: 100 symbols, 1 billion orders per day.
- Trading window: NYSE is open 6.5 hours per day (9:30 AM to 4:00 PM EST).
- Average QPS: 1,000,000,000 / (6.5 * 3600) = ~43,000 QPS.
- Peak QPS: 5 * Average QPS = 215,000 QPS (spiking heavily at market open and close).


## 📂 Category: Chat Systems (3 cards)

### 🟡 Mid Level

#### 1. Describe the end-to-end 1-on-1 chat flow in a real-time messaging architecture.
**Answer:**
1. User A sends a message to Chat Server 1.
2. Chat Server 1 obtains a unique message ID from the distributed ID generator.
3. Chat Server 1 pushes the message into the message sync queue.
4. The message is persisted to the key-value store.
5.a. If User B is online, the message is forwarded to Chat Server 2 where User B maintains a persistent WebSocket connection.
5.b. If User B is offline, a push notification is dispatched via push notification (PN) servers.

#### 2. Describe the high-level architecture and component responsibilities of a real-time chat application.
**Answer:**
Chat servers handle real-time message ingestion and routing. Presence servers track and manage user online/offline status using persistent connections (e.g., WebSockets). API servers handle standard HTTP requests like user login, signup, and profile updates. Notification servers dispatch push alerts to offline users. A distributed key-value store persists chat history so users can sync missed messages upon reconnecting.

#### 3. Describe the message sync flow and architecture for small group chats.
**Answer:**
For small group chats (e.g., WeChat limiting groups to 500 members), when a user sends a message, it is copied to each group member’s individual message sync queue (inbox). This simplifies the sync flow because clients only need to check their own inbox for new messages, and storing copies is inexpensive at small scales.


## 📂 Category: Cloud & Serverless (1 cards)

### 🟢 Junior Level

#### 1. What are the advantages of using serverless architectures (like AWS Lambda) in game leaderboards?
**Answer:**
Serverless functions automatically scale up and down based on incoming traffic volume (such as score submissions and leaderboard retrievals), eliminating the need for infrastructure management, capacity planning, and environment maintenance.


## 📂 Category: Cloud & Storage (1 cards)

### 🟢 Junior Level

#### 1. What is Amazon S3 and how does it ensure high availability?
**Answer:**
Amazon Simple Storage Service (Amazon S3) is an object storage service offering scalability, data availability, security, and performance. S3 supports same-region and cross-region replication. Redundant files are stored across multiple geographic regions and organized into containers called buckets.


## 📂 Category: Cloud Architecture (1 cards)

### 🟡 Mid Level

#### 1. Explain serverless architecture
**Answer:**
A cloud-native execution model where developers write code (functions) managed entirely by a cloud provider (e.g., AWS Lambda). The platform automatically provisions, scales, and de-provisions infrastructure based on demand, charging only for active execution time.


## 📂 Category: Cloud Architecture & Serverless (1 cards)

### 🟡 Mid Level

#### 1. How can serverless cloud infrastructure (API Gateway and AWS Lambda) be orchestrated to host a scalable game leaderboard?
**Answer:**
Route HTTP requests through Amazon API Gateway endpoints (e.g., `GET /v1/scores`, `POST /v1/scores`) which trigger stateless AWS Lambda functions. These functions execute Redis commands (like `ZINCRBY`) or query backing MySQL instances on-demand. This serverless approach eliminates manual server provisioning, handles auto-scaling based on DAU growth, and supports native multi-cloud equivalents.


## 📂 Category: Cloud Computing (1 cards)

### 🟢 Junior Level

#### 1. What is the typical availability SLA (Service Level Agreement) set by major cloud providers?
**Answer:**
Cloud providers typically set their baseline SLAs at 99.9% availability or above (often reaching 'four nines' 99.99% or 'five nines' 99.999% for mission-critical core storage and networking services).


## 📂 Category: Cloud Storage (5 cards)

### 🟢 Junior Level

#### 1. What constitutes an Amazon S3 object?
**Answer:**
An S3 object is an individual piece of data stored within a bucket, consisting of object data (the payload, which can be any sequence of bytes) and metadata (a set of name-value pairs describing the object).

#### 2. What is Amazon S3 versioning and object storage features?
**Answer:**
Amazon S3 is a RESTful object storage service. S3 versioning is a bucket-level feature that keeps multiple variants of an object, enabling users to recover data that is deleted or overwritten by accident.

#### 3. What is an Amazon S3 bucket?
**Answer:**
An Amazon S3 bucket is a globally unique logical container used to store objects in object storage. Creating a bucket is a prerequisite for uploading data to S3.

#### 4. What is an S3 Service Level Agreement (SLA)?
**Answer:**
A contract between AWS and a client defining performance guarantees. For example, Amazon S3 Standard-Infrequent Access is designed for 99.999999999% durability across multiple Availability Zones, resilience against an entire AZ failure, and 99.9% availability.

#### 5. What is an S3 URI?
**Answer:**
An S3 URI is a Uniform Resource Identifier that uniquely identifies resources (buckets and objects) within object storage, which exposes RESTful APIs to access them.


## 📂 Category: Cloud Storage & Architecture (1 cards)

### 🟡 Mid Level

#### 1. What are block servers and how do they interact with cloud storage in file synchronization systems?
**Answer:**
Block servers divide large files into fixed-size blocks (e.g., maximum 4MB like Dropbox), compute a unique hash for each block, and upload them to object storage (like AWS S3). The blocks are treated as independent immutable objects, tracked via metadata, and reassembled on demand.


## 📂 Category: Cloud Storage & File Systems (1 cards)

### 🟡 Mid Level

#### 1. What are the core requirements and scoping questions to ask when designing Google Drive?
**Answer:**
Key scoping questions include:
- Features: Upload/download, file sync, and notifications.
- Clients: Mobile and web apps.
- File formats: Any file type supported.
- Security: Files in storage must be encrypted.
- Limits: File size limit of 10 GB or smaller.
- Scale: 10M Daily Active Users (DAU).


## 📂 Category: Communication Protocols (3 cards)

### 🟢 Junior Level

#### 1. What are the core email protocols and their primary use cases?
**Answer:**
SMTP (Simple Mail Transfer Protocol): Standard protocol for sending emails from one mail server to another. POP (Post Office Protocol): Receives and downloads emails from a remote server to a local client, deleting them from the server upon download (accessible on only one device). IMAP (Internet Mail Access Protocol): Retrieves emails while keeping them on the server, allowing synchronization across multiple devices; only downloads headers initially until an email is opened. HTTPS: Frequently used for web-based email access and mobile synchronization (e.g., Microsoft ActiveSync).


### 🟡 Mid Level

#### 1. What API protocols are typically used in email architectures?
**Answer:**
1. SMTP/POP/IMAP APIs for native mobile and desktop clients.
2. SMTP communications between sender and receiver mail servers.
3. RESTful APIs over HTTP for full-featured and interactive web-based email applications.

#### 2. What are the benefits of WebSocket in system design?
**Answer:**
WebSocket is bidirectional, meaning it can be used for both sending and receiving data, simplifying design and making implementation on both client and server more straightforward. Since connections are persistent, efficient connection management on the server-side is critical.


## 📂 Category: Computer Architecture (1 cards)

### 🟢 Junior Level

#### 1. In terms of computer operations, is memory faster or slower than disk?
**Answer:**
Memory (RAM) is significantly faster than disk storage.


## 📂 Category: Concurrency & Distributed Ordering (2 cards)

### 🟡 Mid Level

#### 1. How does Bitcask manage concurrency control for reads and writes?
**Answer:**
Bitcask uses a single writer thread to ensure strict sequential append-order for writes. Data file segments are append-only and immutable, allowing multiple threads to execute read operations concurrently without locks.


### 🔴 Senior Level

#### 1. How does a high-throughput sequencer operate using memory-mapped (MMap) files and ring buffers?
**Answer:**
A single-writer sequencer pulls events from local component ring buffers to prevent lock contention, stamps each event with a sequential ID, and appends them to a single event store. Backup sequencers can be maintained for high availability.


## 📂 Category: Concurrency & Rate Limiting (2 cards)

### 🟡 Mid Level

#### 1. How do race conditions occur in a rate limiter using Redis?
**Answer:**
In a high concurrency environment, race conditions happen when multiple threads concurrently read the same counter value from Redis (e.g., 3), check that (counter + 1) does not exceed the threshold, and independently increment and write back 4 without accounting for the other threads. Both requests believe the new value is 4 when it should be 5.

#### 2. How do sliding window log and fixed window counter algorithms compare for rate limiting?
**Answer:**
The fixed window counter algorithm suffers from allowing burst traffic at the edges of a window (e.g., double the limit if requests cluster at the boundary). The sliding window log algorithm fixes this by keeping track of exact request timestamps in a cache (such as Redis sorted sets), purging timestamps older than the current window duration, adding the new timestamp, and checking if the log size stays within the allowed limit.


## 📂 Category: Concurrency & Transactions (3 cards)

### 🟡 Mid Level

#### 1. What are common concurrency issues in a hotel reservation system?
**Answer:**
Common concurrency issues include: 1) The same user accidentally or intentionally clicking the 'book' button multiple times. 2) Multiple distinct users attempting to book the exact same room at the exact same time, leading to potential double-booking if not properly isolated via transactions or distributed locks.

#### 2. What are the pros and cons of optimistic locking in a hotel reservation system?
**Answer:**
Pros:
- Prevents applications from editing stale data via version numbers.
- Avoids database-level locking overhead; entirely managed at the application layer.
- Highly performant under low data contention where conflicts are rare.
Cons:
- Poor performance when data contention is heavy due to transaction retries.
- Highly suitable for hotel reservations since QPS for bookings is typically low.

#### 3. What are the pros and cons of pessimistic locking in a hotel reservation system?
**Answer:**
Pros:
- Prevents applications from updating modified data by serializing updates; useful for heavy data contention.
- Easy to implement logically.
Cons:
- Risk of deadlocks when locking multiple resources, making deadlock-free code difficult to write.
- Poor scalability: long-lived locks block concurrent transactions and heavily degrade database performance. Therefore, it is generally not recommended for reservation systems.


## 📂 Category: Content Delivery & Media Systems (1 cards)

### 🔴 Senior Level

#### 1. How do we optimize and reduce the cost of serving videos from a CDN?
**Answer:**
Leverage the long-tail distribution of video viewership by: 1) Serving only popular videos from CDNs while offloading long-tail content to high-capacity origin servers. 2) Encoding short or unpopular videos on-demand rather than pre-generating all formats. 3) Restricting regional distribution based on local popularity. 4) Partnering directly with Internet Service Providers (ISPs) to deploy edge caches closer to end-users.


## 📂 Category: Core Infrastructure (1 cards)

### 🟢 Junior Level

#### 1. What core requirements and encoding parameters govern the design of a hyper-scale URL shortener?
**Answer:**
1. Functionality: Transforms a long original URL into a short, unique alias that redirects users upon access.
2. Scale: 100 million URLs generated per day.
3. Encoding Constraints: Shortened keys must be as compact as possible using alphanumeric characters (0-9, a-z, A-Z).
4. Lifecycle: Shortened URLs are immutable (no deletion or updating required for baseline design).


## 📂 Category: Cryptography & Hashing (1 cards)

### 🟢 Junior Level

#### 1. What is the output range of the SHA-1 hash function?
**Answer:**
0 to 2^160 - 1 (yielding a 160-bit hash value).


## 📂 Category: Data Analytics & Metrics (1 cards)

### 🟢 Junior Level

#### 1. What are the key metrics used in digital advertising?
**Answer:**
The key metrics used in online advertising, including click-through rate (CTR) and conversion rate (CVR), depend on aggregated ad click data.


## 📂 Category: Data Architecture (1 cards)

### 🔴 Senior Level

#### 1. What are the design characteristics and quirks of RDF (Resource Description Framework)?
**Answer:**
RDF is designed for internet-wide data exchange. Its triples (subject, predicate, object) often use URIs for predicates (e.g., http://schema.org/birthDate) rather than simple strings like LIVES_IN. This prevents conflicts when combining datasets from different entities that might attach different meanings to common words.


## 📂 Category: Data Architecture & Patterns (1 cards)

### 🔴 Senior Level

#### 1. What foundational requirement must a state machine satisfy to implement Event Sourcing?
**Answer:**
The behavior of the state machine must be completely deterministic. It must not contain randomness, perform external I/O during state application, or rely on random numbers, ensuring that applying the same event to a given state always yields the exact same result.


## 📂 Category: Data Engineering (17 cards)

### 🟢 Junior Level

#### 1. Are simple compression algorithms fast or slow?
**Answer:**
Simple compression algorithms are generally fast.

#### 2. What is serialization (encoding) and deserialization?
**Answer:**
The translation process from an in-memory data structure representation to a byte sequence (known as encoding, serialization, or marshalling). The reverse translation from a byte sequence back to an in-memory structure is called decoding, parsing, deserialization, or unmarshalling.

#### 3. Where are graphical data analysis operations like drill-down, slicing, and dicing typically utilized?
**Answer:**
They are used in graphical data analysis tools that automatically generate SQL queries, visualize analytical results, and allow data analysts to explore multi-dimensional datasets.

#### 4. Where does the term 'star schema' originate in data warehousing?
**Answer:**
It comes from the visual representation of table relationships where the central fact table is surrounded by its dimension tables, with connections resembling the radiating rays of a star.


### 🟡 Mid Level

#### 1. How do we implement URL prioritization in a large-scale web crawler?
**Answer:**
Measure URL usefulness using PageRank, update frequency, and site traffic via a 'Prioritizer' component. Feed prioritized URLs into multiple queues (f1 to fn) assigned different priority levels, and use a queue selector that probabilistically favors higher-priority queues.

#### 2. How is financial market data typically persisted across real-time and historical states?
**Answer:**
Market data is usually persisted in an in-memory columnar database (such as KDB) to support real-time analytics. After the market closes, the data is typically migrated and persisted into a historical long-term database.

#### 3. What are examples of OLAP (Online Analytical Processing) databases and data warehouse systems?
**Answer:**
Commercial data warehouses include Teradata, Vertica, SAP HANA, ParAccel, and Amazon Redshift (hosted ParAccel). Open-source SQL-on-Hadoop engines include Apache Hive, Spark SQL, Cloudera Impala, Facebook Presto, Apache Tajo, and Apache Drill (many inspired by Google Dremel).

#### 4. What are the primary disadvantages of using MapReduce for data processing?
**Answer:**
1. Usability: Developers must write and coordinate complex low-level procedural mapping/reducing functions rather than utilizing a declarative query.
2. Lack of optimization hooks: Procedural code prevents database query optimizers from analyzing and automatically rewriting queries for better execution performance.

#### 5. What is a data warehouse?
**Answer:**
A dedicated, separate analytical database system introduced in the late 1980s/early 1990s to run heavy OLAP (Online Analytical Processing) queries, decoupling resource-heavy analytics workloads from transactional OLTP (Online Transaction Processing) databases.

#### 6. What is schema evolution in data serialization?
**Answer:**
The ability to modify a data schema over time (e.g., adding, removing, or changing fields) without breaking backward or forward compatibility with older and newer versions of the data format or consumers.

#### 7. What is the advantage of using a separate data warehouse over querying OLTP systems directly?
**Answer:**
Data warehouses are optimized for heavy analytical workloads (OLAP) and complex scan patterns, avoiding the performance degradation that would occur if analytics queries ran directly against row-oriented, index-optimized OLTP databases.

#### 8. Why are the boundaries between data systems (like datastores and message queues) becoming blurred in modern architectures?
**Answer:**
Many modern tools are optimized for a variety of use cases. For example, datastores like Redis are used as message queues, and message queues like Apache Kafka provide database-like durability guarantees. Additionally, applications have increasingly demanding requirements that a single tool can no longer fulfill, requiring developers to stitch multiple specialized tools together via application code.


### 🔴 Senior Level

#### 1. Compare storing raw data versus aggregated data for event aggregators (e.g., ad clicks).
**Answer:**
Raw Data Only: Provides full dataset, supports flexible filtering/recalculation, but incurs huge storage costs and slow query speeds. Aggregated Data Only: Smaller dataset and fast queries, but causes permanent data loss through lossy compression. Best Practice: Store both. Raw data serves as immutable cold-storage backup and source for reprocessing after bug fixes, while aggregated data acts as active hot storage optimized for fast query performance.

#### 2. How do we perform historical data replay or recalculation in an ad click aggregator?
**Answer:**
The recalculation service runs a batched job pulling raw data from storage and routes it to a dedicated aggregation service to avoid impacting real-time processing. The aggregated results are sent to a message queue and updated in the aggregation database.

#### 3. What architectural pattern is an ad click event aggregator, and what technologies are typically used?
**Answer:**
It is a typical big data processing system. Industry-standard solutions include Apache Kafka, Apache Flink, and Apache Spark.

#### 4. What are viable alternatives to Kafka for high-throughput time-series data ingestion?
**Answer:**
Maintaining a production-scale Kafka cluster is operationally complex. Alternatives include bypassing intermediate queues entirely by writing directly to specialized in-memory time-series databases. For example, Facebook's Gorilla is designed to remain highly available for writes even during partial network failures, offering reliability comparable to an intermediate queue.

#### 5. What is a data cube (OLAP cube)?
**Answer:**
A data cube is a multi-dimensional materialized view used in OLAP systems, structured as a grid of aggregates grouped by various dimensions (e.g., date and product). It pre-computes sums, averages, or other metrics across different dimensional intersections to drastically speed up analytical queries.


## 📂 Category: Data Engineering & Logging (1 cards)

### 🟢 Junior Level

#### 1. What are analytics logs in the context of a search autocomplete service?
**Answer:**
Raw, append-only logs that record user search queries without immediate indexing.


## 📂 Category: Data Engineering & Streaming (3 cards)

### 🟡 Mid Level

#### 1. Explain the concept of CDC (Change Data Capture)
**Answer:**
Change Data Capture (CDC) is a design pattern used to track and capture row-level changes (inserts, updates, deletes) made to a database table. Instead of querying tables periodically, CDC typically tails the database transaction log (e.g., PostgreSQL WAL or MySQL binlog) and streams these changes in real-time to downstream systems like search engines, caches, or message brokers.

#### 2. Why is there often a gap in timestamps during ad click event aggregation?
**Answer:**
There is a distinction between Event Time (when the click happens) and Processing Time (system time when the aggregation server processes it). Network delays and asynchronous processing via message queues can introduce massive gaps, such as events arriving hours late.


### 🔴 Senior Level

#### 1. Why use an intermediate message queue (like Kafka) before writing aggregated stream results to a database?
**Answer:**
An intermediate message queue is necessary to decouple processing steps and achieve end-to-end exactly-once semantics via atomic commits.


## 📂 Category: Data Fundamentals (1 cards)

### 🟢 Junior Level

#### 1. How many bytes does a standard ASCII character occupy in memory?
**Answer:**
An ASCII character uses exactly one byte of memory.


## 📂 Category: Data Management & Storage (1 cards)

### 🟡 Mid Level

#### 1. What are the key considerations for data backup strategies?
**Answer:**
1. Recovery Time Objective (RTO)
2. Recovery Point Objective (RPO)
3. Backup Frequency
4. Storage Cost
5. Data Retention Policy


## 📂 Category: Data Modeling (16 cards)

### 🟢 Junior Level

#### 1. What are the advantages of letting users choose from a drop-down list or autocompleter instead of free-form text?
**Answer:**
Benefits include consistent formatting and spelling, avoiding ambiguity, centralized update management, robust localization support, and enhanced search capabilities (e.g., implicitly mapping cities to states or regions).

#### 2. What are the core queries of a hotel reservation system?
**Answer:**
1. View detailed information about a hotel.
2. Find available types of rooms given a specific date range.
3. Record a new reservation.
4. Look up an existing reservation or past reservation history.

#### 3. What is the evolution of the data model for a URL shortener system?
**Answer:**
Initial high-level designs often use an in-memory hash table, which is non-feasible for production due to limited and expensive RAM. A scalable production approach uses a relational database containing a simplified mapping table with at least 3 columns: id, shortURL, and longURL.


### 🟡 Mid Level

#### 1. Can you query graph data using SQL if it is stored in a relational structure?
**Answer:**
Yes, but with difficulty. Relational databases usually require knowing the required joins in advance, whereas graph queries often require traversing a variable number of edges (an unknown number of joins in advance) to find the target vertex.

#### 2. How are candlestick charts and order books modeled in a high-frequency market data processor?
**Answer:**
Market data processors use Candlestick and CandlestickChart classes. A Candlestick stores openPrice, closePrice, highPrice, lowPrice, volume, timestamp, and interval. A CandlestickChart maintains a LinkedList of Candlestick instances. When an interval elapses, a new Candlestick is instantiated for the next interval and appended to the linked list.

#### 3. How does schema-on-read compare to schema-on-write?
**Answer:**
Schema-on-read delays data structure validation until the data is queried or read, acting similarly to dynamic type checking in programming languages. Schema-on-write enforces validation rigidly upfront when data is written to storage, comparable to static (compile-time) type checking.

#### 4. How would you model and query advanced entities (such as organizations, schools, and recommendations) when using a document-oriented database for résumés?
**Answer:**
The core résumé data can be grouped into one document, but references to entities like organizations, schools, and other users need to be represented as explicit references, requiring joins or secondary lookups when queried.

#### 5. What are edge properties in graph databases?
**Answer:**
Edge properties are key-value pairs associated with the relationships between vertices in a graph database, storing metadata about the connection such as weight, timestamp, or relationship type.

#### 6. What are the access and reliability characteristics of email metadata and operational data?
**Answer:**
Email headers are small and frequently accessed; email bodies vary in size and are infrequently accessed (usually read once). Operations are isolated per user. Data recency impacts usage (82% of reads are for data < 16 days old). Reliability requirements are extremely high (zero data loss acceptable).

#### 7. What are the core queries required for an email service's data layer?
**Answer:**
1. Get all folders for a user.
2. Display all emails for a specific folder.
3. Create, delete, or retrieve a specific email.
4. Fetch all read or unread emails.
5. Bonus: Get conversation threads.

#### 8. What are the main limitations of the document data model?
**Answer:**
Document models offer poor support for complex many-to-many relationships and make deep nested querying cumbersome (e.g., referencing deeply nested array items). While denormalization or application-level joins can mitigate this, they shift complexity to the application code and can degrade performance.

#### 9. What is the importance of data models in software development?
**Answer:**
Data models heavily impact both how software is written and how we conceptualize the problem being solved. Most applications are built by layering data models, where each layer's primary question is how it is represented in terms of the next-lower layer.

#### 10. What is the semantic web?
**Answer:**
An initiative where websites publish machine-readable data alongside human-readable text and pictures. Using the Resource Description Framework (RDF), different websites can publish data in a consistent format, allowing automated combination into an internet-wide 'database of everything.'

#### 11. Why are graph databases advantageous for application evolvability?
**Answer:**
Graphs easily accommodate schema and structural changes without massive migrations. For example, adding new entities (like food allergens) and relationships (allergies, food ingredients) can be done by introducing new vertices and edges. Queries can then dynamically traverse these relationships, making graphs highly adaptable to changing data structures.


### 🔴 Senior Level

#### 1. How was data accessed and queried in the historical network (CODASYL) model?
**Answer:**
Data was accessed by moving a cursor through the database, iterating over lists of records and following specific access paths similar to traversing a linked list. If a record had multiple parents, application code had to manually track all incoming pointers and relationships, making queries complex like navigating an n-dimensional data space.

#### 2. What is the Datalog data model?
**Answer:**
Datalog's data model generalizes the triple-store model. Instead of representing data as a triple format like (subject, predicate, object), it expresses facts as relational predicates in the form of `predicate(subject, object)`.


## 📂 Category: Data Modeling & Storage (1 cards)

### 🔴 Senior Level

#### 1. How do we reliably reproduce past states in a wallet service using event sourcing?
**Answer:**
Instead of overwriting mutable state (account balances) in place, store all state changes as an immutable sequence of historical events. The database acts as a read model, and past balances can be deterministically reconstructed at any point in time by replaying the immutable event log from the beginning.


## 📂 Category: Data Partitioning (1 cards)

### 🟡 Mid Level

#### 1. What do 'k' and 'n' represent in data distribution formulas like 'k/n'?
**Answer:**
'k' represents the number of keys, and 'n' represents the number of slots or partitions.


## 📂 Category: Data Partitioning & Scaling (1 cards)

### 🔴 Senior Level

#### 1. How do you mitigate data hotspots in a high-throughput ad click event aggregator?
**Answer:**
Hotspots occur when specific partitions (partitioned by ad_id) receive disproportionate event volumes due to large ad budgets. Mitigation strategies include: 1) Resource Manager scaling: When a node exceeds capacity (e.g., >100 events), the resource manager dynamically allocates more nodes, splitting the event group, processing them across nodes, and writing results back to the original aggregate node. 2) Advanced strategies such as Global-Local Aggregation or Split Distinct Aggregation.


## 📂 Category: Data Pipelines & Fault Tolerance (1 cards)

### 🔴 Senior Level

#### 1. What are the most common root causes for data duplication in distributed event streaming and aggregation pipelines?
**Answer:**
1. Client-side duplication: Clients resending events due to retries or timeouts. 2. Server outages: An aggregation node crashes after sending data downstream but before committing its consumer offset (e.g., in Kafka), causing a failover node to re-consume and re-process the already handled message range.


## 📂 Category: Data Processing (3 cards)

### 🟡 Mid Level

#### 1. What are the core differences between Lambda and Kappa architectures?
**Answer:**
Lambda architecture utilizes two separate processing paths (batch and streaming) simultaneously, requiring two codebases to be maintained. Kappa architecture solves this by combining batch and streaming into a single stream processing engine, handling both real-time data processing and continuous historical data reprocessing through that single path.

#### 2. What are the main use cases of MapReduce in an ad click event aggregator?
**Answer:**
1. Aggregate the number of clicks per ad ID within the last M minutes.
2. Return the top N most clicked ad IDs in the last M minutes.
3. Data filtering.


### 🔴 Senior Level

#### 1. Describe the data model and aggregation structure for an ad click event aggregator.
**Answer:**
Raw ad click logs contain [AdClickEvent] fields: ad_id, click_timestamp, user_ip, and country. For aggregation, records are grouped by ad_id and click_minute (with optional filter_id fields for region, IP, or user_id). To support rapid queries for the top N most clicked ads in the last M minutes, systems maintain a rollup structure containing: window_size (M in minutes), update_time_minute (timestamp at 1-minute granularity), and most_clicked_ads (an array list of top ad IDs in JSON format).


## 📂 Category: Data Processing & Analytics (2 cards)

### 🔴 Senior Level

#### 1. How do you perform data reconciliation in an ad click aggregation service without a third-party source of truth?
**Answer:**
Reconciliation is performed by executing a batch job at the end of the day to sort raw ad click events by event time within every partition, then comparing this batch output against real-time aggregation results. For stricter accuracy, smaller windows (e.g., 1-hour intervals) can be used. Discrepancies are expected due to late-arriving events.

#### 2. How do you support multi-dimensional data filtering (e.g., country-specific metrics) in MapReduce or data warehouse aggregations?
**Answer:**
Use a star schema approach where filtering criteria (dimensions) are pre-defined during aggregation (e.g., grouping clicks by ad_id, minute, and country like USA, GBP, others). Benefits include simplicity, reuse of existing aggregation services, and fast analytical reads via pre-calculated results. Limitations include a combinatorial explosion of buckets and records if filtering dimensions grow too large.


## 📂 Category: Data Processing & Pipelines (1 cards)

### 🟡 Mid Level

#### 1. What is a map node and why is it used in data pipelines?
**Answer:**
A Map node reads data from a data source, and then filters and transforms the data (e.g., routing ads with ad_id % 2 = 0 to node 1). It is used because input data often needs cleaning or normalization before processing, or when direct Kafka partition control is unavailable and events with the same key might land in different partitions.


## 📂 Category: Data Serialization (7 cards)

### 🟢 Junior Level

#### 1. What are the most common data encoding formats?
**Answer:**
Standardized text-based encodings include JSON (widely supported due to browser/JavaScript integration, simpler than XML) and XML (verbose, complex). CSV is another popular language-independent format, though less powerful for nested data.

#### 2. What is the difference between binary and text-based serialization formats?
**Answer:**
Binary formats (like Protocol Buffers) are compact and optimized for processing speed and network bandwidth, while text formats (like JSON) are human-readable and easier to debug.


### 🟡 Mid Level

#### 1. How does Protocol Buffers encode data and optional/required fields?
**Answer:**
Protocol Buffers uses a single binary encoding format that performs bit packing (similar to Thrift's CompactProtocol). Fields are marked as required or optional, but this status does not affect the binary wire format itself. Instead, 'required' enforces a runtime check that throws an error if the field is unset, aiding in bug detection.

#### 2. What are the key components of a serialization framework?
**Answer:**
1. Schema Definition Language
2. Code Generation Tools
3. Serialization/Deserialization Runtime
4. Language Support Libraries

#### 3. What are the limitations of number encoding in formats like JSON?
**Answer:**
JSON does not distinguish between integers and floating-point numbers and lacks a precision specifier. Integers greater than 2^53 (e.g., Twitter IDs) lose precision in IEEE 754 double-precision floats used by languages like JavaScript, requiring strings as workarounds.

#### 4. What are the trade-offs of using binary encodings like MessagePack compared to textual JSON?
**Answer:**
Binary encodings (like MessagePack) offer marginal space reductions (e.g., 66 bytes vs 81 bytes for JSON) and potentially minor parsing speedups, but they result in a complete loss of human-readability. Such small space savings rarely justify abandoning human-readable formats unless operating at massive network scale where bandwidth is severely constrained.

#### 5. What is the primary advantage of using Protocol Buffers over JSON?
**Answer:**
Protocol Buffers offer significantly better network performance, faster serialization/deserialization speeds, and smaller message sizes through binary encoding, while strictly enforcing strong typing and enabling backward/forward schema evolution.


## 📂 Category: Data Serialization & Encoding (4 cards)

### 🟢 Junior Level

#### 1. How do in-memory data representations differ from data structures used for network transmission or file storage?
**Answer:**
In-memory data uses objects, structs, arrays, and pointers optimized for CPU access and manipulation. When persisted or sent over a network, data must be encoded into a self-contained, language-agnostic byte sequence (such as JSON) because pointers are meaningless to external processes.

#### 2. What are language-specific serialization formats and their common use cases?
**Answer:**
Built-in encoding formats that convert in-memory objects into byte sequences. Examples include Java's `java.io.Serializable`, Ruby's `Marshal`, Python's `pickle`, and third-party libraries like Kryo for Java. They allow fast save/restore operations with minimal code, though usually tightly coupled to specific languages.


### 🟡 Mid Level

#### 1. What are the common encoding issues and limitations found in JSON, XML, and CSV formats?
**Answer:**
- Numbers vs Strings: XML/CSV cannot distinguish numbers from numeric strings without schemas; JSON lacks integer vs. float differentiation and precision specs.
- Binary Data: Lack native binary string support, requiring Base64 encoding which inflates data size by 33%.
- Schemas: XML schemas are complex; JSON schemas are often ignored; CSV lacks schemas entirely, requiring manual structural parsing.

#### 2. What are the primary disadvantages of language-specific serialization formats?
**Answer:**
They tie data encoding to a specific programming language, complicating cross-language integration. Decoding often requires instantiating arbitrary classes, posing severe remote code execution security risks. They frequently neglect forward/backward compatibility versioning and suffer from poor CPU and payload efficiency.


## 📂 Category: Data Serialization & Modeling (2 cards)

### 🟢 Junior Level

#### 1. How do RDF and Turtle/N3 formats compare?
**Answer:**
Turtle/N3 is a human-readable text format for RDF data, preferable over the much more verbose XML serialization of RDF. Tools like Apache Jena can automatically convert between different RDF formats.

#### 2. How do Thrift and Protocol Buffers simplify serialization?
**Answer:**
Thrift and Protocol Buffers use custom schema definition files and accompanying code generation tools to automatically produce classes in multiple programming languages, allowing applications to easily encode and decode structured binary records.


## 📂 Category: Data Serialization & Network Protocols (1 cards)

### 🟢 Junior Level

#### 1. What binary serialization formats can replace textual JSON and XML to reduce storage and bandwidth requirements?
**Answer:**
Binary encodings for JSON (such as MessagePack, BSON, UBJSON, and Smile) and XML (such as WBXML and Fast Infoset) significantly reduce payload size compared to their verbose textual counterparts.


## 📂 Category: Data Stores & Caching (2 cards)

### 🟡 Mid Level

#### 1. How do we fetch the top 10 players and the relative position of a user in a leaderboard using Redis?
**Answer:**
To fetch the top 10 players, use ZREVRANGE in descending order with the 'WITHSCORES' attribute: `ZREVRANGE leaderboard_feb_2021 0 9 WITHSCORES`. To fetch the relative position of a user, use ZREVRANGE with the range calculated around the player's rank (e.g., `ZREVRANGE leaderboard_feb_2021 357 365`).


### 🔴 Senior Level

#### 1. How do we implement a self-managed leaderboard with efficient user metadata retrieval and tie-breaking?
**Answer:**
Create a monthly sorted set (ZSET) for scores. Store user profile details in a MySQL database and cache them (or use a Redis Hash for mapping user IDs to user objects and timestamps). For tie-breaking, store a map of user ID to the timestamp of the most recently won game when incrementing scores; the user with the older timestamp ranks higher in a tie.


## 📂 Category: Data Streaming & Ingestion (1 cards)

### 🟡 Mid Level

#### 1. How is user location data ingested and processed in location-based services like Google Maps?
**Answer:**
Clients periodically send location updates (latitude, longitude, timestamp via HTTP Keep-Alive). To reduce network and write load, updates can be buffered on the client and sent in batches. The server writes high-volume updates to a scalable database like Cassandra and simultaneously pushes them to a high-throughput message streaming platform like Kafka. Downstream services consume the Kafka stream for live traffic updates, routing tile processing, and ETA calculations.


## 📂 Category: Data Structures (5 cards)

### 🟢 Junior Level

#### 1. What are classic examples of real-world data modeled as graphs?
**Answer:**
1. Social graphs (vertices: people, edges: relationships/connections). 2. The web graph (vertices: web pages, edges: HTML hyperlinks). 3. Road or rail networks (vertices: junctions, edges: roads or railway tracks).

#### 2. What is a sorted set data structure?
**Answer:**
A collection data type where each unique member is associated with a floating-point score. Members must be unique, but scores can repeat. Elements are automatically ordered and ranked by their scores in ascending order.


### 🟡 Mid Level

#### 1. How do we avoid and resolve hash collisions in URL shorteners while optimizing performance?
**Answer:**
Taking the first 7 characters of a hash can cause collisions; resolve this by recursively appending a predefined string until unique. To avoid expensive database lookups for every check, use a Bloom filter—a space-efficient probabilistic data structure—to test membership before querying the database.

#### 2. How do we optimize search and traversal performance in a skip list?
**Answer:**
Enhance a base sorted singly-linked list (which has O(n) search time) by building multi-level indexes. Add a level 1 index skipping every other node, and subsequent higher levels that skip every other node of the previous level, terminating when the distance reaches n/2 - 1, resembling binary search behavior to achieve O(log n) performance.

#### 3. What data structure is ideal for implementing leaderboards, and how does it work internally?
**Answer:**
Sorted sets are ideal for leaderboards. Internally, a sorted set is typically implemented using two data structures: a hash table and a skip list. The hash table maps users to scores (O(1) lookup), and the skip list maps scores to users, maintaining items sorted by score in descending order.


## 📂 Category: Data Structures & Algorithms (6 cards)

### 🟢 Junior Level

#### 1. How can data be maintained in a sorted order when incoming writes occur in arbitrary order?
**Answer:**
While disk-based sorted structures like B-Trees exist, maintaining sorted data in memory is often achieved using self-balancing binary search trees such as red-black trees or AVL trees, allowing insertions in any order while preserving sorted traversal.

#### 2. How do you extend an autocomplete service to support multiple languages?
**Answer:**
To support non-English queries and multiple writing systems, store Unicode characters in the trie nodes instead of standard ASCII characters.


### 🟡 Mid Level

#### 1. What is the time complexity of retrieving top-k search queries using a Trie data structure?
**Answer:**
Given prefix length p, total trie nodes n, and children count c: 1. Find prefix: O(p). 2. Traverse subtree for valid child strings: O(c). 3. Sort children to get top k: O(c log c). Total time complexity is the sum: O(p) + O(c) + O(c log c).

#### 2. Which data structure is best used to optimize data retrieval in an autocomplete system?
**Answer:**
A Trie (prefix tree). A trie is a tree-like data structure where the root represents an empty string and each node stores a character with children for possible subsequent characters. It compactly stores strings to perform efficient prefix-based retrieval, avoiding inefficient relational database queries for top search queries.


### 🔴 Senior Level

#### 1. How can you achieve O(1) time complexity for order book operations?
**Answer:**
Use a doubly-linked list for price levels where adding/matching orders at the tail/head is O(1). To achieve O(1) order cancellation without traversing the list, maintain a helper hash map (`orderMap`) that maps order IDs directly to their node pointers in the doubly-linked list.

#### 2. What are the performance requirements of an efficient order book?
**Answer:**
1. Constant lookup time O(1) for getting volume at or between price levels.
2. Fast add, cancel, and execute operations with O(1) time complexity.
3. Fast update performance for replacing orders.
4. Instant querying of the best bid/ask.
5. Efficient iteration through price levels.


## 📂 Category: Data Structures & Caching (2 cards)

### 🟡 Mid Level

#### 1. What is the impact of caching top queries and limiting prefix length in a trie?
**Answer:**
By limiting the maximum length of a prefix to a small constant (p) and caching the top-k results at the prefix node, both finding the prefix node and returning the top-k results take O(1) time complexity, resulting in an overall O(1) fetch time.

#### 2. What is the impact of caching top search queries at every node in a trie?
**Answer:**
Storing top-k frequently used queries at each node avoids traversing the whole trie and significantly reduces query retrieval time to O(1). While it requires a trade-off of additional memory space, this trades space for much faster response times.


## 📂 Category: Data Structures & Performance (1 cards)

### 🟡 Mid Level

#### 1. What is the architectural performance flaw in implementing an order book where `PriceLevel` uses a plain `List` for orders?
**Answer:**
Using a plain `List` results in $O(N)$ time complexity for deletion operations like order cancellation or matching. To achieve $O(1)$ performance, the underlying data structure for orders within a price level must be changed to a doubly-linked list.


## 📂 Category: Data Structures & Search (2 cards)

### 🟡 Mid Level

#### 1. How do trie creation, updates, and deletions work in an autocomplete service?
**Answer:**
Creation is handled by workers aggregating logs from a database. Updates can be done weekly by swapping the entire trie, or directly on nodes (though slow, requiring updates to all ancestors up to the root to maintain top queries). Deletions filter out unwanted suggestions using a filter layer in front of the Trie Cache while asynchronously purging them from the backing database for future build cycles.

#### 2. How is frequency-based sorting supported in a trie data structure?
**Answer:**
Frequency information is embedded directly inside the trie nodes alongside characters, enabling traversal algorithms to prioritize child nodes or store pre-computed top queries based on their usage metrics.


## 📂 Category: Data Structures & Spatial Indexing (1 cards)

### 🔴 Senior Level

#### 1. What is a quadtree and how is it used in spatial indexing?
**Answer:**
A quadtree is an in-memory data structure used to partition a 2D space by recursively subdividing it into four quadrants until the contents meet specific criteria (e.g., maximum number of businesses per grid). It runs on each Location-Based Service (LBS) server and is built at server start-up time, rather than acting as a persistent database solution.


## 📂 Category: Data Structures & Storage Optimization (1 cards)

### 🔴 Senior Level

#### 1. What is a Bloom filter and what problem does it solve in database storage engines?
**Answer:**
A Bloom filter is a memory-efficient probabilistic data structure used to test whether an element is a member of a set. In storage engines, it determines if a key definitely does not exist in the database, thereby eliminating unnecessary disk reads for non-existent keys.


## 📂 Category: Data Warehousing (5 cards)

### 🟢 Junior Level

#### 1. What is the structural layout of a star schema in a data warehouse?
**Answer:**
At the center is a fact table (e.g., `fact_sales`), where each row represents an atomic event occurring at a specific time (such as a customer purchasing a product, or a web page view/click). Surrounding dimension tables provide descriptive context.


### 🟡 Mid Level

#### 1. How are facts and dimensions stored in data warehouses?
**Answer:**
Facts are typically captured as individual events to maintain analytical flexibility, resulting in massive fact tables containing foreign keys to dimension tables alongside attributes (like price and cost). Dimension tables provide the context of the event (the who, what, where, when, how, and why).

#### 2. What are materialized aggregates in data warehouses?
**Answer:**
Materialized aggregates are pre-computed, cached results of heavy aggregate functions (such as COUNT, SUM, AVG) stored to bypass scanning raw data on every analytical query execution.

#### 3. What are the disadvantages of materialized data cubes?
**Answer:**
Materialized data cubes lack the flexibility of querying raw data directly because they only store pre-computed aggregates across specific dimensions (e.g., they cannot calculate metrics on un-indexed attributes like item price > $100 if price is not a dimension). Data warehouses use them primarily as read-performance boosts while retaining raw data.


### 🔴 Senior Level

#### 1. What are the downsides of column-store storage optimizations?
**Answer:**
Column-oriented storage, compression, and sorting optimize large read-only analytical queries, but they make writes significantly harder. Update-in-place approaches (like B-trees) are impossible with compressed columns; inserting a row in the middle of a sorted table requires rewriting all column files to maintain correct row positioning across columns.


## 📂 Category: Data Warehousing & Analytics (2 cards)

### 🟡 Mid Level

#### 1. What is ETL (Extract, Transform, Load)?
**Answer:**
ETL is the process used to populate a data warehouse. Data is extracted from various OLTP databases via periodic dumps or continuous streams, transformed into an analysis-friendly schema (such as a star schema), cleaned, and loaded into a read-only data warehouse to support analytical queries without impacting OLTP operations.

#### 2. What is dimensional modeling (star schema)?
**Answer:**
Dimensional modeling, often implemented as a star schema, is a data modeling technique predominantly used in data warehouses and analytics. It organizes data into fact tables (measurable, quantitative data) and dimension tables (attributes describing the facts) to optimize analytical queries.


## 📂 Category: Data Warehousing & OLAP (1 cards)

### 🟡 Mid Level

#### 1. What are the characteristic access patterns and query types of data analytics workloads?
**Answer:**
Analytic workloads (OLAP) typically require scanning huge volumes of records while reading only a few columns per record. Queries compute aggregate statistics (e.g., COUNT, SUM, AVG) rather than returning raw transactional rows, demanding columnar storage and vectorized execution engines.


## 📂 Category: Database Architecture (75 cards)

### 🟢 Junior Level

#### 1. How are database queries structured to retrieve all folders for a specific user in an email service?
**Answer:**
The query uses `user_id` as the partition key, ensuring that all folders owned by the same user are collocated within a single database partition.

#### 2. What are the core use cases for choosing NoSQL over a traditional RDBMS?
**Answer:**
Choose NoSQL when you need: 1. Horizontal scalability, 2. Schema flexibility (schema-on-read), 3. High write throughput, and 4. An eventually consistent model.

#### 3. What are the four primary categories of non-relational (NoSQL) databases?
**Answer:**
1. Key-value stores
2. Document stores
3. Column stores (Wide-column stores)
4. Graph stores

#### 4. What are the historical roots and primary use cases of relational databases?
**Answer:**
Relational databases originated from business data processing on 1960s and 1970s mainframes. Their initial primary use cases centered around online transaction processing (OLTP) such as sales, banking transactions, airline reservations, and inventory management, alongside batch processing tasks like invoicing, payroll, and reporting.

#### 5. What are the reading and writing patterns in database replication architectures?
**Answer:**
A master database typically handles write operations (inserts, updates, deletes) to maintain consistency. Slave databases receive copies of the data from the master and exclusively handle read operations. Because most applications have a higher read-to-write ratio, systems usually deploy a larger number of slave databases than master databases.

#### 6. What are the three main categories of storage systems?
**Answer:**
Block storage, File storage, and Object storage.

#### 7. What is OLAP (Online Analytical Processing)?
**Answer:**
OLAP refers to database access patterns optimized for complex data analytics, aggregations, and business intelligence reporting. Unlike transaction processing, OLAP queries typically scan large volumes of historical data to assist management and analysts in decision-making.

#### 8. What is OLTP (Online Transaction Processing)?
**Answer:**
OLTP is a database access pattern characterized by interactive applications looking up, inserting, or updating a small number of records by key using indexes. It prioritizes low latency, high concurrency, and data consistency for day-to-day operations.

#### 9. What is the difference between clustered and non-clustered indexes?
**Answer:**
A clustered index determines the physical sort order of data rows in a table and is limited to one per table. A non-clustered index is stored separately from the data table as a pointer structure, allowing multiple non-clustered indexes per table.

#### 10. What is the general topology of database replication?
**Answer:**
Database replication is typically structured with a master/slave relationship between the original master database and the slave copies.

#### 11. What is the origin and modern definition of the term 'NoSQL'?
**Answer:**
The term originated in 2009 merely as a catchy Twitter hashtag for a meetup on open-source, distributed, non-relational databases. Despite the misnomer (since it does not refer to a single specific technology), it stuck with the web startup community and has been retroactively reinterpreted to mean 'Not Only SQL'.

#### 12. What is the primary architectural solution when a single database runs out of disk space?
**Answer:**
Data sharding, which distributes datasets horizontally across multiple independent storage servers.

#### 13. What is the role of the metadata database in an email system?
**Answer:**
It stores mail metadata including mail subjects, bodies, sender information, recipient lists, and folder mappings.

#### 14. When should you choose a non-relational database over a traditional relational database?
**Answer:**
Non-relational databases might be the right choice if your application requires super-low latency, your data is completely unstructured or lacks relational structure, you only need to serialize/deserialize data (JSON, XML, YAML), or you need to store and scale massive amounts of data horizontally.

#### 15. Where did the database term 'transaction' originate?
**Answer:**
In early business data processing, a database write typically corresponded to a commercial transaction (e.g., making a sale, placing a supplier order, or paying an employee). The term persisted as databases expanded into non-monetary domains to represent any group of reads and writes forming a logical execution unit.


### 🟡 Mid Level

#### 1. How are database queries structured to display all emails for a specific folder in a messaging/email system?
**Answer:**
To store all emails for the same folder in a single partition for efficient retrieval, a composite partition key is used (e.g., incorporating user_id and folder_id). Additionally, an email_id column with a data type of TIMEUUID is used as a clustering key to sort emails chronologically.

#### 2. How are objects represented in a graph triple-store database?
**Answer:**
An object can be: 1. A primitive datatype value (string, number), where the predicate and object act as a key-value property on the subject vertex (e.g., [lucy, age, 33]). 2. Another vertex in the graph, where the predicate acts as a directed edge connecting the subject (tail vertex) to the object (head vertex) (e.g., [lucy, marriedTo, alain]).

#### 3. How are relational database queries used to implement a leaderboard?
**Answer:**
To record/increment a score: `INSERT INTO leaderboard (user_id, score) VALUES ('mary1934', 1);` or `UPDATE leaderboard SET score = score + 1 WHERE user_id = 'mary1934';`. To find a user's leaderboard position and rank: `SELECT (@rownum := @rownum + 1) AS rank, user_id, score FROM leaderboard ORDER BY score DESC;`

#### 4. How do we shard a hotel reservation database to distribute load?
**Answer:**
Shard data by hotel_id, as most queries naturally filter by it. For example, distributing 30,000 QPS across 16 shards results in 1,875 QPS per shard, which comfortably fits within a single MySQL server's capacity.

#### 5. How is the data model structured for a distributed messaging or email service?
**Answer:**
Data is partitioned using user_id as the partition key so that all data for a single user resides on a single shard or node, simplifying data locality. The table primary keys are split into two components: a Partition Key (responsible for even data distribution across nodes) and a Clustering Key (responsible for sorting data within a partition).

#### 6. What NoSQL database properties are ideal for implementing a leaderboard as an alternative to Redis?
**Answer:**
Ideal NoSQL databases should be optimized for high-frequency writes and efficiently sort items within the same partition by score. Examples include Amazon DynamoDB (using global secondary indexes for querying non-primary key attributes), Cassandra, and MongoDB.

#### 7. What are the common techniques to prevent race conditions when multiple users attempt to reserve the same resource (e.g., a room)?
**Answer:**
Locking mechanisms and concurrency controls including pessimistic locking, optimistic locking, and database constraints.

#### 8. What are the core database characteristics required for email metadata storage?
**Answer:**
An email metadata database requires strong data consistency, support for single-digit MB column sizes, designs focused on reducing disk I/O, high availability, fault tolerance, and ease of creating incremental backups.

#### 9. What are the critical architectural characteristics of the property graph model?
**Answer:**
1. Schema-less flexibility: Any vertex can connect to any other vertex via directed/undirected edges without strict schema constraints.
2. Bidirectional traversal: Given any vertex, both incoming and outgoing edges can be efficiently traversed backward and forward.
3. Multi-label support: Different edge and vertex labels allow diverse relationship types to coexist cleanly in a unified graph store.

#### 10. What are the key factors in choosing an index type?
**Answer:**
1. Query patterns (range vs exact match)
2. Write/read ratio
3. Data size and growth rate
4. Memory constraints
5. Consistency requirements

#### 11. What are the limitations of a hash table index?
**Answer:**
1) The hash table must typically fit entirely in memory; maintaining an on-disk hash map suffers from high random I/O overhead, expensive growth operations, and complex collision handling. 2) Range queries are highly inefficient because you cannot easily scan contiguous key ranges without looking up each key individually.

#### 12. What are the main arguments of document vs relational database models?
**Answer:**
The document data model favors schema flexibility, better read performance due to data locality, and closer alignment with application data structures. The relational model counters by providing robust support for joins, and structured many-to-one and many-to-many relationships.

#### 13. What database characteristics and schema designs are optimal for handling high-velocity user location telemetry in mapping systems?
**Answer:**
Requires write-heavy optimization and horizontal scalability (e.g., Apache Cassandra). A typical row schema maps user tracking telemetry: user_id (PK), timestamp, user_mode, driving_mode, and location coordinates (lat, long).

#### 14. What database optimizations can be applied to implement a leaderboard, and what are their limitations?
**Answer:**
You can add an index on the score column and use a query like: `SELECT (@rownum := @rownum + 1) AS rank, user_id, score FROM leaderboard ORDER BY score DESC LIMIT 10;`
Limitations:
1. Poor scalability: Determining arbitrary user ranks requires costly full-table or index scans.
2. Inefficient for users outside the top tier: Finding the rank of an arbitrary user further down the list is not straightforward or performant.

#### 15. What is Federation in database partitioning?
**Answer:**
Database federation (or functional partitioning) splits up databases by specific services or domains (e.g., separating user tables, product tables, and order tables into distinct database instances) rather than splitting rows of the same table.

#### 16. What is Hash Partitioning?
**Answer:**
Hash partitioning applies a cryptographic or non-cryptographic hash function (such as MurmurHash) to a partitioning key to uniformly distribute rows or records across a fixed number of database partitions or nodes, mitigating skewed data distributions.

#### 17. What is Optimistic Concurrency Control (OCC) / Optimistic Locking?
**Answer:**
OCC is a concurrency control technique where transactions execute without acquiring locks. Before committing, the system validates whether the underlying data has been modified by another transaction. If a conflict is detected, the transaction aborts and must be retried. Implementation typically relies on version numbers (preferred over timestamps due to clock drift) or hash columns checked during the update statement.

#### 18. What is Partition Pruning in database query optimization?
**Answer:**
Partition pruning is an optimization technique where the database query execution engine analyzes the WHERE clause of a query to completely skip scanning partitions that cannot possibly contain matching data, drastically reducing I/O and query latency.

#### 19. What is Pessimistic Concurrency Control (Pessimistic Locking)?
**Answer:**
Pessimistic locking prevents simultaneous updates by immediately locking a database record upon access. Other transactions attempting to modify the same record must block and wait until the lock is released upon commit or rollback. In relational databases like MySQL, this is commonly implemented using the 'SELECT ... FOR UPDATE' statement.

#### 20. What is a major architectural limitation of standard hotel reservation database schemas compared to standard rentals?
**Answer:**
Standard rentals (like Airbnb) use a specific listing_id/room_id at reservation time. Hotels, however, require booking a *room type* (e.g., king-size, standard room) rather than a specific physical room number, which is only assigned dynamically upon guest check-in.

#### 21. What is database normalization and how does it prevent anomalies?
**Answer:**
Normalization is the process of removing data duplication by storing human-meaningful data in a single place and referencing it via surrogate IDs. Because IDs have no human meaning, they rarely change. This eliminates write amplification and reduces the risk of data anomalies and inconsistencies caused by redundant copies falling out of sync.

#### 22. What is impedance mismatch in database modeling?
**Answer:**
Impedance mismatch refers to the conceptual and structural difficulties that occur when translating data between object-oriented programming models and the relational database model of tables, rows, and columns.

#### 23. What is query-side aggregation in data storage systems?
**Answer:**
Query-side aggregation computes data summaries and rollups dynamically at query time rather than pre-aggregating them during ingestion. This approach avoids raw data loss and allows flexible ad-hoc querying, but incurs higher query latency as computations are executed across the full dataset.

#### 24. What is storage locality in document databases and why does it matter?
**Answer:**
Storage locality means a document is stored as a single continuous string (e.g., JSON, XML, BSON). If an application frequently needs to access the entire document at once, storage locality drastically improves performance by eliminating the need for multiple index lookups, disk seeks, and joins across multiple relational tables.

#### 25. What is the appropriate database choice and data model for a location history database in a nearby friends application?
**Answer:**
The location history schema requires user_id, latitude, longitude, and timestamp. Because of the heavy-write workload and the need for horizontal scaling, Cassandra or a sharded relational database (sharded by user_id for even load and operational simplicity) is ideal. Cassandra handles massive writes efficiently while providing high availability and partition tolerance (AP).

#### 26. What is the data access pattern of a monitoring and alerting system?
**Answer:**
The system experiences a constant heavy write load (millions of operational metrics written per day at high frequency) combined with spiky, bursty read volumes driven by visualization and alerting queries.

#### 27. What is the difference between B-Tree and B+Tree?
**Answer:**
B+Trees store keys only in internal nodes, keep all actual data pointers/values exclusively in leaf nodes, and have linked leaf nodes for efficient range scans. B-Trees store keys and data in all nodes and lack leaf node linking.

#### 28. What is the difference between primary and secondary indexes?
**Answer:**
A primary index uniquely identifies a row, whereas a secondary index handles non-unique keys. Secondary indexes resolve duplicates either by storing a list of matching row identifiers (postings list) or by appending a row identifier to make each index key unique.

#### 29. What is the difference between shared and exclusive locks in Two-Phase Locking (2PL)?
**Answer:**
Shared locks (read locks) can be acquired by multiple transactions concurrently for reading. Exclusive locks (write locks) are granted to only one transaction at a time for modifications, blocking all other read and write operations.

#### 30. What is the impact of database sharding on relational joins?
**Answer:**
Sharding a database across multiple servers makes cross-shard relational join operations extremely difficult and expensive. A common architectural workaround is to denormalize the data so that queries can be efficiently executed within a single table or shard.

#### 31. What is the most critical factor when implementing a database sharding strategy?
**Answer:**
The choice of the sharding key (partition key), which consists of one or more columns determining data distribution. A proper sharding key (e.g., 'user_id') allows efficient data retrieval and modification by routing queries to the correct database shard. The primary criteria is choosing a key that evenly distributes data to avoid hotspots.

#### 32. What is the most widely used indexing structure in traditional databases?
**Answer:**
The B-tree. While log-structured indexes (like LSM-trees) are common in write-heavy storage engines, B-trees remain the most widely used indexing structure.

#### 33. What is the table schema structure for a transactional payment service?
**Answer:**
Requires at least two primary tables: (1) The payment event table storing details (checkout_id PK, buyer_info, seller_info, credit_card_info, is_payment_done boolean). (2) The payment order table tracking execution status (payment_order_id PK, buyer_account, amount, currency, checkout_id FK, payment_order_status, ledger_updated boolean, wallet_updated boolean).

#### 34. What kind of database is suitable for a hotel reservation system and why?
**Answer:**
A relational database is suitable because:
1. Read-heavy / write-less workflow: The number of users visiting the platform is orders of magnitude higher than those completing reservations, which aligns well with relational read patterns.
2. ACID guarantees: Critical for preventing issues like double charges, negative balances, and double bookings, while simplifying application-layer logic.
3. Data modeling: Business entities (hotels, rooms, room types) have stable schemas and clear relational structures easily modeled by RDBMS.

#### 35. What performance advantage does maintaining raw logs have compared to maintaining database indexes?
**Answer:**
Maintaining additional indexing structures incurs significant write overhead. Simply appending data to a file is the most optimal write operation, whereas any kind of index slows down writes because it must be updated on every write/modification.

#### 36. When is a document data model preferred over a relational model?
**Answer:**
Use a document model when data exhibits a tree-like, one-to-many relationship structure that is typically loaded entirely at once. The relational technique of shredding data into multiple tables can lead to cumbersome schemas and unnecessarily complicated application code, whereas document storage locality allows entire documents to be stored as a single continuous string (e.g., JSON, BSON), reducing index lookups and disk seeks.

#### 37. When is schema-on-read advantageous over schema-on-write?
**Answer:**
Schema-on-read is advantageous when data is heterogeneous (items do not share the exact same structure), when there are many different types of objects that are impractical to separate into individual tables, or when data structures are determined by external systems outside your control that may change at any time. In these scenarios, schemaless documents provide a natural model, whereas structured schemas are preferred when all records are expected to share a uniform structure.

#### 38. Where is a write request primarily persisted in standard storage engines?
**Answer:**
A write request is primarily persisted sequentially onto a commit log or Write-Ahead Log (WAL) file before being applied to memory structures and background data files.


### 🔴 Senior Level

#### 1. Are column-family databases like Cassandra and HBase truly column-oriented?
**Answer:**
No. Although they feature 'column families' inherited from Bigtable, within each column family they store all columns of a row together with the row key and do not apply true column compression. Thus, the Bigtable storage model remains fundamentally row-oriented.

#### 2. Explain time series data compression techniques.
**Answer:**
Time series databases use specialized compression algorithms to handle high ingestion rates and vast storage volumes. Key techniques include: 1) Delta-of-Delta encoding for timestamps (storing the variance of time intervals rather than absolute timestamps). 2) Gorilla floating-point compression (using XOR bit-masking on consecutive IEEE 754 floating-point values to omit repeating leading and trailing zero bits). 3) Dictionary encoding and run-length encoding (RLE) for categorical or repetitive metric tags.

#### 3. How do hash partitions (e.g., Redis cluster) affect leaderboard score updates and top-K range queries?
**Answer:**
Sharding via consistent hashing or CRC16(key)%16384 handles clustered/clumped scores well; a write updates the target shard directly. However, retrieving top-N players (e.g., top 10) becomes more complex, requiring the application layer to query every individual shard and merge-sort the results.

#### 4. How do we choose the right database for raw vs. aggregated ad click data?
**Answer:**
For write-heavy raw data (50k peak QPS), use NoSQL databases (like Cassandra/InfluxDB) or object storage (Amazon S3 with Parquet/ORC/AVRO) optimized for writes and sequential scans. For read/write-heavy aggregated time-series data queried frequently for dashboards, use a database supporting fast range queries and OLAP functions.

#### 5. How do you design a scalable NoSQL leaderboard schema to avoid full table scans?
**Answer:**
Replace traditional relational setups with a denormalized view in a NoSQL store like DynamoDB containing all render data. To prevent linear scans as rows grow, use a composite primary key structure such as "game_name#{year-month}" as the partition key and the score as the sort key.

#### 6. How does Multi-Master Replication utilize auto_increment for ID generation?
**Answer:**
Multi-master replication configures multiple database servers to generate auto_increment IDs using an offset and increment step equal to the total number of master nodes (e.g., node 1 generates IDs 1, 3, 5; node 2 generates 2, 4, 6). This prevents ID collisions across nodes without cross-server coordination during inserts.

#### 7. How should object-to-metadata mappings be stored and deployed in a large-scale distributed object storage system?
**Answer:**
Store mappings in a relational database (which favors read performance for write-once, read-many workloads) rather than a write-optimized LSM-tree/RocksDB store. To scale without massive centralized cluster management, deploy an embedded file-based relational database (e.g., SQLite) locally on each data node since metadata is naturally isolated per node.

#### 8. How should user profile and friendship data be modeled and scaled in a real-time 'nearby friends' application?
**Answer:**
User profiles and friendships are typically managed via horizontal sharding based on user ID in a relational database. At scale, this data is often abstracted behind an internal API layer so that WebSocket gateway servers fetch states via internal services rather than querying databases directly.

#### 9. Is data locality optimization (grouping related data together) exclusively a feature of document databases?
**Answer:**
No. Other models support locality: Google Spanner allows relational rows to be interleaved within parent tables, Oracle uses multi-table index cluster tables, and Bigtable-derived models (Cassandra, HBase) use column-families for locality.

#### 10. What architectural limitations did early Hierarchical Data Models (like IMS) share with modern document databases?
**Answer:**
They excelled at handling one-to-many relationships but made many-to-many relationships difficult. They lacked native join support, forcing developers to choose between data denormalization (duplication) or manually resolving cross-record references at the application layer.

#### 11. What are the broad categories of database storage engines and their distinct workloads?
**Answer:**
OLTP systems handle high-volume, user-facing requests touching a small number of records via keys and indexes; disk seek time is often the bottleneck. Data warehouses/analytic systems handle low-volume, high-demanding queries requiring millions of scans; disk bandwidth is the bottleneck, and column-oriented storage is typically used.

#### 12. What are the performance limitations and constraints of document databases?
**Answer:**
1. Locality drawback: The database must load the entire document even if only a small sub-field is accessed, wasting I/O on large documents.
2. Update overhead: Document modifications generally require rewriting the entire document unless the update preserves the exact encoded size. Documents should thus be kept small and growth-heavy writes avoided.

#### 13. What are the storage architecture options for storing a complex, nested user profile like a LinkedIn résumé?
**Answer:**
1. Relational normalization: Separate positions, education, and contact info into dedicated child tables with foreign keys linked to the users table.
2. Native structured data types / JSON columns: Use native JSON or XML datatypes supported by modern RDBMS (e.g., PostgreSQL, MySQL, Oracle) which allow indexing and querying inside documents.
3. Encrypted/Encoded document blob: Serialize jobs, education, and contact info into a single JSON/XML text column, letting the application handle parsing entirely while treating the database purely as a key-value/document store.

#### 14. What happens in the metadata schema and object storage during the object versioning write flow?
**Answer:**
(1) Client sends an HTTP PUT request. (2) API service validates identity and WRITE permissions. (3) Data store persists the binary as a new object, returning a new UUID. (4) Metadata store inserts a new record with the same bucket_id and object_name, but a new object_id and a time-ordered unique version identifier (TIMEUUID) as the object_version. The current version is retrieved by querying the largest TIMEUUID for a given object_name.

#### 15. What is the difference between Datalog and standard query languages like Cypher or SPARQL?
**Answer:**
Unlike declarative query languages that execute queries directly via SELECT statements, Datalog builds complex queries incrementally using logical rules and derived predicates that can refer to other rules or recurse iteratively.

#### 16. What is the origin and underlying principle of LSM (Log-Structured Merge-Tree) storage engines?
**Answer:**
Originally described by Patrick O'Neil et al., LSM-trees build on log-structured filesystem concepts using sorted in-memory indexes (like memtables) that flush to immutable SSTables on disk, which are subsequently merged and compacted in the background.

#### 17. What is the primary source of performance advantages in in-memory databases?
**Answer:**
Counterintuitively, the performance advantage is not solely due to avoiding disk reads (since OS page caches already keep recently used disk blocks in memory). Instead, in-memory databases are faster because they avoid the CPU overhead of encoding and decoding in-memory data structures into formats optimized for disk persistence.

#### 18. What is the source of data corruption in B-trees during page splits?
**Answer:**
B-tree updates require overwriting multiple pages (e.g., writing two split child pages and updating their parent page reference). If a database crashes midway through this sequence, it results in a corrupted index, such as an orphan page lacking a valid parent reference.

#### 19. What specialized data problems and scales cannot be efficiently solved by typical relational database systems?
**Answer:**
1. Sequence-similarity searches (e.g., matching DNA strings in bioinformatics, requiring specialized software like GenBank).
2. Big Data-scale analytical workloads with hundreds of petabytes (e.g., Large Hadron Collider data).
3. Full-text search over unstructured text payloads, which typically requires dedicated search engine models rather than standard relational tables.

#### 20. What was the network model (CODASYL model) in database history?
**Answer:**
A generalization of the hierarchical model standardized by CODASYL. Unlike the hierarchical model where every record has exactly one parent, the network model allowed a record to have multiple parents (supporting many-to-one and many-to-many relationships).

#### 21. What were the two prominent solutions that emerged to solve the limitations of the hierarchical data model?
**Answer:**
The relational model (which became SQL) and the network model (which had an initial large following but eventually faded into obscurity). The debate between these two dominated the 1970s.

#### 22. Why is denormalization required when querying read and unread emails in large-scale NoSQL data models?
**Answer:**
NoSQL databases typically only index partition and cluster keys. Since flags like 'is_read' are usually neither, querying them requires full table scans or filtering in application memory, which fails at scale. To solve this, data is denormalized into separate tables (e.g., 'read_emails' and 'unread_emails'), moving items between them on state change to optimize read performance.


## 📂 Category: Database Architecture & Storage Engines (1 cards)

### 🟡 Mid Level

#### 1. What are B-trees and where are they commonly applied?
**Answer:**
B-trees are standard index implementations that keep key-value pairs sorted by key to enable efficient point lookups and range queries. They are widely used in almost all relational databases and many non-relational databases, maintaining a balanced tree structure with predictable read/write characteristics.


## 📂 Category: Database Architectures (1 cards)

### 🟢 Junior Level

#### 1. What are non-relational (NoSQL) databases and their key characteristics?
**Answer:**
NoSQL databases (e.g., Cassandra, Neo4j, DynamoDB) fall into key-value, graph, column, or document stores. They are designed for horizontal scalability and schema flexibility, though they generally lack native cross-table join operations.


## 📂 Category: Database Design (4 cards)

### 🟢 Junior Level

#### 1. How are emails and their attachments queried in a relational email schema?
**Answer:**
Emails are retrieved using a simple query like `SELECT * FROM emails_by_user WHERE email_id = 123;`. Attachments, which can be multiple per email, are retrieved using the composite key combination of `email_id` and `filename` fields.

#### 2. How do you query read or unread emails by folder in a relational database schema?
**Answer:**
The query to fetch read emails uses a composite index filter: `SELECT * FROM emails_by_folder WHERE user_id = <id> AND folder_id = <id> AND is_read = true ORDER BY email_id;`. Unread emails are fetched with the same query by changing the flag to `is_read = false`.

#### 3. What type of database is ideal for geocoding services in applications like Google Maps, and why?
**Answer:**
A key-value database such as Redis is ideal because geocoding requires high-throughput, low-latency reads (converting place names/addresses to lat/lng pairs) against relatively infrequent writes.


### 🔴 Senior Level

#### 1. What is the advantage of having one row per date in a hotel reservation system inventory table?
**Answer:**
Using a composite primary key of (hotel_id, room_type_id, date) simplifies querying and managing inventory across complex date ranges. These rows are typically pre-populated for future dates, and updated via scheduled daily jobs.


## 📂 Category: Database Internals (22 cards)

### 🟢 Junior Level

#### 1. How can a simple key-value database be implemented using bash?
**Answer:**
A key-value store can be built using shell functions (`db_set key value` and `db_get key`) leveraging an append-only log file. Appending to a file provides high write performance, a pattern mirrored by many production databases internally.

#### 2. What are key-value (primary key) indexes?
**Answer:**
Key-value indexes uniquely identify a single row in a relational table, document in a document store, or vertex in a graph database, allowing other records to reference them efficiently.

#### 3. What is the performance drawback of implementing db_get with a simple CSV log?
**Answer:**
A naive CSV log lookup has an O(n) time complexity. Every key retrieval requires scanning the entire database file from beginning to end, meaning lookups take twice as long if the record count doubles.


### 🟡 Mid Level

#### 1. How can additional pointers improve the performance of B-trees?
**Answer:**
Additional pointers can be added to leaf pages (e.g., references to sibling pages to the left and right). This allows scanning keys in order sequentially without needing to jump back up to parent pages.

#### 2. How do multiple segment files affect indexing and lookups in log-structured storage?
**Answer:**
Each segment maintains its own in-memory hash table mapping keys to file offsets. To find a key, the system checks the most recent segment's hash map first, then falls back to older segments sequentially. A compaction and merging process keeps the total number of segments small to bound lookup latency.

#### 3. How does a B-Tree differ from a Binary Search Tree and maintain its balance?
**Answer:**
B-Tree nodes can contain multiple keys, all leaf nodes reside at the same depth, and they are heavily optimized for disk I/O with superior space utilization. To maintain balance, if a page lacks free space for a new key, it splits into two half-full pages, updating the parent page; this guarantees a depth of O(log n) for n keys.

#### 4. What are in-memory databases and why are they used?
**Answer:**
In-memory databases store entire datasets in RAM instead of traditional block storage (SSDs/HDDs), bypassing disk I/O bottlenecks to achieve ultra-low latency at the trade-off of higher cost-per-gigabyte and durability management.

#### 5. What are partial indexes and what benefits do they provide?
**Answer:**
Partial indexes index only a subset of table rows meeting a specified conditional predicate. Benefits include reducing index storage size, improving insert/update performance, and optimizing targeted query execution paths.

#### 6. What are the trade-offs of using compression in storage systems?
**Answer:**
Pros: Reduced storage space, lower I/O bandwidth.
Cons: CPU overhead for compression/decompression algorithms, potential latency increase.

#### 7. What are the trade-offs of using database indexes?
**Answer:**
Key trade-offs include:
1. Faster read operations (O(log n) or O(1) lookups)
2. Slower write operations (indexes must be updated on INSERT/UPDATE/DELETE)
3. Additional storage space required for index structures (e.g., B-Trees)
4. Maintenance overhead for query planners and index fragmentation

#### 8. What is index selectivity and why is it important?
**Answer:**
Index selectivity is the ratio of unique values to total rows in a column. Higher selectivity (closer to 1) means better query performance, more efficient index utilization, and that the column is a strong candidate for indexing.

#### 9. What is the first step in the read path when checking a storage engine if data is not in memory?
**Answer:**
Check the Bloom filter to quickly rule out the existence of the key in non-volatile storage before performing costly disk reads.

#### 10. What is the fundamental difference between imperative and declarative query languages?
**Answer:**
Imperative languages execute explicit procedural operations step-by-step (evaluating conditions, updating variables, managing loops). Declarative query languages (like SQL) specify the desired result pattern and transformation constraints, leaving the database query optimizer to determine the optimal execution plan, index usage, and join strategies.

#### 11. What is the key difference between row-oriented and column-oriented storage?
**Answer:**
Row-oriented stores data consecutively by row (horizontal storage), which is optimal for transactional workloads (OLTP). Column-oriented stores data by column (vertical storage), which is highly efficient for analytical queries (OLAP) as it reads only the required columns and compresses better.


### 🔴 Senior Level

#### 1. How do standard B-trees and LSM-trees handle geospatial queries, and what are the alternatives?
**Answer:**
Standard B-trees and LSM-trees cannot efficiently answer two-dimensional geospatial queries simultaneously (they handle one dimension like latitude or longitude independently). Solutions include translating 2D locations into a single number using space-filling curves for B-trees, or using specialized spatial indexes like R-trees (e.g., PostGIS in PostgreSQL using Generalized Search Trees).

#### 2. What are Composite Partitioning strategies?
**Answer:**
Composite partitioning combines multiple partitioning strategies (such as range and hash, or list and hash) to distribute data across nodes effectively, preventing hotspots while supporting range queries.

#### 3. What are Global Secondary Indexes (GSIs)?
**Answer:**
A Global Secondary Index is an index on attributes other than the primary key where the index data can be partitioned separately from the base table, allowing queries across all partitions of the dataset.

#### 4. What are Local Secondary Indexes (LSIs)?
**Answer:**
A Local Secondary Index is an index maintained within the same partition as the base table item, ensuring strong consistency with the primary item but restricted to querying data within a single partition.

#### 5. What are the two main families of storage engines?
**Answer:**
1. Log-structured storage engines (optimized for writes, append-only, e.g., LSM-trees).
2. Page-oriented storage engines (optimized for reads, in-place updates, e.g., B-trees).

#### 6. What is index fragmentation and why does it matter?
**Answer:**
Index fragmentation occurs when index pages are not physically ordered to match their logical order. It matters because it leads to: 1. Increased I/O operations, 2. Slower query performance due to scattered disk reads, and 3. Inefficient disk space usage.

#### 7. What is the difference between the joins of the relational and network models?
**Answer:**
Foreign key constraints allow you to restrict modifications in relational models, but joins on foreign keys are performed dynamically at query time. In contrast, within the CODASYL network model, the join was effectively resolved and executed at insert time.

#### 8. What is the structural difference between log-structured indexes and B-trees?
**Answer:**
Log-structured indexes break the database down into variable-size segments (typically several megabytes or more) and always write segments sequentially. B-trees break the database down into fixed-size blocks or pages (traditionally 4 KB) and read or write one page at a time, aligning more closely with underlying hardware disk blocks.


## 📂 Category: Database Partitioning (2 cards)

### 🟢 Junior Level

#### 1. How does List Partitioning work for database scaling?
**Answer:**
List partitioning assigns rows to partitions explicitly based on a predefined list of discrete values matching a specific column's contents (e.g., routing rows where region is 'US' or 'CA' to partition A, and 'EU' or 'UK' to partition B).

#### 2. How does Range Partitioning work for database scaling?
**Answer:**
Range partitioning divides data by assigning continuous ranges of key values (such as alphabetical ranges for last names or chronological ranges for timestamps) to specific partitions or nodes. While effective for range queries, it risks hotspots if write workloads are heavily skewed toward recent timestamps.


## 📂 Category: Database Scaling (2 cards)

### 🟢 Junior Level

#### 1. What is vertical database scaling (scaling up)?
**Answer:**
Vertical scaling means adding more hardware resources (CPU, RAM, DISK) to an existing machine. Modern database servers can scale up significantly (e.g., AWS RDS instances with 24 TB of RAM), enabling massive monolithic workloads (like StackOverflow handling millions of unique visitors with a single master database in its early years).


### 🔴 Senior Level

#### 1. What strategies can be used when hotel reservation data exceeds the capacity of a single database?
**Answer:**
Store only current and future reservation data in active storage; archive historical reservation data to cold storage. For active data, shard by hash(hotel_id) % number_of_servers, as most frequent queries (making a reservation or looking up by name/hotel) rely on the hotel_id.


## 📂 Category: Database Storage Engines (6 cards)

### 🟡 Mid Level

#### 1. How do append-only storage engines like Bitcask prevent and handle partially written records during crashes?
**Answer:**
Bitcask includes cryptographic checksums with each appended record. Upon startup or read, the engine uses these checksums to detect and ignore corrupted or partially written records resulting from system crashes.

#### 2. How does the Bitcask storage engine optimize read and write performance?
**Answer:**
Bitcask keeps its entire hash map of keys pointing to file offsets in RAM, enabling extremely fast reads and writes under the constraint that all keys fit in memory. Values require at most a single disk seek, which can be avoided entirely if cached in the OS filesystem cache.

#### 3. What are the step-by-step operations involved in B-Tree insertions?
**Answer:**
1. Traverse the tree to find the appropriate leaf node. 2. If the node has available capacity, insert the key-value pair. 3. If the node is full, split the node into two. 4. Propagate the median key upward into the parent node, repeating the split process up the tree if necessary.

#### 4. What is the idea behind column-oriented storage?
**Answer:**
Instead of storing all values from one row together, column-oriented storage stores all values from each column together. Storing each column in a separate file allows queries to read and parse only the specific columns required, significantly reducing disk I/O.


### 🔴 Senior Level

#### 1. How does an SSTable (Sorted String Table) storage engine process writes, reads, and compaction?
**Answer:**
Writes are appended to an in-memory balanced tree (memtable). When the memtable exceeds a size threshold, it is flushed to disk as a sorted SSTable file. Reads check the memtable first, then scan on-disk segments from newest to oldest. A background compaction process merges segment files and discards overwritten or deleted values.

#### 2. What is the impact of compaction on the performance of LSM-trees?
**Answer:**
Compaction can interfere with ongoing read and write performance, causing latency spikes at higher percentiles due to limited disk resources. Additionally, at high write throughputs, finite disk bandwidth must be shared between initial flushes (memtable to disk) and background compaction threads, becoming more demanding as the database grows.


## 📂 Category: Database Transactions (6 cards)

### 🟢 Junior Level

#### 1. What are the main characteristics of the Read Committed isolation level?
**Answer:**
1. No dirty reads (transactions cannot see uncommitted data)
2. May allow nonrepeatable reads (data can change between reads within a transaction)
3. Most common isolation level in practice
4. Default in many relational databases like PostgreSQL


### 🟡 Mid Level

#### 1. What are the main benefits of Snapshot Isolation?
**Answer:**
1. Readers never block writers
2. Writers never block readers
3. Consistent view of the database via MVCC
4. Good performance for read-heavy workloads
5. Prevents many common anomalies (like dirty reads and nonrepeatable reads)

#### 2. What is Isolation in ACID transactions?
**Answer:**
Isolation ensures that the concurrent execution of multiple transactions leaves the database in the exact same state that would be obtained if the transactions were executed sequentially, preventing transaction interference and race conditions.


### 🔴 Senior Level

#### 1. What is Write Skew in concurrent transactions?
**Answer:**
Write skew is a concurrency anomaly that occurs when two transactions read the same overlapping set of data, make independent decisions based on that data, and write mutually non-conflicting modifications that collectively violate a global domain constraint. It can occur even under snapshot isolation.

#### 2. What is the main characteristic of Serializable Snapshot Isolation (SSI)?
**Answer:**
SSI provides full serializability while maintaining the performance benefits of snapshot isolation. Instead of relying on pessimistic locking, it optimistically detects potential serialization conflicts and aborts transactions when a serialization anomaly is detected.

#### 3. What is the main drawback of Two-Phase Locking (2PL)?
**Answer:**
The primary drawback is reduced concurrency due to heavy lock contention, leading to poor performance under high-concurrency workloads. Additionally, deadlocks are common and require active detection and resolution mechanisms.


## 📂 Category: Databases (48 cards)

### 🟢 Junior Level

#### 1. In a key-value pair, what component must be unique?
**Answer:**
The key must be unique.

#### 2. What are alternative names for key-value stores and relational databases?
**Answer:**
A distributed key-value store is also known as a distributed hash table. A key-value store is often called a key-value database. A relational database is commonly referred to as an RDBMS or SQL database.

#### 3. What are relational databases and how do they represent data?
**Answer:**
Relational databases (RDBMS or SQL databases) like MySQL, Oracle, and PostgreSQL represent and store data in tables composed of rows and columns. They allow users to perform join operations across different database tables using SQL.

#### 4. What are the advantages of database replication?
**Answer:**
Better performance: In a master-slave model, writes go to the master while reads are distributed across slaves, allowing queries to be processed in parallel. Reliability: Data is preserved and protected against localized disasters or hardware failures via multi-location replication. High availability: The website or application remains operational even if one database server goes offline by failing over to a replica.

#### 5. What are the basic core operations of a key-value store?
**Answer:**
put(key, value): inserts or updates the value associated with the specified key. get(key): retrieves the value associated with the specified key.

#### 6. What are the broad approaches for database scaling?
**Answer:**
The two primary approaches are vertical scaling (scale-up: adding CPU, RAM, or storage to a single server) and horizontal scaling (scale-out: distributing the load across multiple servers via techniques like sharding or replication).

#### 7. What does ACID stand for in the context of database transactions?
**Answer:**
Atomicity (all-or-nothing execution), Consistency (valid state transitions), Isolation (concurrent transaction independence), and Durability (persistence of committed data).

#### 8. What is Atomicity in ACID transactions?
**Answer:**
Atomicity ensures that all operations within a transaction are treated as a single indivisible unit: they either all succeed (commit) or all fail and roll back (no partial completion).

#### 9. What is the foundational relational data model for SQL databases?
**Answer:**
Proposed by Edgar Codd in 1970, data is organized into relations (SQL tables), where each relation is an unordered collection of tuples (SQL rows).

#### 10. What is the relationship between a master and slave database in database replication?
**Answer:**
In traditional primary-secondary (master-slave) database replication, the master/primary database supports write operations and replicates changes to the slave/secondary databases, which typically support read operations.

#### 11. Why are analytical queries generally prohibited on primary OLTP (Online Transaction Processing) databases?
**Answer:**
OLTP systems require high availability and low latency for mission-critical transactions. Ad-hoc analytical queries scan large parts of the dataset, causing heavy resource contention (CPU, memory, disk I/O) that degrades concurrently executing transactional performance.

#### 12. Why does the standard auto_increment mechanism fail to work effectively in distributed database environments?
**Answer:**
A single database server is often insufficient for scale, and generating strictly monotonic and unique IDs concurrently across multiple distributed databases with minimal latency and no single point of failure is extremely challenging.

#### 13. Why is column-oriented storage preferred over row-oriented storage for data warehousing and OLAP workloads?
**Answer:**
Column-oriented storage stores data for each column contiguously, yielding significantly higher compression ratios and faster analytical execution because queries only need to read relevant columns rather than scanning entire rows.


### 🟡 Mid Level

#### 1. How are schema changes handled differently in document-based versus statically typed relational databases?
**Answer:**
In a document database, you can immediately start writing new documents with updated fields and handle missing fields gracefully in application code (schema-on-read). In a statically typed database schema, you must explicitly perform a structured database migration to alter table structures.

#### 2. How do you express variable-length traversal paths in SQL queries?
**Answer:**
Since SQL:1999, variable-length traversal paths can be expressed using recursive common table expressions via the WITH RECURSIVE syntax. For example, it can find names of people who emigrated from the US to Europe, though the syntax can be more clumsy compared to graph query languages like Cypher.

#### 3. How does SQL differ from early hierarchical and network models like IMS and CODASYL?
**Answer:**
SQL is a declarative query language where developers specify *what* data to retrieve, leaving the query optimizer to determine *how* to access it. IMS and CODASYL relied on imperative navigation, requiring developers to write explicit programmatic loops and pointer traversals to navigate through hierarchical and graph-like database structures.

#### 4. How does database sharding work and how is routing typically implemented?
**Answer:**
Sharding splits large databases into smaller, manageable parts (shards) sharing the same schema. Routing is commonly handled via a hash function applied to a partition key (e.g., user_id % 4), directing operations to the corresponding shard.

#### 5. How does using a sorted set compare to using a relational database in a leaderboard?
**Answer:**
Sorted sets (e.g., Redis ZSET) provide O(log n) complexity for insert, update, and range queries because elements are automatically ordered by score upon insertion. In contrast, RDBMS implementations require costly subqueries or window functions with full table scans and sorting (e.g., SELECT COUNT(*) WHERE score >= current_score), making them significantly less performant at scale.

#### 6. How have document and relational databases converged in recent years?
**Answer:**
Relational databases (like PostgreSQL, MySQL, and IBM DB2) have added robust native support for semi-structured JSON documents and querying. Conversely, document databases (like MongoDB and RethinkDB) have introduced capabilities like database references, client-side joins, or query-language joins.

#### 7. What are examples of data structures better represented using a property graph model instead of a relational database?
**Answer:**
Data structures with highly variable, interconnected, or hierarchical schemas that differ across entities, such as regional administrative structures (e.g., France using départements and régions vs. the US using counties and states), historical geopolitical anomalies, or varying data granularity (e.g., a person's current residence specified at the city level vs. birth place at the state level).

#### 8. What are the advantages of in-memory databases beyond performance?
**Answer:**
Besides raw performance, in-memory databases provide data models that are difficult or inefficient to implement with disk-based indexes. For example, Redis offers a database-like interface to complex data structures such as priority queues and sets. Because data resides entirely in memory, its internal implementation and operational complexity remain relatively simple.

#### 9. What is SPARQL?
**Answer:**
SPARQL (SPARQL Protocol and RDF Query Language) is a graph query language designed for querying triple-stores using the Resource Description Framework (RDF) data model.

#### 10. What is a naive two-dimensional search approach for proximity/location-based services?
**Answer:**
A naive two-dimensional search queries a relational database using bounding box range checks across latitude and longitude coordinates. Example SQL: `SELECT business_id, latitude, longitude FROM business WHERE (latitude BETWEEN {:my_lat} - radius AND {:my_lat} + radius) AND (longitude BETWEEN {:my_long} - radius AND {:my_long} + radius)`. This approach performs poorly at scale because it fails to leverage spatial indexes effectively.

#### 11. What is a snowflake schema in data warehousing?
**Answer:**
A variation of the star schema where dimensional tables are further normalized into subdimensions (e.g., separate tables for brands and categories linked via foreign keys). While more normalized, star schemas are often preferred for analytics due to simpler querying.

#### 12. What is an alternative to running an expensive UPDATE command on a massive database table?
**Answer:**
Instead of rewriting every row with an UPDATE statement, the application can keep fields at a default value (like NULL) and compute or populate them dynamically at read time, similar to document store patterns.

#### 13. What is sharding and why is it important for storage systems?
**Answer:**
Sharding is the process of partitioning data horizontally across multiple machines to scale out storage and handle larger datasets and higher throughput than a single node could manage.

#### 14. What is the aggregation pipeline in MongoDB?
**Answer:**
MongoDB 2.2 added support for a declarative query language called the aggregation pipeline to counter the performance and expressiveness shortcomings of MapReduce.

#### 15. What is the difference between Read Committed and Snapshot Isolation isolation levels?
**Answer:**
Read Committed sees only committed data at the time of each read, while Snapshot Isolation sees data as it existed at the start of the transaction, effectively preventing non-repeatable reads.

#### 16. What is the key difference between pessimistic and optimistic concurrency control?
**Answer:**
Pessimistic control (such as 2PL) assumes conflicts are likely and blocks operations using locks. Optimistic control assumes conflicts are rare, allows operations to proceed without locks, and checks for conflicts later.

#### 17. What is the triple-store model in database systems?
**Answer:**
The triple-store model is a data structure largely equivalent to the property graph model where all information is stored as simple three-part statements: (subject, predicate, object). For example, in the triple (Jim, likes, bananas), Jim is the subject, likes is the predicate, and bananas is the object.

#### 18. What is the typical number of levels in a B-tree database index?
**Answer:**
Most database B-trees are typically 3 or 4 levels deep. Because of high branching factors (e.g., a 4-level B-tree with 4 KB pages and a branching factor of 500 can store up to 256 TB), traversing 3-4 node page references is sufficient to locate any target leaf page.

#### 19. Why does storing highly interconnected data (like regional population data) create challenges in document databases?
**Answer:**
Document databases lack robust native support for joins because they prioritize tree-structured, self-contained documents. Emulating many-to-one relationships requires application-level joins via multiple queries. As applications evolve, data naturally becomes more interconnected, straining join-free document models.

#### 20. Why doesn't it make sense to sort each column independently in a column-oriented database store?
**Answer:**
Sorting columns independently breaks row reconstruction. Rows can only be reassembled because the kth item in one column corresponds deterministically to the kth item in another column within the same logical row.

#### 21. Why is merging segments in log-structured storage engines (using SSTables) efficient?
**Answer:**
It uses a mechanism analogous to the merge-sort algorithm: input segment files are read side-by-side, keys are compared, and the lowest key according to the sort order is written to a new output file sequentially, ensuring high sequential I/O throughput.

#### 22. Why is storing business IDs as an array inside a single database field inferior to storing them in separate relational rows?
**Answer:**
Array fields complicate mutations: updating or inserting elements requires fetching, scanning, and deserializing the entire array while handling race conditions with explicit row-level locks. Using separate rows with compound keys (e.g., geohash, business_id) allows atomic insertions and deletions without locking entire collections.


### 🔴 Senior Level

#### 1. How do bitmap indexes accelerate analytical queries in data warehouses?
**Answer:**
Bitmap indexes represent column values as bit arrays for rows. They accelerate analytical queries by allowing highly efficient bitwise operations (AND, OR) across multiple columns sharing the same row ordering (e.g., evaluating `WHERE product_sk = 31 AND store_sk = 3` via bitwise AND).

#### 2. How does TimescaleDB extend PostgreSQL?
**Answer:**
TimescaleDB extends PostgreSQL by adding time-series optimizations via automatic partitioning (hypertables) across time and space, transparent chunking, columnar compression, and fast interval-based aggregates, while retaining full ANSI SQL support and relational features.

#### 3. How does Two-Phase Locking (2PL) prevent concurrency anomalies?
**Answer:**
2PL prevents all possible race conditions and ensures serializable execution by dividing transaction execution into two phases: the growing phase (acquiring shared/exclusive locks without releasing any) and the shrinking phase (releasing locks without acquiring new ones), holding all locks until the transaction commits or aborts.

#### 4. How does the indexing of column stores relate to data compression?
**Answer:**
Sorting column stores by a primary sort key creates long sequences of repeated values when low-cardinality columns are sorted first. This enables highly efficient run-length encoding (RLE), compressing columns drastically down to kilobytes even across billions of rows. Secondary sort keys have diminishing compression returns.

#### 5. How is a heap file used for storing database indexes?
**Answer:**
In secondary index architectures, index keys point to references or direct locations in an append-only or unordered 'heap file' where actual row data resides. This heap file approach avoids data duplication when multiple secondary indexes reference the same logical record, keeping the underlying row data stored in a single unified location.

#### 6. What are common optimization techniques for B-tree database indexes?
**Answer:**
Common optimizations include: 1) Using copy-on-write schemes (like LMDB) instead of overwriting pages and maintaining a Write-Ahead Log (WAL) for crash recovery. 2) Saving page space by abbreviating keys rather than storing full keys. 3) Allocating adjacent leaf pages sequentially in disk storage to minimize disk seeks. 4) Adding extra pointers to the tree structure. 5) Using B-tree variants like fractal trees which incorporate log-structured merge concepts to reduce disk seeks.

#### 7. What are the advantages and use cases of the Datalog query language approach?
**Answer:**
Datalog uses a declarative rule-based logic paradigm where rules can be easily combined and reused across queries. While less convenient for simple one-off lookups, it excels at handling complex data relationships and inferences.

#### 8. What are the advantages of using a declarative language (like SQL) for querying databases?
**Answer:**
Declarative languages are more concise and hide database engine implementation details, allowing the system to introduce background performance optimizations (e.g., safely moving records or changing data order) without breaking queries. They also lend themselves better to parallel execution across multi-core CPUs and distributed machines because they specify the pattern of results rather than a strict procedural algorithm.

#### 9. What is an access path in the network database model?
**Answer:**
In the network model, links between records were pointer-based disk references rather than foreign keys. The only way to access a record was to traverse a path from a root record along these chains of links, known as an access path.

#### 10. What is the relationship between keys and transactions in B-trees versus LSM-trees?
**Answer:**
B-trees store each key in exactly one place in the index, allowing range locks to be directly attached to the tree nodes for robust transactional isolation in relational databases. Log-structured storage engines (LSM-trees) may contain multiple copies of the same key across immutable segments.

#### 11. What property of operational data should guide time-series database selection?
**Answer:**
Facebook research shows that at least 85% of queries to operational data stores target data collected within the past 26 hours. Choosing a time-series database optimized for this recency property significantly improves overall system performance.

#### 12. When and why does optimistic locking cause a performance drop?
**Answer:**
Optimistic locking performance drops dramatically under high concurrency due to repeated transaction retries. For instance, when multiple clients read the same initial state (e.g., available hotel rooms and version), only one write succeeds while the rest fail version checks and must retry repeatedly, degrading user experience.

#### 13. When is data flushed from memory to an SSTable on disk in LSM-tree storage engines?
**Answer:**
When the memory cache (memtable) is full or reaches a predefined threshold.


## 📂 Category: Databases & Caching (7 cards)

### 🟢 Junior Level

#### 1. How do you fetch a specific user's position from a sorted set-based leaderboard?
**Answer:**
To query a user's rank from high to low (descending order), use the Redis reverse rank command `ZREVRANK`. Example command: `ZREVRANK leaderboard_feb_2021 'mary1934'`.

#### 2. What are the best practices for setting a cache expiration policy?
**Answer:**
Always implement an expiration policy to prevent permanent memory retention and stale data. However, avoid setting expiration times too short (causing frequent cache misses and excessive database reloads) or too long (leading to stale data). Caches should primarily be used for data that is read frequently but modified infrequently.

#### 3. When is it appropriate to introduce a cache layer in system architecture?
**Answer:**
Use a cache when data is read frequently but modified infrequently. Because caches reside in volatile memory (RAM) and data is lost upon restart, they are unsuitable for primary data persistence. Critical or permanent data must always be stored in persistent data stores.


### 🟡 Mid Level

#### 1. How do database materialized views function as a form of query result caching?
**Answer:**
A materialized view is a table-like disk-backed object that stores pre-computed query results. Unlike a virtual view—which acts as a macro expanded on the fly by the SQL engine during reads—a materialized view avoids runtime query processing costs by maintaining an actual copy of the data.

#### 2. How do you handle record deletions in append-only log-structured hash table indexes?
**Answer:**
To delete a key and its value, you append a special deletion record known as a tombstone to the data file. During background log compaction and segment merging, the tombstone instructs the merging process to discard all previous values associated with that key.

#### 3. How does Redis implement hash partitioning for automated sharding?
**Answer:**
Redis Cluster uses hash slots rather than consistent hashing. There are exactly 16384 hash slots, and the slot for a given key is computed using CRC16(key) % 16384. Each node in the cluster is responsible for a subset of these hash slots, allowing seamless node additions and removals.


### 🔴 Senior Level

#### 1. How do you determine partition sizing and relative ranking for a NoSQL-based distributed leaderboard?
**Answer:**
More partitions decrease per-partition load but increase scatter-gather complexity. To handle user ranking without exact absolute index lookups across shards: assume score distributions are roughly uniform across all shards. Use a cron job to analyze score distributions per shard and cache percentiles (e.g., 10th percentile = score X). This allows quickly returning relative positions (e.g., 'top 10-20%' or 90th percentile) instead of exact costly global ranks.


## 📂 Category: Databases & Concurrency (1 cards)

### 🔴 Senior Level

#### 1. What concurrency issue arises under non-serializable isolation when multiple users book the last available item simultaneously?
**Answer:**
Race conditions occur. If two transactions concurrently read the inventory count (e.g., 1 room left) before either commits their update, both transactions evaluate availability as true, leading to overbooking when both successfully commit under weak isolation levels.


## 📂 Category: Databases & Data Modeling (1 cards)

### 🔴 Senior Level

#### 1. Explain the difference between property graphs and RDF graphs
**Answer:**
Property graphs model data as nodes, edges, and directed relationships, where both nodes and edges can store arbitrary key-value properties, making them popular for operational graph databases like Neo4j. RDF (Resource Description Framework) graphs model data as triples (Subject-Predicate-Object) based on W3C semantic web standards, designed for global data integration, logical reasoning, and ontology querying via SPARQL.


## 📂 Category: Databases & Graph Theory (1 cards)

### 🔴 Senior Level

#### 1. How does Neo4j handle graph relationship traversal?
**Answer:**
Neo4j uses 'index-free adjacency', where every node explicitly maintains direct physical pointers (references) to its adjacent nodes and relationships on disk. Traversing a graph means following these direct pointers rather than performing expensive global index lookups or join tables, yielding $O(1)$ traversal time per hop regardless of the total graph size.


## 📂 Category: Databases & Indexing (4 cards)

### 🟢 Junior Level

#### 1. What is a B-Tree and why is it widely used in databases?
**Answer:**
A B-Tree is a self-balancing tree data structure that maintains sorted data and permits searches, sequential access, insertions, and deletions in logarithmic time. It is heavily optimized for disk-based storage systems because its high branching factor minimizes disk I/O operations.

#### 2. What is a common database approach for generating unique incremental IDs?
**Answer:**
Using an auto_increment attribute paired with a primary key constraint is a traditional database approach for generating unique IDs, though it can become a bottleneck or single point of failure in distributed systems.


### 🟡 Mid Level

#### 1. What is a clustered index?
**Answer:**
A clustered index stores the actual data rows directly within the index structure rather than pointing to a separate heap file, eliminating an extra lookup hop for reads. For example, in MySQL's InnoDB engine, the primary key forms a clustered index, and secondary indexes reference this primary key.


### 🔴 Senior Level

#### 1. What indexing strategies are well-suited for geospatial data?
**Answer:**
Multi-dimensional indexes are utilized for querying several columns simultaneously, which is vital for geospatial data (e.g., storing latitude and longitude). This supports two-dimensional range queries, such as finding all records within a specific map bounding box (e.g., SELECT * FROM restaurants WHERE latitude > 51.4946 AND latitude < 51.5000 AND longitude > -0.1162 AND longitude < -0.1004).


## 📂 Category: Databases & Query Languages (2 cards)

### 🟡 Mid Level

#### 1. What is the Cypher query language?
**Answer:**
Cypher is a declarative query language designed for property graphs, specifically created for the Neo4j graph database.


### 🔴 Senior Level

#### 1. What is Datalog and where is it used?
**Answer:**
Datalog is a declarative logic programming query language originating from 1980s academic research. It provides the foundation for later graph/relational query languages and is used in data systems like Datomic and Cascalog (for Hadoop).


## 📂 Category: Databases & Storage (80 cards)

### 🟢 Junior Level

#### 1. Are all graph databases limited to homogeneous data?
**Answer:**
No. Graphs provide a consistent way of storing completely different types of objects and relationships in a single datastore (e.g., vertices for people, locations, events, and edges for friendships, check-ins, or comments).

#### 2. Describe a relational database solution for implementing a simple game leaderboard.
**Answer:**
For smaller scale applications, a monthly leaderboard can be implemented using a relational database table containing user IDs and score columns. When a user wins, their score is inserted (if new) or incremented. Rankings are determined by querying and sorting the table by score in descending order (ORDER BY score DESC). Real-world implementations may include additional columns such as game_id and timestamps, though the core indexing and sorting logic remains unchanged.

#### 3. How do composite indexes work in relational databases?
**Answer:**
Composite indexes include multiple columns and strictly follow the leftmost prefix rule. For example, an index defined on (a, b, c) can be leveraged for queries filtering on 'a', 'a,b', or 'a,b,c', but not on 'b' or 'c' independently.

#### 4. How do we execute listing commands in a single database backing an S3-like object storage service?
**Answer:**
Run SQL queries against the relational schema. To list buckets, query `SELECT * FROM bucket WHERE owner_id={id}`. To list objects with a specific prefix, run `SELECT * FROM object WHERE bucket_id = '123' AND object_name LIKE 'abc/%'`. Use application code to handle rollups for nested slashes or recursive listings.

#### 5. How does data storage and retrieval work when a hash map is used for indexing a key-value store?
**Answer:**
The storage engine appends new key-value pairs to a data file. An in-memory hash map maps every key to its corresponding byte offset in the data file. To write or update, you append to the file and update the hash map. To read, you look up the offset in the hash map, seek to that location in the file, and read the value.

#### 6. What are common optimizations for fitting more data onto a single database or cache server?
**Answer:**
Data compression (to reduce storage footprint) and keeping only frequently accessed hot data in memory (caching strategies).

#### 7. What are the fundamental operations supported by a key-value store?
**Answer:**
put(key, value) to store or update a value, and get(key) to retrieve the value associated with the specified key.

#### 8. What can a key be, plain text or a hashed value?
**Answer:**
A key can be plain text or a hashed value.

#### 9. What does 'no schema' mean in the context of databases?
**Answer:**
Document databases and JSON support in relational databases do not enforce a rigid schema on stored data. Arbitrary keys and values can be added to documents, meaning clients have no structural guarantees regarding the fields present when reading.

#### 10. What is a key-value store?
**Answer:**
A key-value store, also referred to as a key-value database, is a non-relational database. Each unique identifier is stored as a key with its associated value. This data pairing is known as a “key-value” pair.

#### 11. What is cold storage?
**Answer:**
Cold storage is a computer system designed for storing inactive data that is infrequently accessed and retained for a long time.

#### 12. What is denormalization in database design and when is it useful?
**Answer:**
Denormalization is the process of adding redundant data to a database schema to improve read performance. It is useful when high read throughput is prioritized over write consistency and normalization overhead.

#### 13. What is the primary purpose of database indexes?
**Answer:**
A database index is a data structure (such as a B-Tree or LSM-Tree) that improves the speed of data retrieval operations by providing quick access paths to data in database tables. Flow: Table -> Index -> Data.

#### 14. What is the purpose of indexing in storage systems?
**Answer:**
Indexing improves read performance by creating auxiliary data structures (such as B-Trees or LSM-trees) that allow the database to locate data quickly without performing full table scans across entire datasets.

#### 15. What types of values can be stored in a key-value pair?
**Answer:**
Values can be strings, lists, objects, etc.

#### 16. Which data representation and database type are most appropriate for a self-contained document like a résumé?
**Answer:**
JSON representation, supported by document-oriented databases such as MongoDB, RethinkDB, CouchDB, and Espresso. JSON offers a simpler alternative to XML for self-contained documents.

#### 17. Why aren't OLAP data warehouses common in small companies?
**Answer:**
Small companies typically lack numerous distinct OLTP systems and deal with small volumes of data. Their data is small enough to be queried directly in a conventional SQL database or analyzed in spreadsheets, avoiding the heavy lifting and operational complexity required for large-scale data warehousing.


### 🟡 Mid Level

#### 1. Can we use binary search for finding keys in SSTables if records have variable lengths?
**Answer:**
No. If all keys and values had a fixed size, you could use binary search directly on a segment file and bypass the in-memory index. However, because keys and values are variable-length in practice, an in-memory index is required to locate record boundaries.

#### 2. Compare storing a profile as a JSON document versus a relational multi-table schema.
**Answer:**
JSON reduces impedance mismatch between application code and storage, lacks strict schemas, and offers better data locality (all subordinate info like positions/education in one place, avoiding multi-way joins). A relational model normalizes data into separate tables linked by foreign keys, requiring joins or multiple queries to fetch complete nested trees.

#### 3. Describe the property graph model and its storage layout.
**Answer:**
In the property graph model, each vertex consists of a unique identifier, a set of outgoing edges, a set of incoming edges, and key-value properties. Each edge consists of a unique identifier, a tail (start) vertex, a head (end) vertex, a label, and key-value properties. For storage, it can be conceptualized as two relational tables: one for vertices and one for edges. Each edge stores its head and tail vertex IDs, allowing efficient retrieval of incoming and outgoing relationships by querying against these vertex references.

#### 4. Describe the storage layout of column-oriented storage databases.
**Answer:**
In a column-oriented storage layout, each column is stored in its own dedicated file where rows are maintained in a consistent global sort order. To reassemble an entire logical row, the storage engine fetches the Nth entry from each individual column file and combines them, drastically optimizing analytical queries that only scan a subset of columns.

#### 5. Do transactions strictly require ACID properties?
**Answer:**
No. A transaction does not necessarily need atomicity, consistency, isolation, and durability (ACID). Transaction processing simply means allowing clients to execute low-latency reads and writes, as opposed to periodic, high-latency batch processing jobs.

#### 6. How are access paths and query optimization implemented in relational databases?
**Answer:**
The query optimizer automatically determines the access path—deciding which execution steps, order of operations, and indexes to use. This choice is handled entirely by the database engine rather than the application developer. If new access patterns are needed, declaring a new index allows existing queries to automatically leverage it without modifying application code.

#### 7. How are pages referenced and structured in B-tree indexes?
**Answer:**
B-trees organize data into disk-based pages connected via disk addresses or pointers. The root page contains keys and references to child pages. Each child page is responsible for a continuous range of keys, with boundary keys determining the routing between child pages.

#### 8. How did the relational model differ fundamentally from the network and hierarchical models?
**Answer:**
The relational model lays out data openly as flat relations (tables) made of tuples (rows), eliminating labyrinthine nested structures and complicated access paths. It allows arbitrary condition querying, direct row lookups via keys, and independent row insertions without strict foreign key traversal constraints.

#### 9. How do document databases compare to relational and hierarchical database models?
**Answer:**
Document databases mirror the hierarchical model by nesting records within parent documents rather than normalizing them into separate tables. However, for many-to-one and many-to-many relationships, they behave similarly to relational systems by using foreign keys or document references resolved at read time via joins or follow-up queries.

#### 10. How do in-memory key-value caches and databases handle data durability?
**Answer:**
While caches like Memcached prioritize volatile storage, durable in-memory databases ensure persistence using specialized hardware (battery-backed RAM), writing write-ahead logs to disk, creating periodic disk snapshots, or replicating state across multiple nodes.

#### 11. How does crash recovery work in a hash table indexed database (like Bitcask)?
**Answer:**
If the database restarts, in-memory hash maps mapping keys to file byte offsets are lost. Bitcask speeds up recovery from reading entire segment files by storing a snapshot of each segment's hash map on disk, which can be loaded into memory quickly.

#### 12. What are common geospatial query types?
**Answer:**
Common geospatial query types include Radius Search (objects within distance X from a point), Bounding Box (objects within a rectangular map area), Polygon/Geofence Search (objects within an arbitrary polygon), and K-Nearest Neighbors (KNN for finding the K closest locations).

#### 13. What are real-world options for fetching nearby businesses in geospatial design?
**Answer:**
Production systems typically leverage existing geospatial databases such as Geohash in Redis or PostgreSQL with the PostGIS extension, rather than building custom spatial indexing trees from scratch.

#### 14. What are the performance limitations of using a basic relational database for a real-time leaderboard with millions of rows?
**Answer:**
Calculating exact ranks dynamically over millions of rows requires sorting continuously changing data, leading to slow queries (taking 10s of seconds). Relational databases are not performant for real-time ranking under high write/read loads, and caching is ineffective due to constant data mutation.

#### 15. What are the two main architectural paradigms for OLTP storage engines?
**Answer:**
1. The log-structured school: Only permits appending to files and deleting obsolete files, never updating written files in place. Examples include Bitcask, SSTables, LSM-trees, LevelDB, Cassandra, HBase, and Lucene.
2. The update-in-place school: Treats the disk as a set of fixed-size pages that can be overwritten. B-trees are the primary example, used in all major relational databases and many non-relational ones.

#### 16. What are the two phases in Two-Phase Locking (2PL)?
**Answer:**
1. Growing/Expanding phase: Locks are acquired, but none are released.
2. Shrinking/Contracting phase: Locks are released, but none are acquired.
This protocol ensures serializability in database transactions.

#### 17. What are three common compression techniques used in storage systems?
**Answer:**
1. Dictionary Encoding: Replaces repeating words or phrases with shorter dictionary indexes.
2. Run-Length Encoding (RLE): Replaces sequential repeating data values with a single value and a count.
3. Delta Encoding: Stores the difference (delta) between consecutive data points rather than absolute values.

#### 18. What data model did the historical Information Management System (IMS) use?
**Answer:**
IMS used the hierarchical model, representing all data as a tree of records nested within records, similar to modern JSON document databases.

#### 19. What is a Phantom Read in database transactions?
**Answer:**
Phantom reads occur when a transaction re-executes a query returning a set of rows that satisfy a search condition and finds that the set of rows has changed due to another transaction inserting or deleting rows.

#### 20. What is a concatenated index and how does it work?
**Answer:**
A concatenated (multi-column) index combines several fields into a single key by appending one column to another in a specified order (e.g., (lastname, firstname)). Due to its sort order, it can efficiently find records matching the prefix (e.g., all people with a particular last name or exact combination), but it is useless for queries that filter only by trailing columns (e.g., searching strictly by firstname).

#### 21. What is a covering index (or index with included columns)?
**Answer:**
A covering index is an index that contains all the fields and columns required to process a specific query (storing a compromise between full row data and simple row references). This allows the database engine to satisfy the query entirely from the index structure without needing to perform a random I/O lookup on the actual table data.

#### 22. What is a dirty read in database transactions?
**Answer:**
A concurrency anomaly (Isolation level: Read Uncommitted) where a transaction reads data that has been modified by another concurrent, uncommitted transaction. If the modifying transaction subsequently rolls back, the reading transaction has processed invalid data.

#### 23. What is block storage?
**Answer:**
Block storage presents raw storage blocks (like HDDs, SSDs, or network-attached storage via Fibre Channel/iSCSI) to a server as a volume. It is the most flexible storage form: the server can format it as a file system or hand control directly to applications like databases or hypervisors for maximum performance.

#### 24. What is resharding data and when is it required?
**Answer:**
Resharding is the process of redistributing data across database partitions. It is required when: 1) A single shard can no longer hold growing data volume, or 2) Shard exhaustion occurs faster on certain nodes due to uneven data distribution. It involves updating the sharding function and migrating data, often solved using consistent hashing.

#### 25. What is the branching factor in a B-tree?
**Answer:**
The branching factor is the number of references to child pages in one page of a B-tree. In practice, it depends on the space required to store page references and range boundaries, but is typically several hundred.

#### 26. What is the difference between schema-on-write and schema-on-read databases?
**Answer:**
Schema-on-write is the traditional relational database approach where an explicit schema is enforced during data insertion. Schema-on-read (often found in document/schemaless databases) lacks an enforced database schema, meaning data structure is implicit and interpreted by the application code at read time.

#### 27. What limitations do standard database indexes have regarding query types?
**Answer:**
Standard indexes assume exact data and allow querying for exact key values or ranges with a sort order. They do not support fuzzy queries or searching for similar keys (such as misspelled words), which require different techniques.

#### 28. What techniques can be used to optimize the storage footprint of time-series metrics data?
**Answer:**
Metrics storage costs can be optimized using efficient data encoding schemes, compression algorithms, downsampling (aggregating older high-frequency data into lower-resolution intervals), and migrating stale historical data to cheaper cold storage tiers.

#### 29. Which data model works most naturally for highly interconnected data?
**Answer:**
Graph models. While document models are awkward and relational models are acceptable, graph models naturally represent complex, highly interconnected relationships between data items.

#### 30. Which database systems support both OLAP and OLTP workloads?
**Answer:**
Some databases, such as Microsoft SQL Server and SAP HANA, support both transaction processing (OLTP) and data warehousing (OLAP) within the same product. However, they are increasingly implemented as two separate storage and query engines accessible through a common SQL interface.

#### 31. Which file format is most efficient for log-based and hash-table-based storage indexes?
**Answer:**
Binary format. It is faster and simpler than formats like CSV because it encodes the length of a string in bytes followed by the raw string, avoiding the need for string escaping.

#### 32. Why are materialized views rarely used in OLTP databases?
**Answer:**
Materialized views are denormalized copies of data that must be updated synchronously or asynchronously when the underlying data changes. These updates make write operations significantly more expensive, which hurts OLTP performance.

#### 33. Why are schema changes considered difficult in relational databases, and how do different databases handle ALTER TABLE?
**Answer:**
Schema changes have a reputation for being slow and causing downtime, though this is not entirely deserved. Most relational database systems execute the ALTER TABLE statement in a few milliseconds. However, MySQL is a notable exception: it copies the entire table on ALTER TABLE, which can mean minutes or even hours of downtime when altering a large table, although various tools exist to work around this limitation.

#### 34. Why do SSTables eliminate the need to keep an in-memory index of all keys?
**Answer:**
Because SSTables store keys in sorted order, engines can maintain a sparse index of boundary keys (offsets) and perform a quick binary search jump, followed by a localized linear scan to find the exact key without needing every key indexed in RAM.

#### 35. Why should application developers understand how databases handle storage and retrieval internally?
**Answer:**
Understanding storage engine internals (e.g., transactional vs. analytical optimizations) is crucial for selecting the appropriate storage engine for your application and tuning it to perform well under specific workloads.


### 🔴 Senior Level

#### 1. Describe the read path in distributed LSM-tree or key-value caches.
**Answer:**
When a read request hits a node, the system first checks the in-memory cache. If missing, it checks a Bloom filter to efficiently determine which on-disk SSTables might contain the key, avoiding unnecessary disk reads. If the Bloom filter indicates potential presence, the corresponding SSTables are queried to retrieve the data, which is then returned to the client.

#### 2. How do LSM-trees and B-trees compare in terms of write throughput, read performance, and disk mechanics?
**Answer:**
- **Writes**: LSM-trees generally sustain higher write throughput. They have lower write amplification under certain configurations and perform sequential writes of compact SSTable files rather than random page overwrites, making them vastly superior on magnetic drives.
- **Reads**: B-trees are typically faster for reads. LSM-tree reads must check multiple data structures and SSTables across compaction stages, though performance heavily depends on workloads.

#### 3. How do bitmap indexes work, and how are sparse bitmaps handled?
**Answer:**
A column with n distinct values is transformed into n separate bitmaps (one bit per row: 1 if the row contains the value, 0 otherwise). For columns with many distinct values, bitmaps become sparse (mostly zeros) and are optimized using run-length encoding for compact storage.

#### 4. How do column-oriented databases overcome row-oriented bottlenecks for analytical workloads?
**Answer:**
Column stores minimize disk-to-memory bandwidth bottlenecks and optimize CPU cache utilization. By keeping compressed column chunks in L1 cache, query engines execute tight loops without function calls, reducing branch mispredictions. They leverage vectorized processing and SIMD instructions to operate directly on compressed blocks.

#### 5. How do graph databases differ from the legacy network (CODASYL) model?
**Answer:**
Unlike CODASYL (which restricts record nesting schemas, enforces ordered sets, requires traversing predefined access paths, and uses imperative queries), graph databases allow any vertex to connect to any other, support direct unique ID lookups and indexes, maintain unordered graph elements, and provide declarative query languages like Cypher or SPARQL.

#### 6. How do we mitigate the data imbalance problem when sharding an autocomplete storage service?
**Answer:**
Analyze historical query distribution patterns and deploy a shard map manager with a custom lookup database. Rather than naive alphabetical splits, group high-frequency keys individually (e.g., separate shards for 's' and 'u') while grouping lower-frequency trailing letters together into combined shards.

#### 7. How do we optimize state storage performance in distributed production environments?
**Answer:**
Use local file-based storage such as SQLite or RocksDB instead of network-bound databases for command, event, and state data. RocksDB is ideal due to its Log-Structured Merge-tree (LSM) architecture optimized for high write throughput, paired with an in-memory cache for recent data to ensure fast reads.

#### 8. How does disk access in B-trees compare to LSM-trees?
**Answer:**
B-trees store pages anywhere on disk, leading to potential random disk seeks for range scans unless leaf pages are sequentially laid out (which is hard to maintain). LSM-trees rewrite large storage segments during background compaction, keeping sequential keys close to each other on disk, making sequential range scans more efficient.

#### 9. How does the storage compaction and compression of LSM-trees compare to B-trees?
**Answer:**
LSM-trees compress better and produce smaller files on disk than B-trees. B-tree storage engines leave some disk space unused due to fragmentation (e.g., page splits or rows not fitting). Since LSM-trees are not page-oriented and periodically rewrite SSTables via compaction (such as leveled compaction) to remove fragmentation, they have lower storage overheads.

#### 10. What architectural problems existed with early hierarchical and network database models?
**Answer:**
They required manual access path selection, making query and update code complicated and inflexible. Changing the data model or adding new query paths required extensive rewriting of handwritten database query code.

#### 11. What are the primary use cases and characteristics of a log-structured storage engine like Bitcask?
**Answer:**
Bitcask is well-suited for workloads where values for keys are updated frequently and there are a large number of writes per key, provided that all keys can fit comfortably in RAM. Examples include hit counters or URL play counts.

#### 12. What are the ways of structuring and querying data in graphs?
**Answer:**
There are several related ways of structuring and querying data in graphs: the property graph model (implemented by Neo4j, Titan, and InfiniteGraph) and the triple-store model (implemented by Datomic, AllegroGraph). Declarative query languages include Cypher, SPARQL, and Datalog. Imperative graph query languages include Gremlin, and distributed graph processing frameworks include Pregel.

#### 13. What can happen when write throughput is high and compaction is not configured carefully in SSTable-based storage engines?
**Answer:**
Compaction cannot keep up with incoming writes, causing unmerged segments to grow until disk space runs out. Reads also slow down as they must check more segment files. Standard storage engines do not throttle incoming writes, requiring explicit monitoring.

#### 14. What complexities are introduced by database sharding?
**Answer:**
Data resharding, the celebrity (hotspot) problem, and handling joins and de-normalization.

#### 15. What is a common mistake when scaling a geospatial index?
**Answer:**
A common mistake is jumping straight to a complex sharding scheme without first verifying the dataset size. If the entire index easily fits into the working set/RAM of a modern server (e.g., a quadtree index taking ~1.71GB), sharding for storage is unnecessary. Instead, scale out primarily to handle high read request volume and overcome single-server CPU or network bandwidth bottlenecks.

#### 16. What is a major drawback of the multi-master replication approach?
**Answer:**
IDs do not go up monotonically with time across multiple servers, making global ordering and auto-incrementing challenging without external coordination (e.g., using UUIDs or distributed ID generators).

#### 17. What is the purpose of predicate locks in relational databases?
**Answer:**
Predicate locks prevent phantom reads by locking all rows matching a specific search condition—including rows that do not yet exist in the table but could potentially be inserted by concurrent transactions.

#### 18. What problem arises when using sorted in-memory indexes (memtables) for SSTables, and how is it resolved?
**Answer:**
If the database crashes, recent writes in the memtable are lost. This is resolved by appending every write to an unsorted Write-Ahead Log (WAL) on disk prior to updating the memtable, which is used for crash recovery and discarded after memtable flush.

#### 19. What storage optimization extension did Vertica implement for multi-query optimization?
**Answer:**
Derived from C-Store, Vertica stores the same data sorted in multiple different ways across redundant replica nodes. This allows query execution engines to use the sort order variant that best matches a specific query's access pattern.

#### 20. What underlying engine concerns do real databases deal with beyond simple record storage and retrieval?
**Answer:**
Concurrency control, reclaiming disk space (log compaction/garbage collection), and handling errors and partially written records.

#### 21. What write path steps occur when a write request is directed to a log-structured merge (LSM) storage node?
**Answer:**
1. The write request is appended to an on-disk commit log file for durability.
2. The data is written to an in-memory sorted cache (memtable).
3. When the memory cache reaches a threshold, it is flushed to disk as an immutable Sorted-String Table (SSTable).

#### 22. Which compression technique is particularly effective for repetitive columns in data warehouse column stores?
**Answer:**
Bitmap encoding. The repetitive nature of sorted values in column stores makes them ideal for specialized compression techniques like bitmap indexes.

#### 23. Which database systems and storage engines use a sorted in-memory index with SSTables?
**Answer:**
LevelDB and RocksDB use this algorithm for embedded key-value storage. Similar storage engines are used in Cassandra and HBase, which were inspired by Google’s Bigtable paper (introducing the terms SSTable and memtable).

#### 24. Why are append-only logs preferred over in-place file updates in storage engines?
**Answer:**
Appending and segment merging are sequential write operations, which are much faster than random writes, especially on magnetic spinning disks and SSDs. Concurrency and crash recovery are significantly simpler because you avoid partial writes or corrupted spliced files. Furthermore, merging old segments prevents data file fragmentation over time.

#### 25. Why can property matching syntax be similar in Cypher and SPARQL?
**Answer:**
Because RDF-based graph models do not distinguish between properties and edges, using predicates for both, graph query languages can map property filters using similar predicate-matching syntax (e.g., matching a vertex name property in Cypher vs. SPARQL triples).

#### 26. Why can the LSM-tree algorithm be slow when looking up non-existent keys?
**Answer:**
To confirm a key does not exist, the engine must check the memtable and then traverse all SSTable segments from newest to oldest, potentially causing multiple disk reads. Storage engines optimize this using additional Bloom filters.

#### 27. Why is bounding-box coordinate querying inefficient using separate standard indexes on latitude and longitude?
**Answer:**
A SQL query using `BETWEEN` on latitude and longitude independently requires scanning or hitting multiple indexes and performing a costly dataset intersection. Standard database indexes only optimize search in a single dimension, making multi-dimensional spatial queries inefficient without spatial indices (e.g., Geohash, Quadtrees, R-Trees).

#### 28. Why is it complicated to support pagination for sharded databases?
**Answer:**
Objects are distributed unevenly across shards, causing different shards to return varying counts of matching results. Application code must aggregate and sort results from all shards, track distinct offsets for each shard, and associate those offsets with a complex cursor, making pagination difficult when scaling to hundreds of shards.


## 📂 Category: Databases & Storage Engines (8 cards)

### 🟢 Junior Level

#### 1. How is data storage laid out in OLTP databases versus document databases?
**Answer:**
In most OLTP relational databases, storage is laid out in a row-oriented fashion where all values of a row are stored adjacently. Document databases are similar, storing an entire document as one contiguous sequence of bytes.


### 🟡 Mid Level

#### 1. How does database replication handle failover if a slave or master database goes offline?
**Answer:**
If a slave goes offline, reads temporarily route to the master (or other healthy slaves) until a replacement slave is provisioned. If the master goes offline, a healthy slave is promoted to master (potentially requiring recovery scripts for missing data due to replication lag), and a new slave is spun up for replication.

#### 2. How is disk demand reduced in column-oriented stores?
**Answer:**
By loading only the specific columns required for a query from disk, and applying high-efficiency data compression techniques that column stores naturally facilitate.

#### 3. What happens structurally when an in-memory database (like Redis) is restarted?
**Answer:**
It needs to reload its state from disk (e.g., RDB snapshots or AOF logs) or over the network from a replica. Despite writing to disk for durability and backup advantages, reads are served entirely from memory, and the disk is used merely as an append-only log.

#### 4. When data models feature complex and pervasive many-to-many relationships, which database model becomes most natural to use?
**Answer:**
A graph database model. While relational models handle simple many-to-many relationships via junction tables, highly interconnected networks of data become significantly more performant and natural to model as nodes and edges in a graph.


### 🔴 Senior Level

#### 1. During log-structured storage compaction and merging, what happens when the same key appears across multiple input segments?
**Answer:**
Since adjacent segments are merged and contain values written during specific periods, the values in newer segments supersede older ones. The compaction process keeps the value from the most recent segment and discards duplicate older keys.

#### 2. What are the characteristics and durability models of various in-memory databases?
**Answer:**
- Relational in-memory (VoltDB, MemSQL, Oracle TimesTen): Remove on-disk data structure overheads for high performance.
- RAMCloud: Open-source, in-memory key-value store with strong durability using a log-structured approach for memory and disk.
- Redis & Couchbase: Weak/asynchronous durability by writing to disk asynchronously.

#### 3. What happens at the storage engine level when updating a database value without changing its index key (heap file approach)?
**Answer:**
If the new value is smaller or equal in size, the record is overwritten in place. If the new value is larger, it must be moved to a new location with sufficient space in the heap, requiring either all indexes to be updated to point to the new location or leaving a forwarding pointer behind at the old location.


## 📂 Category: Databases & Transactions (1 cards)

### 🟢 Junior Level

#### 1. What is Durability in ACID transactions?
**Answer:**
Durability guarantees that once a transaction has successfully committed, its changes are permanent and will survive subsequent system failures, power outages, or crashes (typically achieved via write-ahead logging to non-volatile storage).


## 📂 Category: Deployment & CI/CD (1 cards)

### 🟢 Junior Level

#### 1. What is continuous delivery?
**Answer:**
Continuous delivery is the process of deploying code frequently and reliably to production environments.


## 📂 Category: Deployment Strategies (1 cards)

### 🟡 Mid Level

#### 1. Explain Blue-Green deployment
**Answer:**
A deployment strategy where two identical production environments (Blue and Green) are maintained. At any time, one is live (e.g., Blue). Deployment happens on the idle environment (Green), and traffic is switched via a router/load balancer only after verification, enabling zero-downtime and instant rollbacks.


## 📂 Category: DevOps & Engineering Practices (1 cards)

### 🟡 Mid Level

#### 1. Why is automation important in large-scale system design?
**Answer:**
As systems scale in complexity, automation (such as continuous integration, automated builds, tests, and deployments) is critical to catch defects early, ensure code health, and maintain high developer productivity.


## 📂 Category: DevOps & Infrastructure (2 cards)

### 🟢 Junior Level

#### 1. How do containerization and container orchestration work and improve deployment?
**Answer:**
Containerization packages an application and its dependencies into a single lightweight unit that runs in an isolated user space, ensuring consistency across environments. Container orchestration (e.g., Kubernetes) automates the deployment, scaling, networking, and lifecycle management of these containers across cluster nodes.


### 🟡 Mid Level

#### 1. How does Docker Compose differ from Kubernetes?
**Answer:**
Docker Compose is a tool for defining and running multi-container Docker applications on a single host using a YAML file, ideal for local development. Kubernetes is a production-grade container orchestrator designed to manage distributed container workloads across a cluster of multiple nodes with features like self-healing, auto-scaling, and rolling updates.


## 📂 Category: Disaster Recovery (1 cards)

### 🟡 Mid Level

#### 1. What are RPO (Recovery Point Objective) and RTO (Recovery Time Objective)?
**Answer:**
RPO refers to the maximum acceptable amount of data loss measured in time (loss tolerance) before significant business harm occurs. RTO refers to the maximum acceptable duration of time an application can be down during an outage without causing severe business damage.


## 📂 Category: Distributed Algorithms (2 cards)

### 🟡 Mid Level

#### 1. What specific hash function is commonly used in consistent hashing examples?
**Answer:**
SHA-1 is typically used as the hash function for consistent hashing rings.


### 🔴 Senior Level

#### 1. What distinguishes the hash function used in consistent hashing from standard rehashing problems?
**Answer:**
Consistent hashing uses a distributed hash space (e.g., a ring) and maps both servers and keys to this space without requiring the traditional modulo operation (`key % N`), which prevents massive key re-mappings when nodes are added or removed.


## 📂 Category: Distributed Architecture (21 cards)

### 🟢 Junior Level

#### 1. What are the pros and cons of generating IDs independently on each web server?
**Answer:**
Pros:
- Simple to generate (e.g., UUIDs). No coordination or synchronization needed between servers, making scaling trivial.
Cons:
- IDs are large (128 bits), do not guarantee chronological ordering (do not go up with time), and can be non-numeric.


### 🟡 Mid Level

#### 1. Describe the parallel metadata update workflow during video file uploads in a streaming service.
**Answer:**
While a media file is streaming/uploading to primary object storage, the client concurrently sends a metadata request containing parameters like filename, size, and format to the API servers, which subsequently update both the metadata cache and relational/NoSQL database.

#### 2. How did the cryptocurrency industry and technologies like AMMs impact stock exchange systems?
**Answer:**
Many crypto exchanges deploy services on cloud infrastructure, lowering the entry threshold. Some decentralized finance projects use Automated Market Making (AMM), eliminating the need for traditional order books and injecting innovative architectural patterns into financial systems.

#### 3. How do traditional message queues and modern event streaming platforms compare?
**Answer:**
Platforms like Apache Kafka and Pulsar are event streaming platforms utilizing append-only logs, whereas systems like RabbitMQ and ActiveMQ are traditional message queues. However, feature convergence is high: RabbitMQ supports streaming features and log retention, while Pulsar functions efficiently as both an event stream and a distributed message queue.

#### 4. How do you determine which server a key is stored on in consistent hashing versus virtual nodes?
**Answer:**
In standard consistent hashing, traverse clockwise from the key's position on the hash ring until the first server is found. When using virtual nodes, traverse clockwise from the key's location and find the first virtual node encountered, which maps back to a physical server to ensure better load balancing.

#### 5. What are the consistency and availability trade-offs in a distributed email system?
**Answer:**
Distributed databases relying on replication for high availability must choose between consistency and availability (CAP theorem). Email systems prioritize correctness and consistency by design, utilizing a single primary node for any given mailbox. During a failover event, the mailbox becomes inaccessible to clients, pausing sync/update operations to trade availability in favor of strong consistency.

#### 6. What are the core differences between online (services), offline (batch), and near real-time (streaming) systems?
**Answer:**
Online systems respond rapidly to real-time client requests prioritizing availability and low latency. Offline (batch) systems process unbounded historical data with finite boundaries to produce views/metrics optimizing throughput. Streaming systems process infinite input streams near-real-time to maximize data ingestion throughput and minimize processing latency.

#### 7. What are the core trade-offs of the 'fanout on write' (write-amplification) model in a news feed architecture?
**Answer:**
Pros: News feed is pre-computed in real-time and pushed to friends immediately, making reads extremely fast. Cons: The 'hotkey problem' occurs when users with massive follower counts require extensive CPU and time to generate feeds; additionally, pre-computing feeds for inactive users wastes storage and compute resources.

#### 8. What are the pros and cons of asynchronous communication in microservices architectures?
**Answer:**
Pros: Decouples services, acts as a buffer for traffic spikes, improves availability and fault isolation. Supports both single-receiver patterns (shared queues where messages are removed once consumed, e.g., standard queues) and multiple-receiver patterns (publish-subscribe logs like Kafka where the same message is processed by multiple downstream services like analytics, billing, and notifications without removal upon first read).
Cons: Introduces eventual consistency, complicates error handling and distributed tracing, and requires managing broker availability and message ordering.

#### 9. What are the pros and cons of calculating server indexes using modular division?
**Answer:**
Pros:
- Works well when the server pool size is fixed and data distribution is even.
Cons:
- Causes massive cache misses and key remapping when servers are added or removed, as changing the pool size alters the modular calculation results for almost all keys.

#### 10. What are the pros and cons of synchronous communication (e.g., HTTP) between services?
**Answer:**
Pros: Simple to implement, intuitive request-response cycle, works well for small-scale systems.
Cons: Low performance (blocked chains impact total system latency), poor failure isolation (downstream dependency failures cascade to clients), tight coupling (sender must know the recipient), and hard to scale without buffering layers.

#### 11. What are the pros and cons of using ticket servers for distributed ID generation?
**Answer:**
Pros:
- Produces sequential numeric IDs; easy to implement for small-to-medium scale applications.
Cons:
- Single point of failure (SPOF). If the ticket server goes down, dependent systems fail. Setting up multiple ticket servers introduces data synchronization challenges.

#### 12. What storage technology and commands are commonly used to implement rate limiter counters?
**Answer:**
An in-memory cache like Redis is chosen due to its fast access times and support for time-based expiration. Redis offers two primary commands for this purpose: `INCR` (to increment the stored counter by 1) and `EXPIRE` (to set a time-to-live timeout after which the counter is automatically deleted).

#### 13. Where should rate limiters be placed in a distributed system architecture?
**Answer:**
Rate limiters can be placed on the client-side (unreliable because clients can be spoofed or bypassed), directly on the API servers, or via a dedicated rate limiter middleware/proxy layer that intercepts and throttles requests before they reach core backend services.

#### 14. Which configuration of the CAP theorem cannot exist in real-world distributed systems?
**Answer:**
CA (Consistency and Availability without Partition Tolerance). In real-world distributed systems, network partitions are inevitable; therefore, a system must choose between Consistency (CP) or Availability (AP) when a partition occurs.


### 🔴 Senior Level

#### 1. Does erasure coding impact data durability in distributed storage systems?
**Answer:**
Yes. Erasure coding provides high space efficiency compared to simple replication while drastically increasing data durability (e.g., achieving up to '11 nines' of durability based on standard annual hardware failure rates).

#### 2. How do you architect email full-text search using Elasticsearch, and how do you keep the primary store in sync?
**Answer:**
Group underlying documents to specific Elasticsearch nodes using `user_id` as the partition key. Because search operations are synchronous while mutations (send/receive/delete) require background reindexing, use an asynchronous event broker like Kafka to decouple the email store mutations from the search index workers.

#### 3. How do you handle component failures in a distributed cloud storage architecture?
**Answer:**
Load Balancers failover via secondary heartbeats; Block servers reassign jobs; S3 Cloud storage uses multi-region replication; API servers are stateless and traffic is re-routed; Metadata caches are replicated; DB Master failures trigger replica promotion; Notification long-poll connections automatically reconnect to alternate alive servers; Queues use redundant backups.

#### 4. What are the architectural trade-offs across different digital wallet design iterations?
**Answer:**
1) In-memory key-value stores (e.g., Redis) provide high performance but lack durability. 2) Transactional databases with protocols like 2PC, TC/C, or Saga ensure ACID properties across nodes but make data auditing complex. 3) Event sourcing storing commands, events, and states locally, replicated via Raft consensus and exposed via CQRS with a reverse proxy, provides high reliability, auditability, and low-latency reads/writes.

#### 5. What are the core concepts of Event Sourcing: Commands, Events, and State?
**Answer:**
- Command: An intended action from the outside world (an intention, not a fact). Commands must be validated and are typically processed through a FIFO queue.
- Event: The immutable record of the successful fulfillment of a validated command.
- State: The derived result updated when an event is applied (e.g., account balances stored in a key-value store or relational DB).

#### 6. What are the issues of the basic consistent hashing approach?
**Answer:**
The basic consistent hashing approach suffers from two main problems: 1) Partition size inequality, where adding or removing a server leads to uneven hash space partitions (some very small, some twice as large as adjacent ones). 2) Non-uniform key distribution, which can cause hot spots where most keys cluster onto a single server while others receive no data.


## 📂 Category: Distributed Batch Processing (3 cards)

### 🟢 Junior Level

#### 1. Explain the basic components of MapReduce
**Answer:**
MapReduce consists of a JobTracker/Master node and multiple TaskTracker/Worker nodes. The core phases are: 1) Input Reader, which splits data into logical chunks; 2) Map function, which processes chunks and emits key-value pairs; 3) Shuffle and Sort, which aggregates and routes keys to appropriate reducers across the network; and 4) Reduce function, which aggregates values per key and writes the final output to persistent storage.


### 🟡 Mid Level

#### 1. Explain the concept of data locality in batch processing
**Answer:**
Data locality is an optimization technique in distributed storage and compute frameworks (like Hadoop/HDFS and YARN) where computation (tasks/mappers) is scheduled on the exact physical node or rack where the required data blocks reside. This drastically reduces network I/O congestion and bandwidth bottlenecks by avoiding moving massive datasets across the network to compute nodes.


### 🔴 Senior Level

#### 1. Explain the difference between map-side and reduce-side joins
**Answer:**
A map-side join (broadcast join) is used when one dataset is small enough to fit in memory; the mapper loads the small dataset and joins it locally against streaming/chunked partitions of the large dataset, avoiding network shuffle. A reduce-side join is used when both datasets are large; both datasets are tagged, shuffled across the network based on join keys, and grouped together in the reduce phase.


## 📂 Category: Distributed Caching (4 cards)

### 🟡 Mid Level

#### 1. How is high performance and scalability guaranteed for the Redis Pub/Sub cluster in a nearby friends application?
**Answer:**
Channels are completely independent of one another. This allows horizontal scaling and sharding of channels across hundreds of Redis servers based on the publisher's user ID.

#### 2. Why is Redis an optimal choice for storing user location data in a 'nearby friends' tracking application?
**Answer:**
Location tracking requires only the current transient state per user. Redis offers ultra-fast read/write operations and native TTL (Time-To-Live) support to automatically purge inactive users. Data durability is unnecessary; if the Redis instance crashes, it can be replaced with an empty instance and repopulated as fresh location updates stream in.


### 🔴 Senior Level

#### 1. What is the hot-key problem in distributed caching and storage?
**Answer:**
The hot-key problem occurs when a small subset of keys (e.g., viral posts, celebrity profiles) receives a disproportionately massive volume of read or write requests compared to other keys. This overwhelms a single cache node or database partition, causing bottlenecks, high latency, and potential cascading failures.

#### 2. Why should a distributed Redis Pub/Sub cluster be treated as stateful rather than stateless despite messages being ephemeral?
**Answer:**
While messages passing through channels are transient (not persisted and dropped if there are no subscribers), the pub/sub servers maintain vital state: the subscriber list for each channel. If a channel moves due to node scaling or hash ring adjustments, subscribers must be coordinated to unsubscribe from the old server and resubscribe to the new one. Scaling requires careful planning and over-provisioning to avoid service interruptions.


## 📂 Category: Distributed Caching & Pub-Sub (1 cards)

### 🔴 Senior Level

#### 1. What are the potential scaling issues and mitigation strategies when resizing distributed Redis Pub/Sub clusters?
**Answer:**
Resizing shifts channels across the hash ring, triggering mass resubscription storms via service discovery updates, which can cause clients to drop location updates. Mitigation: Execute cluster resizing operations during off-peak hours.


## 📂 Category: Distributed Caching & Sharding (2 cards)

### 🟡 Mid Level

#### 1. What happens to the number of redistributed keys when a server is added or removed using consistent hashing?
**Answer:**
Only a small fraction (specifically, $K/N$ where $K$ is the total number of keys and $N$ is the number of servers) of keys need to be redistributed, rather than rehashing all keys as in traditional modulo hashing.

#### 2. What happens to the standard deviation of key distribution as the number of virtual nodes increases in consistent hashing?
**Answer:**
The standard deviation gets smaller, leading to a much more balanced and uniform distribution of keys across physical servers/nodes.


## 📂 Category: Distributed Computing (4 cards)

### 🟡 Mid Level

#### 1. Explain micro-batch processing
**Answer:**
A hybrid data processing approach that treats streaming data as a sequence of very small, time-bounded batches (e.g., every few seconds). It bridges the gap between low-latency streaming and high-throughput batch processing frameworks (like Spark Streaming).

#### 2. What are RDDs (Resilient Distributed Datasets) in Apache Spark?
**Answer:**
RDDs are the fundamental fault-tolerant, immutable collections of records partitioned across cluster nodes in Apache Spark, enabling parallel distributed processing with lineage tracking for recomputation on failure.


### 🔴 Senior Level

#### 1. Explain Spark's DAG (Directed Acyclic Graph) execution
**Answer:**
Apache Spark builds a DAG of stages and tasks for every RDD/DataFrame transformation job before execution. It optimizes execution plans by grouping operations into pipelined stages (narrow vs. wide transformations) and skipping intermediate disk writes where possible.

#### 2. Explain broadcast joins in Spark
**Answer:**
An optimization technique in Apache Spark where a small dataset/DataFrame is broadcasted (copied) to all worker nodes in the cluster. This avoids expensive shuffle operations by allowing each node to perform a local map-side join with its partition of the large dataset.


## 📂 Category: Distributed Consensus (5 cards)

### 🔴 Senior Level

#### 1. Explain the leader election process in the Raft consensus algorithm.
**Answer:**
The leader sends periodic heartbeat messages (AppendEntries) to followers. If a follower stops receiving heartbeats and its election timeout expires, it increments its term, becomes a candidate, and sends RequestVote RPCs to other nodes. If it receives a majority of votes, it becomes the new leader. If multiple followers time out simultaneously, a 'split vote' occurs, triggering a new election timeout.

#### 2. Explain the term 'safety' in consensus protocols.
**Answer:**
In distributed consensus protocols (like Paxos or Raft), 'safety' refers to the guarantee that 'nothing bad happens'. Specifically, it means that nodes never return an incorrect result or violate system invariants. For example, safety ensures that two different leaders are not elected for the same term, and that committed log entries are never lost or corrupted across node failures.

#### 3. How do we use the Raft algorithm to guarantee reliability in event sourcing?
**Answer:**
Set up multiple event sourcing nodes (e.g., 3 nodes) using the Raft consensus algorithm to synchronize the event list reliably. The leader takes incoming command requests, converts them into events, appends them locally, and uses Raft to replicate the new events to followers. All nodes process the event list to update their state deterministically, eliminating single points of failure.

#### 4. How does Raft differ fundamentally from Paxos?
**Answer:**
Raft is explicitly designed for understandability and decomposes consensus into explicit, independent sub-problems: leader election, log replication, and safety. Paxos models consensus around agreeing on a single value through unconstrained round-trips (Basic Paxos) or multi-decree variants, making it notoriously difficult to implement correctly in practical systems.

#### 5. What is the split-brain problem in distributed replication?
**Answer:**
A failure scenario in partitioned or leader-based distributed systems where network partitions isolate nodes into separate groups, causing two nodes to independently assume they are the active leader, leading to conflicting writes, data divergence, and loss of consistency.


## 📂 Category: Distributed Consensus & Protocols (1 cards)

### 🟡 Mid Level

#### 1. What does each node maintain locally when participating in a Gossip protocol?
**Answer:**
Each node maintains a membership list containing peer member IDs and their corresponding heartbeat counters to detect failures and propagate cluster state.


## 📂 Category: Distributed Consistency (1 cards)

### 🔴 Senior Level

#### 1. How does lease-based consistency work in distributed systems?
**Answer:**
A lease is a time-bound grant of authority issued by a designated coordinator or consensus group to a node. The node holding the lease can serve reads or execute writes locally without checking in with the cluster, guaranteed that no conflicting operation will be committed until the lease expires. This optimizes read performance and reduces coordination overhead.


## 📂 Category: Distributed Data Processing (2 cards)

### 🟡 Mid Level

#### 1. How does the shuffling phase work in MapReduce?
**Answer:**
The shuffle phase acts as the bridge between the map and reduce tasks. It collects the intermediate key-value outputs produced by all map nodes, partitions them by key, sorts them, and transfers (network transport) the grouped data to the designated reduce nodes so that all values for a given key arrive at the same reducer.


### 🔴 Senior Level

#### 1. What is MapReduce?
**Answer:**
MapReduce is a distributed programming model designed for processing massive datasets in parallel across a cluster of machines. It consists of a map phase (filtering and transforming) and a reduce phase (aggregating). Some NoSQL datastores (e.g., MongoDB, CouchDB) use a limited form of MapReduce for read-only queries across unstructured documents.


## 📂 Category: Distributed Data Structures (1 cards)

### 🟡 Mid Level

#### 1. What are the high-level design options for generating unique IDs in distributed systems?
**Answer:**
1. Multi-master replication
2. Universally unique identifier (UUID)
3. Ticket server
4. Twitter Snowflake approach


## 📂 Category: Distributed Databases (9 cards)

### 🟡 Mid Level

#### 1. How does multi-master replication handle ID generation using the auto_increment offset strategy?
**Answer:**
Using the auto_increment feature, each of the $k$ database servers increments IDs by $k$ instead of 1 (e.g., Server 1 generates 1, 3, 5; Server 2 generates 2, 4, 6). While this prevents collisions, it struggles to scale across multiple data centers, does not guarantee monotonically increasing timestamps globally, and fails to handle dynamic cluster scaling easily.

#### 2. What is replication lag?
**Answer:**
The delay between writing data to a primary/leader database and that data becoming visible on read replicas in an asynchronous or semi-synchronous replication setup, which can lead to eventual consistency issues like 'read-after-write' inconsistencies.

#### 3. What mechanism guarantees consistency for both read and write operations using replicas?
**Answer:**
Quorum consensus, defined by the formula R + W > N (where N is replication factor, R is read quorum, and W is write quorum).

#### 4. Why does the auto_increment primary key attribute fail in distributed database systems?
**Answer:**
A traditional auto_increment relies on a single database server to guarantee sequentially increasing unique IDs. In a distributed environment, a single server is insufficient for scale, and coordinating unique ID generation across multiple independent database nodes with minimal latency is extremely challenging.


### 🔴 Senior Level

#### 1. Explain the CAP theorem implications for specialized stores
**Answer:**
The CAP theorem states that a distributed data store can simultaneously provide at most two of three guarantees: Consistency (linearizability), Availability, and Partition tolerance. Since network partitions are inevitable in distributed systems, architects must choose between CP (consistency over availability during splits, e.g., HBase, etcd) or AP (high availability with eventual consistency, e.g., Cassandra, DynamoDB) depending on the business requirements of the specialized store.

#### 2. What is guaranteed in a distributed database when W + R > N?
**Answer:**
Strong consistency is guaranteed (where W is the write quorum, R is the read quorum, and N is the replication factor), ensuring that read operations will always overlap with the most recent write operation.

#### 3. What is strong consistency in distributed data stores?
**Answer:**
Strong consistency (often linearizability) guarantees that any read operation executed on any node will return the value of the most recent write, regardless of which replica the reader connects to. It requires synchronous coordination (e.g., via consensus protocols like Raft or Paxos) before acknowledging writes, trading off higher write latency and reduced availability during partitions for absolute correctness.

#### 4. What mechanism is used to achieve data consistency in a distributed database when a server is temporarily unavailable?
**Answer:**
Hinted handoff is used, where another node temporarily accepts writes meant for the unavailable node and hands them over once it recovers.

#### 5. What protocol is used to keep database replicas in sync when a replica is permanently or semi-permanently unavailable/diverged?
**Answer:**
Anti-entropy protocol, which uses cryptographic hashes (like Merkle trees) to compare datasets across replicas and sync missing or outdated records.


## 📂 Category: Distributed Messaging (5 cards)

### 🟢 Junior Level

#### 1. What are the most popular distributed message queues and messaging models?
**Answer:**
Popular message queues include Apache Kafka, RabbitMQ, and Apache Pulsar. The two fundamental messaging models are Point-to-Point (queues) and Publish-Subscribe (topics).


### 🟡 Mid Level

#### 1. What are the functional requirements for a distributed message queue?
**Answer:**
Producers send messages; consumers pull or push consume messages; messages can be consumed repeatedly or exactly once depending on configuration; historical data can be truncated; message sizes are typically in the kilobyte range; FIFO (First-In-First-Out) ordering delivery where possible; configurable delivery semantics (at-least-once, at-most-once, exactly-once).

#### 2. What are the non-functional requirements for a distributed message queue?
**Answer:**
1. High throughput or low latency (configurable based on use cases).
2. Scalability: Distributed nature capable of handling sudden volume surges.
3. Persistence and durability: Data must be persisted to disk and replicated across multiple nodes.


### 🔴 Senior Level

#### 1. How should a distributed architecture handle failover and recovery of Redis Pub/Sub servers in real-time messaging systems?
**Answer:**
1. Monitoring software detects node failure and alerts the on-call operator.
2. The operator updates the consistent hash ring key in the service discovery layer, swapping the dead node (e.g., p_1) with a fresh standby node (p1_new).
3. WebSocket servers are notified of the topology change via service discovery.
4. Each WebSocket connection handler checks its internal list of active subscriptions against the updated hash ring and automatically re-subscribes affected channels to the new Pub/Sub server node.

#### 2. What foundational features and delivery guarantees must be scoped when designing a modern distributed message queue?
**Answer:**
1. Message Format/Size: Text-only payloads, typically in the kilobyte (KB) range.
2. Consumption Model: Support for multiple, repeated consumption by distinct consumers (extending beyond traditional single-delivery queues).
3. Ordering: Strict FIFO delivery order guarantees.
4. Persistence: Data retention capabilities (e.g., 2 weeks).
5. Throughput & Latency: High throughput for log aggregation and low latency for standard messaging use cases.
6. Delivery Semantics: Configurable support for at-most-once, at-least-once, and exactly-once processing semantics.


## 📂 Category: Distributed Messaging & Communication (2 cards)

### 🟡 Mid Level

#### 1. What are the primary architectural flaws of a monolithic notification system?
**Answer:**
- Single Point of Failure (SPOF): A single notification service instance risks total outage.
- Scaling Bottlenecks: Inability to scale databases, caches, and processing pipelines independently.
- Resource Contention: Heavy tasks like HTML generation and synchronous third-party API calls block execution flows and overload the system during peak hours.


### 🔴 Senior Level

#### 1. What are the key architectural considerations (fault tolerance, compliance, security, optimizations) when designing a distributed email system?
**Answer:**
- Fault tolerance: Handle node failures, network issues, and event delays.
- Compliance: GDPR compliance for Personally Identifiable Information (PII) from Europe, plus legal intercept support.
- Security: Phishing protection, safe browsing, proactive alerts, account safety, confidential mode, and email encryption.
- Optimizations: De-duplicate file attachments in object storage (e.g., Amazon S3) by checking existence before saving.


## 📂 Category: Distributed Messaging & Streaming (2 cards)

### 🔴 Senior Level

#### 1. How do you architect a multi-stage Kafka message queue pipeline for an ad click aggregator?
**Answer:**
Decouple log watchers, aggregation services, and databases using intermediate message queues: 1) The first queue stores raw ad click events with attributes (ad_id, click_timestamp, user_id, ip, country). 2) The aggregation service processes these and pushes to a second queue containing pre-aggregated metrics: per-minute ad click counts (ad_id, click_minute, count) and top-N most clicked ads per minute (update_time_minute, most_clicked_ads). A database writer polls the second queue to persist records.

#### 2. How do you scale message streaming throughput when the data volume in a topic exceeds a single server's capacity?
**Answer:**
Use partitioning (sharding). Divide a topic into ordered, FIFO-based partitions distributed across multiple servers (brokers). Producers route messages via keys to specific partitions, and consumer groups scale out by consuming subsets of partitions in parallel.


## 📂 Category: Distributed Processing (6 cards)

### 🟡 Mid Level

#### 1. How do we aggregate ad click events using MapReduce?
**Answer:**
Input events are partitioned by ad_id (using a modulo operation like ad_id % 3) in Map nodes and are then aggregated by downstream Aggregation nodes.

#### 2. Is MapReduce considered a declarative query language or an imperative query API?
**Answer:**
MapReduce is neither fully declarative nor fully imperative; it sits in between, expressing query logic via snippets of code (map and reduce functions) repeatedly invoked by the processing framework.

#### 3. What are the functional restrictions imposed on Map and Reduce functions in distributed data processing?
**Answer:**
Map and Reduce functions must be pure functions: they can only use explicitly passed input data, cannot perform additional database queries, and must not have side effects. These constraints enable databases or distributed engines (like MapReduce frameworks) to execute functions anywhere, in any order, and safely retry them upon failure.

#### 4. What is an aggregate node in stream processing or MapReduce?
**Answer:**
An Aggregate node counts ad click events by ad_id in memory every minute. In the MapReduce paradigm, the Aggregate node typically functions as part of the Reduce step, transforming the process into a map-aggregate-reduce (or map-reduce-reduce) pipeline.


### 🔴 Senior Level

#### 1. What is a reduce node in distributed computing and MapReduce?
**Answer:**
A Reduce node reduces aggregated results from all 'Aggregate' nodes into a final result. In the DAG model representing the MapReduce paradigm, it processes big data using parallel distributed computing. Intermediate data can be stored in memory, and nodes communicate via TCP (different processes) or shared memory (different threads).

#### 2. What is speculative execution in MapReduce?
**Answer:**
Speculative execution is a fault tolerance optimization where the framework launches duplicate tasks (speculative tasks) for tasks that are running slower than average, helping to mitigate straggler nodes and reduce overall job completion time.


## 📂 Category: Distributed Storage (17 cards)

### 🟢 Junior Level

#### 1. What are the scaling limitations of a single-server key-value store and how can they be mitigated?
**Answer:**
Single-server K-V stores typically use an in-memory hash table. Limitations include physical memory constraints. Optimizations include data compression and storing only frequently accessed data in memory while keeping the rest on disk. Beyond this, a distributed key-value store is required.


### 🟡 Mid Level

#### 1. How do block, file, and object storage categories compare?
**Answer:**
Block storage provides high/very high performance, strong consistency, SAS/iSCSI/FC access, and medium scalability, making it ideal for VMs and databases. File storage offers medium-to-high performance, strong consistency, standard access (CIFS/SMB/NFS), and high scalability. Object storage offers low-to-medium performance, strong consistency, RESTful API access, and vast scalability for unstructured binary data, supporting object versioning instead of in-place updates.

#### 2. How do clients detect file additions or modifications made by other clients in a distributed file synchronization service?
**Answer:**
If a client is online during a modification, a notification service alerts it to pull the latest updates. If offline, changes are cached and pulled upon reconnecting. Once aware of a change, the client fetches metadata via API servers and downloads blocks to construct the file.

#### 3. What are the core components in the high-level design of an object storage system?
**Answer:**
Components include: (1) Load Balancer for distributing RESTful API requests, (2) Stateless API Service orchestrating remote procedure calls, (3) Identity and Access Management (IAM) for authentication/authorization, (4) Data Store for object binaries (referenced via UUID), and (5) Metadata Store for object details.

#### 4. What are the three main types of storage systems in distributed computing?
**Answer:**
1. File Systems
2. Block Storage
3. Object Storage

#### 5. What is the optimized data storage write flow in an append-only object storage node?
**Answer:**
1. API service sends a request to save a new object ('object 4'). 2. The data node service appends 'object 4' sequentially to the end of the active read-write data file (e.g., `/data/c`). 3. A new metadata record mapping 'object 4' is inserted into the `object_mapping` table. 4. The data node service returns the generated UUID back to the API service.

#### 6. What is the step-by-step workflow for downloading an object from an S3-like object storage using logical folder hierarchies?
**Answer:**
1. Client sends an HTTP GET request (e.g., `GET /bucket-to-share/script.txt`). 2. API service queries IAM to verify READ access to the bucket. 3. API service queries the metadata store to resolve the object name to its underlying UUID (object_id). 4. API service fetches the raw object data from the data store using the UUID. 5. API service returns the object data in the HTTP GET response.


### 🔴 Senior Level

#### 1. Compare data replication and erasure coding in terms of storage efficiency and performance.
**Answer:**
Replication provides high write performance and low compute overhead, but incurs high storage cost (e.g., 200% overhead for 3x copies) and lower durability (e.g., 6 nines). Erasure coding (such as Reed-Solomon) divides data into data and parity chunks, achieving high durability (e.g., 11 nines) with low storage overhead (e.g., 50%), but increases write latency and CPU usage due to parity calculations, and slows down recovery reads during failures.

#### 2. Describe the consistency and replication trade-offs in distributed data storage flows.
**Answer:**
In distributed storage, a placement service uses consistent hashing deterministically to map an object UUID to a replication group. For persistence and consistency, choices include: 1) Strong consistency: The primary node replicates data to all secondary nodes before returning a response, ensuring maximum consistency at the highest latency cost. 2) Medium consistency: Data is acknowledged after the primary and one secondary store it (medium latency). 3) Eventual/Low consistency: Acknowledged immediately after the primary persists it, offering lowest latency but weakest consistency.

#### 3. Describe the exact step-by-step data persistence flow in an S3-like distributed object store.
**Answer:**
1) The API service forwards object data to the data store layer. 2) The data routing service generates a UUID (ObjId) and queries the placement service. 3) The placement service checks the virtual cluster map and returns the primary data node. 4) The data routing service sends the raw data and UUID directly to the primary data node. 5) The primary node saves data locally and replicates it synchronously to secondary data nodes, responding to the data routing service once replication completes. 6) The object UUID is returned to the API service.

#### 4. How can distributed sharded databases handle object listing operations in an S3-like object storage system?
**Answer:**
When the metadata table is sharded (e.g., by bucket_id or hash ranges), prefix-based listing queries (like `SELECT * FROM object WHERE bucket_id = "123" AND object_name LIKE 'a/b/%'`) cannot target a single shard because files matching the prefix may reside across multiple shards. The brute-force distributed solution requires the metadata service to fan-out the query to every individual shard, gather all partial result sets, and aggregate/sort them in-memory before returning the response to the client.

#### 5. How do hardware failure rates, replication factors, and failure domains impact overall storage system durability?
**Answer:**
To protect against inevitable hard drive failures, data is typically replicated (e.g., 3 copies). Assuming a 0.81% annual drive failure rate, 3-way replication yields approximately `1 - (0.0081)^3 = ~99.9999%` reliability. Furthermore, data must be isolated across different failure domains (node-level, rack-level, and Availability Zones with separate power/cooling/network infrastructures) to prevent correlated mass outages during extreme disasters.

#### 6. How does garbage collection and compaction work in an append-only S3 storage data node?
**Answer:**
The garbage collector copies active objects from an old read-only file to a new compacted file (e.g., `/data/d`), skipping objects where the delete flag is set to true. Afterward, it updates the `object_mapping` table (updating file names and start offsets) within a database transaction to ensure consistency. Compaction usually waits until a large number of read-only files accumulate to merge them efficiently.

#### 7. What are the primary challenges when partitioning data?
**Answer:**
1. Distributing data evenly to prevent hotspots.
2. Minimizing data movement when nodes are added or removed (addressed by techniques like consistent hashing).

#### 8. What is quorum consistency in leaderless replication?
**Answer:**
A mechanism in leader-less data replication (like in Dynamo-style databases) where read and write operations must obtain acknowledgments from a quorum of replicas (W + R > N, where N is the total number of replicas, W is write quorum, and R is read quorum) to ensure strong consistency and handle node failures.

#### 9. What is the step-by-step workflow for uploading a large file via a multipart upload in object storage?
**Answer:**
(1) Client initiates a multipart upload, receiving a unique uploadID. (2) Client splits the large file into chunks (e.g., 200MB parts). (3) Client uploads parts sequentially or in parallel with the uploadID. (4) Data store returns an ETag (MD5 checksum) for each uploaded part. (5) After all parts are uploaded, client sends a complete multipart request containing uploadID, part numbers, and ETags. (6) Data store reassembles the parts based on part numbers.

#### 10. What scalability issues arise when using a NoSQL database (like DynamoDB) for a leaderboard, and how do you solve them?
**Answer:**
Problem: Naive partition keys (e.g., grouping all data for the current month under one partition key) create a 'hot partition' under high load because DynamoDB splits data using consistent hashing based on partition keys.
Solution: Write sharding. Split data into $N$ partitions by appending a calculated suffix (`user_id % number_of_partitions`) to the partition key, distributing writes evenly across nodes (at the cost of increased read/write query complexity).


## 📂 Category: Distributed Storage & Caching (1 cards)

### 🔴 Senior Level

#### 1. How do we use fixed partitions to implement a leaderboard?
**Answer:**
Divide the overall range of points into equal ranges (shards) across a set number of shards. Store the score mapping in a secondary cache (like Redis) or database to quickly lookup a user's shard. To fetch top players, query the shard with the highest score range. To fetch a user's rank, compute their local rank within their current shard and add the total count of players in higher-scoring shards (retrieved efficiently using commands like Redis 'info keyspace' in O(1) time). Handle edge cases when users move between shards due to score updates.


## 📂 Category: Distributed Storage & Databases (9 cards)

### 🟢 Junior Level

#### 1. What are the drawbacks and physical limits of vertical database scaling?
**Answer:**
Vertical scaling (adding CPU, RAM, etc.) hits hard hardware limits, introduces a single point of failure (SPOF) for the database layer, and incurs exponentially higher costs for high-end enterprise servers.


### 🟡 Mid Level

#### 1. How do we save storage space and manage file versions in cloud storage systems like Google Drive?
**Answer:**
Implement storage-saving techniques: 1) Account-level block deduplication using cryptographic hash values. 2) Intelligent backup strategies, such as setting a hard version limit or decaying version retention to favor recent edits. 3) Tiering infrequently accessed historical data to cheap cold storage (e.g., Amazon S3 Glacier).

#### 2. What are the driving forces behind the adoption of NoSQL databases?
**Answer:**
Key drivers include the need for massive scalability beyond relational database limits (very large datasets or high write throughput), preference for free/open-source software, specialized query operations not supported by relational models, and frustration with rigid relational schemas in favor of dynamic, expressive data models.

#### 3. What are the primary data sharding options for handling high-throughput leaderboards?
**Answer:**
Leaderboards are typically sharded using either fixed partitions (pre-allocated score ranges) or hash partitions (consistent hashing based on user IDs or score attributes).


### 🔴 Senior Level

#### 1. How do distributed databases like Cassandra scale horizontally without manual resharding?
**Answer:**
Cassandra utilizes a consistent hashing ring architecture with virtual nodes. Data is evenly distributed across nodes based on token ranges, and replication factors ensure copies are kept. Adding new nodes triggers automatic, transparent token rebalancing across the cluster.

#### 2. How do we process and store routing tiles in a mapping service like Google Maps?
**Answer:**
Run a periodic offline processing pipeline to transform raw, multi-source road datasets into multi-resolution routing tiles containing adjacency lists of graph nodes and edges. Store these binary-serialized tiles in object storage (like S3) using geohashes for fast lat/lng lookup, and cache them aggressively on the routing service.

#### 3. What are the architectural differences and trade-offs of size-tiered vs. leveled compaction in LSM-tree storage engines?
**Answer:**
In size-tiered compaction (used by HBase, supported by Cassandra), newer and smaller SSTables are successively merged into older and larger ones. In leveled compaction (used by LevelDB, RocksDB), the key range is split into smaller SSTables organized into discrete levels, allowing incremental compaction and lower disk space overhead.

#### 4. What are the core components, design characteristics, and trade-offs of a distributed key-value store?
**Answer:**
Characteristics include small key-value pairs (<10 KB), massive scalability, high availability, low latency, and tunable consistency. Core components comprise data partitioning, data replication, consistency models, inconsistency resolution (e.g., vector clocks), failure handling mechanisms, system architecture diagrams, and clear read/write paths.

#### 5. What factors dictate the choice of data storage solutions for high-concurrency payment systems?
**Answer:**
For payment systems, raw performance is secondary to proven stability (e.g., used by financial firms for 5+ years), rich monitoring/investigation tooling, and a mature DBA job market. Traditional relational databases with ACID transaction support are typically preferred over NoSQL/NewSQL.


## 📂 Category: Distributed Storage & Sync (1 cards)

### 🟢 Junior Level

#### 1. What is the role of an offline backup queue in distributed sync systems?
**Answer:**
When a client is offline and unable to pull the latest file changes or updates, the offline backup queue stores this metadata temporarily so that changes can be successfully synced as soon as the client reconnects.


## 📂 Category: Distributed Streaming (2 cards)

### 🔴 Senior Level

#### 1. How can you leverage Apache Kafka's partition mechanism to scale a metrics pipeline?
**Answer:**
1. Configure the number of partitions based on throughput requirements. 2. Partition metrics data by metric names so consumers can aggregate efficiently. 3. Further partition using tags/labels. 4. Categorize and prioritize metrics streams to process critical alerts first.

#### 2. How do you solve data duplication and offset management issues in stream processing pipelines?
**Answer:**
Saving offsets to external storage (like HDFS/S3) before downstream processing can cause message loss if downstream fails. To achieve 'exactly-once' processing, offsets must be committed only after receiving an acknowledgment from downstream, or the operations between ingestion and downstream dispatch must be wrapped in a distributed transaction.


## 📂 Category: Distributed Systems (163 cards)

### 🟢 Junior Level

#### 1. Can a notification system guarantee that recipients receive a notification exactly once?
**Answer:**
No. While notifications are delivered exactly once most of the time, the distributed nature of network partitions, retries, and client disconnects can occasionally result in duplicate notifications.

#### 2. How are key-value stores classified according to the CAP theorem?
**Answer:**
Key-value stores are classified as CP (Consistency and Partition tolerance) by sacrificing availability, or AP (Availability and Partition tolerance) by sacrificing consistency. CA (Consistency and Availability) systems do not exist in real-world distributed applications because network partitions are unavoidable.

#### 3. How are servers and nodes distributed in a consistent hashing key-value store?
**Answer:**
Servers and nodes are mapped onto a hash ring using a consistent hash function based on their unique identifiers, such as their IP address or server name.

#### 4. How is server lookup performed when using consistent hashing?
**Answer:**
To determine which server a key is stored on, traverse the hash ring clockwise from the key's position until the first server node is encountered.

#### 5. What are the four core requirements for unique IDs in distributed system design?
**Answer:**
1. Uniqueness: IDs must be globally unique.
2. Numerical values only.
3. Size constraint: IDs must fit into 64 bits.
4. Ordering: IDs must be roughly ordered by generation date/time.

#### 6. What is Partition Tolerance in the context of distributed systems?
**Answer:**
Partition tolerance refers to a distributed system's ability to continue operating correctly despite arbitrary network partitions (communication breaks between nodes causing dropped or delayed messages).

#### 7. What is a UUID and what are its key characteristics?
**Answer:**
A UUID (Universally Unique Identifier) is a 128-bit number used to identify information in computer systems (e.g., 09c93e62-50b4-468d-bf8a-c07e1040bfb2). It has an extremely low collision probability (e.g., generating 1 billion UUIDs per second for 100 years yields a 50% chance of a single duplicate). UUIDs can be generated independently without coordination between servers.

#### 8. What is a distributed key-value store and what core theorem governs its design?
**Answer:**
A distributed key-value store (distributed hash table) distributes key-value pairs across many servers. When designing such systems, it is critical to understand the CAP theorem (Consistency, Availability, and Partition Tolerance).

#### 9. What is a partition in consistent hashing?
**Answer:**
In consistent hashing, a partition is the hash space between adjacent servers.

#### 10. What is system availability?
**Answer:**
Availability is the property where any non-failing client request for data receives a valid response, even in the presence of node failures or partial system outages.

#### 11. What is the basic algorithm of a web crawler?
**Answer:**
1. Given a seed set of URLs, download all the web pages addressed by those URLs.
2. Extract hyperlinks and new URLs from these web pages.
3. Add new URLs to the frontier/list of URLs to be downloaded, and repeat the process.

#### 12. What is the difference between a fault and a failure?
**Answer:**
A fault is a component deviating from its specification, whereas a failure occurs when the system as a whole stops providing the required service to the user. Fault-tolerance mechanisms are designed to prevent faults from escalating into failures.

#### 13. What is the problem with traditional modulo hashing when servers are added or removed?
**Answer:**
Most keys are invalidated and redistributed, causing a massive cache miss storm and overwhelming backend services.

#### 14. What strategy is primarily used to decouple components in high-scale distributed systems?
**Answer:**
Message queues and event brokers are key strategies employed to decouple disparate components, allowing them to scale independently and absorb traffic spikes.

#### 15. Where are keys redistributed when a new server is added in consistent hashing?
**Answer:**
When a server is added, keys located between the last server and the new server need to be redistributed to the new server.

#### 16. Where are keys redistributed when a server is removed in consistent hashing?
**Answer:**
When a server is removed, keys located between the adjacent server and the removed server must be redistributed to the next available server moving clockwise.

#### 17. Why do distributed data centers experience latency during data transfer?
**Answer:**
Latency occurs primarily because data centers are geographically distributed across different regions, constrained by the physical speed of light over fiber optic networks.


### 🟡 Mid Level

#### 1. Are the hash functions used for consistent hashing rings identical to those used in traditional hash-based sharding?
**Answer:**
No, they are typically different hash functions; consistent hashing requires mapping both servers and keys onto a shared uniform hash space (ring), whereas traditional hash functions often use modulo arithmetic directly on keys.

#### 2. Describe the end-to-end payment flow using a Payment Service Provider (PSP).
**Answer:**
1. Client sends payment order to the payment service.
2. Payment service sends a registration request containing amount, currency, and a unique UUID (nonce) to the PSP to ensure exactly-once registration.
3. PSP returns a token (UUID identifying the registration).
4. Payment service persists the token.
5. Client loads the PSP-hosted payment page (or mobile SDK) using the token and a redirect URL.
6. User submits payment details directly to the PSP.
7. PSP processes payment and returns status.
8. Browser is redirected to the redirect URL with the payment status appended.
9. Asynchronously, the PSP calls the payment service via a webhook to update the payment order status in the database.

#### 3. Describe the resource manager workflow and task worker responsibilities in a video streaming or processing pipeline.
**Answer:**
The task scheduler retrieves the highest-priority task from the task queue, selects an optimal task worker from the worker queue, instructs the chosen worker to run the task defined in the DAG, and binds the task/worker info into a running queue. Once completed, the job is removed from the running queue by the scheduler. Task workers are responsible for executing the specific data processing steps defined within the DAG tasks.

#### 4. Describe the structural components of the Snowflake ID generation approach, including timestamp and sequence bits.
**Answer:**
Snowflake IDs are 64-bit identifiers composed of: 1) A sign bit (usually unused), 2) A 41-bit timestamp representing milliseconds since a custom epoch, yielding ~69 years of capacity and time-sortability, 3) Machine/datacenter ID bits for node identification, and 4) A 12-bit sequence number (4,096 combinations) which increments if multiple IDs are generated within the exact same millisecond on the same server node.

#### 5. Does consistent hashing utilize a modular operation when mapping keys onto the hash ring?
**Answer:**
No, consistent hashing does not use a modular operation for mapping keys to the ring; it maps keys to the next server moving clockwise along the ring based on hash values.

#### 6. Explain the concept of backpressure
**Answer:**
Backpressure is a flow control mechanism used when a downstream consumer or service is overwhelmed by the rate of incoming data from an upstream producer. Instead of failing or crashing due to out-of-memory errors, the system signals the upstream producer to slow down its emission rate (e.g., via reactive streams protocols, TCP window sizes, or queue length monitoring).

#### 7. How are errors typically handled in distributed video transcoding pipelines?
**Answer:**
1. Recoverable errors (e.g., a video segment failing to transcode): Handled by retrying the operation a few times. If persistent and deemed unrecoverable, an appropriate error code is returned to the client.
2. Non-recoverable errors (e.g., malformed video format): The system immediately halts running tasks associated with that video and returns a failure code.

#### 8. How are keys redistributed when servers are added or removed in consistent hashing with virtual nodes?
**Answer:**
When a new server (S4) is added, the affected key range moves anticlockwise from S4 until the previous active server (S3) is found; keys in this range migrate to S4. When a server (S1) is removed, keys between its predecessor (S0) and S1 are redistributed to its successor (S2).

#### 9. How can we optimize the naive pull model in distributed event-driven execution?
**Answer:**
Add a reverse proxy between the client and event-sourcing nodes to receive commands and poll execution status. To achieve near real-time responses, modify the read-only state machine to push execution status updates back to the reverse proxy asynchronously as soon as events are received.

#### 10. How can you ensure strong consistency in a storage service with caches?
**Answer:**
To achieve strong consistency, data across cache replicas and the primary database must be synchronized. This is typically done by invalidating or updating caches directly upon database writes. While relational databases natively support ACID properties to guarantee strong consistency, NoSQL databases often require programmatic synchronization logic.

#### 11. How do backward and forward compatibility differ when managing concurrent versions of code and data formats?
**Answer:**
Backward compatibility means newer code can read data written by older code (usually straightforward since newer code knows older formats). Forward compatibility means older code can read data written by newer code (trickier, requiring older code to safely ignore unknown additions/fields introduced by newer versions).

#### 12. How do virtual nodes work in consistent hashing?
**Answer:**
Virtual nodes map physical servers to multiple distinct points (e.g., s0_0, s0_1, s0_2) on the consistent hashing ring, allowing each physical server to manage multiple partitions. Keys are mapped to servers by traversing clockwise from the key's location to the first virtual node encountered, ensuring uniform data distribution and minimal key redistribution when servers are added or removed.

#### 13. How do we generate message IDs in a chat system while ensuring uniqueness and time-based sortability?
**Answer:**
Requirements for message IDs: unique and sortable by time (newer rows have higher IDs). Approaches include: 1) MySQL auto_increment (unsuitable for NoSQL), 2) Global 64-bit sequence number generator like Snowflake, and 3) Local sequence number generators per channel/group, which are sufficient for 1-on-1 or group chats and easier to implement.

#### 14. How do we improve the robustness and fault tolerance of a web crawler?
**Answer:**
Implement consistent hashing to distribute loads across downloaders dynamically. Persist crawl states and data continuously to storage systems to allow seamless restarts after failures. Ensure robust exception handling to prevent crashes, and enforce strict data validation.

#### 15. How do we resolve data inconsistencies among distributed replicas?
**Answer:**
Use versioning mechanisms such as vector clocks combined with conflict resolution strategies (e.g., last-write-wins or application-level merging) to detect and reconcile concurrent updates across distributed replicas.

#### 16. How do you handle synchronization conflicts in online collaborative or cloud storage systems?
**Answer:**
Use a first-write-wins strategy for the primary processor, while subsequent concurrent updates trigger a sync conflict. The system presents both conflicting versions (the local copy and the server's latest version) to the user, allowing them to manually merge the files or choose to overwrite one version.

#### 17. How does a distributed web crawler achieve high performance?
**Answer:**
Crawl jobs are distributed across multiple servers, each running multiple threads. The URL space is partitioned into smaller subsets so that each downloader/crawler instance is responsible for fetching and processing a specific partition of URLs.

#### 18. How does adding a server affect data distribution in consistent hashing?
**Answer:**
When a new server is added to a consistent hashing ring, only a fraction of keys (specifically those falling between the new virtual nodes and their immediate counter-clockwise predecessors) need to be redistributed. All other keys remain assigned to their existing servers.

#### 19. How does consistent hashing minimize key redistribution when a server is removed from a caching cluster?
**Answer:**
Consistent hashing maps both servers and keys onto a ring space. When a server is removed, only the keys mapped directly to that server's immediate range are remapped to its next clockwise neighbor. All other keys residing elsewhere on the ring remain completely unaffected.

#### 20. How does consistent hashing work and how does it help in load balancing?
**Answer:**
Consistent hashing maps both servers and keys onto a ring (e.g., hash space from 0 to 2^160 - 1 using SHA-1). When a server is added or removed, only a fraction of keys (k/n, where k is keys and n is servers) need to be remapped, minimizing cache misses and rebalancing overhead in distributed load balancers and caches.

#### 21. How does data replication work in HDFS?
**Answer:**
HDFS breaks files into large blocks (typically 128MB or 256MB) and replicates each block across multiple DataNodes (default replication factor of 3) to ensure fault tolerance. The NameNode manages the metadata and block locations, placing replicas across different racks to survive rack-level failures.

#### 22. How does fault tolerance work in MapReduce?
**Answer:**
MapReduce achieves fault tolerance by re-executing failed tasks. If a map task fails, the master node reschedules it on another node since intermediate outputs are written to local disk. If a reduce task fails, it re-reads the required map outputs from the distributed storage nodes where they were safely replicated.

#### 23. How does hardware component redundancy compare to multi-machine redundancy in modern cloud architecture?
**Answer:**
Hardware component redundancy (e.g., RAID, dual power supplies) protects against single-part failures on a single machine. However, due to scale and cloud elasticity where VMs can terminate without warning, multi-machine redundancy and distributed replication have become essential for achieving high availability.

#### 24. How does message queueing reduce coupling in distributed systems?
**Answer:**
Message queues decouple producers and consumers asynchronously. A producer can post a message even if the consumer is offline, and vice versa. This allows independent scaling; for instance, adding more background workers when queue size spikes without changing producer logic.

#### 25. How does synchronous communication compare to asynchronous communication in distributed systems?
**Answer:**
Synchronous communication is simpler in design, but services are tightly coupled and cannot operate autonomously. As the dependency graph grows, overall performance suffers. Asynchronous communication trades design simplicity and consistency for scalability and failure resilience. For large-scale systems with complex business logic and numerous third-party dependencies, asynchronous communication is generally the preferred choice.

#### 26. How does the Raft consensus algorithm handle leader and follower node failures?
**Answer:**
- **Leader Failure**: If the leader crashes, the cluster automatically elects a new leader from healthy nodes. If the crash occurred before command-to-event conversion, clients experience timeouts or errors and must retry against the new leader.
- **Follower Failure**: Requests sent to a crashed follower will fail. Raft handles this by having the sender retry indefinitely until the follower restarts or is replaced.

#### 27. How is URL shortening implemented using a distributed unique ID generator and base conversion?
**Answer:**
Given a long URL, a distributed unique ID generator returns a unique numeric ID (e.g., 2009215674938). This ID is converted to a short URL string using base 62 encoding (resulting in 'zn9edcu'). The mapping of ID, shortURL, and longURL is saved to the database. Distributed unique ID generators are critical and challenging to implement in distributed environments.

#### 28. How is data kept consistent and replicated across multiple data centers?
**Answer:**
To achieve high availability, reliability, and fault tolerance against regional outages, data is asynchronously replicated across N servers placed in distinct, geographically separate data centers connected via high-speed networks.

#### 29. How many keys need to be remapped on average when servers change in consistent hashing?
**Answer:**
Only k/n keys need to be remapped on average, where k is the number of keys and n is the number of slots/servers.

#### 30. What are the advantages and benefits of consistent hashing in distributed systems?
**Answer:**
Consistent hashing provides automatic scaling (servers can be added/removed dynamically), heterogeneity support (virtual nodes are proportional to server capacity), minimized key redistribution during topology changes, even data distribution for horizontal scaling, and mitigation of hotspot key problems (preventing overloaded shards by spreading high-traffic keys).

#### 31. What are the advantages and limitations of using UUIDs for distributed ID generation?
**Answer:**
Advantage: UUIDs are 128 bits long and can be generated independently on any node without coordination or central server bottlenecks. Disadvantage: Their 128-bit length often exceeds standard system requirements (such as 64-bit integer IDs), and their lack of sequential ordering causes poor database index locality (B-Tree fragmentation).

#### 32. What are the core characteristics of a highly scalable key-value store?
**Answer:**
High availability, high scalability, and automatic scaling capabilities to handle fluctuating loads and data volumes seamlessly.

#### 33. What are the core functional and non-functional requirements typically gathered when designing a distributed unique ID generator?
**Answer:**
1. IDs must be globally unique.
2. IDs must be numerical values only.
3. IDs must fit into a 64-bit integer.
4. IDs must be sortable/ordered by timestamp (chronologically increasing, though not strictly incrementing by 1).
5. The system must support high throughput, such as generating over 10,000 unique IDs per second.

#### 34. What are the five sections a 64-bit ID is divided into in the Snowflake approach?
**Answer:**
Sign bit, timestamp, datacenter ID, machine ID, and sequence number.

#### 35. What are the primary performance optimization strategies for distributed rate limiters?
**Answer:**
1. Multi-data center deployment using globally distributed edge servers (e.g., Cloudflare CDN nodes) to route client traffic to the geographically closest location, minimizing network latency. 2. Synchronizing rate-limiting counter data across regions using an eventual consistency model.

#### 36. What are the roles of the queue router and queue selector in a web crawler?
**Answer:**
The queue router ensures that each downstream FIFO queue only contains URLs from the same host to respect politeness constraints. The queue selector maps each worker thread to a specific FIFO queue, dictating which queue the thread downloads URLs from.

#### 37. What are the sections of a 64-bit Snowflake ID?
**Answer:**
Sign bit: 1 bit (always 0, reserved for future use/signed-unsigned distinction). Timestamp: 41 bits (milliseconds since a custom epoch, e.g., Twitter epoch 1288834974657, yielding ~69 years). Datacenter ID: 5 bits (supports up to 32 datacenters). Machine ID: 5 bits (supports up to 32 machines per datacenter). Sequence number: 12 bits (incremented for every ID generated per machine/process, resets to 0 every millisecond, supporting up to 4096 IDs/ms per machine).

#### 38. What are the standard consistency models in distributed data stores?
**Answer:**
Strong consistency: reads always return the most updated write; clients never see stale data. Weak consistency: subsequent reads may not immediately see updated values. Eventual consistency: a form of weak consistency where, given enough time without new updates, all replicas converge to the same value.

#### 39. What are three common consistency models in distributed data stores?
**Answer:**
Strong consistency (linearizability), weak consistency, and eventual consistency.

#### 40. What are three popular data serialization frameworks used in microservices?
**Answer:**
1. Protocol Buffers (protobuf): Strongly typed, binary, highly efficient, utilizes schema files (.proto).
2. Apache Thrift: Binary serialization framework with built-in RPC support, developed by Facebook.
3. Apache Avro: Schema-based binary serialization format heavily used in big data ecosystems (like Kafka/Hadoop) where schemas travel with the data.

#### 41. What are ticket servers as a distributed ID generation mechanism?
**Answer:**
Ticket servers are a centralized approach to generating unique primary keys in a distributed system, pioneered by Flickr. The design relies on a centralized auto_increment feature in a single database server (or a cluster of failover servers) that dispenses unique IDs upon request.

#### 42. What do N, R, and W represent in the context of quorum consensus?
**Answer:**
• N: The total number of replicas storing the data.
• R: The size of the read quorum (number of replicas that must respond to a read).
• W: The size of the write quorum (number of replicas that must acknowledge a write).

#### 43. What does availability mean in the context of the CAP theorem?
**Answer:**
Any non-failing node returns a non-error response to every request it receives, without a guarantee that it contains the most recent write (ensuring every client gets a response even if some nodes are down).

#### 44. What does partition tolerance mean in the context of the CAP theorem?
**Answer:**
It means the distributed system continues to operate despite arbitrary message loss or network partitions between nodes.

#### 45. What does the CAP theorem state?
**Answer:**
It states that a distributed data store can simultaneously provide at most two of the following three guarantees: Consistency, Availability, and Partition Tolerance.

#### 46. What does the CAP theorem state?
**Answer:**
The CAP theorem states that a distributed data store can simultaneously provide at most two of three guarantees: Consistency (every read receives the most recent write or an error), Availability (every non-failing node returns a non-error response), and Partition Tolerance (the system continues to operate despite an arbitrary number of messages being dropped or delayed by the network).

#### 47. What happens if a node's heartbeat has not increased for a predefined period in a cluster?
**Answer:**
The cluster orchestration or failure detector considers the member to be offline/dead and initiates node removal or failover protocols.

#### 48. What is a "URL Seen?" data structure and why is it used?
**Answer:**
The "URL Seen?" data structure tracks URLs that have already been visited or are currently residing in the crawler's frontier. It prevents duplicate processing, reduces server load, and avoids infinite loops. Common implementations include Bloom filters (for space efficiency) and hash tables.

#### 49. What is a consistency model in distributed key-value stores?
**Answer:**
A consistency model defines the degree and guarantees of data consistency across distributed replicas. There exists a wide spectrum of consistency models ranging from strong consistency (e.g., linearizability) to eventual consistency.

#### 50. What is a coordinator node in a distributed key-value store architecture?
**Answer:**
A coordinator node acts as a transparent proxy layer between the client and the distributed key-value store nodes, routing read and write requests to the appropriate replica nodes.

#### 51. What is a disadvantage of using a high number of virtual nodes in consistent hashing?
**Answer:**
It requires significantly more storage space to maintain the mapping data for all the virtual nodes.

#### 52. What is a hash ring in distributed systems?
**Answer:**
A hash ring is created by taking the ends of a hash space (e.g., mapping 0 and 2^32-1 together in a circle) to facilitate consistent hashing, allowing servers and keys to be mapped onto the ring for minimal key migration during scaling.

#### 53. What is a key advantage of a decentralized system design?
**Answer:**
Nodes can be added, removed, or moved automatically without requiring a centralized coordinator.

#### 54. What is a sample schema layout for a distributed commit log message (e.g., Kafka)?
**Answer:**
A typical log message structure includes: key (byte[]), value (byte[]), topic (string), partition (integer), offset (long), timestamp (long), message size (integer), and CRC checksum (integer).

#### 55. What is a snapshot in state machine replication?
**Answer:**
An immutable view of a historical system state. Once saved, a state machine can load the snapshot to bypass replaying the entire event log from inception, verifying its position and resuming execution directly from that point.

#### 56. What is a virtual node in consistent hashing?
**Answer:**
A virtual node represents a real node on the hash ring. It helps distribute the load more evenly across physical nodes by allowing a single physical node to be mapped to multiple points on the hash ring.

#### 57. What is consistent hashing and what is its main benefit?
**Answer:**
Consistent hashing is a special hashing scheme where, when a hash table is resized, only k/n keys need to be remapped on average (where k is the number of keys and n is the number of slots). In contrast, traditional hash tables cause nearly all keys to be remapped when the array size changes.

#### 58. What is data versioning in the context of inconsistency resolution?
**Answer:**
Versioning treats each data modification as a completely new, immutable version of the data, allowing distributed systems to track changes over time and reconcile conflicting concurrent writes (e.g., using vector clocks or last-write-wins).

#### 59. What is sacrificed in CP vs. AP distributed systems under the CAP theorem?
**Answer:**
In a CP (Consistency/Partition Tolerance) system, availability is sacrificed during a network partition to ensure all operating nodes return the exact same consistent data. In an AP (Availability/Partition Tolerance) system, strong consistency is sacrificed so that every non-failing node returns a response, potentially resulting in stale or conflicting data.

#### 60. What is the 'celebrity problem' (hotspot key problem) in distributed databases?
**Answer:**
Excessive read or write access to a specific shard caused by highly popular entities (e.g., Katy Perry, Justin Bieber). This can cause server overload and queue bottlenecks on that specific shard, requiring specialized mitigations like dedicated shards or fine-grained sub-partitioning.

#### 61. What is the CAP theorem in distributed storage systems?
**Answer:**
The CAP theorem states that a distributed data store can simultaneously provide at most two of three guarantees: Consistency (every read receives the most recent write or an error), Availability (every non-failing node returns a non-error response without a guaranteed recent write), and Partition Tolerance (the system continues to operate despite network drops or delays).

#### 62. What is the consistency model of read-only state machines in eventual consistency architectures?
**Answer:**
Read-only state machines lag behind the primary state to some extent, but are guaranteed to eventually catch up, achieving an eventually consistent architecture.

#### 63. What is the main function of a coordinator node in distributed key-value stores?
**Answer:**
A coordinator node acts as a proxy between the client and the key-value store's storage nodes, routing read and write requests to the correct replicas based on consistent hashing or partition keys.

#### 64. What is the primary architectural tradeoff in distributed key-value store design?
**Answer:**
The fundamental tradeoff is between consistency and availability, as described by the CAP theorem.

#### 65. What is the primary benefit of using virtual nodes in consistent hashing?
**Answer:**
To achieve a more balanced data distribution across servers by mitigating hot spots and reducing variance in load when nodes join or leave.

#### 66. What is the primary goal of consistent hashing?
**Answer:**
To distribute requests or data evenly across servers for horizontal scaling while minimizing key redistribution when servers are added or removed.

#### 67. What is the problem of storing state exclusively in local disk storage?
**Answer:**
While performance is superior to remote databases/brokers, storing state on a local disk makes the server stateful and introduces a single point of failure (SPOF).

#### 68. What is the role of a data node in distributed storage systems?
**Answer:**
A data node stores the actual raw object or block data and ensures durability by replicating it to other nodes (replication group). It runs a local daemon that periodically reports disk capacity, layout, and health to a central placement/metadata service via heartbeats.

#### 69. What is the role of the notification service in collaborative applications like Google Drive?
**Answer:**
The notification service maintains file consistency across clients by immediately broadcasting events when local mutations occur, reducing sync conflicts and pushing real-time updates to connected clients.

#### 70. What is the trade-off between strong consistency and eventual consistency?
**Answer:**
Strong consistency guarantees linearizability across all replicas but typically incurs higher latency and lower availability during network partitions. Eventual consistency trades immediate read consistency for lower latency and higher write availability.

#### 71. What is the tradeoff associated with increasing the number of virtual nodes in consistent hashing?
**Answer:**
Increasing the number of virtual nodes improves the distribution uniformity of data across physical nodes and reduces hotspots, but it requires significantly more memory/storage space to maintain and lookup the virtual-node-to-physical-node mapping metadata ring.

#### 72. What problems can naive alphabetical sharding cause in an autocomplete or search service?
**Answer:**
Naive character-based sharding (e.g., sharding servers by initial letters like 'a-m' and 'n-z', or via multi-level prefixes) leads to severe uneven data and traffic distribution because natural language is heavily skewed (e.g., words starting with 'c' vastly outnumber words starting with 'x').

#### 73. What protocol standards, client connection models, and functional boundaries should be established when designing a distributed email service?
**Answer:**
1. Scale: 1 billion active users.
2. Core Features: Email sending, receiving, inbox fetching, read/unread filtering, advanced keyword search (subject, sender, body), attachments, and anti-spam/anti-virus scanning (authentication out of scope).
3. Communication Protocol: Modern clients communicate with mail servers via HTTP (superseding legacy protocols like SMTP, POP, and IMAP for client-server interactions).

#### 74. What standard must be met in a distributed system to consider a server down?
**Answer:**
It is insufficient for a single server to declare another server down. Reliable failure detection in a distributed system typically requires at least two independent sources of information.

#### 75. When are the various IDs chosen in the Snowflake ID generation approach?
**Answer:**
Datacenter IDs and machine IDs are chosen at startup and are generally fixed. Timestamp and sequence numbers are generated dynamically while the ID generator service is running.

#### 76. Which prominent distributed systems and large-scale applications utilize consistent hashing?
**Answer:**
Amazon’s Dynamo database (partitioning component), Apache Cassandra (cluster data partitioning), Discord chat application, Akamai CDN, and Maglev network load balancer.

#### 77. Why is a chat service considered a stateful service in a system design architecture?
**Answer:**
Each client maintains a persistent network connection (such as WebSocket) to a specific chat server. Clients typically do not switch to another chat server as long as the current one is available, requiring service discovery to closely coordinate with the chat service to prevent server overloading.


### 🔴 Senior Level

#### 1. Describe the Saga workflow pattern for a distributed financial transfer (e.g., moving $1 from account A to account C).
**Answer:**
A Saga pattern manages distributed transactions through a sequence of local transactions. For a transfer from account A to account C, the forward execution path first performs a deduction on account A, followed by an addition on account C. If any step fails, compensating transactions are executed in reverse order to roll back the changes (e.g., refunding account A if account C addition fails), ensuring eventual consistency without holding long-lived distributed locks.

#### 2. Describe the core architecture, components, and coordination mechanisms of a distributed messaging queue.
**Answer:**
Producers push messages to specific topics, and Consumer Groups subscribe to topics to consume messages. Brokers host multiple partitions, where each partition contains a subset of a topic's messages. Storage is split into Data Storage (message persistence), State Storage (consumer offsets/state), and Metadata Storage (topic configurations). A Coordination Service (such as Apache Zookeeper or etcd) handles service discovery for alive brokers and executes leader election to select a single active controller responsible for partition assignments.

#### 3. Explain quorum consistency with N, W, and R parameters and how they guarantee strong consistency.
**Answer:**
In a replicated system with total replicas N, write quorum W, and read quorum R: the coordinator waits for W acknowledgements on writes and R responses on reads. If W + R > N, strong consistency is guaranteed because there is always at least one overlapping node containing the latest write. W=1 or R=1 yields lower latency but weaker consistency; higher values increase consistency at the cost of latency.

#### 4. How do Merkle trees optimize data synchronization between replicas?
**Answer:**
Merkle trees minimize the amount of data transferred during synchronization. The data sent is proportional only to the actual differences between the replicas rather than the total volume of stored data, using hierarchical cryptographic hashing over bucketed keys.

#### 5. How do consensus algorithms like Raft guarantee reliable event replication across distributed nodes?
**Answer:**
Raft elects a single leader node responsible for receiving commands and replicating event logs to followers. As long as a strict majority of nodes (`N/2 + 1`, e.g., 3 out of 5 nodes) remain online and operational, the cluster achieves consensus, ensuring all active nodes maintain identical append-only event lists despite individual node failures.

#### 6. How do database replication conflicts occur and how are they handled?
**Answer:**
Replication conflicts occur when concurrent updates are made to the same data item on different replica nodes (e.g., server n1 changes a value to v1 and n2 changes it to v2 simultaneously). To detect and reconcile these conflicts, versioning systems such as vector clocks are commonly used.

#### 7. How do distributed systems handle leader election during a failover?
**Answer:**
Battle-tested consensus algorithms like Raft or Paxos are used. In Raft, a new leader is elected when a follower stops receiving heartbeats and triggers an election. A candidate requires a strict majority of votes (N/2 + 1, where N is cluster size) to become the leader. Once elected, the leader coordinates state replication and logs updates to follower mmap event stores.

#### 8. How do file-based command logs and in-memory caching optimize event sourcing architectures?
**Answer:**
Writing commands and events to local disk instead of remote brokers (like Kafka) removes network transit latency. Using an append-only file structure capitalizes on operating system optimizations for sequential disk writes (which can outperform random memory access). Recent commands/events are simultaneously cached in memory to eliminate subsequent disk read overhead.

#### 9. How do vector clocks track causality and detect concurrent updates in distributed systems?
**Answer:**
A vector clock is an array of (server, counter) pairs assigned to data items. When server Sx updates data, its counter increments. If concurrent updates occur on different servers (e.g., Sy and Sz) without causal knowledge of each other, reading both branches reveals a conflict, which must be resolved (often by client application logic) before writing a merged version.

#### 10. How do we efficiently compare two Merkle trees for data synchronization?
**Answer:**
Compare root hashes first. If they match, data is synchronized. If they disagree, compare left child hashes followed by right child hashes, recursively traversing the tree to isolate and sync only the out-of-sync buckets.

#### 11. How do we guarantee event replication properties across multiple nodes?
**Answer:**
Replication must guarantee: 1) No data loss, and 2) The relative order of data within a log file remains identical across nodes. Consensus-based replication algorithms are best suited to achieve these guarantees.

#### 12. How do we manage hundreds of distributed Redis pub/sub servers dynamically?
**Answer:**
Introduce a service discovery component like etcd or ZooKeeper acting as a lightweight configuration key-value store holding the hash ring mapping (e.g., Key: `/config/pub_sub_ring`, Value: `['p_1', 'p_2']`). WebSocket servers cache a local copy of this hash ring and subscribe to changes in service discovery to route messages accurately.

#### 13. How do you minimize task latency on the critical path in an ultra-low latency system like a stock exchange?
**Answer:**
Network round-trips over distributed servers and disk persistence introduce milliseconds of latency. To achieve tens of microseconds of latency, eliminate network hops by collocating all critical-path components on the same physical server. Replace remote event stores (like Kafka) with high-performance local memory mapping (`mmap`) for append-only event logs.

#### 14. How do you utilize checksums and erasure coding to guarantee data integrity in distributed S3-compatible object storage?
**Answer:**
Append a checksum (such as MD5) to the end of each object before marking it read-only. During reads: (1) Fetch the data chunks and stored checksum, (2) Recompute the checksum locally, (3) If they match, the data is valid; if corrupted, automatically reconstruct the missing or damaged data using erasure coding slices from alternative failure domains.

#### 15. How does a placement service operate in a distributed object storage system?
**Answer:**
The placement service determines primary and replica data nodes for objects using a virtual cluster map that tracks physical topology to ensure replicas are physically separated for durability. It monitors nodes via heartbeats (marking nodes 'down' after a 15-second grace period). It is typically built as a cluster of 5 or 7 nodes using Paxos or Raft consensus.

#### 16. How does conflict resolution work in multi-leader replication?
**Answer:**
Multi-leader replication allows multiple nodes to accept writes concurrently. Conflict resolution strategies include last-write-wins (LWW) using timestamps, vector clocks, multi-version concurrency control, application-defined merge logic, or conflict-free replicated data types (CRDTs).

#### 17. How does online status fanout work in presence systems, and what are its scalability limitations?
**Answer:**
Presence servers use a publish-subscribe model where each friend pair shares a channel via WebSockets. When a user's status changes, an event is published to all friend channels. While effective for small groups (e.g., WeChat capped at 500), it becomes a massive performance bottleneck for large groups (e.g., 100,000 members generating 100,000 events per status change), requiring pull-on-demand strategies instead.

#### 18. How is a watermark used in event aggregation pipelines?
**Answer:**
Watermarks are temporal extensions to aggregation windows in stream processing frameworks that account for out-of-order and slightly delayed events. By extending the processing window by a configured buffer duration (e.g., 15 seconds), the system captures late-arriving data to improve accuracy, trading off a minor increase in processing latency.

#### 19. How is computation related to durability when event sourcing is used?
**Answer:**
In event-sourcing architectures, state is derived purely from immutable event logs. Because computation is stateless and deterministic, system reliability reduces entirely to data durability; if state or compute nodes fail, the computational state can always be fully recovered by re-running the exact code sequence against the durable event log.

#### 20. How is data partitioned and distributed using consistent hashing?
**Answer:**
To partition data across multiple servers evenly while minimizing data movement during node additions/removals, servers and keys are mapped onto a hash ring. A key is stored on the first server encountered moving clockwise from its hashed position. Virtual nodes and unique server checks are used to ensure balanced replication across physical nodes.

#### 21. How is resizing a distributed Redis or WebSocket server cluster performed using a hash ring?
**Answer:**
Determine the new ring size and provision new servers (e.g., adding p_5 and p_6 to [p_1, p_2, p_3, p_4]). Update the keys of the hash ring with the new content and monitor dashboards for expected CPU usage spikes in the cluster.

#### 22. What architectural patterns optimize write throughput and efficiency in a distributed messaging queue?
**Answer:**
1. Use sequential on-disk data structures that leverage OS disk caching and optimal rotational/SSD sequential access. 2. Pass immutable message data structures directly from producer to queue to consumer without modification, minimizing expensive memory copying. 3. Maximize batching at all layers: producers send in batches, queues persist in larger batches, and consumers fetch in batches.

#### 23. What are the components and responsibilities of a resource manager in a video streaming processing cluster?
**Answer:**
The resource manager optimizes resource allocation using priority queues: a Task Queue (pending tasks), Worker Queue (worker utilization info), and Running Queue (active tasks and assigned workers). The Task Scheduler continuously selects optimal task-worker pairings and instructs workers to execute jobs.

#### 24. What are the core considerations for client gateways in financial exchange systems?
**Answer:**
Client gateways vary for retail vs. institutional clients, balancing latency, transaction volume, and security. Institutional market makers require extreme low latency. Colocation (colo) setups place trading engine software directly within the exchange's data center, minimizing physical network propagation delay.

#### 25. What are the core technical challenges when implementing a rate limiter in a distributed environment?
**Answer:**
Race conditions (concurrent updates to counter keys) and Synchronization issues (keeping distributed nodes consistent across a cluster, often solved using centralized stores like Redis with Lua scripts or sorted sets).

#### 26. What are the fundamental technical questions required to evaluate and design a fault-tolerant distributed system?
**Answer:**
1. Failover mechanism: How and when is a primary instance failure detected to trigger failover to a backup instance?
2. Leader election: How do backup instances reach consensus to choose a new leader?
3. Recovery Time Objective (RTO): What is the acceptable maximum downtime/recovery duration?
4. Recovery Point Objective (RPO): What is the acceptable data loss window, and can the system operate under degraded conditions?

#### 27. What are the key challenges in a multi-data center architecture setup?
**Answer:**
The two primary challenges are traffic redirection (routing users to the optimal data center) and data synchronization (replicating state reliably across geographically distributed regions).

#### 28. What are the key properties of consensus algorithms (FLP impossibility / safety and liveness)?
**Answer:**
Key properties include Safety (nothing bad happens, e.g., no two nodes agree on different values for the same slot/index) and Liveness (something good eventually happens, nodes eventually reach agreement). The FLP impossibility result states that no deterministic asynchronous consensus protocol can guarantee safety and liveness in the presence of even a single unannounced node crash failure.

#### 29. What are the main features and architectural patterns of a distributed cache or key-value store?
**Answer:**
Clients communicate via simple APIs: get(key) and put(key, value). A coordinator node acts as a proxy between the client and the store. Nodes are mapped on a token ring using consistent hashing. The system is completely decentralized for automatic node scaling, data is replicated across multiple nodes, and it has no single point of failure.

#### 30. What are the non-functional requirements of a distributed email service?
**Answer:**
1. Reliability: Zero data loss for email storage.
2. Availability: Automatic replication across nodes to withstand partial system failures.
3. Scalability: Horizontal scaling to handle increasing user bases and email volumes without performance degradation.
4. Flexibility and extensibility: Custom protocols beyond limited traditional IMAP/POP to support modern feature sets.

#### 31. What are the operational disadvantages and limitations of using vector clocks for conflict resolution?
**Answer:**
Vector clocks add complexity by shifting conflict resolution logic to the client. Additionally, the [server: version] metadata pairs can grow rapidly; pruning old pairs via thresholds can compromise historical descendant tracking, though it remains widely acceptable in practice.

#### 32. What are the primary responsibilities of a matching engine in financial systems?
**Answer:**
1. Maintain the order book for each trading symbol (tracking buy and sell orders).
2. Match buy and sell orders accurately and with high performance, generating execution fills.
3. Distribute the execution stream downstream as real-time market data.

#### 33. What are the responsibilities of a DAG scheduler in a distributed processing pipeline?
**Answer:**
The DAG scheduler splits a Directed Acyclic Graph (DAG) into execution stages consisting of distinct tasks and places them into a task queue managed by the resource manager. For example, a video processing workflow might split into stages for video/audio extraction, followed by parallel encoding and thumbnail generation tasks.

#### 34. What are the solutions for synchronization and race condition issues in distributed rate limiters?
**Answer:**
Sticky sessions are not scalable or flexible and should be avoided. Instead, use a centralized data store like Redis to share state across nodes. To solve race conditions without relying on heavy locks that degrade throughput, use Redis Lua scripts or Redis sorted sets data structures.

#### 35. What are the steps to build a Merkle tree given a key space from 1 to 12?
**Answer:**
Step 1: Divide the key space into buckets (e.g., 4 buckets) to maintain a limited depth of the tree.
Step 2: Hash each key in a bucket using a uniform hashing method.
Step 3: Create a single hash node per bucket.
Step 4: Build the tree upwards to the root by calculating the hashes of the children nodes.

#### 36. What are two primary issues with the basic consistent hashing approach?
**Answer:**
1. Uneven partition sizes (hotspotting where certain nodes handle disproportionate traffic). 
2. Non-uniform key distribution across the ring.

#### 37. What are vector clocks used for in distributed systems and replication?
**Answer:**
Vector clocks are data structures used to track causality and version history of data items in distributed, eventually consistent data stores, helping detect concurrent writes and resolve conflicts during replication.

#### 38. What consistency issues arise in a pure microservices architecture compared to monolithic architectures?
**Answer:**
In microservices, each service has its own database, meaning a logically atomic operation spans multiple services and cannot use a single ACID transaction. Failures require compensating actions (rollbacks), increasing the risk of data inconsistency.

#### 39. What core trade-offs do real-world distributed systems face during network partitions?
**Answer:**
In a distributed system, partitions cannot be avoided, and when a partition occurs, we must choose between consistency and availability. For example, if node n3 goes down and cannot communicate with n1 and n2, clients writing data to n1 or n2 cannot propagate it to n3. If data is written to n3 but not yet propagated to n1 and n2, those nodes will serve stale data.

#### 40. What critical challenges and design considerations must be addressed for distributed ID generation systems?
**Answer:**
Key considerations include: 1) Clock synchronization: Ensuring ID generation servers share time consistency using mechanisms like NTP (Network Time Protocol), especially across multi-core or multi-machine environments. 2) Section length tuning: Allocating bit lengths (e.g., more timestamp bits vs. fewer sequence bits) based on expected concurrency and lifespan. 3) High availability: Ensuring the ID generator is fault-tolerant as a mission-critical component.

#### 41. What do vector clocks help to identify in distributed data versions?
**Answer:**
Whether one version precedes, succeeds, or is in conflict with other versions.

#### 42. What does versioning mean in the context of inconsistency resolution?
**Answer:**
Treating each data modification as creating a new, immutable version of the data to handle concurrent updates and resolve conflicts (e.g., using vector clocks).

#### 43. What happens if root hashes match when comparing two Merkle trees?
**Answer:**
It guarantees that both servers have identical data across the entire dataset, avoiding the need to compare individual leaf nodes or blocks.

#### 44. What is Consistency in ACID transactions versus Consistency in the CAP theorem?
**Answer:**
In ACID transactions, Consistency ensures a transaction brings the database from one valid state to another, maintaining all predefined rules and constraints. In the CAP theorem, Consistency (often called linearizability) means all clients see the same data at the same time regardless of which node they connect to.

#### 45. What is Fixed Partition Rebalancing?
**Answer:**
Fixed Partition Rebalancing is a partition assignment strategy where a fixed number of partitions are created upfront (often significantly more than the number of nodes), and partitions are moved between nodes when nodes join or leave, without changing the total number of partitions.

#### 46. What is a Merkle tree and what is it used for?
**Answer:**
A Merkle tree (or hash tree) is a tree in which every non-leaf node is labeled with the cryptographic hash of the values of its child nodes. It allows efficient and secure verification of large data structures. In distributed systems, it is primarily used for inconsistency detection (anti-entropy) and minimizing the amount of data transferred between nodes.

#### 47. What is a data routing service in a distributed architecture?
**Answer:**
A stateless service providing RESTful or gRPC APIs to access a data node cluster. It queries a placement service to find the optimal data node for reads and writes, acting as an intermediary layer between API services and the data storage tier.

#### 48. What is a major downside of using vector clocks in distributed databases?
**Answer:**
It adds client-side complexity because the client application must implement and handle conflict resolution logic when concurrent updates are detected.

#### 49. What is a sequencer in a deterministic matching engine?
**Answer:**
A core component that stamps every incoming order and completed execution pair with sequence IDs before processing. It operates inbound and outbound instances with strict sequential numbering to ensure determinism and detect any missing message gaps.

#### 50. What is a vector clock and how does it work?
**Answer:**
A vector clock is a [server, version] pair associated with a data item, represented as D([S1, v1], [S2, v2], ..., [Sn, vn]). It is used to determine if one version precedes, succeeds, or conflicts with others. When data item D is written to server Si, the system increments vi if [Si, vi] exists, or creates a new entry [Si, 1] otherwise.

#### 51. What is colocation in a stock exchange system?
**Answer:**
Colocation places hedge funds' or brokers' servers in the same data center as the exchange matching engine. Latency in placing an order is proportional to the length of the cable. Colocation does not break fairness; it is considered a paid-for VIP service.

#### 52. What is the Twitter Snowflake ID generation approach?
**Answer:**
Snowflake is a distributed 64-bit unique ID generation algorithm. It divides the 64-bit space into distinct sections, typically including a timestamp, data center ID, machine ID, and a sequence number to ensure uniqueness and sortability across distributed nodes without coordination.

#### 53. What is the difference between strict and sloppy quorum for handling temporary failure?
**Answer:**
In strict quorum, read and write operations are strictly blocked if quorum cannot be met due to node failures. Sloppy quorum improves availability by choosing the first W healthy servers for writes and the first R healthy servers for reads on the hash ring, ignoring offline servers. If a server is unavailable, a temporary healthy server handles the request, and uses hinted handoff to push changes back to the original server once it comes back online.

#### 54. What is the difference between strong consistency and eventual consistency?
**Answer:**
Strong consistency ensures all clients see the same data at the same time by forcing replicas to agree on writes before acknowledging them, at the cost of availability and latency. Eventual consistency allows temporary inconsistencies across replicas to maximize availability and partition tolerance, requiring clients or backend processes to reconcile concurrent writes later.

#### 55. What is the first step when comparing two replicas using Merkle trees for anti-entropy?
**Answer:**
Compare the root hashes of the Merkle trees. If they match, the data is identical, avoiding lower-level tree traversal.

#### 56. What is the key architectural requirement of a highly available matching engine?
**Answer:**
A highly available matching engine must be strictly deterministic. Given an identical sequence of input orders, it must produce the exact same sequence of executions (fills) upon replay, which is foundational for state machine replication and high availability.

#### 57. What is the role of a client gateway in a high-frequency trading or exchange system?
**Answer:**
The client gateway acts as the gatekeeper for an exchange, receiving client orders and routing them to the order manager. Because it sits directly on the critical path and is latency-sensitive, it must remain lightweight, offloading complex tasks like deep risk checks and matching algorithms to downstream components.

#### 58. What is the statistical MTTF of a hard disk, and what are the operational implications for a large storage cluster?
**Answer:**
Hard disks typically have a Mean Time To Failure (MTTF) of about 10 to 50 years. In a storage cluster with 10,000 disks, this translates to an expectation of roughly one disk failure per day, necessitating automated replication and self-healing mechanisms.

#### 59. What is the structure and purpose of the components in a Snowflake ID?
**Answer:**
A Snowflake ID consists of:
1. Sign bit: Always 0, reserved for future uses.
2. Timestamp: Milliseconds since the epoch, ensuring IDs are sortable by time.
3. Datacenter and machine IDs: Unique identifiers for the node.
4. Sequence number: Incremented for every ID generated on that node within the same millisecond.

#### 60. What is the synchronization issue encountered in distributed rate limiters?
**Answer:**
When multiple rate limiter servers are deployed behind a stateless web tier to handle massive traffic, a client's requests may hit different rate limiter nodes over time. Without synchronization, local rate-limiting data (like token counts or counters) on one node is unknown to others, causing rate limits to be miscalculated. This is typically solved using centralized data stores like Redis with Lua scripts or sticky sessions.

#### 61. What metadata is required for object lookup in a custom S3-like object storage data node?
**Answer:**
The data node needs: object_id (UUID of the object), file_name (the name of the file containing the object), start_offset (beginning address of the object in the file), and object_size (number of bytes in the object).

#### 62. What protocol is commonly used to detect node failures in a distributed system without central coordination?
**Answer:**
The gossip protocol, where nodes periodically exchange state information with randomly chosen peers to quickly discover membership changes and failures.

#### 63. What technical challenges must be resolved to achieve a reliable multi-data center architecture?
**Answer:**
1. Traffic Redirection: Use GeoDNS or traffic managers to route users to the nearest data center. 2. Data Synchronization: Implement cross-region asynchronous replication (e.g., similar to Netflix's models) to handle regional failovers where local databases/caches might be out of sync or unavailable. 3. Testing and Deployment: Utilize automated deployment tooling and multi-region testing environments to maintain configuration and service consistency globally.

#### 64. What techniques are used to solve data inconsistency problems in distributed systems?
**Answer:**
Versioning and vector clocks.

#### 65. What trade-offs do we make regarding consistency and availability in a distributed system (CAP Theorem)?
**Answer:**
Choosing consistency (CP) requires blocking write operations during a network partition to prevent data divergence, increasing unavailability (common in banks). Choosing availability (AP) allows the system to continue accepting reads (potentially stale data) and writes, syncing partitions later.

#### 66. When a server is added or removed from a consistent hashing ring, how do you find the affected range of keys for redistribution?
**Answer:**
Start from the target server (newly added or removed) and move anticlockwise along the ring until the next available server is found.

#### 67. Which message delivery semantic is suitable for an ad click event aggregator where financial accuracy is critical?
**Answer:**
Exactly-once delivery. While message queues like Kafka offer at-most-once, at-least once, and exactly-once, financial systems require exactly-once processing to prevent discrepancies of millions of dollars from duplicate or missing events.

#### 68. Why are incoming orders and outgoing executions stamped with sequence IDs in financial trading systems?
**Answer:**
Sequence IDs ensure timeliness and fairness, enable fast disaster recovery and event replay, and support exactly-once processing guarantees.

#### 69. Why is implementing pagination challenging when executing queries across multiple sharded datasets (e.g., S3-like metadata stores)?
**Answer:**
Executing queries across all shards using standard OFFSET and LIMIT clauses requires coordinating global ordering and pagination cursors. Maintaining correct offsets and limits across distributed partitions complicates result aggregation and cursor decoding.


## 📂 Category: Distributed Systems & Concurrency (1 cards)

### 🔴 Senior Level

#### 1. What architectural alternatives exist to Redis pub/sub for real-time applications like nearby friends tracking?
**Answer:**
Erlang (using the BEAM VM and OTP libraries) is a powerful alternative. Its lightweight processes take about 300 bytes each, allowing millions of concurrent user processes on a single modern server. Each user can be modeled as an individual Erlang process that natively subscribes to friends' updates, creating an efficient distributed mesh of connections without external pub/sub brokers.


## 📂 Category: Distributed Systems & Consensus (1 cards)

### 🔴 Senior Level

#### 1. What is a decentralized alternative to all-to-all multicasting for failure detection in large distributed systems?
**Answer:**
The gossip protocol. Each node maintains a node membership list containing member IDs and heartbeat counters. Nodes periodically increment their counters and send heartbeats to a random set of other nodes, which propagate the information. If a node's heartbeat does not increase beyond a predefined threshold, it is marked as offline and this state is propagated cluster-wide.


## 📂 Category: Distributed Systems & Consistency (1 cards)

### 🔴 Senior Level

#### 1. What technique is used to improve write and read availability when using quorum consensus in distributed databases?
**Answer:**
Sloppy quorum, where writes and reads are accepted by a designated number of healthy nodes even if they are not the primary replica nodes designated for that key, temporarily relaxing strict consistency.


## 📂 Category: Distributed Systems & Hashing (2 cards)

### 🟢 Junior Level

#### 1. What is the mathematical formula used for traditional modular hashing in load balancing or distributed storage?
**Answer:**
serverIndex = hash(key) % N, where N represents the total number of servers in the pool.


### 🟡 Mid Level

#### 1. What is the impact of increasing virtual nodes in consistent hashing?
**Answer:**
Increasing virtual nodes decreases the standard deviation of key distribution (reducing it from ~10% with 100 vnodes to ~5% with 200 vnodes), leading to a more balanced load distribution. However, this requires more memory space to track the virtual node mappings.


## 📂 Category: Distributed Systems & Load Balancing (1 cards)

### 🟢 Junior Level

#### 1. What technique is commonly used to distribute requests and data evenly across distributed servers?
**Answer:**
Consistent hashing is a commonly used technique to distribute keys/requests uniformly across a dynamic set of nodes while minimizing key redistribution when nodes are added or removed.


## 📂 Category: Distributed Systems Architecture (2 cards)

### 🟡 Mid Level

#### 1. What technique is used to address the problems of uneven partition sizes and non-uniform key distribution in basic consistent hashing?
**Answer:**
Virtual nodes (vnodes) or replicas, which assign multiple smaller partitions/tokens on the hash ring to a single physical server to ensure a more uniform distribution of data.


### 🔴 Senior Level

#### 1. What are the primary talking points and components to consider when designing a news feed service?
**Answer:**
Scaling the database (vertical vs horizontal scaling, SQL vs NoSQL, master-slave replication, read replicas, consistency models, database sharding), keeping the web tier stateless, aggressive caching, supporting multi-data center architectures, decoupling components with message queues, and monitoring key metrics like peak QPS and refresh latency.


## 📂 Category: Distributed Systems Theory (5 cards)

### 🟢 Junior Level

#### 1. What is the ideal situation of distributed systems regarding the CAP theorem?
**Answer:**
In an ideal world, network partitions never occur, and data written to node n1 is automatically replicated to n2 and n3, achieving both high consistency and high availability simultaneously.


### 🟡 Mid Level

#### 1. How is consistency defined under the CAP theorem?
**Answer:**
Consistency in CAP means linearizability: every read receives the most recent write or an error, ensuring all clients see the exact same data at the same time.

#### 2. What are the three types of systems based on CAP characteristics?
**Answer:**
CP (Consistency/Partition Tolerance), AP (Availability/Partition Tolerance), and CA (Consistency/Availability). Note that in distributed systems, network partitions are inevitable, so CA is generally theoretical over a wide-area network.

#### 3. What are the trade-offs of various quorum configurations (W, R, N)?
**Answer:**
If R=1 and W=N, the system optimizes for fast reads. If W=1 and R=N, it optimizes for fast writes. Strong consistency is guaranteed when W + R > N (typically N=3, W=R=2), while W + R <= N does not guarantee strong consistency.

#### 4. What are the two key data consistency models used in distributed databases?
**Answer:**
The two key data consistency models are strong consistency (linearizability) and eventual consistency.


## 📂 Category: Distributed Systems: Consensus & Replication (1 cards)

### 🟡 Mid Level

#### 1. What are the core parameters of Quorum Consensus in distributed data stores?
**Answer:**
N = Total number of replicas.
W = Write quorum size (must be acknowledged by W replicas for a write to succeed).
R = Read quorum size (must wait for responses from at least R replicas for a read to succeed).


## 📂 Category: Distributed Systems: Event Sourcing & CQRS (1 cards)

### 🔴 Senior Level

#### 1. What architectural challenges arise when implementing high-performance event sourcing with CQRS and distributed consensus?
**Answer:**
1. Latency in read/write splits: CQRS request/response flows can be slow for immediate read-after-write consistency (e.g., digital wallets), forcing clients to rely on periodic polling.
2. Consensus scaling limits: A single Raft group has capacity limits, necessitating data sharding and complex distributed transactions at scale.


## 📂 Category: Distributed Systems: Rate Limiting (2 cards)

### 🟢 Junior Level

#### 1. What are the core parameters of the Leaking Bucket rate-limiting algorithm?
**Answer:**
1. Bucket size: Represents the queue capacity holding requests waiting to be processed.
2. Outflow rate: Defines the fixed rate at which requests are processed and removed from the queue (typically measured per second).

#### 2. What are the core parameters of the Token Bucket rate-limiting algorithm?
**Answer:**
1. Bucket size: The maximum number of tokens the bucket can hold.
2. Refill rate: The number of tokens added to the bucket per second.


## 📂 Category: Distributed Transactions (15 cards)

### 🟡 Mid Level

#### 1. Explain the Two-Phase Commit (2PC) protocol.
**Answer:**
Two-Phase Commit (2PC) is a distributed atomic commitment protocol that ensures all nodes in a distributed transaction either commit or abort together. Phase 1 (Prepare): The coordinator asks all participant nodes if they can commit. Each node writes changes to a local transaction log and replies with a vote (prepared/yes or abort/no). Phase 2 (Commit): If all participants vote yes, the coordinator sends a commit command, and participants finalize the transaction. If any vote no, the coordinator issues an abort command. 2PC is a blocking protocol susceptible to coordinator failures.

#### 2. What common scenarios cause double payments, and how do we prevent them?
**Answer:**
Scenarios include: (1) clients clicking the pay button twice on a hosted payment page, and (2) network errors dropping the PSP response, triggering client retries. Prevent double payments by enforcing at-most-once execution guarantees, also known as idempotency.

#### 3. What core reservation semantics, pricing models, and business constraints must be addressed when designing a hotel booking system?
**Answer:**
1. Scale: 5,000 hotels and 1 million rooms globally.
2. Transaction Flow: Full payment collected upfront at reservation time.
3. Channel Support: Multi-channel booking via web and mobile applications.
4. Inventory Management: Explicit support for 10% overbooking to account for cancellations.
5. Core Features: Property detail pages, room detail views, reservation creation/cancellation, and an admin panel for inventory management.
6. Pricing Model: Dynamic pricing where room rates vary daily based on projected occupancy levels.


### 🔴 Senior Level

#### 1. Explain the Saga pattern in microservices.
**Answer:**
A Saga is a design pattern used to manage data consistency across distributed microservices in scenarios where traditional ACID transactions (like 2PC) are impractical due to performance or availability constraints. A Saga is a sequence of local transactions where each step updates data within a single service. If a step fails, the Saga executes a series of compensating transactions (rollbacks) in reverse order to undo the changes made by preceding steps. It can be orchestrated centrally (Orchestrator pattern) or implemented via event-driven choreography.

#### 2. How do TC/C (Try-Confirm/Cancel) and Saga patterns compare in distributed transactions?
**Answer:**
Both are application-level distributed transaction models. 
- **Compensating action**: TC/C uses 'Cancel' in the cancel phase, while Saga uses rollback actions.
- **Central coordination**: Both support orchestration modes (e.g., central coordinator).
- **Operation execution order**: TC/C allows arbitrary or parallel orders, whereas Saga typically runs in a linear or defined sequence.
- **Partial inconsistency visibility**: Both can expose intermediate or partially inconsistent states during execution.
- **Logic level**: Both are implemented at the application or database business logic level.

#### 3. How do Two-Phase Commit (2PC) and Sagas address data consistency in microservices, and what are their tradeoffs?
**Answer:**
Two-Phase Commit (2PC) guarantees strict ACID atomicity across distributed nodes using a blocking coordinator protocol. However, a single node failure blocks progress, making it unperformant. Sagas handle distributed transactions via a sequence of local steps relying on eventual consistency; if a step fails, compensating transactions are executed to undo prior changes. Sagas improve availability and performance at the cost of design complexity and handling transient inconsistencies.

#### 4. How do distributed transactions apply to event sourcing consensus node groups?
**Answer:**
When synchronous execution is enforced across event sourcing node groups, distributed transaction patterns such as Try-Confirm/Cancel (TC/C) or Saga patterns can be reused to maintain consistency across partitioned hash keys.

#### 5. How do we achieve exactly-once execution for payment systems to avoid double charging?
**Answer:**
Mathematically, an operation is executed exactly-once if it is guaranteed to be executed both at-least-once (via retries) and at-most-once (via idempotency).

#### 6. How do we choose between TC/C (Try-Confirm/Cancel) and Saga distributed transaction patterns?
**Answer:**
Choose Saga for standard microservices where steps are executed in linear order and simplicity/industry trends are favored. Choose TC/C if the system is latency-sensitive and requires parallel execution of operations across many services.

#### 7. How do we coordinate distributed transactions using the Saga pattern (Choreography vs. Orchestration)?
**Answer:**
Choreography uses decentralized event subscription where each service listens to events and maintains an internal state machine (harder to manage at scale). Orchestration uses a centralized coordinator to instruct services in the correct order, managing complexity better and making it preferred for systems like digital wallets.

#### 8. How do we handle out-of-order operations in Try-Cancel (TC/C) distributed transactions?
**Answer:**
Enhance the phase status table and logic: 1) Allow out-of-order Cancel operations to leave a flag in the database indicating a Cancel was seen without a prior Try instruction, and 2) Update Try operations to check for this out-of-order flag and return a failure if it exists.

#### 9. How does a distributed money transfer workflow execute using Event Sourcing and the Saga pattern?
**Answer:**
1. User initiates a transfer (e.g., A-1, C+1) via the Saga coordinator.
2. Coordinator logs the transaction state in a phase status table.
3. Coordinator sends the first command (A-1) to Partition 1 (Account A).
4. Partition 1 Raft leader receives the command, validates it, and appends it to its command list. Once Raft consensus synchronizes the event, it executes.
5. The Event Sourcing framework updates the read path via CQRS and returns success to the Saga coordinator.
6. Coordinator updates its status table and triggers the second operation (C+1) on Partition 2.
7. Partition 2 repeats the Raft consensus, event execution, and CQRS sync steps.
8. Upon success, the Saga coordinator marks the transaction complete and responds to the client.

#### 10. What is the impact of out-of-order execution in Try-Cancel/Confirm (TCC) distributed transactions?
**Answer:**
Out-of-order execution can cause cancel instructions to arrive at a database shard before the corresponding try instruction due to network delays (e.g., account C receiving a Cancel before Try), requiring the transaction participant to gracefully handle orphan cancel operations.

#### 11. What is the primary difference between 2PC (Two-Phase Commit) and 3PC (Three-Phase Commit)?
**Answer:**
2PC consists of a prepare phase and a commit phase, and can block if the coordinator fails permanently. 3PC introduces a pre-commit phase and non-blocking properties under certain network assumptions, though it is rarely used in practice due to network partition complexities.

#### 12. Why might distributed transactions fail to solve all consistency or business logic issues in a digital wallet system?
**Answer:**
Distributed transactions handle atomicity across nodes, but they do not prevent application-level logic errors (e.g., users entering incorrect transfer amounts). Systems also require audit logs and trace mechanisms to track root causes of application errors.


## 📂 Category: Distributed Transactions & Event Sourcing (1 cards)

### 🔴 Senior Level

#### 1. How do event sourcing commands operate within a wallet service?
**Answer:**
Balance transfer requests are submitted as commands into a FIFO queue (e.g., Apache Kafka). A state machine processes each command sequentially in FIFO order against state stored in a relational database. For each command (e.g., 'A -> $1 -> C'), the state machine validates sufficient account balances and generates corresponding immutable events (e.g., 'A: -$1' and 'C: +$1').


## 📂 Category: Distributed Transactions & Payments (5 cards)

### 🟡 Mid Level

#### 1. What are common system and external factors that cause end-to-end payment requests to stall for hours or days?
**Answer:**
While most payment requests complete within seconds, transactions can stall due to:
- Risk management: The Payment Service Provider (PSP) flags the request as high-risk, triggering mandatory manual human review.
- Authentication protocols: Extra security layers like 3D Secure Authentication require interactive cardholder validation steps.

#### 2. What is the typical sequence of steps in a payment pay-in flow?
**Answer:**
1. Payment event generated and stored in DB.
2. Payment service calls payment executor for orders.
3. Executor calls external PSP for credit card processing.
4. Wallet service updates seller balance.
5. Ledger service appends new ledger entry.


### 🔴 Senior Level

#### 1. How do Payment Service Providers (PSPs) handle long-running payment requests?
**Answer:**
The PSP returns a 'pending' status to the client, which displays a status-check page to the user. The PSP tracks the pending payment and notifies the payment service via a registered webhook upon completion. Alternatively, the payment service periodically polls the PSP for status updates.

#### 2. How do you ensure data consistency in a distributed payment system?
**Answer:**
To maintain internal service consistency, ensuring exactly-once processing is critical. For external Payment Service Providers (PSPs), rely on idempotency keys for retry operations and implement periodic reconciliation, as external systems cannot be assumed to be always correct.

#### 3. How do you handle idempotency and payment retries when a PSP response fails due to network errors?
**Answer:**
Use a nonce-to-token mapping strategy: The payment service sends a unique nonce (representing the payment order) to the Payment Service Provider (PSP). The PSP returns a corresponding token that uniquely maps back to the nonce and order. This token acts as the idempotency key on the PSP side. If a user retries (clicks 'pay' again), the same token is sent, allowing the PSP to identify the duplicate transaction and return the status of the previous execution safely.


## 📂 Category: Distributed Transactions & Resilience (1 cards)

### 🟡 Mid Level

#### 1. What are the standard payment retry strategies in distributed transactional workflows?
**Answer:**
- Immediate retry: Client instantly resends the request.
- Fixed intervals: Static wait time between attempts.
- Incremental intervals: Gradually increasing wait times per retry.
- Exponential backoff: Doubling the wait interval after each failure (e.g., 1s, 2s, 4s).
- Cancel: Aborting retries when failures are permanent or repetitive calls are futile.


## 📂 Category: Distributed Transactions & Storage (1 cards)

### 🔴 Senior Level

#### 1. What is the impact of replication on payment systems and how is it managed?
**Answer:**
Replication lag can cause data inconsistencies between primary and replica databases. To prevent this in financial systems, architectures either route all reads and writes exclusively through the primary database (sacrificing replica utility for simplicity) or enforce strict synchronous replication using consensus algorithms like Paxos/Raft or consensus-based databases like CockroachDB.


## 📂 Category: Domain Modeling (2 cards)

### 🟢 Junior Level

#### 1. What does a candlestick chart represent in financial systems?
**Answer:**
A candlestick chart displays the price movement of an asset over a specific time interval (e.g., 1-minute, 1-day). Each candlestick explicitly shows the market's open, close, high, and low prices for that period.


### 🔴 Senior Level

#### 1. What are the core data models for products, orders, and executions in a stock exchange system?
**Answer:**
1) Product: Attributes of a traded symbol (type, trading symbol, display symbol, settlement currency, lot size, tick size). Highly cacheable, rarely changes, used for UI. 2) Order: Inbound instruction for a buy or sell action. 3) Execution (Fill): Outbound matched result. Not every order produces an execution; matches generate two executions representing the buy and sell sides.


## 📂 Category: Domain-Specific Architecture (2 cards)

### 🟡 Mid Level

#### 1. How do retail clients interact with stock exchanges compared to institutional clients?
**Answer:**
Retail clients trade via consumer-facing brokers (e.g., Robinhood, Fidelity) using standard user interfaces. Institutional clients (pension funds, hedge funds) trade in large volumes via specialized software, requiring advanced features like order splitting for large blocks or ultra-low latency setups for market making.


### 🔴 Senior Level

#### 1. What is the primary function of a stock exchange matching engine?
**Answer:**
To process billions of transactions daily by efficiently matching buyers and sellers for equities, derivatives, and other financial instruments while maintaining determinism, high throughput, and low latency.


## 📂 Category: Event Sourcing & Architecture (2 cards)

### 🟡 Mid Level

#### 1. What is the function of the state machine in event sourcing?
**Answer:**
A state machine drives the event sourcing process and has two major functions: validating commands and generating events, and applying events to update the state.


### 🔴 Senior Level

#### 1. What is the hot-warm matching engine in event sourcing?
**Answer:**
The hot matching engine works as the primary instance, while the warm engine receives and processes the exact same events without emitting outbound messages. If the primary goes down, the warm instance immediately takes over. State recovery is made reliable and deterministic via the underlying event store.


## 📂 Category: Event Sourcing & CQRS (2 cards)

### 🔴 Senior Level

#### 1. How are state machines used in CQRS and Event Sourcing?
**Answer:**
Read-only state machines can derive different state representations from the event queue. For example, one can serve user balance queries, while another builds state for specific time periods to investigate issues like potential double charges. The state information acts as an audit trail to reconcile financial records and enables answering historical queries by replaying events from the start.

#### 2. How can we optimize reproducibility and performance in event-sourced systems?
**Answer:**
To optimize reproducibility, use periodic 'snapshots'—saving the current state of the state machine into a file so it doesn't need to reprocess the entire event log from inception every time. For file-based event sourcing performance, use `mmap` to map local disk files to memory arrays, caching recent content and leveraging OS-level optimizations for fast append-only operations.


## 📂 Category: Event-Driven Architecture (3 cards)

### 🟡 Mid Level

#### 1. What is a consumer group in Kafka and how does it function?
**Answer:**
A consumer group is a set of independent consumer instances working together to consume messages from topics. Each consumer group can subscribe to multiple topics, maintain its own independent consuming offsets, and process traffic in parallel. When multiple groups subscribe to the same topic, it enables the publish-subscribe messaging pattern where each group receives a full copy of the message stream.


### 🔴 Senior Level

#### 1. What is functional determinism?
**Answer:**
Functional determinism is a property where the absolute real-world time of an event is secondary, and the primary constraint is the strict order of events. Event timestamps from discrete uneven intervals in time can be mapped, significantly reducing the time and resources spent on replay and disaster recovery.

#### 2. What is the difference between an event and a command?
**Answer:**
A command represents an intention to perform an action (may contain randomness, I/O, or generate zero or more events), whereas an event represents a validated historical fact (must be deterministic, written in the past tense, and stored in a FIFO queue following the order of commands).


## 📂 Category: External APIs & Services (1 cards)

### 🟢 Junior Level

#### 1. How is a geocoding service utilized in mapping and navigation systems?
**Answer:**
It resolves textual or place-name addresses into latitude and longitude coordinate pairs (e.g., via Google's Geocoding API). Navigation services call this service for origin and destination points before passing the coordinates downstream for route finding.


## 📂 Category: Fault Tolerance (2 cards)

### 🔴 Senior Level

#### 1. How do we handle temporary and permanent failures in distributed key-value stores?
**Answer:**
Use hinted handoff to handle temporary replica failures. For permanently unavailable replicas, implement an anti-entropy protocol to sync data across replicas. Merkle trees are used for efficient inconsistency detection and minimizing data transfer amounts.

#### 2. What is a systematic error or failure in distributed systems?
**Answer:**
Correlated faults across nodes that are hard to anticipate and trigger widespread failures. Examples include software bugs exposed by specific inputs (e.g., leap second kernel hangs), runaway resource consumption (CPU, memory, disk), cascading failures, or dependent downstream services returning corrupted data.


## 📂 Category: Fault Tolerance & High Availability (1 cards)

### 🔴 Senior Level

#### 1. What are typical failure scenarios and mitigation strategies in a large-scale video streaming pipeline?
**Answer:**
1) Upload/Transcoding errors: retry operation. 2) Video split/GOP alignment errors: perform splitting server-side if clients lack support. 3) Preprocessor/DAG scheduler failures: regenerate DAG / reschedule tasks. 4) Resource manager queue down: failover to a replica. 5) API servers down: traffic routes to other stateless API servers. 6) Metadata cache/DB down: leverage read replicas, promote standby master, or replace dead nodes.


## 📂 Category: Fault Tolerance & Stream Processing (1 cards)

### 🔴 Senior Level

#### 1. How is fault tolerance and recovery implemented in an in-memory aggregation service?
**Answer:**
Since aggregation state is held in-memory, crashes result in data loss. Fault tolerance is achieved by periodically persisting system status and window metrics (e.g., top N items) to snapshots. Upon failure, a new node recovers from the latest snapshot and replays only the delta events subsequently published by upstream message brokers like Kafka.


## 📂 Category: FinTech Systems (1 cards)

### 🟡 Mid Level

#### 1. What are the three tiers of market data levels in financial systems?
**Answer:**
L1 (Level 1): Best bid price, ask price, and quantities. 
L2: Expanded price levels beyond L1. 
L3: Detailed price levels including the queued order book quantity at each specific price level.


## 📂 Category: Financial Systems (11 cards)

### 🟢 Junior Level

#### 1. What is a ledger in financial payment systems?
**Answer:**
The ledger keeps a financial record of payment transactions (e.g., debiting $1 from a user and crediting $1 to a seller). The ledger system is crucial for post-payment analysis, such as calculating total e-commerce revenue or forecasting future revenue.

#### 2. What is a payment system?
**Answer:**
A payment system is any system used to settle financial transactions through the transfer of monetary value, encompassing the institutions, instruments, people, rules, procedures, standards, and technologies that make exchange possible.


### 🟡 Mid Level

#### 1. What is a card scheme?
**Answer:**
A card scheme is the network organization (such as Visa, MasterCard, or Discover) that sets the rules, manages the infrastructure, and coordinates the processing of credit and debit card transactions between acquiring and issuing banks.

#### 2. What is a limit order?
**Answer:**
A limit order is a buy or sell order with a fixed price. It might not find a match immediately, or it might just be partially matched.

#### 3. What is a market order?
**Answer:**
A market order doesn’t specify a price. It is executed at the prevailing market price immediately. A market order sacrifices cost control in order to guarantee execution, which is useful in fast-moving market conditions.

#### 4. What is a payment executor?
**Answer:**
The payment executor executes a single payment order via a Payment Service Provider (PSP). A single payment event may contain several payment orders.

#### 5. What is an order book?
**Answer:**
An order book is a list of buy and sell orders for a specific security or financial instrument, organized by price level. It serves as a core data structure in a financial matching engine for rapid order matching.


### 🔴 Senior Level

#### 1. What functional capabilities, order types, regulatory constraints, and financial checks must be designed for a high-throughput stock exchange?
**Answer:**
1. Securities & Hours: Equity trading restricted to standard market trading hours.
2. Operations: Support for placing and canceling limit orders; real-time order book visibility and trade matching.
3. Scale & Performance: Tens of thousands of concurrent users, at least 100 symbols, and billions of orders per day.
4. Risk & Compliance: Mandatory pre-trade risk checks (e.g., max 1 million share limit per user per day).
5. Wallet Management: Synchronous capital verification and fund withholding for open orders to prevent overspending.

#### 2. What is the architectural role of the reporting flow in a high-throughput trading system?
**Answer:**
The reporter sits off the critical trading path to handle trading history, tax reporting, compliance, and settlements. While less sensitive to low latency, it requires high accuracy and compliance. It merges data attributes from both incoming orders and outgoing executions.

#### 3. What is the role of an order manager in a trading system?
**Answer:**
The order manager receives inbound orders from the client gateway and manages their lifecycle states. It performs risk checks (e.g., verifying trade volume is below a daily limit), validates sufficient funds against the user's digital wallet, and sends the validated order to a sequencer to be stamped with a sequence ID before processing by the matching engine. It optimizes transmission size by sending only necessary attributes.

#### 4. What operational factors, security boundaries, and integration flows must be considered when designing a global e-commerce payment system?
**Answer:**
1. Integration: Utilization of third-party payment gateways (Stripe, Braintree, Square) to offload sensitive credit card handling.
2. Compliance & Security: Zero raw storage of credit card data to meet strict PCI DSS security mandates.
3. Scope: Support for credit cards, PayPal, bank cards, multi-currency international flows, and payout flows for marketplace sellers.
4. Scale: 1 million transactions per day.
5. Reliability: Implementation of automated financial reconciliation jobs to resolve state discrepancies across internal accounting services and external payment service providers.


## 📂 Category: Fintech & Payments (3 cards)

### 🟡 Mid Level

#### 1. What are the regulatory benefits of using a hosted payment page?
**Answer:**
Using hosted payment pages (such as PSP-provided iframes, widgets, or SDKs) allows companies to avoid capturing and storing credit card data directly, thereby bypassing the complex and stringent compliance requirements of the Payment Card Industry Data Security Standard (PCI DSS).

#### 2. What is the FIX protocol in financial systems?
**Answer:**
FIX (Financial Information eXchange) protocol is a vendor-neutral communications protocol created in 1991 specifically for exchanging securities transaction information electronically.


### 🔴 Senior Level

#### 1. What is a double-entry ledger system and why is it essential for payment systems?
**Answer:**
Also called double-entry bookkeeping, it is fundamental to payment systems and accurate accounting. It records every transaction into two separate ledger accounts with the same amount (one debited, one credited), ensuring the sum of all entries equals zero. This provides end-to-end traceability, maintains strict consistency, and guarantees that one account's loss is another's gain.


## 📂 Category: Fintech Systems (3 cards)

### 🟡 Mid Level

#### 1. What are the pay-in and pay-out flows in a payment system architecture?
**Answer:**
Pay-in flow: Money flows from the buyer's payment source into the platform's merchant/custodial bank account after an order is placed. Pay-out flow: After goods/services are delivered, the balance (minus platform fees) flows from the platform's bank account to the seller's bank account.

#### 2. What is the role of the payment service and its integration with risk management?
**Answer:**
The payment service accepts payment events and coordinates processing. It first initiates a risk check (often via a specialized third-party provider) to assess compliance with regulations like AML/CFT and screen for criminal activities like money laundering before processing transactions.


### 🔴 Senior Level

#### 1. What are the key processing steps in a stock exchange market data flow?
**Answer:**
Step M1: The matching engine generates an execution (fill) stream and sends it to the market data publisher. Step M2: The publisher constructs candlestick charts and order books from the stream and sends them to the data service. Step M3: Market data is written to specialized storage for real-time analytics, while brokers fetch data via the data service to relay to clients.


## 📂 Category: Frontend Architecture (1 cards)

### 🟡 Mid Level

#### 1. How is map rendering optimized using the tiling technique?
**Answer:**
Instead of rendering an entire map as a single massive image, the world is broken down into smaller 256x256 pixel tiles organized across various zoom levels. Clients dynamically download and stitch together only the relevant tiles for their current viewport, saving bandwidth and optimizing performance.


## 📂 Category: Fundamentals (1 cards)

### 🟢 Junior Level

#### 1. What is a byte?
**Answer:**
A byte is a unit of digital information that consists of a sequence of 8 bits.


## 📂 Category: Game Architecture & Real-Time Systems (1 cards)

### 🟢 Junior Level

#### 1. Should the client communicate directly with the leaderboard service to set scores?
**Answer:**
No. Allowing the client to set scores directly is insecure and vulnerable to man-in-the-middle attacks (e.g., proxies modifying scores). Scores must be set server-side. For server-authoritative games (like online poker), the game server handles all logic and updates scores internally without client intervention.


## 📂 Category: Geo-Distributed Systems (1 cards)

### 🔴 Senior Level

#### 1. Describe a naive algorithmic solution and its time complexity for adaptive ETA and rerouting in navigation systems.
**Answer:**
Each active user's route is represented as an ordered sequence of routing tiles (r_1, r_2, ..., r_k). The database maintains active user routing tables. When a traffic incident occurs in a specific tile (e.g., r_2), a naive approach scans every single active user row and checks if r_2 is present in their tile list. If n is the number of active users and m is the average length of a route, the time complexity to find all affected users is O(n * m), which fails to scale for millions of concurrent users.


## 📂 Category: Geospatial Systems (14 cards)

### 🟢 Junior Level

#### 1. How are geographical locations represented using a positioning system?
**Answer:**
Using Latitude (Lat), which denotes how far north or south a point is from the equator, and Longitude (Long), which denotes how far east or west it is from the prime meridian, mapping points on a rotating spherical coordinate system.

#### 2. How can precomputed map images optimize map rendering performance for clients?
**Answer:**
Rendering nearby roads and generating map images dynamically on demand involves heavy, redundant computations. To avoid this, map images are precomputed across various zoom levels and stored in cloud object storage (e.g., Amazon S3) backed by a CDN for rapid global delivery.

#### 3. What is the route planner service?
**Answer:**
A service that computes a suggested route optimized for travel time according to current traffic and road conditions.


### 🟡 Mid Level

#### 1. How can geospatial index tables be structured for a proximity service using Geohashes?
**Answer:**
Option 1: A single row per geohash key containing a JSON array of all business IDs within that region.
Option 2: Multiple rows per geohash, with one row per individual business ID located in that geohash block.

#### 2. How do you handle complex filtering (e.g., businesses open now or specific types) when using spatial indexing like geohash or quadtree?
**Answer:**
When the world is divided into small grids with geohash or quadtree, the number of businesses returned from the search result is relatively small. Therefore, it is acceptable to return business IDs first, hydrate business objects, and filter them based on opening time or business type. This solution assumes opening time and business type are stored in the business table.

#### 3. How is Geohashing utilized in mapping software?
**Answer:**
Geohashing encodes geographic areas into short strings of letters and digits by recursively dividing a flattened surface into a grid of sub-grids (represented by numbers 0 to 3). In mapping architectures, geohashing is primarily used for map tiling and spatial indexing.

#### 4. What are the core characteristics of a location-based service (LBS)?
**Answer:**
An LBS finds nearby businesses for a given radius and location. Characteristics include: 1) Read-heavy service with no write requests, 2) High QPS, especially during peak hours in dense areas, 3) Stateless architecture, making it easy to scale horizontally.

#### 5. What are the non-functional requirements for a location-based proximity service?
**Answer:**
1. Low latency for real-time nearby business discovery.
2. Data privacy compliance (GDPR, CCPA, etc.) regarding sensitive location data.
3. High availability and scalability to handle traffic spikes during peak hours in densely populated areas.

#### 6. What does Geohashing guarantee?
**Answer:**
Geohashing guarantees that the longer a shared prefix is between two geohashes, the closer they are geographically.

#### 7. What is a Nearby Friends feature architectural pattern?
**Answer:**
For an opt-in user who grants permission to access their location, the mobile client periodically reports location updates and presents a list of friends who are geographically nearby using spatial indexing (e.g., Geohash, H3) and pub/sub or polling.


### 🔴 Senior Level

#### 1. How can hierarchical routing tiles be used to optimize adaptive ETA and traffic rerouting calculations?
**Answer:**
Keep a hierarchical stack of routing tiles for each active user (current tile, parent tile, grandparent tile up to destination). When traffic changes, check if the affected routing tile intersects with the highest-level tile of a user's row to quickly filter out unaffected users. For recovery, track possible routes, continuously recalculate ETAs, and notify users if shorter alternative paths become available.

#### 2. How would you design a nearby friends location-sharing feature to support broadcasting updates to random opted-in users using pub/sub channels?
**Answer:**
Divide the geographical area into grids using Geohash, creating a pub/sub channel for each grid. When a user updates their location, compute their Geohash ID and publish to that channel. To handle boarder cases, clients can subscribe to their current Geohash grid plus the eight surrounding grids.

#### 3. What are the memory requirements and sizing calculations for a quadtree index in a proximity service?
**Answer:**
Example calculation: Assuming each grid stores a maximum of 100 businesses, for 200 million businesses, leaf nodes = ~2 million. Internal nodes = 2 million * 1/3 = ~0.67 million. Total memory requirement = (2 million * 832 bytes) + (0.67 million * 64 bytes) = ~1.71 GB. The quadtree index fits easily in a single server's memory, but read/network bandwidth limits may require scaling out read replicas.

#### 4. What is the shortest-path service and how does it function?
**Answer:**
A service that receives origin and destination lat/lng pairs and returns top-k shortest paths without considering real-time traffic (relying purely on road structure, making caching effective). It converts coordinates to geohashes, loads routing tiles from object storage, and runs a variation of the A* pathfinding algorithm across hierarchical tile graphs, dynamically hydrating neighboring or higher-level resolution tiles as needed.


## 📂 Category: High Availability (5 cards)

### 🟢 Junior Level

#### 1. In the context of load balancing and database replication, what happens if a master database goes offline?
**Answer:**
A slave (replica) database will be promoted to become the new master to restore write capabilities.

#### 2. What is a single point of failure (SPOF)?
**Answer:**
A specific component or node in a system that, if it fails, causes the entire system or application to halt operations entirely.


### 🟡 Mid Level

#### 1. Explain active-passive vs active-active setup
**Answer:**
Active-passive involves one primary node handling traffic while a secondary standby node replicates state and takes over on failure (high availability, simpler replication). Active-active splits traffic across multiple nodes simultaneously, requiring complex distributed consensus or conflict resolution to handle concurrent writes safely.


### 🔴 Senior Level

#### 1. How is tolerance to losing entire machines implemented in modern distributed systems?
**Answer:**
There is a move toward systems that can tolerate the loss of entire machines by using software fault-tolerance techniques in preference to or in addition to hardware redundancy. Such systems also have operational advantages: a single-server system requires planned downtime to reboot for patches, whereas a failure-tolerant system can be patched one node at a time without downtime.

#### 2. What are the architectural challenges of a basic single-server hot-warm matching engine?
**Answer:**
It is limited to a single server's boundaries. Extending it for high availability across multiple machines or data centers requires replicating the entire event store, which takes time. Reliable UDP is often needed to efficiently broadcast event messages to warm servers.


## 📂 Category: High Availability & Disaster Recovery (2 cards)

### 🟢 Junior Level

#### 1. What happens to traffic when a data center goes offline?
**Answer:**
All incoming traffic is dynamically redirected (typically via global traffic management tools like GeoDNS or Anycast) to a healthy, operational secondary data center.


### 🔴 Senior Level

#### 1. How do large-scale tech companies mitigate the catastrophic risk of warm instances or primary data centers going down?
**Answer:**
They replicate core data and traffic across data centers located in multiple distinct geographical cities/regions. This mitigates the risk of catastrophic events such as large-scale power outages or natural disasters like earthquakes.


## 📂 Category: High Availability & Resilience (1 cards)

### 🔴 Senior Level

#### 1. How is high availability achieved in a stock exchange system?
**Answer:**
To achieve 4 nines (99.99%) availability (max 8.64 seconds of downtime daily), systems must eliminate single points of failure by deploying redundant instances (e.g., matching engines), implement rapid failure detection and automated failover, horizontally scale stateless components (client gateways), and securely replicate state across replicas for stateful components (order managers).


## 📂 Category: High Availability & Scalability (2 cards)

### 🟢 Junior Level

#### 1. How does adding a load balancer and multiple web servers resolve single-point-of-failure and availability issues?
**Answer:**
If Server 1 goes offline, the load balancer automatically reroutes all incoming traffic to healthy instances like Server 2, preventing total downtime. Additional web servers can be dynamically provisioned and added to the pool as traffic grows, allowing the load balancer to distribute the load gracefully.

#### 2. What should we do if a website starts getting a lot of traffic from many countries?
**Answer:**
To improve availability and provide a better user experience across wider geographical areas, supporting multiple data centers is crucial.


## 📂 Category: High-Frequency Trading & Exchanges (3 cards)

### 🔴 Senior Level

#### 1. Besides generating sequence IDs, what other roles does a sequencer play in a trading exchange?
**Answer:**
The sequencer functions as a message queue (routing incoming orders to the matching engine and executions back to the order manager) and acts as an immutable event store for orders and executions, serving a role similar to an ultra-low-latency event stream.

#### 2. How do order managers and matching engines interact in an exchange architecture?
**Answer:**
The order manager sends incoming orders through the sequencer to the matching engine, and receives execution reports back from the matching engine to return to brokers via the client gateway.

#### 3. What is the architectural pattern of modern high-performance financial exchanges?
**Answer:**
Surprisingly, many large exchanges run almost everything on a single gigantic, highly optimized server to minimize network hop latency and locking overhead, utilizing fast sequencers and deterministic matching engines.


## 📂 Category: High-Frequency Trading & FinTech (3 cards)

### 🔴 Senior Level

#### 1. How are ledger and state mismatches handled during reconciliation?
**Answer:**
Mismatches found during financial reconciliation are routed to specific handling workflows: classifiable mismatches with low automation costs are fixed via automated adjustment programs; classifiable mismatches with high automation costs are sent to a job queue for manual finance team resolution; and unclassifiable mismatches are sent to a separate queue for investigation.

#### 2. How are orders, executions, and data archived in stock exchange flows?
**Answer:**
In the critical trading path, orders and executions bypass databases to achieve high performance, executing trades in-memory while persisting to hard disk or shared memory (such as a sequencer) for fast recovery. A reporter process writes orders/executions to a database for reconciliation and tax reporting, while executions are forwarded to market data processors to build order books and charts.

#### 3. How are snapshots utilized in financial applications and event sourcing?
**Answer:**
Snapshots in financial event-sourcing systems capture the exact state of an entity at a specific time (e.g., 00:00). Instead of replaying an event log from the beginning, read-only state machines load the latest snapshot file (often stored in object storage like HDFS) to quickly verify transactions, utilizing maximum hardware I/O throughput.


## 📂 Category: High-Frequency Trading & Real-Time Systems (3 cards)

### 🔴 Senior Level

#### 1. How do Market Data Publishers (MDP) handle optimizations, order book rebuilding, and lock-free ring buffers?
**Answer:**
MDP receives matched results, rebuilds order books/candlesticks, and publishes data to subscribers with varying access levels (e.g., L2 vs L3). To prevent memory bloat, candlestick growth has upper limits. Architecturally, it utilizes lock-free ring buffers (circular fixed-size queues with pre-allocated space and no dynamic allocation), incorporating cache-line padding to isolate sequence numbers.

#### 2. What are common order matching algorithms used in trading systems and dark pools?
**Answer:**
Various algorithmic models exist, such as FIFO with LMM (Lead Market Maker), which allocates a guaranteed quantity to the LMM based on a pre-negotiated ratio ahead of the standard FIFO queue.

#### 3. What are the core non-functional requirements for designing a stock exchange system?
**Answer:**
- Availability: At least 99.99% uptime.
- Fault tolerance: Rapid recovery to limit production impact.
- Latency: Sub-millisecond round-trip latency, with a strong focus on 99th percentile (p99) latency.
- Security: Account management, KYC (Know Your Client) verification, and DDoS mitigation.


## 📂 Category: Infrastructure (1 cards)

### 🟡 Mid Level

#### 1. What is the first line of defense against hardware and hard disk failures in infrastructure?
**Answer:**
Adding component-level redundancy. Examples include setting up disks in a RAID configuration, equipping servers with dual power supplies and hot-swappable CPUs, and utilizing backup batteries and diesel generators for datacenters to ensure continuous uptime during hardware faults.


## 📂 Category: Infrastructure & Networking (1 cards)

### 🔴 Senior Level

#### 1. What strategies improve email deliverability and sender reputation?
**Answer:**
Use dedicated IPs for sending, warm up new IPs slowly over 2-6 weeks, and classify emails to separate marketing from transactional traffic. Set up feedback loops with ISPs to handle hard bounces, soft bounces, and spam complaints quickly. Implement authentication protocols including SPF, DKIM, and DMARC to prevent spoofing.


## 📂 Category: Infrastructure & Operations (1 cards)

### 🟢 Junior Level

#### 1. What is the role of automation in scaling up systems?
**Answer:**
Automation is used to reduce manual operational work, increase execution efficiency, and ensure configuration and deployment consistency across distributed nodes.


## 📂 Category: Infrastructure & Virtualization (1 cards)

### 🟢 Junior Level

#### 1. Explain the difference between containers and VMs
**Answer:**
Virtual Machines (VMs) virtualize physical hardware using a hypervisor, running a full guest operating system on top of a virtualized CPU, RAM, and disk, resulting in higher resource overhead and slower startup times. Containers virtualize the operating system kernel, sharing the host OS kernel while isolating user-space processes via Linux namespaces and cgroups, making them lightweight, portable, and fast to boot.


## 📂 Category: Integration & Messaging (2 cards)

### 🟢 Junior Level

#### 1. How are third-party integrations like SMS implemented in distributed systems?
**Answer:**
Third-party commercial APIs (such as Twilio, Nexmo, etc.) are commonly used to handle external channels like SMS messages, decoupling the core application logic from telecommunication infrastructure via asynchronous API calls and webhooks for delivery status tracking.

#### 2. How is email notification integration commonly implemented in modern backends?
**Answer:**
Rather than self-hosting and managing email servers, backends typically integrate with commercial third-party email services like SendGrid or Mailchimp via APIs to ensure higher deliverability rates and built-in data analytics.


## 📂 Category: Interview Strategy (3 cards)

### 🟢 Junior Level

#### 1. What are common red flags to avoid during a system design interview?
**Answer:**
1) Over-engineering (prioritizing design purity and ignoring real-world tradeoffs and compounding costs); 2) Jumping straight into a solution without clarifying requirements; 3) Getting bogged down in low-level details of a single component too early; 4) Narrow-mindedness and stubbornness.

#### 2. What is the best approach to propose a high-level system design and secure buy-in during an interview?
**Answer:**
Start by establishing an initial blueprint, treating the interviewer as a collaborative teammate. Draw box diagrams for core components (clients, APIs, web servers, data stores, caches, CDNs, message queues). Use back-of-the-envelope calculations to validate scale constraints and communicate assumptions clearly before diving deeper.

#### 3. What is the recommended time allocation for a 45-minute system design interview session?
**Answer:**
Step 1: Understand the problem and establish design scope (3 - 10 mins). Step 2: Propose high-level design and get buy-in (10 - 15 mins). Step 3: Design deep dive (10 - 25 mins). Step 4: Wrap up and summarize (3 - 5 mins).


## 📂 Category: LBS & Geospatial (3 cards)

### 🟢 Junior Level

#### 1. What is Geocoding and Reverse Geocoding?
**Answer:**
Geocoding is the process of converting human-readable addresses (e.g., '1600 Amphitheatre Parkway, Mountain View, CA') into geographic coordinates (latitude/longitude pairs like 37.423021, -122.083739). Reverse geocoding is the exact opposite: converting latitude/longitude coordinates back into a human-readable address. Common implementation methods include interpolation using geographic information systems (GIS) data.


### 🟡 Mid Level

#### 1. What is Geohash?
**Answer:**
Geohash is a hierarchical spatial index that converts two-dimensional longitude and latitude coordinates into a compact, one-dimensional string of letters and digits. It works by recursively subdividing the earth's surface into smaller and smaller grids with each additional bit or character.


### 🔴 Senior Level

#### 1. What is Google S2 geometry library?
**Answer:**
Google S2 is an in-memory spatial indexing library that maps a 2D sphere to a 1D index using a space-filling curve known as the Hilbert curve. Because points close to each other on a Hilbert curve remain close in 1D space, spatial searches and range queries become significantly more efficient compared to 2D space searches.


## 📂 Category: Load Balancing (3 cards)

### 🟢 Junior Level

#### 1. Explain health checks in load balancing
**Answer:**
Periodic probes (HTTP GET, TCP handshake) sent by a load balancer to backend servers to verify availability and performance. Unhealthy servers are automatically removed from the active routing pool until they recover, ensuring fault tolerance.

#### 2. What are the main load balancing algorithms?
**Answer:**
Common load balancing algorithms include Round Robin, Weighted Round Robin, Least Connections, Weighted Least Connections, IP Hash, and Least Response Time.

#### 3. What is session persistence (sticky sessions)?
**Answer:**
Session persistence, or sticky sessions, is a load balancing technique that ensures all requests from a specific client session are routed to the same backend server, maintaining state consistency across requests.


## 📂 Category: Location-Based Services (2 cards)

### 🟡 Mid Level

#### 1. Describe the WebSocket and HTTP API design for a nearby friends tracking application.
**Answer:**
Uses WebSocket for real-time bidirectional communication: periodic location updates (latitude, longitude, timestamp), receiving location updates, WebSocket initialization, and subscribing/unsubscribing to friends. HTTP requests handle non-real-time operations like adding/removing friends and updating user profiles.

#### 2. Describe the business service architecture and request patterns in a proximity service.
**Answer:**
The business service handles two core traffic patterns: 1) Write operations (create, update, delete businesses by owners) with low QPS, and 2) Read operations (customers viewing detailed business information) with high QPS during peak hours.


## 📂 Category: Low-Latency Systems (3 cards)

### 🔴 Senior Level

#### 1. How are application loops structured in a stock exchange system?
**Answer:**
An application loop is a single-threaded while loop that continuously polls and executes mission-critical tasks to meet strict latency budgets and guarantee predictable 99th percentile execution times. To maximize CPU efficiency, each component runs as a separate process with its thread pinned to a fixed CPU core.

#### 2. How do you minimize latency on the critical path of a high-performance stock exchange system?
**Answer:**
Streamline the critical execution path to contain only absolute essentials. For example, the critical trading path is restricted to: gateway -> order manager -> sequencer -> matching engine. Non-essential synchronous tasks, such as logging, are stripped from the critical path to achieve ultra-low latency.

#### 3. What are the latency requirements of a stock exchange system?
**Answer:**
Latency is critical for a stock exchange. Both average latency must be low, and the overall latency must remain stable. A standard measure for stability is the 99th percentile (p99) or 99.9th percentile latency.


## 📂 Category: Media Streaming (2 cards)

### 🟢 Junior Level

#### 1. Why is video transcoding important in system design?
**Answer:**
Raw video consumes massive storage (e.g., hundreds of GBs for an hour at 60fps). Transcoding ensures compatibility across various devices and browsers, and enables adaptive bitrate streaming to match changing network conditions (delivering higher resolution to high-bandwidth users and lower resolution to low-bandwidth users).


### 🔴 Senior Level

#### 1. What are the key components of the video uploading and processing pipeline in a streaming service?
**Answer:**
Components include Client, Load Balancer, API Servers, Metadata DB/Cache (sharded/replicated), Original Storage (Blob storage for raw inputs), Transcoding Servers (converting formats like HLS/MPEG), Transcoded Storage, CDN, Completion Queue (message queue for events), and Completion Handler workers updating the metadata state.


## 📂 Category: Message Brokers & Streaming (1 cards)

### 🟡 Mid Level

#### 1. What concurrency issue occurs when reading data in parallel from a message broker, and how is it mitigated?
**Answer:**
Reading in parallel from multiple consumers on the same partition breaks message order guarantees. This is mitigated by enforcing a constraint that a single partition can only be consumed by one consumer within the same consumer group.


## 📂 Category: Messaging & Event Streaming (2 cards)

### 🟡 Mid Level

#### 1. Explain the difference between Apache Kafka and RabbitMQ
**Answer:**
Apache Kafka is a distributed, append-only log optimized for high-throughput, log aggregation, and stream processing where consumers pull messages and retain them based on time/space configurations. RabbitMQ is a traditional message broker implementing AMQP, optimized for complex message routing, low-latency task queues, and push-based delivery where messages are typically deleted from queues once acknowledged by a consumer.

#### 2. What is the difference between point-to-point and publish-subscribe messaging models?
**Answer:**
In a point-to-point model, a message is sent to a queue and consumed by one and only one consumer; once acknowledged, it is removed. In a publish-subscribe model, a message is sent to a topic and received by all consumers subscribing to that topic. The publish-subscribe model is implemented via topics, while point-to-point can be simulated using consumer groups.


## 📂 Category: Messaging & Event-Driven (2 cards)

### 🟢 Junior Level

#### 1. What is a message queue?
**Answer:**
A message queue is a durable component, stored in-memory/disk, that supports asynchronous communication. It serves as a buffer and distributes asynchronous requests. Producers/publishers create messages and publish them to the queue, while consumers/subscribers connect to the queue and perform actions defined by the messages.

#### 2. What is a topic in a message queue system?
**Answer:**
A logical category or channel used to organize messages within a message broker. Each topic has a globally unique name, acting as an abstraction where producers publish messages and consumers subscribe to read them.


## 📂 Category: Messaging & Event-Driven Architecture (6 cards)

### 🟢 Junior Level

#### 1. How do we prevent duplicate notification occurrences in distributed notification systems?
**Answer:**
Implement a deduplication mechanism using event IDs. When a notification event arrives, check a fast-lookup data store or cache to see if the event ID has been processed. If seen, discard it; otherwise, process and send the notification.

#### 2. How does a message queue contribute to system scalability?
**Answer:**
A message queue decouples producers and consumers asynchronously, allowing different components of a system to scale independently based on their respective load and throughput requirements.

#### 3. What are the key components and processes of a message queue?
**Answer:**
A message queue consists of: 1) Producers that send messages to the queue, 2) Consumers that subscribe to the queue and consume messages, and 3) The message queue service itself, which acts as the intermediary. Both producers and consumers act as clients communicating over the network with the queue server, decoupling them to operate and scale independently.


### 🟡 Mid Level

#### 1. What are the primary architectural benefits of introducing message queues?
**Answer:**
Decoupling (components evolve independently), improved scalability (producers/consumers scale separately based on load), increased availability (system resilience if a consumer goes offline), and better performance via asynchronous communication.

#### 2. What operational bottlenecks should be monitored in an email system's outgoing queue?
**Answer:**
The size of the outgoing queue must be monitored closely. Accumulating messages indicate recipient mail server unavailability (requiring exponential backoff retry strategies) or insufficient consumer worker pools (requiring horizontal scaling of consumers to lower processing latency).


### 🔴 Senior Level

#### 1. How do we scale message queues (like Kafka) in an ad click aggregation pipeline?
**Answer:**
Scale producers horizontally without limits. Scale consumers via consumer group rebalancing (adding/removing nodes), though large rebalances should be done off-peak. Use `ad_id` as the message partitioning key to guarantee ordering and localized processing. Pre-allocate sufficient partitions upfront to avoid production re-partitioning, and use physical topic sharding (by geography or business type) to boost system throughput and reduce rebalance times.


## 📂 Category: Messaging & Queues (2 cards)

### 🟢 Junior Level

#### 1. How can we scale SMTP outgoing workers independently in an email delivery system?
**Answer:**
Use a distributed message queue between the web servers and the SMTP outgoing workers. Since each message in the queue contains all metadata required to build an email, decoupling asynchronous processing allows the SMTP workers to scale independently based on queue depth.

#### 2. What is the benefit of using a message queue in asynchronous tasks (e.g., photo customization)?
**Answer:**
A message queue allows web servers (producers) to publish processing jobs without waiting for completion, while backend workers consume and execute tasks asynchronously. This decouples producers and consumers, enabling them to scale independently and smoothing out traffic spikes.


## 📂 Category: Messaging & Streaming (2 cards)

### 🟢 Junior Level

#### 1. What are the two main components of a message queue?
**Answer:**
The two main components of a message queue are producers/publishers and consumers/subscribers.


### 🔴 Senior Level

#### 1. What are the differences between traditional message queues and event streaming platforms?
**Answer:**
Traditional Message Queues (e.g., RabbitMQ): Retain messages in memory just long enough to be consumed, with small on-disk overflow capacity. Messages are typically acknowledged and removed, and strict global ordering is not always maintained.
Event Streaming Platforms (e.g., Kafka): High retention requirements storing large volumes of data on disk for extended periods. Provide partition-level ordering and allow multiple consumer groups to replay event streams independently.


## 📂 Category: Messaging Systems (1 cards)

### 🟡 Mid Level

#### 1. What is the typical traffic pattern and data access profile of a message queue or data streaming platform?
**Answer:**
Message queues and streaming platforms are typically write-heavy and read-heavy with predominantly sequential read/write access patterns. Traditional queues generally perform no updates or deletes unless falling behind. Distributed data streaming platforms (e.g., Kafka) persist messages immutably append-only, relying on offset tracking rather than in-place updates.


## 📂 Category: Microservices (2 cards)

### 🔴 Senior Level

#### 1. What is the Saga pattern in microservices?
**Answer:**
A distributed transaction management pattern where operations are executed in a sequential chain across independent microservice databases. If an operation fails, the Saga executes compensating transactions in reverse order to roll back the changes. For n operations, it requires 2n operations total (n normal, n compensating).

#### 2. Why is a hybrid microservices approach used in some transactional systems like hotel reservations, and how does it prevent concurrency issues?
**Answer:**
While traditional monoliths use shared relational databases for consistency, microservices often use isolated databases. A hybrid approach has the Reservation Service handle both reservation and inventory APIs so their tables reside in the same relational database. This leverages database ACID properties to gracefully manage concurrency issues during reservations.


## 📂 Category: Microservices & Networking (1 cards)

### 🟡 Mid Level

#### 1. How does a service mesh improve microservices architectures?
**Answer:**
A service mesh (e.g., Istio, Linkerd) abstracts service-to-service communication, security (mTLS), observability (metrics, tracing), and resilience patterns (retries, circuit breaking, rate limiting) out of application code and into dedicated sidecar proxies deployed alongside each service.


## 📂 Category: Microservices Architecture (1 cards)

### 🟢 Junior Level

#### 1. How do microservices communicate in high-performance production environments like hotel reservation systems?
**Answer:**
Inter-service communication in production microservice architectures frequently relies on modern, high-performance Remote Procedure Call (RPC) frameworks such as gRPC.


## 📂 Category: Mobile & LBS Architecture (1 cards)

### 🟡 Mid Level

#### 1. Why is peer-to-peer messaging impractical for implementing a 'nearby friends' feature on mobile devices?
**Answer:**
P2P is impractical due to mobile devices having flaky network connections and strict power consumption budgets. A practical architecture uses a shared backend to receive location updates, evaluate distance thresholds, and forward relevant updates to active friends.


## 📂 Category: Monitoring & Observability (2 cards)

### 🟡 Mid Level

#### 1. What are the metrics data collection models and their trade-offs?
**Answer:**
The two primary models are Pull (the monitoring system scrapes targets) and Push (targets send metrics to the monitoring system). There is an ongoing architectural debate regarding which model is superior depending on firewall configurations, target discovery, and network topology.


### 🔴 Senior Level

#### 1. What are the main topics and key components related to designing a metrics and alerting system?
**Answer:**
Key topics include: Metrics collection (Push vs Pull model), scaling the metrics transmission pipeline (utilizing Kafka), choosing the right time-series database, query service, storage layer, utilizing downsampling to reduce data size, alerting system, and visualization system (build vs buy options).


## 📂 Category: Network & Protocols (2 cards)

### 🟡 Mid Level

#### 1. How do we optimize file synchronization and network traffic in cloud storage?
**Answer:**
Apply two primary optimizations: 1) Delta sync, where only modified file blocks are synced instead of the entire file. 2) Compression, where blocks are compressed using algorithms tailored to file types (e.g., gzip/bzip2 for text, specialized algorithms for images and videos) to minimize network payload size.


### 🔴 Senior Level

#### 1. How do we guarantee distribution fairness of market data in stock trading exchanges?
**Answer:**
To prevent smart clients from racing to be first on connection lists, exchanges can use multicasting via reliable UDP to broadcast updates to all participants simultaneously, or assign a random order upon subscriber connection.


## 📂 Category: Network Protocols (2 cards)

### 🟢 Junior Level

#### 1. What is WebSocket and why is it used for server-to-client communication?
**Answer:**
WebSocket is a bi-directional, persistent protocol initiated by the client via an HTTP handshake. It allows servers to push asynchronous updates over a single TCP connection, often bypassing firewalls by operating on standard HTTP/HTTPS ports (80 or 443).


### 🟡 Mid Level

#### 1. Which delivery protocol is best suited for real-time navigation and live tracking clients?
**Answer:**
WebSocket is preferred over mobile push notifications (due to strict payload size limits like 4096 bytes on iOS and lack of web support), long polling, and Server-Sent Events (SSE). WebSocket provides lightweight, low-overhead, bi-directional real-time communication essential for features like dynamic route updates and last-mile delivery tracking.


## 📂 Category: Network Protocols & Communication (1 cards)

### 🟡 Mid Level

#### 1. What is long polling and what are its primary limitations?
**Answer:**
In long polling, a client holds an HTTP connection open until new messages are available or a timeout threshold is reached, after which it immediately sends a new request. Limitations include: 1. Stateless HTTP routing issues (sender and receiver may hit different servers if using round-robin load balancing), 2. Difficulty in detecting dead or disconnected clients, and 3. Inefficiency when message volume is low due to constant reconnection overhead.


## 📂 Category: Networking (12 cards)

### 🟢 Junior Level

#### 1. Explain DNS caching and TTL
**Answer:**
DNS caching stores domain-to-IP resolution mappings in resolvers, operating systems, or browsers to speed up subsequent requests. TTL (Time-To-Live) defines the expiration time in seconds for a DNS record, balancing DNS propagation speed against query load.

#### 2. Explain the key differences between TCP and UDP
**Answer:**
TCP (Transmission Control Protocol) is a connection-oriented, reliable transport protocol that guarantees ordered delivery, flow control, and error checking through handshakes and acknowledgments, though with higher latency overhead. UDP (User Datagram Protocol) is a connectionless, lightweight protocol that provides no guarantees regarding delivery, ordering, or duplicate protection, making it ideal for real-time streaming, VoIP, and gaming where speed outweighs reliability.

#### 3. How does DNS resolution work?
**Answer:**
DNS resolution translates human-readable domain names into IP addresses. It queries a recursive resolver, which checks root nameservers, TLD (Top-Level Domain) nameservers, and authoritative nameservers sequentially, utilizing caching at various layers to reduce latency.

#### 4. What is the TCP three-way handshake?
**Answer:**
The TCP three-way handshake is the connection-establishment process between a client and server: 
1. SYN: Client sends a segment with the SYN flag set and an initial sequence number. 
2. SYN-ACK: Server responds with a segment containing its own SYN flag, an acknowledgment number (Client's ISN + 1), and its own sequence number. 
3. ACK: Client sends an acknowledgment back to the server confirming receipt, completing the handshake.

#### 5. What is the purpose of the Domain Name System (DNS) in a single server setup?
**Answer:**
The DNS translates domain names, like api.mysite.com, into IP addresses.

#### 6. What is the role of a DNS resolver in web scraping or crawling architectures?
**Answer:**
To download a web page, a URL must be translated into an IP address. The HTML downloader calls the DNS resolver to get the corresponding IP address for the given URL (e.g., converting www.wikipedia.org to an IP address).

#### 7. What type of network address does the DNS return to a browser or mobile application?
**Answer:**
IP address.

#### 8. What type of requests are sent directly to a web server after obtaining its IP address?
**Answer:**
HTTP requests.

#### 9. Why does cross-region data transfer inherently introduce latency in distributed systems?
**Answer:**
Data centers are geographically distributed across different regions, and network propagation delays are bounded by the physical speed of light through fiber optics and routing overheads.


### 🟡 Mid Level

#### 1. Explain how WebSocket differs from HTTP
**Answer:**
HTTP is a stateless, unidirectional request-response protocol requiring a new handshake or polling for updates. WebSocket establishes a persistent, full-duplex TCP connection via an HTTP upgrade header, allowing real-time, low-latency, bidirectional data flow between client and server.

#### 2. What is the WebSocket handshake process?
**Answer:**
The WebSocket handshake begins as an HTTP/HTTPS request sent by the client containing specific upgrade headers (`Upgrade: websocket`, `Connection: Upgrade`, `Sec-WebSocket-Key`). If the server supports WebSockets, it responds with an HTTP 101 Switching Protocols status code and a corresponding `Sec-WebSocket-Accept` hash, switching the underlying TCP connection to a full-duplex WebSocket framing protocol.


### 🔴 Senior Level

#### 1. What is TCP congestion control?
**Answer:**
TCP congestion control is a mechanism used by transport layer protocols to prevent network congestion by dynamically throttling the sender's transmission rate using algorithms like slow start, congestion avoidance, fast retransmit, and fast recovery.


## 📂 Category: Networking & API Design (1 cards)

### 🟡 Mid Level

#### 1. What functionalities are typically implemented within an API gateway?
**Answer:**
An API gateway is a fully managed ingress component that commonly supports rate limiting, SSL termination, authentication, IP whitelisting, request routing, and serving static content.


## 📂 Category: Networking & CDN (3 cards)

### 🟢 Junior Level

#### 1. How does a Content Delivery Network (CDN) work at a high level?
**Answer:**
A CDN caches and delivers static content to users via edge servers deployed globally. When a user requests content, the CDN routes them to the geographically closest edge server, minimizing network latency and speeding up page load times.

#### 2. What is a Content Delivery Network (CDN)?
**Answer:**
A CDN is a geographically distributed network of proxy and edge servers designed to cache and deliver static content (like images, videos, CSS, and JavaScript) closer to end users to reduce latency and origin server load. Modern CDNs also support targeted edge caching of dynamic content based on query strings, headers, and cookies.

#### 3. What is a Content Delivery Network (CDN)?
**Answer:**
A CDN is a distributed network of geographically dispersed proxy servers designed to cache and deliver static and dynamic content closer to end-users, reducing latency and origin server load.


## 📂 Category: Networking & DNS (2 cards)

### 🟢 Junior Level

#### 1. Explain the concept of DNS propagation
**Answer:**
DNS propagation is the time it takes for global DNS name servers to update their cached records after a change (such as an A record or CNAME modification) is made at the authoritative DNS provider. It is not an active transmission process; rather, it depends on the Time To Live (TTL) values configured on previous DNS responses, causing different recursive resolvers around the world to fetch the new record at different times.


### 🟡 Mid Level

#### 1. What is GeoDNS routing?
**Answer:**
GeoDNS routing is a DNS service configuration that resolves domain names to IP addresses based on the geographic location of the user, helping direct traffic to the nearest regional data center.


## 📂 Category: Networking & Infrastructure (3 cards)

### 🟢 Junior Level

#### 1. How are public and private IP addresses configured for load balancers and web servers?
**Answer:**
Users connect directly to the public IP address of the load balancer. Web servers sit behind the load balancer and are unreachable directly by external clients, communicating instead via secure private IPs within an isolated internal network.

#### 2. What is the primary function of a load balancer in distributed systems?
**Answer:**
A load balancer distributes incoming network traffic across multiple backend servers to ensure high availability, reliability, and optimal resource utilization.


### 🟡 Mid Level

#### 1. How is multi-data center routing and failover handled using geoDNS?
**Answer:**
GeoDNS resolves domain names to IP addresses based on client geographic location, splitting normal traffic across multiple data centers (e.g., US-East and US-West). In the event of a significant data center outage, traffic is automatically failed over to route 100% of requests to the remaining healthy data center.


## 📂 Category: Networking & Load Balancing (5 cards)

### 🟢 Junior Level

#### 1. How does Round Robin load balancing work?
**Answer:**
Round Robin distributes incoming client requests sequentially across a list of backend servers in a cyclic order. It assumes all backend servers have equal processing capacity and state, though weighted variants can account for hardware capability differences.

#### 2. How does a load balancer improve network and system security?
**Answer:**
A load balancer enhances security by masking the private IP addresses of backend servers from the public internet, routing all incoming traffic through a controlled entry point and preventing direct client-to-server exposure.

#### 3. What are key metrics for load balancer monitoring?
**Answer:**
Key metrics include request rate (QPS/RPS), error rates (HTTP 4xx/5xx status codes), latency (p95, p99 response times), backend server health/availability, active connections, and bandwidth usage/throughput.


### 🟡 Mid Level

#### 1. Explain the advantages of Layer 7 load balancing
**Answer:**
Layer 7 (Application Layer) load balancing operates on the contents of the network packet (e.g., HTTP headers, URLs, cookies, and payload data). Advantages include content-based routing (routing requests to different microservices based on URI paths like /api/v1/users vs /api/v1/orders), SSL/TLS termination, cookie-based session persistence, request transformation, and advanced rate limiting or security filtering.

#### 2. What are load balancer persistence (sticky session) options?
**Answer:**
Load balancer persistence ensures requests from a specific client are routed to the same backend server, often implemented via source IP hashing, cookies, or application session tokens.


## 📂 Category: Networking & Protocols (7 cards)

### 🟢 Junior Level

#### 1. How do Server-Sent Events (SSE) work?
**Answer:**
Server-Sent Events (SSE) is a technology where a browser receives automatic updates from a server via an HTTP connection. Unlike WebSockets, SSE is unidirectional (server-to-client), uses standard HTTP/HTTPS protocols, and has built-in features such as automatic reconnection and event IDs.

#### 2. What is the end-to-end communication flow and protocol usage in a traditional email service?
**Answer:**
1. Client composes an email and sends it to their mail server using SMTP.
2. The sending mail server queries DNS to locate the recipient's SMTP server address.
3. The sending mail server transfers the email to the recipient's mail server using SMTP.
4. The recipient's server stores the email.
5. The recipient's client fetches new messages using IMAP or POP protocols when logging in.

#### 3. Why do new email servers often suffer from poor deliverability?
**Answer:**
New email servers lack sender reputation, causing spam filters to frequently route their outgoing emails directly to the recipient's spam folder rather than the inbox.


### 🟡 Mid Level

#### 1. How do client-server communication patterns differ between the sender and receiver sides in a chat application?
**Answer:**
The sender side typically uses standard HTTP with keep-alive headers to maintain persistent connections and reduce TCP handshakes. The receiver side is more complex because HTTP is client-initiated, requiring server-simulated push techniques like polling, long polling, or WebSockets.

#### 2. What are Apache Thrift and Protocol Buffers?
**Answer:**
Apache Thrift and Protocol Buffers (protobuf) are binary serialization/encoding libraries. Protocol Buffers was originally developed at Google, and Thrift at Facebook; both were open-sourced in 2007-2008 to provide efficient, compact wire-protocol formats.

#### 3. What are WebSocket sub-protocols?
**Answer:**
WebSocket sub-protocols are application-level protocols built on top of the WebSocket transport layer (negotiated via the Sec-WebSocket-Protocol handshake header) that define specific message formats and rules for communication (e.g., STOMP, WAMP).

#### 4. What is the difference between unicast, broadcast, and multicast protocols, and where is multicast used?
**Answer:**
Unicast is from one source to one destination; broadcast is from one source to an entire subnetwork; multicast is from one source to a set of hosts across different subnetworks. Multicast is commonly used in stock exchange design to send data to several receivers in the same multicast group simultaneously, though UDP unreliability requires retransmission mechanisms.


## 📂 Category: Networking & Traffic Management (2 cards)

### 🟢 Junior Level

#### 1. What is the function of a load balancer?
**Answer:**
A load balancer evenly distributes incoming traffic among web servers that are defined in a load-balanced set.


### 🟡 Mid Level

#### 1. What is geographic load balancing?
**Answer:**
Geographic load balancing is a technique used to route user traffic to the geographically closest or most optimal data center or server region. This minimizes network latency, ensures compliance with data residency laws, and improves overall system resilience and fault tolerance.


## 📂 Category: Notification Systems (1 cards)

### 🟢 Junior Level

#### 1. What functional and non-functional requirements are typical when designing a large-scale notification system?
**Answer:**
Functional Requirements: Support multiple notification channels (Push notifications, SMS, Email); support client application triggers and server-side scheduled triggers; allow user opt-out preferences.
Non-Functional Requirements: Soft real-time delivery (low latency under normal loads, acceptable minor delays under peak loads); cross-platform support (iOS, Android, Web/Desktop); high throughput scaling (e.g., millions of daily pushes, SMS, and emails).


## 📂 Category: Observability (12 cards)

### 🟢 Junior Level

#### 1. How is metrics data typically structured and stored?
**Answer:**
Metrics data is usually recorded as a time series containing a set of numerical values coupled with timestamps. Each series is uniquely identified by its metric name and an optional set of key-value labels (tags).

#### 2. Why is centralized error logging important in distributed systems?
**Answer:**
Monitoring error logs helps identify bugs, system failures, and anomalies. While individual server-level logs are useful, aggregating them to a centralized service allows for efficient searching, indexing, and debugging across distributed microservices.

#### 3. Why is comprehensive logging essential in distributed backend systems?
**Answer:**
Logging provides critical observability, enabling engineers to trace distributed request flows, debug intermittent failures, and identify performance bottlenecks.


### 🟡 Mid Level

#### 1. Describe the high-level design and core components of a metrics and alerting system.
**Answer:**
Metrics Source: Application servers, databases, and message queues generating metrics.
Metrics Collector: Gathers raw metrics and writes them to a time-series database.
Time-Series Database (TSDB): Optimized storage with label indexing for fast times-series lookups and analytical rollups.
Query Service: Provides a clean query wrapper over the TSDB.
Alerting System: Evaluates conditions against metrics to dispatch notifications to destinations.
Visualization System: Renders metrics into graphs and charts (e.g., Grafana).

#### 2. What are real-world examples of push vs. pull architectures in metrics monitoring services?
**Answer:**
Pull architectures: Prometheus (where the monitoring server actively scrapes targets). Push architectures: Amazon CloudWatch and Graphite (where target instances proactively transmit metrics to the monitoring backend).

#### 3. What are the core components of a monitoring and alerting system?
**Answer:**
Data collection (gathering metrics from sources), Data transmission (transferring metrics), Data storage (organizing and storing timeseries/metric data), Alerting (analyzing data for anomalies and dispatching alerts to communication channels), and Visualization (presenting metrics in graphs/charts for pattern identification).

#### 4. What are the core components of a monitoring and tracing system?
**Answer:**
Core components include log monitoring (commonly using the Elasticsearch, Logstash, Kibana (ELK) stack) and distributed system tracing, which tracks service requests as they flow and propagate across multiple distributed services.

#### 5. What is a visualization system in observability, and why use off-the-shelf tools?
**Answer:**
A visualization system sits on top of the data layer to display metrics (server requests, memory/CPU utilization, page load time, traffic, login info) and alerts on a dashboard over various time scales. Building a high-quality visualization system is difficult, so using off-the-shelf tools like Grafana, which integrates well with popular time-series databases, is strongly recommended.

#### 6. What is the difference between push and pull models in metrics collection?
**Answer:**
In a push model, metrics sources (e.g., web/database servers via collection agents) directly send metrics to a centralized metrics collector periodically. In a pull model, the collector actively scrapes metrics endpoints from the targets.

#### 7. What is the structure of time-series metric data and how is it formatted?
**Answer:**
Time-series metric data consists of a metric name, a set of key-value labels/tags, timestamps, and numeric values. Line protocol is a common input format used by monitoring systems (e.g., Prometheus, OpenTSDB), structured as: `metric_name label1=value1,label2=value2 timestamp value`.

#### 8. Where can metrics aggregation occur in a monitoring and observability pipeline?
**Answer:**
Metrics aggregation can happen at three distinct points: 1. In the collection agent on the client-side, 2. In the ingestion pipeline before writing to storage, and 3. On the query side after writing to storage.


### 🔴 Senior Level

#### 1. How does the alert flow work in a large-scale monitoring and alerting system?
**Answer:**
1. **Config Loading**: Rules (defined as YAML) are loaded into cache servers.
2. **Fetch Configs**: The alert manager fetches alert configurations from the cache.
3. **Evaluation**: The alert manager calls the query service at regular intervals. If a threshold is violated, an alert event is created. The alert manager filters, merges, deduplicates alerts, enforces access control, and ensures retries.
4. **Alert State Store**: A key-value database (e.g., Cassandra) tracks the state of all alerts (inactive, pending, firing, resolved).
5. **Event Streaming**: Eligible alerts are pushed into Kafka.
6. **Consumption**: Alert consumers pull events from Kafka.
7. **Notification**: Consumers send alerts across channels like email, SMS, PagerDuty, or HTTP webhooks.


## 📂 Category: Observability & Infrastructure (1 cards)

### 🔴 Senior Level

#### 1. What are the scale and retention requirements for a large-scale monitoring and alerting infrastructure?
**Answer:**
Scale: Supporting ~100M daily active users across 1,000 server pools (100 machines per pool, 100 metrics per machine), resulting in ~10 million active metrics.
Data Retention: 1-year total data retention policy structured as raw form for 7 days, 1-minute resolution aggregated for 30 days, and 1-hour resolution aggregated for 1 year.


## 📂 Category: Observability & Metrics (1 cards)

### 🔴 Senior Level

#### 1. How can we optimize or replace a separate query service for metrics?
**Answer:**
Most industrial-scale visualization and alerting systems have powerful plugins to interface directly with well-known time-series databases. Using a well-chosen time-series database often eliminates the need for a custom query service or additional caching layers.


## 📂 Category: Observability & Monitoring (14 cards)

### 🟢 Junior Level

#### 1. How do we prevent metrics collectors from falling behind in a push-based monitoring model?
**Answer:**
Deploy the metrics collectors in an auto-scaling cluster fronted by a load balancer, ensuring the cluster dynamically scales up and down based on the CPU utilization of the collector instances.

#### 2. What categories of metrics should be collected to monitor system health and business insights?
**Answer:**
- Host-level metrics: CPU, memory, disk I/O, etc.
- Aggregated-level metrics: Performance of the database tier, cache tier, etc.
- Key business metrics: Daily active users (DAU), user retention, revenue, etc.

#### 3. What is the purpose of system metrics tracking?
**Answer:**
System metrics are quantitative measurements used to monitor infrastructure and application performance, detect anomalies or bottlenecks, and drive data-backed capacity planning and operational decisions.


### 🟡 Mid Level

#### 1. Describe the pull metric collection model in distributed monitoring systems.
**Answer:**
The metrics collector fetches configuration metadata of service endpoints from Service Discovery, including pulling intervals, IP addresses, timeouts, and retry parameters. The metrics collector pulls metrics data via a pre-defined HTTP endpoint (e.g., /metrics) exposed by client libraries embedded in the target services. Optionally, the metrics collector registers change event notifications or periodically polls Service Discovery to receive updates whenever service endpoints change.

#### 2. Describe the pull model for metrics data collection and how it handles service discovery.
**Answer:**
In the pull model, dedicated metric collectors periodically pull metric values from running applications. To maintain a scalable list of service endpoints without manual configuration files, the setup integrates with a Service Discovery component (e.g., etcd, ZooKeeper). Services register their availability upon startup, and the metrics collector is dynamically notified of endpoint additions, removals, or updates, using these configuration rules to dictate when and where to scrape metrics.

#### 3. How can systems reduce the volume of data sent to a metrics collector, and what are the trade-offs of local buffering?
**Answer:**
Aggregation at the edge/agent is an effective way to reduce metrics volume. If push traffic fails, agents can buffer data locally on disk to resend later. However, in auto-scaling environments where servers frequently terminate, local buffering can lead to permanent data loss if the metrics collector falls behind.

#### 4. How can we guarantee that a metrics collector can handle large volumes of ingestion data?
**Answer:**
Regardless of whether a push or pull model is used, the metrics collector tier should be architected as a cluster of servers configured with automatic scaling (auto-scaling) to dynamically provision adequate collector instances based on load.

#### 5. How do pull and push architectures compare for metrics collection?
**Answer:**
Pull architecture uses TCP, provides easier debugging (e.g., querying /metrics endpoints directly), enables straightforward health checks for down servers, and guarantees data authenticity via pre-configured target files. However, it can face firewall/network complexity in multi-datacenter setups. Push architecture typically uses UDP for lower-latency transport, naturally handles short-lived batch jobs (often via push gateways), and works seamlessly behind load balancers and auto-scaling groups, but requires client whitelisting or authentication to ensure data authenticity.

#### 6. What is the role of a collection agent in metrics and monitoring systems?
**Answer:**
The collection agent installed on the client-side supports simple aggregation logic, such as aggregating a counter every minute before sending it to the metrics collector to reduce network overhead.

#### 7. What is the role of a query service in a metrics collection system?
**Answer:**
The query service comprises a cluster of query servers that access time-series databases and handle requests from visualization or alerting systems. This dedicated layer decouples time-series storage from clients, providing flexibility to swap out storage or visualization layers independently.

#### 8. Why do metrics monitoring systems like Prometheus and InfluxDB use custom query languages instead of SQL?
**Answer:**
Metrics monitoring systems use dedicated query languages (like Flux or PromQL) because relational SQL is difficult and verbose to construct for time-series data analysis. For example, operations like computing an exponential moving average require complex nested windows, subqueries, and partitioning in SQL, whereas time-series languages provide native, concise functions for time ranges and sliding averages.


### 🔴 Senior Level

#### 1. What core categories of metrics are crucial for monitoring an event aggregation service?
**Answer:**
1. Latency: Track timestamps as events flow through different pipeline stages. The differences expose stage-specific latency metrics.
2. Message queue size / consumer lag: Sudden spikes indicate backpressure or slow processing. For Kafka, monitor records-lag metrics instead of just queue length.
3. System resource utilization: CPU, disk IO, and JVM metrics on aggregation nodes.

#### 2. What requirements gathering questions should be asked when designing a metrics and monitoring system?
**Answer:**
Candidate should clarify: 1) Target audience/use case (internal infra vs SaaS like Datadog); 2) Metrics scope (operational system metrics like CPU/memory/disk, high-level RPS/server counts, excluding business metrics); 3) Scale (100M DAU, 1,000 server pools, 100 machines/pool); 4) Retention period (e.g., 1 year); 5) Downsampling/roll-up policies (raw for 7 days, 1-min resolution for 30 days, 1-hour resolution thereafter); 6) Alert channels (email, phone, PagerDuty, webhooks); 7) Exclusion of logs and distributed tracing.

#### 3. What scaling problem occurs with a single metrics collector, and how is it solved?
**Answer:**
A single collector cannot handle thousands of servers. Using a pool of collectors introduces potential duplicate data collection. This is resolved using a coordination scheme like a consistent hash ring, mapping source servers to distinct collector ranges.


## 📂 Category: Observability & Operations (2 cards)

### 🟢 Junior Level

#### 1. What are the three key areas to invest in when a website grows?
**Answer:**
The three key areas are logging, metrics, and automation.

#### 2. Which operational tools are generally not considered a strict necessity for small projects, but become essential at scale?
**Answer:**
Comprehensive logging, advanced metrics, and full automation support. While good practices, they are not mandatory for small websites running on a few servers.


## 📂 Category: Payment Systems (2 cards)

### 🟢 Junior Level

#### 1. What is the function of a wallet in transactional systems?
**Answer:**
The wallet keeps the account balance of the merchant and may also record the total amount a given user has paid in aggregate.


### 🔴 Senior Level

#### 1. What is the difference between pay-in and pay-out flows when integrating with a third-party Payment Service Provider (PSP)?
**Answer:**
In the pay-in flow, money from the buyer's credit card is transferred directly to the e-commerce platform's bank account (requiring buyer card details, not seller bank details). In the pay-out flow, once fulfillment conditions (like product delivery) are satisfied, funds are transferred from the e-commerce platform's bank account to the seller's bank account.


## 📂 Category: Performance & Concurrency (1 cards)

### 🔴 Senior Level

#### 1. What are the pros and cons of CPU pinning in backend systems?
**Answer:**
Pros:
- No context switching (CPU fully allocated to the application loop).
- No locks and zero lock contention since a single thread updates states.
- Contributes to ultra-low 99th percentile latency.
Cons:
- Makes coding significantly more complex. Engineers must carefully profile task execution times to prevent long-running tasks from blocking the application loop thread.


## 📂 Category: Performance & Observability (1 cards)

### 🔴 Senior Level

#### 1. What is latency determinism and how is it measured?
**Answer:**
Latency determinism refers to maintaining highly consistent latency across requests. It is critical for high-throughput, low-latency systems (e.g., financial exchanges). It is measured using high-percentile metrics like the 99th or 99.99th percentile (p99/p9999) using tools like HdrHistogram. Latency fluctuations can be caused by runtime events such as Java HotSpot JVM Stop-the-World garbage collection safepoints.


## 📂 Category: Performance Optimization (3 cards)

### 🟡 Mid Level

#### 1. What are the general backend recommendations regarding data compression and disk I/O?
**Answer:**
1. Compress data before sending it over the internet to reduce network bandwidth usage.
2. Avoid random disk seeks where possible to optimize I/O performance (favoring sequential reads/writes or memory-mapped structures).


### 🔴 Senior Level

#### 1. How do we optimize map rendering using vector tiles instead of raster images?
**Answer:**
Shift from sending pre-rendered images over the network to sending vector information (paths and polygons), allowing the client to render the graphics via WebGL. Advantages include: 1) Substantial bandwidth savings due to superior vector data compression. 2) A smoother zooming experience since vector elements scale dynamically without pixelation.

#### 2. How do we systematically reduce latency in high-frequency trading or stock exchange systems?
**Answer:**
Break down latency along the critical path (Latency = Σ executionTimeAlongCriticalPath). Reduce it by: 1) Decreasing the number of tasks on the critical path. 2) Shortening the execution time of each task by eliminating unnecessary network I/O and disk access.


## 📂 Category: Performance Optimization & Memory Management (1 cards)

### 🔴 Senior Level

#### 1. How can memory consumption be optimized when tracking high-frequency price history in candlestick charts across multiple symbols and time intervals?
**Answer:**
1) Use pre-allocated ring buffers to hold candlestick data structures, reducing garbage collection overhead and object allocations. 2) Impose a strict memory cap on the number of active candlesticks held in-memory, flushing older or historical data segments to disk or persistent time-series storage.


## 📂 Category: Rate Limiting (2 cards)

### 🟢 Junior Level

#### 1. What is the token bucket algorithm used in rate limiting?
**Answer:**
The token bucket algorithm is a rate-limiting algorithm where a bucket has a fixed capacity and is refilled with tokens at a constant rate. Each incoming request consumes one token. If the bucket contains enough tokens, the request is allowed; if the bucket is empty, the request is throttled or dropped.


### 🔴 Senior Level

#### 1. How does the sliding window counter rate limiting algorithm work?
**Answer:**
It combines the fixed window counter and sliding window log. It calculates requests in a rolling window using the formula: Requests in current window + (Requests in previous window * overlap percentage of the rolling window). The resulting count is then rounded and checked against the rate limit threshold.


## 📂 Category: Rate Limiting & Traffic Management (1 cards)

### 🟡 Mid Level

#### 1. How does the leaking bucket rate limiting algorithm work?
**Answer:**
The leaking bucket algorithm processes requests at a fixed, regulated rate using a first-in-first-out (FIFO) queue. When a request arrives, the system checks if the queue is full; if not, the request is added, otherwise it is dropped. Requests are pulled from the queue and processed at regular, uniform intervals.


## 📂 Category: Real-Time Systems (5 cards)

### 🟢 Junior Level

#### 1. How is the user login flow tied to online presence systems?
**Answer:**
Once a persistent WebSocket connection is established between the client and the real-time service during login, the user's online status and `last_active_at` timestamp are immediately updated and persisted in a low-latency Key-Value (KV) store to drive presence indicators.


### 🟡 Mid Level

#### 1. How do we handle user disconnections and presence status in a chat service without excessive state flapping?
**Answer:**
Avoid updating online status on every brief disconnect/reconnect (e.g., passing through a tunnel). Instead, implement a heartbeat mechanism where online clients periodically send a heartbeat event (e.g., every 5 seconds) to presence servers. If no heartbeat is received within a threshold window (e.g., x = 30 seconds), the user is marked offline.

#### 2. What algorithmic score mechanics, time boundaries, and pagination requirements must be implemented for a competitive gaming leaderboard?
**Answer:**
1. Scoring Logic: Point-based increments awarded per match win.
2. Temporal Scope: Monthly tournament intervals that reset leaderboards periodically.
3. Query Requirements: Return the top 10 users globally, query the absolute rank of a specific user, and fetch adjacent users (four positions above and below).
4. Scale & Latency: 5 million DAU, 25 million MAU, averaging 10 matches per player daily; results must update in real-time.
5. Tie-Breaking: Deterministic ranking rules when multiple players hold identical scores.


### 🔴 Senior Level

#### 1. Explain the periodic location update flow in a real-time tracking or nearby friends architecture.
**Answer:**
1. The mobile client sends a location update over a persistent WebSocket connection to the load balancer.
2. The load balancer forwards the update to the specific WebSocket server handling that client connection.
3. The WebSocket server persists the location data to a history database and updates the location cache, refreshing its TTL.
4. The WebSocket server updates a local variable in the user's connection handler for in-memory distance calculations and publishes the new location to the user's Redis Pub/Sub channel (steps 3-5 can be parallelized).
5. Redis Pub/Sub broadcasts the location update to all subscribed WebSocket connection handlers of the user's online friends.
6. For each friend, their WebSocket server computes the distance between the sender and the subscriber (whose location is held in memory). If the distance is within the search radius, the new location and timestamp are pushed down the WebSocket to the subscriber's client; otherwise, it is dropped.

#### 2. How does a periodical location update work using WebSocket and Redis pub/sub?
**Answer:**
When a user's location changes, it's sent to the WebSocket server holding their connection. The location is published to the user's channel in a Redis pub/sub server, which broadcasts it to all subscriber handlers (friends' connection handlers). If the distance between the sender and subscriber doesn't exceed the search radius, the update is sent to the client. For 400 friends on average with 10% online/nearby, about 40 location updates are forwarded per user update.


## 📂 Category: Real-Time Systems & Caching (1 cards)

### 🔴 Senior Level

#### 1. How is the Redis pub/sub server used in a nearby friends application, and what are the architectural trade-offs?
**Answer:**
Redis pub/sub is used as a lightweight routing layer to direct location updates to online friends. A unique channel is assigned to every user upon app initialization, and users subscribe to each friend's channel regardless of online status. This simplifies the backend by eliminating dynamic sub/unsub logic. 

Trade-offs:
- Memory vs. Simplicity: Higher memory usage (e.g., ~200 GB for 100M channels with 100 friends each), but memory is rarely the bottleneck.
- CPU vs. Memory: The primary bottleneck is CPU throughput (handling subscriber pushes). At scale (e.g., 14M updates/sec), a distributed Redis pub/sub cluster is required since a single instance cannot handle the message push load.


## 📂 Category: Real-Time Systems & WebSockets (1 cards)

### 🟡 Mid Level

#### 1. How do you manage potential performance hotspots caused by users with thousands of friends in a nearby friends application?
**Answer:**
Assuming a hard cap on bidirectional friendships (e.g., Facebook's 5,000 friend limit) rather than a celebrity follower model: 1) Subscribers (friends) are scattered across multiple WebSocket servers in the cluster, distributing the update load. 2) 'Whale' users place slightly higher load on their specific pub/sub channel server, but with a large pool of pub/sub servers (e.g., >100), these users are distributed, preventing any single server from being overwhelmed.


## 📂 Category: Real-time Architecture (3 cards)

### 🟡 Mid Level

#### 1. How is long polling utilized in storage service notifications?
**Answer:**
Clients maintain a long-poll connection to a notification service. When a file change is detected, the server closes the connection, prompting the client to fetch updates from a metadata server. Once received or timed out, the client immediately establishes a new long-poll connection.

#### 2. How is message synchronization across multiple devices implemented in chat applications?
**Answer:**
Each connected device maintains a local 'cur_max_message_id' variable tracking the latest received message. Devices query the key-value store for new messages where the recipient ID matches the user and the message ID exceeds the local 'cur_max_message_id'.

#### 3. What is the role of WebSocket servers in a nearby friends feature?
**Answer:**
A cluster of stateful servers that handles near real-time updates of friends' locations. Each client maintains one persistent WebSocket connection to one of these servers. Responsibilities include routing location updates from friends within the search radius and handling client initialization by seeding the mobile client with the locations of all nearby online friends.


## 📂 Category: Real-time Communication (1 cards)

### 🔴 Senior Level

#### 1. What is the role of real-time servers in an email system?
**Answer:**
Real-time servers are stateful servers responsible for maintaining persistent connections (such as WebSockets with long-polling fallback, or protocols like JMAP over WebSocket) to push new email updates to clients instantly.


## 📂 Category: Real-time Systems (4 cards)

### 🟡 Mid Level

#### 1. How do clients manage friend addition, removal, and location status updates in a nearby friends application via WebSockets?
**Answer:**
When a new friend is added, the mobile client triggers a callback that sends a message to the WebSocket server to subscribe to the new friend's pub/sub channel. The WebSocket server replies with the new friend's latest location and timestamp if active. Conversely, removing a friend triggers a callback to unsubscribe from their pub/sub channel. This mechanism also handles user opt-in/opt-out status for location updates.

#### 2. What are the non-functional requirements of a scalable leaderboard system?
**Answer:**
1. Real-time updates where score changes reflect immediately on the leaderboard.
2. General distributed system requirements including high scalability, low latency, high availability, and fault tolerance.


### 🔴 Senior Level

#### 1. How do we implement lightweight messaging for a real-time feature like nearby friends?
**Answer:**
Use Redis Pub/Sub as a lightweight message bus. Channels are cheap to create, allowing millions of topics. WebSocket servers publish location updates to a user's specific channel, and active friends' connection handlers subscribe to compute distances in memory, pushing updates to clients if within the search radius.

#### 2. What are the exact initialization steps executed by a server upon establishing a client WebSocket connection in a nearby friends application?
**Answer:**
1. Update the user's location in the location cache and in connection handler memory. 2. Load all friends from the user database. 3. Make a batched request to the location cache to fetch friends' locations (inactive friends are omitted due to TTL expiration). 4. Compute distances to active friends; return profiles, locations, and timestamps for those within the search radius. 5. Subscribe to all friends' channels in Redis Pub/Sub (inactive friends consume minimal memory without CPU/IO overhead). 6. Publish the user's current location to their own Redis Pub/Sub channel.


## 📂 Category: Reliability & Availability (2 cards)

### 🟢 Junior Level

#### 1. How is high availability uptime traditionally measured?
**Answer:**
Uptime is traditionally measured in 'nines' (e.g., 99.9% or 'three nines', 99.999% or 'five nines').

#### 2. What does high availability mean for a system?
**Answer:**
It means the system is able to remain continuously operational for a long period of time without significant downtime.


## 📂 Category: Reliability & Fault Tolerance (3 cards)

### 🟡 Mid Level

#### 1. How are resiliency, retries, and failures handled in a payment system?
**Answer:**
Transient or retryable errors are routed to a retry queue. Non-retryable errors (like invalid input) are stored directly in a database. If a message fails repeatedly in the retry queue and exceeds the threshold, it moves to a dead letter queue (DLQ) for debugging and isolation.


### 🔴 Senior Level

#### 1. How do you detect and handle in-memory data corruption in large-scale systems?
**Answer:**
While complete disk failures can be mitigated via erasure coding, in-memory data corruption is handled by verifying checksums across process boundaries. Checksums are compact data blocks used to detect transmission or memory errors. By comparing the original data checksum with the checksum computed after transmission, a mismatch indicates corruption. While not 100% theoretically, matching checksums provide extremely high practical confidence.

#### 2. What is the solution for mitigating systematic faults in software systems?
**Answer:**
There is no silver bullet. Mitigations include carefully analyzing assumptions and interactions, thorough testing, process isolation, implementing crash-and-restart paradigms, and continuous monitoring/alerting. Systems should implement internal invariants checks (e.g., verifying incoming versus outgoing message counts) to raise alerts upon discrepancies.


## 📂 Category: Reliability & Messaging (1 cards)

### 🟡 Mid Level

#### 1. How do you guarantee zero data loss in a distributed notification system?
**Answer:**
Because notifications can tolerate latency or re-ordering but never loss, the system must durably persist all notification payloads to a persistent database before dispatching them, combined with an asynchronous retry mechanism (such as dead-letter queues and backoff policies) to handle transient downstream failures.


## 📂 Category: Reliability & Metrics (1 cards)

### 🟢 Junior Level

#### 1. What is an SLA (Service Level Agreement)?
**Answer:**
An SLA is a formal contract between a service provider and a customer that defines the expected level of uptime and reliability. It is traditionally measured in 'nines' of availability (e.g., 99.9% uptime or 'three nines').


## 📂 Category: Reliability & Operations (3 cards)

### 🟡 Mid Level

#### 1. What is the leading cause of outages in large internet services?
**Answer:**
Configuration errors made by human operators are the leading cause of outages in large internet services, whereas hardware faults (servers or network issues) typically account for only 10–25% of outages.


### 🔴 Senior Level

#### 1. How do we monitor hot-warm matching engines to guarantee high availability?
**Answer:**
Combine standard infrastructure and process monitoring with active heartbeats sent directly from the matching engine. If a heartbeat fails to arrive within the defined SLA window, initiate automated failover protocols assuming the primary engine is degraded or unresponsive.

#### 2. What design principles ensure system reliability despite human error?
**Answer:**
Design constrained abstractions and APIs that make 'the right thing' easy. Provide fully functional non-production sandboxes using real data. Test thoroughly at all levels (unit, integration, chaos). Enable quick recovery via gradual rollouts and fast rollbacks, and implement extensive monitoring/telemetry for early anomaly detection.


## 📂 Category: Reliability & Resiliency (2 cards)

### 🟡 Mid Level

#### 1. What is fault tolerance in distributed systems?
**Answer:**
Fault tolerance refers to a system's ability to anticipate and cope with faults. Because making a system tolerant of every possible kind of fault is not feasible in reality, fault tolerance specifically targets tolerating certain predefined types of faults.


### 🔴 Senior Level

#### 1. What challenges arise when detecting node failure for automated failovers in distributed systems?
**Answer:**
False alarms can cause unnecessary failovers, and bugs that crashed the primary instance can also crash backup instances during failover. Mitigation strategies include manual failovers on new releases, gathering operational metrics, and utilizing chaos engineering.


## 📂 Category: Reliability & SRE (1 cards)

### 🟢 Junior Level

#### 1. How is high availability typically measured?
**Answer:**
High availability is measured as an uptime percentage (e.g., 'four nines' or 99.99%), representing the proportion of time a system is operational and accessible over a given period.


## 📂 Category: Replication & Consensus (1 cards)

### 🟡 Mid Level

#### 1. What is the primary purpose of single-leader replication?
**Answer:**
To ensure all writes go through a single designated leader node to prevent write conflicts, while followers pull or receive updates asynchronously or synchronously for read scalability and high availability.


## 📂 Category: Resilience (1 cards)

### 🟡 Mid Level

#### 1. What is a recommended retry strategy for payment processing?
**Answer:**
Use exponential backoff if network issues are persistent, avoiding overly aggressive retries that waste resources or cause service overload. A best practice is for downstream services to provide an error code accompanied by a Retry-After header.


## 📂 Category: Scalability (2 cards)

### 🟢 Junior Level

#### 1. How do we handle the scalability of business services and Location-Based Services (LBS)?
**Answer:**
Business services and LBS are typically stateless, enabling auto-scaling (adding servers during peak traffic like meal times, removing them during off-peak hours). In cloud deployments, multi-region and multi-availability zone setups further maximize availability.

#### 2. What are the pros and cons of vertical scaling?
**Answer:**
Vertical scaling offers simplicity and works well when traffic is low. However, it has serious limitations: it has a hard limit where it is impossible to add unlimited CPU and memory to a single server, and it lacks built-in failover and redundancy, meaning if the server goes down, the entire application goes down.


## 📂 Category: Scalability & Architecture (3 cards)

### 🟡 Mid Level

#### 1. How is a system architecture redesigned after making the web tier stateless?
**Answer:**
Session data is decoupled from the web servers and stored in a shared, external data store (e.g., Redis, Memcached, or a NoSQL database). This enables seamless horizontal auto-scaling of the web tier by dynamically adding or removing web server instances based on traffic load.

#### 2. What are the core issues and architectural drawbacks of a stateful application architecture?
**Answer:**
In a stateful architecture, every request from a specific client must be routed to the exact same server holding their session data (e.g., Server 1 holding User A's session). While sticky sessions in load balancers can achieve this, it introduces operational overhead, complicates horizontal scaling (adding/removing servers), and makes handling server failures challenging.

#### 3. What improvements can be applied to online storage to move away from a single-server design?
**Answer:**
Load balancer: Add a load balancer to distribute network traffic evenly and handle server failovers. Web servers: Easily scale web servers up or down based on traffic load. Metadata database: Move the database out of the application server to avoid a single point of failure, utilizing data replication and sharding to meet availability and scalability requirements. File storage: Utilize distributed object storage (e.g., Amazon S3) where files are replicated across separate geographical regions to ensure high availability and durability.


## 📂 Category: Scalability & Caching (1 cards)

### 🟡 Mid Level

#### 1. What is the impact of scaling from 5 million DAU to 500 million DAU for a leaderboard?
**Answer:**
Scaling up by 100x increases the worst-case leaderboard size to ~65 GB and QPS to 250,000 queries per second, exceeding the capacity of a single Redis cache and necessitating a horizontal sharding solution.


## 📂 Category: Scaling & Architecture (1 cards)

### 🟢 Junior Level

#### 1. What is the primary advantage of vertical scaling?
**Answer:**
The primary advantage of vertical scaling is its simplicity.


## 📂 Category: Search & Caching (1 cards)

### 🔴 Senior Level

#### 1. How do we optimize a Trie to retrieve frequency-sorted words in an autocomplete system?
**Answer:**
A standard Trie with full traversal and sorting is too slow for top-K queries. Optimizations include: 1) Limiting the maximum length of prefixes. 2) Caching top search queries directly at each Trie node.


## 📂 Category: Search & Data Processing (1 cards)

### 🟡 Mid Level

#### 1. What is the role of aggregators in an autocomplete search service?
**Answer:**
Aggregators process and structure massive, raw analytics search logs into formats consumable by the system. Depending on requirements (e.g., real-time results for Twitter vs. weekly batch updates for a trie rebuild), they aggregate data at varying time intervals.


## 📂 Category: Search & Indexing (2 cards)

### 🟡 Mid Level

#### 1. What is sharding in Elasticsearch?
**Answer:**
In Elasticsearch, sharding involves dividing an index into smaller pieces called shards, allowing the cluster to distribute document storage and query processing workloads across multiple nodes for horizontal scalability.

#### 2. What is the high-level architecture of a real-time autocomplete system?
**Answer:**
The system is divided into two primary parts: (1) Data gathering service, which aggregates user input queries in real-time (or via batch processing for large datasets), and (2) Query service, which takes a search query or prefix and returns the top 5 most frequently searched terms.


## 📂 Category: Search & Information Retrieval (1 cards)

### 🔴 Senior Level

#### 1. Explain the concept of document scoring in search engines
**Answer:**
Document scoring is the process used by search engines (like Elasticsearch or Apache Solr) to calculate how relevant a retrieved document is to a user's search query. Algorithms like BM25 or TF-IDF evaluate term frequency (how often terms appear in a document), inverse document frequency (how rare the term is across the entire corpus), and field-length normalization to rank documents in order of relevance.


## 📂 Category: Search & Recommendation (1 cards)

### 🟡 Mid Level

#### 1. Why is updating a trie in real-time on every keystroke inefficient for a search autocomplete service?
**Answer:**
Billions of user queries per day would require constant trie updates, significantly slowing down the query service. Furthermore, top suggestions do not change rapidly enough to justify the overhead of real-time write updates.


## 📂 Category: Search & Storage (1 cards)

### 🔴 Senior Level

#### 1. What are the primary storage and disk I/O challenges when designing a custom large-scale email search engine?
**Answer:**
Daily metadata and attachment sizes reach the petabyte scale, with individual accounts holding over 500,000 emails, making disk I/O the primary performance bottleneck for index servers. Because indexing is write-heavy, Log-Structured Merge-Trees (LSM) (used in Cassandra, RocksDB, BigTable) are ideal to optimize for sequential write paths and leverage in-memory L0 caches. LSMs also help separate frequently changing data (e.g., folder metadata and filter rules) from immutable email content.


## 📂 Category: Search Engines & Indexing (2 cards)

### 🟡 Mid Level

#### 1. What search and indexing capabilities do full-text search engines like Lucene provide?
**Answer:**
Synonym expansion, ignoring grammatical variations, proximity searches, linguistic text analysis, and fuzzy matching via edit distance (e.g., detecting insertions, deletions, or substitutions within a specific threshold).


### 🔴 Senior Level

#### 1. How does Apache Lucene utilize log-structured merge-tree (LSM) concepts?
**Answer:**
Lucene maps terms (words) to postings lists (document IDs containing the term) inside SSTable-like sorted files. These files are immutable and merged in the background as needed, mirroring the write and compaction pattern of LSM-trees.


## 📂 Category: Search Systems (2 cards)

### 🟡 Mid Level

#### 1. What are the core functional requirements and constraints of a search autocomplete system?
**Answer:**
Key requirements include: 1) Fast response time (must return results within 100 milliseconds to avoid UI stuttering), 2) Relevance to the search term, 3) Sorted output (by popularity or ranking models), 4) High scalability to handle massive traffic volume, and 5) High availability during network partitions or node failures.


### 🔴 Senior Level

#### 1. How can we support real-time trending search queries in an autocomplete system?
**Answer:**
Basic offline weekly trie builders are too slow for trending topics. Real-time autocomplete requires: 1. Reducing the working dataset via sharding. 2. Adjusting ranking models to weight recent queries higher. 3. Employing stream processing frameworks (e.g., Apache Kafka, Spark Streaming, Flink) to process data continuously as streams.


## 📂 Category: Security (2 cards)

### 🟢 Junior Level

#### 1. Explain HTTPS and its benefits
**Answer:**
HTTPS uses TLS (Transport Layer Security) over HTTP to encrypt communication between client and server. Benefits include data confidentiality (preventing eavesdropping), data integrity (preventing tampering), and authentication (preventing man-in-the-middle attacks via certificates).

#### 2. What is a Denial of Service (DoS) attack?
**Answer:**
A malicious attempt to disrupt normal services of a host or network resource, making it unavailable to intended users typically by flooding it with superfluous traffic or requests.


## 📂 Category: Security & Compliance (1 cards)

### 🔴 Senior Level

#### 1. What critical security threats must be mitigated when designing a payment processing system, and what solutions address them?
**Answer:**
1. Request/response eavesdropping -> Enforce HTTPS.
2. Data tampering -> Enforce encryption and integrity monitoring.
3. Man-in-the-middle attacks -> Use SSL with certificate pinning.
4. Data loss -> Database replication across multiple regions and periodic point-in-time snapshots.
5. Distributed denial-of-service (DDoS) -> Implement rate limiting and firewalls.
6. Card theft -> Tokenization (storing arbitrary tokens instead of raw card numbers).
7. Compliance -> Meet PCI DSS standards.
8. Fraud -> Address Verification System (AVS), Card Verification Value (CVV), and user behavior analysis.


## 📂 Category: Security & Networking (3 cards)

### 🟡 Mid Level

#### 1. How does TLS certificate verification work?
**Answer:**
TLS certificate verification involves the client validating the server's SSL/TLS certificate against a trusted root Certificate Authority (CA) store. The client checks the certificate chain of trust, expiration dates, domain name matching (SAN/CN), and verifies the cryptographic signature using the CA's public key, alongside checking Certificate Revocation Lists (CRL) or Online Certificate Status Protocol (OCSP).

#### 2. How does UDP multicast work?
**Answer:**
UDP multicast enables a single sender to transmit a single data packet to multiple receivers simultaneously across a network using specially designated Class D IP multicast addresses (224.0.0.0 to 239.255.255.255). Routers use IGMP (Internet Group Management Protocol) to forward packets only to network segments with active listeners.

#### 3. How is a DNS service related to email routing?
**Answer:**
DNS uses Mail Exchanger (MX) records to route emails to the correct recipient mail servers. Sending mail servers query the recipient domain's DNS for MX records, which contain priority numbers (lower numbers indicate higher preference). The sender attempts delivery to the highest-priority server first and falls back to lower-priority servers upon failure.


## 📂 Category: Security & Reliability (1 cards)

### 🔴 Senior Level

#### 1. Why is fault prevention preferred over fault tolerance in security contexts?
**Answer:**
While fault tolerance is generally preferred for availability, certain scenarios like security cannot tolerate the initial failure. If an attacker compromises a system and accesses sensitive data, that security breach is irreversible, making prevention mandatory over mere tolerance.


## 📂 Category: Security & Resilience (1 cards)

### 🔴 Senior Level

#### 1. How do we combat DDoS attacks in a stock exchange system?
**Answer:**
Isolate public services from private ones, utilize read-only data copies, implement a caching layer for static/infrequent data, harden URLs to prevent query-string-based cache busting (e.g., /data/recent vs /data?from=... and cache at CDN), apply robust safelist/blocklists at API gateways, and enforce strict rate limiting.


## 📂 Category: Security & Storage Systems (1 cards)

### 🟡 Mid Level

#### 1. How do you optimize upload security and architecture using pre-signed URLs?
**Answer:**
To ensure unauthorized users cannot write data directly to internal storage: 1) The client makes an HTTP request to API servers requesting a pre-signed URL (known as a Shared Access Signature in Azure Blob Storage, or pre-signed URLs in Amazon S3). 2) The API server validates permissions and responds with the restricted pre-signed URL. 3) The client uses this token-secured URL to upload the file directly to object storage.


## 📂 Category: Serialization (2 cards)

### 🟡 Mid Level

#### 1. What are the requirements for data encoding in Apache Thrift and Protocol Buffers?
**Answer:**
Both Thrift and Protocol Buffers require a predefined schema (using an Interface Definition Language, or IDL) for any data that is encoded, allowing efficient binary serialization and forward/backward compatibility.


### 🔴 Senior Level

#### 1. How does the Apache Thrift CompactProtocol optimization work?
**Answer:**
Thrift CompactProtocol is semantically equivalent to BinaryProtocol but encodes the same payload into fewer bytes by: 1) Packing field types and tag numbers into a single byte, and 2) Using variable-length integers (varints) where the top bit of each byte indicates if more bytes follow. Small numbers (-64 to 63) take 1 byte, medium numbers take 2 bytes, reducing overall network payload size.


## 📂 Category: Serialization & Encoding (1 cards)

### 🟡 Mid Level

#### 1. What are field tags in binary serialization formats like Thrift?
**Answer:**
Field tags are numerical identifiers (e.g., 1, 2, 3) defined in a schema that act as compact aliases for field names, replacing verbose string keys (like 'userName') to optimize encoded data size.


## 📂 Category: Serialization & Protocols (1 cards)

### 🟡 Mid Level

#### 1. What are the binary serialization formats used by Apache Thrift?
**Answer:**
Apache Thrift utilizes two primary binary encoding formats: BinaryProtocol and CompactProtocol.


## 📂 Category: Service Discovery (1 cards)

### 🟡 Mid Level

#### 1. What is service discovery and how does it work in distributed systems?
**Answer:**
Service discovery is the process of automatically detecting the location and availability of network services. In architectures like chat servers, it recommends the best server for a client based on criteria such as geographical location and server capacity. Tools like Apache Zookeeper are commonly used to register available servers and select the optimal one.


## 📂 Category: Social Networks & Feeds (1 cards)

### 🟢 Junior Level

#### 1. What are the basic RESTful API endpoints required for a social media newsfeed system?
**Answer:**
1. Feed publishing: POST /v1/me/feed with parameters content and auth_token.
2. Newsfeed retrieval: GET /v1/me/feed requiring an auth_token for request authentication.


## 📂 Category: Software Architecture (6 cards)

### 🟢 Junior Level

#### 1. What is meant by a 'big ball of mud' in software architecture?
**Answer:**
A 'big ball of mud' describes a software system or project mired in growing complexity, lacking perceivable architectural structure, and characterized by haphazardly structured code and tangled dependencies.

#### 2. Which tool category reduces boilerplate code required for the data-to-object translation layer in applications?
**Answer:**
Object-Relational Mapping (ORM) frameworks, such as ActiveRecord and Hibernate. They reduce translation boilerplate, though they cannot entirely hide underlying database model differences.


### 🟡 Mid Level

#### 1. How do good software abstractions reduce accidental complexity?
**Answer:**
A good abstraction hides intricate implementation details behind a clean, simple-to-understand facade. Reusing well-designed abstractions across multiple applications prevents reimplementation overhead, standardizes behavior, and improves overall software quality as fixes and optimizations benefit all consumers.

#### 2. What are the fundamental terms used in event-sourcing architectures?
**Answer:**
Command, Event, State, and State machine.

#### 3. What is accidental complexity in software engineering?
**Answer:**
As defined by Moseley and Marks, complexity is accidental if it is not inherent in the problem that the software solves (from the users' perspective) but arises solely from implementation decisions and tooling.

#### 4. What is the Strangler Fig Pattern?
**Answer:**
The Strangler Fig Pattern is a software development pattern used to incrementally migrate a legacy system by gradually replacing specific pieces of functionality with new applications and services, until the old system is completely 'strangled' and decommissioned.


## 📂 Category: Software Architecture & Deployment (1 cards)

### 🟢 Junior Level

#### 1. Why can code changes in server-side and client-side applications rarely happen instantaneously?
**Answer:**
Server-side applications require rolling upgrades (staged rollouts) to deploy changes across a few nodes at a time for zero downtime. Client-side applications depend on users choosing to install updates, preventing instantaneous rollout.


## 📂 Category: Software Engineering Practices (1 cards)

### 🟢 Junior Level

#### 1. What is the purpose of continuous integration (CI)?
**Answer:**
Continuous integration is the practice of automatically building, testing, and merging code changes into a shared repository frequently to detect integration errors and bugs as early as possible.


## 📂 Category: Software Engineering Principles (1 cards)

### 🟢 Junior Level

#### 1. What is maintainability in software and system architecture?
**Answer:**
Maintainability ensures that over time, different engineering and operations teams can work on the system productively, successfully maintaining current behaviors while adapting the architecture to new functional and non-functional requirements.


## 📂 Category: Spatial & Geospatial Systems (1 cards)

### 🟢 Junior Level

#### 1. What is the evenly divided grid algorithm for location-based services and what are its limitations?
**Answer:**
The evenly divided grid algorithm splits a geographic map into a uniform grid of small squares where each business belongs to a single grid. While simple, it causes a severe uneven data distribution due to high business density in urban centers versus sparse regions like deserts or oceans. Ideally, systems should use more granular grids for dense areas and larger grids for sparse areas.


## 📂 Category: Spatial & Proximity Systems (2 cards)

### 🟡 Mid Level

#### 1. What geometric definitions, concurrency metrics, and lifecycle rules define a social network's 'nearby friends' feature?
**Answer:**
1. Proximity Threshold: Straight-line distance radius set to 5 miles (configurable).
2. Scale: 1 billion total users, with 10% utilizing the nearby friends feature concurrently.
3. Data Retention: Persistent location history storage required to feed downstream machine learning pipelines.
4. Inactivity Policy: Friends inactive for more than 10 minutes are automatically dropped from the active nearby list rather than displaying stale last-known locations.

#### 2. What scoping parameters and update frequencies must be determined when designing a location-based proximity service?
**Answer:**
1. Search Radius: Fixed or variable ranges (e.g., 0.5km up to 20km) with explicit policies on whether searches expand dynamically if few results match.
2. Data Freshness: Business additions, deletions, and updates do not require real-time reflection; updates can take effect on a batch schedule (e.g., the next day).
3. Client Movement: Client velocity is assumed to be slow enough that real-time continuous page refreshing is unnecessary.


## 📂 Category: Spatial Data Structures (1 cards)

### 🔴 Senior Level

#### 1. What kind of metadata and data structures are stored inside quadtree nodes for spatial indexing?
**Answer:**
Leaf nodes store grid boundary coordinates (top-left and bottom-right) alongside a list of business IDs located within that grid. Internal nodes store boundary coordinates plus four pointers to their child quadrants.


## 📂 Category: Spatial Databases (1 cards)

### 🔴 Senior Level

#### 1. What are the primary boundary issues encountered with Geohashing?
**Answer:**
1. Proximity without prefix match: Two geographically close locations separated by a major boundary (like the prime meridian or equator) can have completely different geohash prefixes. 
2. Long prefix mismatch: Locations with long shared prefixes can sometimes belong to adjacent, non-contiguous grid blocks. 
Mitigation: Query the target geohash along with its neighboring geohashes.


## 📂 Category: Spatial Indexing (2 cards)

### 🟡 Mid Level

#### 1. What are the recommended approaches for scaling a geohash index database?
**Answer:**
While sharding is a common talking point, it adds complexity to the application layer and may be unnecessary if data fits within a single server's working set. Adding read replicas is the recommended approach for scaling geospatial index tables because it is significantly simpler to develop, maintain, and handle read-heavy workloads.


### 🔴 Senior Level

#### 1. What are the advantages of Google S2 over traditional geohashing?
**Answer:**
S2 excels at arbitrary geofencing (dynamic or predefined perimeters) and triggers notifications for objects outside/inside areas. Its Region Cover algorithm allows specifying min level, max level, and max cells, yielding more granular and flexible cell sizes compared to fixed-precision geohashes.


## 📂 Category: Spatial Indexing & Algorithms (2 cards)

### 🟡 Mid Level

#### 1. How do you query nearby businesses using an in-memory Quadtree?
**Answer:**
Start traversing the quadtree from the root node down until you find the leaf node matching the search origin coordinates. If that leaf node contains enough businesses (e.g., 100), return them. Otherwise, expand the search outward by aggregating businesses from neighboring leaf nodes until the desired quota is met.


### 🔴 Senior Level

#### 1. What is the time complexity and operational cost of building a spatial Quadtree for 200 million businesses?
**Answer:**
Assuming each leaf node holds roughly 100 business IDs, the time complexity to build the tree is O((N/100) log(N/100)), where N is the total number of businesses. Building a full quadtree for 200 million items can take a few minutes and is typically done in-memory on startup.


## 📂 Category: Spatial Systems (4 cards)

### 🟢 Junior Level

#### 1. What are the functional requirements for a proximity/location-based service?
**Answer:**
Return all businesses based on a user's coordinate pair (latitude, longitude) and a search radius; allow business owners to perform CRUD operations on business listings (does not require real-time reflection); allow customers to view detailed information about a business.

#### 2. What is Map Projection when moving from a 2D map to a 3D globe?
**Answer:**
Map Projection is the process of translating points from a 3D globe to a 2D plane. Almost all projection methods distort actual geometry. Google Maps uses a modified version of the Mercator projection called Web Mercator.


### 🟡 Mid Level

#### 1. What are the geometric and algorithmic steps for creating a Geohash?
**Answer:**
1. Divide the world along the prime meridian and equator: latitudes [-90, 0] = 0, [0, 90] = 1; longitudes [-180, 0] = 0, [0, 180] = 1. 2. Subdivide each quadrant recursively into four smaller grids, interleaving longitude and latitude bits. 3. Repeat until the desired precision is met, and encode the resulting bit string using Base32 representation.

#### 2. What is a real-world use case of a quadtree in spatial indexing?
**Answer:**
Quadtrees are used for spatial indexing (e.g., mapping services near Denver). They adapt dynamically by providing smaller, more granular grids for densely populated areas and larger grids for sparse regions.


## 📂 Category: Storage (1 cards)

### 🟢 Junior Level

#### 1. Explain S3-compatible object storage
**Answer:**
A scalable storage architecture modeled after Amazon S3 that manages data as discrete objects (data, metadata, and unique identifiers) accessed via RESTful APIs. It provides high durability, flat namespace organization, and horizontal scalability.


## 📂 Category: Storage & Caching (1 cards)

### 🟡 Mid Level

#### 1. How should temporary and permanent storage be structured in a video streaming service?
**Answer:**
Metadata is small and frequently accessed, making in-memory caching and relational/NoSQL storage ideal. Large video or audio binaries are stored in distributed blob storage. Temporary storage used during video processing pipelines (encoding/transcoding) is freed up once processing completes.


## 📂 Category: Storage & Database Design (1 cards)

### 🟡 Mid Level

#### 1. Why are cloud object stores (like Amazon S3) preferred over NoSQL column-family databases (like Cassandra) for storing large attachments?
**Answer:**
Object stores like S3 are scalable storage infrastructures specifically designed for large files (images, videos, documents). Cassandra is poorly suited for large attachments because: 1) Although its theoretical blob size limit is 2GB, practical limits are under 1MB, and 2) Storing large attachments in Cassandra consumes excessive memory space, preventing effective use of row caches.


## 📂 Category: Storage & Databases (19 cards)

### 🟢 Junior Level

#### 1. What are the core properties of a key-value pair and how are keys/values handled?
**Answer:**
The key must be unique, and the associated value is accessed through it. Keys can be plain text (e.g., “last_logged_in_at”) or hashed (e.g., 253DDEC4). Short keys work better for performance. Values can be strings, lists, objects, etc., and are usually treated as opaque objects by key-value stores like Amazon Dynamo, Memcached, and Redis.

#### 2. What is the fundamental performance trade-off introduced when adding database indexes?
**Answer:**
Well-chosen indexes significantly speed up read queries by avoiding full table scans, but every index introduces write overhead because the index structure must be updated on every INSERT, UPDATE, or DELETE operation.


### 🟡 Mid Level

#### 1. How do you leverage data encoding and delta compression to minimize metrics storage footprint in time-series databases?
**Answer:**
Instead of storing full absolute values (e.g., full 32-bit timestamps), store a single base value accompanied by the computed delta (differences) of subsequent points. For instance, timestamps `1610087371` and `1610087381` differ by only 10 seconds, which can be encoded using far fewer bits (e.g., `1610087371, 10, 10, 9, 11`).

#### 2. How do you manage and scale the S3 bucket metadata table?
**Answer:**
Since users have a limit on the number of buckets they can create, the total bucket table size remains relatively small (e.g., 1 million customers * 10 buckets * 1 KB = 10 GB), which can easily fit in a modern single database server. If CPU or network bandwidth becomes a bottleneck for read requests, read load can be scaled horizontally using multiple database read replicas.

#### 3. How do you use database CHECK constraints to prevent over-booking in low-contention inventory systems?
**Answer:**
Add a database-level check constraint to the inventory table, such as: `CONSTRAINT check_room_count CHECK ((total_inventory - total_reserved >= 0))`. If a concurrent reservation attempt violates this constraint, the transaction automatically rolls back. While simple to implement and ideal for low-contention systems, high data contention can lead to heavy transaction failure rates.

#### 4. How do you use downsampling policies to optimize long-term storage utilization in time-series metric databases?
**Answer:**
Downsampling converts high-resolution raw data into lower-resolution aggregates as data ages, governed by time-retention rules. For example: raw 10-second resolution for 7 days; rolled-up 1-minute resolution for 30 days; and rolled-up 1-hour resolution (using averages/mins/maxes) for 1 year, drastically dropping total disk usage.

#### 5. How does a Hash Index work internally?
**Answer:**
A Hash Index is a data structure that uses a hash function to map keys directly to bucket locations in a fixed-size array (key -> hash(key) -> array position).

#### 6. What are the primary performance trade-offs in key-value store design?
**Answer:**
The core architectural trade-offs revolve around optimizing read latency, write throughput, and memory/storage usage.

#### 7. What are the pros and cons of using databases (Relational or NoSQL) for persisting message queues?
**Answer:**
Pros:
- Handles general storage requirements using tables or collections.
Cons:
- Databases are not ideal for message queues because designing a single database architecture that handles both write-heavy ingestion and high-throughput read patterns at massive scale is extremely difficult. It frequently becomes a system bottleneck.

#### 8. What storage systems are ideal for monitoring, metrics, and alerting systems, and why?
**Answer:**
Time-series databases (TSDBs) like InfluxDB, Prometheus, OpenTSDB, and Amazon Timestream. They are optimized for high-volume time-series writes, use in-memory caches combined with on-disk storage, offer custom query interfaces, and support efficient aggregation and analysis by low-cardinality labels (tags).


### 🔴 Senior Level

#### 1. How do LSM-trees simplify write operations in column-oriented stores?
**Answer:**
All writes first target an in-memory store (MemTable), adding data to a sorted structure regardless of whether it is row or column-oriented. Once accumulated, memtables are flushed and merged with immutable column files on disk in bulk. Query engines combine recent in-memory writes with older on-disk column data transparently via the query optimizer.

#### 2. How do you design partitioning for a NoSQL-based leaderboard to balance write load and read complexity?
**Answer:**
Partitions can be structured based on write volume or DAU (Daily Active Users) with a partition key pattern like `game_name#{year-month}#p{partition_number}` and a Global Secondary Index (GSI) using the score as the sort key.

Trade-off:
- Spreading monthly data across N partitions lowers individual partition write/storage load.
- However, reading top items requires a 'scatter-gather' pattern—querying all N local partitions concurrently ('scatter') and merging/sorting the results at the application layer ('gather').

#### 3. How do you scale an object metadata table in large-scale distributed object storage (like S3)?
**Answer:**
Sharding by bucket_id causes hotspot shards for buckets with billions of objects. Sharding purely by object_id evenly distributes load but makes URI-based queries inefficient. The optimal strategy is to shard by a combination of `bucket_name` and `object_name`, using the hash of `(bucket_name, object_name)` as the sharding key to uniformly distribute data while supporting URI-based metadata operations and uploads.

#### 4. How do you solve pagination and listing performance issues in a sharded object storage database?
**Answer:**
Because object storage is tuned for durability and massive scale rather than quick listing, list operations are inherently sub-optimal. To fix this, denormalize listing data into a separate, dedicated table sharded purely by `bucket_id`. This isolates pagination/listing queries to a single database shard, drastically improving performance even for buckets with billions of items.

#### 5. What are the engineering solutions for issues caused by storing many small objects as individual files?
**Answer:**
Merge many small objects into a larger file (similar to a Write-Ahead Log / WAL). New objects are appended sequentially. When the file reaches capacity (e.g., a few GBs), it becomes read-only and a new read-write file is created. To prevent write serialization bottlenecks across multiple CPU cores, maintain dedicated read-write files per core.

#### 6. What are the pros and cons of database query optimizers?
**Answer:**
Pros:
- Built once for relational databases, allowing all applications to automatically benefit from optimized access paths without handcoding queries.
Cons:
- Query optimizers are extremely complex engineering systems that require years of research and development. Without one, handcoding specific paths for individual queries is easier in the short term, but general-purpose optimizers win in long-term maintainability.

#### 7. What are the pros and cons of using a Write-Ahead Log (WAL) for persisting messages?
**Answer:**
Pros:
- Plain append-only file structure providing pure sequential read/write disk access patterns, which are highly performant and run on affordable high-capacity rotational disks.
- Supports monotonically increasing offsets per partition.
- Segment-based division prevents infinite file growth; non-active segments can be read or truncated based on retention limits.
Cons:
- Requires careful management of active versus inactive segments and manual implementation of log truncation and rotation.

#### 8. What is the role of a garbage collector in distributed object storage (like S3)?
**Answer:**
Garbage collection automatically reclaims unused storage space from lazy object deletions, orphaned data (e.g., abandoned multipart uploads), and corrupted data (failed checksums). Compaction mechanisms periodically clean up these files across primary nodes, replicas, and erasure-coded shards.

#### 9. Why are traditional file-directory mail servers (like Maildir) inadequate for modern high-scale email storage?
**Answer:**
Traditional mail servers store emails in local file directories (one file per email), which worked well for small user bases. However, at scale, they face severe limitations:
- Disk I/O bottlenecks when handling billions of files and complex directory structures.
- Inability to efficiently run backups or fast retrievals.
- Lack of native high availability and fault tolerance (disk failures cause data loss). 
Modern email systems require reliable, distributed storage layers.


## 📂 Category: Storage & Indexing (2 cards)

### 🔴 Senior Level

#### 1. How do SSDs mitigate write amplification?
**Answer:**
SSD firmware internally uses a log-structured algorithm to translate random writes from the storage engine into sequential writes on the underlying flash memory chips. Lower write amplification and reduced fragmentation increase available I/O bandwidth and extend SSD lifespan.

#### 2. How do full-text search engines like Lucene access data and handle fuzzy matching?
**Answer:**
Lucene uses an SSTable-like structure for its term dictionary, paired with an in-memory finite state automaton over the characters of the keys (acting like a trie) instead of LevelDB's sparse sorted key index. This automaton can be transformed into a Levenshtein automaton to support efficient fuzzy searches within a given edit distance.


## 📂 Category: Storage & Infrastructure (1 cards)

### 🟢 Junior Level

#### 1. How does object storage differ from file storage?
**Answer:**
File storage organizes data hierarchically in directories and files, using POSIX-compliant semantics suitable for shared file systems. Object storage strips away the hierarchical directory tree, storing data as flat 'objects' identified by a unique key/ID alongside customizable metadata, accessed primarily via RESTful HTTP APIs for massive scale and durability.


## 📂 Category: Storage & Persistence (2 cards)

### 🟡 Mid Level

#### 1. What are SSTables (Sorted String Tables) and how do they function within LSM Trees?
**Answer:**
SSTables are immutable, sorted files used in LSM (Log-Structured Merge) Trees to store key-value pairs in sorted order on disk. Because keys are sorted, SSTables allow efficient point lookups, fast range queries, and streamlined background compaction/merging processes.


### 🔴 Senior Level

#### 1. How can disk-based distributed messaging queues achieve high throughput despite using rotational disks?
**Answer:**
By leveraging sequential access patterns. While rotational disks are slow for random I/O, writing data sequentially (such as in an append-only Write-Ahead Log) combined with RAID striping can achieve hundreds of MB/sec of read/write throughput. Additionally, modern operating systems aggressively cache sequential disk data in main memory (Page Cache), drastically reducing physical disk reads.


## 📂 Category: Storage Engines (27 cards)

### 🟢 Junior Level

#### 1. What are the limitations of Hash Indexes?
**Answer:**
1. Only supports exact match lookups
2. No range queries support
3. Not suitable for dynamic resizing
4. Poor performance with high collision rates

#### 2. What are the main advantages of B-Trees?
**Answer:**
1. Balanced tree structure
2. Efficient for range queries
3. Good for both reads and writes
4. Minimal height with large branching factor

#### 3. What is a database index and how does it affect database operations?
**Answer:**
An index is an additional data structure derived from the primary data (such as a CSV log or table) used to efficiently locate values for particular keys. Adding or removing indexes does not affect the underlying data contents; it only optimizes query performance at the cost of additional write overhead and storage space.

#### 4. What is the simplest way to index key-value stores on disk?
**Answer:**
Using hash maps (hash tables), similar to in-memory dictionary implementations, to index data on disk.


### 🟡 Mid Level

#### 1. Is column-oriented storage strictly limited to the relational data model?
**Answer:**
No. While easiest to understand in relational models, columnar storage applies to nonrelational data as well. For example, Apache Parquet is a columnar storage format supporting document data models.

#### 2. What are LSM trees and what are their use cases?
**Answer:**
Log-Structured Merge-Trees are write-optimized data structures that buffer writes in memory (MemTable) before flushing them to immutable sorted files on disk (SSTables), commonly used in engines like RocksDB and Cassandra for high-throughput write workloads.

#### 3. What are the main advantages of LSM-trees?
**Answer:**
LSM-trees maintain a cascade of SSTables that are merged in the background. They continue to work well even when datasets exceed available memory. Because data is stored in sorted order, they efficiently perform range queries, and sequential disk writes allow LSM-trees to support remarkably high write throughput.

#### 4. What are the main components of an LSM Tree?
**Answer:**
1. Memtable (in-memory buffer, typically a red-black tree or skiplist)
2. Write-ahead log (WAL) for crash recovery
3. Multiple levels of immutable sorted string tables (SSTables)
4. Background compaction process to merge and clean up SSTables

#### 5. What are the performance issues and limitations of storing small objects as individual standalone files in a file system?
**Answer:**
It causes two major issues: (1) Wasted disk blocks, as files smaller than the fixed block size (e.g., 4 KB) still consume an entire block; (2) Exhaustion of inode capacity, since file systems have a fixed number of inodes initialized at format time, and operating systems struggle to manage massive numbers of inodes efficiently.

#### 6. What does a B-tree leaf page contain?
**Answer:**
A B-tree leaf page either contains the actual value for each key inline or contains references (pointers) to the disk pages where the values can be found.

#### 7. What is a Write-Ahead Log (WAL) and how does it ensure crash resilience?
**Answer:**
A WAL (or redo log) is an append-only disk file to which every database modification must be written before it can be applied to the actual data pages (e.g., in B-trees). Upon recovery after a crash, the database replays this log to restore the data structures to a consistent state.

#### 8. What is the core difference in how B-trees and LSM-trees handle data overwrites?
**Answer:**
B-trees overwrite existing pages in place on disk, assuming the physical page location remains unchanged. In contrast, LSM-trees never modify files in place; they exclusively append new writes to immutable log files (SSTables) and lazily reclaim obsolete records via background compaction.

#### 9. What is the sort order of column stores?
**Answer:**
Rows can be stored in insertion order for fast appends, or an explicit sort order (similar to SSTables) can be imposed to act as an indexing mechanism for faster queries.


### 🔴 Senior Level

#### 1. How do multiple sort orders in a column-oriented store compare to secondary indexes in a row-oriented store?
**Answer:**
Multiple sort orders in a column store are similar to secondary indexes in a row-oriented store. However, a row-oriented store keeps every row in a heap file or clustered index, and secondary indexes contain pointers to those matching rows. In a column store, there are normally no pointers to data elsewhere; columns contain values directly, eliminating pointer chasing overhead.

#### 2. How do you prevent log-structured storage engines from eventually running out of disk space during continuous appends?
**Answer:**
Break the log into fixed-size segments by closing a file when it reaches a threshold and writing to a new one. Perform background compaction to discard duplicate keys, keeping only the most recent update per key, and merge smaller compacted segments together.

#### 3. How is concurrency handled in B-trees versus LSM-trees?
**Answer:**
B-trees require lightweight locks called latches to protect data structures against concurrent updates in place to prevent reading inconsistent states. In contrast, LSM-trees are simpler for concurrency because they perform all merging in the background without interfering with incoming queries, and atomically swap old segments for new segments.

#### 4. What are the advantages of SSTables (Sorted String Tables) over log segments with hash indexes?
**Answer:**
Segment merging is simple and efficient even for files larger than available RAM. An index of all keys in memory is no longer required to find a key. Records can be grouped into blocks and compressed before disk writes, saving disk space and reducing I/O.

#### 5. What data structure is used to quickly determine which SSTable contains a given key in LSM-tree storage engines?
**Answer:**
A Bloom filter, which is a space-efficient probabilistic data structure used to test whether an element is definitely not in a set or possibly in it.

#### 6. What is an LSM Tree (Log-Structured Merge-Tree) and what is its primary advantage?
**Answer:**
An LSM Tree is a storage engine data structure designed to provide high write throughput. It maintains a hierarchy of data structures that are periodically merged from memory down to disk (Memtable -> SSTable Level 0 -> SSTable Level 1 -> ...), converting random writes into sequential disk I/O.

#### 7. What is an SSTable (Sorted String Table)?
**Answer:**
An SSTable is a log-structured storage file format where a sequence of key-value pairs is sorted by key. Each key appears only once within each merged segment file (enforced by compaction). This design allows for efficient point lookups and range queries while supporting sequential write optimizations during flushes.

#### 8. What is an alternative to a Write-Ahead Log (WAL) for database crash recovery and concurrency control?
**Answer:**
Instead of overwriting pages and maintaining a WAL, databases like LMDB use a copy-on-write (CoW) scheme. A modified page is written to a different location, and a new version of the parent pages in the tree is created, pointing to the new location.

#### 9. What is key abbreviation in B-trees?
**Answer:**
Key abbreviation saves internal page space by storing only enough characters of a key to act as boundaries between key ranges, rather than the entire key. This optimization increases the branching factor, reduces the number of tree levels, and is a foundational characteristic often generalized in B+ trees.

#### 10. What is the anti-caching approach in database architecture?
**Answer:**
An architecture that extends in-memory databases to support datasets larger than RAM by evicting Least Recently Used (LRU) data to disk and reloading it upon future access. Unlike OS virtual memory/swapping, the database manages memory at the granularity of individual records rather than entire memory pages. Note that indexes typically still need to fit entirely in memory.

#### 11. What is the compaction process in LSM-Trees and how are frozen segments handled?
**Answer:**
Compaction merges multiple sorted string tables (SSTables) into a single optimized SSTable, purging duplicate keys and deleted (tombstone) entries to reclaim disk space and maintain read performance. Because immutable segment files are never modified in-place, merging runs safely in a background thread while reads/writes continue against old segments. Once complete, read routing is atomically switched to the new segment and old files are deleted.

#### 12. What is the purpose of a Bloom filter in database storage engines like LSM-trees?
**Answer:**
A Bloom filter is a space-efficient probabilistic data structure used to quickly determine which SSTables might contain a specific key, avoiding unnecessary disk reads for non-existent keys.

#### 13. What is the purpose of in-memory sparse indexes in SSTables?
**Answer:**
In-memory sparse indexes map a subset of keys to their file offsets (e.g., one key for every few kilobytes), enabling rapid disk seeks since a few kilobytes of sequential data can be scanned quickly into memory.

#### 14. What is write amplification in database storage engines?
**Answer:**
Write amplification is the phenomenon where a single logical write to a database results in multiple physical writes to the disk over its lifetime. Examples include writing to a WAL and then to a tree page in B-trees, or repeated compaction and merging in LSM-tree SSTables. It is especially critical for SSD longevity.


## 📂 Category: Storage Systems (20 cards)

### 🟢 Junior Level

#### 1. Describe a single-server conceptual design for a file storage and synchronization service like Google Drive.
**Answer:**
Consists of an Apache web server for handling file uploads/downloads, a relational database (e.g., MySQL) for managing relational metadata (user accounts, authentication credentials, file attributes, and namespaces), and a local root directory ('drive/') acting as the flat or hierarchical file store. Each user is allocated a dedicated namespace directory where filenames map directly to their relative paths on disk.

#### 2. How does Amazon S3 organize objects and simulate directory hierarchies using prefixes?
**Answer:**
S3 stores objects in a flat structure rather than a traditional hierarchical file system, accessed via paths formatted as `s3://bucket-name/object-name`. To simulate directories, S3 uses 'prefixes'—strings at the beginning of an object name (e.g., `abc/d/e/f/` in `s3://mybucket/abc/d/e/f/file.txt`). Listing a bucket by prefix limits results to objects starting with that exact string.

#### 3. How does a block server handle newly added files for cloud storage?
**Answer:**
The file is first split into smaller blocks. Each block is compressed using compression algorithms, encrypted for security, and subsequently uploaded to cloud storage.

#### 4. What are the most important core workflows in an object storage system?
**Answer:**
1. Uploading an object.
2. Downloading an object.
3. Object versioning and listing objects within a bucket.

#### 5. What is file storage?
**Answer:**
File storage is built on top of block storage, providing a higher-level abstraction where data is stored as files under a hierarchical directory structure. It is accessible by many servers using common file-level network protocols like SMB/CIFS and NFS, shielding accessing servers from managing blocks or formatting volumes. It is ideal for sharing large numbers of files and folders within an organization.

#### 6. What is the 'write once, read many times' (WORM) property in object storage?
**Answer:**
The WORM data access pattern characterizes workloads where data objects are written once and subsequently read many times. For instance, data analytics and enterprise storage research (such as data from LinkedIn) indicates that up to 95% of object storage requests are read operations.

#### 7. What is the difference between hot and cold storage?
**Answer:**
Hot storage is designed for frequently accessed data with optimization for low latency and high performance, whereas cold storage is meant for rarely accessed archival data optimized for minimal storage cost.


### 🟡 Mid Level

#### 1. How is deletion handled for versioned objects in object storage?
**Answer:**
Deleting a versioned object does not remove existing versions from the bucket; instead, a delete marker is inserted. This delete marker becomes the new current version of the object. Subsequent GET requests targeting a delete marker return a `404 Object Not Found` error.

#### 2. What are the required object listing APIs in an S3-like object storage system?
**Answer:**
1. List all buckets owned by a user (`aws s3 list-buckets`).
2. List objects at the same level as a specified prefix, rolling up deeper paths into common prefixes (`aws s3 ls s3://mybucket/abc/`).
3. Recursively list all objects sharing a prefix (`aws s3 ls s3://mybucket/abc/ --recursive`).

#### 3. What is RAID in network attached storage?
**Answer:**
Redundant Array of Independent Disks (RAID) is a data storage virtualization technology that combines multiple physical disk drive components into one or more logical units for the purposes of data redundancy, performance improvement, or both.

#### 4. What is a search store in an email system?
**Answer:**
A distributed document store utilizing an inverted index data structure to support extremely fast, full-text searches over email messages and metadata.

#### 5. What is object immutability in object storage systems?
**Answer:**
Object immutability means that stored objects cannot be incrementally modified. They can only be deleted entirely or replaced wholesale with a brand new version of the object.

#### 6. What is object storage and what are its typical use cases?
**Answer:**
Object storage sacrifices low-latency performance to achieve high durability, massive horizontal scale, and low cost. It stores data as flat objects (no hierarchical directory structures) accessed via RESTful APIs. It is primarily used for 'cold' data, backups, and archival storage (e.g., AWS S3, Google Cloud Storage, Azure Blob Storage).

#### 7. What is object versioning in S3-compatible object storage?
**Answer:**
Versioning keeps multiple variants of an object in a bucket to protect against accidental deletions or overwrites. Without versioning, replacing a file updates its metadata and marks the old version as deleted for garbage collection. With versioning, all previous versions are retained in the metadata store and never marked as deleted in the underlying object store.


### 🔴 Senior Level

#### 1. How is metadata stored in Ceph’s Rados Gateway?
**Answer:**
There is no standalone metadata store in Ceph’s Rados Gateway. Everything, including the object bucket, is persisted as one or multiple Rados objects, treating metadata and data as logical components.

#### 2. What alternatives exist to full data replication for increasing data durability, such as erasure coding?
**Answer:**
Erasure coding breaks data into K data chunks and computes M parity chunks (e.g., 4+2 erasure coding), distributing them across different failure domains (servers/racks). It provides high data durability with significantly lower storage overhead than triple replication (3x). If K chunks are available, lost data chunks can be mathematically reconstructed using linear algebra/parity calculations.

#### 3. What architectural requirements, object scales, and durability SLAs define an S3-like object storage service?
**Answer:**
1. Core Features: Bucket creation, object upload/download, object versioning, and bucket listing (similar to `aws s3 ls`).
2. Data Distribution: Efficiently handles both massive objects (several gigabytes or more) and a high volume of tiny objects (tens of kilobytes).
3. Capacity: 100 petabytes (PB) stored within a one-year horizon.
4. SLAs: 6 nines (99.9999%) data durability and 4 nines (99.99%) service availability.

#### 4. What are the primary trade-offs of using Relational Databases, Distributed Object Storage, and NoSQL for storing email metadata and raw emails?
**Answer:**
1. Relational Databases (MySQL/PostgreSQL): Excellent for indexing headers and fast search, but poorly optimized for large payloads (like HTML emails >100KB) and unstructured BLOB search efficiency.
2. Distributed Object Storage (Amazon S3): Highly scalable and ideal for raw email backups and attachments, but inefficient for granular metadata operations like marking read/unread, keyword searching, or threading.
3. NoSQL (Bigtable/Cassandra): Proven at hyper-scale (e.g., Gmail using Bigtable), but complex to configure schemas for full-text search and open-source availability varies.

#### 5. What is erasure coding and what are its trade-offs compared to traditional replication?
**Answer:**
Erasure coding (e.g., an (8+4) setup) breaks original data into K chunks and calculates M parity chunks, distributing all K+M pieces across different failure domains. Trade-offs: It significantly lowers storage overhead (e.g., 50% overhead for (8+4) compared to 200% for 3-copy replication) and increases durability, but requires reading from multiple healthy nodes concurrently (lower access speed).

#### 6. What is the design philosophy behind object storage?
**Answer:**
Object storage separates mutable metadata (stored in a metadata store, similar to a UNIX inode) from immutable object data (stored in a data store over a network). This separation enables independent implementation, scaling, and optimization of both components.


## 📂 Category: Stream Processing (8 cards)

### 🟡 Mid Level

#### 1. What are common stream processing use cases?
**Answer:**
Common stream processing use cases include real-time fraud detection, live metrics and monitoring dashboards, IoT sensor data anomaly detection, real-time recommendation engines, and continuous ETL pipelines.

#### 2. What are the four primary types of aggregation windows in data-intensive systems?
**Answer:**
According to 'Designing Data-Intensive Applications', the four types of window functions are:
1. Tumbling (fixed) window: Non-overlapping, same-length chunks of time (e.g., aggregating ad clicks every minute).
2. Hopping window: Overlapping fixed-length windows.
3. Sliding window: Events grouped within a window that moves continuously across the data stream (e.g., top N most clicked ads during the last M minutes).
4. Session window: Dynamic window based on user inactivity periods.

#### 3. What are the key differences between batch and stream processing?
**Answer:**
Batch processing handles large, bounded datasets over extended intervals with high throughput and higher latency. Stream processing handles unbounded, real-time data incrementally with low (sub-second) latency, often trading off some exactness for timeliness (e.g., using approximate algorithms or watermarks for out-of-order data).

#### 4. What is stream processing?
**Answer:**
Stream processing is a data processing paradigm designed to ingest, process, and analyze continuous, unbounded streams of real-time data with low latency.

#### 5. What is stream windowing and what are its primary types?
**Answer:**
Stream windowing is a technique used in stream processing to divide an unbounded stream of data into finite chunks over which calculations can be applied. Primary types include: Tumbling windows (fixed-size, non-overlapping, contiguous time intervals), Sliding windows (fixed-size, overlapping intervals defined by a window size and slide parameter), Session windows (dynamic windows grouped by periods of activity separated by gaps of inactivity), and Global windows (grouping events by a global key or custom trigger logic).


### 🔴 Senior Level

#### 1. Explain stream-table join
**Answer:**
A stream-table join involves enriching a continuous stream of events with reference data from a static or slowly changing table (e.g., joining real-time clickstream events with a user profile database). In distributed stream processing engines like Kafka Streams or Flink, this is typically implemented by loading the table into local state stores (or compact topics) and performing low-latency lookups for each incoming record.

#### 2. What are the trade-offs of using a stream processing engine in an ingestion pipeline?
**Answer:**
Using engines like Flink aggregates data before writing, significantly reducing write volume. However, drawbacks include challenges in handling late-arriving events, loss of data precision, and reduced flexibility since raw data is no longer stored.

#### 3. What are the trade-offs of using event time versus processing time in event aggregation?
**Answer:**
Event Time:
- Pros: Aggregation results are more accurate because they reflect when the event actually occurred.
- Cons: Must handle delayed/out-of-order events (e.g., via watermarks). Relies on client-side clocks which may be skewed or manipulated.
Processing Time:
- Pros: Server timestamps are reliable and easy to process sequentially.
- Cons: Inaccurate representation of reality if an event experiences high latency or network delays en route to the system.


## 📂 Category: Streaming & Data Pipelines (1 cards)

### 🟡 Mid Level

#### 1. How do we prevent data loss in time-series database pipelines during outages?
**Answer:**
Place a highly reliable and scalable distributed messaging platform like Apache Kafka in front of the time-series database. Use stream processors (Apache Flink, Spark) to read from Kafka and write to the database. Kafka acts as a durable buffer that retains metrics and prevents data loss if the database goes down.


## 📂 Category: Streaming & Event Processing (1 cards)

### 🔴 Senior Level

#### 1. What is an updater service in real-time location or mapping architectures?
**Answer:**
Updater services tap into streams (such as Kafka location update streams) and asynchronously update databases like traffic databases and routing tiles. For example, routing tile processing services transform road datasets with newly found roads and closures to help shortest path/ETA services remain accurate.


## 📂 Category: System Architecture (17 cards)

### 🟢 Junior Level

#### 1. How is data represented across multiple abstraction layers from application to hardware?
**Answer:**
Applications model real-world domains via objects, APIs, and general-purpose data models (JSON, relational tables, graphs). Databases translate these models into bytes in memory, on disk, or over a network for querying and manipulation, which hardware ultimately represents via electrical currents, light pulses, or magnetic fields.

#### 2. What are the advantages of horizontal scaling over vertical scaling?
**Answer:**
Horizontal scaling overcomes the hardware ceiling limitations of vertical scaling. Combined with a load balancer, it prevents single-point-of-failure outages and mitigates performance degradation or connection failures under massive simultaneous user spikes.

#### 3. What are the architectural benefits of integrating message queues and operational tooling into a single-datacenter system design?
**Answer:**
Integrating a message queue decouples producer and consumer services, turning tight synchronous dependencies into asynchronous boundaries that absorb traffic spikes and improve failure resilience. Incorporating centralized logging, continuous monitoring, telemetry metrics, and automation tools ensures operational visibility, rapid incident detection, and predictable recovery procedures.

#### 4. What are the key limitations of vertical scaling (scaling up)?
**Answer:**
Vertical scaling has a hard hardware limit and fails to provide inherent failover, redundancy, or high availability.

#### 5. What is high availability?
**Answer:**
High availability is the ability of a system to remain continuously operational for a desirably long period of time. It is measured as an uptime percentage (e.g., 'five nines' or 99.999%), where 100% represents absolute zero downtime.

#### 6. What is horizontal scaling (sharding / scale-out)?
**Answer:**
Horizontal scaling, also referred to as 'scale-out' or sharding, is the practice of expanding system capacity by adding more servers or nodes into a pool of resources, rather than upgrading the hardware specifications of an existing single machine.

#### 7. What is system reliability?
**Answer:**
The ability of a system to continue to work correctly—performing the correct function at the desired level of performance—even in the face of adversity, such as hardware faults, software faults, or human error.

#### 8. What is system scalability?
**Answer:**
A system's ability to cope with increased load. Scalability is not a binary label ('X is scalable'); rather, it describes how a system can expand its computing resources or architectural options to handle growth in specific dimensions.

#### 9. What is the initial setup for a system designed to support millions of users?
**Answer:**
The initial setup typically involves everything running on a single server, handling web requests, application logic, and database operations locally before scaling out.

#### 10. What is the role of web servers in an email system architecture?
**Answer:**
Web servers act as public-facing request/response services used to manage stateless control-plane features such as login, signup, user profiles, and API endpoints for sending emails or loading folder structures.

#### 11. What is vertical scaling in distributed systems?
**Answer:**
Vertical scaling, referred to as 'scale up', is the process of adding more raw compute power (CPU, RAM, etc.) to a single server instance.


### 🟡 Mid Level

#### 1. What architectural pattern is commonly adopted for modern enterprise systems like hotel reservation platforms (e.g., Amazon, Netflix, Airbnb)?
**Answer:**
Microservice architecture, which decouples business domains (such as booking, inventory, payment, and notifications) into independently deployable, scalable services.

#### 2. What is fanout on read and how does it compare to fanout?
**Answer:**
Fanout is the process of delivering a post to all friends, using either fanout on write (push model) or fanout on read (pull model). In fanout on read (on-demand model), the news feed is generated and recent posts are pulled only when a user loads their home page. 
Pros: Efficient for inactive users or those who rarely log in, as it wastes no computing resources and avoids the hotkey problem since data is not pushed.
Cons: Fetching the news feed is slow because it is not pre-computed.

#### 3. What is polyglot persistence?
**Answer:**
Polyglot persistence is the architectural pattern of using multiple distinct database technologies (e.g., relational, document, key-value, graph) within a single application ecosystem, matching each specific subsystem or microservice to the datastore best suited for its access patterns.

#### 4. What is the purpose of the 'feed publishing' flow in a news feed system?
**Answer:**
The feed publishing flow handles the path when a user creates a new post, writing the post data into the persistent database/cache and fanning it out or populating it into the news feeds of their friends or followers.


### 🔴 Senior Level

#### 1. Describe a classic CQRS (Command Query Responsibility Segregation) architecture.
**Answer:**
CQRS separates read and write workloads into distinct models. Writes are handled by Command services that mutate state, often emitting events into an append-only, immutable Event Sourcing queue (enabling system reproducibility and correctness verification). Reads are handled by Query services optimized for retrieval, typically fed asynchronously by projecting data from the event stream into read-optimized denormalized stores.

#### 2. What is evolvability in data systems?
**Answer:**
Evolvability refers to the agility and ease with which a data system can be modified and adapted to changing requirements over time. It is heavily tied to system simplicity, loose coupling, and clean abstractions.


## 📂 Category: System Design (123 cards)

### 🟢 Junior Level

#### 1. Describe the RESTful API request flow and architecture for auxiliary tasks in a nearby friends feature.
**Answer:**
The entry layer consists of a cluster of stateless HTTP servers handling standard request/response traffic. This API layer manages auxiliary, non-spatial tasks such as adding or removing friends, managing user profiles, and handling authentication before requests reach downstream storage or spatial indexing layers.

#### 2. Describe the high-level architecture and components of a gaming leaderboard system.
**Answer:**
1. Players interact with a game service to play matches.
2. Upon winning, the client sends a request to the game service, which validates the win and calls the leaderboard service.
3. The leaderboard service updates the player's score in the leaderboard storage engine.
4. Players query the leaderboard service directly to fetch top-N leaderboards or their specific player rank.

#### 3. Describe the read/write ratio and database selection rationale for a proximity/location-based service.
**Answer:**
A proximity service is read-heavy due to frequent operations like searching for nearby businesses and viewing detailed business profiles. Conversely, write volume is low since adding, removing, or editing business information occurs infrequently. Due to the high read-to-write ratio and standard relational requirements, a relational database (e.g., MySQL) or specialized spatial index store is often a suitable fit.

#### 4. How do applications interact with caching servers?
**Answer:**
Applications interact with caching servers (like Memcached or Redis) via language-specific client libraries that wrap simple key-value APIs (e.g., get, set, delete, add) over TCP/IP sockets, abstracting network communication and connection pooling.

#### 5. How do clients communicate in a scalable chat system?
**Answer:**
Clients (mobile or web) do not communicate directly with each other. Instead, each client connects to a centralized chat service. The chat service receives messages, resolves target recipients, relays messages to active recipients, and temporarily holds messages on the server for offline users until they reconnect.

#### 6. How do message queues decouple modules in a video encoding architecture?
**Answer:**
Without a message queue, the video encoding module must synchronously block and wait for the output of the download module. Introducing a message queue decouples them: the encoding module pulls jobs asynchronously from the queue and can execute parallel encoding tasks independently of download speeds.

#### 7. How do push notifications work on Android devices?
**Answer:**
Android utilizes Firebase Cloud Messaging (FCM) as the primary mechanism to route and deliver push notifications to Android client applications, serving a similar function to Apple's APNs.

#### 8. How do we use cold storage to optimize the storage of metrics data?
**Answer:**
Cold storage is utilized for inactive, infrequently accessed historical data, offering significantly lower financial cost per gigabyte compared to primary/hot storage tiers. Metrics data is tiered asynchronously from hot/warm storage to cold storage (e.g., AWS S3 Glacier) based on data age and access frequency policies.

#### 9. How does URL redirecting work with URL shortening?
**Answer:**
When a client requests a shortened URL, the server responds with a 301 Moved Permanently (or 302 Found) HTTP status code and includes the original long URL in the 'Location' header, instructing the client browser to automatically redirect to the target destination.

#### 10. How does delta sync work in cloud storage?
**Answer:**
Delta sync transfers only modified blocks instead of the entire file to cloud storage. For example, if 'block 2' and 'block 5' change, only those two specific blocks are uploaded, significantly reducing network bandwidth consumption.

#### 11. How does the fixed window counter rate-limiting algorithm work?
**Answer:**
The algorithm divides the timeline into fixed-size time windows (e.g., 1 minute) and assigns a counter to each. Each incoming request increments the counter. Once the counter reaches the predefined threshold, subsequent requests are dropped or rate-limited until the next time window starts.

#### 12. How does weighted load balancing work?
**Answer:**
Weighted load balancing routes incoming traffic to backend servers proportionally based on assigned weight values (representing server capacity, CPU, or memory). Servers with higher weights receive a proportionately larger share of connections compared to those with lower weights.

#### 13. How is Peak QPS calculated and utilized in capacity planning?
**Answer:**
Peak QPS is the maximum expected query-per-second load at any given time. It is frequently approximated for capacity planning as 2 times the average QPS to ensure infrastructure can handle traffic bursts.

#### 14. What are common real-world examples of rate-limiting policies?
**Answer:**
Examples include limiting a user to a maximum of 2 posts per second, restricting account creation to 10 accounts per day per IP address, or limiting reward claims to 5 times per week per device.

#### 15. What are the core communication paradigms and formats between mobile/web clients and application servers?
**Answer:**
Web apps combine server-side logic (Java, Python) for storage/business logic with client-side presentation (HTML/JS). Mobile apps communicate via HTTP using JavaScript Object Notation (JSON) payloads for simplicity, e.g., a GET request to `/users/12` retrieving user objects.

#### 16. What are the functional requirements of a gaming or ranking leaderboard system?
**Answer:**
Display the top 10 players globally; show a specific user's exact rank; display players who are four positions above and below the target user (bonus requirement).

#### 17. What are the fundamental functional use cases of a URL shortener?
**Answer:**
The core functional use cases are: 1) URL shortening: taking a long URL as input and returning a compact, unique short URL. 2) URL redirecting: taking a short URL and redirecting the client to the original long URL, alongside non-functional guarantees like high availability, scalability, and fault tolerance.

#### 18. What are the key milestones to achieve at the end of a high-level system design phase?
**Answer:**
1. Agree on overall goals and feature scope.
2. Sketch out a high-level blueprint for the overall architecture.
3. Obtain feedback from the interviewer on the high-level design.
4. Establish initial ideas and focal points for the deep-dive phase based on feedback.

#### 19. What are the main APIs required when designing Google Drive?
**Answer:**
The core system relies primarily on 3 fundamental APIs: uploading a file, downloading a file, and retrieving file revisions.

#### 20. What are the trade-offs of polling vs push-based communication models?
**Answer:**
Polling requires clients to periodically ask servers for new data at fixed intervals. While simple to implement, frequent polling wastes network bandwidth and consumes precious server resources processing redundant requests that return no new data ('empty' polls). Push models (such as WebSockets or SSE) are more efficient for real-time updates.

#### 21. What components are needed to send iOS push notifications?
**Answer:**
A Provider (which builds and sends notification requests containing a device token and JSON payload), APNS (Apple Push Notification Service), and the iOS Device (the end client receiving the notification).

#### 22. What initial scoping questions should be clarified when designing a search autocomplete system?
**Answer:**
Key scoping parameters to establish include: 1) Whether matching is supported only at the query prefix or anywhere in the string. 2) The number of suggestions to return (e.g., top 5). 3) The ranking metric (e.g., historical query frequency/popularity). 4) Exclusion of spell-check or autocorrect features. 5) Language and character sets (e.g., English, lowercase alphabetic only). 6) Scale estimates (e.g., 10 million Daily Active Users).

#### 23. What is the first consideration and best practice when scaling the web tier horizontally?
**Answer:**
To scale horizontally, the web tier must be stateless. This is achieved by removing state (such as user sessions) from local server memory and storing it in a centralized persistent data store like a relational database or NoSQL cluster accessible by all web servers.

#### 24. What is the first step in the four-step framework for system design interviews?
**Answer:**
Understand the problem and establish the design scope.

#### 25. What is the high-level design and request flow of a newsfeed system?
**Answer:**
The system involves a Client sending requests (e.g., GET /v1/me/feed) routed via a Load Balancer to Web Servers. The Web Servers route requests to the Newsfeed Service, which fetches aggregated post IDs from a Newsfeed Cache for rendering.

#### 26. What is the initial architecture upgrade when a single monolithic server is no longer sufficient?
**Answer:**
Separating concerns by splitting traffic onto multiple servers: one tier dedicated to web/mobile traffic and a separate tier dedicated to the database, allowing them to scale independently.

#### 27. What is the most intuitive way to implement URL redirecting?
**Answer:**
Using hash tables. Given a shortURL, retrieve the longURL via hashTable.get(shortURL) and perform an HTTP redirect.

#### 28. What is the primary responsibility of a navigation service in mapping architecture?
**Answer:**
It is responsible for computing and finding the fastest travel routes between specified geographic locations.

#### 29. What is the purpose of a robots.txt file in web crawling?
**Answer:**
A robots.txt file specifies rules for web crawlers (User-agents) detailing which directories or URLs they are disallowed from accessing (e.g., Disallow: /creatorhub/* for Googlebot).

#### 30. What is the third step in the four-step framework for system design interviews?
**Answer:**
The third step is the design deep dive, where you focus on drilling down into specific bottlenecks, scaling bottlenecks, database choices, data partitioning, caching strategies, and edge cases identified during the high-level design.

#### 31. What third-party integration is critical for chat applications to alert users of incoming messages when the app is backgrounded?
**Answer:**
Push notification services (such as APNs for iOS and FCM for Android) are essential third-party integrations required to inform users of new messages when the application is not actively running.

#### 32. When should a client fetch new map tiles from a server?
**Answer:**
Clients should fetch new map tiles when the user is zooming and panning the map viewpoint to explore surroundings, or during active navigation when the user moves out of the current map tile into a nearby tile.

#### 33. Which graph traversal technique is preferred for a web crawler, and why is the alternative avoided?
**Answer:**
Breadth-First Search (BFS) is preferred. Depth-First Search (DFS) is generally avoided because the depth of the web graph can be extremely deep, leading to infinite paths or trapped subgraphs.

#### 34. Why is avoiding over-engineering a critical best practice in system design?
**Answer:**
Over-engineered systems introduce unnecessary complexity, operational overhead, and compounding maintenance costs that outweigh initial architectural benefits.

#### 35. Why is it important to explicitly label units during back-of-the-envelope estimations?
**Answer:**
To remove mathematical and conceptual ambiguity, ensuring that calculations (such as throughput, storage, and bandwidth) are coherent and defensible.

#### 36. Why should you explicitly write down your assumptions during back-of-the-envelope estimations?
**Answer:**
To establish a baseline for discussion, allowing you and interviewers to revisit, challenge, or adjust parameters systematically later.


### 🟡 Mid Level

#### 1. Calculate the QPS and 5-year media storage requirements for a platform with 300M MAU.
**Answer:**
Assumptions: 50% DAU (150M), 2 tweets/day, 10% media attachment, 5-year retention. QPS: Average = ~3,500 QPS; Peak = ~7,000 QPS. Media Storage: 150M * 2 * 10% * 1MB = 30 TB/day. 5-Year Media Storage = 30 TB * 365 * 5 = ~55 PB.

#### 2. Describe the core news feed publishing flow in a social media architecture.
**Answer:**
1. A user posts content via an API endpoint (/v1/me/feed?content=Hello&auth_token=...).
2. A load balancer distributes the request to web servers, which route traffic to internal services.
3. The Post Service persists the post in both the database and cache.
4. The Fanout Service pushes the new content to friends' news feeds stored in caches for rapid retrieval.
5. The Notification Service triggers push notifications to inform friends of the new content.

#### 3. Describe the end-to-end operational flow of a URL shortening service.
**Answer:**
Check if longURL exists in the database. If it exists, return the existing shortURL. If new, generate a unique primary key ID via a Unique ID Generator, convert the ID to a string using Base 62 encoding, and persist a new mapping record (ID, shortURL, longURL) in the database.

#### 4. Describe the file download flow in a cloud storage synchronization system.
**Answer:**
1. The notification service informs Client 2 that a file has been modified elsewhere.
2. Client 2 requests metadata changes from API servers, which query the Metadata DB.
3. Upon receiving metadata, Client 2 requests specific file blocks from block servers.
4. Block servers fetch the required blocks from underlying cloud storage.
5. Client 2 downloads all new blocks and locally reconstructs the file.

#### 5. Explain events tracking in the context of a notification system
**Answer:**
Notification metrics, such as open rate, click rate, and engagement, are vital for understanding customer behaviors. An analytics service implements events tracking, requiring deep integration between the notification delivery system and the analytics pipeline.

#### 6. Explain rate limiting in load balancers and notification systems
**Answer:**
Rate limiting restricts the number of requests or actions allowed within a specific time window using algorithms like Token Bucket or Leaky Bucket. In load balancers, it protects backend services from DDoS and abuse. In notification systems, it prevents overwhelming users to reduce opt-out and churn rates.

#### 7. Explain the contact info gathering and end-to-end flow of a notification system
**Answer:**
To send notifications, API servers collect mobile device tokens, phone numbers, or email addresses during user signup or app installation and store them in database tables (e.g., users table for emails/phones, devices table for multi-device push tokens). The high-level flow involves: 1) Services (microservices, cron jobs) triggering notification events; 2) The Notification System centralizing payload generation and routing; 3) Extensible Third-Party Services (FCM, APNS, Twilio, SendGrid) handling carrier delivery, accounting for regional availability (e.g., Jpush in China); and 4) End-user devices receiving the alerts.

#### 8. How do we architecture a scalable notification system and decouple its components?
**Answer:**
Move databases and caches out of the notification servers. Add stateless notification servers behind an auto-scaling group, and introduce message queues (e.g., Kafka/RabbitMQ) for asynchronous parallel processing. Implement internal-only APIs, request validation, and fetch metadata before queuing payloads.

#### 9. How do we select the right precision in Geohashing for location-based features?
**Answer:**
Find the minimal geohash length that fully covers the radius defined by the user (e.g., a 0.5 km radius maps to a geohash length of 6, while larger radii map to smaller lengths). Boundary edge cases must be handled explicitly with the interviewer.

#### 10. How do you design a navigation service to find routes between points?
**Answer:**
The navigation service accepts an origin and destination via an HTTP GET request behind a load balancer. It computes a reasonably fast and accurate route, returning metadata such as total distance, duration, end/start locations, step-by-step HTML instructions, and polyline coordinates. Real-time traffic changes and rerouting are handled by an auxiliary Adaptive ETA service.

#### 11. How does data flow conceptually in a nearby friends feature at a high level?
**Answer:**
It relies on efficient message passing where active users receive location updates from active friends in their vicinity, which can conceptually scale through various routing or spatial partitioning strategies.

#### 12. How does feed retrieval work in a news feed system?
**Answer:**
Clients send a feed request to a load balancer, which routes it to web servers. Web servers call the news feed service, which retrieves a ordered list of post IDs from the feed cache. The service then fully hydrates the feed by fetching complete user profiles and post payloads from respective user and post caches before returning a consolidated JSON payload to the client.

#### 13. How does write-around caching work?
**Answer:**
In write-around caching, data is written directly to the persistent datastore, bypassing the cache entirely. The cache is only populated later when a read request for that data results in a cache miss, preventing cache pollution from write-heavy workloads that are rarely read.

#### 14. How is a URL frontier designed for web crawlers?
**Answer:**
A URL frontier is typically split into two tiers: front queues, which manage prioritization and ensure important pages are crawled first, and back queues, which manage politeness constraints to ensure the crawler does not overload target web servers with excessive concurrent requests.

#### 15. How is a cached DNS resolver used in a web crawler?
**Answer:**
DNS resolution is synchronous and slow (10ms to 200ms), acting as a major bottleneck where one crawler thread can block others. Maintaining an internal DNS cache (mapping domain names to IP addresses, updated periodically via cron jobs) eliminates redundant DNS lookups and optimizes crawler throughput.

#### 16. How is communication idempotency implemented in distributed APIs?
**Answer:**
Idempotency is implemented by requiring clients to pass a unique idempotency key (typically a UUID recommended by standards like Stripe and PayPal) in the HTTP headers of mutation requests. The server records processed keys in a fast datastore with an expiration TTL, ensuring that retried requests with the same key return the cached original response without re-executing the operation.

#### 17. How is geographic locality applied in distributed web crawlers and systems?
**Answer:**
Locality is achieved by distributing components like crawl servers, caches, queues, and storage geographically closer to website hosts or users, minimizing network latency and speeding up data transfer times.

#### 18. How is online presence managed in chat applications?
**Answer:**
Online presence indicators (e.g., green status dots) are managed by dedicated presence servers that maintain persistent connections (such as WebSockets) with clients. These servers track connection states, handle heartbeat/timeout mechanisms, and broadcast status changes to authorized peers.

#### 19. How should you effectively conclude and handle follow-up discussions in a system design interview?
**Answer:**
Best practices include: 1) Providing a concise recap of your final architecture, especially if multiple options were discussed. 2) Discussing error cases (server failures, network partitions). 3) Addressing operational concerns such as metrics monitoring, error logs, and rollout strategies. 4) Explaining how to scale the system to the next tier (e.g., moving from 1M to 10M users). 5) Proposing further refinements if given more time.

#### 20. Should business counts within a spatial grid be explicitly stored inside quadtree nodes?
**Answer:**
No. Although tree subdivision logic depends on the density of businesses within a bounding box, explicit counts do not need to be stored inside the quadtree node structures since they can be dynamically computed or inferred directly from the underlying database records.

#### 21. What are the advantages of deploying a location-based service to multiple regions and availability zones?
**Answer:**
Brings users physically closer to data centers, reducing latency. Allows flexible traffic distribution across high-density population areas. Ensures compliance with local privacy and data residency laws (using DNS routing to restrict requests to specific regions).

#### 22. What are the core responsibilities of a preprocessor in a video streaming service?
**Answer:**
1. Video splitting: Divides streams into independently playable chunks known as Group of Pictures (GOP) alignment, helping legacy devices that lack dynamic splitting.
2. DAG generation: Generates workflow execution graphs based on configuration files.
3. Caching: Temporarily stores segmented GOPs and metadata in local/temporary storage to facilitate fast retries if video encoding fails.

#### 23. What are the core video processing steps required after ingestion in a video streaming architecture?
**Answer:**
The raw video is split into audio, video, and metadata components, followed by: (1) Inspection for quality and malformation, (2) Encoding across various bitrates, resolutions, and codecs, (3) Thumbnail generation (auto or user-uploaded), and (4) Watermark image overlays.

#### 24. What are the file upload types supported in cloud storage services like Google Drive, and how do resumable uploads work?
**Answer:**
Supports Simple uploads (for small files) and Resumable uploads (for large files prone to network interruptions). Resumable upload workflow: (1) Send an initial request to retrieve a unique resumable session URL, (2) Upload data chunks and monitor state, (3) Resume automatically from the last acknowledged byte offset if interrupted.

#### 25. What are the functional and non-functional requirements for a 'nearby friends' feature?
**Answer:**
Functional requirements: Users can see nearby friends on mobile apps with distance and last-updated timestamps; lists update every few seconds. Non-functional requirements: Low latency for location updates, high reliability (though occasional data loss is acceptable), and eventual consistency (location replicas can tolerate a few seconds of delay).

#### 26. What are the key clarification questions to ask when designing a web crawler?
**Answer:**
1. What is the main purpose? (e.g., search engine indexing, data mining)
2. Scale? (e.g., how many pages per month, such as 1 billion)
3. Content types? (e.g., HTML only vs PDFs/images)
4. Handle newly added or edited pages?
5. Storage requirements? (e.g., store HTML up to 5 years)
6. How to handle duplicate content? (e.g., ignore duplicate pages)

#### 27. What are the main considerations when choosing a storage system?
**Answer:**
1. Access Patterns (reads vs writes, point lookups vs range scans)
2. Consistency Requirements (strong eventual, linearizability)
3. Scalability Needs (horizontal vs vertical scaling)
4. Cost (infrastructure and operational overhead)
5. Performance Requirements (latency and throughput bounds)

#### 28. What are the main flows when designing a news feed system?
**Answer:**
1. Feed publishing: When a user publishes a post, the data is written to the database and cache, and pushed/populated to friends' news feeds.
2. Newsfeed building: The feed is dynamically built or retrieved by aggregating friends' posts, typically sorted in reverse chronological order.

#### 29. What are the major industry-standard video streaming protocols?
**Answer:**
1. MPEG-DASH (Dynamic Adaptive Streaming over HTTP)
2. Apple HLS (HTTP Live Streaming)
3. Microsoft Smooth Streaming
4. Adobe HTTP Dynamic Streaming (HDS)
Different protocols support various video encodings and playback players, which must be considered during video architecture design.

#### 30. What are the primary types of geospatial indexing methods used in industry?
**Answer:**
1. Hash-based approaches: Even grid, geohash, cartesian tiers.
2. Tree-based approaches: Quadtree, Google S2, R-Tree.
Both strategies share the high-level goal of partitioning a map into smaller spatial regions to build fast lookup indexes.

#### 31. What are the two primary flows in a news feed system architecture?
**Answer:**
1. Feed publishing: When a user publishes a post, the data is written to cache/databases and fan-out/populated into friends' news feeds.
2. News feed building: The news feed is built dynamically or pre-computed by aggregating friends' posts in a reverse chronological order.

#### 32. What are the two primary integration methods between a payment system and a Payment Service Provider (PSP)?
**Answer:**
1. API-based integration: The company is responsible for developing payment pages and safely collecting, handling, and storing sensitive payment information while relying on the PSP to connect to banks/card schemes.
2. Hosted payment page: The company avoids storing sensitive data due to regulations; instead, the PSP provides a hosted page to collect and securely store card details directly.

#### 33. What core techniques and components are involved in architecting a web crawler?
**Answer:**
Deciding between Depth-First Search (DFS) and Breadth-First Search (BFS), managing the URL frontier, building an efficient HTML Downloader, ensuring system robustness and extensibility, and mechanisms to detect and avoid problematic or duplicate content.

#### 34. What data store is generally recommended for chat systems and why?
**Answer:**
Key-value stores (e.g., HBase, Cassandra) are recommended because they allow easy horizontal scaling, provide very low latency access, and handle the long tail of data much better than relational databases as indexes grow.

#### 35. What databases are required to support a 'nearby friends' feature?
**Answer:**
A user database (relational or NoSQL) to store user profiles and friendship data, and a location history database to store historical location data.

#### 36. What is Real-Time Bidding (RTB) in digital advertising?
**Answer:**
RTB is the core automated process where digital ad inventory is bought and sold programmatically in auctions that typically execute in under a second. High data throughput and accuracy (such as aggregated click events) are vital for measuring campaign efficacy, driving dynamic billing, and allowing campaign managers to adjust bidding strategies in real-time.

#### 37. What is a ranker service in routing architectures?
**Answer:**
A service that takes route ETA predictions from a route planner, applies user-defined filters (e.g., avoid tolls or freeways), ranks the possible routes from fastest to slowest, and returns the top-K results to the navigation service.

#### 38. What is the detailed end-to-end architecture flow of a notification sending and receiving system?
**Answer:**
1. A microservice calls notification server APIs to trigger alerts. 2. Notification servers fetch user metadata, device tokens, and settings from cache or database. 3. Notification events are pushed to platform-specific message queues (e.g., iOS PN queue). 4. Background workers pull events from queues. 5. Workers dispatch notifications to third-party push providers (APNS, FCM). 6. Third-party services deliver the notifications to end-user devices.

#### 39. What is the difference between a proximity service and a nearby friends feature?
**Answer:**
In proximity services, target locations (such as business addresses) are static. In a 'nearby friends' feature, the data is highly dynamic because user locations change frequently.

#### 40. What is the purpose of the "news feed building" flow in a news feed system?
**Answer:**
The "news feed building" flow is for aggregating friends’ posts in a reverse chronological order.

#### 41. What supplementary features and scaling strategies are essential for a robust URL shortener service?
**Answer:**
Essential features include: 1) Rate limiters to filter out malicious high-volume requests based on IP or rules. 2) Horizontal scaling of the stateless web tier. 3) Database scaling via replication and sharding. 4) Analytics integration to track click metrics and traffic patterns. 5) High availability, consistency, and reliability guarantees.

#### 42. What techniques can optimize the performance of a web crawler?
**Answer:**
Distributed crawling, DNS resolver caching, locality optimization, and short timeouts.

#### 43. When should you introduce an intermediate message queue (like Kafka) between a game service and a leaderboard service?
**Answer:**
Decoupling via a message queue is only necessary if game score data must be consumed by multiple downstream services simultaneously (e.g., leaderboards, analytics, push notifications, or multiplayer turn notifications). If it's a single-purpose feature, direct synchronous calls reduce unneeded infrastructure complexity.

#### 44. Which fan-out approach is best suited for designing a scalable news feed system?
**Answer:**
A hybrid approach. Use a push model for the majority of users to ensure fast reads, and a pull model on-demand for celebrities or users with massive follower counts to avoid hotkey and system overload issues. Consistent hashing can further mitigate hotkeys.

#### 45. Why is a content parser typically decoupled from the main crawl server in web crawlers?
**Answer:**
Parsing and validating web pages (especially handling malformed HTML) is computationally intensive and prone to errors. Decoupling the content parser into a separate component prevents parsing bottlenecks from slowing down the core network crawling process.


### 🔴 Senior Level

#### 1. Compare Geohash and Quadtree for spatial indexing.
**Answer:**
Geohash: Easy to implement without building a tree; supports radius-based queries; fixed grid size per precision level (cannot dynamically adjust to population density without complex logic); easy index updates. Quadtree: Slightly harder to implement as a tree structure; natively supports k-nearest neighbor queries by dynamically adjusting query range; automatically adjusts grid size based on data density; updates and rebalancing are more complex and require thread synchronization/locking.

#### 2. Describe the architecture and data flow of a distributed rate limiter.
**Answer:**
Rules are loaded from persistent disk into a local worker cache. When a client request arrives, it hits the rate limiter middleware. The middleware inspects rules, then queries an in-memory datastore (like Redis) for sliding window counters and timestamps. If within limits, the request proceeds to API servers; otherwise, it returns HTTP 429 (Too Many Requests), optionally dropping or redirecting the payload to an async queue.

#### 3. Describe the asynchronous file upload flow in a video streaming service architecture.
**Answer:**
1. Videos are uploaded to original storage.
2. Transcoding servers fetch raw videos and perform transcoding.
3. Upon completion, two parallel steps occur: transcoded videos are sent to transcoded storage, and completion events are pushed to a completion queue.
4. Transcoded videos are distributed to CDNs.
5. Completion handler workers continuously pull events from the queue to update the metadata database and cache.
6. API servers notify the client that the video is successfully uploaded and ready for streaming.

#### 4. Describe the detailed file upload flow in a cloud storage file synchronization system.
**Answer:**
1. Add File Metadata: Client 1 requests metadata creation; the Metadata DB stores it with a 'pending' status. The notification service informs Client 2.
2. Upload Files: Client 1 uploads file content to block servers. Block servers chunk, compress, and encrypt the blocks before uploading them to cloud storage.
3. Completion: Cloud storage triggers an upload completion callback to API servers, updating the file status to 'uploaded' in the Metadata DB, and triggering the notification service to alert Client 2.

#### 5. Describe the end-to-end email receiving flow in a distributed mail system.
**Answer:**
1. Incoming emails arrive at an SMTP load balancer, which distributes traffic to SMTP servers where connection-level email acceptance policies and spam/invalid email bounces are applied.
2. Large attachments are optionally offloaded directly to an object store (e.g., S3).
3. Validated emails are placed into an incoming email queue, decoupling SMTP servers from processing workers and acting as a traffic buffer.
4. Mail processing workers filter out spam and viruses.
5. Valid emails are persisted in mail storage, cache, and object data stores.
6. If the receiver is online, the email is pushed via WebSocket real-time servers; otherwise, it waits in storage until fetched via RESTful API when the user reconnects.

#### 6. Describe the end-to-end email sending flow in a distributed mail system.
**Answer:**
1. A user submits an email via webmail; the request passes through a load balancer to rate-limit and route to web servers.
2. Web servers perform basic validation (e.g., size limits).
3. If the recipient is on the same domain, the server verifies it is spam/virus-free and inserts it directly into the sender's Sent Folder and recipient's Inbox, bypassing outbound queues.
4. Otherwise, valid emails enter an outgoing message queue (with large attachments stored in object storage and references queued), while invalid ones go to an error queue.
5. SMTP outgoing workers pull messages, perform spam/virus checks, store a copy in the Sent Folder, and transmit the email to the recipient's mail server.

#### 7. Describe the pseudo-code flow and mechanics of a FIFO order matching algorithm in a trading system.
**Answer:**
The flow begins by handling order events: checking sequence IDs (out-of-order detection), validating parameters, and branching based on message type (NEW, CANCEL). New buy orders are matched against the sell book and vice versa using FIFO ordering (orders arriving first at a given price level match first). The match loop iterates through the limit order queue at a specified price, computing leaves quantity and generating matched fills until the order is fully satisfied or no liquidity remains. Cancels verify existence in the order map before removing and marking as canceled.

#### 8. How can an event sourcing design using an mmap event store function as a message bus?
**Answer:**
An mmap event store (acting similarly to Kafka) processes external messages (e.g., FIX protocol transformed to Simple Binary Encoding) via an event store client. The matching engine consumes events, updates internal state, generates resulting events (e.g., OrderFilledEvent), and writes them back to the event store, allowing downstream microservices (reporters, market data processors) to subscribe and react.

#### 9. How can location update throughput be optimized in system design (e.g., Google Maps)?
**Answer:**
Sending GPS coordinates every second for millions of users creates massive write QPS (millions of QPS). To optimize, clients batch location updates locally and flush them less frequently (e.g., every 15-30 seconds depending on movement speed), drastically lowering peak write QPS to manageable levels.

#### 10. How do fixed partitions and hash partitions compare when implementing a leaderboard?
**Answer:**
Hash partitions cause high query latency for top-K results because large entries must be fetched and sorted across every shard, and the query is bottlenecked by the slowest partition. Hash partitioning also complicates rank lookups for specific users. Consequently, fixed partitions are typically preferred for leaderboard systems.

#### 11. How do modern high-frequency trading exchanges utilize mmap for low-latency IPC?
**Answer:**
Exchanges use the POSIX `mmap(2)` system call to map files into process memory. By targeting `/dev/shm` (a memory-backed filesystem), inter-process communication bypasses disk and network I/O entirely, achieving sub-microsecond message bus communication and enabling low-latency microservices via event sourcing.

#### 12. How do order book matching engines process large market orders?
**Answer:**
A large market buy order matches against all sell orders in the best ask queue sequentially until fulfilled. Once the shares are exhausted, the bid/ask spread widens and the market price increases to the next price level.

#### 13. How do we safely auto-scale and deploy stateful WebSocket clusters?
**Answer:**
Since WebSocket servers are stateful, gracefully remove or update nodes by marking them as 'draining' at the load balancer. This prevents new connections from being routed to the draining server while existing connections are allowed to drain and close completely before termination.

#### 14. How do you calculate map data bandwidth and CDN usage for a navigation system like Google Maps?
**Answer:**
Assuming a user moves at 30 km/h with a zoom level where each image covers 200m x 200m (256x256 pixels, ~100KB per image), an area of 1km x 1km requires 25 images (2.5 MB). At 30 km/h, this demands 75 MB per hour (1.25 MB per minute). For scale (e.g., 5 billion minutes of navigation/day), this translates to 6.25 billion MB per day, or 62,500 MB per second. Distributed across 200 CDN POPs, each POP serves a few hundred MBs per second.

#### 15. How do you modify an API and database schema to support reserving a room type rather than a specific room?
**Answer:**
API Request: Replace `roomID` with `roomTypeID` in the request parameters (e.g., POST /v1/reservations containing `startDate`, `endDate`, `hotelID`, `roomTypeID`, `roomCount`, and `reservationID`). Database Schema: Implement tables for `room` (room details), `room_type_rate` (pricing data per room type for future dates), `reservation` (guest reservation data), and `room_type_inventory` containing `hotel_id`, `room_type_id`, `date`, `total_inventory` (total rooms minus maintenance), and `total_reserved` (rooms booked for the specific criteria).

#### 16. How does email search differ from Google search in terms of architecture and scale?
**Answer:**
Google search indexes the entire internet, optimizes for relevance, and can tolerate indexing delays, with significantly more reads than writes. Email search covers a single user's mailbox, requires near real-time incremental reindexing on send/receive/delete (higher write ratio), sorts by attributes (date, unread, attachments), and demands absolute accuracy.

#### 17. How does event sourcing compare to traditional state persistence in systems like a stock exchange?
**Answer:**
Traditional databases persist only the current state, losing the historical sequence of actions. Event sourcing stores an immutable, append-only log of all state-changing events as the single source of truth, enabling complete auditability and state recovery by replaying events in sequence.

#### 18. How is the database schema and architecture designed for a proximity or location-based service (LBS)?
**Answer:**
A proximity service relies on a Business Table (keyed by business_id) and a Geo Index Table for spatial indexing. The database cluster utilizes a primary-secondary setup where writes go to the primary and reads scale via replicas. For high-throughput user location updates (e.g., 1M/sec), a NoSQL/column-oriented key-value store like Cassandra is used, prioritizing Availability and Partition Tolerance (AP system under CAP). Keys are structured as (user_id, timestamp) combinations with lat/lng values, enabling rapid range-query lookups for a user's trajectory.

#### 19. Walk through the end-to-end workflow of a web crawler.
**Answer:**
Step 1: Seed URLs are added to the URL Frontier. Step 2: HTML Downloader fetches URLs from the Frontier. Step 3: Resolves IPs via DNS and downloads pages. Step 4: Content Parser validates HTML. Step 5-6: 'Content Seen?' checks storage to discard duplicate contents. Step 7-11: Link Extractor pulls links, passes them to filters and 'URL Seen?' component, finally pushing unseen URLs back to the URL Frontier.

#### 20. What advanced features and edge cases should be considered when designing a chat service?
**Answer:**
Important considerations include: 1) Supporting rich media files (compression, cloud storage, thumbnails). 2) Implementing end-to-end encryption for message privacy. 3) Client-side message caching to reduce server transfer overhead. 4) Geographically distributed caching (e.g., Slack's architecture) to improve load times. 5) Service discovery (e.g., Zookeeper) for handling chat server failures and reconnecting persistent connections. 6) Message resend mechanisms using retries and queues.

#### 21. What architectural model can be used to support different video processing pipelines with high parallelism?
**Answer:**
A Directed Acyclic Graph (DAG) programming model, which defines tasks in stages so they can be executed sequentially or in parallel.

#### 22. What are common types of problematic content encountered by web crawlers and how are they handled?
**Answer:**
1) Redundant content: ~30% of web pages are duplicates; handled via URL/content hashes or checksums. 2) Spider traps: Infinite loops caused by patterns like deep recursive directory structures (e.g., /foo/bar/foo/bar/); mitigated by enforcing maximum URL length limits and custom filters. 3) Data noise: Low-value content like ads or boilerplate code that should be filtered out during parsing.

#### 23. What are hierarchical routing tiles?
**Answer:**
Hierarchical routing tiles segment road networks across multiple zoom levels of detail (e.g., local streets, arterial roads, and major highways) to limit memory consumption and speed up cross-country pathfinding algorithms.

#### 24. What are the architectural trade-offs between hardcoding client-side geohashing vs. introducing a map tile service for fetching CDN map tiles?
**Answer:**
- **Client-side geohashing**: Highly efficient as clients compute latitude/longitude and zoom levels into geohash URLs (e.g., `https://cdn.map-provider.com/tiles/9q9hvu.png`) directly. However, the geohashing algorithm becomes hardcoded across mobile/web clients, making future encoding changes extremely difficult and risky.
- **Map tile service intermediary**: A service receives the client's location and zoom level, determines the target and surrounding 8 tiles, and returns 9 URLs. This adds operational flexibility and allows backend changes to encoding logic without redeploying mobile apps, at the cost of an extra network hop.

#### 25. What are the architectural trade-offs of uploading files directly to cloud storage versus via block servers in a cloud drive system?
**Answer:**
Uploading directly to cloud storage makes uploads faster since data is transferred only once. However, drawbacks include: 1) Chunking, compression, and encryption logic must be redundantly implemented across multiple client platforms (iOS, Android, Web), increasing engineering effort and error rates. 2) Client-side encryption logic is less secure as clients can be hacked or manipulated. Centralized block servers mitigate these issues.

#### 26. What are the core APIs required for a Stock Exchange System?
**Answer:**
1. Order Placement (POST /v1/order): Accepts parameters like symbol, side, price, orderType, and quantity, returning order status, IDs, and quantities.
2. Execution Query (GET /execution): Queries execution details by symbol, orderId, and time range.
3. Order Book (GET /marketdata/orderBook/L2): Queries L2 order book depth for bids and asks.
4. Historical Prices (GET /marketdata/candles): Queries candlestick chart data with open, close, high, and low prices for given resolutions and time ranges.

#### 27. What are the core components of a high-level Google Maps architecture?
**Answer:**
The high-level architecture is partitioned into three core pillars: 1. Location Service (ingests and tracks real-time user/driver positions), 2. Navigation Service (computes routes, turns, and ETAs using graph databases and routing algorithms), and 3. Map Rendering (serves vector map tiles and style sheets to clients via CDN).

#### 28. What are the core steps required in the framework for designing a proximity service (Location-Based Service)?
**Answer:**
1. Understand the problem and establish design scope (e.g., QPS, supported radius, read/write ratio). 
2. Propose a high-level design and get buy-in (choose data storage, indexing mechanism like Geohash or Quadtrees). 
3. Design deep dives (handling scale, load balancing, caching hot spots, handling spatial indexes). 
4. Wrap up (monitoring, scaling, failure handling).

#### 29. What are the functional and non-functional requirements for Google Maps?
**Answer:**
Functional: User location updates, navigation service (including ETA), and map rendering optimized primarily for mobile devices.
Non-functional: High accuracy (correct directions), smooth client-side map rendering, minimized data/battery consumption, and general high availability and scalability.

#### 30. What are the functional and non-functional requirements of a payment system?
**Answer:**
Functional requirements: Pay-in flow (receiving money from customers on behalf of sellers) and pay-out flow (sending money globally to sellers). Non-functional requirements: High reliability and fault tolerance with careful failure handling, alongside an asynchronous reconciliation process between internal systems (payments, accounting) and external PSPs to ensure data consistency.

#### 31. What are the trade-offs between building versus buying an alerting system?
**Answer:**
Industrial-scale alerting systems are widely available off-the-shelf, offering native integration with popular time-series databases and notification channels like email and PagerDuty. Building a custom system is rarely justifiable in practice, and architects must defend such decisions rigorously in senior-level interviews.

#### 32. What are the typical stateful services and components in a payment system architecture?
**Answer:**
Payment Service: stores payment-related data like nonces, tokens, payment orders, and execution status. Ledger: records all double-entry accounting data. Wallet: maintains merchant account balances. PSP (Payment Service Provider): maintains external payment execution status. Data is typically replicated across database replicas to ensure durability and reliability.

#### 33. What is a high-level design for a 'nearby friends' feature?
**Answer:**
A nearby friends system typically utilizes geospatial indexing. Clients periodically send their GPS coordinates via WebSocket or HTTP polling. Location updates are ingested by a location service and stored in an in-memory geospatial store (e.g., Redis Geohash or Quadtree/S2 geometry). A fan-out service matches user coordinates with geofenced friend lists to push updates to active connections.

#### 34. What is an ETA service and what are its core challenges in routing systems?
**Answer:**
An ETA service uses machine learning models trained on real-time traffic and historical data to predict travel time estimates for candidate routes. A primary challenge is not only processing real-time traffic data but accurately predicting future traffic states 10 to 20 minutes ahead.

#### 35. What is an optimized design for a navigation/routing service?
**Answer:**
An optimized navigation service models maps as weighted graphs (nodes as intersections, edges as road segments with weights like distance/time). It uses hierarchical routing algorithms (like Contraction Hierarchies or A* search with landmarks) to pre-compute shortcuts, drastically reducing pathfinding query latency compared to raw Dijkstra's algorithm.

#### 36. What is payment reconciliation in distributed financial systems?
**Answer:**
Reconciliation is an asynchronous verification process used as a final line of defense to ensure internal consistency and agreement between external payment service providers (PSPs/banks) and internal ledgers. It typically parses nightly settlement files containing balances and transactions, cross-referencing them against internal records to detect and flag discrepancies.

#### 37. What is the critical path in a stock exchange system?
**Answer:**
The trading flow is on the critical path, whereas the market data flow and reporting flow are not, as they have different and more relaxed latency requirements.

#### 38. What is the high-level design of a web crawler?
**Answer:**
A web crawler consists of a URL frontier (managing prioritization and politeness queues), HTML fetchers (DNS resolution and HTTP requests), a content parser (extracting links and text), a duplicate/visited URL filter (using Bloom filters or hash tables), and a persistent storage layer to save crawled documents.

#### 39. What is the workflow and design of a proximity service (e.g., finding nearby restaurants)?
**Answer:**
1. Client sends user coordinates and radius to the load balancer, which forwards to the Location-Based Service (LBS).
2. LBS maps radius to a geohash length and computes neighboring geohashes to form a list.
3. LBS queries a Redis cluster in parallel for business IDs corresponding to each geohash.
4. LBS fetches fully hydrated business info, calculates precise distances, ranks the results, and returns them to the client.

#### 40. What key architectural points should be discussed when scaling a video streaming service?
**Answer:**
Key points include: 1) Scaling the API tier horizontally since API servers are stateless. 2) Scaling databases via replication and sharding. 3) Supporting live streaming (handling higher latency requirements, real-time chunking, and strict error handling). 4) Managing video takedowns for copyright or illegal content via automated checks or user flagging.

#### 41. What operational and financial factors must be accounted for when designing a global payment processing system?
**Answer:**
Key factors include: 1) Comprehensive monitoring and alerting dashboards for key metrics (acceptance rates, CPU usage, PSP logs). 2) Debugging tools for engineers and support staff to review transaction states and history. 3) Multi-currency exchange handling for international users. 4) Regional payment method variations (e.g., localized methods or cash payments common in specific geographies like India and Brazil) and digital wallet integrations (Apple/Google Pay).

#### 42. Which spatial indexing technologies are commonly used by major mapping and geospatial platforms?
**Answer:**
Geohash is used by Bing Maps, Redis, MongoDB, and Lyft. Quadtree is used by Yext. Both Geohash and Quadtree are used by Elasticsearch. S2 Geometry is utilized by Google Maps and Tinder.


## 📂 Category: System Design & Algorithms (1 cards)

### 🟡 Mid Level

#### 1. Compare rate limiting algorithms: Token Bucket, Leaking Bucket, Fixed Window Counter, Sliding Window Log, and Sliding Window Counter.
**Answer:**
- Token Bucket: Pros: Simple, memory-efficient, allows short traffic bursts. Cons: Challenging to tune bucket size and refill rate properly.
- Leaking Bucket: Pros: Memory-efficient (fixed queue size), steady outflow rate. Cons: Traffic bursts fill the queue with old requests, causing recent ones to be dropped; hard to tune parameters.
- Fixed Window Counter: Pros: Memory-efficient, easy to understand. Cons: Traffic spikes at window edges can exceed allowed limits.
- Sliding Window Log: Pros: Highly accurate with rolling windows. Cons: High memory consumption because timestamps of rejected requests are stored.
- Sliding Window Counter: Pros: Smooths out traffic spikes using averages of previous windows, memory-efficient. Cons: Approximation based on previous window distribution (though error rates are extremely low in practice).


## 📂 Category: System Design & Architecture (9 cards)

### 🟢 Junior Level

#### 1. What is a Payment Service Provider (PSP)?
**Answer:**
A Payment Service Provider is a third-party service that handles financial transactions, securely moving funds between accounts (such as transferring money out of a buyer's credit card account to a merchant account).

#### 2. What is a proximity service and what are its core use cases?
**Answer:**
A proximity service is used to discover nearby geographical points of interest (such as restaurants, hotels, gas stations) and powers features like finding k-nearest locations on maps or local business directories.


### 🟡 Mid Level

#### 1. How do you handle orphaned temporary chunks or parts in large file upload systems?
**Answer:**
Old or leftover parts are no longer useful after the final object has been reassembled. To prevent storage leaks, introduce a garbage collection service responsible for periodically scanning and freeing up space from multipart upload chunks that are no longer needed.

#### 2. In a high-load system architecture (like a hotel booking site), when stateless services scale horizontally easily, what typically acts as the primary system bottleneck?
**Answer:**
The relational or transactional database, because it holds state and cannot be scaled horizontally as easily as stateless application servers due to ACID constraints, consensus protocols, and data consistency requirements.


### 🔴 Senior Level

#### 1. Compare Elasticsearch versus a custom search solution (e.g., for email search).
**Answer:**
Elasticsearch: Easy to integrate with lower initial development effort, but introduces system complexity (maintaining dual systems), data consistency challenges across datastores, and potential infrastructure scaling hurdles at massive scale. Custom Search Engine: Engineered specifically for the domain, single-system simplicity, and easier long-term scaling, but demands significant upfront engineering effort.

#### 2. What architectural components should be added to a robust notification system?
**Answer:**
Key components include: 1) Notification servers equipped with authentication and rate-limiting. 2) A retry mechanism using a message queue to re-enqueue and retry failed notifications for a predefined number of times. 3) Notification templates for consistent and efficient message creation. 4) Monitoring and tracking systems for health checks and analytics.

#### 3. What are the architectural implications of using memory-mapped files (mmap) for event sourcing in low-latency stock exchange systems?
**Answer:**
Order managers become reusable libraries embedded directly into multiple components rather than centralized services, reducing critical-path network hops and latency. While components maintain their own states, event sourcing guarantees identical, replayable states across components, and dedicated sequencers may be eliminated.

#### 4. What are the data access patterns and scaling strategies for a large-scale chat system?
**Answer:**
Chat systems handle two primary data types: generic data (user profiles, settings, friend lists) stored in robust relational databases using sharding/replication, and chat history data. Chat history features massive write volumes (e.g., billions of messages), high access frequency for recent chats, and random access requirements (search, mentions). The read-to-write ratio is roughly 1:1 for 1-on-1 chats.

#### 5. Why is over-engineering considered a red flag in a system design interview?
**Answer:**
Over-engineering introduces unnecessary complexity, operational overhead, and failure points without addressing immediate scale or product requirements, demonstrating a lack of focus on pragmatic trade-offs.


## 📂 Category: System Design & Storage (1 cards)

### 🔴 Senior Level

#### 1. Walk through the architectural steps of creating a bucket and uploading an object to an S3-like object storage service.
**Answer:**
Bucket Creation: Client sends HTTP PUT to API service -> IAM authorizes WRITE permissions -> Metadata store persists bucket entry. Object Upload: Client sends PUT request -> API service validates user permissions -> Object data payload streamed to data store which returns a UUID -> Metadata store creates entry mapping object_id, bucket_id, and object_name.


## 📂 Category: System Design Architecture (3 cards)

### 🟡 Mid Level

#### 1. What are the high-level components of a hotel reservation system architecture?
**Answer:**
Includes Clients (User/Admin), CDN (static assets), Public API Gateway (rate limiting, auth), Internal APIs (VPN-protected staff tools), Hotel Service (static hotel/room info), Rate Service (dynamic pricing based on occupancy), Reservation Service (inventory tracking and bookings), Payment Service, and Hotel Management Service.

#### 2. What are the two main flows to consider when designing a news feed system?
**Answer:**
1. Feed publishing (writing posts to storage/fan-out to followers).
2. News feed building (reading and aggregating posts to construct the user's view, via pull/fan-out-on-read or push/fan-out-on-write models).


### 🔴 Senior Level

#### 1. How do we guarantee high availability, scalability, and disaster recovery in an email system?
**Answer:**
Most components are horizontally scalable because individual user data access patterns are independent. Data is replicated across multiple data centers for high availability. Users connect to the nearest mail server via network topology, allowing access to messages from other data centers during network partitions or outages.


## 📂 Category: System Design Basics (2 cards)

### 🟢 Junior Level

#### 1. What are three key concepts to understand for back-of-the-envelope estimation?
**Answer:**
The three key concepts are the power of two (for memory/data sizes), standard latency numbers across various storage media, and availability numbers (calculating 'nines' of uptime).


### 🟡 Mid Level

#### 1. What is the role of workers in a distributed autocomplete service?
**Answer:**
Workers are background servers that execute asynchronous jobs at regular intervals to analyze raw search query logs, build optimized trie data structures, and persist them to the Trie DB.


## 📂 Category: System Design Fundamentals (22 cards)

### 🟢 Junior Level

#### 1. What are general conclusions regarding hardware and network latencies in distributed systems?
**Answer:**
Memory access is orders of magnitude faster than disk seeks; avoid disk seeks when possible. Simple compression algorithms are fast and should be used to compress data over the internet to save bandwidth. Inter-region cross-datacenter communication introduces high, bounded-by-physics latency due to geographic distance.

#### 2. What are the core building blocks of a data-intensive application?
**Answer:**
Databases (store data for later retrieval), Caches (remember results of expensive operations to speed up reads), Search indexes (allow keyword search and filtering), Stream processing (send messages asynchronously between processes), and Batch processing (periodically crunch large amounts of accumulated data).

#### 3. What are the foundational pillars for scaling a system to support millions of users?
**Answer:**
1) Keep the web tier stateless, 2) Build redundancy at every tier, 3) Cache data aggressively, 4) Support multiple data centers, 5) Host static assets in a CDN, 6) Scale the data tier via sharding, 7) Split tiers into discrete microservices, and 8) Monitor systems and utilize automation tooling.

#### 4. What are the key advantages and differences of a stateless architecture compared to stateful architecture?
**Answer:**
A stateful server remembers client data (state) from one request to the next. In contrast, a stateless server keeps no state information; clients send all necessary context with each request. Key advantages of a stateless architecture include simplicity, higher robustness, and effortless horizontal scalability.

#### 5. What are the key steps for estimating Queries Per Second (QPS)?
**Answer:**
Key steps include estimating the daily active users (DAU) and then using the DAU and average user actions per day to calculate the average and peak QPS.

#### 6. What are two common approaches for generating unique short URLs in a URL shortener?
**Answer:**
1. Hash + Collision Resolution: Generate a hash (e.g., MD5/SHA-256) of the long URL, take the first N characters, and if a collision occurs, append a predefined string or counter until unique.
2. Base 62 Conversion: Use an atomic counter (like a distributed ID generator or auto-increment DB ID) and convert the integer base-10 ID to a base-62 string ([a-zA-Z0-9]) for a compact representation.

#### 7. What core requirements must a hash function satisfy for URL shortening services?
**Answer:**
The hash function must map each long URL to exactly one unique hashValue (`longURL -> hashValue`), and each hashValue must be deterministically mapped back to its corresponding long URL (`hashValue -> longURL`).

#### 8. What differentiates data-intensive applications from compute-intensive applications?
**Answer:**
Data-intensive applications are rarely limited by raw CPU power. Instead, their primary bottlenecks and challenges involve the volume of data, the complexity of data structures, and the high velocity at which the data is changing.

#### 9. What is Base 62 conversion and why is it used in URL shorteners?
**Answer:**
Base conversion helps to convert numbers between different representation systems. Base 62 conversion uses characters [a-zA-Z0-9] (62 possible characters) to represent large numeric IDs compactly as short alphanumeric strings for URL shorteners.

#### 10. What is a Service Level Agreement (SLA)?
**Answer:**
A formal agreement between a service provider and a customer that defines the expected level of uptime, performance, and reliability the service will deliver.

#### 11. What is a straightforward solution to shortening a URL, and what are its limitations?
**Answer:**
A straightforward approach is to use standard cryptographic hash functions like CRC32, MD5, or SHA-1. However, these produce strings too long for a short URL, requiring truncation which introduces potential hash collision risks.

#### 12. What is back-of-the-envelope estimation?
**Answer:**
Back-of-the-envelope estimation is a rapid calculation technique using mental models, thought experiments, and standard hardware/network performance numbers to approximate system capacity, bandwidth, and performance bottlenecks.

#### 13. What is the initial critical step when designing a chat application?
**Answer:**
Nailing down exact functional requirements with the interviewer (e.g., distinguishing between one-on-one chat vs. group chat, media sharing, presence detection, etc.) to avoid designing for the wrong core use case.

#### 14. What is the main purpose of back-of-the-envelope calculations?
**Answer:**
To quickly estimate system capacity, storage requirements, network bandwidth, and performance bottlenecks during early-stage system design.

#### 15. What is the main purpose of data serialization in system design?
**Answer:**
Data serialization converts structured in-memory data objects into a standardized format (such as JSON, Protocol Buffers, or Avro) that can be stored persistently or transmitted efficiently over a network, allowing the data to be reliably reconstructed later.

#### 16. What is the primary goal of a system design interview?
**Answer:**
To assess a candidate's problem-solving, architectural trade-off evaluation, and design skills.

#### 17. What is the purpose of A/B testing in software systems?
**Answer:**
A/B testing is a methodology used to test different system features, UI changes, or algorithmic variations on a subset of users to evaluate performance or business metrics empirically.

#### 18. What is the purpose of conducting back-of-the-envelope calculations during system design?
**Answer:**
Back-of-the-envelope calculations are rapid estimations used to evaluate if a proposed architecture can meet scale, throughput, storage, and latency constraints before committing to a detailed design.

#### 19. Why should you avoid building every component from scratch in system design (e.g., video streaming or blob storage)?
**Answer:**
System design prioritizes choosing the right managed technologies within limited timeframes over detailing how every component works. Building scalable systems like distributed blob storage or global CDNs is extremely complex and costly; even tech giants like Netflix and Facebook leverage third-party cloud services and CDNs.


### 🟡 Mid Level

#### 1. How do web crawlers handle duplicate content using hash values?
**Answer:**
Since a significant portion of web pages contain duplicate content, crawlers use a 'Content Seen?' data structure to eliminate redundancy and save processing time. Instead of comparing massive HTML documents character-by-character, the crawler compares the hash values of the web pages to quickly detect previously stored content.

#### 2. How do you optimize the upload of very large files (gigabytes) to cloud object storage like S3?
**Answer:**
Directly uploading massive files is prone to network timeout failures, requiring a restart from scratch. Instead, use 'multipart upload': slice the large file into smaller independent chunks, upload them concurrently, and have the object store reassemble the parts upon successful completion of all chunks.

#### 3. What is the underlying data foundation shared by scalable data gathering services despite differing use cases?
**Answer:**
While real-time features (like Twitter trends or autocomplete) have different freshness requirements than static datasets (like daily keyword suggestions), their underlying data foundation remains identical: the data used to build analytical structures (like tries) is consistently sourced from unified analytics or logging services.


## 📂 Category: System Design Interview (3 cards)

### 🟢 Junior Level

#### 1. Is the final system architecture diagram the most critical evaluation factor in a system design interview?
**Answer:**
No, the design process, trade-off analysis, communication, and clarification steps are more important than the final static design.

#### 2. What is the primary focus during a back-of-the-envelope estimation in a system design interview?
**Answer:**
It is more important to focus on the process, assumptions, and logical approximations rather than obtaining hyper-exact results.

#### 3. What is the risk of answering a system design question too quickly without clarifying requirements?
**Answer:**
It can be a major red flag during an interview and may lead to designing the wrong system that fails to meet scale, consistency, or functional constraints.


## 📂 Category: System Design Methodology (10 cards)

### 🟢 Junior Level

#### 1. How should you handle requests for assumptions during a system design interview?
**Answer:**
You should explicitly write down and communicate your assumptions regarding scale, read/write ratios, data retention, and constraints.

#### 2. Should you jump straight into a solution during a system design interview?
**Answer:**
No. You should slow down, clarify functional and non-functional requirements, and establish constraints before proposing a solution.

#### 3. What are the primary considerations during the system design deep dive step?
**Answer:**
The primary focus is to prioritize core system components, handle bottlenecks, scale specific sub-systems, and manage interview or design time effectively.

#### 4. What are the primary scoping questions to ask in step one of a system design interview?
**Answer:**
Example questions include: "What specific features are we going to build?", "How many users does the product have?", and "What is the company’s technology stack?"

#### 5. What is the fourth step in the four-step framework for system design interviews?
**Answer:**
The fourth step is to wrap up

#### 6. What is the recommended time allocation breakdown for a 45-minute System Design interview?
**Answer:**
1. Understanding the problem and establishing design scope: 3-10 minutes
2. Proposing high-level design and getting buy-in: 10-15 minutes
3. Design deep dive: 10-25 minutes
4. Wrapping up and summarizing: 3-5 minutes

#### 7. What is the second step in the four-step framework for system design interviews?
**Answer:**
Propose a high-level design and get buy-in.

#### 8. What key skills do interviewers evaluate during a system design interview?
**Answer:**
Collaboration, working under pressure, resolving ambiguity, and core technical design skills.


### 🟡 Mid Level

#### 1. What are the core activities during the high-level design step in a system design interview?
**Answer:**
You should draw box diagrams of key components, outline data flows, select core technologies, and perform back-of-the-envelope calculations.

#### 2. What should you do during the wrap-up step of a system design interview?
**Answer:**
You should identify system bottlenecks, discuss potential improvements (such as scaling, caching, or fault tolerance), and recap your design.


## 📂 Category: System Design Patterns (5 cards)

### 🟢 Junior Level

#### 1. What are the common formats of a notification system?
**Answer:**
A notification system alerts users with important information (breaking news, updates, events). Beyond mobile push notifications, the three primary notification formats are mobile push notifications, SMS messages, and Emails.

#### 2. What are the limitations of the pull model for polling execution status?
**Answer:**
The pull model is not real-time and may overload the target service if the polling frequency is set too high.

#### 3. What is a leaderboard?
**Answer:**
Leaderboards are common in gaming and elsewhere to show who is leading a particular tournament or competition. Users are assigned points for completing tasks or challenges, and whoever has the most points is at the top of the leaderboard. The leaderboard shows the ranking of the leading competitors and also displays the position of the user on it.

#### 4. What is a news feed?
**Answer:**
A news feed is a constantly updating list of stories in the middle of a home page, including status updates, photos, videos, links, app activity, and likes from people, pages, and groups that a user follows.


### 🔴 Senior Level

#### 1. What is the architecture and workflow of a social media fanout service?
**Answer:**
The fanout service fetches friend IDs from a graph database, retrieves user settings (e.g., mutes/privacy) from cache, pushes the post ID to a message queue, and fanout workers process the queue to store post IDs in users' news feed caches (storing only IDs to minimize memory usage).


## 📂 Category: System Design Principles (1 cards)

### 🔴 Senior Level

#### 1. Which Domain-Driven Design (DDD) philosophy systematically answers questions regarding account balance accuracy, auditability, and historical correctness?
**Answer:**
Event Sourcing. It is a design technique where state changes are stored as a sequence of immutable events, allowing complete audit trails and historical state reconstruction.


## 📂 Category: System Design Requirements (1 cards)

### 🟡 Mid Level

#### 1. What core questions should be asked during a video-sharing platform (e.g., YouTube) system design interview?
**Answer:**
Candidate should clarify: 1) Important features (upload/watch videos); 2) Client types (mobile, web, smart TV); 3) Scale (e.g., 5M DAU, 30 min daily time spent); 4) International users and languages; 5) Supported resolutions/formats; 6) Encryption requirements; 7) File size limits (e.g., max 1GB); 8) Utilization of existing cloud infrastructure (AWS/GCP/Azure) vs building from scratch.


## 📂 Category: System Design: Booking & Reservation Systems (1 cards)

### 🟢 Junior Level

#### 1. What are the core non-functional requirements for a reservation system?
**Answer:**
1. Support high concurrency: Handle massive concurrent booking attempts for popular inventory during peak seasons.
2. Moderate latency: Fast response time for user bookings is ideal, though processing times of a few seconds are acceptable.


## 📂 Category: System Design: Data Streaming & Aggregation (1 cards)

### 🟡 Mid Level

#### 1. What are the non-functional requirements for an ad click event aggregator?
**Answer:**
1. Correctness: Data must be accurate since it drives real-time bidding (RTB) and ad billing.
2. Resilience: Must properly handle delayed, out-of-order, or duplicate events.
3. Robustness: Resilient to partial infrastructure failures.
4. Latency: End-to-end processing latency should be at most a few minutes.


## 📂 Category: System Design: Distributed Storage (1 cards)

### 🟡 Mid Level

#### 1. What are the key non-functional requirements for a cloud storage system like Google Drive or Object Storage?
**Answer:**
1. Reliability & Durability: Data loss is unacceptable (e.g., target 6 nines durability).
2. Availability: High service availability (e.g., 4 nines) ensuring access despite partial outages.
3. Sync Speed & Performance: Fast synchronization and file transfers to maintain user retention.
4. Bandwidth & Storage Efficiency: Minimize unnecessary network bandwidth and optimize storage costs while scaling to massive volumes (e.g., 100+ PB).


## 📂 Category: System Design: Geospatial Systems (5 cards)

### 🟢 Junior Level

#### 1. What are the common algorithmic options for fetching nearby businesses in location-based services?
**Answer:**
1. Two-dimensional search
2. Evenly divided grid
3. Geohash
4. Quadtree
5. Google S2 geometry library


### 🟡 Mid Level

#### 1. How is a Quadtree data structure constructed recursively for spatial indexing?
**Answer:**
The root node represents the entire map boundary and is recursively subdivided into 4 quadrants as long as a node contains more than a threshold number of entities (e.g., >100 businesses). 

Pseudocode reference:
public void buildQuadtree(TreeNode node) {
    if (countNumberOfBusinessesInCurrentGrid(node) > 100) {
        node.subdivide();
        for (TreeNode child : node.getChildren()) {
            buildQuadtree(child);
        }
    }
}

#### 2. What are the architectural trade-offs between dynamic map tile rendering and pre-generated static map tiles?
**Answer:**
Option 1 (Dynamic Rendering): Generates tiles on the fly based on client location and zoom level. Disadvantages include massive server compute load and the inability to effectively utilize caching due to infinite parameter combinations.
Option 2 (Static Pre-generated Tiles): Serves pre-rendered tiles mapped to fixed rectangular grids via subdivision schemes (e.g., Geohashes) per zoom level, enabling highly efficient caching and serving.

#### 3. What strategies can be used when a spatial search returns an insufficient number of nearby businesses?
**Answer:**
Option 1: Only return businesses within the exact initial radius (simple, but often results in poor user satisfaction due to lack of results).
Option 2: Dynamically expand the search radius by stripping the last digit of the geohash (or expanding grid boundaries) and iteratively fetching until the target result count is met.


### 🔴 Senior Level

#### 1. What are the operational considerations and deployment strategies when building and updating large-scale spatial data structures like Quadtrees?
**Answer:**
1. Server Start-up Time: Building a quadtree for ~200 million businesses can take minutes during startup, during which the server cannot serve traffic. Mitigate via incremental rolling deployments to prevent cluster-wide brownouts.
2. Cluster Strain: Blue/green deployments can overwhelm database services if an entire cluster simultaneously fetches 200 million records.
3. Updates & Stale Data: Incremental cluster rebuilding serves temporary stale data, which can be mitigated with nightly batch jobs (though this risks cache stampedes). On-the-fly updates require thread-safe locking mechanisms that drastically complicate implementation.


## 📂 Category: System Design: Notification Systems (1 cards)

### 🟢 Junior Level

#### 1. What are the fundamental components of a scalable notification system design?
**Answer:**
1. Multi-channel support (Push notifications, SMS, Email, etc.)
2. Contact info gathering and user preference flows
3. Notification delivery, queuing, routing, and sending/receiving execution flows


## 📂 Category: System Design: Video Streaming (2 cards)

### 🟢 Junior Level

#### 1. What are the primary components of video encoding formats?
**Answer:**
1. Container: The file wrapper (.mp4, .mov, .avi) holding interleaved video, audio, and metadata.
2. Codecs: Compression/decompression algorithms (e.g., H.264, VP9, HEVC) designed to reduce file size while preserving visual quality.

#### 2. What parallel processes are involved in uploading media files to a video streaming service?
**Answer:**
1. Media binary upload: Streaming the actual raw video file to object storage.
2. Metadata synchronization: Updating the database with metadata such as video URL, size, resolution, format, and user details.


## 📂 Category: System Estimation & Core Algorithms (1 cards)

### 🟢 Junior Level

#### 1. How do you calculate the required hash value length for a URL shortener using base 62 encoding?
**Answer:**
Base 62 uses characters [0-9, a-z, A-Z] (10 + 26 + 26 = 62 possibilities). To support N URLs (e.g., 365 billion), find the smallest n such that 62^n >= N. For 365 billion URLs, n = 7 yields ~3.5 trillion combinations, making a hash length of 7 sufficient.


## 📂 Category: System Fundamentals (1 cards)

### 🟢 Junior Level

#### 1. What is the typical request flow in a single-server web setup from user entry to response?
**Answer:**
1. User accesses the website via a domain name (e.g., api.mysite.com); DNS resolves the domain to an IP address. 2. Browser or client sends HTTP requests directly to the target web server using the obtained IP. 3. The web server processes the request and returns HTML pages or JSON responses.


## 📂 Category: System Scalability (1 cards)

### 🟢 Junior Level

#### 1. What architectural components are added immediately after load-balancing and database replication to improve response times?
**Answer:**
A caching layer to reduce database load and a Content Delivery Network (CDN) to shift static assets (JavaScript, CSS, images, and videos) closer to the users.


## 📂 Category: Time-Series Data (1 cards)

### 🔴 Senior Level

#### 1. Why are general-purpose relational or NoSQL databases discouraged for time-series monitoring and alerting systems?
**Answer:**
1. Relational Databases: Lack optimizations for rolling time-window aggregations (requiring complex, unreadable SQL), perform poorly under constant heavy write loads, and require excessive indexing overhead for arbitrary tagging/labeling.
2. NoSQL Databases (Cassandra/Bigtable): Technically capable, but demand deep internal systems knowledge to engineer custom, scalable schemas for time-series range queries, making dedicated time-series databases (TSDBs) the superior choice.


## 📂 Category: Trading Systems (3 cards)

### 🔴 Senior Level

#### 1. How does the market data flow function in a financial exchange system?
**Answer:**
The market data publisher (MDP) receives executions (fills) from the matching engine and builds order books and candlestick charts from the stream. This collective market data is sent to the data service to make it available to subscribers.

#### 2. What are the core requirements and design patterns for an exchange system's order manager?
**Answer:**
The order manager must be fast, efficient, and accurate while maintaining current states for orders. State transition complexity is a major challenge, often involving tens of thousands of cases in a real exchange system. Event sourcing is the ideal architectural pattern for designing an order manager.

#### 3. What is the exact critical path order of the trading flow in an exchange?
**Answer:**
1. Client places an order via broker web/mobile app.
2. Broker sends order to the exchange.
3. Order enters via client gateway (performs input validation, rate limiting, auth, normalization) and forwards to order manager.
4-5. Order manager performs risk checks based on rules set by the risk manager.
6. Order manager verifies sufficient funds in the wallet.
7-9. Order is sent to the matching engine. When matched, the engine emits two executions (fills) for buy/sell sides, sequenced via a sequencer for deterministic replay.
10-14. Executions are returned to the client.


## 📂 Category: Transactions & Consistency (1 cards)

### 🟡 Mid Level

#### 1. How do we implement idempotency in the database of a payment system?
**Answer:**
Use the database's unique key constraint where the primary key of the table serves as the idempotency key. A successful insertion means the request has not been seen before. If the insertion fails due to a primary key collision, the request is recognized as a duplicate and is not processed further.


## 📂 Category: Transactions & Payments (2 cards)

### 🟡 Mid Level

#### 1. How is payment state managed during transaction processing failures?
**Answer:**
A definitive payment state is maintained and persisted in an append-only database table at every stage of the payment cycle, allowing the system to inspect failures and decide whether a retry or refund is required.


### 🔴 Senior Level

#### 1. How is the payment status updated across services in a payment execution lifecycle?
**Answer:**
Payment order status transitions through NOT_STARTED, EXECUTING, SUCCESS, or FAILED. Upon SUCCESS, the wallet and ledger services are updated sequentially (updating wallet_updated and ledger_updated flags). A scheduled job monitors in-flight orders and alerts on stalled transactions.


## 📂 Category: Video Streaming (1 cards)

### 🟢 Junior Level

#### 1. What is the high-level design of a video streaming service utilizing CDNs?
**Answer:**
Videos are stored and delivered directly via Content Delivery Networks (CDNs) using edge servers located closest to the end-users to minimize latency. API servers handle all auxiliary operations outside of actual video streaming, including feed recommendations, generating pre-signed video upload URLs, updating metadata databases, caching, and user management (signup/auth).


## 📂 Category: Video Streaming & CDN (3 cards)

### 🟢 Junior Level

#### 1. Explain the step-by-step workflow of a Content Delivery Network (CDN).
**Answer:**
1. User requests a resource via a CDN domain URL.
2. If the CDN cache lacks the file, it requests it from the origin server (web server or S3).
3. The origin returns the file along with an HTTP Time-to-Live (TTL) header.
4. The CDN caches the asset and returns it to the user.
5. Subsequent requests from other users are served directly from the CDN cache until the TTL expires.


### 🟡 Mid Level

#### 1. How can video upload speed be optimized using chunking and global distribution?
**Answer:**
1. Client-side splitting: Split videos into smaller chunks via GOP (Group of Pictures) alignment to allow fast resumable uploads on failure and improve speed.
2. Upload Centers: Set up multiple global upload centers (leveraging CDNs like CloudFront or Akamai) close to users to reduce latency (e.g., US users upload to North America centers, Asian users to Asian centers).


### 🔴 Senior Level

#### 1. How do you achieve high parallelism in a video processing and transfer pipeline?
**Answer:**
To eliminate tight sequential dependencies where each output depends strictly on the previous step, introduce decoupled message queues between processing stages, enabling asynchronous and highly parallelized data flows from original storage to the CDN.


## 📂 Category: Web Architecture (4 cards)

### 🟢 Junior Level

#### 1. What is the detailed architectural flow of URL redirection in a URL shortener?
**Answer:**
1. User clicks a short URL (e.g., https://tinyurl.com/zn9edcu). 2. Load balancer forwards the request to web servers. 3. Check the cache for the short URL; if present, return the long URL immediately. 4. If absent in cache, query the database. If not found in the database, return an invalid URL error. 5. Return the long URL to the client.

#### 2. What is the division of responsibilities between client-side and server-side languages in web applications?
**Answer:**
Client-side languages are primarily used for UI presentation and rendering, whereas server-side languages handle core business logic, validation, and data storage interactions.

#### 3. What is the role of the web server in the request-response flow?
**Answer:**
The web server receives HTTP/HTTPS requests from clients, routes them to appropriate business logic handlers, and returns rendered HTML pages or JSON responses.


### 🟡 Mid Level

#### 1. What is the difference between a 301 redirect and a 302 redirect?
**Answer:**
A 301 redirect indicates a 'permanently' moved URL; the browser caches the response, and subsequent requests bypass the redirection service and go directly to the target URL. A 302 redirect indicates a 'temporarily' moved URL; subsequent requests still go to the redirection service first. 301 reduces server load, whereas 302 is better for tracking click rates and analytics.


## 📂 Category: Web Architecture & High Availability (1 cards)

### 🟢 Junior Level

#### 1. What resilience and fallback considerations must be accounted for when using a Content Delivery Network (CDN)?
**Answer:**
Applications must implement CDN failure detection mechanisms so that if a temporary CDN outage occurs, clients can automatically fallback to fetch assets directly from the origin server.


## 📂 Category: Web Crawlers (1 cards)

### 🟢 Junior Level

#### 1. What is a mapping table in a web crawler?
**Answer:**
A mapping table maps each host to a specific queue to ensure politeness and proper domain-based request throttling.


## 📂 Category: Web Crawling (10 cards)

### 🟢 Junior Level

#### 1. How is content storage structured in a web crawler?
**Answer:**
Web crawlers store HTML content using a hybrid disk and memory storage system. Most content resides on disk because datasets exceed memory capacity, while popular or frequently accessed content is kept in memory to reduce latency.

#### 2. What are the primary use cases of a web crawler?
**Answer:**
1. Search engine indexing (collecting web pages to create a local index, e.g., Googlebot). 2. Web archiving (preserving data for future uses, e.g., US Library of Congress). 3. Web mining (discovering useful knowledge and data trends from the internet). 4. Web monitoring (monitoring copyright and trademark infringements).

#### 3. What is a URL Extractor in web crawling systems?
**Answer:**
A URL Extractor parses and extracts links from HTML pages. It converts relative paths to absolute URLs by prefixing them with the base domain (e.g., 'https://en.wikipedia.org').

#### 4. What is a URL Frontier?
**Answer:**
The URL Frontier is the component in modern web crawlers that stores URLs to be downloaded, splitting the crawl state into 'to be downloaded' and 'already downloaded'. It typically functions as a First-in-First-out (FIFO) queue.

#### 5. What is robots.txt (Robots Exclusion Protocol)?
**Answer:**
A standard used by websites to communicate with web crawlers, specifying which pages crawlers are allowed to download. Crawlers check and cache this file periodically to adhere to the site's scraping rules.

#### 6. What is the role of a worker thread in a web crawler?
**Answer:**
A worker thread downloads web pages one by one from the same host. A configurable delay can be added between two download tasks to respect politeness constraints.

#### 7. What is the role of the URL Filter in a web crawler?
**Answer:**
The URL filter explicitly excludes certain content types, unwanted file extensions, broken/error links, and URLs matching blacklisted domains.


### 🟡 Mid Level

#### 1. How is extensibility achieved in a web crawler architecture?
**Answer:**
Extensibility is designed into the system by using modular plugin architectures. New content types or monitoring capabilities can be added by plugging in specialized modules (e.g., a PNG Downloader module or a Web Monitor module for copyright tracking).

#### 2. What is the role of the URL frontier in a web crawler?
**Answer:**
A URL frontier is a specialized data structure that stores unvisited URLs to be downloaded, serving as a critical component to enforce politeness policies, URL prioritization, and content freshness.

#### 3. What strategies are used to select seed URLs for a web crawler?
**Answer:**
Seed URLs serve as starting points for a web crawler to traverse as many links as possible. Strategies include dividing the URL space based on locality (popular websites per country) or topics (shopping, sports, healthcare, etc.). Seed URL selection is an open-ended problem aimed at maximizing traversal coverage.


## 📂 Category: Web Crawling & Data Ingestion (2 cards)

### 🟡 Mid Level

#### 1. How do you enforce politeness constraints in a distributed web crawler?
**Answer:**
Politeness requires downloading one page at a time from the same host, often with enforced delays between requests. This is implemented by maintaining a mapping of website hostnames to specific downloader worker threads. Each downloader thread maintains its own separate FIFO queue and exclusively processes URLs assigned to that specific queue.


### 🔴 Senior Level

#### 1. What architectural patterns and strategies are essential for implementing a scalable web crawler?
**Answer:**
1) Server-side rendering (dynamic rendering) to parse scripts like JavaScript/AJAX and discover dynamically generated links; 2) Anti-spam components to filter out low-quality/spam pages and optimize finite crawl resources; 3) Database replication and sharding for data layer availability and scalability; 4) Horizontal scaling with stateless download workers; 5) Built-in analytics pipelines for fine-tuning based on crawled data.


## 📂 Category: Web Crawling & Scrapers (2 cards)

### 🟢 Junior Level

#### 1. How does setting a short timeout optimize a web crawler?
**Answer:**
To avoid long wait times caused by slow or non-responsive web servers, a maximal wait time is specified. If a host fails to respond within this predefined window, the crawler abandons the job and moves on to other pages.


### 🔴 Senior Level

#### 1. How is storage for a URL frontier implemented in large-scale web crawlers?
**Answer:**
A hybrid approach is used: the majority of URLs are stored on disk for scalability and durability, while in-memory buffers are maintained for enqueue and dequeue operations to minimize disk I/O bottlenecks. Buffered data is periodically flushed to disk.


## 📂 Category: Web Crawling & Search (1 cards)

### 🟡 Mid Level

#### 1. How do we optimize freshness in a web crawler without repeatedly downloading all pages?
**Answer:**
To keep data fresh without heavy resource consumption from full recrawls, use strategies such as: 1) Recrawling based on individual web pages' update histories, and 2) Prioritizing URLs to recrawl important pages first and more frequently.


## 📂 Category: Web Scale Architecture (1 cards)

### 🟡 Mid Level

#### 1. How can we optimize traversal and crawling prioritization in a web crawler?
**Answer:**
Standard BFS treats all URLs equally. To optimize, incorporate a priority queue that factors in page ranks, web traffic, update frequency, and document quality to determine crawl order.


## 📂 Category: Web Scraping (2 cards)

### 🟢 Junior Level

#### 1. What is a web crawler (spider/robot) and how does it operate?
**Answer:**
A web crawler is widely used by search engines to discover new or updated content (web pages, images, videos, PDFs). It starts by collecting a seed set of web pages and then recursively follows hyperlinks on those pages to discover and collect new content.

#### 2. When is a web crawler considered to be 'impolite'?
**Answer:**
When it sends too many requests to the same hosting server within a short period, risking overwhelming web servers or triggering a denial-of-service (DoS) attack.


## 📂 Category: Web Scraping & Crawling (1 cards)

### 🟡 Mid Level

#### 1. What are the key characteristics and requirements of a well-designed web crawler?
**Answer:**
Scalability (handling billions of web pages efficiently via parallelization), Robustness (handling traps, bad HTML, and unresponsive servers), Politeness (avoiding overwhelming target websites with too many rapid requests), and Extensibility (flexibility to support new content types like images without system redesign).

