# 04_Redis_Caching - Redis & In-Memory Caching Architecture Study Guide

- **Total Cards**: 151

---

## 📂 Category: Architecture (2 cards)

### 🔴 Senior Level

#### 1. Compare single-cluster and multi-cluster caching and data system architectures in terms of fault tolerance and scalability.
**Answer:**
• Single Cluster: Easier to manage with centralized operations, but more vulnerable to system-wide failures, bottlenecks, and scalability limits. • Multi-Cluster: Offers better fault isolation and scalability by separating workloads and partitioning availability zones, though it increases operational complexity, network overhead, and infrastructure cost.

#### 2. Redis 6.0 使用多线程是怎么回事？
**Answer:**
Redis 6.0 的多线程用于处理网络数据的读写和协议解析，但执行具体命令仍然是单线程的。这样做的原因是 Redis 的性能瓶颈主要在于网络 IO 而非 CPU，引入多线程可以提升 IO 读写的效率，从而整体提升 Redis 性能，同时避免了多线程并发修改数据带来的锁竞争复杂性。


## 📂 Category: Architecture & Performance (2 cards)

### 🟢 Junior Level

#### 1. Redis为什么快呢
**Answer:**
1. 完全基于内存操作。
2. 使用单线程模型，避免了线程切换和竞态产生的消耗。
3. 基于非阻塞的I/O多路复用机制。
4. C语言实现，优化过的数据结构。Redis做了大量底层性能优化，基于多种基础数据结构性能极佳。


### 🔴 Senior Level

#### 1. Redis阻塞？怎么解决？
**Answer:**
1. API或数据结构使用不合理：高并发场景应避免在大对象上执行算法复杂度超过O(N)的命令。
   - 发现慢查询：使用 slowlog get {n} 获取最近的n条慢查询命令。
   - 优化方法：修改为低复杂度命令（如hgetall改为hmget，禁用keys、sort），或缩减/拆分大对象。
2. CPU饱和问题：单线程Redis处理命令只能使用一个CPU。OPS达到极限时应做集群化水平扩展分担OPS压力；若OPS不高需排查命令和内存持久化相关的阻塞。
3. 持久化相关阻塞：
   - fork阻塞：RDB和AOF重写时主线程调用fork产生共享内存的子进程，若fork耗时过长会导致主线程阻塞。
   - AOF刷盘阻塞：当AOF采用每秒刷盘（fsync）时，若磁盘压力过大导致fsync需要等待，主线程发现距离上一次fsync超过2秒会阻塞等待。
   - HugePage写操作阻塞：开启Transparent HugePages的操作系统，每次写命令引起的复制内存页单位由4K变为2MB，放大512倍，会拖慢写操作执行时间。


## 📂 Category: Architecture & Use Cases (1 cards)

### 🟢 Junior Level

#### 1. Redis 可以用来干什么（主要应用场景有哪些）？
**Answer:**
1. 缓存：通过减少数据库访问次数提高系统响应速度。
2. 会话存储：提供快速的会话读写，提高用户体验。
3. 消息队列：通过异步处理增加系统的可扩展性和解耦性。
4. 实时分析：在内存中对复杂数据进行实时处理。
5. 排行榜和计数器：利用有序集合（ZSet）等快速更新和检索排行榜信息。
6. 发布和订阅：构建实时消息系统，如实时通知。


## 📂 Category: Big Data Architecture (4 cards)

### 🟢 Junior Level

#### 1. What is Apache Hive and its primary use case?
**Answer:**
Hive is a data warehousing tool built on top of Hadoop. It is used to analyze large datasets and load structured data into Hive tables to execute queries and run analysis tasks.

#### 2. What is Apache Spark and what components make up its ecosystem?
**Answer:**
Spark is an open-source computational framework that processes and analyzes huge amounts of data using commodity servers. Its ecosystem includes Apache Spark Core, Spark SQL, Spark Streaming, Spark MLlib, Spark GraphX, and SparkR, supporting batch, streaming, machine learning, and graph processing.

#### 3. What is Hadoop and what are its core architectural components?
**Answer:**
Hadoop is an open-source distributed processing framework that manages data processing and storage for big data applications in clusters. It consists of a Master/Slave architecture where it uses HDFS (Hadoop Distributed File System) for storage and YARN (Yet Another Resource Negotiator) for data processing.


### 🔴 Senior Level

#### 1. How does Apache Hive execute a query internally?
**Answer:**
Step 1: executeQuery: The user interface calls the execute interface to the driver.
Step 2: get Plan: The driver accepts the query, creates a session handle for the query, and passes the query to the compiler for generating the execution plan.
Step 3: getMetaData: The compiler sends the metadata request to the metastore.
Step 4: send metadata: The metastore sends the metadata to the compiler for type-checking and semantic analysis, generating a Directed Acyclic Graph (DAG) for MapReduce.
Step 5: send Plan: The compiler sends the execution plan to the driver.
Step 6: execute the plan: The driver sends the execution plan to the execution engine.
Step 7: Submit a job to MapReduce: The execution engine executes mapper/reducer operator trees, reading/writing via deserializers/serializers in HDFS.
Step 8: sendResult: The engine reads temporary files and sends results back to the Hive interface.


## 📂 Category: Cache Consistency (1 cards)

### 🔴 Senior Level

#### 1. 如何保证缓存和数据库(DB)数据的最终一致性？
**Answer:**
常见策略与方案包括：
1. 选择合适的更新策略：优先采用“先删除缓存，再更新数据库”或“先更新数据库，再删除缓存”。推荐“删缓存而不是更新缓存”，因为更新缓存开销大且易产生脏数据。
2. 延时双删：在删除缓存并更新数据库后，间隔一段时间再次删除缓存，以防止并发写导致的脏数据。
3. 消息队列重试机制：将删除失败的 key 写入消息队列，利用队列的重试机制确保 key 被最终删除。
4. 数据库 binlog 订阅：使用类似 Canal 监听数据库 binlog，通过消费订阅日志异步删除缓存，降低业务侵入性（但提升了系统复杂度）。
5. 设置过期时间兜底：给缓存设置合理的 TTL，即使发生不一致，过期后也能自动恢复一致。


## 📂 Category: Cache Design & Patterns (2 cards)

### 🟢 Junior Level

#### 1. 什么是缓存预热？有哪些常用的实现方式？
**Answer:**
缓存预热是指在系统上线或重启前，提前将数据库中的热点数据加载到缓存中，避免冷启动时大量请求直接打到数据库。
常用方法：
1. 编写专门的缓存刷新页面或管理端接口，上线时手动触发。
2. 数据量较小时，在项目启动时通过实现ApplicationRunner或InitializingBean接口自动加载。
3. 通过定时任务（如Cron Job）定期刷新缓存。


### 🔴 Senior Level

#### 1. 什么是热点key重建问题？会带来什么影响？有哪些解决方案？
**Answer:**
当一个高并发访问的热点key在缓存失效的瞬间，由于重建缓存的操作耗时较长（如复杂SQL、多次IO等），大量线程同时去重建缓存，会导致后端数据库负载激增甚至应用崩溃。
解决方案：
1. 互斥锁（Mutex Key）：只允许一个线程重建缓存，其他线程等待重建完成后重新获取缓存。
2. 永远不过期（逻辑过期）：物理缓存不设置过期时间，为每个value设置逻辑过期时间，当发现超过逻辑过期时间时，使用独立异步线程去构建缓存。


## 📂 Category: Caching Architecture (3 cards)

### 🟢 Junior Level

#### 1. What is Apache Redis and in-memory caching?
**Answer:**
Redis is an open-source, in-memory data structure store used as a database, cache, message broker, and streaming engine. In-memory caching stores frequently accessed data in RAM to drastically reduce read latency and database load compared to disk-based storage.


### 🟡 Mid Level

#### 1. 如何保证缓存和数据库（DB）数据的一致性？
**Answer:**
根据 CAP 理论，在保证可用性和分区容错性的前提下，无法保证强一致性。因此缓存和数据库的绝对一致是不可能实现的，只能通过合理的策略（如 Cache Aside 模式、延时双删等）尽可能保证缓存和数据库的最终一致性。


### 🔴 Senior Level

#### 1. 如何保证本地缓存和分布式缓存的一致性？
**Answer:**
可以采用以下几种方式：
1. 采用 Redis 的 Pub/Sub 机制：分布式集群的所有节点订阅删除本地缓存频道，当删除 Redis 缓存节点时，同时发布删除本地缓存消息，订阅者收到消息后删除对应的本地 key。缺点是 Redis 的发布订阅是不可靠的，不能保证一定删除成功。
2. 引入专业的分布式消息队列（如 RocketMQ）：保证消息的可靠性，但增加了系统复杂度。
3. 设置合适的过期时间兜底：本地缓存可以设置相对短一些的过期时间作为最终防线。


## 📂 Category: Caching Architecture & Resilience (1 cards)

### 🔴 Senior Level

#### 1. What are cache stampede, cache penetration, and cache avalanche, and how do you mitigate them?
**Answer:**
Cache Stampede (Breakdown): High-traffic key expires simultaneously, hitting the DB. Mitigation: Mutex locks on cache miss or asynchronous background refresh.
Cache Penetration: Queries for non-existent data in both cache and DB, bypassing the cache layer. Mitigation: Cache null/default values with short TTLs or use a Bloom filter.
Cache Avalanche: Mass expiration or crash of cache instances at the same time, flooding the DB. Mitigation: Cluster deployment, multi-level caching, randomized TTL jitter, and permanent retention for ultra-hot keys, along with service circuit-breaking and fallback mechanisms.


