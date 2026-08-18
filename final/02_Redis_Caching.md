# 02_Redis_Caching - Redis & In-Memory Caching Study Guide

- **Total Pure Cards**: 112

---

## 📂 Category: IN-MEMORY STORAGE & REDIS & CACHING

### Junior Level (16 cards)

#### 1. Can you elaborate on the 6 core underlying data structures of Redis?
**Answer:**
1. Simple Dynamic String (SDS): A wrapper around C-style strings. It records length information (reducing length retrieval time complexity from O(N) to O(1)), prevents buffer overflows, and minimizes memory re-allocations when modifying strings.
2. Doubly Linked List (linkedlist): A doubly linked circular list with head and tail pointers, used to implement features like Pub/Sub, slow queries, and monitors.
3. Dictionary (dict): Implemented via hash tables, internally containing two hash tables (for smooth rehashing), using chaining to resolve collisions. Rehashing is performed incrementally to guarantee service availability.
4. Skip List (skiplist): One of the underlying implementations of sorted sets, composed of zskiplist and zskiplistNode. Heights range randomly from 1-32, supporting average O(log N) complexity node lookups.
5. Integer Set (intset): An abstract data structure used to store integer values, implemented via an underlying array without duplicate elements.
6. Ziplist: A sequential data structure developed for memory optimization, composed of contiguous blocks of memory, capable of storing multiple nodes (including byte arrays or integer values).

#### 2. Explain Redis Cluster architecture and data sharding mechanism.
**Answer:**
Redis Cluster provides automatic sharding across multiple nodes using a 16384 hash slot space. Every key is mapped to a hash slot using the formula CRC16(key) % 16384. Nodes in the cluster manage subsets of these slots, enabling horizontal scaling and high availability via master-replica setups.

#### 3. How do you choose between Redis RDB and AOF persistence mechanisms?
**Answer:**
For maximum data safety, use both RDB and AOF simultaneously; upon restart, Redis will prioritize loading the AOF file because it typically contains a more complete dataset. If you can tolerate data loss within a span of minutes, you can rely solely on RDB. While some users rely exclusively on AOF, it is generally not recommended because periodic RDB snapshots are highly efficient for backups, allow faster data restoration, and avoid potential bugs within the AOF rewriting/replay engine. If persistence is not required, both can be disabled.

#### 4. How does Redis implement a delayed queue?
**Answer:**
You can use a sorted set (ZSET) structure to achieve delayed queues. Store timestamps as the score for ordering, and continuously produce messages into memory using the ZADD command. Then, query all pending tasks that meet the conditions using ZRANGEBYSCORE, and process them in a loop.

#### 5. How is Redis data recovered and what is the startup loading workflow?
**Answer:**
When a Redis failure occurs, data can be recovered from RDB or AOF files by copying the files to the Redis data directory and starting `redis-server`. The Redis startup data loading workflow: 1. If AOF persistence is enabled and an AOF file exists, Redis prioritizes loading the AOF file; 2. If AOF is disabled or the AOF file does not exist, Redis loads the RDB file; 3. Upon successful loading of the AOF/RDB file, Redis starts successfully; 4. If errors exist in the AOF/RDB files, Redis fails to start and logs error messages.

#### 6. How to ensure eventual consistency between Redis cache and Database (DB)?
**Answer:**
Common strategies and patterns include:
1. Choosing the right update policy: Prioritize 'Delete cache, then update DB' or 'Update DB, then delete cache'. Deleting cache rather than updating is recommended because updating cache is expensive and prone to dirty data.
2. Delayed double-deletion: Delete the cache, update the DB, and after a short pause, delete the cache again to prevent concurrent writes from creating dirty data.
3. Message queue retry mechanism: Write failed cache deletions to a message queue and rely on queue retries to ensure keys are eventually deleted.
4. Database binlog subscription: Listen to DB binlogs using tools like Canal, asynchronously deleting cache by consuming logs to lower business coupling (though increasing system complexity).
5. Setting fallback TTL: Assign a reasonable TTL to the cache so that even if inconsistencies occur, data naturally converges upon expiration.

#### 7. How to ensure eventual consistency between cache and database data?
**Answer:**
Common strategies and solutions include: 1. Choosing the right cache update policy: Adopt 'delete cache, then update database' or 'update database, then delete cache'. Deleting the cache rather than updating it directly is recommended because it is faster and lowers the probability of reading stale data. 2. Introducing message queues for assurance: Utilize retry mechanisms in message queues by pushing keys that failed deletion into a queue to retry deletion. 3. Database subscription + message queue (e.g., Canal): Listen to database binlog changes to capture modified data and asynchronously execute cache deletions, reducing business intrusion while increasing system complexity. 4. Dual-deletion with delay: After deleting the cache and updating the database for the first time, delete the cache a second time after a brief delay to prevent race conditions from writing stale data. 5. Setting cache expiration times as a fallback: Assign reasonable expiration times to caches as an ultimate safety net.

#### 8. What are the Redis persistence mechanisms and what are their differences?
**Answer:**
Redis primarily supports two persistence mechanisms: 1. RDB (Redis DataBase): Saves a compressed binary snapshot of the current process data to disk. Supports manual triggers (`SAVE` blocking, `BGSAVE` asynchronous child process via `fork`) and automatic triggers (`save m n`). Advantages: fast recovery speed, compact file size; Disadvantages: poor real-time durability, potential data loss. 2. AOF (Append Only File): Records every write command in an independent log format. Operates via append, sync policies (`appendfsync`), rewrite compression (`BGREWRITEAOF`), and load processes. Advantages: high data security, strong real-time performance; Disadvantages: larger file size, slower recovery.

#### 9. What are the data synchronization methods in Redis master-slave replication?
**Answer:**
Redis uses the PSYNC command to complete master-slave synchronization, which is split into full replication and partial replication: 1. Full Replication: Used for initial synchronization. The master node executes BGSAVE to generate an RDB file and sends it to the replica. The replica clears old data and loads the RDB, while buffered write commands accumulated during this process in the replication backlog are subsequently sent and applied. 2. Partial Replication: Used for recovery from transient network disconnections. The replica sends PSYNC with runId and offset. If the master finds the corresponding data within the replication backlog buffer (default 1MB), it replies with +CONTINUE to perform incremental command synchronization.

#### 10. What causes Redis blocking, and how do you diagnose and resolve slow queries and high CPU utilization?
**Answer:**
Redis blocking is typically caused by high time-complexity commands ($O(N)$ or worse) executed on large objects, or serialization/persistence bottlenecks. Diagnosis and resolution steps:
1. Slow Query Analysis: Use `slowlog get {n}` to retrieve the slowest commands. Mitigate by replacing heavy commands (e.g., swapping `hgetall` for `hmget`, avoiding `keys` or `sort`), and splitting large objects/keys into smaller chunks.
2. CPU Saturation: Check Redis usage via `redis-cli -h {ip} -p {port} --stat`. If the OPS reaches peak limits (tens of thousands+), scale out using Redis Cluster. If OPS is moderate (hundreds/thousands), inspect commands and persistence locks.
3. Persistence Bottlenecks:
   - Fork Blocking: `fork()` during RDB/AOF rewrites causes main-thread latency if execution time is too high.
   - AOF Fsync Blocking: Background threads issuing `fsync` can cause the main thread to block if the previous sync is >2 seconds overdue.
   - Transparent HugePages (THP): Enabled OS kernels increase copy-on-write memory pages from 4KB to 2MB, significantly slowing write operations.

#### 11. What is the HotKey Rebuilding (Cache Stampede) problem? What impacts does it bring, and what are the solutions?
**Answer:**
When a high-concurrency hotkey expires, because the cache reconstruction operation is time-consuming (e.g., complex SQL, multiple I/O calls), a large number of concurrent threads attempt to rebuild the cache simultaneously. This causes backend database load to surge and can even crash the application. Solutions: 1. Mutex Key: Allow only one thread to rebuild the cache while other threads wait and retry fetching from the cache once reconstruction completes. 2. Logical Expiration (Never Expire): Do not set a physical expiration time on the physical cache; instead, store a logical expiration time inside each value. When the logical expiration time is exceeded, trigger an independent asynchronous thread to rebuild the cache.

