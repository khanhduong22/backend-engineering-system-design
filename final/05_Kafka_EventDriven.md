# 05_Kafka_EventDriven - Kafka & Event-Driven Systems Study Guide

- **Total Cards**: 197

---

## 📂 Category: Apache Hive (3 cards)

### 🟢 Junior Level

#### 1. What is the underlying processing framework and resource management system for Hive?
**Answer:**
Hive internally uses the MapReduce framework as its default execution engine (along with integration for others like Spark/Tez) and YARN (Yet Another Resource Negotiator) for cluster resource management. It uses Hadoop Distributed File System (HDFS) for distributed storage.


### 🟡 Mid Level

#### 1. What are the types of Hive Clients?
**Answer:**
Hive clients are categorized into three types:
1. Thrift Clients: The Hive server is based on Apache Thrift to handle requests from Thrift clients.
2. JDBC Client: Allows Java applications to connect using a JDBC driver, which uses Thrift to communicate with HiveServer2.
3. ODBC Client: Allows ODBC-protocol-based applications to connect using an ODBC driver, which also uses Thrift to communicate with HiveServer2.


### 🔴 Senior Level

#### 1. What are the core Hive Services and architecture components?
**Answer:**
Core Hive components include Beeline, HiveServer2, Hive Driver, Compiler, Optimizer, Execution Engine, and Metastore.
• Beeline: A command shell supported by HiveServer2 for executing queries.
• HiveServer2: Enables multiple concurrent clients to execute queries and retrieve results, optimized for JDBC/ODBC APIs.
• Hive Driver: Receives HiveQL statements, creates session handles, and sends queries to the compiler.
• Hive Compiler & Optimizer: Parses queries, performs semantic analysis using the Metastore, and generates a DAG execution plan, optimized for efficiency.
• Execution Engine: Executes the compiled plan sequentially via Hadoop.
• Metastore: Stores table schemas, partitions, columns, and SerDe info in a relational database, providing a Thrift interface (Remote mode) or direct JDBC access (Embedded mode).
• HCatalog & WebHCat: HCatalog is a table/storage management layer built on Hive Metastore, while WebHCat provides a REST API interface for it.


## 📂 Category: Architecture (20 cards)

### 🟢 Junior Level

#### 1. What are the core foundational components of a traditional Apache Kafka architecture?
**Answer:**
Kafka consists of Topics (categorized logs supporting partitions and replication for fault tolerance and scalability), Producers (publish messages to topics), Consumers (extract and process messages from topics), Brokers (systems maintaining published data and partition logs), and ZooKeeper (handles metadata, health checks, and broker leadership election).

#### 2. What are the four core APIs of Apache Kafka?
**Answer:**
• Producer API: Allows applications to publish streams of records to one or more Kafka topics.
• Consumer API: Permits applications to subscribe to topics and process record streams.
• Streams API: Enables applications to act as stream processors, transforming input streams from topics into output streams.
• Connector API: Used to build and run reusable producers/consumers that connect Kafka topics to external systems and data stores (e.g., relational databases).

#### 3. What are the primary responsibilities of a Kafka broker?
**Answer:**
The key responsibilities include: • Message Management: Receiving messages from producers and assigning them to partitions. • Data Storage: Maintaining topics divided into partitions. • Replication: Duplicating partition data across brokers for high availability. • Metadata Management: Tracking topic configurations, partition locations, and consumer offsets.

#### 4. What challenges are associated with Kafka?
**Answer:**
Despite its high performance and scalability, Kafka has a steep learning curve. Configuring and managing a Kafka cluster can be complex, and developers must carefully design their applications to handle issues like partitioning, replication, and consumer rebalancing.

#### 5. What defines a Single Kafka Cluster architecture?
**Answer:**
A Single Kafka Cluster architecture centralizes all brokers, metadata, topics, and partitions within one unified system. It is simpler to deploy and manage but may encounter scalability and fault tolerance issues as the workload grows.

#### 6. What is Apache Kafka?
**Answer:**
Apache Kafka is an open‑source distributed event streaming platform used for high-performance data pipelines, streaming analytics, and data integration. It is architected as a distributed commit log providing durable, ordered, and scalable event storage.

#### 7. What is a Kafka broker?
**Answer:**
A Kafka broker is the core computational node in the Apache Kafka ecosystem. It stores topic partitions (immutable log files), manages message ingestion from producers, and serves consumer requests—all while handling replication and metadata management to ensure fault tolerance and scalability.

#### 8. What is a Kafka cluster?
**Answer:**
A Kafka cluster is a group of interconnected Kafka brokers that work together to manage real‑time data streams. It handles tasks such as partitioning, replication, and message processing, ensuring high availability and scalability.

#### 9. What is a Kafka partition, and why is it important in Kafka’s architecture?
**Answer:**
A Kafka partition is an append-only, ordered log file that stores a subset of a topic’s data. Partitions are crucial because they enable horizontal scalability (by distributing data across multiple brokers), parallel processing by consumers, and fault tolerance through replication.

#### 10. What is a Kafka topic?
**Answer:**
A Kafka topic is the fundamental organizational unit in Apache Kafka. It serves as a logical channel for grouping messages (or events) that relate to a specific business objective. Topics allow producers to write messages and consumers to read them, forming the basis of data flow in Kafka.

#### 11. What is the role of a Kafka broker within a cluster?
**Answer:**
Kafka brokers are independent processes running on separate machines. They store data partitions, manage client requests, and communicate with other brokers to distribute data and metadata, ensuring fault tolerance and scalability.


### 🟡 Mid Level

#### 1. Compare single-cluster and multi-cluster architectures in terms of fault tolerance and scalability.
**Answer:**
• Single Cluster: Easier to manage with centralized operations but more vulnerable to system-wide failures and scalability limits.
• Multi-Cluster: Offers better fault isolation and scalability by separating workloads, though it increases operational complexity and cost.

#### 2. How does workload segregation improve multi-cluster deployments in Kafka?
**Answer:**
By dedicating separate clusters to different workloads, workload segregation reduces resource contention, enhances performance, and isolates failures. Each cluster can be scaled independently, ensuring optimized resource allocation and improved overall system resilience.

#### 3. Redis 6.0 使用多线程是怎么回事？
**Answer:**
Redis 6.0 的多线程用于处理网络数据的读写和协议解析，但执行命令依然是单线程的。这样做的原因是 Redis 的性能瓶颈主要在于网络 IO 而非 CPU，引入多线程可以提升 IO 读写的效率，从而大幅提升整体性能。

#### 4. What is the purpose of leader election in ZooKeeper for Kafka?
**Answer:**
ZooKeeper handles leader election by tracking the current leader broker in the Kafka cluster. If the leader fails, ZooKeeper triggers a new election to promptly designate a replacement, ensuring uninterrupted cluster operations.

#### 5. What metadata do Kafka brokers manage, and why is it important?
**Answer:**
Brokers manage metadata such as the list of topics, the number of partitions per topic, the location of each partition across brokers, and consumer offsets. This metadata is crucial for maintaining the structure of the data, coordinating consumers, and enabling efficient data retrieval and recovery.


### 🔴 Senior Level

#### 1. Compare the two methods of Kafka metadata management (ZooKeeper vs. KRaft).
**Answer:**
ZooKeeper-based: Traditionally, Kafka stored metadata in Apache ZooKeeper, which handled configuration, naming, and coordination.
KRaft mode: Newer Kafka clusters can use KRaft mode, where metadata is stored internally in a dedicated metadata topic. KRaft eliminates the need for ZooKeeper and reduces bottlenecks, simplifying the architecture and improving performance.

#### 2. What characterizes a Multiple Kafka Cluster architecture?
**Answer:**
In a Multiple Kafka Cluster architecture, workloads are distributed across separate clusters. This decentralized approach enhances fault tolerance and scalability by isolating data streams, though it increases configuration and operational complexity.

#### 3. What is a stretched Kafka cluster?
**Answer:**
A stretched cluster is a single logical Kafka cluster that spans multiple geographical locations or availability zones. Replicas of partitions are distributed across different data centers to improve redundancy and protect against localized catastrophic failures.

#### 4. 无底洞问题是什么？如何解决？
**Answer:**
2010年，Facebook的Memcache节点已经达到了3000个，承载着TB级别的缓存数据。开发和运维人员发现了一个问题，为了满足业务要求添加了大量新Memcache节点，但是发现性能不仅没有好转反而下降了，当时将这种现象称为缓存的“无底洞”现象。
为什么会产生这种现象：
键值数据库由于通常采用哈希函数将 key 映射到各个节点上，造成key的分布与业务无关，但是由于数据量和访问量的持续增长，造成需要添加大量节点做水平扩容，导致键值分布到更多的 节点上，所以无论是Memcache还是Redis的分布式，批量操作通常需要从不同节点上获取，相比于单机批量操作只涉及一次网络操作，分布式批量操作会涉及多次网络时间。
无底洞问题如何优化：
客户端一次批量操作会涉及多次网络操作，意味着批量操作会随着节点的增多，耗时不端增大。网络连接数变多，对节点的性能也有一定影响。
常见的优化思路如下：
1. 命令本身的优化，例如优化操作语句等。
2. 减少网络通信次数。
3. 降低接入成本，例如客户端使用长连/连接池、NIO等。


## 📂 Category: Big Data (1 cards)

### 🟡 Mid Level

#### 1. What is Apache YARN?
**Answer:**
YARN (Yet Another Resource Negotiator) is a large-scale, distributed operating system for big data applications sitting between HDFS and processing engines. It consists of a master daemon known as Resource Manager, slave daemons called Node Managers, and Application Masters to monitor processing operations.


## 📂 Category: Big Data Architecture (5 cards)

### 🟢 Junior Level

#### 1. What are the core responsibilities of a Hadoop HDFS DataNode?
**Answer:**
A DataNode manages physical data storage for the file system. Its tasks include block replica creation, deletion, and replication according to NameNode instructions. It also sends periodic heartbeats to the NameNode to report node health and block inventories.


### 🟡 Mid Level

#### 1. How does Spark execute applications on YARN?
**Answer:**
When Spark runs on YARN, the cluster manager, resource management, scheduling, and security are fully controlled by YARN. It supports two primary deployment modes: Cluster Mode (Spark driver runs inside a YARN application master process) and Client Mode (Spark driver runs locally on the submitter client machine).