## 📂 Category: Cluster & Replication (1 cards)

### 🟡 Mid Level

#### 1. Redis 集群中数据是如何分区的？有哪些常见方案？
**Answer:**
常见的数据分区方案有三种：1. 节点取余分区：使用特定的数据（如键或用户 ID）对哈希值取余 hash(key)%N 来决定映射到哪个节点。缺点是当节点数量变化（扩容或缩容）时，数据映射关系需要重新计算，导致大规模数据迁移。2. 一致性哈希分区：将整个 Hash 值空间组织成一个虚拟圆环，将缓存节点的 IP 或主机名做 Hash 后放置在环上。Key 做同样的 Hash 确定位置后，顺时针方向遇到的第一个缓存节点即为目标节点。3. 虚拟槽分区（Virtual Slot）：在一致性哈希基础上引入虚拟节点概念，Redis 集群采用此方案。其中的虚拟节点称为“槽”（slot，共 16384 个），槽是介于数据和实际节点之间的虚拟概念，每个实际节点包含一定数量的槽。


## 📂 Category: Cluster Architecture (1 cards)

### 🔴 Senior Level

#### 1. How does an active-active Kafka cluster operate?
**Answer:**
An active-active cluster comprises two homogeneous Kafka clusters that perform bi‑directional, asynchronous mirroring. Both clusters actively serve client requests, ensuring high availability while balancing load and minimizing access delays.


## 📂 Category: Cluster Metadata (2 cards)

### 🟡 Mid Level

#### 1. What does membership management entail in ZooKeeper?
**Answer:**
Membership management involves tracking which nodes (e.g., Kafka brokers) are connected to the ZooKeeper ensemble. ZooKeeper updates its records as nodes join or leave, thereby maintaining an accurate view of the cluster’s state.


### 🔴 Senior Level

#### 1. What does KRaft stand for and why was it introduced in Kafka?
**Answer:**
KRaft stands for Kafka Raft. It was introduced to eliminate Kafka’s dependency on ZooKeeper by replacing a single controller with a distributed quorum of controllers. This change aims to improve fault tolerance, simplify configuration management, and reduce operational overhead.


## 📂 Category: Cluster Operations (1 cards)

### 🟡 Mid Level

#### 1. What challenges are associated with Kafka?
**Answer:**
Despite its high performance and scalability, Kafka has a steep learning curve. Configuring and managing a Kafka cluster can be complex, and developers must carefully design their applications to handle issues like partitioning, replication, and consumer rebalancing.


## 📂 Category: Cluster Topology (2 cards)

### 🟢 Junior Level

#### 1. What defines a Single Kafka Cluster architecture?
**Answer:**
A Single Kafka Cluster architecture centralizes all brokers, metadata, topics, and partitions within one unified system. It is simpler to deploy and manage but may encounter scalability and fault tolerance issues as the workload grows.


### 🔴 Senior Level

#### 1. What characterizes a Multiple Kafka Cluster architecture?
**Answer:**
In a Multiple Kafka Cluster architecture, workloads are distributed across separate clusters. This decentralized approach enhances fault tolerance and scalability by isolating data streams, though it increases configuration and operational complexity.


## 📂 Category: Clustering & Scaling (2 cards)

### 🟡 Mid Level

#### 1. Redis 集群了解吗
**Answer:**
1. 数据分区（数据分片）：集群的核心功能，将数据分散到多个节点，突破单机内存限制，大幅增加存储容量；每个主节点都可对外提供读写服务，大大提高集群响应能力。
2. 高可用：集群支持主从复制和主节点自动故障转移（与哨兵类似），任一节点发生故障时，集群依然可以对外提供服务。


### 🔴 Senior Level

#### 1. Explain Redis Cluster architecture and data sharding mechanism.
**Answer:**
Redis Cluster provides automatic sharding across multiple nodes using a 16384 hash slot space. Every key is mapped to a hash slot using the formula CRC16(key) % 16384. Nodes in the cluster manage subsets of these slots, enabling horizontal scaling and high availability via master-replica setups.


## 📂 Category: Consumer Groups (4 cards)

### 🟢 Junior Level

#### 1. What happens when the number of partitions is greater than the number of consumers in a group?
**Answer:**
When there are more partitions than consumers, the available partitions are divided among the consumers. This means one consumer might be assigned multiple partitions, enabling the group to process more messages concurrently.

#### 2. What is a consumer group and how does it function with Kafka topics?
**Answer:**
A consumer group is a collection of consumers that work together to process messages from Kafka topics. The partitions of a topic are distributed among the consumers in the group, ensuring that each message is processed by only one consumer. This design provides scalability and fault tolerance, as the workload can be rebalanced if consumers join or leave.


### 🟡 Mid Level

#### 1. How do range and round-robin assignors work in consumer partition assignment?
**Answer:**
The range assignor divides the list of partitions into contiguous ranges, assigning each range to a consumer (with the first few consumers getting an extra partition if not evenly divisible). The Round Robin strategy collects all available partitions into a single list and assigns them one by one to consumers in a cyclic order for a more balanced distribution.

#### 2. What are the two common partition assignment strategies in Kafka consumer groups?
**Answer:**
The two common strategies are: Range: Assigns consecutive partitions to each consumer. Round Robin: Distributes partitions evenly by cycling through the list of consumers, assigning one partition at a time.


## 📂 Category: Consumer Groups & Delivery Semantics (1 cards)

### 🟡 Mid Level

#### 1. How does the "at least once" delivery guarantee work in relation to consumer groups and offset commits?
**Answer:**
Each consumer group tracks its own set of committed offsets. For "at least once" delivery, consumers commit offsets only *after* they have processed messages. This minimizes the risk of missing data, though a failure after processing and before committing may cause some messages to be reprocessed upon recovery.


## 📂 Category: Coordination Services (2 cards)

### 🟢 Junior Level

#### 1. What is a ZooKeeper ensemble?
**Answer:**
An ensemble is a group of ZooKeeper server nodes (typically at least three) that work together to maintain replicated data and provide fault tolerance. The ensemble ensures that the coordination service remains operational even if one or more nodes fail.


### 🟡 Mid Level

#### 1. What is lock management in ZooKeeper and why is it critical?
**Answer:**
Lock management in ZooKeeper prevents simultaneous modifications of shared resources. By enforcing mutual exclusion through distributed locks, ZooKeeper helps avoid data corruption or loss in concurrent distributed environments.


## 📂 Category: Core Concepts (1 cards)

### 🟢 Junior Level

#### 1. 什么是Redis？它有哪些核心特点？
**Answer:**
Redis是一种基于键值对（key-value）的NoSQL内存数据库。
- 丰富的数据结构：value支持String（字符串）、Hash（哈希）、List（列表）、Set（集合）、Zset（有序集合）、Bitmaps（位图）、HyperLogLog、GEO（地理信息定位）等，满足多样化业务场景。
- 极致的性能：所有数据存放在内存中，读写性能极高。
- 数据持久化：支持将内存中的数据通过RDB快照和AOF日志异步/同步保存到磁盘上，保证断电或机器故障时数据不丢失。


## 📂 Category: Core Internals (1 cards)

### 🔴 Senior Level

#### 1. Redis 为什么早期选择单线程？
**Answer:**
Redis 的瓶颈往往不在 CPU，而是在内存和网络带宽。单线程避免了不必要的线程上下文切换和多线程竞争带来的锁开销，简化了数据结构和算法的实现。同时，Redis 4.0 之后开始引入多线程（如后台线程用于清理脏数据、无连接释放、大 Key 删除等），在 6.0 中引入了多线程处理网络 IO（I/O threading）。


## 📂 Category: Data Integration (2 cards)

### 🟢 Junior Level

#### 1. What is Sqoop2 and what is its primary use case?
**Answer:**
Sqoop is a bulk data transfer tool. Sqoop2 allows the import and export of data between structured datastores (relational databases, enterprise data warehouses, NoSQL systems) and HDFS, as well as populating tables in Hive and HBase.


### 🟡 Mid Level

#### 1. How do distributed import/export tools (like Sqoop) handle parallel data transfer between RDBMS and distributed filesystems?
**Answer:**
• Import Tool: Splits the RDBMS table import into parallel subtasks mapped to map tasks. Each map task concurrently fetches a specific chunk/range of the dataset, collectively loading the entire table into the distributed filesystem. • Export Tool: Maps an HDFS file dataset into parallel map tasks, where each task reads a chunk of data from storage and bulk-inserts or loads it into the target structured RDBMS.


## 📂 Category: Data Structures (5 cards)

### 🟡 Mid Level

#### 1. Redis 的 SDS 和 C 中字符串相比有什么优势？
**Answer:**
C 语言使用长度为 N+1 的字符数组且以 \0 结尾，存在获取长度 O(n)、无法杜绝缓冲区溢出、不能保存二进制数据等问题。Redis 的 SDS（Simple Dynamic String）优势包括：1. O(1) 复杂度获取字符串长度（内部维护 len 属性）；2. 自动扩展空间，避免缓冲区溢出；3. 有效降低内存分配次数（通过空间预分配和惰性空间释放机制）；4. 二进制安全，可保存任意二进制数据。