#### 12. What is the bottomless pit problem and how can it be solved?
**Answer:**
In 2010, Facebook's Memcached nodes reached 3,000, carrying TB-level cached data. Development and operations teams noticed that adding many new Memcached nodes to meet business requirements did not improve performance, but instead degraded it. This phenomenon was termed the cache 'bottomless pit' problem. Why this happens: Because key-value databases typically map keys to nodes using hash functions, key distribution is decoupled from business logic. Due to the continuous growth of data volume and access traffic, adding many nodes for horizontal scaling causes keys to be distributed across even more nodes. Thus, whether in Memcached or Redis distributed setups, batch operations usually need to be fetched from different nodes. Unlike single-server batch operations which involve only one network operation, distributed batch operations involve multiple network round-trips. Optimization strategies: 1. Optimize commands themselves, e.g., optimizing operation syntax. 2. Reduce network communication frequency. 3. Lower integration costs, e.g., clients using persistent connections/connection pools, NIO, etc.

#### 13. What is the cache hot key rebuilding problem, and how can it be resolved?
**Answer:**
When a high-concurrency cache key expires, a massive number of threads simultaneously try to rebuild the cache (e.g., executing complex SQL queries, multiple IO operations), leading to a sudden surge in backend load or even application crash. Solutions include: 1. Mutex Key: Allow only one thread to build the cache while other threads wait. 2. Logical Expiration (Never expire physically): Do not let the cache expire physically, but set a logical expiration time for each value, updating the cache asynchronously via an independent thread.

#### 14. What is the underlying mechanism of Redis Master-Slave replication?
**Answer:**
1. Master information storage: Slaves store the master's IP and port.
2. Connection establishment: Slaves connect to the master.
3. PING command: Slaves issue PING to check network connectivity and master status.
4. Authentication: Slaves provide credentials if the master requires authentication.
5. Dataset synchronization: The master sends its complete dataset (full resynchronization via RDB).
6. Continuous command replication: The master continuously streams write commands to slaves to ensure data consistency.

#### 15. Why did Redis choose a single-threaded architecture initially, and how does multithreading manifest in Redis 4.0 and later?
**Answer:**
Redis initially chose a single-threaded model because in-memory operations are extremely fast, making network I/O the primary bottleneck rather than CPU. This avoids unnecessary thread context switching and complex lock contention. Starting from Redis 4.0 and later, multithreading was introduced (primarily via background threads) to handle slower operations off the main thread, such as flushing dirty data, releasing unused connections, and asynchronous deletion of large keys using UNLINK.

#### 16. Why is Redis so fast?
**Answer:**
1. Operations are completely in-memory.
2. It uses a single-threaded model, avoiding overhead from context switching and race conditions.
3. It is based on non-blocking I/O multiplexing mechanisms.
4. Written in C with highly optimized data structures and tailored performance tuning across various foundational structures.


### Mid Level (55 cards)

#### 1. Can you detail the master-slave data synchronization mechanisms in Redis (Full Resynchronization and Partial Resynchronization)?
**Answer:**
Redis uses the PSYNC command to complete master-slave data synchronization, split into full and partial resynchronization:
1. Full Resynchronization (used for initial replication):
   - The replica sends PSYNC ? -1, and the master responds with +FULLRESYNC along with its runId and offset.
   - The master executes BGSAVE to generate an RDB file and sends it to the replica.
   - The replica clears old data and loads the newly received RDB file.
   - Write commands generated by the master during RDB generation/transmission are buffered in the "replication client buffer" and sent to the replica afterward.
2. Partial Resynchronization (optimized for network blips or command loss):
   - When master-slave disconnection exceeds repl-timeout, the connection breaks.
   - The master buffers recent write commands in the "replication backlog buffer" (default 1MB).
   - Upon network recovery, the replica sends PSYNC {runId} {offset}.
   - The master validates that the runId matches and the offset remains inside the backlog buffer. If valid, it responds with +CONTINUE and transmits the missing data from the buffer to restore sync.

#### 2. Can you explain in detail the core architecture, data sharding mechanism, and failover process of Redis Cluster?
**Answer:**
Redis Cluster achieves distributed storage through data sharding and high availability through automatic failover.
1. Data Sharding: The cluster is pre-partitioned into 16,384 hash slots. Each key is mapped to a specific slot via CRC16 checksum modulo 16384. Nodes must be assigned slots to respond to related commands.
2. Node Communication: Nodes perform handshakes (CLUSTER MEET) and state maintenance (PING/PONG messages) via the Gossip protocol.
3. Failover:
   - Failure Detection: When a node fails to communicate within cluster-node-timeout, it is marked as provisionally offline (PFAIL). When a majority of master nodes holding slots flag it as offline, it triggers a confirmed failure (FAIL).
   - Voting & Election: Replicas check the master's disconnection duration, and once qualified, wait for an election delay to trigger an election. Master nodes holding slots vote (1 vote per master). The replica winning N/2 + 1 votes wins and replaces the failed master.
4. Deployment Recommendation: To prevent single points of failure and split-brain scenarios, all master nodes in the cluster should be distributed across at least 3 distinct physical machines or availability zones.

#### 3. Compare Fair Scheduler and Capacity Scheduler in multi-tenant cluster environments.
**Answer:**
• Fair Scheduler: Assigns resources to jobs dynamically so all applications share an equal amount of cluster resources over time. Ideal for ensuring equal progress, optimizing data locality across varying pool utilizations, and preventing FIFO starvation. • Capacity Scheduler: Allows multi-tenant clusters to maximize throughput via isolated resource queues with guaranteed minimum capacities. Ideal for workloads requiring scheduling determinism, strict memory-based guarantees, and predictable hierarchical resource allocations.

#### 4. Compare single-cluster and multi-cluster architectures in terms of fault tolerance and scalability.
**Answer:**
• Single Cluster: Easier to manage with centralized operations but more vulnerable to system-wide failures and scalability limits.
• Multi-Cluster: Offers better fault isolation and scalability by separating workloads, though it increases operational complexity and cost.

#### 5. Does Redis support transactions? What are its principles and limitations?
**Answer:**
Redis provides basic transaction support, but it does not fully comply with ACID. Transactions are implemented using `MULTI` (start), `EXEC` (execute), `DISCARD`, and `WATCH`. Commands are not executed immediately upon invocation; instead, they are queued in a server-side transaction queue and executed atomically and sequentially upon receiving `EXEC`. Limitations: 1. No rollback (syntax errors cause the entire transaction to be rejected, but runtime errors allow remaining commands to continue executing to maintain simplicity and speed); 2. Transaction execution cannot be interrupted by other clients; 3. Durability guarantees are not strictly fulfilled.

#### 6. Does Redis support transactions? What are the underlying principles and caveats?
**Answer:**
Redis provides simple transaction support (not fully ACID-compliant). Transactions are initiated with the MULTI command and terminated with EXEC. Intermediate commands are queued in sequence within the server's transaction queue, and upon receiving EXEC, the entire queue is executed atomically. Key caveats: 1. Redis transactions do not support rollbacks (syntax errors reject the transaction, but runtime errors allow remaining commands to continue executing) to maintain simplicity and speed. 2. Transactions will not be interrupted by other client requests during execution.

#### 7. How are Lua scripts used in Redis?
**Answer:**
Redis transactions are relatively simple, so Lua scripts can be utilized to extend Redis command functionality: 1. Atomic Execution: Lua scripts execute atomically in Redis, ensuring no other commands are interleaved during execution. 2. Custom Command Reuse: Helps developers and operators create customized commands that can reside permanently in Redis memory for reuse. 3. Reduced Network Overhead: Multiple commands can be packaged together, efficiently decreasing network round-trip overhead.

#### 8. How can I intuitively understand I/O Multiplexing?
**Answer:**
I/O Multiplexing is similar to a teacher on a podium waiting for students to raise their hands to answer questions. Compared to polling everyone one by one (non-concurrent) or assigning a clone to every single person (multithreading), multiplexing allows a single thread to wait for multiple Socket events. When a certain Socket is ready (raises its hand), the system notifies the thread to process the data corresponding to that Socket, thereby achieving efficient handling of massive concurrent connections with a single thread.

#### 9. How can Redis be used to implement asynchronous queues?
**Answer:**
Main approaches include: 1. Using a List as a queue: LPUSH to produce messages, RPOP to consume messages. A consumer running an infinite RPOP loop causes excessive CPU consumption, which can be mitigated with sleep intervals at the cost of latency. 2. Using a List as a queue with BRPOP: LPUSH to produce, BRPOP to consume. BRPOP is the blocking version of RPOP; when the queue is empty, it blocks until a value arrives or a timeout occurs, supporting only point-to-point queues. 3. Using Redis Pub/Sub: Supports 1:N message publishing and subscribing, but it is unreliable, provides no guarantee that subscribers will receive messages, and does not store messages. Complex asynchronous queue requirements should generally be delegated to dedicated message queue systems like Kafka.