#### 2. What are the core responsibilities of the Hadoop HDFS NameNode?
**Answer:**
The NameNode manages the file system namespace, regulates client file access, and executes directory/file metadata operations (naming, opening, closing). It tracks block placement via continuous heartbeats and block reports from DataNodes and enforces cluster replication factors.

#### 3. What is the architecture of Apache Hive?
**Answer:**
Apache Hive consists of four major components:
1. Hive Client: Interfaces (CLI, JDBC/ODBC, WebUI) to submit queries.
2. Hive Services: Driver, Compiler, Optimizer, and Execution Engine that parse and plan queries.
3. Processing and Resource Management: Integration with underlying cluster engines like YARN or MapReduce.
4. Distributed Storage: HDFS or cloud object storage holding the underlying data files.

#### 4. What is the role of the Resource Manager (RM) in YARN?
**Answer:**
The Resource Manager (RM) is the master daemon of Apache YARN. It manages global assignments of compute resources (CPU and memory) across all applications and arbitrates system resources between competing applications.


## 📂 Category: Big Data Ecosystem (6 cards)

### 🟢 Junior Level

#### 1. What is Apache Spark?
**Answer:**
Apache Spark is an open-source computational framework for processing and analyzing massive datasets across commodity servers. The ecosystem includes Spark Core, Spark SQL, Spark Streaming, Spark MLlib, Spark GraphX, and SparkR, supporting both batch and streaming workflows.

#### 2. What is Hadoop?
**Answer:**
Hadoop is an open-source distributed processing framework that manages data processing and storage for big data applications in clusters. It consists of a Master/Slave architecture using HDFS for storage and YARN for data processing.

#### 3. What is Hive?
**Answer:**
Hive is a data warehousing tool used to analyze data and load structured data into Hive tables for analysis.

#### 4. What is Sqoop2?
**Answer:**
Sqoop2 is a bulk data transfer tool used to import and export data between structured datastores (relational databases, enterprise data warehouses, NoSQL systems) and HDFS, Hive, or HBase.


### 🟡 Mid Level

#### 1. What is Apache Impala?
**Answer:**
Apache Impala provides high-performance, low-latency SQL queries on data stored in Hadoop file formats, enabling interactive exploration rather than long batch jobs. Developed in C++, the Impala server is a distributed, massively parallel processing (MPP) database engine.

#### 2. What is a namespace ID in HDFS?
**Answer:**
When an HDFS instance is formatted, the NameNode generates a unique namespace ID. When DataNodes first connect, they bind to this namespace ID and establish a unique 'storage ID' identifying that specific DataNode in the HDFS instance.


## 📂 Category: Caching (4 cards)

### 🟢 Junior Level

#### 1. 缓存预热有哪些常见做法？
**Answer:**
缓存预热是指系统上线前或运行初期，提前将数据库中的数据加载到缓存中。常见做法包括：1. 编写专门的缓存刷新页面或管理后台接口，在上线时手动触发；2. 数据量较小时，在项目启动时自动加载；3. 通过定时任务周期性刷新缓存。


### 🟡 Mid Level

#### 1. 什么是缓存热点key重建问题？如何解决？
**Answer:**
当一个高并发的缓存Key失效时，大量线程同时去重建缓存（如执行复杂SQL、多次IO），会导致后端负载骤增甚至应用崩溃。解决方案包括：1. 互斥锁（Mutex Key）：只允许一个线程构建缓存，其他线程等待；2. 永不过期：物理层不过期，逻辑上为每个Value设置过期时间，由独立线程异步更新缓存。

#### 2. 如何保证本地缓存和分布式缓存的一致性？
**Answer:**
可以采用以下几种方式：
1. 采用Redis自身的Pub/Sub机制：分布式集群的所有节点订阅删除本地缓存频道，删除Redis缓存的节点同时发布删除本地缓存消息，订阅者订阅到消息后，删除对应的本地key。注意Redis的发布订阅不是可靠的，不能保证一定删除成功。
2. 引入专业的消息队列，比如RocketMQ，保证消息的可靠性，但增加了系统的复杂度。
3. 设置合适的过期时间兜底，本地缓存可以设置相对短一些的过期时间。

#### 3. 如何保证缓存和数据库数据的最终一致性？
**Answer:**
根据CAP理论，在保证可用性和分区容错性的前提下，无法保证一致性，所以缓存和数据库的绝对一致是不可能实现的，只能尽可能保证缓存和数据库的最终一致性。


## 📂 Category: Caching & Storage (1 cards)

### 🔴 Senior Level

#### 1. What are the common causes of Redis blocking and how can they be resolved?
**Answer:**
Redis blocking typically occurs due to high algorithmic complexity commands (> O(N) on large objects), CPU saturation, or persistence/OS-level blocks. 

1. Slow Queries:
- Detection: Use `slowlog get {n}` to find slow commands.
- Mitigation: Avoid O(N) commands like `KEYS`, `SORT`, or heavy `HGETALL`. Use alternative commands like `HMGET` and split large objects into smaller chunks.

2. CPU Saturation:
- Detection: Run `redis-cli -h {ip} -p {port} --stat` to check OPS. If OPS reaches limits (> tens of thousands), scale out via clustering.

3. Persistence and OS Bottlenecks:
- Fork Blocking: RDB and AOF rewrites require main thread `fork()`, which can be slow with massive shared memory.
- AOF Fsync Blocking: Background threads performing `fsync` can cause the main thread to block if the disk cannot keep up and fsync lags by > 2 seconds.
- Transparent HugePages (THP): If enabled, copy-on-write memory page size jumps from 4KB to 2MB, amplifying write latency significantly. Disable THP at the OS level.


## 📂 Category: Cluster Architecture (2 cards)

### 🟡 Mid Level

#### 1. Redis 集群（Cluster）的核心功能和优势是什么？
**Answer:**
1. 数据分区（分片）：将数据分散到多个节点，突破单机内存限制，大幅增加存储容量；每个主节点都可以对外提供读写服务，大大提高了集群的响应能力。
2. 高可用：集群支持主从复制和主节点的自动故障转移（与哨兵类似），当任一节点发生故障时，集群仍然可以对外提供服务。


### 🔴 Senior Level

#### 1. How does an active-active Kafka cluster operate?
**Answer:**
An active-active cluster comprises two homogeneous Kafka clusters that perform bi‑directional, asynchronous mirroring. Both clusters actively serve client requests, ensuring high availability while balancing load and minimizing access delays.


## 📂 Category: Cluster Management (3 cards)

### 🟡 Mid Level

#### 1. What are Fair and Capacity Schedulers?
**Answer:**
1-Fair Scheduler: Assigns resources to jobs so that all jobs get, on average, an equal share of resources over time. When a single job runs, it uses the entire cluster; new tasks share space as they arrive.
2-Capacity Scheduler: Allows sharing of a large cluster while giving each organization a minimum capacity guarantee. Unused capacity can be accessed by other organizations for elasticity.

#### 2. What are the core components of a Resource Manager in YARN?
**Answer:**
A) Scheduler: Responsible for allocating resources to running applications based on constraints and policies.
B) Application Manager: Manages running Application Masters in the cluster, including starting application masters, monitoring them, and restarting them on different nodes in case of failures.


### 🔴 Senior Level

#### 1. Compare the Fair Scheduler and Capacity Scheduler in Hadoop.
**Answer:**
• Fair Scheduler: Assigns resources to jobs over time so that all applications share an equal share of resources. Ideal for equal progress, jobs with high data locality needs, or pools with high utilization variance.
• Capacity Scheduler: Allows a Hadoop cluster to run as a shared, multi-tenant cluster with dedicated capacity per queue/tenant. Ideal when scheduler determinism, memory-based scheduling, and strict resource guarantees are required.


## 📂 Category: Cluster Metadata & KRaft (1 cards)

### 🔴 Senior Level

#### 1. What does KRaft stand for and why was it introduced in Kafka?
**Answer:**
KRaft stands for Kafka Raft. It was introduced to eliminate Kafka’s dependency on ZooKeeper by replacing a single controller with a distributed quorum of controllers. This change aims to improve fault tolerance, simplify configuration management, and reduce operational overhead.


## 📂 Category: Consumer Groups (3 cards)

### 🟡 Mid Level

#### 1. Describe the Range partition assignment strategy in Kafka consumer groups.
**Answer:**
In the Range strategy, partitions are assigned to consumers in contiguous ranges based on partition order. For example, if a topic has partitions 0-3 and two consumers, consumer 0 gets partitions 0-1 and consumer 1 gets 2-3. This can lead to uneven distribution if the partition count is not divisible by the consumer count.

#### 2. Describe the role of the group coordinator in a Kafka consumer group.
**Answer:**
The group coordinator (a dedicated Kafka broker) manages consumer membership and partition assignments. It triggers rebalances when consumers join or leave, monitors heartbeats to detect failures, and ensures that each partition is assigned to at most one consumer in the group.


### 🔴 Senior Level

#### 1. Explain how partition assignment works during a rebalance in Kafka consumer groups.
**Answer:**
During a rebalance, the group coordinator collects metadata from all active consumers and reassigns partitions based on the configured assignment strategy (e.g., Range, RoundRobin, CooperativeSticky). This process ensures that partitions are cleanly redistributed among available consumers without overlap.


## 📂 Category: Consumer Management (3 cards)

### 🟢 Junior Level

#### 1. What is a Kafka consumer group?
**Answer:**
A Kafka consumer group is a collection of one or more consumer instances that work together to consume messages from one or more Kafka topics. In a group, each partition of a topic is consumed by only one consumer, ensuring that messages are processed efficiently across the group.

#### 2. What is a consumer offset in Kafka and why is it important?
**Answer:**
A consumer offset is a pointer that indicates the last message a consumer has processed within a partition. Stored in Kafka’s internal topic (__consumer_offsets), it allows consumers to resume processing from the correct position after restarts or failures, preventing duplicate processing or data loss.


### 🟡 Mid Level

#### 1. What is consumer rebalancing in Kafka, and why is it necessary?
**Answer:**
Consumer rebalancing is the protocol by which Kafka redistributes partition ownership among consumer instances within a group when topology changes occur (such as a consumer joining, leaving, or crashing, or partitions being added). It ensures high availability and load distribution, though older protocols (Eager) caused a 'stop-the-world' pause for all consumers.


## 📂 Category: Consumers (3 cards)

### 🟡 Mid Level

#### 1. What is the round-robin assignor for consumer groups, and what advantage does it offer?
**Answer:**
The round-robin assignor cycles through the available partitions and assigns them one-by-one to each consumer. This approach tends to distribute the partitions more evenly, especially when dealing with topics having a variable number of partitions.