#### 2. 压缩列表（ziplist）了解吗？其内部结构是如何组成的？
**Answer:**
压缩列表是 Redis 为了节约内存而开发的一种顺序型数据结构，由一系列特殊编码的连续内存块组成。它可以包含任意多个节点（entry），每个节点可以保存一个字节数组或者一个整数值。
压缩列表的组成部分主要包括：
- zlbytes：记录整个压缩列表占用的内存字节数。
- zltail：记录压缩列表表尾节点距离压缩列表的起始地址有多少字节。
- zllen：记录压缩列表包含的节点数量。
- entryX：列表节点。
- zlend：用于标记压缩列表的末端。

#### 3. 快速列表（quicklist）了解吗？它解决了什么问题？
**Answer:**
Redis 早期版本存储 list 列表数据结构使用的是压缩列表 ziplist 和普通的双向链表 linkedlist。但链表的附加空间相对较高（64位系统下 prev 和 next 指针占用 16 字节），且每个节点的内存都是单独分配的，容易造成内存碎片。
因此 Redis 3.2 引入了 quicklist 代替 ziplist 和 linkedlist。quicklist 是综合考虑了时间效率与空间效率引入的新型数据结构，本质上是一个由 ziplist 充当节点的双向链表。


### 🔴 Senior Level

#### 1. 字典（dict）是如何实现的？Rehash 是怎么进行的？
**Answer:**
字典是 Redis 中最为频繁的复合型数据结构，除了 hash 结构外，整个 Redis 数据库的全局键值对以及带过期时间的 key 也都基于字典实现。
内部实现：类似于 Java 的 HashMap，采用“数组 + 链表”的链地址法解决哈希冲突。
扩容与渐进式 Rehash：字典结构内部包含两个哈希表 ht[0] 和 ht[1]。通常情况下只有 ht[0] 有值，扩容时将 ht[0] 的值 rehash 到 ht[1]。为了避免一次性集中迁移造成主线程阻塞，Redis 采用“渐进式 rehash”，将迁移操作分多次、渐进式地完成。搬迁结束后，ht[1] 取代 ht[0] 成为新的哈希表。

#### 2. 跳跃表是如何实现的？原理是什么？为什么 Redis 使用跳跃表而不是红黑树来支持 Sorted Set？
**Answer:**
跳跃表（skiplist）是一种有序数据结构，通过在每个节点中维持多个指向其他节点的指针来达到快速访问节点的目的。针对为什么不用红黑树/平衡树：1. 性能考量：在高并发情况下，树形结构需要执行复杂的 rebalance 操作，可能涉及整树的操作，而跳跃表的变动通常只涉及局部；2. 实现考量：在复杂度与红黑树相同的情况下，跳跃表实现起来更简单直观。Redis 基于 William Pugh 的论文做了改进。节点核心元素包含：层（level数组，通过幂次定律随机生成1到32之间的值作为高度，层数越多访问越快）、前进指针（level[i].forward）、跨度（span，用于记录两个节点间的距离，遍历时累加跨度可计算 rank 排名）、分值（score属性，double类型，从小到大排序）和成员对象（obj属性，指向保存 SDS 值的字符串对象）。


## 📂 Category: Data Structures & Algorithms (2 cards)

### 🟡 Mid Level

#### 1. 什么是布隆过滤器（Bloom Filter）？它的核心原理和优缺点是什么？
**Answer:**
布隆过滤器是一个由连续的二进制位（bit数组，初始全为0）和K个独立哈希函数组成的高效数据结构，用于检索一个元素是否在一个集合中。
- 原理：存储时，用K个哈希函数将元素映射到位数组的K个点并置为1；判断时，同样通过K个哈希函数检查对应点是否全为1。若全为1，则元素“可能存在”；若有一个不为1，则“一定不存在”。
- 优点：空间效率和查询时间都远远超过一般的算法。
- 缺点：
  1. 存在一定的误判率（False Positive），因为哈希碰撞无法完全避免。
  2. 默认不支持删除元素（Deletion），因为多个元素可能会共享相同的bit位。


### 🔴 Senior Level

#### 1. 请详细介绍Redis底层的6大核心数据结构
**Answer:**
1. 动态字符串（SDS）：C语言传统字符串的包装。不仅记录长度信息（使获取长度时间复杂度从O(N)降为O(1)），还能避免缓冲区溢出，减少修改字符串时的内存重分配次数。
2. 双向链表（linkedlist）：带有表头和表尾指针的双向环形链表，用于实现发布订阅、慢查询、监视器等功能。
3. 字典（dict）：由哈希表实现，内部包含两个哈希表（用于平滑rehash），采用链地址法解决键冲突，rehash过程是渐进式的以保证服务可用性。
4. 跳跃表（skiplist）：有序集合的底层实现之一，由zskiplist和zskiplistNode组成，层高1-32随机数，支持平均O(log N)复杂度的节点查找。
5. 整数集合（intset）：用于保存整数值的集合抽象数据结构，底层实现为数组，不包含重复元素。
6. 压缩列表（ziplist）：为节约内存而开发的顺序性数据结构，由连续内存块组成，可保存任意多个节点（包含字节数组或整数值）。


## 📂 Category: Data Structures & Use Cases (2 cards)

### 🟢 Junior Level

#### 1. Redis 如何实现延迟队列?
**Answer:**
可以使用 zset（有序集合）结构，利用排序实现。
将设置好的时间戳作为 score 进行排序，通过 zadd 命令持续往内存中生产消息。再利用 zrangebyscore 查询符合条件的所有待处理任务，通过循环执行队列任务即可。

#### 2. Redis 有哪些数据结构
**Answer:**
1. String（字符串）：最基础的数据结构，可存储字符串、数字、二进制数据，最大512MB。应用：缓存、计数器、共享Session、限速。
2. Hash（哈希）：键值对本身的键值对结构。应用：缓存用户详情、对象。
3. List（列表）：有序字符串列表，可充当栈和队列。应用：消息队列、文章列表。
4. Set（集合）：无序且唯一的字符串集合。应用：标签（tag）、共同关注。
5. Sorted Set（有序集/zset）：每个元素关联一个权重（score）进行排序。应用：用户点赞统计、用户排行榜。


## 📂 Category: Data Warehousing (1 cards)

### 🟡 Mid Level

#### 1. What are the core architectural features and storage characteristics of Apache Hive?
**Answer:**
Hive is a distributed data warehouse built on top of HDFS/cloud storage designed for OLAP batch processing. It uses HiveQL (HQL) for declarative, non-procedural querying, translating high-level commands into execution engines like MapReduce, Tez, or Spark. It stores metadata schemas in an external relational database (Metastore), supports table partitioning and bucketing, and integrates with columnar and row storage formats (ORC, Parquet).


## 📂 Category: Distributed Architecture (2 cards)

### 🟡 Mid Level

#### 1. Redis集群是如何进行伸缩（扩容与缩容）的？
**Answer:**
Redis集群提供了灵活的节点扩容和收缩方案，可以在不影响集群对外服务的情况下增减节点。
其核心原理在于“槽（Slot）和节点的对应关系”：扩容和收缩本质上就是将一部分槽和对应的数据从源节点安全迁移到目标节点（新节点或待下线节点）。


### 🔴 Senior Level

#### 1. 请详细说明Redis集群（Redis Cluster）的核心原理、数据分区机制及故障转移流程
**Answer:**
Redis集群通过数据分区（Sharding）实现分布式存储，通过自动故障转移实现高可用。
1. 数据分区：集群预分化为16384个哈希槽（Slot），每个键根据CRC16校验后对16384取模决定放置在哪一个槽，节点必须分配了槽才能响应相关命令。
2. 节点通信：通过Gossip协议进行节点握手（cluster meet）和状态维护（Ping/Pong消息）。
3. 故障转移：
   - 故障发现：当节点在 cluster-node-timeout 时间内通信失败会被标记为主观下线（pfail）。当半数以上持有槽的主节点将其标记为主观下线时，触发客观下线（failover）。
   - 选举投票：从节点检查主节点断线时间，符合资格后到达选举时间发起选举，由持有槽的主节点进行投票（每个主节点1票），获得 N/2+1 票的从节点胜出并替换故障主节点。
4. 部署建议：为了避免单点故障和脑裂，集群的所有主节点至少应分散部署在3个不同的物理机或可用区上。


## 📂 Category: Distributed Computing (2 cards)

### 🟡 Mid Level

#### 1. What are the core architectural components of Apache Spark?
**Answer:**
• Driver Program: Uses a SparkContext object (entry point) to connect to the cluster, construct the DAG, split jobs into tasks, launch executors on worker nodes, and distribute application code. • Executor: A dedicated JVM process running on worker nodes that executes tasks assigned by the driver and caches data in memory or disk. • Task: The fundamental unit of data processing work executed by an executor.


### 🔴 Senior Level

#### 1. Compare Spark Cluster Deployment Mode vs. Client Deployment Mode on YARN.
**Answer:**
• Cluster Mode: The Spark Driver runs inside the ApplicationMaster container on a cluster node. The resource manager handles allocation, and the driver runs remotely. This mode is unsuited for interactive work (no spark-shell). • Client Mode: The Spark Driver runs locally on the host machine where the job is submitted. The ApplicationMaster only requests executor containers from YARN, and the local client directly communicates with executors to schedule work, fully supporting interactive use via spark-shell.


## 📂 Category: Distributed Consensus & HA (1 cards)