#### 10. How can asynchronous queues be implemented using Redis?
**Answer:**
Main approaches include:
1. Using Lists as Queues: Produce messages via `LPUSH`, consume via `RPOP`. Consumers typically need to spin `RPOP`, but an empty queue causes CPU spikes; this can be mitigated with sleep intervals, which introduce message latency.
2. Using Lists with Blocking Reads (`LPUSH` + `BRPOP`): `BRPOP` is the blocking counterpart of `RPOP`. When the queue is empty, it blocks until a value arrives or a timeout occurs, supporting only 1-to-1 queues.
3. Using Pub/Sub (Publish/Subscribe): Supports 1-to-N message publishing and subscription where clients subscribe to channels. However, this approach is unreliable, does not guarantee delivery to subscribers, and lacks message persistence. Production environments generally recommend dedicated message queues (MQ).

#### 11. How do you ensure consistency between local caches and distributed caches?
**Answer:**
The following methods can be adopted:
1. Use Redis's built-in Pub/Sub mechanism: All nodes in the distributed cluster subscribe to a local cache invalidation channel. When a node deletes a Redis cache, it simultaneously publishes an invalidation message. Subscribers receive the message and delete the corresponding local key. Note that Redis Pub/Sub is not reliable and cannot guarantee 10opedic delivery.
2. Introduce a dedicated message queue, such as RocketMQ, to guarantee message reliability, though this increases system complexity.
3. Set an appropriate expiration time as a fallback; local caches can be configured with a relatively short TTL.

#### 12. How do you ensure eventual consistency between a cache and a database?
**Answer:**
According to the CAP theorem, under availability and partition tolerance, consistency cannot be fully guaranteed. Therefore, absolute consistency between cache and database cannot be achieved; we can only strive to ensure the eventual consistency of the cache and the database.

#### 13. How does Redis handle memory eviction when it reaches maxmemory?
**Answer:**
When Redis hits the maxmemory limit, it applies configured eviction policies like noeviction, volatile-lru, allkeys-lru, volatile-lfu, allkeys-lfu, volatile-random, allkeys-random, or volatile-ttl to free up space by removing keys.

#### 14. How does the quorum journal manager work with fencing?
**Answer:**
To work with fencing, the journal manager uses epoch numbers. Epoch numbers are integers that always increase and have a unique value once assigned. The NameNode generates epoch numbers using a simple algorithm and uses them while sending RPC requests to the QJM. When configuring NameNode HA, the first Active NameNode gets epoch value 1. In case of failover or restart, the epoch number increases. The NameNode with a higher epoch number is considered newer than any NameNode with an earlier epoch number.

#### 15. How is a SkipList implemented? What are its internal principles and application scenarios?
**Answer:**
A skip list is an ordered data structure that achieves fast element access by maintaining multiple pointers to other nodes within each node. Why does Redis use skip lists instead of red-black trees in Sorted Sets (zsets)? 1. Performance consideration: Under high concurrency, tree structures require complex rebalance operations spanning the entire tree or large ranges, whereas skip list modifications typically involve local pointer adjustments. 2. Implementation consideration: Under comparable complexity and performance, skip lists are simpler and more intuitive to implement. Skip list nodes include: level (random height from 1 to 32 generated via power law), forward pointers (level[i].forward, used to traverse from head to tail), span (distance between nodes used to compute rank), score (double-precision floating-point number for sorting), and obj (pointing to the string object saving the SDS value).

#### 16. How is data partitioned in Redis Cluster? What are the common schemes?
**Answer:**
There are three common data partitioning schemes: 1. Node modulo partitioning: Use specific data (such as key or user ID) and hash value modulo hash(key)%N to determine the target node. The downside is that when the node count changes (scaling out or in), data mappings must be recalculated, leading to massive data migration. 2. Consistent hashing: Organize the entire hash space into a virtual ring, hash the cache nodes' IPs or hostnames and place them on the ring, and locate keys via the same hash, directing them to the first cache node encountered clockwise. 3. Virtual Slot partitioning: Introduce virtual nodes on top of consistent hashing, which Redis Cluster adopts. The virtual nodes are called "slots" (16,384 in total), acting as an abstraction layer between data and physical nodes, with each physical node holding a fixed subset of slots.

#### 17. How is the Leader node elected in a Redis Sentinel cluster?
**Answer:**
1. When an online Sentinel node determines that the master node is subjectively/objectively down, it sends a `sentinel is-master-down-by-addr` command to other Sentinel nodes, requesting to set itself as the leader.
2. Receiving Sentinel nodes will grant their vote if they have not already agreed to another Sentinel's request for this round; otherwise, they decline.
3. If a Sentinel node finds that the number of votes it received is greater than or equal to the configured quorum and satisfies `num(sentinels)/2 + 1`, it successfully wins the election as the leader.
4. If no leader is elected in the current round, the system waits and enters the next election cycle to retry.

#### 18. How should insufficient memory errors in Redis be handled?
**Answer:**
1. Modify the `maxmemory` parameter in the `redis.conf` configuration file to increase available memory, or configure it dynamically via the CLI command: `CONFIG SET maxmemory <bytes>`.
2. Adjust the memory eviction policy (`maxmemory-policy`) to free up memory space promptly.
3. Scale horizontally by deploying a Redis Cluster mode.

#### 19. How to handle insufficient memory errors in Redis?
**Answer:**
Primary ways to handle insufficient Redis memory: 1. Modify the 'maxmemory' parameter in the redis.conf configuration file, or dynamically set the memory limit via the command `set maxmemory` to increase available Redis memory. 2. Change the memory eviction policy to promptly free up memory space. 3. Use Redis Cluster mode to perform horizontal scale-out.

#### 20. What are Fair and Capacity Schedulers?
**Answer:**
1-Fair Scheduler: Assigns resources to jobs so that all jobs get, on average, an equal share of resources over time. When a single job runs, it uses the entire cluster; new tasks share space as they arrive. 2-Capacity Scheduler: Allows sharing of a large cluster while giving each organization a minimum capacity guarantee. Unused capacity can be accessed by other organizations for elasticity.

#### 21. What are Redis's expired data eviction strategies?
**Answer:**
1. Passive Expiration (Lazy Deletion): Keys are checked and deleted upon access. Flaw: Expired keys that are never accessed remain in memory indefinitely.
2. Active Expiration (Periodic Deletion): Redis periodically samples the keyspace and deletes expired keys. Since scanning all keys is unfeasible, it randomly samples a subset of keys during each cycle.

#### 22. What are cache stampede, cache penetration, and cache avalanche, and how do you mitigate them?
**Answer:**
Cache Stampede (Breakdown): High-traffic key expires simultaneously, hitting the DB. Mitigation: Mutex locks on cache miss or asynchronous background refresh.
Cache Penetration: Queries for non-existent data in both cache and DB, bypassing the cache layer. Mitigation: Cache null/default values with short TTLs or use a Bloom filter.
Cache Avalanche: Mass expiration or crash of cache instances at the same time, flooding the DB. Mitigation: Cluster deployment, multi-level caching, randomized TTL jitter, and permanent retention for ultra-hot keys, along with service circuit-breaking and fallback mechanisms.

#### 23. What are some common practices for cache warm-up?
**Answer:**
Cache warm-up refers to pre-loading data from the database into the cache before the system goes live or during its initial startup. Common practices include: 1. Writing dedicated cache refresh pages or management backend endpoints to manually trigger warm-up upon deployment. 2. Automatically loading data upon project startup when the data volume is small. 3. Periodically refreshing the cache using scheduled background tasks.

#### 24. What are the Redis persistence mechanisms and how do they differ?
**Answer:**
Redis provides two main persistence mechanisms: 1. RDB (Redis DataBase): Generates a compressed binary snapshot of the current process data and saves it to disk. It supports manual triggering (SAVE blocks the current server, BGSAVE forks a child process to run asynchronously) and automatic triggering (meeting save m n configurations, full-disk replication, debug reload, or shutdown without AOF). 2. AOF (Append Only File): Records every write command in an independent log file, replaying the AOF file upon restart to recover data. The workflow includes command appending, file synchronization, file rewriting, and startup loading. AOF is currently the mainstream method for real-time data persistence.