#### 2. What is the significance of the internal topic __consumer_offsets in Kafka?
**Answer:**
The __consumer_offsets topic stores each consumer group’s offsets for each partition. This internal mechanism is crucial for tracking consumption progress, enabling consumers to resume processing from the last committed offset in the event of a failure or restart.

#### 3. What is the sticky assignor, and how does it benefit consumer groups during rebalancing?
**Answer:**
The sticky assignor minimizes partition movement between rebalances by preserving as many existing partition assignments as possible. This leads to fewer disruptions and more stable processing in consumer groups.


## 📂 Category: Consumers & Consumer Groups (6 cards)

### 🟢 Junior Level

#### 1. How does the consumer group concept relate to Kafka offsets?
**Answer:**
Each consumer group tracks its own set of committed offsets for the partitions it consumes. This ensures that, even when multiple consumers share the workload within a group, each partition's messages are processed only once per group and progress is tracked independently across different groups.

#### 2. What is a consumer group and how does it function with Kafka topics?
**Answer:**
A consumer group is a collection of consumers that work together to process messages from Kafka topics. The partitions of a topic are distributed among the consumers in the group, ensuring that each message is processed by only one consumer. This design provides scalability and fault tolerance, as the workload can be rebalanced if consumers join or leave.


### 🟡 Mid Level

#### 1. How do the Range and Round Robin partition assignment strategies differ in Kafka consumers?
**Answer:**
The Range assignor divides the list of topic partitions into contiguous ranges per topic for each consumer (meaning consumers assigned multiple topics might take extra partitions on the first topics). The Round Robin assignor collects all available partition-topic pairs into a single flat list and assigns them cyclically to consumers one by one, resulting in a more balanced distribution when multiple topics are consumed.

#### 2. How does the "at least once" delivery guarantee work in relation to offset commits?
**Answer:**
In an "at least once" delivery semantic, consumers commit offsets only *after* they have successfully processed messages. This minimizes the risk of missing messages; however, if a failure occurs after processing but before the offset is committed, those messages will be re-processed upon consumer recovery.

#### 3. What are the two common partition assignment strategies in Kafka consumer groups?
**Answer:**
The two common strategies are: Range: Assigns consecutive partitions to each consumer. Round Robin: Distributes partitions evenly by cycling through the list of consumers, assigning one partition at a time.

#### 4. What happens when the number of partitions is greater than the number of consumers in a group?
**Answer:**
When there are more partitions than consumers, the available partitions are divided among the consumers. This means one consumer might be assigned multiple partitions, enabling the group to process more messages concurrently.


## 📂 Category: Consumers & Offsets (1 cards)

### 🟢 Junior Level

#### 1. How is consumer lag calculated in Kafka, and what role do offsets play in message ordering?
**Answer:**
Consumer lag is calculated as the difference between the log-end offset (latest available message) and the committed offset (last processed message). Offsets preserve the sequential order of messages within a partition's log, allowing consumers to process them reliably in the order produced.


## 📂 Category: Coordination (4 cards)

### 🟡 Mid Level

#### 1. What is Apache ZooKeeper?
**Answer:**
Apache ZooKeeper is a centralized coordination service for distributed systems. In legacy Kafka architectures, it provides essential functions—such as broker registry, controller election, topic configurations, and quota management—to simplify operations in distributed environments.

#### 2. What is a ZooKeeper session?
**Answer:**
A session is the active stateful connection between a client (such as a Kafka broker) and the ZooKeeper ensemble. When a client connects, it receives a unique session ID and must send periodic heartbeats (pings) to keep the session active. Failure to do so within the session timeout leads to session expiration and cleanup of ephemeral nodes.

#### 3. What is a znode in ZooKeeper?
**Answer:**
A znode is a data node within ZooKeeper’s hierarchical namespace. Much like a file in a file system, each znode can store data, have child znodes, and is uniquely identified by its absolute path. Znodes can be persistent or ephemeral.


### 🔴 Senior Level

#### 1. What is a ZooKeeper quorum and why is it important?
**Answer:**
A quorum is the minimum number of ZooKeeper nodes (calculated as N/2 + 1, where N is the total number of nodes) that must be operational for the ensemble to process requests and maintain consistency. It prevents split-brain scenarios and ensures fault tolerance up to N/2 - 1 failures.


## 📂 Category: Data Consistency (1 cards)

### 🔴 Senior Level

#### 1. 如何保证缓存和数据库数据的最终一致性？
**Answer:**
常用的策略和方案包括：
1. 选择合适的缓存更新策略：采用“先删除缓存，再更新数据库”或“先更新数据库，再删除缓存”。推荐删除缓存而不是直接更新，因为速度更快、读到脏数据的概率更低。
2. 引入消息队列保障：利用消息队列的重试机制，将删除失败的 key 丢进队列重试删除。
3. 数据库订阅 + 消息队列（如 Canal）：监听数据库 binlog 获取变更数据并异步执行缓存删除，降低业务侵入性但提升了系统复杂度。
4. 延时双删：在第一次删除缓存并更新数据库后，间隔一段时间再次删除缓存，防止并发写脏数据。
5. 设置缓存过期时间保底：给缓存设置合理的过期时间，作为最终兜底方案。


## 📂 Category: Data Integration (1 cards)

### 🟡 Mid Level

#### 1. What are the primary tools and execution models in Sqoop 2?
**Answer:**
• Sqoop Import Tool: Imports individual tables from an RDBMS to HDFS by dividing the main task into subtasks handled internally by parallel Map tasks.
• Sqoop Export Tool: Exports a set of files from HDFS back to an RDBMS by mapping jobs into Map tasks that fetch data chunks and push them to structured data destinations.


## 📂 Category: Data Processing (4 cards)

### 🟢 Junior Level

#### 1. What are the primary components of Apache Spark?
**Answer:**
• Driver Program: Uses a SparkContext object as an entry point to connect to a cluster, launches executors on worker nodes, and sends application code.
• Executor: A JVM process running on worker nodes that processes jobs submitted by the driver program.
• Task: Subcomponents of a data processing job that are split and executed by executor processes on worker nodes.


### 🟡 Mid Level

#### 1. What are the key architectural features and use cases of Apache Hive?
**Answer:**
Apache Hive is an OLAP data warehousing system built on top of HDFS, HBase, or S3. It uses a declarative SQL-like language (HiveQL) supporting ETL operations, table partitioning, and bucketing. It stores schema in a metastore, processes petabyte-scale data, supports multiple engines (MapReduce, Tez, Spark), and delegates fault tolerance to HDFS.


### 🔴 Senior Level

#### 1. Compare Cluster Deployment Mode vs. Client Deployment Mode in Spark on YARN.
**Answer:**
• Cluster Deployment Mode: The Spark driver runs inside the ApplicationMaster process on a cluster host. YARN starts the container for the ApplicationMaster, which requests resources and coordinates execution. Does not support spark-shell interactively.
• Client Deployment Mode: The Spark driver runs on the client machine where the job is submitted. The ApplicationMaster's sole responsibility is requesting executor containers from YARN. Supports interactive use via spark-shell.

#### 2. What are the core components of Apache Impala and their roles?
**Answer:**
• Impala Daemon (ImpalaD): Core component running on worker nodes. Accepts queries (from shell, Hue, JDBC/ODBC), parallelizes and distributes work, and communicates health to the StateStore.
• StateStore: Checks the health of all Impala daemons continuously and relays findings so unhealthy nodes can be avoided.
• Catalog Service: Relays metadata changes from SQL statements to all Impala daemons, reducing the need for manual REFRESH/INVALIDATE METADATA commands.


## 📂 Category: Data Structures (8 cards)

### 🟢 Junior Level

#### 1. Redis 有哪些基本数据结构及典型使用场景？
**Answer:**
1. string（字符串）：最基础结构，可存数字、文本、二进制数据（最大512MB）。场景：缓存、计数器、共享Session、限流。
2. hash（哈希）：键值对结构。场景：缓存用户对象信息。
3. list（列表）：有序字符串列表，可充当栈和队列。场景：消息队列、文章列表。
4. set（集合）：无序不重复字符串集合。场景：标签（tag）、共同关注。
5. sorted set（有序集合）：带权重的有序集合。场景：用户点赞统计、用户排行榜。


### 🟡 Mid Level

#### 1. Redis 如何实现延迟队列？
**Answer:**
可以使用 zset（有序集合）结构来实现。利用设置好的时间戳作为 score 进行排序，通过 zadd 命令持续往内存生产任务。再利用 zrangebyscore 查询符合条件的所有待处理任务，通过循环执行队列任务即可。

#### 2. 压缩列表 (ziplist) 了解吗？
**Answer:**
压缩列表是 Redis 为了节省内存而使用的一种数据结构，是由一系列特殊编码的连续内存块组成的顺序型数据结构。一个压缩列表可以包含任意多个节点（entry），每个节点可以保存一个字节数组或者一个整数值。压缩列表由以下几部分组成：
1. zlbytes：记录整个压缩列表占用的内存字节数。
2. zltail：记录压缩列表表尾节点距离压缩列表的起始地址有多少字节。
3. zllen：记录压缩列表包含的节点数量。
4. entryX：列表节点。
5. zlend：用于标记压缩列表的末端。

#### 3. 布隆过滤器（Bloom Filter）的原理及优缺点是什么？
**Answer:**
布隆过滤器是一个由二进制位数组和K个哈希函数组成的连续数据结构。当元素加入时，通过K个哈希函数将其映射到位数组的K个点并置为1。判断是否存在时，如果对应位全为1则“可能存在”，只要有一个不为1则“一定不存在”。缺点：存在一定的误判率（哈希冲突），且默认不支持删除元素。

#### 4. 快速列表 quicklist 了解吗？
**Answer:**
Redis 早期版本存储 list 列表数据结构使用的是压缩列表 ziplist 和普通的双向链表 linkedlist，即元素少时使用 ziplist，元素多时使用 linkedlist。但考虑到链表的附加空间相对较高（64位操作系统下 prev 和 next 指针要占去 16 个字节），另外每个节点的内存都是单独分配，会造成内存的碎片化，影响内存管理效率。后来 Redis 新版本（3.2）对列表数据结构进行了改造，使用 quicklist 代替了 ziplist 和 linkedlist。quicklist 是综合考虑了时间效率与空间效率引入的新型数据结构，它由 list 和 ziplist 组合而成，是一个由 ziplist 充当节点的双向链表。