### 🔴 Senior Level

#### 1. How does the quorum journal manager work with fencing?
**Answer:**
To work with fencing, the journal manager uses epoch numbers. Epoch numbers are integers that always increase and have a unique value once assigned. The NameNode generates epoch numbers using a simple algorithm and uses them while sending RPC requests to the QJM. When configuring NameNode HA, the first Active NameNode gets epoch value 1. In case of failover or restart, the epoch number increases. The NameNode with a higher epoch number is considered newer than any NameNode with an earlier epoch number.


## 📂 Category: Distributed Locking (1 cards)

### 🟡 Mid Level

#### 1. Redis实现分布式锁了解吗？
**Answer:**
Redis分布式锁本质是在Redis中占一个“茅坑”。
V1: setnx命令。先来先占，用完了调用del释放。问题：若中途异常导致del没被调用，会陷入死锁。
V2: 锁超时释放。拿到锁后加上过期时间（如5s）。问题：setnx和expire是两条命令而非原子指令，若二者之间服务进程突然挂掉（如掉电或被kill），expire得不到执行仍会导致死锁。
V3: set命令。Redis 2.8引入了set命令的扩展参数，使得setnx和expire可以一起执行的原子指令。当然实际开发中建议使用成熟的轮子——Redisson。


## 📂 Category: Distributed Query Engines (1 cards)

### 🔴 Senior Level

#### 1. What are the primary components of an analytical query engine like Impala, and how do they interact?
**Answer:**
• Impala Daemon (impalad): Runs on worker nodes, accepts client queries (via shell, JDBC, ODBC), parallelizes execution, distributes work across the cluster, and acts as the central coordinator. • StateStore: Periodically checks the health of all Impala daemons and propagates reachability status so that query coordinators can route around failed or unreachable nodes. • Catalog Service: Relays metadata changes from DDL/DML statements to all Impala daemons, minimizing or eliminating the need for manual REFRESH/INVALIDATE METADATA commands.


## 📂 Category: Distributed Storage (4 cards)

### 🟢 Junior Level

#### 1. What is the role of a DataNode (Slave) in a distributed storage architecture like HDFS?
**Answer:**
A DataNode stores the actual block data in the distributed filesystem. It performs read and write operations directly requested by clients, communicates block reports periodically to the NameNode, and is typically deployed on commodity hardware.


### 🟡 Mid Level

#### 1. What is an HDFS namespace ID?
**Answer:**
When an HDFS instance is formatted, the NameNode generates a unique namespace ID. When DataNodes first connect to the NameNode, they bind to this namespace ID and establish a unique 'storage ID' that identifies that particular DataNode within the HDFS instance.

#### 2. What is the distinction between FsImage and EditLogs in HDFS NameNode architecture?
**Answer:**
• FsImage: A serialized point-in-time snapshot of the entire filesystem namespace, directory structures, and file inode metadata stored on the NameNode's local disk. • EditLogs: A transaction log recording every incremental modification, create, update, and delete request made to the filesystem since the last checkpointed FsImage.


### 🔴 Senior Level

#### 1. What is the role and mechanism of Journal Nodes in HDFS NameNode High Availability?
**Answer:**
Journal nodes store edits in a distributed system to keep NameNodes in sync and avoid split-brain scenarios. The Active NameNode writes edits to journal nodes and commits only when replicated to all nodes. The Standby NameNode reads from these edits. Fencing methods (like ZKFC) are still required to prevent stale reads from a former Active NameNode.


## 📂 Category: Distributed Systems (4 cards)

### 🟡 Mid Level

#### 1. What is Apache Impala and how does it achieve high performance?
**Answer:**
Apache Impala provides high-performance, low-latency SQL queries on data stored in Hadoop file formats (like HDFS and Apache HBase). Developed in C++, Impala operates as a distributed, massively parallel processing (MPP) database engine, enabling interactive exploration rather than traditional batch jobs.

#### 2. What is Apache YARN and what are its core framework components?
**Answer:**
YARN (Yet Another Resource Negotiator) is a large-scale distributed operating system for big data applications sitting between HDFS and processing engines. It consists of a master daemon (Resource Manager), slave daemons (Node Managers), and Application Masters.


### 🔴 Senior Level

#### 1. Compare ZooKeeper-based metadata management vs. KRaft mode in distributed systems.
**Answer:**
ZooKeeper-based: Traditionally used an external quorum (ZooKeeper) to handle configuration, naming, and coordination, which introduced external dependencies and metadata bottlenecks. KRaft mode: Stores metadata internally in a dedicated metadata raft quorum/topic. This eliminates external ZooKeeper dependencies, reduces coordination bottlenecks, simplifies deployment architecture, and significantly improves startup and failover performance.

#### 2. 什么是缓存的“无底洞”现象？如何解决？
**Answer:**
无底洞现象是指：为了满足业务需求不断增加分布式缓存（如 Memcached/Redis）节点做水平扩容时，发现集群性能不但没有提升反而下降了。
原因：键值对由于通过哈希函数映射到各个节点，导致分布式批量操作（如 MGET）需要跨多个网络节点获取，随着节点增多，网络往返次数和耗时不断增加。
优化思路：
1. 优化命令本身，减少不必要的批量操作。
2. 减少网络通信次数，使用长连接、连接池、NIO 等技术。


## 📂 Category: Event Streaming (7 cards)

### 🟢 Junior Level

#### 1. What is Apache Kafka and what are its core APIs?
**Answer:**
Kafka is a fast, scalable, fault-tolerant messaging system that enables communication between producers and consumers using message-based topics. It combines messaging, storage, and stream processing. Its four core APIs are the Producer API, Consumer API, Streams API, and Connector API.

#### 2. What is the primary function and workflow of a Kafka producer?
**Answer:**
A Kafka producer is responsible for creating messages, serializing them into byte arrays, and sending them to Kafka topics using the Kafka producer API. It also handles internal configurations for batching, message delivery guarantees, error handling, and performance tuning.


### 🟡 Mid Level

#### 1. What is schema management in the context of Kafka topics?
**Answer:**
Schema management involves using a schema registry to define and enforce the structure of messages flowing through Kafka topics. It ensures that producers and consumers agree on the data format, which is critical when data formats evolve over time.

#### 2. What is the active-passive Kafka cluster configuration?
**Answer:**
In an active-passive setup, data is replicated from an active cluster to a passive one in a unidirectional manner. The passive cluster acts as a backup, taking over operations if the active cluster fails, though replication lag can temporarily lead to data inconsistencies.

#### 3. What is the effect of having more consumers than partitions in a Kafka consumer group?
**Answer:**
If there are more consumers than partitions, some consumers will remain idle because each partition can only be consumed by one consumer at a time within a single group. These idle consumers act as failover standbys to take over if an active consumer fails.


### 🔴 Senior Level

#### 1. How is metadata managed in Kafka topics?
**Answer:**
Metadata management in Kafka involves storing and maintaining information about topics, such as partition assignments, replica configurations, and other settings. This metadata can be managed externally via Apache ZooKeeper or internally in newer KRaft (Kafka Raft) mode, where it is stored in a dedicated metadata topic to ensure cluster consistency and efficient routing.

#### 2. What is the difference between the high watermark offset and log-end offset in Kafka?
**Answer:**
The log-end offset (LEO) is the offset of the last message currently present in a partition’s log. The high watermark offset is the point up to which all messages have been fully replicated to all in-sync replicas (ISRs). Consumers only read up to the high watermark offset to guarantee data durability.


## 📂 Category: High Availability (5 cards)

### 🟡 Mid Level

#### 1. What is Redis Sentinel and how does it provide high availability?
**Answer:**
Redis Sentinel is a distributed monitoring and failover system for Redis deployments. It monitors master and replica instances, performs automatic failover by promoting a replica to master if the original master fails, and acts as a configuration provider for clients.


### 🔴 Senior Level

#### 1. Redis Sentinel（哨兵）实现原理知道吗？
**Answer:**
哨兵模式是通过哨兵节点完成对数据节点的监控、下线、故障转移。
定时监控：通过三个定时任务完成对各个节点的发现和监控：
1. 每隔10秒，每个Sentinel节点会向主节点和从节点发送info命令获取最新拓扑结构。
2. 每隔2秒，每个Sentinel节点会向Redis数据节点的 sentinel :hello 频道上发送该Sentinel节点对于主节点的判断以及当前Sentinel节点的信息。
3. 每隔1秒，每个Sentinel节点会向主节点、从节点、其余Sentinel节点发送一条ping命令做一次心跳检测，来确认这些节点当前是否可乐。

主观下线和客观下线：
1. 主观下线：每个Sentinel节点每隔1秒对主、从、其他Sentinel节点发送ping命令做心跳检测，当这些节点超过 down-after-milliseconds 没有进行有效回复，Sentinel节点就会对该节点做失败判定。
2. 客观下线：当Sentinel主观下线的节点是主节点时，该Sentinel节点会通过 sentinel is-master-down-by-addr 命令向其他Sentinel节点询问对主节点的判断，当超过 quorum 个数，Sentinel节点认为主节点确实有问题，做出客观下线决定。

领导者Sentinel节点选举：使用Raft算法在Sentinel集群中选出一个Leader进行故障转移。
故障转移步骤：
1. 在从节点列表中选出一个节点作为新主节点。
2. Sentinel领导者节点对选出的从节点执行 slaveof no one 命令使其成为主节点。
3. 向其余从节点发送命令使其成为新主节点的从节点。
4. 将原来的主节点更新为从节点并保持关注，当其恢复后去复制新的主节点。