#### 25. What are the advantages and disadvantages of RDB and AOF persistence in Redis?
**Answer:**
RDB:
- Pros: Generates a compact binary file (dump.rdb), ideal for backups, full replication, and disaster recovery; recovery speed is significantly faster than AOF.
- Cons: Lower real-time capability, unable to achieve second-level persistence without data loss if a crash occurs between intervals; older Redis versions may face backward compatibility issues with newer RDB formats.
AOF:
- Pros: Better real-time durability through configurable policies like appendfsync always; log-append-only design makes files easily repairable via redis-check-aof upon corruption.
- Cons: Larger file sizes and slower recovery speeds compared to RDB; startup efficiency is lower with very large datasets.

#### 26. What are the advantages of Redis SDS (Simple Dynamic String) compared to traditional C-style strings?
**Answer:**
C-style strings are null-terminated ('\0') and do not record their length, leading to issues such as O(N) complexity for length retrieval, vulnerability to buffer overflows, and inability to store binary data containing '\0'. The advantages of Redis SDS include: 1. It records the 'len' property, making length retrieval an O(1) operation. 2. It automatically expands space through pre-allocation and lazy space release mechanisms, effectively reducing memory allocation frequency and preventing buffer overflows. 3. It is binary-safe, meaning it can store arbitrary binary data like images and audio.

#### 27. What are the advantages of Redis's SDS (Simple Dynamic String) compared to traditional C-style strings?
**Answer:**
C uses N+1 length character arrays terminated by '\0', which suffers from O(N) length retrieval, vulnerability to buffer overflows, and inability to store binary data. Advantages of Redis's SDS include: 1. O(1) complexity for retrieving string length (internally maintaining the `len` property); 2. Automatic space expansion to prevent buffer overflows; 3. Effective reduction of memory allocation frequency (via space preallocation and lazy space release mechanisms); 4. Binary safety, allowing arbitrary binary data to be stored.

#### 28. What are the advantages of combining Redis with Lua scripts?
**Answer:**
1. Atomicity: Lua scripts execute atomically in Redis without interruption from other commands.
2. Reusability: Custom commands can be stored persistently in memory and invoked multiple times.
3. Reduced Network Overhead: Multiple commands can be packaged into a single invocation, significantly reducing round-trip latency.

#### 29. What are the basic data structures in Redis and their typical use cases?
**Answer:**
1. String: The most basic structure, storing numbers, text, or binary data (max 512MB). Use cases: Caching, counters, shared sessions, rate limiting. 2. Hash: Key-value pair structure. Use cases: Caching user object information. 3. List: Ordered string list, which can act as stacks and queues. Use cases: Message queues, article lists. 4. Set: Unordered non-duplicate string set. Use cases: Tags, mutual follows. 5. Sorted Set: Weighted ordered set. Use cases: User like statistics, user leaderboards.

#### 30. What are the common performance issues and best practices in Redis?
**Answer:**
1. It is recommended that Master nodes avoid any persistence tasks (such as memory snapshots and AOF logs), particularly avoiding memory snapshots for persistence. 2. If data criticality requires it, enable AOF backups on a Slave node with a synchronization policy set to every second. 3. Ensure Slaves and Masters are in the same LAN to guarantee replication speed and connection stability. 4. Avoid adding replica nodes to heavily loaded master databases. 5. Running BGREWRITEAOF on the Master consumes significant CPU and memory resources, causing high load and potential transient service pauses. 6. Master-replica replication is recommended to use a unidirectional chain structure (Master -> Slave1 -> Slave2) to simplify single-point failure handling and failovers.

#### 31. What are the common replication topologies in Redis master-slave architecture?
**Answer:**
Redis replication topologies support single-layer or multi-layer relationships and are categorized into three main types: 1. One Master, One Slave: The simplest replication topology, providing failover support when the master node crashes; 2. One Master, Multiple Slaves (Star Topology): Applications can utilize multiple slave nodes to implement read/write splitting, distributing the read load from the master node; 3. Tree-Structured Master-Slave: Slave nodes can replicate data from the master node while simultaneously acting as parent master nodes to downstream slave nodes, effectively reducing master node load and bandwidth overhead.

#### 32. What are the common replication topologies in Redis?
**Answer:**
Redis replication topologies support single-layer or multi-layer replication relationships, categorized into three primary types: 1. Master-Replica (One-to-One): The simplest topology, used to provide failover support when the master node crashes. 2. Master-Multiple-Replicas (Star Topology): Applications can leverage multiple replica nodes for read/write splitting, offloading read pressure from the master node. 3. Tree Topology: Replica nodes not only replicate data from the master node but can also serve as master nodes for other replica nodes, propagating replication further down. By introducing intermediate replication layers, this effectively reduces the load on the primary master and minimizes the volume of data transmitted to replicas.

#### 33. What are the common use cases for Redis?
**Answer:**
Common application scenarios for Redis include: 1. Caching: Reducing database access queries and vastly improving system response speed. 2. Session Storage: Providing fast session read/write operations to enhance user experience. 3. Message Queues: Increasing system scalability and decoupling via asynchronous processing (suitable for lightweight scenarios). 4. Real-time Analytics: Processing complex data analytics quickly in-memory. 5. Leaderboards and Counters: Utilizing data structures like Sorted Sets (ZSet) to rapidly update and query social or gaming rankings. 6. Publish/Subscribe: Building real-time messaging notifications or real-time analytics systems.

#### 34. What are the core functions and advantages of Redis Cluster?
**Answer:**
1. Data Partitioning (Sharding): Disperses data across multiple nodes, breaking through single-machine memory limits and significantly increasing storage capacity; each master node can provide read and write services externally, greatly improving cluster response capability. 2. High Availability: The cluster supports master-slave replication and automatic failover of master nodes (similar to Sentinel). When any node fails, the cluster can still provide external services.

#### 35. What are the expiration eviction strategies for keys in Redis?
**Answer:**
1. Lazy Deletion: Keys are checked only when queried; if their expiration time has been reached, they are deleted. Disadvantage: If expired keys are never accessed, they remain undeleted and continuously consume memory.
2. Periodic Deletion: Redis checks the database at regular intervals to delete expired keys. Since scanning all keys is impossible, Redis randomly samples a subset of keys for inspection and deletion during each cycle.

#### 36. What are the memory overflow control and memory eviction policies in Redis?
**Answer:**
1. noeviction: The default policy; it does not delete any data, rejects all write operations, and returns an error while continuing to respond to read operations. 2. volatile-lru: Evicts keys based on the LRU (Least Recently Used) algorithm among those with an expiration field set, until enough space is freed. 3. allkeys-lru: Evicts keys based on the LRU algorithm regardless of whether an expiration field is set, until enough space is freed. 4. allkeys-random: Randomly deletes keys until enough space is freed. 5. volatile-random: Randomly deletes expired keys until enough space is freed. 6. volatile-ttl: Deletes keys closest to expiration based on their 'ttl' attribute.

#### 37. What are the primary use cases and applications of Redis?
**Answer:**
1. Caching: Improves system response speed by reducing database access frequency.
2. Session Storage: Provides rapid session read/write access to enhance user experience.
3. Message Queues: Increases system scalability and decoupling through asynchronous processing.
4. Real-time Analytics: Processes complex data streams in memory in real time.
5. Leaderboards and Counters: Leverages sorted sets (ZSet) and other structures to rapidly update and retrieve leaderboard metrics.
6. Publish/Subscribe: Builds real-time messaging systems, such as live notifications.

#### 38. What are the principles, advantages, and disadvantages of a Bloom Filter?
**Answer:**
A Bloom filter is a compact data structure consisting of a bit array and K hash functions. When an element is added, it is mapped to K positions in the bit array via the K hash functions, and those bits are set to 1. When checking for existence, if all corresponding bits are 1, it 'may exist'; if any bit is not 1, it 'definitely does not exist'. Disadvantages: It has a certain false positive rate (due to hash collisions), and by default, it does not support deleting elements.

#### 39. What are the respective advantages and disadvantages of Redis RDB and AOF persistence?
**Answer:**
RDB Advantages: 1. Compact binary file (dump.rdb), ideal for backups and full replication; 2. Great disaster recovery profile and easy to transport; 3. Faster recovery speed than AOF. RDB Disadvantages: 1. Lower real-time safety, cannot achieve second-level persistence without data loss after the last snapshot; 2. Potential version compatibility issues. AOF Advantages: 1. High real-time safety, supports appendfsync configurations (e.g., 'always' logging every write); 2. Append-only write design makes it easily repairable via redis-check-aof upon crashes. AOF Disadvantages: 1. Larger file sizes and slower recovery times compared to RDB; 2. Lower startup efficiency under large datasets than RDB.