#### 5. 跳跃表（SkipList）是如何实现的？它的内部原理与应用场景是什么？
**Answer:**
跳跃表是一种有序数据结构，通过在每个节点中维持多个指向其他节点的指针，从而达到快速访问节点的目的。为什么 Redis 在 Sorted Set (zset) 中使用跳跃表而不是红黑树？1. 性能考量：在高并发情况下，树形结构需要执行复杂的 rebalance 操作，涉及整树或较大范围的调整，而跳跃表的变动通常只涉及局部指针修改。2. 实现考量：在复杂度和性能相当的情况下，跳跃表实现更简单直观。跳跃表节点包含：层（level，通过幂次定律随机生成1到32之间的值作为高度）、前进指针（level[i].forward，用于从表头向表尾访问）、跨度（span，用于记录两个节点间的距离以计算rank排名）、分值（score，double类型浮点数，从小到大排序）以及成员对象（obj，指向保存SDS值的字符串对象）。


### 🔴 Senior Level

#### 1. Redis 的 SDS 和 C 中字符串相比有什么优势？
**Answer:**
C 语言字符串以 '\0' 结尾且不记录长度，存在以下问题：获取长度复杂度为 O(N)、容易造成缓冲区溢出、无法保存包含 '\0' 的二进制数据。Redis 的简单动态字符串（SDS）优势包括：1. 记录 len 属性，获取长度复杂度为 O(1)。2. 自动扩展空间，通过空间预分配和惰性空间释放机制有效降低内存分配次数，避免缓冲区溢出。3. 二进制安全，可以保存图片、音频等任意二进制数据。

#### 2. 字典是如何实现的？Rehash 了解吗？
**Answer:**
字典是 Redis 服务器中最为频繁的复合型数据结构。除了 hash 结构的数据会用到字典外，整个 Redis 数据库的所有 key 和 value 也组成了一个全局字典，还有带过期时间的 key 也是一个字典（存储在 RedisDb 数据结构中）。
字典结构类似于 Java 中的 HashMap，采用哈希与运算计算下标位置；通过“数组 + 链表”的链地址法来解决哈希冲突。
字典是如何扩容的：
字典结构内部包含两个 hashtable，通常情况下只有一个哈希表 ht[0] 有值，在扩容的时候，把 ht[0] 里的值 rehash 到 ht[1]，然后进行渐进式 rehash ——所谓渐进式 rehash，指的是这个 rehash 的动作并不是一次性、集中式地完成的，而是分多次、渐进式地完成的。待搬迁结束后，h[1] 就取代 h[0] 存储字典的元素。


## 📂 Category: Delivery Semantics (1 cards)

### 🟢 Junior Level

#### 1. How is the "at most once" delivery guarantee implemented with respect to offsets?
**Answer:**
In the "at most once" scenario, consumers commit offsets immediately upon receiving messages—often before processing. This ensures messages are never processed twice, though it risks message loss if a failure occurs during processing.


## 📂 Category: Distributed Systems (4 cards)

### 🔴 Senior Level

#### 1. Application Master (AM)
**Answer:**
One application master runs per application. It negotiates resources from the resource manager and works with the node manager. The AM acquires containers from the RM's Scheduler before contacting the corresponding NMs to start the application's tasks.

#### 2. How does the quorum journal manager work with fencing in distributed systems?
**Answer:**
To prevent split-brain scenarios, the journal manager uses epoch numbers—monotonically increasing integers that are assigned unique values upon state changes. A primary node generates epoch numbers and includes them in RPC requests to the Quorum Journal Manager (QJM). If a failover or restart occurs, the epoch number increases, and any older node with a lower epoch is fenced out and considered invalid.

#### 3. Redis 实现分布式锁的演进过程及最终方案是什么？
**Answer:**
1. V1 (setnx)：使用 setnx 占坑，用完 del 释放。缺点：若逻辑中途异常导致 del 未执行，会陷入死锁。
2. V2 (锁超时释放)：拿锁后加 expire 过期时间。缺点：若在 setnx 和 expire 之间进程挂掉（如掉电或被kill），expire 无法执行仍会导致死锁（两步操作非原子性）。
3. V3 (set命令扩展参数)：在 Redis 2.8 中引入了 set 命令的扩展参数，使 setnx 和 expire 可以作为一条原子指令执行。实际开发中推荐直接使用成熟的轮子 —— Redisson。

#### 4. 分布式集群中的数据分区方案有哪些？各有何优缺点？
**Answer:**
常见的数据分区方案包括：
1. 节点取样/取余分区（Modulo Partitioning）：使用特定数据（如键或用户ID）的 hash 值取余：hash(key) % N。优点是非常容易理解和实现；缺点是当节点数量变化（扩容或缩容）时，数据节点映射关系需要重新计算，会导致大规模的数据重新迁移。
2. 一致性哈希分区（Consistent Hashing）：将整个 Hash 值空间组织成一个虚拟圆环，将缓存节点的 IP 或主机名做 Hash 后放置在环上。Key 经过 Hash 后定位到环上的位置，然后顺时针行走的第一个缓存节点即为目标节点。解决了部分扩缩容痛点。
3. 虚拟槽分区（Virtual Slot Partitioning）：在一致性哈希的基础上引入虚拟节点的概念（如 Redis Cluster 的 slot 槽）。槽是介于数据和实际节点之间的虚拟概念，每个实际节点包含一定数量的槽，哈希值落在一定范围内的数据映射到对应的槽中。


## 📂 Category: Fault Tolerance (1 cards)

### 🟢 Junior Level

#### 1. Describe how Kafka brokers ensure fault tolerance.
**Answer:**
Fault tolerance in Kafka is provided by data replication. Each partition's data is replicated across multiple brokers. If the leader broker handling a partition fails, one of the follower brokers is automatically elected as the new leader, ensuring continuous data availability.


## 📂 Category: HDFS (1 cards)

### 🔴 Senior Level

#### 1. What is the Role of Journal nodes in Namenode HA?
**Answer:**
Journal nodes are distributed systems used to store HDFS NameNode edits to keep Active and Standby NameNodes in sync and avoid a split-brain scenario. The Active NameNode writes edits to journal nodes and commits only when replicated to all journal nodes. The Standby NameNode reads from these edits. While ZKFC handles active election, fencing methods must still be configured to prevent out-of-date writes from a previous Active NameNode.


## 📂 Category: Hadoop Architecture (1 cards)

### 🔴 Senior Level

#### 1. What is Hadoop NameNode fencing and why is it required?
**Answer:**
Fencing ensures only one NameNode is active at a time to prevent split-brain scenarios when using a shared edits directory. During a failover, the fencing method ensures the previous active NameNode no longer accesses the shared edits. Cloudera Manager defaults to a shell fencing method (shell(true)). With Quorum-based Storage, only one NameNode can write to JournalNodes. Explicit fencing methods (like agent-based fencers) prevent narrow windows of serving stale read responses.


## 📂 Category: High Availability (5 cards)

### 🟡 Mid Level

#### 1. Redis Sentinel（哨兵）集群中领导者（Leader）节点是如何选举出来的？
**Answer:**
1. 当某个在线的 Sentinel 节点确认主节点客观下线（Subjectively/Objectively Down）时，它会向其他 Sentinel 节点发送 `sentinel is-master-down-by-addr` 命令，要求将自己设置为领导者。
2. 收到命令的 Sentinel 节点如果尚未同意过其他 Sentinel 的该请求，则会同意，否则拒绝。
3. 如果某个 Sentinel 节点发现自己获得的票数大于等于设定的 quorum 且满足 `num(sentinels)/2 + 1`，那么它将成功当选为领导者。
4. 如果此轮选举没有选出领导者，系统将等待进入下一轮选举周期重试。


### 🔴 Senior Level

#### 1. Redis Sentinel 的故障转移（Failover）流程是怎样的？
**Answer:**
1. Sentinel节点之间通过Raft算法选出一个领导者Sentinel节点进行故障转移工作。
2. 在从节点列表中选出一个节点作为新的主节点（过程较复杂）。
3. Sentinel领导者节点会对第一步选出来的从节点执行 slaveof no one 命令使其成为主节点。
4. Sentinel领导者节点会向剩余的从节点发送命令，让它们成为新主节点的从节点。
5. Sentinel节点集合会将原来的主节点更新为从节点，并保持对其关注，当其恢复后命令它去复制新的主节点。

#### 2. Redis Sentinel（哨兵）实现原理及核心定时任务是什么？
**Answer:**
哨兵模式通过哨兵节点完成对数据节点的监控、下线和故障转移。主要包含三个定时监控任务：1. 每隔10秒，每个Sentinel节点向主节点和从节点发送 info 命令获取最新的拓扑结构。2. 每隔2秒，每个Sentinel节点会向Redis数据节点的 sentinel:hello 频道上发送该Sentinel节点对于主节点的判断以及当前Sentinel节点的信息。3. 每隔1秒，每个Sentinel节点会向主节点、从节点、其余Sentinel节点发送一条ping命令做一次心跳检测，来确认这些节点当前是否可达。

#### 3. Redis主观下线（SDOWN）和客观下线（ODOWN）的区别是什么？
**Answer:**
1. 主观下线（SDOWN）：每个Sentinel节点每隔1秒对主节点、从节点、其他Sentinel节点发送ping命令做心跳检测，当这些节点超过 down-after-milliseconds 没有进行有效回复，Sentinel节点就会对该节点做失败判定。
2. 客观下线（ODOWN）：当Sentinel主观下线的节点是主节点时，该Sentinel节点会通过 sentinel is-master-down-by-addr 命令向其他Sentinel节点询问对主节点的判断，当达到指定数量（quorum）的Sentinel节点认为主节点有问题时，该Sentinel节点会做出客观下线的决定。

#### 4. 新的主节点是怎么被挑选出来的？
**Answer:**
选出新的主节点，大概分为这么几步：
1. 过滤：“不健康”（主观下线、断线）、5秒内没有回复过Sentinel节点ping响应、与主节点失联超过down-after-milliseconds*10秒的节点。
2. 选择slave-priority（从节点优先级）最高的从节点列表，如果存在则返回，不存在则继续。
3. 选择复制偏移量最大的从节点（复制的最完整），如果存在则返回，不存在则继续。
4. 选择runid最小的从节点。


## 📂 Category: Infrastructure & Networking (1 cards)

### 🟡 Mid Level