#### 2. Redis Sentinel（哨兵）模式下，新的主节点是如何被挑选出来的？
**Answer:**
选出新的主节点主要分为以下步骤：
1. 过滤：过滤掉“不健康”的节点（主观下线、断线、5秒内没有回复过 Sentinel 节点 ping 响应、与主节点失联超过 down-after-milliseconds * 10 秒的节点）。
2. 优先级：选择 slave-priority（从节点优先级）最高的从节点列表。
3. 偏移量：如果优先级相同，选择复制偏移量最大（复制最完整）的从节点。
4. RunID：如果前两者都相同，选择 runid 最小的从节点。

#### 3. Redis Sentinel（哨兵）领导者（Leader）节点是如何选举出来的？
**Answer:**
1. 每个在线的 Sentinel 节点都有资格成为领导者，当它确认主节点主观下线时，会向其他 Sentinel 节点发送 sentinel is-master-down-by-addr 命令，要求将自己设置为领导者。2. 收到命令的 Sentinel 节点，如果没有同意过其他 Sentinel 节点的同名请求，将同意该请求，否则拒绝。3. 如果该 Sentinel 节点发现自己的票数已经大于等于 max(quorum, num(sentinels)/2+1)，那么它将成为领导者。4. 如果此过程没有选举出领导者，将进入下一次选举。

#### 4. What does cross‑region replication mean in Kafka clusters?
**Answer:**
Cross‑region replication involves duplicating Kafka clusters across different geographical regions. This ensures that if one region experiences an outage, another region can take over, thereby maintaining data availability and business continuity.


## 📂 Category: High Availability & Clustering (2 cards)

### 🟡 Mid Level

#### 1. What is Redis Sentinel and what are its core capabilities?
**Answer:**
Redis Sentinel is a distributed system designed to provide high availability and automated failover for Redis master-slave deployments. It consists of Sentinel nodes (which do not store data, but monitor data nodes) and data nodes (masters and slaves). Its core features include: Monitoring (continuously checking if master and slave instances operate correctly), Automatic failover (promoting a slave to master if the master fails), Configuration provider (acting as a trusted authority for clients to discover the current master address), and Notification (alerting clients of failover events).


### 🔴 Senior Level

#### 1. What is the internal working principle and timeline of tasks in Redis Sentinel?
**Answer:**
Sentinel uses three periodic tasks to maintain cluster health: (1) Every 10 seconds, each Sentinel sends an 'INFO' command to masters and slaves to gather topology changes. (2) Every 2 seconds, Sentinels publish/subscribe state information on the 'sentinel:hello' channel. (3) Every 1-second, Sentinels send a 'PING' to all nodes and other Sentinels for heartbeat checks. Failure detection moves from Subjective Down (SDOWN, declared by a single Sentinel when a node fails to respond within 'down-after-milliseconds') to Objective Down (ODOWN, confirmed when a quorum of Sentinels agree). Leader election is then performed using the Raft algorithm, and the leader executes failover via 'SLAVEOF NO ONE' on the selected replica.


## 📂 Category: KRaft & Cluster Management (1 cards)

### 🔴 Senior Level

#### 1. How does KRaft enhance fault tolerance, replace ZooKeeper, and simplify metadata management?
**Answer:**
KRaft (Kafka Raft) integrates metadata coordination directly into Kafka brokers by using a distributed controller quorum to replicate metadata. This removes the dependency on an external ZooKeeper ensemble, reduces communication overhead, simplifies configuration, minimizes downtime during leader re-elections, and allows the system to quickly recover by synchronizing only missing events.


## 📂 Category: Kafka Architecture (5 cards)

### 🟢 Junior Level

#### 1. What are the primary responsibilities of a Kafka broker?
**Answer:**
The key responsibilities include: • Message Management: Receiving messages from producers and assigning them to partitions. • Data Storage: Maintaining topics divided into partitions. • Replication: Duplicating partition data across brokers for high availability. • Metadata Management: Tracking topic configurations, partition locations, and consumer offsets.

#### 2. What is the role of a Kafka broker within a cluster?
**Answer:**
Kafka brokers are independent processes running on separate machines. They store data partitions, manage client requests, and communicate with other brokers to distribute data and metadata, ensuring fault tolerance and scalability.

#### 3. What metadata do Kafka brokers manage, and why is it important?
**Answer:**
Brokers manage metadata such as topic lists, partition counts, partition placement across brokers, and consumer offsets. This metadata is crucial for maintaining data structure, coordinating consumers, and enabling efficient retrieval and recovery.


### 🟡 Mid Level

#### 1. What is the purpose of leader election in distributed clusters for Kafka?
**Answer:**
ZooKeeper or KRaft handles leader election by tracking the current leader broker in the Kafka cluster. If the leader fails, a new election is triggered to promptly designate a replacement, ensuring uninterrupted cluster operations.

#### 2. What problems can occur with underpartitioning in a Kafka deployment?
**Answer:**
Underpartitioning may cause individual partitions to become overloaded with messages, leading to processing delays, backlogs, and resource bottlenecks such as CPU or disk I/O constraints on the hosting broker.


## 📂 Category: Kafka Consumers (3 cards)

### 🟢 Junior Level

#### 1. What is the round-robin assignor for consumer groups, and what advantage does it offer?
**Answer:**
The round-robin assignor cycles through the available partitions and assigns them one-by-one to each consumer. This approach tends to distribute the partitions more evenly, especially when dealing with topics having a variable number of partitions.


### 🟡 Mid Level

#### 1. What is the significance of the internal topic __consumer_offsets in Kafka?
**Answer:**
The __consumer_offsets topic stores each consumer group’s offsets for each partition. This internal mechanism is crucial for tracking consumption progress, enabling consumers to resume processing from the last committed offset in the event of a failure or restart.

#### 2. What is the sticky assignor, and how does it benefit consumer groups during rebalancing?
**Answer:**
The sticky assignor minimizes partition movement between rebalances by preserving as many existing partition assignments as possible. This leads to fewer disruptions and more stable processing in consumer groups.


## 📂 Category: Kafka KRaft (2 cards)

### 🟡 Mid Level

#### 1. What is the role of the controller quorum in KRaft?
**Answer:**
The controller quorum in KRaft is a group of controllers that jointly manage the cluster’s metadata and coordinate operations. This distributed approach ensures that metadata is consistently replicated and available, even if individual controllers fail.


### 🔴 Senior Level

#### 1. What performance benefits does KRaft provide over the traditional ZooKeeper-based architecture?
**Answer:**
KRaft reduces operational overhead by eliminating a separate ZooKeeper cluster, simplifying deployment and maintenance. This leads to lower latency in metadata operations, improved system throughput, and reduced risk of performance bottlenecks.


## 📂 Category: Kafka Producers (5 cards)

### 🟢 Junior Level

#### 1. What is the purpose of producer partitioning strategies in Kafka?
**Answer:**
Producer partitioning strategies decide how messages are distributed across the partitions of a topic, affecting message ordering, load distribution, and overall system performance.

#### 2. What is the significance of message keys and values in Kafka?
**Answer:**
In Kafka, the key is used to determine which partition a message goes to, ensuring messages with the same key maintain order. The value contains the actual event data, which can be simple or complex, and is serialized before being sent to the broker.


### 🟡 Mid Level

#### 1. What is the significance of batch size and linger time in Kafka producer performance?
**Answer:**
Increasing the batch size allows more messages to be sent together, improving throughput, but it may require more memory and increase latency. The linger time controls how long messages are held to form a batch—longer linger times can lead to larger, more efficient batches but at the cost of increased delay in message delivery.

#### 2. What partitioning strategies are used when no message key is provided?
**Answer:**
If no key is provided, Kafka may use a round-robin strategy, cycling through partitions evenly, or a sticky partitioning approach that batches messages to one partition until a threshold (time or batch size) is reached, then switches to another.


### 🔴 Senior Level

#### 1. What problem does the uniform sticky partitioner solve, and how does it function?
**Answer:**
The uniform sticky partitioner addresses small batch sizes in round-robin distribution by temporarily assigning unkeyed records to the same partition until a batch limit or time limit is reached, optimizing throughput and latency while maintaining even distribution over time.


## 📂 Category: Kafka Replication (1 cards)

### 🟢 Junior Level

#### 1. What is the significance of leader and follower roles in broker replication?
**Answer:**
In replication, the leader broker handles all read and write operations for its partition, while follower brokers continuously sync with the leader, ensuring that if the leader fails, a follower can seamlessly take over without data loss.


## 📂 Category: Memory Management (4 cards)

### 🟡 Mid Level

#### 1. How does Redis handle memory eviction when it reaches maxmemory?
**Answer:**
When Redis hits the maxmemory limit, it applies configured eviction policies like noeviction, volatile-lru, allkeys-lru, volatile-lfu, allkeys-lfu, volatile-random, allkeys-random, or volatile-ttl to free up space by removing keys.

#### 2. Redis 报内存不足怎么处理？
**Answer:**
1. 修改配置文件 redis.conf 的 maxmemory 参数增加可用内存，或通过命令行动态设置：`CONFIG SET maxmemory <bytes>`。
2. 修改内存淘汰策略（maxmemory-policy），及时释放内存空间。
3. 使用 Redis 集群模式（Cluster），进行横向扩容。