#### 40. What data structures are available in Redis?
**Answer:**
1. String: The most basic data structure, storing strings, numbers, or binary data up to 512MB. Use cases: Caching, counters, shared sessions, rate limiting.
2. Hash: A map of key-value pairs inside a single key. Use cases: Caching user details, objects.
3. List: Ordered lists of strings, capable of acting as stacks or queues. Use cases: Message queues, article timelines.
4. Set: Unordered and unique collections of strings. Use cases: Tags, mutual followers.
5. Sorted Set (ZSET): Elements associated with a score for sorting. Use cases: User like statistics, leaderboards.

#### 41. What is Apache Redis and in-memory caching?
**Answer:**
Redis is an open-source, in-memory data structure store used as a database, cache, message broker, and streaming engine. In-memory caching stores frequently accessed data in RAM to drastically reduce read latency and database load compared to disk-based storage.

#### 42. What is Hybrid Persistence in Redis 4.0?
**Answer:**
When restarting Redis, relying solely on RDB can cause massive data loss, while replaying a pure AOF log is relatively slow. Redis 4.0 introduced hybrid persistence, combining RDB file contents and incremental AOF logs together in the same file. The AOF log here is no longer a full historical log, but rather an incremental AOF log starting from the moment persistence begins, which is typically very small. Upon restart, Redis loads the RDB content first and then replays the incremental AOF log, drastically improving startup efficiency.

#### 43. What is I/O multiplexing?
**Answer:**
I/O multiplexing is a technique that allows a single thread to monitor multiple descriptors (sockets). Once a descriptor becomes ready (readable or writable), it notifies the program to perform the corresponding read or write operation. Compared to traditional blocking loops or creating a thread for every connection (multi-process/multi-thread models), I/O multiplexing drastically improves system concurrency capacity and resource utilization. Redis implements its efficient single-threaded event loop based on the Reactor pattern using epoll/kqueue.

#### 44. What is Redis Hybrid Persistence (introduced in Redis 4.0)?
**Answer:**
Restarting Redis using only RDB can result in significant data loss, while replaying a pure AOF file is much slower. Redis 4.0 introduced hybrid persistence, combining the memory snapshot from an RDB file with incremental AOF logs generated during the self-persistence period. Upon restart, Redis first loads the RDB content and then replays the incremental AOF logs, drastically improving startup efficiency.

#### 45. What is Redis Sentinel and what are its core capabilities?
**Answer:**
Redis Sentinel is a distributed system designed to provide high availability and automated failover for Redis master-slave deployments. It consists of Sentinel nodes (which do not store data, but monitor data nodes) and data nodes (masters and slaves). Its core features include: Monitoring (continuously checking if master and slave instances operate correctly), Automatic failover (promoting a slave to master if the master fails), Configuration provider (acting as a trusted authority for clients to discover the current master address), and Notification (alerting clients of failover events).

#### 46. What is Redis and what are its features?
**Answer:**
Redis is an open-source, in-memory key-value NoSQL database. Its values support multiple data structures such as Strings, Hashes, Lists, Sets, Sorted Sets, Bitmaps, HyperLogLogs, and GEO, capable of satisfying complex business scenarios. Because data is fully stored in memory, read and write performance is extremely high. At the same time, it supports RDB snapshot and AOF log persistence mechanisms, ensuring data is not lost upon power failure or restart.

#### 47. What is Redis master-slave replication and what are its primary use cases?
**Answer:**
Master-slave replication copies data from a master Redis server to one or more slave servers in a unidirectional flow (master to slave). It supports master-slave and slave-slave synchronization. Main use cases include:
- Data Redundancy: Provides hot backups as an additional layer of safety beyond persistence.
- Fault Recovery: Slaves can provide read availability or be promoted during failures.
- Load Balancing: Combined with read/write splitting (writes to master, reads from slaves), it increases read throughput.
- High Availability Foundation: Serves as the base for Redis Sentinel and Cluster.

#### 48. What is a Redis ziplist and how does it work?
**Answer:**
A ziplist is a data structure designed by Redis to save memory. It consists of a sequence of specially encoded contiguous memory blocks. A ziplist can contain any number of entries, where each entry can store a byte array or an integer value. A ziplist is composed of the following parts:
1. zlbytes: Records the total number of memory bytes used by the entire ziplist.
2. zltail: Records the offset in bytes from the starting address of the ziplist to the tail entry.
3. zllen: Records the number of entries contained in the ziplist.
4. entryX: The list entries/nodes.
5. zlend: Used to mark the end of the ziplist.

#### 49. What is a quicklist in Redis, and what problems does it solve?
**Answer:**
Early versions of Redis used ziplist and standard linkedlist for the list data structure. However, linkedlists have relatively high overhead (e.g., prev and next pointers consume 16 bytes on 64-bit systems), and each node is allocated independently, which easily leads to memory fragmentation. Therefore, Redis 3.2 introduced quicklist to replace both ziplist and linkedlist. Quicklist is a hybrid data structure that balances time and space efficiency, and it is essentially a doubly linked list whose nodes are ziplists.

#### 50. What is a ziplist in Redis, and what is its internal structure composed of?
**Answer:**
A ziplist is a sequential data structure developed by Redis to save memory, composed of a series of specially encoded continuous memory blocks. It can contain any number of entries, where each entry can store a byte array or an integer value.
The components of a ziplist mainly include:
- zlbytes: Records the total bytes of memory occupied by the entire ziplist.
- zltail: Records the offset of the tail node from the starting address of the ziplist, in bytes.
- zllen: Records the number of nodes contained in the ziplist.
- entryX: List nodes.
- zlend: Used to mark the end of the ziplist.

#### 51. What is the data recovery process in Redis?
**Answer:**
When a Redis failure occurs, data can be recovered from either RDB or AOF files. The recovery process simply requires copying the RDB or AOF file into the Redis data directory, configuring the corresponding persistence switches, and starting redis-server. Startup data loading workflow: 1. If AOF persistence is enabled and an AOF file exists, it takes priority and is loaded first. 2. If AOF is disabled or the AOF file does not exist, the RDB file is loaded. 3. Upon successful loading of the AOF/RDB file, Redis starts successfully. 4. If errors exist in the AOF/RDB file, Redis startup fails and prints an error message.

#### 52. What is the difference between Redis RDB and AOF persistence?
**Answer:**
RDB (Redis Database) takes point-in-time snapshots of dataset at specified intervals, offering faster restarts and smaller file sizes. AOF (Append Only File) logs every write operation received by the server, providing better durability with minimal data loss risk at the cost of larger file sizes and potentially slower recovery.

#### 53. What is the internal working principle and timeline of tasks in Redis Sentinel?
**Answer:**
Sentinel uses three periodic tasks to maintain cluster health: (1) Every 10 seconds, each Sentinel sends an 'INFO' command to masters and slaves to gather topology changes. (2) Every 2 seconds, Sentinels publish/subscribe state information on the 'sentinel:hello' channel. (3) Every 1-second, Sentinels send a 'PING' to all nodes and other Sentinels for heartbeat checks. Failure detection moves from Subjective Down (SDOWN, declared by a single Sentinel when a node fails to respond within 'down-after-milliseconds') to Objective Down (ODOWN, confirmed when a quorum of Sentinels agree). Leader election is then performed using the Raft algorithm, and the leader executes failover via 'SLAVEOF NO ONE' on the selected replica.

#### 54. What is the master-slave replication process in Redis?
**Answer:**
1. Store Master Info: The slave node stores the IP and port of the master node.
2. Establish Connection: Once the slave finds the new master, it attempts to establish a network connection.
3. Send PING: After connection, a PING request is sent for initial communication to verify network socket usability and ensure the master can accept commands.
4. Authentication: If the master requires password authentication, the slave must pass correct credentials.
5. Synchronize Dataset: After replication connection is normal, the master sends all its data to the slave.
6. Continuous Replication: The master continuously streams write commands to the slave to maintain master-slave data consistency.