#### 1. What are the core components and default network ports for an enterprise Hadoop ecosystem (HDFS, YARN, Hive, Kafka, ZooKeeper)?
**Answer:**
Key service default ports include:
- Cloudera Manager Admin (HTTP/HTTPS): 7180 / 7183
- HDFS NameNode: 8020, 9870 (WebUI)
- YARN Resource Manager: 8032 / 9870
- ZooKeeper Server: 2181
- Kafka Broker (Plain / TLS): 9092 / 9093
- Hive Metastore / HiveServer2: 9083 / 10000
- MySQL: 3306


## 📂 Category: KRaft (2 cards)

### 🔴 Senior Level

#### 1. What is the role of the controller quorum in KRaft?
**Answer:**
The controller quorum in KRaft is a group of controllers that jointly manage the cluster’s metadata and coordinate operations. This distributed approach ensures that metadata is consistently replicated and available, even if individual controllers fail.

#### 2. What performance benefits does KRaft provide over the traditional ZooKeeper-based architecture?
**Answer:**
KRaft reduces operational overhead by eliminating a separate ZooKeeper cluster, which simplifies deployment and maintenance. This leads to lower latency in metadata operations, improved system throughput, and a reduced risk of performance bottlenecks.


## 📂 Category: KRaft & Metadata (2 cards)

### 🔴 Senior Level

#### 1. How does KRaft enhance fault tolerance, eliminate ZooKeeper, and simplify metadata management?
**Answer:**
KRaft (Kafka Raft) integrates metadata coordination directly into Kafka brokers using a distributed controller quorum that replicates metadata via the Raft consensus protocol. This removes the separate ZooKeeper dependency, eliminates the single controller bottleneck, reduces communication overhead, simplifies configuration, and drastically minimizes downtime during leader re-elections.

#### 2. How is metadata managed in KRaft, and how does it improve scalability compared to ZooKeeper?
**Answer:**
KRaft uses an event-sourced storage model where state changes are recorded in a metadata topic, trimmed periodically via snapshots to prevent indefinite growth. By limiting metadata access to the controller quorum and eliminating the independent ZooKeeper cluster, KRaft reduces communication overhead and scales more efficiently to handle larger broker and topic counts.


## 📂 Category: Kafka Architecture (11 cards)

### 🟢 Junior Level

#### 1. What are standard enterprise use cases for Apache Kafka?
**Answer:**
Kafka is widely used for real-time stream processing, user activity tracking (page views, clicks), log aggregation across microservices, metrics collection, event sourcing patterns, and act as a reliable commit log for database change data capture (CDC).

#### 2. What are the primary architectural benefits of partitions in Kafka topics?
**Answer:**
Partitions provide:
- Horizontal Scalability: Distributing topic data across multiple broker nodes.
- Parallelism: Enabling multiple consumers within a consumer group to process data concurrently.
- Fault Tolerance: Facilitating leader-follower replication across brokers.

#### 3. What is Apache Kafka and what are its core APIs?
**Answer:**
Kafka is a fast, scalable, fault-tolerant messaging and event streaming platform that combines messaging, storage, and stream processing for real-time and historical data pipelines. It has four core APIs: Producer API, Consumer API, Streams API, and Connector API.

#### 4. What role do partitions play in the architecture of Kafka brokers?
**Answer:**
Partitions break topics into smaller, manageable segments. They: • Store messages in an immutable sequence. • Enable parallel processing and scalability by allowing data to be distributed across multiple brokers and processed concurrently by consumers.

#### 5. What role does replication play in Kafka topics?
**Answer:**
Replication in Kafka topics ensures high durability and fault tolerance. Each partition is replicated across multiple brokers, with one replica designated as the leader and the others as followers. In case of broker failure, one of the follower replicas can quickly take over, ensuring continuous availability of data.

#### 6. What roles do producers and consumers play in Apache Kafka’s architecture?
**Answer:**
In Kafka, producers are client applications that publish messages (or events) to topics, while consumers subscribe to topics to read those messages. This separation enables scalable, decoupled, and real-time data processing.

#### 7. What structural components comprise a Kafka message?
**Answer:**
A Kafka message contains:
- Value (Payload): Serialized byte array containing the core data.
- Key: Optional identifier used for deterministic hash partitioning.
- Timestamp: Event-time or log-append time.
- Headers: Optional key-value metadata pairs.
- Compression type & offset/partition metadata assigned by the broker upon write.


### 🟡 Mid Level

#### 1. What alternative to ZooKeeper has been introduced in Kafka's evolution, and what are its advantages?
**Answer:**
Kafka introduced KRaft (Kafka Raft Metadata Mode), a built-in consensus protocol that replaces ZooKeeper. KRaft consolidates metadata configuration and controller leadership management directly into the Kafka cluster, reducing operational overhead, eliminating external metadata sync bottlenecks, and allowing much faster cluster startup times.


### 🔴 Senior Level

#### 1. What are hot standby clusters in Kafka architectures, and why are they important?
**Answer:**
Hot standby clusters are secondary Kafka clusters that continuously synchronize data (using tools like MirrorMaker 2 or Confluent Cluster Linking) from a primary cluster. They are immediately available for failover scenarios, drastically reducing Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO) during disaster recovery.

#### 2. What are the primary limitations and operational challenges of using ZooKeeper with Kafka?
**Answer:**
Key limitations include:
- Single Point of Failure/Quorum Risk: ZooKeeper metadata outages disable Kafka control-plane operations.
- Operational Overhead: Maintaining an entirely separate quorum cluster alongside Kafka.
- Upgrade/Security Complexity: Synchronizing ACLs, JAAS configs, and rolling upgrades across two disparate distributed systems.

#### 3. What is metadata management in Kafka topics and how is it handled?
**Answer:**
Kafka metadata contains critical information about topics, brokers, partitions, and consumer groups to enable efficient routing and replication. It can be managed externally via Apache ZooKeeper or internally using KRaft (Kafka Raft) mode via a dedicated metadata topic.


## 📂 Category: Kafka Configuration (1 cards)

### 🟡 Mid Level

#### 1. Which broker-side configurations interact with the producer’s durability settings?
**Answer:**
Two key broker-side settings are:
• replication.factor: Determines how many copies of a topic are maintained across brokers.
• min.insync.replicas: Sets the minimum number of replicas that must acknowledge a write when using acks=all.
These settings help balance durability and availability.


## 📂 Category: Kafka Consumers (8 cards)

### 🟢 Junior Level

#### 1. What are the key benefits of using Kafka consumer groups?
**Answer:**
Consumer groups enable decoupled parallel processing by distributing topic partitions among members, provide linear scalability for high-throughput ingestion, and ensure automatic fault tolerance and partition redistribution if a consumer instance crashes.

#### 2. What are the primary root causes of consumer lag in Kafka?
**Answer:**
Consumer lag commonly stems from:
- Sudden message spikes outpacing processing capacity.
- Data skew causing uneven partition distribution.
- Inefficient message processing logic, DB bottlenecks, or slow downstream external API calls.
- Consumer rebalances or frequent thread stalls.

#### 3. Why are Kafka offsets necessary in a distributed streaming system?
**Answer:**
Offsets enable Kafka to:

- Track message progress from production to consumption
- Maintain message ordering within partitions
- Support fault tolerance by allowing consumers to restart from the last committed offset
- Facilitate parallel processing and horizontal scalability


### 🟡 Mid Level

#### 1. How are messages distributed among consumers within a Kafka consumer group?
**Answer:**
Messages are distributed based on partitions. Each partition is assigned exclusively to one consumer within a consumer group at any given time to maintain message ordering. If partitions outnumber consumers, some handle multiple partitions; if consumers outnumber partitions, excess consumers remain idle.

#### 2. How do Kafka consumer groups enhance scalability in message processing systems?
**Answer:**
Consumer groups enable horizontal scaling by allowing multiple consumers to share the workload of reading from topic partitions. As message volume increases, additional consumers can be added to the group to process messages concurrently and maintain overall system throughput.

#### 3. How do Kafka offsets support consumer failure recovery and horizontal scalability?
**Answer:**
Offsets are sequential identifiers assigned to messages within a partition. Each consumer tracks its own offset manually or via offset commits. If a consumer fails, it restarts processing from its last committed offset, ensuring no reprocessing of handled messages (barring duplicate processing scenarios). This independent tracking allows the system to scale horizontally while maintaining order within partitions.

#### 4. What is the effect of having more consumers than partitions in a Kafka consumer group?
**Answer:**
If there are more consumers than partitions, some consumers remain idle since each partition can only be consumed by one consumer at a time within a single group. These idle consumers serve as hot standbys to take over if an active consumer fails.


### 🔴 Senior Level

#### 1. Under what circumstances would you implement a custom partition assignor for Kafka consumers?
**Answer:**
Use a custom assignor when default assignment strategies (Range, RoundRobin, CooperativeSticky) do not adequately balance workloads based on consumer capacity, geographical data locality, processing history, or specialized resource constraints. Extending `AbstractPartitionAssignor` allows implementing tailored assignment algorithms.


## 📂 Category: Kafka Coordination (1 cards)

### 🟡 Mid Level

#### 1. What role does ZooKeeper play in a Kafka cluster?
**Answer:**
In Kafka, ZooKeeper coordinates broker interactions by tracking broker availability, managing leader elections, storing configuration data (e.g., topic creation/deletion), handling access control lists (ACLs), and ensuring consistent cluster membership and synchronization.


## 📂 Category: Kafka Core Concepts (2 cards)

### 🟢 Junior Level

#### 1. How are Kafka topics structured, and how do they relate to partitions?
**Answer:**
Kafka topics are logical groupings of messages, while partitions are the physical divisions of a topic. Each partition is an ordered, immutable sequence of messages. This structure organizes data and enables horizontal scalability and parallelism by allowing multiple consumers to read from different partitions simultaneously.

#### 2. How do Kafka producers and consumers interact with a Kafka cluster?
**Answer:**
Producers send messages to designated topics on Kafka brokers using a partition mapper (often based on message keys). Consumers subscribe to topics and pull messages from assigned partitions. The Kafka cluster manages partitioning and replication, ensuring efficient data flow, reliable storage, and high availability.


## 📂 Category: Kafka Producers (4 cards)

### 🟢 Junior Level

#### 1. What is the primary function of a Kafka producer?
**Answer:**
A Kafka producer is responsible for creating messages, serializing keys and values into byte arrays, and sending them to Kafka topics using the Producer API, while handling delivery semantics, batching, error handling, and performance tuning configurations.