#### 3. Redis 有哪些内存溢出控制/内存淘汰策略？
**Answer:**
Redis 提供 6 种内存淘汰策略：1. noeviction（默认）：不删除任何数据，拒绝所有写入操作并返回错误信息，此时只响应读操作；2. volatile-lru：根据 LRU 算法删除设置了超时属性（expire）的键，直到腾出足够空间；3. allkeys-lru：根据 LRU 算法删除任意键，直到腾出足够空间；4. allkeys-random：随机删除任意键，直到腾出足够空间；5. volatile-random：随机删除过期键，直到腾出足够空间；6. volatile-ttl：根据键值对象的 ttl 属性，删除最近将要过期的数据。

#### 4. Redis的过期数据回收策略有哪些？
**Answer:**
1. 惰性删除：指当我们查询key的时候才对key进行检测，如果已经达到过期时间，则删除。缺点：如果这些过期的key没有被访问，那么它就一直无法被删除，并且一直占用内存。
2. 定期删除：指Redis每隔一段时间对数据库做一次检查，删除里面的过期key。由于不可能对所有key去做轮询来删除，所以Redis会每次随机取一些key去做检查和删除。


## 📂 Category: Message Brokers (7 cards)

### 🟢 Junior Level

#### 1. Describe the round-robin partitioning strategy for producers and explain when it is useful.
**Answer:**
The round-robin strategy sequentially cycles through all available partitions, assigning each successive message to the next partition in order. It is particularly useful when messages lack a natural partitioning key or when preventing 'hot partitions' under uniform key distributions is required.

#### 2. What are the four core APIs provided by Apache Kafka?
**Answer:**
• Producer API: Enables applications to publish streams of records to one or more Kafka topics. • Consumer API: Enables applications to subscribe to topics and process record streams. • Streams API: Acts as a stream processor, transforming input streams from topics into output streams. • Connecter API: Builds and runs reusable producers/consumers that integrate Kafka topics with external data systems (e.g., databases, search indexes).


### 🟡 Mid Level

#### 1. Describe the interplay between producers, brokers, and consumers regarding offset management in a log-based messaging system.
**Answer:**
Producers append messages sequentially to partitions, where brokers assign them immutable offsets in an ordered commit log. Consumers pull messages by tracking their current offset position. To ensure at-least-once or exactly-once processing guarantees and enable crash recovery, consumers periodically commit their processed offsets back to the broker (or external store).

#### 2. How do distributed message brokers (e.g., Kafka) ensure high availability and fault tolerance?
**Answer:**
Fault tolerance is achieved through data replication across multiple brokers. Each partition has a designated leader broker handling read/write traffic and multiple follower brokers syncing the data. If the partition leader fails, an automated leader election among in-sync replicas (ISRs) ensures uninterrupted data availability.

#### 3. How does the Range partition assignment strategy work in consumer groups, and what are its potential pitfalls?
**Answer:**
The Range strategy assigns partitions to consumers in contiguous blocks based on sorted partition and consumer order. For example, if a topic has 4 partitions and 2 consumers, Consumer 1 gets partitions 0 and 1, while Consumer 2 gets 2 and 3. Pitfall: If the total number of partitions is not evenly divisible by the number of consumers, it leads to skewed workloads where some consumers handle more partitions than others.


### 🔴 Senior Level

#### 1. Explain how partition assignment and rebalancing work in Kafka consumer groups.
**Answer:**
During a rebalance (triggered by members joining, leaving, or topic metadata changes), the group coordinator pauses processing, collects consumer metadata, and executes a partition assignment strategy (e.g., Range, Cooperative Sticky). This ensures exclusive partition ownership per consumer and attempts to balance the processing workload across the group.

#### 2. What is the role of the group coordinator in a Kafka consumer group?
**Answer:**
The group coordinator (a designated broker) manages consumer group membership, heartbeats, and partition reassignments. It detects consumer dropouts via missed heartbeats, coordinates group rebalances, and ensures that each partition within a subscribed topic is assigned to exactly one active consumer per group.


## 📂 Category: Messaging & Delivery Guarantees (2 cards)

### 🟡 Mid Level

#### 1. What are the three common message delivery guarantees in Kafka that relate to offset management?
**Answer:**
The three delivery guarantees are:

- At most once: Messages may be lost, but are never processed more than once.
- At least once: No messages are lost, though some may be processed more than once.
- Exactly once: Each message is processed only once, with no loss or duplication.


### 🔴 Senior Level

#### 1. What configurations are typically used to achieve "exactly once" semantics in Kafka?
**Answer:**
To achieve exactly once semantics, you must:

- Enable idempotence on the producer by setting `enable.idempotence=true`.
- Configure the stream processing application with `processing.guarantee=exactly_once`.

This ensures that offset commits and message processing occur as a single atomic transaction.


## 📂 Category: Messaging & Queues (1 cards)

### 🟡 Mid Level

#### 1. 使用Redis如何实现异步队列？
**Answer:**
主要有以下几种方式：
1. 使用List作为队列：通过 lpush 生产消息，rpop 消费消息。消费者通常需要进行自旋 rpop，但队列为空时会导致 CPU 飙升；可通过休眠处理，但会带来消息延迟问题。
2. 使用List作为队列配合阻塞读：lpush 生产消息，brpop 消费消息。brpop 是 rpop 的阻塞版本，队列为空时会阻塞直到有值或超时，只能实现一对一的队列。
3. 使用 Pub/Sub（发布/订阅）：支持 1:N 的消息发布与订阅，客户端订阅 channel 接收消息。但这种方式不可靠，不保证订阅者一定能收到消息，且不进行消息持久化。生产环境中通常建议使用专业的MQ。


## 📂 Category: Network & Concurrency (1 cards)

### 🟡 Mid Level

#### 1. 什么是I/O多路复用？
**Answer:**
I/O多路复用是一种让单个线程去监视多个描述符（Socket），一旦某个描述符就绪（读就绪或写就绪），能够通知程序进行相应的读写操作的技术。相比于传统的阻塞循环或者为每个连接创建一个线程（多进程/多线程）的模型，I/O多路复用极大地提升了系统的并发处理能力和资源利用率。Redis正是基于Reactor模式利用epoll/kqueue等实现了高效的单线程事件循环。


## 📂 Category: Offsets & State (2 cards)

### 🟢 Junior Level

#### 1. What are topic partition offsets and why are they important?
**Answer:**
Offsets are numeric markers that indicate the position of a message within a partition. They are used by Kafka to track which messages have been consumed. This mechanism ensures that consumers can resume reading from the correct position, maintain order, and provide at-least-once or exactly-once processing guarantees.

#### 2. What does the term “committed offset” refer to?
**Answer:**
The committed offset is the offset of the last message that a consumer has successfully processed and acknowledged. It serves as a checkpoint for consumer progress.


## 📂 Category: Partitioning & Distribution (3 cards)

### 🟢 Junior Level

#### 1. How does a Kafka broker decide which partition to store an incoming message?
**Answer:**
When a producer sends a message, the broker uses either: • A deterministic partitioning strategy based on a producer-specified key, or • A round-robin algorithm if no key is provided, ensuring balanced distribution across partitions.

#### 2. How does the default Kafka partitioner work when a message key is provided versus when it is null?
**Answer:**
With a provided key, Kafka applies a hash function to the key to consistently map messages to a specific partition. If the key is null, the partition is chosen at random (or by a simple round-robin algorithm), distributing messages across available partitions.


### 🟡 Mid Level

#### 1. How does choosing the wrong partitioning key affect message distribution in Kafka?
**Answer:**
An inappropriate key can lead to uneven distribution, with messages concentrating in a few partitions (hot partitions) while others remain underutilized. This imbalance can degrade performance and overload specific consumers.


## 📂 Category: Partitioning & Scaling (2 cards)

### 🔴 Senior Level

#### 1. What are the risks associated with overpartitioning in Kafka?
**Answer:**
Overpartitioning can lead to long and resource-intensive rebalances, inefficient resource utilization (as some partitions may remain underused), and increased management complexity, especially if the message volume does not justify the high partition count.

#### 2. What best practices should be followed to avoid common partitioning pitfalls in Kafka?
**Answer:**
Best practices include:

- Starting with a lower number of partitions and scaling up as needed.
- Choosing meaningful keys to ensure even message distribution.
- Continuously monitoring key Kafka metrics (such as partition lag and consumer offsets) to detect and address performance issues early.


## 📂 Category: Performance & Operations (2 cards)

### 🟡 Mid Level

#### 1. Suppose Redis has 100 million keys, with 100k keys matching a known prefix. How do you find them efficiently?
**Answer:**
Using the 'keys' command will scan for the pattern but blocks the main thread, causing a service outage until complete. Instead, use the 'SCAN' command, which provides non-blocking cursor-based iteration. SCAN may return duplicate keys requiring client-side deduplication, but it avoids thread starvation and service freezes.


### 🔴 Senior Level

#### 1. Redis 常见性能问题和解决方案有哪些？
**Answer:**
常见性能优化建议包括：1. Master 节点尽量不做任何持久化工作（如内存快照和 AOF 日志），特别是关闭内存快照；2. 关键数据可由某个 Slave 开启 AOF 备份（策略为每秒同步一次）；3. Slave 和 Master 尽量在同一个局域网内以保证主从复制速度和连接稳定性；4. 尽量避免在压力较大的主库上增加从库；5. 注意 BGREWRITEAOF 重写 AOF 会消耗大量 CPU 和内存资源导致服务短暂停顿；6. 尽量使用单向链表结构的主从架构，避免图状结构以保证稳定性。