#### 55. What memory overflow control / memory eviction policies does Redis provide?
**Answer:**
Redis provides 6 memory eviction policies: 1. `noeviction` (default): Does not delete any data, rejects all write operations and returns an error, responding only to reads; 2. `volatile-lru`: Deletes keys with an expiration attribute set (`expire`) using the LRU algorithm until enough space is freed; 3. `allkeys-lru`: Deletes any key using the LRU algorithm until enough space is freed; 4. `allkeys-random`: Randomly deletes any key until enough space is freed; 5. `volatile-random`: Randomly deletes expired keys until enough space is freed; 6. `volatile-ttl`: Deletes data closest to expiration based on the `ttl` property of the key-value object.


### Senior Level (41 cards)

#### 1. Compare single-cluster and multi-cluster caching and data system architectures in terms of fault tolerance and scalability.
**Answer:**
• Single Cluster: Easier to manage with centralized operations, but more vulnerable to system-wide failures, bottlenecks, and scalability limits. • Multi-Cluster: Offers better fault isolation and scalability by separating workloads and partitioning availability zones, though it increases operational complexity, network overhead, and infrastructure cost.

#### 2. How do you ensure consistency between cache and database (DB)?
**Answer:**
According to the CAP theorem, under the premise of maintaining availability and partition tolerance, strong consistency cannot be guaranteed. Therefore, absolute consistency between cache and database cannot be achieved; you can only use appropriate strategies (such as Cache Aside pattern, delayed double deletion, etc.) to ensure eventual consistency between cache and database as much as possible.

#### 3. How do you ensure consistency between local cache and distributed cache?
**Answer:**
You can adopt the following approaches:
1. Use Redis Pub/Sub mechanism: All distributed cluster nodes subscribe to a local cache deletion channel. When deleting a Redis cache node, simultaneously publish a local cache deletion message. Subscribers receive the message and delete the corresponding local key. The drawback is that Redis Pub/Sub is unreliable and cannot guarantee successful deletion.
2. Introduce a professional distributed message queue (e.g., RocketMQ): Ensures message reliability, but increases system complexity.
3. Set appropriate expiration times as a fallback: Local cache can use a relatively short expiration time as a last line of defense.

#### 4. How do you handle hot keys?
**Answer:**
Handling hot keys critically depends on monitoring them. Monitoring can be done from: 1. Client-side: Set up a global dictionary on the client (tracking keys and call counts), and record using this dictionary every time a Redis command is called. 2. Proxy-side: Distributed Redis architectures based on proxies like Twemproxy or Codis handle all client requests through the proxy, allowing statistics to be collected at the proxy layer. 3. Redis Server: Use the MONITOR command to track hot keys. Once hot keys are detected, handling strategies include: 1. Scatter hot keys across different servers to reduce centralized pressure. 2. Add a secondary cache to load hot key data into memory in advance; if Redis crashes, degrade to querying local memory.

#### 5. How do you monitor and handle HotKey issues in Redis?
**Answer:**
Monitoring paths for HotKeys:
1. Client-side: Maintain a global dictionary in the client application to record key invocation counts.
2. Proxy-side: Use proxy-based architectures like Twemproxy or Codis to aggregate statistics at the proxy layer.
3. Redis Server: Use the MONITOR command to track all executed commands (beware of performance impact in production environments).
Methods to handle HotKeys:
1. Distribute/sharded hot keys across different servers to reduce single-node pressure.
2. Add multi-level caching (such as local caching) to preload hot key data into memory. If Redis goes down, gracefully fall back to querying the local cache.

#### 6. How does Redis Cluster scale (scale-out and scale-in)?
**Answer:**
Redis Cluster provides flexible node scaling solutions, allowing nodes to be added or removed without impacting external cluster service. Its core principle relies on the "mapping relationship between slots and nodes": scaling out and scaling in essentially means safely migrating a subset of slots and their corresponding data from source nodes to target nodes (new nodes or nodes slated for decommissioning).

#### 7. How does Redis implement distributed locks?
**Answer:**
Redis distributed locks essentially function by claiming a resource slot. 
V1: SETNX command. First-come, first-served, releasing via DEL when finished. Issue: If an exception occurs midway and DEL is never called, it causes a deadlock.
V2: Lock expiration. Attaching an expiration time (e.g., 5s) after acquiring the lock. Issue: SETNX and EXPIRE are two separate commands rather than atomic; if the service process crashes between them (e.g., power loss or kill), EXPIRE won't execute, still causing a deadlock.
V3: SET command with options. Redis 2.8 introduced extended parameters for the SET command, allowing SETNX and EXPIRE to execute atomically. In production, however, it is recommended to use a mature client library like Redisson.

#### 8. How does Redis utilize multithreading in Redis 6.0?
**Answer:**
In Redis 6.0, multithreading is used exclusively for handling network data reading/writing and protocol parsing, while specific command execution remains single-threaded. This design addresses the fact that Redis performance bottlenecks typically lie in network I/O rather than CPU. Introducing multithreading boosts I/O read/write efficiency, thereby enhancing overall Redis performance while avoiding the lock-contention complexity introduced by multithreaded concurrent data modifications.

#### 9. How does multi-threading work in Redis 6.0?
**Answer:**
In Redis 6.0, multi-threading is used to handle network data reading/writing and protocol parsing, while command execution remains single-threaded. This design is chosen because Redis's performance bottleneck typically lies in network I/O rather than CPU. Introducing multi-threading improves I/O read/write efficiency, thereby substantially boosting overall performance.

#### 10. How does the quorum journal manager work with fencing in distributed systems?
**Answer:**
To prevent split-brain scenarios, the journal manager uses epoch numbers—monotonically increasing integers that are assigned unique values upon state changes. A primary node generates epoch numbers and includes them in RPC requests to the Quorum Journal Manager (QJM). If a failover or restart occurs, the epoch number increases, and any older node with a lower epoch is fenced out and considered invalid.

#### 11. How is a Skip List implemented? What is its mechanism, and why does Redis use a Skip List instead of a Red-Black Tree to support Sorted Sets?
**Answer:**
A skip list is an ordered data structure that achieves fast element access by maintaining multiple forward pointers to other nodes inside each node. Regarding why balanced trees (like Red-Black Trees) are avoided: 1. Performance consideration: Under high concurrency, tree structures require complex rebalance operations that can affect the entire tree, whereas skip list modifications are often localized. 2. Implementation consideration: At similar complexity to Red-Black Trees, skip lists are simpler and more intuitive to implement, adapted by Redis from William Pugh's paper. Core node elements include: level (array generated via a power law randomly between 1 and 32; higher levels mean faster traversal), forward pointers (level[i].forward), span (records distance between nodes, used to calculate rank during traversal), score (double type, ordered ascending), and member object (obj property pointing to the string object holding the SDS value).

#### 12. How is a new master node elected in Redis Sentinel?
**Answer:**
Electing a new master node generally involves the following steps: 1. Filtering: Exclude 'unhealthy' nodes (subjectively offline, disconnected, nodes that haven't responded to Sentinel's ping within 5 seconds, or nodes disconnected from the master for longer than down-after-milliseconds * 10 seconds). 2. Select the replica with the highest slave-priority. If it exists, return; otherwise, continue. 3. Select the replica with the largest replication offset (most complete data replication). If it exists, return; otherwise, continue. 4. Select the replica with the lexicographically smallest runid.

#### 13. How is the Redis Sentinel Leader node elected?
**Answer:**
1. Every online Sentinel node is eligible to become the leader. When a Sentinel confirms that the master node is subjectively down, it sends a 'sentinel is-master-down-by-addr' command to other Sentinel nodes, requesting to be set as the leader.
2. A Sentinel node that receives the command will grant its vote if it has not already voted for another Sentinel in the same epoch; otherwise, it rejects the request.
3. If a Sentinel node finds that its vote count is greater than or equal to both the predefined 'quorum' and (num(sentinels)/2 + 1), it becomes the leader.
4. If no leader is successfully elected during the current round, the process repeats after a random time delay in the next epoch.

#### 14. How is the Redis dictionary implemented, and how does Rehash work?
**Answer:**
The dictionary is the most frequent composite data structure in a Redis server. Beyond hash-type values, the entire Redis database keys and values form a global dictionary, and keys with expiration times are also stored as a dictionary (within the RedisDb data structure). The dictionary structure is similar to Java's HashMap, using hashing and mathematical calculations to determine index positions, and resolves hash collisions via chaining using an array plus linked lists (separate chaining). How the dictionary expands: The dictionary structure internally contains two hash tables, ht[0] and ht[1]. Normally, only ht[0] has values. During expansion, the values in ht[0] are rehashed into ht[1], followed by incremental rehash. Incremental rehash means the rehash operation is not completed all at once or centrally, but performed in multiple steps and incrementally. After the migration ends, ht[1] takes over ht[0] to store dictionary elements.