#### 2. Why is message serialization important in Kafka producers and how is it typically implemented?
**Answer:**
Kafka treats messages as simple byte arrays. Serialization converts structured data (like JSON) into byte arrays before sending.


### 🔴 Senior Level

#### 1. How do Kafka producers handle delivery semantics, retries, and timeouts?
**Answer:**
Producers use delivery semantics ranging from fire-and-forget, wait-for-leader acknowledgment, to wait-for-all in-sync replicas (acks=all). Key configurations affecting producer reliability include:
• retries: Specifies how many times the producer attempts to resend a failed message.
• retry.backoff.ms: Sets the delay between successive retry attempts.
• delivery.timeout.ms: Defines the maximum wall-clock time the producer waits for an acknowledgment before considering delivery failed.

#### 2. When and why would you implement a custom partitioner on the producer side?
**Answer:**
A custom partitioner is implemented when built-in strategies do not meet specific application needs. By overriding the default partitioning logic (via the Kafka Producer API), you can tailor the key-to-partition mapping to handle special cases—such as dedicating a partition for high-volume sources—to avoid hotspots.


## 📂 Category: Kafka Replication (3 cards)

### 🟡 Mid Level

#### 1. How do partitions contribute to fault tolerance in Kafka?
**Answer:**
Partitions provide fault tolerance by being replicated across multiple brokers in a Kafka cluster. If a broker hosting a leader partition fails, an in-sync replica (ISR) is promoted to leader, ensuring redundancy, fault tolerance, and high availability.


### 🔴 Senior Level

#### 1. How do offsets help manage partition replication and data consistency in Kafka?
**Answer:**
When messages are written to a leader partition, they take time to replicate across followers. By using the high watermark offset, consumers ensure they only read and process messages that have been fully replicated to all in-sync replicas (ISRs), thereby maintaining strong data consistency.

#### 2. What is the active-passive Kafka cluster configuration?
**Answer:**
In an active-passive setup, data is replicated unidirectionally from an active cluster to a passive backup cluster. The passive cluster can take over operations during a failure, though replication lag may temporarily lead to data inconsistencies.


## 📂 Category: Kafka Schema Registry (1 cards)

### 🟡 Mid Level

#### 1. What is schema management in Kafka?
**Answer:**
Schema management uses a schema registry to define and enforce the structure of messages flowing through Kafka topics, ensuring producers and consumers agree on data formats as they evolve over time.


## 📂 Category: Kafka Storage (2 cards)

### 🟡 Mid Level

#### 1. What is the log-end offset in Kafka?
**Answer:**
The log-end offset is the offset of the very last message currently present in a partition’s log, indicating the maximum available data point for replication and consumption.


### 🔴 Senior Level

#### 1. What is the high watermark offset in Kafka?
**Answer:**
The high watermark offset is the point in the partition log up to which all messages have been fully replicated to all in-sync replicas (ISRs). Consumers are only allowed to read messages up to this offset to ensure data durability.


## 📂 Category: Memory Management (2 cards)

### 🟡 Mid Level

#### 1. Redis 有哪些内存溢出控制/内存淘汰策略？
**Answer:**
1. noeviction：默认策略，不删除任何数据，拒绝所有写操作并返回错误信息，此时 Redis 只响应读操作。2. volatile-lru：根据 LRU 算法删除设置了超时属性（expire）的键，直到腾出足够空间为止。3. allkeys-lru：根据 LRU 算法删除键，不管有没有设置超时属性，直到腾出足够空间为止。4. allkeys-random：随机删除所有键，直到腾出足够空间为止。5. volatile-random：随机删除过期键，直到腾出足够空间为止。6. volatile-ttl：根据键值对象的 ttl 属性，删除最近将要过期数据。

#### 2. Redis 的过期数据回收策略有哪些？
**Answer:**
1. 惰性删除：指的是当我们查询 key 的时候才对 key 进行检测，如果已经达到过期时间，则删除。缺点：如果这些过期的 key 没有被访问，那么它们就无法被删除，从而一直占用内存。
2. 定期删除：指的是 Redis 每隔一段时间对数据库做一次检查，删除部分的过期 key。由于不可能对所有 key 去做轮询来删除，所以 Redis 会每次随机取一些 key 去做检查和删除。


## 📂 Category: Message Queues & Caching (1 cards)

### 🟡 Mid Level

#### 1. 如何使用Redis实现异步队列？
**Answer:**
主要有以下几种方式：
1. 使用 List 作为队列：lpush 生产消息，rpop 消费消息。消费者死循环 rpop 会导致 CPU 消耗过高，可以通过休眠缓解但会带来延迟问题。
2. 使用 List 作为队列：lpush 生产消息，brpop 消费消息。brpop 是 rpop 的阻塞版本，队列为空时会一直阻塞直到有值或超时，只能实现一对一队列。
3. 使用 Redis 的 Pub/Sub（发布/订阅）：支持 1:N 的消息发布订阅，但不是可靠的，不保证订阅者一定能收到消息，也不进行消息存储。
通常复杂的异步队列需求仍建议交给专业的消息队列系统（如 Kafka）。


## 📂 Category: Messaging (1 cards)

### 🟡 Mid Level

#### 1. Describe the interplay between producers, brokers, and consumers regarding offset management.
**Answer:**
Producers assign sequential offsets when sending messages to a partition. Brokers store these messages in an ordered log, and consumers read messages by tracking offsets. Consumers then commit offsets to mark their progress, enabling recovery and consistent processing.


## 📂 Category: Network & IO (1 cards)

### 🟡 Mid Level

#### 1. 如何通俗地理解I/O多路复用？
**Answer:**
I/O多路复用类似于老师在讲台上等学生举手回答问题。相比于轮询检查每个人（非并发）或为每个人派一个分身（多线程），多路复用让单个线程等待多个Socket事件。当某个Socket准备就绪（举手）时，系统通知线程去处理该Socket对应的数据，从而实现单线程高效处理大量并发连接。


## 📂 Category: Partitions & Scalability (2 cards)

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


## 📂 Category: Performance (1 cards)

### 🟡 Mid Level

#### 1. What problems can occur with underpartitioning in a Kafka deployment?
**Answer:**
Underpartitioning may cause individual partitions to become overloaded with messages, leading to processing delays, backlogs, and resource bottlenecks such as CPU or disk I/O constraints on the hosting broker.


## 📂 Category: Performance & Operations (1 cards)

### 🔴 Senior Level

#### 1. Redis 常见性能问题和解决方案有哪些？
**Answer:**
1. Master 最好不要做任何持久化工作（如内存快照和 AOF 日志），特别不要启用内存快照做持久化。2. 如果数据比较关键，某个 Slave 开启 AOF 备份数据，策略为每秒同步一次。3. Slave 和 Master 最好在同一个局域网内以保证主从复制速度和连接稳定性。4. 尽量避免在压力较大的主库上增加从库。5. Master 调用 BGREWRITEAOF 重写 AOF 文件会占用大量 CPU 和内存资源导致服务 load 过高，出现短暂服务暂停现象。6. 主从复制推荐使用单向链表结构（Master -> Slave1 -> Slave2），方便处理单点故障和主备切换。


## 📂 Category: Performance Optimization (2 cards)

### 🔴 Senior Level

#### 1. 大key问题了解吗？包括危害、发现方式及处理方法
**Answer:**
Redis使用过程中可能会出现大key的情况，例如：单个简单的key存储的value很大（size超过10KB），或者hash、set、zset、list中存储过多的元素（以万为单位）。
大key造成的危害：
1. 客户端耗时增加，甚至超时。
2. 对大key进行IO操作时，严重占用带宽和CPU。
3. 造成Redis集群中数据倾斜。
4. 主动删除、被动删除等可能会导致阻塞。
如何找到大key：
1. bigkeys命令：遍历分析Redis实例中的所有Key，返回整体统计信息与每个数据类型中Top1的大Key。
2. redis-rdb-tools：Python编写的用来分析Redis的rdb快照文件的工具，可生成json文件或报告进行分析。
如何处理大key：
1. 删除大key：Redis 4.0及以上可使用UNLINK命令以非阻塞方式逐步安全清理；小于4.0时建议通过SCAN命令增量迭代扫描key后判断删除。
2. 压缩和拆分key：当value是string时，可通过序列化、压缩算法控制大小，或拆分为不同的部分使用mget等操作实现事务读取；当value是集合类型时，根据预估数据规模进行分片处理。

#### 2. 怎么处理热key？
**Answer:**
对热key的处理，最关键的是对热点key的监控，可以从这些端来监控热点key：
1. 客户端：在客户端设置全局字典（key和调用次数），每次调用Redis命令时，使用这个字典进行记录。
2. 代理端：像Twemproxy、Codis这些基于代理的Redis分布式架构，所有客户端的请求都是通过代理端完成的，可以在代理端进行收集统计。
3. Redis服务端：使用monitor命令统计热点key。
只要监控到了热key，处理方式如下：
1. 把热key打散到不同的服务器，降低压力的集中。
2. 加二级缓存，提前加载热key数据到内存中，如果redis宕机，降级到本地内存查询。


## 📂 Category: Performance Tuning (2 cards)

### 🟡 Mid Level

#### 1. Redis 为什么性能这么快？
**Answer:**
1. 完全基于内存操作。
2. 使用单线程模型，避免了线程切换和竞态产生的消耗。
3. 基于非阻塞的I/O多路复用机制（epoll等）。
4. C语言实现，优化过的数据结构，针对底层数据结构做了大量的极致优化。


### 🔴 Senior Level

#### 1. Redis 发生阻塞的原因有哪些？如何排查和解决？
**Answer:**
主要原因包括：1. API或数据结构使用不当（如在大对象上执行复杂度 O(N) 的命令）。排查：通过 slowlog get {n} 获取慢查询，优化低效命令（如 hgetall 改 hmget，禁用 keys 等）或拆分大对象。2. CPU饱和：单线程OPS到达极限，可通过 redis-cli --stat 获取使用情况，若并发极高需做集群水平扩展，若并发不高需排查持久化阻塞。3. 持久化阻塞：包括 fork 阻塞（RDB/AOF重写时主线程调用 fork 耗时过长）、AOF刷盘阻塞（fsync等待过久导致主线程阻塞）、HugePage写操作阻塞（开启Transparent HugePages时复制内存页从4K变为2MB放大512倍导致慢查询）。


## 📂 Category: Persistence (3 cards)

### 🟢 Junior Level