## 📂 Category: Performance Optimization (1 cards)

### 🟡 Mid Level

#### 1. 对 Redis 的管道（Pipelining）了解多少？
**Answer:**
Redis 提供了 Pipelining、Transactions 和 Lua Scripts 三种将客户端多条命令打包发送给服务端执行的方式。
Pipelining 是其中最简单的，允许客户端一次性将多条命令发送给服务端，服务端将结果缓存，直到最后一条命令执行完后一次性返回。
优势：
1. 节省 RTT（Round Trip Time）：减少客户端与服务端的网络往返次数。
2. 减少上下文切换：将多次用户态到内核态的系统调用合并，降低开销。


## 📂 Category: Performance Tuning (2 cards)

### 🔴 Senior Level

#### 1. Redis 中的大key（BigKey）问题有哪些危害？如何发现并处理？
**Answer:**
大key表现为：单个string类型的value过大（size超过10KB），或者hash、set、zset、list中存储了过多的元素（以万为单位）。
危害：
1. 客户端耗时增加甚至超时。
2. 对大key进行IO操作时严重占用带宽和CPU。
3. 造成Redis集群数据倾斜。
4. 主动或被动删除时可能导致阻塞。
发现方式：
1. bigkeys命令：遍历分析实例中的所有Key，返回整体统计信息与每个数据类型中Top1的大Key。
2. redis-rdb-tools：Python编写的工具，用于分析RDB快照文件。
处理方式：
1. 删除大key：Redis >= 4.0 可使用 UNLINK 命令安全地非阻塞删除；Redis < 4.0 建议通过 SCAN 命令增量迭代扫描并删除。
2. 压缩和拆分key：对string进行序列化/压缩算法，或拆分为多个key使用 mget；对集合类型按预估规模进行分片存储。

#### 2. 如何监控和处理 Redis 的热 key（HotKey）问题？
**Answer:**
监控热 key 的途径：
1. 客户端：在客户端维护全局字典记录 key 的调用次数。
2. 代理端：如 Twemproxy、Codis 等基于代理的架构，在代理层进行收集统计。
3. Redis 服务端：使用 monitor 命令监控执行的所有命令（注意生产环境性能影响）。
处理热 key 的方法：
1. 将热 key 打散分发到不同的服务器，降低单机压力。
2. 增加多级缓存（如本地缓存），提前加载热 key 数据到内存中，若 Redis 宕机可降级查询本地缓存。


## 📂 Category: Performance Tuning & Diagnostics (1 cards)

### 🔴 Senior Level

#### 1. What causes Redis blocking, and how do you diagnose and resolve slow queries and high CPU utilization?
**Answer:**
Redis blocking is typically caused by high time-complexity commands ($O(N)$ or worse) executed on large objects, or serialization/persistence bottlenecks. Diagnosis and resolution steps:
1. Slow Query Analysis: Use `slowlog get {n}` to retrieve the slowest commands. Mitigate by replacing heavy commands (e.g., swapping `hgetall` for `hmget`, avoiding `keys` or `sort`), and splitting large objects/keys into smaller chunks.
2. CPU Saturation: Check Redis usage via `redis-cli -h {ip} -p {port} --stat`. If the OPS reaches peak limits (tens of thousands+), scale out using Redis Cluster. If OPS is moderate (hundreds/thousands), inspect commands and persistence locks.
3. Persistence Bottlenecks:
   - Fork Blocking: `fork()` during RDB/AOF rewrites causes main-thread latency if execution time is too high.
   - AOF Fsync Blocking: Background threads issuing `fsync` can cause the main thread to block if the previous sync is >2 seconds overdue.
   - Transparent HugePages (THP): Enabled OS kernels increase copy-on-write memory pages from 4KB to 2MB, significantly slowing write operations.


## 📂 Category: Persistence (5 cards)

### 🟢 Junior Level

#### 1. Redis 持久化方式有哪些？有什么区别？
**Answer:**
Redis 主要支持两种持久化方式：1. RDB（Redis DataBase）：将当前进程数据生成压缩的二进制快照保存到磁盘。支持手动触发（save 阻塞、bgsave 异步子进程 fork）和自动触发（save m n）。优点是恢复速度快、文件紧凑；缺点是实时性差，可能会丢失数据。2. AOF（Append Only File）：以独立日志方式记录每次写命令。通过 append、sync（同步策略）、rewrite（重写压缩）、load 流程运作。优点是数据安全性高、实时性好；缺点是文件体积大、恢复较慢。

#### 2. Redis 的数据是如何恢复的？启动加载流程是什么？
**Answer:**
当 Redis 发生故障时，可以从 RDB 或 AOF 文件中恢复，只需将文件复制到 Redis 数据目录下并启动 redis-server 即可。Redis 启动时加载数据的流程：1. AOF 持久化开启且存在 AOF 文件时，优先加载 AOF 文件；2. AOF 关闭或者 AOF 文件不存在时，加载 RDB 文件；3. 加载 AOF/RDB 文件成功后，Redis 启动成功；4. AOF/RDB 文件存在错误时，Redis 启动失败并打印错误信息。


### 🟡 Mid Level

#### 1. RDB 和 AOF 各自有什么优缺点？
**Answer:**
RDB 优点：1. 紧凑的二进制文件 dump.rdb，非常适合备份、全量复制；2. 容灾性好，易于传输；3. 恢复速度远快于 AOF。RDB 缺点：1. 实时性低，无法做到秒级持久化，可能丢失最后一次快照后的数据；2. 存在版本兼容性问题。
AOF 优点：1. 实时性高，支持 appendfsync 配置（如 always 每次修改都记录）；2. 通过 append 模式写文件，若宕机可通过 redis-check-aof 工具修复。AOF 缺点：1. AOF 文件比 RDB 大，恢复速度慢；2. 数据集大时启动效率低于 RDB。

#### 2. Redis 4.0 的混合持久化了解吗？
**Answer:**
重启 Redis 时很少单独使用 RDB 恢复，因为会丢失大量数据；使用 AOF 重放又比 RDB 慢得多。Redis 4.0 引入了混合持久化选项，结合了 RDB 文件的内存快照内容和自持久化开始期间发生的增量 AOF 日志。重启时先加载 RDB 内容，再重放增量 AOF 日志，大幅提升了重启效率。

#### 3. What is the difference between Redis RDB and AOF persistence?
**Answer:**
RDB (Redis Database) takes point-in-time snapshots of dataset at specified intervals, offering faster restarts and smaller file sizes. AOF (Append Only File) logs every write operation received by the server, providing better durability with minimal data loss risk at the cost of larger file sizes and potentially slower recovery.


## 📂 Category: Persistence & Durability (1 cards)

### 🟡 Mid Level

#### 1. How do you choose between Redis RDB and AOF persistence mechanisms?
**Answer:**
For maximum data safety, use both RDB and AOF simultaneously; upon restart, Redis will prioritize loading the AOF file because it typically contains a more complete dataset. If you can tolerate data loss within a span of minutes, you can rely solely on RDB. While some users rely exclusively on AOF, it is generally not recommended because periodic RDB snapshots are highly efficient for backups, allow faster data restoration, and avoid potential bugs within the AOF rewriting/replay engine. If persistence is not required, both can be disabled.


## 📂 Category: Producer & Cluster Discovery (1 cards)

### 🟡 Mid Level

#### 1. How does a Kafka producer discover and connect to the Kafka cluster?
**Answer:**
A producer initially connects to a Kafka bootstrap server—a subset of Kafka brokers—to discover the full cluster topology. It sends a MetaDataRequest, which returns details such as broker addresses and current leaders for each topic partition. Once discovered, the producer sends messages directly to the leader broker for the target partition.


## 📂 Category: Producers & Durability (1 cards)

### 🟡 Mid Level

#### 1. What do the different acks settings mean in Kafka producers?
**Answer:**
acks=0: The producer does not wait for any acknowledgment from the broker (fire-and-forget). acks=1: The producer waits for acknowledgment from the partition leader only. acks=all (or -1): The producer waits for acknowledgments from all in-sync replicas, which maximizes durability at the expense of some latency.


## 📂 Category: Replication (2 cards)

### 🟡 Mid Level

#### 1. Redis 主从有哪些常见的拓扑结构？
**Answer:**
Redis 的复制拓扑结构支持单层或多层关系，主要分为三种：1. 一主一从：最简单的复制拓扑结构，用于主节点宕机时从节点提供故障转移支持；2. 一主多从（星形拓扑）：应用端可以利用多个从节点实现读写分离，分担主节点读压力；3. 树状主从结构：从节点不仅可以复制主节点数据，同时可以作为其他从节点的上层主节点继续向下复制，有效降低主节点负载和需要传给从节点的数据量。

#### 2. Redis的主从复制原理了解吗？
**Answer:**
1. 保存主节点（master）信息：从节点（slave）保存主节点的ip和port。
2. 主从建立连接：从节点发现新主节点后，尝试和主节点建立网络连接。
3. 发送ping命令：连接建立成功后发送ping请求进行首次通信，检测网络套接字是否可用、主节点当前是否可接受处理命令。
4. 权限验证：如果主节点要求密码验证，从节点必须正确的密码才能通过验证。
5. 同步数据集：主从复制连接正常通信后，主节点会把持有的数据全部发送给从节点。
6. 命令持续复制：接下来主节点会持续地把写命令发送给从节点，保证主从数据一致性。