#### 15. How is the dictionary (dict) implemented in Redis? How does Rehash work?
**Answer:**
The dictionary is the most frequent composite data structure in Redis. Aside from hash structures, the global key-value pairs of the entire Redis database as well as keys with expiration times are also implemented based on dictionaries.
Internal implementation: Similar to Java's HashMap, it uses an array plus linked lists (separate chaining) to resolve hash collisions.
Expansion and Incremental Rehash: A dictionary structure internally contains two hash tables, ht[0] and ht[1]. Normally, only ht[0] has values, and during expansion, values from ht[0] are rehashed into ht[1]. To avoid main thread blocking caused by a massive monolithic migration, Redis uses "incremental rehash", distributing migration operations across multiple steps. Once migration finishes, ht[1] replaces ht[0] as the new hash table.

#### 16. Suppose Redis has 100 million keys, with 100k keys matching a known prefix. How do you find them efficiently?
**Answer:**
Using the 'keys' command will scan for the pattern but blocks the main thread, causing a service outage until complete. Instead, use the 'SCAN' command, which provides non-blocking cursor-based iteration. SCAN may return duplicate keys requiring client-side deduplication, but it avoids thread starvation and service freezes.

#### 17. Under Redis Sentinel mode, how is a new master node elected?
**Answer:**
Selecting a new master node involves the following steps:
1. Filtering: Filter out "unhealthy" nodes (nodes marked as subjectively offline, disconnected, having failed to reply to Sentinel's PING response within 5 seconds, or out of contact with the master for longer than down-after-milliseconds * 10 seconds).
2. Priority: Select the replica with the highest slave-priority.
3. Offset: If priorities are identical, select the replica with the largest replication offset (most complete data).
4. RunID: If both of the above are identical, select the replica with the lexicographically smallest runid.

#### 18. What are common Redis performance issues and solutions?
**Answer:**
Common performance optimization recommendations include: 1. Master nodes should avoid persistence operations (such as RDB snapshots and AOF logs) where possible, specifically disabling RDB snapshots; 2. Critical data can be backed up by a Slave node running AOF (configured with `appendfsync everysec`); 3. Keep Slaves and Masters within the same local area network (LAN) to ensure fast replication speed and connection stability; 4. Avoid adding new slave nodes during periods of high master database load; 5. Be aware that `BGREWRITEAOF` consumes significant CPU and memory resources, potentially causing temporary service pauses; 6. Prefer unidirectional linear master-slave architectures and avoid complex graph topologies to maintain stability.

#### 19. What are the architectural limitations of Redis master-slave replication?
**Answer:**
1. Failover requires manual intervention to promote a slave, update application connection strings, and reconfigure other slaves (unless Sentinel or Cluster is used).
2. Master write capability is limited by a single machine's resources.
3. Master storage capacity is limited by a single machine's RAM.
The first issue pertains to High Availability, while the latter two are distributed scaling limitations.

#### 20. What are the common causes of Redis blocking and how can they be diagnosed and resolved?
**Answer:**
Primary causes include: 1. Improper API or data structure usage (e.g., executing O(N) complexity commands on large objects). Diagnostics: Use `slowlog get {n}` to identify slow queries; optimize inefficient commands (e.g., replacing `HGETALL` with `HMGET`, banning `KEYS`) or split large objects. 2. CPU Saturation: Single-threaded OPS reaches its limits. Diagnostics: Use `redis-cli --stat` to check usage. Scale out via clustering for high concurrency, or check persistence overhead. 3. Persistence Blocking: Includes fork blocking (main thread takes too long to fork during RDB/AOF rewrites), AOF fsync blocking (fsync thread lags and stalls the main thread), and Transparent HugePages (THP) memory copy expansion (allocating 2MB pages instead of 4KB amplifies copy-on-write latency).

#### 21. What are the common data partitioning strategies in distributed clusters, and what are their respective pros and cons?
**Answer:**
Common data partitioning strategies include:
1. Modulo Partitioning (Node Modulo): Takes the hash value of a specific piece of data (such as a key or user ID) and applies modulo: hash(key) % N. Pros: Very easy to understand and implement. Cons: When the number of nodes changes (scaling out or in), data-to-node mapping relationships must be recalculated, leading to massive data re-migration.
2. Consistent Hashing: Organizes the entire hash space into a virtual ring, hashes the IP or hostname of cache nodes, and places them on the ring. A key is hashed to locate its position on the ring, and moving clockwise, the first cache node encountered is the target node. This resolves some scaling pain points.
3. Virtual Slot Partitioning: Introduces the concept of virtual nodes (such as the slots in Redis Cluster) on top of consistent hashing. Slots are a virtual layer between data and physical nodes. Each physical node holds a specific number of slots, and data whose hash falls within a specific range maps to the corresponding slot.

#### 22. What are the core architectural components of Apache Spark?
**Answer:**
• Driver Program: Uses a SparkContext object (entry point) to connect to the cluster, construct the DAG, split jobs into tasks, launch executors on worker nodes, and distribute application code. • Executor: A dedicated JVM process running on worker nodes that executes tasks assigned by the driver and caches data in memory or disk. • Task: The fundamental unit of data processing work executed by an executor.

#### 23. What are the core underlying data structures of Redis?
**Answer:**
Redis underlying structures include: 1. SDS (Simple Dynamic String): Records length info, lowering length lookup complexity to O(1) and preventing buffer overflows. 2. linkedlist: Doubly linked circular list. 3. dict (Dictionary/Hash Table): Resolves collisions using separate chaining and incremental rehash. 4. skiplist: One of the underlying implementations of sorted sets, with random heights ranging from 1 to 32. 5. intset (Integer Set): An array storing integer values. 6. ziplist: A sequential data structure engineered for memory efficiency.

#### 24. What are the hazards of BigKeys in Redis, and how do you discover and handle them?
**Answer:**
A BigKey manifests when a single string value is too large (size > 10KB), or hash, set, zset, and list collections store too many elements (in the tens of thousands).
Hazards:
1. Increased client latency or timeouts.
2. IO operations on BigKeys heavily consume bandwidth and CPU.
3. Causes Redis cluster data skew.
4. Deletion (active or passive) can cause blocking.
Discovery methods:
1. bigkeys command: Iterates and analyzes all keys in the instance, returning overall statistics and the Top 1 key for each data type.
2. redis-rdb-tools: A Python-based tool for analyzing RDB snapshot files.
Handling strategies:
1. Deleting BigKeys: Redis >= 4.0 can use the UNLINK command for safe non-blocking deletion; Redis < 4.0 should use the SCAN command for incremental iteration scanning and deletion.
2. Compression and splitting: Serialize/compress string data, or split into multiple keys using mget; shard collection types based on estimated size.

#### 25. What are the implementation principles and core periodic tasks of Redis Sentinel?
**Answer:**
Sentinel mode uses sentinel nodes to complete the monitoring, offline detection, and failover of data nodes. It mainly includes three periodic monitoring tasks: 1. Every 10 seconds, each Sentinel node sends an 'info' command to the master and slave nodes to obtain the latest topology structure. 2. Every 2 seconds, each Sentinel node sends its own assessment of the master node and its own information to the 'sentinel:hello' channel of the Redis data nodes. 3. Every 1 second, each Sentinel node sends a 'ping' command to the master node, slave nodes, and other Sentinel nodes to perform a heartbeat check to confirm whether these nodes are currently reachable.

#### 26. What do you know about Redis Pipelining?
**Answer:**
Redis provides three mechanisms to batch multiple client commands for server-side execution: Pipelining, Transactions, and Lua Scripts. Pipelining is the simplest, allowing clients to send multiple commands to the server in a single batch. The server buffers the results and returns them all at once after the final command executes.
Advantages:
1. Saves RTT (Round Trip Time): Reduces network round-trips between client and server.
2. Reduces context switching: Merges multiple user-space to kernel-space system calls, lowering overhead.

#### 27. What is Redis Cluster and what are its core features?
**Answer:**
1. Data Partitioning (Sharding): The core feature of the cluster, distributing data across multiple nodes to bypass single-machine memory limitations and significantly increase storage capacity; every master node handles read and write operations, boosting cluster throughput.
2. High Availability: Supports master-slave replication and automatic master failover (similar to Sentinel), ensuring the cluster continues to function if any node fails.

#### 28. What is Redis Pipelining?
**Answer:**
Redis offers three ways to bundle and send multiple client commands to the server for execution: Pipelining, Transactions, and Lua Scripts. Pipelining is the simplest batching method, where the client sends multiple commands at once, with its core objective being to minimize the impact of RTT (Round Trip Time) on performance. Advantages: 1. Saves RTT: Reduces the number of network round trips between the client and server. 2. Reduces context switching: Minimizes system call overhead when programs switch from user mode to kernel mode.

#### 29. What is Redis Sentinel and how does it provide high availability?
**Answer:**
Redis Sentinel is a distributed monitoring and failover system for Redis deployments. It monitors master and replica instances, performs automatic failover by promoting a replica to master if the original master fails, and acts as a configuration provider for clients.

#### 30. What is Redis and what are its core features?
**Answer:**
Redis is an in-memory key-value NoSQL database.
- Rich Data Structures: Values support String, Hash, List, Set, Zset, Bitmaps, HyperLogLog, and GEO, satisfying diverse business scenarios.
- Extreme Performance: All data resides in memory, delivering extremely high read and write performance.
- Data Persistence: Supports saving in-memory data to disk asynchronously or synchronously via RDB snapshots and AOF logs, ensuring data durability during power outages or machine failures.

#### 31. What is a Bloom Filter? What is its core principle, along with its pros and cons?
**Answer:**
A Bloom Filter is an efficient data structure composed of a contiguous binary array (bit array, initially all 0s) and K independent hash functions, used to test whether an element is a member of a set.
- Principle: When storing, K hash functions map the element to K positions in the bit array and set them to 1. When querying, the same K hash functions check if the corresponding bits are all 1. If all are 1, the element is "possibly present". If any bit is not 1, it is "definitely not present".
- Pros: Space efficiency and query time far exceed typical algorithms.
- Cons:
  1. Subject to a certain false positive rate because hash collisions cannot be completely avoided.
  2. Deletion is not supported by default, as multiple elements may share the same bit positions.

#### 32. What is cache warming, and what are some commonly used implementation methods?
**Answer:**
Cache warming refers to preloading hot data from the database into the cache before system launch or restart, preventing a massive wave of requests from hitting the database directly during a cold start. Common methods: 1. Write a dedicated cache refresh page or management backend API to manually trigger warming upon deployment. 2. For smaller data volumes, use ApplicationRunner or InitializingBean interfaces to automatically load data when the project starts. 3. Periodically refresh the cache using scheduled tasks (such as Cron jobs).

#### 33. What is the Failover process of Redis Sentinel?
**Answer:**
1. Sentinel nodes elect a leader Sentinel node via the Raft algorithm to perform the failover work. 2. A node is selected from the slave node list to become the new master node. 3. The Sentinel leader node executes the 'slaveof no one' command on the selected slave node to make it a master node. 4. The Sentinel leader node sends commands to the remaining slave nodes to make them follow the new master node. 5. The Sentinel node collection updates the original master node to a slave node and continues to monitor it, commanding it to replicate from the new master node once it recovers.

#### 34. What is the Redis big key problem? Include its hazards, detection methods, and handling strategies.
**Answer:**
A big key occurs when a single key has an excessively large value (e.g., a string size exceeding 10KB) or when collection types like hash, set, zset, or list store an extremely large number of elements (tens of thousands or more).
Hazards of big keys:
1. Increased client latency, potentially causing timeouts.
2. I/O operations on big keys severely consume bandwidth and CPU.
3. Data skew across the Redis cluster.
4. Blocking of the event loop during active or passive deletion.
How to find big keys:
1. bigkeys command: Iterates through all keys in a Redis instance, returning overall statistics and the top largest key for each data type.
2. redis-rdb-tools: A Python tool used to analyze Redis RDB snapshot files, capable of generating JSON files or analysis reports.
How to handle big keys:
1. Deleting big keys: For Redis 4.0 and above, use the UNLINK command to asynchronously and safely reclaim memory in a non-blocking way; for versions below 4.0, it is recommended to use the SCAN command to incrementally iterate and delete keys.
2. Compression and splitting: For string values, control the size using serialization and compression algorithms, or split them into parts and use operations like MGET for transactional reading; for collection types, perform sharding based on estimated data scale.

#### 35. What is the cache "bottomless pit" phenomenon, and how can it be resolved?
**Answer:**
The bottomless pit phenomenon refers to the situation where, as distributed cache nodes (such as Memcached/Redis) are continuously added for horizontal scaling to meet growing business demands, cluster performance drops instead of increasing. Cause: Key-value pairs are mapped to various nodes via hash functions, requiring distributed batch operations (such as MGET) to fetch across multiple network nodes. As nodes increase, network round-trips and latency continuously grow. Optimization ideas: 1. Optimize commands themselves to reduce unnecessary batch operations. 2. Reduce network communication rounds by using persistent connections, connection pools, and NIO technologies.

#### 36. What is the core principle of Redis Cluster? How many physical nodes are required for a cluster deployment at minimum?
**Answer:**
Redis Cluster achieves distributed storage and high availability through data partitioning (16384 hash slots) and automatic failover. Nodes communicate and discover failures via the Gossip protocol (Ping/Pong messages). When more than half of the master nodes holding slots mark a node as subjectively offline (pfail), it triggers objectively offline status and initiates master-slave Failover. To avoid single points of failure and split-brain scenarios where it cannot satisfy the N/2+1 voting requirement, master nodes must be deployed across at least 3 distinct physical machines.

#### 37. What is the difference between Redis Subjective Down (SDOWN) and Objective Down (ODOWN)?
**Answer:**
1. Subjective Down (SDOWN): Every Sentinel node sends 'ping' commands to the master, slaves, and other Sentinel nodes every 1 second for heartbeat checks. When these nodes fail to effectively respond for longer than 'down-after-milliseconds', the Sentinel node makes a failure determination for that node. 2. Objective Down (ODOWN): When the node judged as SDOWN by a Sentinel is the master node, this Sentinel node queries other Sentinels regarding their judgment of the master using the 'sentinel is-master-down-by-addr' command. When a specified quorum of Sentinel nodes agree that the master has issues, the Sentinel node makes an Objective Down decision.

#### 38. What is the evolution process and final recommended solution for implementing distributed locks in Redis?
**Answer:**
1. V1 (SETNX): Uses SETNX to acquire the lock and DEL to release. Flaw: If an exception occurs before DEL, a permanent deadlock results.
2. V2 (Lock timeout release): Acquires the lock then sets an EXPIRE timeout. Flaw: The gap between SETNX and EXPIRE is not atomic; if the process crashes between commands, a deadlock still occurs.
3. V3 (SET command with extended options): Introduced in Redis 2.8, combining SETNX and EXPIRE into a single atomic instruction. For production environments, mature client libraries like Redisson are strongly recommended.

#### 39. What is the principle behind Redis Cluster scaling (expansion and contraction)?
**Answer:**
Redis Cluster achieves smooth scaling through flexible node addition and removal without disrupting external services. The core of scaling lies in the 'mapping relationship between slots and nodes': Expansion or contraction fundamentally involves migrating a subset of slots and their corresponding data from source nodes to target nodes (new nodes).

#### 40. What is the quicklist data structure in Redis?
**Answer:**
Early versions of Redis used ziplist (ziplist) and standard linked lists (linkedlist) to store list data structures; that is, ziplist was used when there were few elements, and linkedlist when there were many. However, considering that the pointer overhead of a linked list is relatively high (on 64-bit operating systems, prev and next pointers take 16 bytes), and the memory of each node is allocated independently, it causes memory fragmentation and impacts memory management efficiency. Later, new versions of Redis (3.2) redesigned the list data structure, using quicklist to replace ziplist and linkedlist. Quicklist is a new data structure introduced by balancing time and space efficiency, consisting of a combination of lists and ziplists—a doubly linked list whose nodes are ziplists.

#### 41. Why did Redis choose a single-threaded model in its early stages?
**Answer:**
The bottleneck in Redis is rarely CPU bound; instead, it is constrained by memory and network bandwidth. The single-threaded model avoids unnecessary thread context switching and lock contention overhead introduced by multithreading, simplifying the implementation of data structures and algorithms. Furthermore, background threads were introduced starting in Redis 4.0 (for tasks like lazy-free dirty data cleaning, connection release, and large key deletion), and Redis 6.0 introduced multithreaded network I/O (I/O threading).