#### 1. Redis 的数据恢复流程是怎样的？
**Answer:**
当 Redis 发生了故障，可以从 RDB 或者 AOF 中恢复数据。恢复过程只需把 RDB 或者 AOF 文件复制到 Redis 的数据目录下，配置好对应的持久化开关，然后启动 redis-server 即可。启动时加载数据的流程：1. AOF 持久化开启且存在 AOF 文件时，优先加载 AOF 文件。2. AOF 关闭或者 AOF 文件不存在时，加载 RDB 文件。3. 加载 AOF/RDB 文件成功后，Redis 启动成功。4. AOF/RDB 文件存在错误时，Redis 启动失败并打印错误信息。


### 🟡 Mid Level

#### 1. Redis 4.0 的混合持久化了解吗？
**Answer:**
重启 Redis 时，如果只用 RDB 会丢失大量数据，而重放纯 AOF 日志速度较慢。Redis 4.0 引入了混合持久化选项，将 RDB 文件的内容和增量的 AOF 日志文件存在一起。这里的 AOF 日志不再是全量的日志，而是自持久化开始这段时间发生的增量 AOF 日志，通常这部分很小。重启时可以先加载 RDB 内容，然后重放增量 AOF 日志，从而大幅提升启动效率。

#### 2. Redis 持久化方式有哪些？有什么区别？
**Answer:**
Redis 主要有两种持久化方式：1. RDB（Redis DataBase）：把当前进程数据生成快照保存到磁盘的压缩二进制文件。支持手动触发（SAVE 阻塞当前服务器，BGSAVE fork 子进程异步执行）和自动触发（满足 save m n 配置、全盘复制、debug reload 或无 AOF 时的 shutdown）。2. AOF（Append Only File）：以独立日志方式记录每次写命令，重启时重新执行 AOF 文件恢复数据。工作流程包括命令写入 (append)、文件同步 (sync)、文件重写 (rewrite)、重启加载 (load)。目前 AOF 是解决数据持久化实时性的主流方式。


## 📂 Category: Producers (8 cards)

### 🟢 Junior Level

#### 1. Describe the round-robin partitioning strategy for Kafka producers and when it is useful.
**Answer:**
The round-robin strategy cycles through available partitions, assigning each successive message to the next partition sequentially. This is useful when messages do not have keys, as it evenly distributes the load across partitions and prevents hot spots.

#### 2. What is the purpose of producer partitioning strategies in Kafka?
**Answer:**
Producer partitioning strategies decide how messages are distributed across the partitions of a topic, affecting message ordering, load distribution, and overall system performance.

#### 3. What is the significance of message keys and values in Kafka?
**Answer:**
In Kafka, the key (often a string or integer) is used to determine which partition a message goes to, ensuring messages with the same key maintain order. The value contains the actual event data, which can be simple or complex, and is serialized before being sent to the broker.


### 🟡 Mid Level

#### 1. What do the different acks settings mean in Kafka producers?
**Answer:**
acks=0: The producer does not wait for any acknowledgment from the broker (fire-and-forget). acks=1: The producer waits for acknowledgment from the partition leader only. acks=all (or -1): The producer waits for acknowledgments from all in-sync replicas, which maximizes durability at the expense of some latency.

#### 2. What is a potential issue when adding new partitions to a topic that uses the default partitioning strategy?
**Answer:**
Adding partitions can change the mapping of keys to partitions (since partition calculation typically uses hash(key) % num_partitions). New messages with the same key might be sent to a different partition than earlier messages, potentially disrupting strict per-key message ordering.

#### 3. What is the significance of batch size and linger time in Kafka producer performance?
**Answer:**
Increasing the batch size allows more messages to be sent together, improving throughput, but it may require more memory and increase latency. The linger time controls how long messages are held to form a batch—longer linger times can lead to larger, more efficient batches but at the cost of increased delay in message delivery.

#### 4. What partitioning strategies are used when no message key is provided?
**Answer:**
If no key is provided, Kafka may use a round-robin strategy, cycling through partitions evenly, or a sticky partitioning approach that batches messages to one partition until a threshold (time or batch size) is reached, then switches to another.


### 🔴 Senior Level

#### 1. What problem does the uniform sticky partitioner solve, and how does it function?
**Answer:**
The uniform sticky partitioner addresses the issue of small batch sizes when using round-robin distribution. It temporarily assigns records without explicit partition information to the same partition until a batch is full or a time limit is reached, allowing for larger batches and lower latency while eventually distributing records evenly.


## 📂 Category: Producers & Partitioning (3 cards)

### 🟢 Junior Level

#### 1. How does a Kafka broker decide which partition to store an incoming message?
**Answer:**
When a producer sends a message, the broker or producer client uses either: • A deterministic partitioning strategy based on a producer-specified key (where a hash function consistently maps the key to a specific partition), or • A round-robin or sticky algorithm if no key is provided (key is null), distributing messages across available partitions.

#### 2. How does choosing the wrong partitioning key affect message distribution in Kafka?
**Answer:**
An inappropriate key can lead to uneven distribution, with messages concentrating in a few partitions (hot partitions) while others remain underutilized. This imbalance can degrade performance, increase latency, and overload specific consumers.


### 🟡 Mid Level

#### 1. How does a Kafka producer discover and connect to the Kafka cluster?
**Answer:**
A producer initially connects to a Kafka bootstrap server—a subset of Kafka brokers—to discover the full cluster topology. It sends a MetaDataRequest, which returns details such as broker addresses and current leaders for each topic partition. Once discovered, the producer sends messages directly to the leader broker for the target partition.


## 📂 Category: Redis Architecture (5 cards)

### 🟢 Junior Level

#### 1. Redis 可以用来干什么？
**Answer:**
Redis 的常见应用场景包括：
1. 缓存：减少数据库访问次数，极大提高系统响应速度。
2. 会话存储：提供快速的会话读写，提高用户体验。
3. 消息队列：通过异步处理增加系统的可扩展性和解耦性（适用于轻量级场景）。
4. 实时分析：在内存中快速处理复杂数据分析。
5. 排行榜和计数器：利用有序集合（ZSet）等数据结构快速更新和检索社交或游戏排行。
6. 发布和订阅：构建实时消息通知或实时分析系统。


### 🟡 Mid Level

#### 1. RDB 和 AOF 各自有什么优缺点？
**Answer:**
RDB 优缺点：
- 优点：生成紧凑的二进制文件 dump.rdb，非常适合备份、全量复制和容灾恢复；恢复速度远快于 AOF。
- 缺点：实时性差，无法做到秒级持久化，间隔期发生故障会导致数据丢失；存在老版本 Redis 无法兼容新版本 RDB 的问题。
AOF 优缺点：
- 优点：实时性好，可通过配置 appendfsync（如 always）每次操作都记录；通过 append 模式写文件，崩溃后可通过 redis-check-aof 修复。
- 缺点：AOF 文件体积比 RDB 大，恢复速度慢；数据集大时启动效率低于 RDB。

#### 2. Redis 报内存不足怎么处理？
**Answer:**
处理 Redis 内存不足的主要方式有：
1. 修改配置文件 redis.conf 的 maxmemory 参数，或者通过命令 `set maxmemory` 动态设置内存上限，增加 Redis 可用内存。
2. 修改内存淘汰策略（eviction policy），及时释放内存空间。
3. 使用 Redis 集群模式（Cluster），进行水平横向扩容。

#### 3. Redis 的管道（Pipelining）了解吗？
**Answer:**
Redis 提供三种将客户端多条命令打包发送给服务端执行的方式：Pipelining、Transactions 和 Lua Scripts。
Pipelining 是一种最简单的批量发送方式，客户端将多条命令一次性发送给服务端，其核心目的是降低 RTT（Round Trip Time）对性能的影响。
优势：
1. 节省了 RTT：减少客户端与服务端之间的网络调用次数。
2. 减少了上下文切换：减少了程序从用户态切换到内核态的系统调用开销。


### 🔴 Senior Level

#### 1. Redis 为什么早期选择单线程？Redis 4.0 之后的多线程体现在哪里？
**Answer:**
Redis 早期选择单线程主要是因为其内存操作非常快，瓶颈往往是网络 IO 而非 CPU，单线程避免了不必要的线程上下文切换和复杂的锁竞争。
Redis 4.0 之后引入了多线程（主要是后台线程），除了主线程外，后台线程用于处理一些较为缓慢的操作，例如清理脏数据、无用连接的释放、大 Key 的异步删除（UNLINK）等。


## 📂 Category: Redis Basics (1 cards)

### 🟢 Junior Level

#### 1. 什么是Redis？它有哪些特点？
**Answer:**
Redis是一种基于键值对（Key-Value）的NoSQL内存数据库。其Value支持String、Hash、List、Set、Zset、Bitmaps、HyperLogLog、GEO等多种数据结构，能够满足复杂业务场景。由于数据全量存储在内存中，读写性能极高，同时支持RDB快照和AOF日志持久化机制，保证断电或重启时数据不丢失。


## 📂 Category: Redis Cluster (2 cards)

### 🟡 Mid Level

#### 1. Redis集群的伸缩（扩容与收缩）原理是什么？
**Answer:**
Redis集群通过灵活的节点增减实现平滑伸缩，且不影响集群对外提供服务。伸缩的核心在于“槽（Slot）和节点的对应关系”：扩容或收缩本质上是将一部分槽和对应的数据从源节点迁移到目标节点（新节点）。


### 🔴 Senior Level

#### 1. Redis集群的核心原理是什么？集群部署至少需要几个物理节点？
**Answer:**
Redis集群通过数据分区（16384个Slot槽）和自动故障转移实现分布式存储与高可用。节点间通过Gossip协议（Ping/Pong消息）进行通信和故障发现。当半数以上持有槽的主节点标记某节点为主观下线（pfail）后，触发客观下线并进行主从Failover。为避免单点故障和脑裂导致无法满足N/2+1的投票要求，集群主节点至少需要部署在3台不同的物理机上。


## 📂 Category: Redis Internals (1 cards)

### 🔴 Senior Level

#### 1. Redis底层有哪些核心数据结构？
**Answer:**
Redis底层包括：1. SDS（简单动态字符串）：记录长度信息，降低获取长度复杂度至O(1)，避免缓冲区溢出；2. linkedlist：双端环形链表；3. dict（字典/哈希表）：使用链地址法解决冲突，采用渐进式rehash；4. skiplist（跳跃表）：有序集合的底层实现之一，层高1-32随机数；5. intset（整数集合）：保存整数值的数组；6. ziplist（压缩列表）：为节约内存开发的顺序性数据结构。