## 📂 Category: Replication & Fault Tolerance (1 cards)

### 🟡 Mid Level

#### 1. How does Kafka achieve fault tolerance through topic replication?
**Answer:**
By replicating each partition across several brokers, Kafka minimizes the risk of data loss. The leader handles all writes while followers stay in sync. If the leader fails, one of the in-sync replicas is promoted to leader, thereby ensuring that data remains available and consistent.


## 📂 Category: Replication & High Availability (3 cards)

### 🟢 Junior Level

#### 1. What is Redis master-slave replication and what are its primary use cases?
**Answer:**
Master-slave replication copies data from a master Redis server to one or more slave servers in a unidirectional flow (master to slave). It supports master-slave and slave-slave synchronization. Main use cases include:
- Data Redundancy: Provides hot backups as an additional layer of safety beyond persistence.
- Fault Recovery: Slaves can provide read availability or be promoted during failures.
- Load Balancing: Combined with read/write splitting (writes to master, reads from slaves), it increases read throughput.
- High Availability Foundation: Serves as the base for Redis Sentinel and Cluster.


### 🟡 Mid Level

#### 1. What are the architectural limitations of Redis master-slave replication?
**Answer:**
1. Failover requires manual intervention to promote a slave, update application connection strings, and reconfigure other slaves (unless Sentinel or Cluster is used).
2. Master write capability is limited by a single machine's resources.
3. Master storage capacity is limited by a single machine's RAM.
The first issue pertains to High Availability, while the latter two are distributed scaling limitations.


### 🔴 Senior Level

#### 1. 请详细说明Redis主从数据同步的方式（全量复制与部分复制）
**Answer:**
Redis使用psync命令完成主从数据同步，分为全量复制和部分复制：
1. 全量复制（用于初次复制）：
   - 从节点发送 psync ? -1，主节点响应 +FULLRESYNC 命令及 runId 和 offset。
   - 主节点执行 bgsave 生成 RDB 文件发送给从节点。
   - 从节点清空旧数据，载入新收到的 RDB 文件。
   - 主节点在生成/传输 RDB 期间产生的写命令会写入“复制客户端缓冲区”，RDB传输完成后再发送给从节点补齐。
2. 部分复制（用于网络闪断或命令丢失的场景优化）：
   - 当主从断线超过 repl-timeout 后连接断开。
   - 主节点在“复制积压缓冲区”（默认1MB）中保存最近一段时间的写命令。
   - 网络恢复后，从节点发送 psync {runId} {offset}。
   - 主节点校验 runId 一致且 offset 仍在复制积压缓冲区内，则响应 +CONTINUE，并发送缓冲区中丢失的数据，恢复主从同步。


## 📂 Category: Resource Management (2 cards)

### 🟡 Mid Level

#### 1. What are the core components of a distributed resource manager (e.g., YARN), and what are their primary responsibilities?
**Answer:**
A) Scheduler: Responsible for allocating cluster resources (CPU, memory) to running applications based on pre-defined scheduling policies (e.g., capacity, fairness). B) Application Manager: Manages running Application Masters in the cluster, including starting application masters, monitoring their health, and restarting them on different nodes in case of container or node failures.


### 🔴 Senior Level

#### 1. Compare Fair Scheduler and Capacity Scheduler in multi-tenant cluster environments.
**Answer:**
• Fair Scheduler: Assigns resources to jobs dynamically so all applications share an equal amount of cluster resources over time. Ideal for ensuring equal progress, optimizing data locality across varying pool utilizations, and preventing FIFO starvation. • Capacity Scheduler: Allows multi-tenant clusters to maximize throughput via isolated resource queues with guaranteed minimum capacities. Ideal for workloads requiring scheduling determinism, strict memory-based guarantees, and predictable hierarchical resource allocations.


## 📂 Category: Scripting & Transactions (1 cards)

### 🟡 Mid Level

#### 1. Redis和Lua脚本的使用了解吗？
**Answer:**
Redis的事务功能比较简单，开发中可利用Lua脚本增强Redis的命令：
1. 原子执行：Lua脚本在Redis中是原子执行的，执行过程中间不会插入其他命令。
2. 自定义命令复用：可以帮助开发和运维人员创造出自己定制的命令，并常驻在Redis内存中实现复用。
3. 减少网络开销：可以将多条命令一次性打包，有效减少网络开销。


## 📂 Category: Security & Authentication (1 cards)

### 🟡 Mid Level

#### 1. What is Kerberos and how does it function in a distributed environment?
**Answer:**
Kerberos provides a centralized authentication server whose function is to authenticate users to servers and servers to users. It runs as a third-party trusted server known as the Key Distribution Center (KDC), where each user and service on the network is treated as a principal.


## 📂 Category: Storage & Messaging Semantics (1 cards)

### 🟢 Junior Level

#### 1. How does Kafka guarantee message ordering and use offsets internally?
**Answer:**
Each partition in Kafka is an append-only log where messages are written in sequence and marked with an offset. This ordering mechanism ensures that consumers process messages in the exact order they were written within a single partition.


## 📂 Category: Storage & Performance (1 cards)

### 🟡 Mid Level

#### 1. How does Kafka compression work at the topic level?
**Answer:**
Kafka supports compression to optimize disk space and network usage. Compression can be applied at the topic level, either by accepting already compressed messages from producers or by re-compressing data using algorithms like gzip, snappy, lz4, or zstd. Consistent use of a compression algorithm between producers and topics can prevent the overhead of recompression.


## 📂 Category: Streaming Architecture (9 cards)

### 🟢 Junior Level

#### 1. What roles do producers and consumers play in Apache Kafka’s architecture?
**Answer:**
In Kafka, producers are client applications that publish messages (or events) to topics, while consumers subscribe to topics to read those messages. This separation enables scalable, decoupled, and real-time data processing.

#### 2. Why is message serialization important in Kafka producers and how is it typically implemented?
**Answer:**
Kafka treats messages as simple byte arrays. Serialization converts structured data (like JSON) into byte arrays before sending.


### 🟡 Mid Level

#### 1. What role do partitions play in the architecture of Kafka brokers?
**Answer:**
Partitions break topics into smaller, manageable segments. They: • Store messages in an immutable sequence. • Enable parallel processing and scalability by allowing data to be distributed across multiple brokers and processed concurrently by consumers.

#### 2. What role does replication play in Kafka topics?
**Answer:**
Replication in Kafka topics ensures high durability and fault tolerance. Each partition is replicated across multiple brokers, with one replica designated as the leader and the others as followers. In case of broker failure, one of the follower replicas can quickly take over, ensuring continuous availability of data.

#### 3. Which broker-side configurations interact with the producer’s durability settings?
**Answer:**
Two key broker-side settings are:
• replication.factor: Determines how many copies of a topic are maintained across brokers.
• min.insync.replicas: Sets the minimum number of replicas that must acknowledge a write when using acks=all.
These settings help balance durability and availability.

#### 4. Why are Kafka offsets necessary in a distributed streaming system?
**Answer:**
Offsets enable Kafka to:

- Track message progress from production to consumption
- Maintain message ordering within partitions
- Support fault tolerance by allowing consumers to restart from the last committed offset
- Facilitate parallel processing and horizontal scalability

#### 5. Why was ZooKeeper originally chosen for use with Kafka?
**Answer:**
ZooKeeper was adopted because it simplified the coordination of distributed brokers by managing configuration, leader election, ACLs, locks, and membership, thereby ensuring data consistency and high availability in Kafka clusters.


### 🔴 Senior Level

#### 1. What role does ZooKeeper play in a Kafka cluster?
**Answer:**
In Kafka, ZooKeeper coordinates broker interactions by tracking broker availability, managing leader elections, storing configuration data (e.g., topic creation/deletion), handling access control lists (ACLs), and ensuring consistent cluster membership and synchronization.

#### 2. When and why would you implement a custom partitioner on the producer side?
**Answer:**
A custom partitioner is implemented when built-in strategies do not meet specific application needs. By overriding the default partitioning logic (via the Kafka Producer API), you can tailor the key-to-partition mapping to handle special cases—such as dedicating a partition for high-volume sources—to avoid hotspots.


## 📂 Category: Transactions (1 cards)

### 🟡 Mid Level

#### 1. Redis 支持事务吗？其原理与注意事项是什么？
**Answer:**
Redis 提供了简单的事务支持，但不完全支持 ACID。通过 `multi`（开始）、`exec`（执行）、`discard`、`watch` 实现。原理是命令在 `exec` 之前不执行，而是缓存在服务器的事务队列中，收到 `exec` 后原子顺序执行。注意事项：1. 不支持回滚（语法错误会整体拒绝，但运行时错误会继续执行剩余命令，以保持简单快速）；2. 事务执行期间不会被其他客户端打断；3. 不满足持久性要求。


## 📂 Category: ZooKeeper (1 cards)

### 🟢 Junior Level

#### 1. What is the significance of ZooKeeper’s file system–like data model?
**Answer:**
The file system–like model, with hierarchical znodes, provides an intuitive structure for storing configuration data, state information, and coordination metadata. This structure makes it easier to manage and retrieve data in a distributed system.