## 📂 Category: Redis Replication (1 cards)

### 🔴 Senior Level

#### 1. Redis主从数据同步的方式有哪些？
**Answer:**
Redis使用psync命令完成主从同步，分为全量复制和部分复制：1. 全量复制：用于初次复制，主节点执行bgsave生成RDB文件发送给从节点，从节点清空旧数据并加载RDB，期间积压的写命令缓存在复制缓冲区中后续补发。2. 部分复制：用于网络闪断等异常恢复，从节点发送psync带上runId和offset，主节点若在复制积压缓冲区（默认1MB）中查到对应数据，则发送+CONTINUE进行增量命令补发。


## 📂 Category: Reliability & Delivery Guarantees (2 cards)

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


## 📂 Category: Replication (3 cards)

### 🟢 Junior Level

#### 1. Redis 主从有哪些常见的拓扑结构？
**Answer:**
Redis 的复制拓扑结构支持单层或多层复制关系，主要分为三种：1. 一主一从结构：最简单的拓扑结构，用于主节点宕机时从节点提供故障转移支持。2. 一主多从结构（星形拓扑）：应用端可以利用多个从节点实现读写分离，分担主节点读压力。3. 树状主从结构：从节点不仅可以复制主节点数据，同时可以作为其他从节点的主节点继续向下层复制，通过引入复制中间层，有效降低主节点负载和需要传给从节点的数据量。

#### 2. What is the significance of leader and follower roles in broker replication?
**Answer:**
In replication: • The leader broker handles all read and write operations for its partition. • Follower brokers continuously sync with the leader, ensuring that if the leader fails, a follower can seamlessly take over without data loss.


### 🟡 Mid Level

#### 1. Redis 的主从复制原理是怎样的？
**Answer:**
1. 保存主节点（master）信息：从节点保存主节点的 IP 和 port。
2. 主从建立连接：从节点发现主节点后，尝试建立网络连接。
3. 发送 ping 命令：连接成功后从节点发送 ping 请求检测网络及主节点状态。
4. 权限验证：若主节点要求密码，从节点必须提供正确密码通过验证。
5. 同步数据集：主节点把持有的数据全部发送给从节点（全量同步）。
6. 命令持续复制：主节点持续把写命令发送给从节点，保证主从数据一致性。


## 📂 Category: Replication & Fault Tolerance (1 cards)

### 🟡 Mid Level

#### 1. How does Kafka achieve fault tolerance through topic replication?
**Answer:**
By replicating each partition across several brokers according to the replication factor, Kafka minimizes the risk of data loss. The leader handles all writes while followers stay in sync (ISR - In-Sync Replicas). If the leader fails, one of the in-sync replicas is promoted to leader, ensuring data remains available and consistent.


## 📂 Category: Replication & High Availability (1 cards)

### 🔴 Senior Level

#### 1. What does cross‐region replication mean in Kafka clusters?
**Answer:**
Cross‐region replication involves duplicating Kafka clusters across different geographical regions. This ensures that if one region experiences an outage, another region can take over, thereby maintaining data availability and business continuity.


## 📂 Category: Scripting & Transactions (1 cards)

### 🟡 Mid Level

#### 1. Redis 和 Lua 脚本结合使用的优势是什么？
**Answer:**
1. 原子性：Lua脚本在Redis中是原子执行的，执行过程中不会插入其他命令。
2. 可复用：可以将自定义命令常驻在Redis内存中，实现复用。
3. 减少网络开销：可以将多条命令一次性打包，有效减少网络开销。


## 📂 Category: Security (3 cards)

### 🟡 Mid Level

#### 1. What is Kerberos?
**Answer:**
Kerberos provides centralized authentication for users and servers. It runs as a third-party trusted server known as the Key Distribution Center (KDC), where each user and network service is registered as a principal.


### 🔴 Senior Level

#### 1. How does the Ticket Granting Service (TGS) Exchange function in Kerberos?
**Answer:**
The TGS exchange is used to obtain session tickets for accessing specific servers without exposing the client's secret key. The TGS validates the client's TGT, does not require the client's secret key for encryption, but encrypts the resulting service ticket using the destination server's secret key. The client sends a `KRB_TGS_REQ` and receives a `KRB_TGS_REP`.

#### 2. What are the three major authentication exchanges in Kerberos?
**Answer:**
1. Authentication Service (AS) Exchange: Client obtains a Ticket Granting Ticket (TGT) from the KDC.
2. Ticket Granting Service (TGS) Exchange: Client uses the TGT to request service tickets for specific application servers.
3. Client Server (CS) Exchange: Client presents the service ticket to the target service/broker for authorized access.


## 📂 Category: Security & Authentication (3 cards)

### 🟡 Mid Level

#### 1. 3 Components of Kerberos
**Answer:**
The core components are:
1. Client
2. Authentication Server or Key Distribution Server (KDC)
3. Server


### 🔴 Senior Level

#### 1. Authentication Service (AS) Exchange
**Answer:**
The exchange between client and Authentication Server (KDC):
1. The client sends KRB_AS_REQ message to KDC specifying desired credentials.
2. Server replies with KRB_AS_REP containing the ticket and session key.
3. The session key is encrypted with the client's secret key.
4. The TGT is encrypted with the server's secret key (DES encryption by default).

#### 2. Client Server (CS) Exchange
**Answer:**
The authentication exchange when a client contacts the real server:
The server validates the client by decrypting the ticket with the server's secret key and decrypting the authenticator with the session key contained within the ticket.


## 📂 Category: Security & Coordination (1 cards)

### 🟡 Mid Level

#### 1. How does ZooKeeper manage access control and configuration in Kafka?
**Answer:**
ZooKeeper stores Access Control Lists (ACLs) to define permissions for Kafka topics, controlling read and write access. Additionally, it acts as a centralized repository for configuration settings, propagating changes like topic creation, deletion, and updates across all brokers to ensure cluster consistency.


## 📂 Category: Storage (4 cards)

### 🟢 Junior Level

#### 1. What is a Kafka offset?
**Answer:**
A Kafka offset is a unique, continuously increasing 64-bit integer assigned to each message within a partition. It represents the logical position of the message in the partition’s append-only log.

#### 2. What is the role of a DataNode in HDFS architecture?
**Answer:**
The DataNode (also known as a slave node) stores actual data blocks in HDFS and performs read and write operations directly as requested by clients. DataNodes are typically deployed on commodity hardware.


### 🟡 Mid Level

#### 1. What is an active segment in a Kafka partition?
**Answer:**
Within each partition, data is stored on disk in segment files. The active segment is the specific file that is currently receiving new incoming messages. Once it reaches a configured size threshold (log.segment.bytes) or age (log.segment.ms), Kafka closes it and begins writing to a new active segment.

#### 2. What is the difference between FsImage and EditLogs in HDFS NameNode architecture?
**Answer:**
• FsImage: Contains the complete filesystem namespace, including a serialized form of all directories and file inodes, stored as a file on the NameNode's local disk.
• EditLogs: Contains a sequential log of all recent modifications and transactional requests (create, update, delete) made to the filesystem since the last FsImage checkpoint.


## 📂 Category: Storage & Core Concepts (1 cards)

### 🟢 Junior Level

#### 1. How does Kafka guarantee message ordering within a partition and use offsets?
**Answer:**
Each partition in Kafka is an append-only log where messages are written in a strict sequence and marked by an integer position called an offset. This ordering mechanism ensures that consumers process messages in the exact order they were written, though messages across different partitions may be interleaved.


## 📂 Category: Storage & Offsets (2 cards)

### 🟢 Junior Level

#### 1. What are topic partition offsets and why are they important?
**Answer:**
Offsets are numeric markers that indicate the position of a message within a partition. They are used by Kafka to track which messages have been consumed. This mechanism ensures that consumers can resume reading from the correct position, maintain order, and provide at-least-once or exactly-once processing guarantees.

#### 2. What does the term “committed offset” refer to?
**Answer:**
The committed offset is the offset of the last message that a consumer has successfully processed and acknowledged. It serves as a checkpoint for consumer progress.


## 📂 Category: Storage & Performance (1 cards)

### 🟡 Mid Level

#### 1. How does Kafka compression work at the topic and producer level?
**Answer:**
Kafka supports compression to optimize disk space and network usage. Compression can be applied at the producer level and passed through or re-compressed at the topic level using algorithms like gzip, snappy, lz4, or zstd. Consistent use of a compression algorithm between producers and topics prevents the CPU overhead of broker-side recompression.


## 📂 Category: Transactions (1 cards)

### 🟡 Mid Level

#### 1. Redis 支持事务吗？原理与注意事项是什么？
**Answer:**
Redis 提供了简单的事务支持（不完全满足 ACID）。通过 MULTI 命令开始事务，EXEC 命令结束事务，中间的命令会按顺序放入服务器的事务队列中，收到 EXEC 后原子性地一次性执行整个队列。注意点：1. Redis 事务不支持回滚（语法错误会拒绝，运行时错误会继续执行），以保持简单快速。2. 事务执行期间不会被其他客户端打断。


## 📂 Category: ZooKeeper (5 cards)

### 🟢 Junior Level

#### 1. What is a ZooKeeper ensemble?
**Answer:**
An ensemble is a group of ZooKeeper server nodes (typically at least three) that work together to maintain replicated data and provide fault tolerance, ensuring the service remains operational even if one or more nodes fail.

#### 2. What is the significance of ZooKeeper’s file system–like data model?
**Answer:**
The file system–like model, with hierarchical znodes, provides an intuitive structure for storing configuration data, state information, and coordination metadata. This structure makes it easier to manage and retrieve data in a distributed system.


### 🟡 Mid Level

#### 1. How do watches function in ZooKeeper?
**Answer:**
Watches are one-time notification triggers that clients can set on ZooKeeper znodes. When the data of a znode or its children changes, the watch triggers a notification event to inform the client of the update, after which the watch must be reset.

#### 2. What does membership management entail in ZooKeeper?
**Answer:**
Membership management involves tracking which nodes (e.g., Kafka brokers) are connected to the ZooKeeper ensemble. ZooKeeper updates its records as nodes join or leave, thereby maintaining an accurate view of the cluster’s state.

#### 3. What is lock management in ZooKeeper and why is it critical?
**Answer:**
Lock management in ZooKeeper prevents simultaneous modifications of shared resources. By enforcing mutual exclusion through distributed locks, ZooKeeper helps avoid data corruption or loss in concurrent distributed environments.

