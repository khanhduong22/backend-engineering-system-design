# 02_Storage_DDIA - Storage Engines & Distributed Data (DDIA) Study Guide

- **Total Cards**: 746

---

## 📂 Category: API Design & Data Interchange (1 cards)

### 🟡 Mid Level

#### 1. What are two distinguishing traits of SOAP compared to REST?
**Answer:**
1. SOAP enables code generation (often via WSDL in statically typed languages).
2. SOAP is not human-readable (uses XML-based protocol envelopes), thus requiring more heavy tool support, IDE integration, and specialized clients.


## 📂 Category: APIs and Data Models (2 cards)

### 🟢 Junior Level

#### 1. How do REST and SOAP fundamentally differ in architecture, and what are two distinguishing traits of SOAP?
**Answer:**
REST is a design philosophy building upon HTTP principles without a strict protocol definition, whereas SOAP is an XML-based protocol for making network API requests.
Two distinguishing traits of SOAP:
1. Enables code generation.
2. Is not human-readable, requiring extensive tooling.

#### 2. In RESTful APIs using JSON, what types of changes to request and response payloads are generally considered backward-compatible?
**Answer:**
Adding optional request parameters and adding new fields to response objects.


## 📂 Category: Architectural Patterns (1 cards)

### 🟡 Mid Level

#### 1. What is Command Query Responsibility Segregation (CQRS)?
**Answer:**
An architectural pattern that separates the data models and paths used for writing data (Commands) from those used for reading data (Queries), often maintaining multiple denormalized read views optimized for specific access patterns.


## 📂 Category: Asynchronous Messaging (1 cards)

### 🟢 Junior Level

#### 1. What are JMS and AMQP?
**Answer:**
JMS (Java Message Service) and AMQP (Advanced Message Queuing Protocol) are industry standards for message brokers and asynchronous messaging systems.


## 📂 Category: Batch & Stream Processing (6 cards)

### 🟡 Mid Level

#### 1. How do distributed dataflow engines typically structure operators within a processing job?
**Answer:**
As a Directed Acyclic Graph (DAG), where the flow of data from one operator transformation to another is structured explicitly as a graph.

#### 2. How does compaction affect operational latencies, and what is materialization in the context of MapReduce jobs?
**Answer:**
Compaction can increase latencies of read and write operations because background disk I/O and disk bandwidth contention can stall active operations. Materialization is the process of writing intermediate state files when the output of one MapReduce job is passed as input to another.

#### 3. What core programming paradigm and data characteristic does batch processing encourage to minimize side effects and speed up feature development?
**Answer:**
Batch processing is functional: it encourages deterministic, pure functions whose outputs depend only on their inputs, have no side effects, and operate on immutable inputs. This minimizes irreversibility, making it safer and faster to develop and iterate on features because mistakes are not permanently destructive.


### 🔴 Senior Level

#### 1. How do distributed dataflow engines handle intermediate state faults without fully materializing state to HDFS?
**Answer:**
They tolerate faults that lose intermediate state by recomputing it from other available data, such as a prior checkpointed intermediate stage or the original input data.

#### 2. When building a dataflow engine workflow, why might recomputing intermediate data upon a fault be a bad idea, and when should you materialize instead?
**Answer:**
If the intermediate derived dataset is much smaller than the source data, recomputing it is too expensive, so it is better to materialize (persist) the intermediate results.

#### 3. Why is using batch and stream processing to reprocess existing data a good mechanism for evolving to support new features?
**Answer:**
Derived views allow gradual evolution: instead of performing a disruptive sudden schema migration, you can maintain the old and new derived data schemas side by side and shift users or services over time.


## 📂 Category: Batch Processing (41 cards)

### 🟢 Junior Level

#### 1. Following the Unix philosophy, what two principles are critical for performance and maintainability in batch processing?
**Answer:**
1. Treating inputs as immutable.
2. Avoiding side effects.

#### 2. How does Hadoop's architecture compare to a distributed version of Unix?
**Answer:**
Hadoop is analogous to a distributed Unix system where HDFS acts as the distributed filesystem and MapReduce acts as a distributed process framework that inherently runs a sort utility between the map and reduce phases, allowing users to indiscriminately dump raw data into HDFS and figure out how to process it later (schema-on-read).

#### 3. In MapReduce, how do you handle a bug in code that produces wrong or corrupted output?
**Answer:**
You can simply roll back the code and rerun the job, or keep the old output.

#### 4. In MapReduce, what are the intermediate state files called, and how are they typically used?
**Answer:**
The intermediate state files are called materialization. In many cases, the output of one MapReduce job is only used as the input to one other job.

#### 5. What architectural components and steps are typically illustrated in a basic batch processing job pipeline?
**Answer:**
A MapReduce task structure consisting of multiple mappers and multiple reducers processing partitioned datasets.

#### 6. What is MapReduce?
**Answer:**
MapReduce is a programming model and framework for batch processing large datasets across a distributed filesystem.

#### 7. What is a common design pattern for chaining multiple MapReduce jobs?
**Answer:**
They are chained together into workflows, where the output of one MapReduce job automatically becomes the input to the subsequent job.

#### 8. What is a common production use case for batch processing systems like MapReduce or Spark?
**Answer:**
Building and training machine learning models, running offline data warehouse aggregations, and large-scale historical log analysis.

#### 9. What is the characteristic of input data in a batch processing job?
**Answer:**
The input data is bounded, meaning it has a known, fixed size, allowing the job to know when it has finished reading and will eventually complete.

#### 10. What is the function of the Mapper in a MapReduce job?
**Answer:**
It is called once for every input record, extracts zero or more (key, value) pairs, and maintains no state across records.

#### 11. What is the role of the Reducer in MapReduce?
**Answer:**
The framework collects all values sharing the same key and calls the reducer with an iterator over that collection, allowing the reducer to emit output records.

#### 12. What project demonstrated that a SQL query execution engine could be built on top of HDFS and MapReduce?
**Answer:**
The Hive project.

#### 13. What separation of concerns does the MapReduce programming model provide?
**Answer:**
MapReduce separates physical network communication (the wiring—getting data to the right machine) from the application logic (processing the data once it is received).


### 🟡 Mid Level

#### 1. Describe the lifecycle stages of data handling between mappers and reducers in MapReduce.
**Answer:**
Mappers are partitioned according to input file blocks. The output of mappers is repartitioned, sorted, and merged into a configurable number of reducer partitions. The purpose is to bring all related data (e.g., records with the same key) together in the same place.

#### 2. How are operations like GROUP BY implemented in MapReduce?
**Answer:**
Similar to distributed joins, by having mappers emit key-value pairs where the key is the desired grouping key, allowing the shuffle phase to group all matching values together for the reducers.

#### 3. How do MapReduce map tasks partition their output?
**Answer:**
Each map task in MapReduce partitions its output by reducer (using a partitioning function like hashing on the key) so that all records for the same key are sent to the same reducer.

#### 4. How do sort-merge joins operate in distributed batch processing frameworks?
**Answer:**
Each input dataset goes through a mapper that extracts the join key. Through partitioning, sorting, and merging stages, all records with the same join key are routed to the same reducer function, which then outputs the joined records.

#### 5. How does MapReduce determine which reduce task should receive a particular key-value pair during the shuffle phase?
**Answer:**
MapReduce uses a hash function of the key to route the key-value pair to the appropriate reduce task.

#### 6. How does a sort-merge join bring together related data for a specific key (such as a user ID) in MapReduce?
**Answer:**
The mappers and the distributed sorting process ensure that all necessary data for a particular key is brought together and routed to a single call to the reducer.

#### 7. How is MapReduce utilized to build a distributed search index?
**Answer:**
Mappers partition the set of input documents as needed (e.g., by term hash or range), and the reducers aggregate the terms and build the inverted index for their assigned partition.

#### 8. In a MapReduce job, where should external dataset copies be placed to perform an efficient reduce-side join instead of querying a live database server?
**Answer:**
Take a copy of the database via an ETL process and place it directly into the same distributed filesystem used by the MapReduce cluster.

#### 9. In batch processing, what is the term for a system design where a failed task is retried and produces an output effect as if it was processed exactly once?
**Answer:**
This is known as exactly-once semantics, or more accurately, effectively-once semantics (achieved via idempotent writes or atomic transactions).

#### 10. In distributed dataflow frameworks like MapReduce, which data processing task is implemented using a mechanism similar to joins?
**Answer:**
Grouping (GROUP BY operations), which also requires shuffling data by key across the network to colocate related records.

#### 11. What are dataflow engines (like Spark) and how do they differ from traditional MapReduce?
**Answer:**
Dataflow engines do not take strict roles of alternating map and reduce phases. Instead, they can be assembled in more flexible ways, where each processing function is called an operator.

#### 12. What are the performance trade-offs of using a reduce-side join in MapReduce?
**Answer:**
It requires no prior assumptions about the input data, but comes at a high performance cost due to network shuffling, sorting, copying to reducers, and merging.

#### 13. What are the size and memory requirements for the two datasets involved in a broadcast hash join?
**Answer:**
One dataset is large, and the other dataset is small enough to fit entirely into memory.

#### 14. What are the trade-offs of MapReduce frequently writing intermediate state to disk?
**Answer:**
Writing to disk makes it easy to recover from an individual failed task without restarting the entire job, but it slows down execution in the failure-free case compared to in-memory processing frameworks.

#### 15. What does a reduce-side sort-merge join on a user ID visualize?
**Answer:**
A distributed batch processing join operation where mappers tag and partition records by key (user ID), and reducers pull, sort, and merge the sorted streams from both datasets.

#### 16. What is 'sessionization' in the context of MapReduce and log analysis?
**Answer:**
Sessionization is the process of grouping and collating all activity events for a user session when those events are initially scattered across various servers' log files.

#### 17. What is a broadcast hash join in distributed stream/batch processing?
**Answer:**
An optimization where a small dataset is small enough to fit completely in memory, allowing it to be broadcast and loaded into local memory on each mapper or worker node, eliminating the need for a heavy shuffle phase.

#### 18. What is the MapReduce scheduling optimization known as 'putting the computation near the data' and why is it used?
**Answer:**
The scheduler tries to run each mapper on one of the machines that stores a replica of the input file blocks. This saves network load and unnecessary data copying.

#### 19. What is the primary role of output and input directories in MapReduce jobs, and why is this design advantageous for publishing data?
**Answer:**
Every MapReduce job is independent. The only contact points of a job with the rest of the world are its input and output directories on the distributed filesystem. This is ideal when the output is something you want to publish (e.g., serving as the input to several other downstream jobs).

#### 20. Why is MapReduce considered appropriate for larger jobs that expect at least one task failure along the way?
**Answer:**
MapReduce is designed with fault tolerance in mind. It provides automatic retries for individual map or reduce tasks that experience transient failures. These retries are safe because map inputs are immutable, and tasks write eagerly to disk.

#### 21. Why is it important to execute a reduce-side sort-merge join rather than remote lookups in large-scale analytic batch jobs?
**Answer:**
Making a remote database network lookup for every individual ID across millions of rows creates excessive network round-trips, making it orders of magnitude too slow compared to batch sorting and merging.


### 🔴 Senior Level

#### 1. How does the Pregel graph processing model operate and differ from MapReduce?
**Answer:**
In the Pregel model, a vertex can send messages along edges. In each iteration, a function is called for each vertex along with its incoming messages (like a reducer). Unlike MapReduce, a vertex remembers its state from one iteration to the next and only processes new incoming messages.

#### 2. Instead of writing directly to an online database from a MapReduce batch job, what architectural pattern should be used?
**Answer:**
You should build a brand-new database inside the batch job which can then be bulk-loaded into servers that handle read-only queries, avoiding race conditions and high locking overhead on the online transactional database.

#### 3. What are the primary strengths and limitations of Massively Parallel Processing (MPP) databases compared to MapReduce?
**Answer:**
MPP databases are highly optimized for analytic SQL queries and often keep working sets in memory when possible. However, not all complex processing workflows (such as machine learning pipeline training, building search indexes, or image analysis) can be expressed cleanly as SQL queries, which is where flexible frameworks like MapReduce excel.

#### 4. What are the three downsides of MapReduce materializing intermediate state between jobs?
**Answer:**
1. A MapReduce job can only start when all tasks in preceding jobs have completed, slowing down workflows if there are straggler tasks caused by skew or varying load.
2. Mappers are sometimes unnecessary when reducers could otherwise be chained directly.
3. Intermediate state stored in a distributed filesystem means files are replicated across multiple nodes, adding unnecessary I/O overhead.

#### 5. What are the three main reasons to avoid writing directly to your online database from inside a MapReduce batch job?
**Answer:**
1. Making network requests to the database is significantly slower than the typical throughput capacity of a batch task.
2. MapReduce runs tasks in massive parallelism, which can easily overwhelm and degrade the database.
3. MapReduce provides clean all-or-nothing guarantees for final job outputs, whereas writing side effects directly during job execution complicates handling partially-completed jobs and rollbacks.

#### 6. What is a partitioned hash join?
**Answer:**
If two join inputs are partitioned in the exact same way (using the same key, hash function, and number of partitions), the hash table join approach can be executed independently and in parallel for each corresponding pair of partitions.

#### 7. What methods are used in distributed data processing and batch joins to compensate for data skew?
**Answer:**
Skewed join or sharded join methods are used to compensate for data skew by redistributing or handling disproportionately large partitions.


## 📂 Category: Batch Processing & Joins (2 cards)

### 🟡 Mid Level

#### 1. When writing an analytic batch job over event logs, what algorithm is typically needed to perform a join between the events and a user database?
**Answer:**
Sort-merge join.


### 🔴 Senior Level

#### 1. How can you optimize joins in MapReduce when making assumptions about the input data structure?
**Answer:**
By using a map-side join, which eliminates the need for reducers and network shuffling/sorting.


## 📂 Category: Batch Processing & MapReduce (6 cards)

### 🟢 Junior Level

#### 1. What is the original primary use case for MapReduce?
**Answer:**
To build search indexes.


### 🟡 Mid Level

#### 1. In a MapReduce join between activity events and a user database, how does a sort-merge join organize records at the reducer?
**Answer:**
One set of mappers reads activity events using the user ID as the key, and another set reads the user database with the user ID as the key. The MapReduce framework sorts by user ID so that matching user records and activity events become adjacent. Using a secondary sort, the framework can be arranged to place the user database record first, followed by the activity events in timestamp order on the reducer.

#### 2. What is 'shuffling' in the context of MapReduce processing?
**Answer:**
Shuffling is the process where the MapReduce scheduler notifies the reducers when they can start fetching the output files of sorted key-value pairs for their specific partition from the mappers over the network.

#### 3. When does the MapReduce pattern of bringing all records with the same key to the same place break down?
**Answer:**
It breaks down if there is a very large amount of data related to a single key (skewed keys), causing severe hot-spotting on a single reducer node.


### 🔴 Senior Level

#### 1. How could you use two stages of MapReduce to deal with hot spots and data skew?
**Answer:**
Perform grouping in two stages: the first sends records to a random reducer, so each reducer performs grouping on a subset of records for hot keys and outputs a compact aggregate value per key. The second job then combines the values from the first stage.

#### 2. Why do graph processing algorithms (like PageRank or shortest path) not lend themselves well to standard MapReduce?
**Answer:**
Graph processing algorithms are iterative ('repeat until done') and require frequent communication across heavily interconnected data vertices. Standard MapReduce is designed for acyclic, batch-oriented data flows, making multi-phase iterative graph traversals extremely inefficient due to repeated disk I/O and network shuffling between jobs.


## 📂 Category: Batch and Stream Processing (1 cards)

### 🟡 Mid Level

#### 1. What is the 'read path' in the context of derived datasets and stream/batch processing architectures?
**Answer:**
The read path is how the system responds to a user request to read from a derived dataset. In contrast to the write path (which precomputes and materializes data ahead of time), the read path executes dynamically only when a user explicitly requests the data.


## 📂 Category: Clocks & Time (2 cards)

### 🟡 Mid Level

#### 1. Why are time-of-day clocks unsuitable for measuring elapsed time?
**Answer:**
Time-of-day clocks are unsuitable for measuring elapsed time because they can jump backwards in time (e.g., due to NTP synchronizations) and handle leap seconds unpredictably.

#### 2. Why is the absolute value of a monotonic clock meaningless and why can't it be compared across computers?
**Answer:**
Monotonic clocks measure relative time (e.g., time elapsed since system boot or an arbitrary point) and tick at a rate that can drift. Their absolute values have no relation to wall-clock time and differ across independent machines, making them only useful for measuring time intervals on a single node.


## 📂 Category: Column-Oriented Storage (1 cards)

### 🔴 Senior Level

#### 1. How does Vertica store replicas of its column-oriented data?
**Answer:**
Vertica stores replicas of its column-oriented data in different sort orders to optimize different query access paths.


## 📂 Category: Concurrency & Hardware (1 cards)

### 🔴 Senior Level

#### 1. Is RAM on a modern multi-core CPU linearizable? Why or why not?
**Answer:**
No. Modern multi-core CPU RAM is not linearizable because each core has its own private memory cache and store buffer. Writes are asynchronously propagated to main memory or other caches unless explicit memory barriers or fences are used.


## 📂 Category: Concurrency Control (5 cards)

### 🟡 Mid Level

#### 1. How does Two-Phase Locking (2PL) handle deadlocks, and what is the responsibility of the application when they occur?
**Answer:**
The database automatically detects deadlocks by analyzing transaction wait-for graphs and aborts one of the transactions to allow others to progress. The application is responsible for catching the error and safely retrying the aborted transaction.

#### 2. How does Two-Phase Locking (2PL) work for concurrency control?
**Answer:**
It allows multiple transactions to concurrently read the same object as long as no transaction is writing to it. However, the moment any transaction wants to write (modify or delete) an object, exclusive access is strictly required, blocking other readers and writers.

#### 3. T/F: Although deadlocks occur with lock-based read committed isolation, they happen much more frequently under 2PL serializable isolation.
**Answer:**
True. Strict Two-Phase Locking (2PL) holds locks until the end of the transaction and acquires many more locks, significantly increasing the probability of deadlock depending on access patterns.

#### 4. What are the blocking rules in Two-Phase Locking (2PL) between readers and writers?
**Answer:**
If transaction A has read an object and B wants to write, B must wait until A commits or aborts. If A has written an object and B wants to read, B must also wait until A commits or aborts to prevent reading uncommitted or dirty data.


### 🔴 Senior Level

#### 1. T/F: Snapshot isolation (and Serializable Snapshot Isolation) is linearizable.
**Answer:**
False. Snapshot isolation reads from a consistent snapshot to avoid reader/writer lock contention. Because it purposefully excludes writes more recent than the snapshot's timestamp, reads are not linearizable.


## 📂 Category: Consensus & Linearizability (1 cards)

### 🔴 Senior Level

#### 1. How does application requirement for linearizability affect system availability during network partitions?
**Answer:**
If an application does not require linearizability (e.g., multi-leader), replicas process requests independently, remaining available during network partitions but sacrificing linearizability. If linearizability is required, disconnected replicas become unavailable to preserve correctness.


## 📂 Category: Consistency & Consensus (2 cards)

### 🔴 Senior Level

#### 1. What consensus and coordination abstractions act as the distributed equivalent of single-node transactions?
**Answer:**
Consensus algorithms (such as Paxos, Raft, or Zab), leader election protocols, and atomic commit protocols (like Two-Phase Commit). These hide network partitions, process crashes, and split-brain risks from application logic.

#### 2. What database consistency models reflect the difference between total ordering and partial ordering, and what is a classic non-database analog for the latter?
**Answer:**
Total ordering is reflected by Linearizability (every operation has a single, global timeline). Partial ordering is reflected by Causality (concurrent operations are incomparable, forming a DAG). A classic analog for partial ordering is Git version control history, which has linear commits, branches, and merges.


## 📂 Category: Data Architecture (1 cards)

### 🟢 Junior Level

#### 1. What is polyglot persistence?
**Answer:**
The architectural approach of using a mix of different relational and non-relational datastores chosen specifically to fit the varying requirements of different application use cases.


## 📂 Category: Data Encoding & Evolution (4 cards)

### 🟢 Junior Level

#### 1. What are 2 fundamental memory representations programs use to handle data?
**Answer:**
1. In-memory structures: Objects, structs, arrays, hash tables, and trees optimized for CPU access via memory pointers.
2. Serialized byte sequences: Self-contained byte streams (e.g., JSON, Avro, Protobuf) optimized for network transmission or persistent disk storage where pointers are invalid.

#### 2. What are the three primary modes of dataflow, and what famous aphorism describes data evolution across them?
**Answer:**
1. Through Databases (the writer encodes, future reader decodes).
2. Through RPC and REST APIs (clients encode requests, servers decode requests and encode responses).
3. Through Asynchronous Message Passing (message brokers or actors passing encoded payloads between nodes).
Aphorism: "May your application’s evolution be rapid and your deployments be frequent."


### 🟡 Mid Level

#### 1. Why is Protocol Buffers often frowned upon in dynamically typed programming languages, and why is Avro more flexible in this regard?
**Answer:**
Protocol Buffers rely strictly on code generation from .proto files, presenting an unnecessary obstacle in dynamically typed languages that lack a compile-time type checker. Avro is more flexible because it does not require code generation; it supports self-describing container files that embed the writer's schema directly alongside the binary data.


### 🔴 Senior Level

#### 1. Define backward and forward compatibility, explain why each is achieved or challenging, and describe their role in rolling deployments and databases.
**Answer:**
Backward compatibility means newer code can read data written by older code; it is usually straightforward because the author of newer code knows the old format. Forward compatibility means older code can read data written by newer code; it is trickier because it requires older code to ignore additions made by newer versions. Both are vital in databases and distributed systems during rolling upgrades where old and new application versions coexist and access shared data formats.


## 📂 Category: Data Encoding & Serialization (4 cards)

### 🟢 Junior Level

#### 1. What are the three primary types of data encoding formats, along with characteristics or examples of each?
**Answer:**
1. Programming language-specific encodings (e.g., Python pickle): Restricted to a single language, often lack forward/backward compatibility and security guarantees.
2. Textual formats (JSON, XML, CSV): Human-readable, widespread, but have ambiguous typing and weak/optional schemas.
3. Binary schema-driven formats (Thrift, Protocol Buffers, Avro): Compact, efficient, with explicitly defined forward/backward compatibility semantics and code generation capabilities.


### 🟡 Mid Level

#### 1. What are the key advantages of schema-driven binary encoding formats (e.g., Protocol Buffers, Avro) over textual formats?
**Answer:**
1. Much more compact payloads due to omitted field names.
2. Schemas act as authoritative, up-to-date documentation.
3. Schema registries enable automated validation of forward and backward compatibility before deployment.
4. Seamless code generation and type checking for statically typed languages.

#### 2. What are the primary problems with textual encoding formats like JSON, XML, and CSV? Give an example of a related issue at Twitter.
**Answer:**
1. Ambiguity around the encoding of numbers (e.g., lack of distinction between integers and floats, lack of precision specification, issues with numbers exceeding 2^53 in JavaScript).
2. Lack of native support for binary strings (requiring Base64 encoding which increases size by ~33%).
3. Schema support is either complex/optional (JSON/XML) or completely absent (CSV).
Example: Twitter IDs exceeded 2^53 and could not be accurately represented by JavaScript floating-point numbers, forcing Twitter to transmit IDs both as numbers and as decimal strings.

#### 3. Why is it a bad practice to use a programming language's built-in object serialization/encoding for long-term storage or inter-system communication?
**Answer:**
1. Language-lock-in: Tightly coupled to a specific programming language, making cross-platform or polyglot integration extremely difficult.
2. Security vulnerabilities: Decoding often requires instantiating arbitrary classes, allowing attackers who supply malicious byte sequences to execute remote code.
3. Poor versioning support: Built-in libraries typically neglect forward and backward compatibility needs.
4. Suboptimal performance: CPU overhead for encoding/decoding and bloated payload sizes are often major performance bottlenecks (e.g., Java serialization).


## 📂 Category: Data Engineering (1 cards)

### 🟢 Junior Level

#### 1. Why is it often acceptable in practice to dump raw data indiscriminately into a data lake (like HDFS) instead of upfront modeling?
**Answer:**
Making raw data available quickly has higher immediate value than trying to predict the ideal data model upfront, especially since different downstream teams often require entirely different data models.


## 📂 Category: Data Engineering Principles (1 cards)

### 🟢 Junior Level

#### 1. What is the 'sushi principle' philosophy in data engineering?
**Answer:**
The sushi principle states that 'raw data is better', advocating for capturing and storing immutable raw data streams before applying heavy transformations or schemas.


## 📂 Category: Data Integration (1 cards)

### 🟡 Mid Level

#### 1. What is Change Data Capture (CDC) and how does it work?
**Answer:**
Taking data in the exact order it was written to a source database (usually via transaction log tailing) and applying those changes asynchronously to downstream systems in the same order.


## 📂 Category: Data Integration / Streaming (1 cards)

### 🟡 Mid Level

#### 1. What is Change Data Capture (CDC)?
**Answer:**
CDC is the process of observing all data changes written to a database (the system of record acting as a leader) and extracting them so they can be replicated to derived data systems (followers) as a stream immediately as they are written.


## 📂 Category: Data Integration / Unix Philosophy (1 cards)

### 🟢 Junior Level

#### 1. What is it called when Unix programs do not care where their input comes from or where their output goes (relying purely on stdin and stdout), leading to loose coupling, late binding, or inversion of control?
**Answer:**
Separating the input/output wiring from the program logic, allowing small tools to be easily composed into bigger systems.


## 📂 Category: Data Modeling (4 cards)

### 🟢 Junior Level

#### 1. In data engineering, what is generally considered more valuable between making raw data available quickly versus designing an ideal upfront data model?
**Answer:**
Simply making data available quickly, even if in raw format, is more valuable than trying to decide on the ideal data model upfront.


### 🟡 Mid Level

#### 1. What are the two primary types of columns found in an OLAP fact table?
**Answer:**
1. Attributes (such as prices, quantities, and costs used for metrics calculations).
2. Foreign key references to dimension tables representing the context (who, what, where, when, why) of the event.

#### 2. What is a key structural indicator that a relational database schema is not normalized?
**Answer:**
Duplicating values that could otherwise be stored in a single centralized location.

#### 3. What is at the center of an OLAP star schema, and what do its rows represent?
**Answer:**
A fact table is at the center, where each row represents an event that occurred at a particular point in time (e.g., a customer purchase or page view).


## 📂 Category: Data Modeling & Storage (1 cards)

### 🟡 Mid Level

#### 1. What is the operational difference and trade-off between schema-on-read and schema-on-write when performing schema evolutions (e.g., splitting a full name field)?
**Answer:**
Schema-on-read (e.g., document databases) allows applications to immediately start writing new documents with updated structures, handling legacy document formats dynamically via application logic. Schema-on-write ('statically typed' DBs) requires executing explicit data migrations upfront, which on large tables can be resource-intensive and cause downtime.


## 📂 Category: Data Models (4 cards)

### 🟢 Junior Level

#### 1. What are the structural components and attributes of vertices and edges in the property graph model?
**Answer:**
Each vertex consists of a unique identifier, outgoing edges, incoming edges, and a collection of properties (key-value pairs). Each edge consists of a unique identifier, a tail vertex, a head vertex, a relationship label, and a collection of properties (key-value pairs).

#### 2. What term describes the awkward translation layer required between in-memory object models in application code and relational database tables?
**Answer:**
An impedance mismatch (a term borrowed from electronics regarding input/output resistance and signal efficiency).

#### 3. Which two primary directions have new nonrelational "NoSQL" datastores diverged into, and what are two additional NoSQL data models?
**Answer:**
1. Document databases target use cases where data comes in self-contained documents and relationships between documents are rare.
2. Graph databases target use cases where anything is potentially related to everything.
Additional types:
3. Key-value stores
4. Column-family stores (aka wide-column stores)


### 🟡 Mid Level

#### 1. Why do Document Databases often require multi-object transactions?
**Answer:**
Document databases frequently use denormalized data across separate objects, requiring atomic updates across multiple documents to maintain consistency when relationships exist.


## 📂 Category: Data Models & Evolution (1 cards)

### 🟡 Mid Level

#### 1. When considering evolvability and dataflow through services, assuming servers are updated before clients, what RPC compatibility rules are required for requests and responses?
**Answer:**
You only need backward compatibility on requests (new servers must be able to process old client requests), and forward compatibility on responses (old clients must be able to process new server responses).


## 📂 Category: Data Models & Query Languages (6 cards)

### 🟢 Junior Level

#### 1. What are the 2 common database modeling representations used for structuring and querying graph data?
**Answer:**
1. Property graph model: Stores graphs as relational-style tables split into vertices (nodes) and edges (relationships), both capable of holding property maps.
2. Triple-store model: Stores all information as simple three-part statements: (subject, predicate, object).

#### 2. What is misleading about the term 'schemaless' for document databases, and what are more accurate terms and programming language analogies?
**Answer:**
It is misleading because applications reading the data usually assume an implicit schema, even if it isn't enforced by the database.
- Better terms: Schema-on-read (used by document dbs) vs. Schema-on-write (traditional relational dbs).
- Programming analogy: Schema-on-read is like dynamic (runtime) type checking, while schema-on-write is like static (compile-time) type checking.

#### 3. What web technology is analogous to SQL's success as a declarative query language?
**Answer:**
HTML and CSS. Just as declarative CSS styling is superior to manipulating DOM styles imperatively in JavaScript, declarative query languages like SQL are cleaner and less error-prone than imperative database query APIs.


### 🟡 Mid Level

#### 1. In a triple-store graph structure, what are the two possible types of values that an object can represent relative to the subject?
**Answer:**
1. A value in a primitive datatype (e.g., string, number), where the predicate and object act as a key-value property on the subject vertex.
2. Another vertex in the graph, where the predicate acts as a directed edge connecting the subject (tail vertex) to the object (head vertex).

#### 2. In what specific scenarios is schema-on-read advantageous over schema-on-write?
**Answer:**
Schema-on-read is advantageous when data is heterogeneous, specifically when:
1. There are many different types of objects, and putting each type in its own table is impractical.
2. The structure of the data is determined by external systems over which you have no control and which may change at any time.

#### 3. What are the three main arguments in favor of a document data model, and what three things does the relational model counter with?
**Answer:**
Document model advantages: 1. Schema flexibility, 2. Better performance due to data locality, 3. Closer alignment with application data structures (less impedance mismatch).
Relational model counter-support: 1. Joins, 2. Many-to-one relationships, 3. Many-to-many relationships.


## 📂 Category: Data Models & Storage Engines (1 cards)

### 🟡 Mid Level

#### 1. When does the storage locality advantage of a document database apply, and what are the performance recommendations regarding document size?
**Answer:**
Locality applies only when you need large parts of the document at the same time, avoiding multiple index lookups. However, because databases often must load the entire document and rewrite it on size-increasing updates, it is recommended to keep documents fairly small and avoid updates that increase their encoded size.


## 📂 Category: Data Processing (2 cards)

### 🟢 Junior Level

#### 1. What are the two callback functions you must implement to create a MapReduce job?
**Answer:**
Mapper and Reducer.


### 🟡 Mid Level

#### 1. What types of dataset transformation functions require application-specific code?
**Answer:**
Full-text search, machine learning feature engineering, and caches for displaying UI.


## 📂 Category: Data Processing & Architecture (1 cards)

### 🟢 Junior Level

#### 1. When one dataset is derived from another, what functional component does it pass through?
**Answer:**
A transformation function.


## 📂 Category: Data Serialization (2 cards)

### 🟡 Mid Level

#### 1. In Protocol Buffers, how are omitted/unset field values handled in the encoded record, and what makes up the encoded record bytes?
**Answer:**
If a field value is not set, it is simply omitted from the encoded record. An encoded record is just the concatenation of its encoded fields.


### 🔴 Senior Level

#### 1. What are the rules regarding renaming fields, maintaining forward compatibility, and maintaining backward compatibility when evolving a Protocol Buffers schema?
**Answer:**
1. Rename: Allowed since encoded data never references field names. 2. Forward compatibility: Allowed to add new fields with new tag numbers; old code ignores unrecognized tags using datatype lengths. 3. Backward compatibility: New fields cannot be required unless they have a default value.


## 📂 Category: Data Serialization & Evolution (1 cards)

### 🟢 Junior Level

#### 1. What is encoding in the context of data systems, what are its synonyms, and what terminology conflicts exist?
**Answer:**
Encoding is the translation from an in-memory application representation to a byte sequence. Synonyms include serialization or marshalling. The reverse is called decoding (aka parsing, deserialization, unmarshalling). Terminology clash: 'Serialization' is also used in the context of database transactions (Serializable isolation) with a completely different meaning, so 'encoding' is preferred to avoid ambiguity.


## 📂 Category: Data Structures & Compression (1 cards)

### 🟡 Mid Level

#### 1. How can sparse bitmaps be efficiently encoded?
**Answer:**
Sparse bitmaps can be efficiently encoded using run-length encoding (RLE), which compresses sequences of repeated bits (typically zeros) by storing the count and the value.


## 📂 Category: Data System Foundations (1 cards)

### 🟢 Junior Level

#### 1. What are the 3 core design principles that cover software maintainability, and what famous aphorism applies to the first?
**Answer:**
1. Operability: Making life easy for operations teams. Aphorism: 'Good operations can often work around the limitations of bad software, but good software cannot run reliably with bad operations.'
2. Simplicity: Managing complexity and avoiding the 'big ball of mud' to help new engineers understand the system.
3. Evolvability: Making change easy and adapting the system to unanticipated use cases as requirements shift.


## 📂 Category: Data Systems & APIs (1 cards)

### 🟡 Mid Level

#### 1. What are 3 common ways for RESTful APIs to implement API versioning?
**Answer:**
1. Use a version number in the URL.
2. Use a version number in the HTTP Accept header.
3. Store a client's requested API version on the server (often tied to API keys) and allow updates via an administrative interface.


## 📂 Category: Data Systems Architecture (2 cards)

### 🟢 Junior Level

#### 1. What are the two categories of data systems?
**Answer:**
- Systems of record
- Derived data systems


### 🔴 Senior Level

#### 1. What is commonly cited as the missing piece of composing heterogeneous data systems together?
**Answer:**
Unlike the Unix shell which provides a universal piping mechanism (e.g., cat file | grep | awk), data systems lack a standardized, unbundled-database equivalent for piping data systems together seamlessly (e.g., MySQL piped directly into Elasticsearch).


## 📂 Category: Data Warehousing (4 cards)

### 🟢 Junior Level

#### 1. In data warehousing and dimensional modeling, how are dates and times typically represented?
**Answer:**
Dimension tables (often called date dimensions or calendar tables), which store attributes like day of week, month, holiday status, etc., to simplify analytical queries.

#### 2. What is a data cube or OLAP cube?
**Answer:**
A data cube (or OLAP cube) is a multi-dimensional grid of pre-computed aggregates grouped by different business dimensions, optimized for fast analytical querying.

#### 3. What is the process of getting data into an OLAP data warehouse called?
**Answer:**
ETL (Extract, Transform, Load)


### 🔴 Senior Level

#### 1. What compression technique is particularly effective in columnar data warehouses?
**Answer:**
Bitmap encoding (and run-length encoding on sorted columns), which converts distinct values into separate bitmaps where each bit represents a row.


## 📂 Category: Distributed Architecture (1 cards)

### 🟢 Junior Level

#### 1. Most web applications are deployed as stateless services, delegating state management entirely to databases which maintain the shared mutable state.
**Answer:**



## 📂 Category: Distributed Communication & RPC (2 cards)

### 🟡 Mid Level

#### 1. What are the 5 primary advantages of using an asynchronous message broker compared to direct RPC communication?
**Answer:**
1. Acts as a buffer if the recipient is unavailable or overloaded, improving system reliability.
2. Automatically redelivers messages to prevent data loss if a consumer process crashes.
3. Eliminates the need for the sender to know the recipient's IP address and port (crucial in dynamic cloud environments).
4. Enables fan-out by allowing a single message to be delivered to multiple recipients.
5. Logically decouples the producer from the consumer.


### 🔴 Senior Level

#### 1. Why is the "location transparency" abstraction in Remote Procedure Calls (RPC) considered fundamentally flawed compared to local function calls?
**Answer:**
1. Unpredictability: Network requests can fail silently due to transient network partitions.
2. Timeouts: A timeout leaves the caller uncertain whether the request reached the remote service and executed.
3. Retries & Idempotency: Retrying failed requests requires explicit deduplication mechanisms.
4. Latency: Network round-trips are orders of magnitude slower and exhibit high variance.
5. Memory References: Complex pointers cannot be passed across the network and must be serialized.
6. Language Interoperability: Type systems differ across languages, requiring complex translation layers.


## 📂 Category: Distributed Consensus (13 cards)

### 🟢 Junior Level

#### 1. How is the consensus problem formally defined, and what is a classic business/system example?
**Answer:**
Formal definition: One or more nodes may propose values, and the consensus algorithm must decide on exactly one of those proposed values.
Example: Determining the winner when multiple concurrent users attempt to book the last seat on an airplane or register with the same unique username.


### 🟡 Mid Level

#### 1. What is the most common type of quorum used in distributed systems, and why are quorums necessary?
**Answer:**
The most common quorum is an absolute majority (more than half the nodes: n/2 + 1). Quorums are necessary because individual nodes cannot trust their own local view due to potential network partitions or node failures. By requiring minimum overlapping votes for reads, writes, or node failure declarations, quorums guarantee system safety and ensure conflicting decisions cannot happen concurrently.

#### 2. What role do epoch numbers (ballots, terms, or view numbers) play in consensus and leader-based replication protocols?
**Answer:**
Consensus protocols define an epoch number (also known as a ballot number, term, or view number) to guarantee that within any given epoch, the leader is strictly unique. This helps prevent split-brain scenarios and orders state changes monotonically across leadership transitions.

#### 3. What type of failure poses a significant challenge for consensus systems that require a strict majority of nodes to operate?
**Answer:**
Network failures (such as network partitions), which can split the cluster and prevent a strict majority (quorum) from being reached.


### 🔴 Senior Level

#### 1. What are the 4 properties that a fault-tolerant consensus algorithm must satisfy?
**Answer:**
1. Uniform agreement: No two nodes decide differently.
2. Integrity: No node decides twice.
3. Validity: If a node decides value v, then v was proposed by some node (rules out trivial solutions like always returning null).
4. Termination: Every node that does not crash eventually decides some value (a liveness property requiring a majority of nodes to be functioning correctly).

#### 2. What are the major structural and operational costs/limitations associated with consensus algorithms?
**Answer:**
1. Synchronous Replication Overhead: Nodes must vote on proposals, behaving like synchronous replication which can lead to blocked writes or data loss during failovers if not properly managed.
2. Strict Majority Requirement: Consensus systems require a strict majority (quorum) to operate. A minority partition cannot make progress, and network splits can lead to unavailability.
3. Fixed Membership Assumptions: Most standard consensus algorithms assume a static set of participating nodes. Dynamic membership changes introduce significant protocol complexity.
4. Timeout Sensitivity and Instability: Systems rely on timeouts for failure detection. In networks with high variance in latency, false-positive node failure assumptions trigger frequent, performance-degrading leader elections (e.g., Raft edge cases with unstable links).

#### 3. What are the two primary situations in distributed systems where it is critical for nodes to reach consensus?
**Answer:**
1. Leader election (preventing split-brain and divergence in single-leader replication).
2. Atomic commit (ensuring all nodes agree on transaction outcomes across partitions).

#### 4. What is a Byzantine fault and what is the Byzantine Generals Problem?
**Answer:**
A Byzantine fault occurs when nodes can fail arbitrarily by sending false, conflicting, or corrupted data ("lying"). The Byzantine Generals Problem is the classic distributed consensus challenge of achieving agreement among decentralized nodes when such malicious or faulty actors are present.

#### 5. What is the difference between consensus and quorum in distributed systems?
**Answer:**
Consensus requires all participants in a discussion or system to agree on a proposal, result, or plan (e.g., if N participants agree, N/2 + 1 or more is a quorum). Quorum achieves a minimum number of votes (typically N/2 + 1) that a distributed transaction must obtain to perform an operation. Consensus is difficult when human emotions or complex voting are involved, whereas quorums are used in distributed systems to enforce consistent operations.

#### 6. What is the primary difference between Two-Phase Commit (2PC) and fault-tolerant consensus algorithms regarding voting and coordination?
**Answer:**
Fault-tolerant consensus algorithms require votes only from a majority (quorum) of nodes, and use an elected leader with epoch/term numbers. In contrast, 2PC requires a unanimous 'yes' vote from every participant, and its coordinator is pre-determined rather than elected.

#### 7. What is the relationship between consensus services (such as ZooKeeper and etcd), total order broadcast, and consensus?
**Answer:**
Consensus services like ZooKeeper and etcd actually implement total order broadcast. This demonstrates that there is a strong, deep mathematical equivalence and connection between total order broadcast and consensus.

#### 8. What role do tools like ZooKeeper play in distributed systems regarding coordination primitives?
**Answer:**
They provide 'outsourced' consensus, failure detection, and membership services so applications do not need to implement complex fault-tolerant consensus algorithms from scratch.

#### 9. What two safety properties must always be satisfied for total order broadcasting?
**Answer:**
1. Reliable delivery (no messages are lost; if a message is delivered to one node, it is delivered to all nodes).
2. Total ordered delivery (messages are delivered to every node in the exact same order).


## 📂 Category: Distributed Consensus & Consistency (2 cards)

### 🟡 Mid Level

#### 1. What are synonyms for linearizability in distributed data systems?
**Answer:**
Atomic consistency, strong consistency, immediate consistency, or external consistency.


### 🔴 Senior Level

#### 1. What are the four primary distributed replication methods, and how do they align with linearizability?
**Answer:**
1. Single-leader replication: Potentially linearizable if reads go to the leader or synchronously updated followers, but prone to violations due to snapshot isolation, async failover, or split-brain/delusional leaders.
2. Consensus algorithms (e.g., Raft, Paxos): Linearizable. Protocols explicitly prevent split-brain and stale reads, safely implementing strong consistency (e.g., etcd, ZooKeeper).
3. Multi-leader replication: Not linearizable. Concurrent writes on multiple nodes with asynchronous propagation create conflicts.
4. Leaderless replication (Dynamo-style): Probably not linearizable. Even with strict quorums ($w + r > n$), mechanisms like 'Last Write Wins' (LWW) utilizing time-of-day clocks fail due to clock skew, and sloppy quorums break linearizability entirely.


## 📂 Category: Distributed Consensus & Coordination (3 cards)

### 🔴 Senior Level

#### 1. What are the two core safety properties required by a total order broadcast protocol?
**Answer:**
1. Reliable delivery: No messages are lost; if a message is delivered to one node, it is delivered to all nodes.
2. Totally ordered delivery: Messages are delivered to every node in the exact same order.

#### 2. What fundamental challenges in distributed systems does total order broadcasting address when moving beyond single-leader replication?
**Answer:**
It addresses how to scale throughput beyond what a single leader's CPU core can handle, and how to handle failover when the primary leader node fails.

#### 3. What is total order broadcasting (also known as atomic broadcasting) in distributed systems?
**Answer:**
It is generally described as a protocol for exchanging messages between nodes such that all messages are delivered to all nodes in the same exact order.


## 📂 Category: Distributed Consensus & Fault Tolerance (1 cards)

### 🔴 Senior Level

#### 1. What are the performance implications of nodes voting on proposals in a consensus algorithm?
**Answer:**
Consensus algorithms act as a form of synchronous replication. Because nodes must coordinate and agree on proposals across the network before committing, it introduces latency and impacts overall write performance.


## 📂 Category: Distributed Consensus & Replication (1 cards)

### 🟡 Mid Level

#### 1. What is the state machine replication principle, and what distributed primitive helps fulfill it?
**Answer:**
State machine replication dictates that if every message represents a write, and every replica processes the exact same writes in the exact identical order, all replicas will remain consistent (barring replication lag). Total order broadcast is the primitive required to fulfill this principle.


## 📂 Category: Distributed Consistency (5 cards)

### 🟡 Mid Level

#### 1. What are the alternative names for Linearizability?
**Answer:**
Linearizability is also frequently referred to as atomic consistency, strong consistency, immediate consistency, or external consistency.


### 🔴 Senior Level

#### 1. T/F: A consistency model that provides causal consistency must also be linearizable. Give two examples to justify your position.
**Answer:**
False. Examples include: 1) Git version control (tracks causal commit history and branches without global linearizability), and 2) Snapshot Isolation (reads from a consistent causal snapshot, but stale reads mean it is not linearizable).

#### 2. What do points on a linearizability timeline graph visualize, and what does a failing final read indicate?
**Answer:**
They show the points in time between invocation and completion where reads and writes appear to take effect atomically. A failing final read indicates a violation of linearizability (staleness or monotonicity violation).

#### 3. What is linearizability in distributed data systems?
**Answer:**
Linearizability is a recency guarantee: as soon as one client successfully completes a write, all clients reading must be able to see the most recent value.

#### 4. When a web server and image resizer communicate via both file storage and a message queue, what potential race condition is introduced, and what property must the file storage possess to prevent it?
**Answer:**
Communicating via both side-channels opens up potential race conditions where messages arrive out-of-order relative to the file writes. If the File storage guarantees linearizability (strong consistency), the system will safely avoid these race conditions.


## 📂 Category: Distributed Coordination (2 cards)

### 🟡 Mid Level

#### 1. What distributed coordination service is Apache ZooKeeper modeled after?
**Answer:**
Apache ZooKeeper is modeled after Google's Chubby lock service, providing a centralized infrastructure for coordination, configuration management, and distributed locking.


### 🔴 Senior Level

#### 1. Why are logical clocks often considered a safer alternative to physical clocks for ordering events in distributed systems?
**Answer:**
Logical clocks are based on monotonically incrementing counters and causality rather than quartz-based physical time, avoiding issues caused by clock drift and synchronization skew.


## 📂 Category: Distributed Coordination & Consensus (2 cards)

### 🟡 Mid Level

#### 1. How are coordination services like ZooKeeper or Chubby commonly used in distributed systems?
**Answer:**
They are frequently used for service discovery (determining which IP address to reach for a specific service instance) and for allocating work or leadership to particular nodes in a cluster.

#### 2. What is consensus in distributed systems?
**Answer:**
Consensus is the fundamental problem of getting several distributed nodes to agree on a single value or decision (such as committing a transaction or electing a leader), which is one of the most critical abstractions in fault-tolerant distributed systems.


## 📂 Category: Distributed Data (23 cards)

### 🟢 Junior Level

#### 1. How does Network Time Protocol (NTP) synchronize computer clocks?
**Answer:**
NTP adjusts computer clocks by synchronizing them with a group of time servers that typically obtain precise time from highly accurate sources such as atomic clocks or GPS receivers.

#### 2. What are RabbitMQ and ActiveMQ examples of?
**Answer:**
They are classic examples of message brokers that implement a message-passing queue model where messages are typically deleted once acknowledged by a consumer.

#### 3. What is 'Integrity' in the context of data consistency requirements?
**Answer:**
The absence of corruption (preventing data loss or insertion of false/malformed data), such as ensuring secondary indexes accurately reflect the primary table. If integrity is violated, the resulting inconsistency is typically permanent.


### 🟡 Mid Level

#### 1. What core capability is required for applications that use event sourcing to present data to users?
**Answer:**
They must be able to deterministically transform the log of historical write events into the current application state.

#### 2. What is an AMQP/JMS-style message broker and in what scenarios is it most useful?
**Answer:**
A message broker where individual messages are assigned to consumers who acknowledge them upon successful processing, after which the messages are deleted. It is useful for task queues where strict ordering is not required and there is no need to replay historical messages.

#### 3. What is an MPP (Massively Parallel Processing) database?
**Answer:**
An MPP database is a system that focuses on the parallel execution of complex analytic SQL queries across a cluster of multiple machines, dividing workloads to accelerate data processing.

#### 4. What is an asynchronous message broker (message queue or message-oriented middleware), and how does it facilitate communication?
**Answer:**
An intermediary component in asynchronous message-passing systems that temporarily stores messages, decoupling senders from receivers without requiring a direct network connection.

#### 5. What is an atomic commit in distributed transactions?
**Answer:**
An ACID transaction guarantee across multiple nodes requiring all participating nodes to unanimously agree on the final outcome, either committing or aborting together.

#### 6. What role do load parameters play in scalable system architecture, and what are the consequences of incorrect assumptions?
**Answer:**
Architectures are built around assumptions of common versus rare operations (load parameters). If these assumptions are wrong, scaling efforts can be wasted or counterproductive, emphasizing the need for application-specific designs over generic solutions.

#### 7. What term describes modern applications (like single-page JS and mobile apps) that gain stateful client-side capabilities to function without a constant network connection?
**Answer:**
Offline-first applications.

#### 8. What underlying distributed filesystem is HBase built on top of, and what is its primary use case?
**Answer:**
HBase is an OLTP database built on top of HDFS (Hadoop Distributed File System).

#### 9. Why is writing data first to a system of record (with CDC) preferred over writing concurrently to multiple datastores?
**Answer:**
Writing first to a system of record captures changes and applies them sequentially (via Change Data Capture) to derived data systems. This avoids conflicting writes and race conditions caused by writing concurrently directly to multiple separate datastores.


### 🔴 Senior Level

#### 1. How can atomicity be achieved with partitioned logs without using an atomic commit protocol?
**Answer:**
1. The client assigns a unique request ID and appends it to a log partition.
2. A stream processor reads the log and emits multiple instruction messages to output streams (including the original request ID).
3. Further processors consume the streams, deduplicate by request ID, and apply the changes.

#### 2. What are the advantages of loose coupling using asynchronous event logs with idempotent writes for heterogeneous storage systems?
**Answer:**
1. Asynchronous event streams make the system robust to outages or slowdowns of individual components (e.g., a slowed consumer doesn't block producers or other consumers). 2. It facilitates organizational scaling by allowing different teams to independently own and develop different services and consumers.

#### 3. What core assumptions embedded in databases, frameworks, and protocols make it difficult to extend the write path end-to-end to clients?
**Answer:**
Stateless clients and synchronous request/response interactions.

#### 4. What is linearizability, and what kind of guarantee does it provide?
**Answer:**
Linearizability is a recency guarantee (also known as atomic or strong consistency). It gives the illusion that there is only a single copy of data across multiple replicas. Once a write completes, all subsequent reads must immediately return that value or a newer one, never a stale cache or replica value.

#### 5. What is the 'monotonic reads' consistency guarantee, and what anomaly does it prevent?
**Answer:**
Monotonic reads is a guarantee ensuring that if a user makes several reads in sequence, they will not see time go backward (i.e., they will not read older data after previously reading newer data). It prevents the anomaly where a user reading from asynchronous followers hits different replicas that are out of sync, making data appear to move backward in time. It can be achieved by routing a given user's requests to the same replica via consistent hashing of the user ID.

#### 6. What is the difference between how a distributed transaction system orders events versus a CDC/event sourcing system?
**Answer:**
CDC (Change Data Capture) and event sourcing use an append-only log for event ordering and asynchronous propagation, whereas distributed transactions typically rely on locking mechanisms (such as 2PL) for mutual exclusion and synchronous coordination across nodes.

#### 7. What is the relationship between linearizability and causal consistency?
**Answer:**
Linearizability is stronger than causal consistency. Linearizability implies causality: any system that is linearizable will automatically preserve causality correctly without requiring explicit vector clocks or timestamp passing.

#### 8. Why are fully linearizable systems relatively rare in practice despite their utility?
**Answer:**
Because of performance penalties (governed by network delays and the CAP theorem), not fault tolerance. Even multi-core CPU RAM often lacks strict linearizability across cores for performance reasons.

#### 9. Why is multi-leader replication not linearizable?
**Answer:**
Multi-leader replication is not linearizable because it concurrently processes writes on multiple leader nodes and asynchronously replicates those changes to other nodes, making global real-time ordering impossible without heavy coordination.

#### 10. Why is parallel execution difficult in distributed graph algorithms?
**Answer:**
Distributed graph algorithms suffer from high cross-machine communication overhead because graphs have arbitrary edges, making it extremely difficult to partition vertices across machines optimally without frequent traversal across network boundaries.

#### 11. Why is prematurely declaring a node dead problematic in distributed systems?
**Answer:**
Prematurely declaring a node dead (e.g., due to a slow GC pause or network delay) can lead to split-brain scenarios or duplicate actions, such as a failover node taking over and performing a write or side-effect that the original node is also still executing.


## 📂 Category: Distributed Data & Partitioning (2 cards)

### 🟢 Junior Level

#### 1. What is the primary reason for partitioning (sharding) data in a distributed database?
**Answer:**
The main reason is scalability. By placing different partitions on different nodes in a shared-nothing cluster, a large dataset can be distributed across many disks, and query load can be distributed across many processors.


### 🟡 Mid Level

#### 1. What are disproportionately active database records called?
**Answer:**
They are known as linchpin objects or hot keys.


## 📂 Category: Distributed Data & Replication (11 cards)

### 🟢 Junior Level

#### 1. What are the core technical motivations for replicating data across multiple machines?
**Answer:**
1. High availability: Ensuring system operation despite machine or datacenter failures.
2. Disconnected operation: Allowing applications to continue operating during network partitions or offline states.
3. Latency reduction: Placing data geographically closer to end-users.
4. Scalability: Distributing read query load across multiple read replicas to handle higher throughput.


### 🟡 Mid Level

#### 1. In multi-leader replication using custom conflict resolution logic, does conflict resolution typically apply at the level of an entire transaction or an individual row/document?
**Answer:**
It applies at the level of an individual row or document. If a transaction atomically makes multiple writes, each individual write is evaluated separately for conflict resolution.

#### 2. What are three operational scenarios where a multi-leader replication configuration makes sense?
**Answer:**
1. Multi-datacenter operation: Placing a leader in each datacenter to reduce write latency and tolerate whole-datacenter outages.
2. Clients with offline operation: Allowing devices (e.g., mobile phones, laptops) to function locally as a leader while disconnected and sync later asynchronously.
3. Collaborative editing: Enabling multiple users to make changes simultaneously to shared documents using small units of change (like keystrokes) backed by local replicas.

#### 3. What is a classic real-world example of a linearizability violation?
**Answer:**
Watching a live sports broadcast with a friend: if one person refreshes their app and sees the final score, and another person subsequently refreshes their app and sees an older ongoing score due to reading from a lagging replica, this violates linearizability because the second query is not at least as recent as the first.

#### 4. What replication topology will not work for enforcing a uniqueness constraint?
**Answer:**
Asynchronous multi-leader replication, because concurrent writes on different leaders can violate uniqueness before conflicts are detected and resolved.

#### 5. What type of timestamp provides a total ordering of operations consistent with causality?
**Answer:**
Lamport timestamp.


### 🔴 Senior Level

#### 1. How does the quorum condition w + r > n function in Dynamo-style databases, and what does it guarantee?
**Answer:**
In a system with n replicas, every write must be confirmed by w nodes, and every read must query r nodes. As long as w + r > n, at least one of the replicas read from will overlap with the most recent successful write, guaranteeing an up-to-date value can be read. If fewer than w or r nodes are available, operations fail with an error.

#### 2. What are the four primary types of database replication log implementations and their examples?
**Answer:**
1. Statement-based replication (e.g., old versions of MySQL): Logs every SQL statement executed by the leader.
2. Write-ahead log (WAL) shipping (e.g., Postgres, B-trees, LSM-tree SSTables): Replicates the stream of low-level disk block writes.
3. Logical (row-based) log replication (e.g., MySQL binlog row-based mode, CDC): Logs changes at the granularity of individual inserted, updated, or deleted rows.
4. Trigger-based replication (e.g., Oracle Databus, Postgres Bucardo): Uses application-level triggers to write changes to a side table for external replication.

#### 3. What is the defining characteristic of distributed systems, and what are three common examples?
**Answer:**
The fact that partial failures can occur is the defining characteristic of distributed systems.
Three examples:
1. Unbounded delay or loss when sending a packet over a network.
2. A node's clock may be significantly out of sync with other nodes despite NTP.
3. A process may pause arbitrarily (e.g., due to stop-the-world GC) and be falsely declared dead.

#### 4. What techniques can be used to handle events with causal dependencies when total order broadcast is not feasible?
**Answer:**
1. Using logical timestamps (e.g., Lamport timestamps or vector clocks) to track causality.
2. Logging an explicit snapshot of the system state observed by a user prior to an action, assigning it a unique ID that subsequent dependent events reference.
3. Applying deterministic conflict resolution algorithms (though not recommended if actions trigger external side effects).

#### 5. Why are Lamport timestamps insufficient for solving uniqueness constraints (e.g., username availability), and what mechanism is required instead?
**Answer:**
Lamport timestamps define a total order only *after* all operations are collected. When a node receives a create request, it cannot know if a concurrent request with a lower timestamp is inflight from another node without blocking the entire system. 
Solution: Total order broadcast.


## 📂 Category: Distributed Data Architecture (2 cards)

### 🟢 Junior Level

#### 1. What is a system of record?
**Answer:**
The authoritative source of truth where new, typically normalized data is initially written.


### 🔴 Senior Level

#### 1. How can you ensure read-your-own-writes consistency in event sourcing or Change Data Capture (CDC)?
**Answer:**
By performing updates to the read view synchronously with appending to the event log. This requires a transaction, meaning you must keep the event log and read view in the same storage system or use a distributed transaction.


## 📂 Category: Distributed Data Integration (2 cards)

### 🟡 Mid Level

#### 1. What is a federated database (also known as a polystore), and what problem does it solve?
**Answer:**
A federated database (polystore) provides a unified query interface across a wide variety of underlying storage engines and processing methods. Applications can either access the underlying storage engines directly or combine data from disparate places through the unified interface, mirroring the relational model's abstraction of a high-level query language over complex physical implementations.


### 🔴 Senior Level

#### 1. What is the better architectural solution to keep writes across several heterogeneous storage systems in sync compared to distributed transactions?
**Answer:**
Distributed transactions across heterogeneous systems are generally brittle and scale poorly. A more robust and practical solution is using an asynchronous event log combined with idempotent consumer writes.


## 📂 Category: Distributed Data Models (1 cards)

### 🔴 Senior Level

#### 1. What is the difference between eventual consistency and perpetual inconsistency regarding timeliness and integrity?
**Answer:**
Violations of timeliness are 'eventual consistency' (data converges across replicas given time). Violations of integrity are 'perpetual inconsistency' (permanent data corruption, phantom reads, or lost updates that never reconcile correctly).


## 📂 Category: Distributed Dataflow / Batch Processing (1 cards)

### 🔴 Senior Level

#### 1. Post-MapReduce dataflow engines try to avoid what operation unless it is strictly required, while maintaining a broadly similar approach to partitioning?
**Answer:**
Sorting


## 📂 Category: Distributed Messaging (4 cards)

### 🟢 Junior Level

#### 1. How do 'fan-out' and 'load balancing' differ as messaging patterns in message queues?
**Answer:**
Fan-out delivers each published message to all subscribed consumers. Load balancing distributes each message to only one consumer within a worker pool, allowing consumers to share the processing workload for expensive tasks.

#### 2. How is a log used to implement a log-based message broker?
**Answer:**
Producers send messages by appending them to the end of the log, and consumers read the log sequentially. If a consumer reaches the end, it waits for new notifications (similar to 'tail -f').


### 🟡 Mid Level

#### 1. How are messages ordered within a log-based message broker?
**Answer:**
The broker assigns a monotonically increasing sequence number (offset) to every message within a partition, making messages within a single partition totally ordered (though not across partitions).

#### 2. What is a key architectural difference between Remote Procedure Calls (RPC) and message brokers?
**Answer:**
Message-passing communication is typically asynchronous and one-way: the sender publishes a message to a broker and forgets about it without waiting for an immediate response. RPCs are generally synchronous and expect an immediate return value over a direct channel.


## 📂 Category: Distributed Messaging & Logs (2 cards)

### 🟢 Junior Level

#### 1. How can you scale throughput of a log-based message broker?
**Answer:**
The log can be partitioned, and different partitions can be hosted on different machines.


### 🟡 Mid Level

#### 1. How do consumer offsets in a log-based messaging system improve throughput?
**Answer:**
The broker does not need to track acknowledgements for every individual message because consumer offsets track which messages have been processed.


## 📂 Category: Distributed Processing (2 cards)

### 🟡 Mid Level

#### 1. Why are task-level retries necessary for MapReduce jobs running in shared resource environments like Google?
**Answer:**
Because MapReduce tasks can be preempted to free up resources for higher-priority jobs, task-level retries ensure job completion while maximizing overall resource utilization.


### 🔴 Senior Level

#### 1. How does handling a skewed join in map-reduce/Pig mitigate hot keys?
**Answer:**
After running a sampling job to detect key skew, records associated with a hot key are sent from the mapper to one of several reducers at random (or distributed across multiple reducers), and the results are later combined.


## 📂 Category: Distributed Processing & Joins (1 cards)

### 🔴 Senior Level

#### 1. What is required to perform a partitioned hash join in distributed data processing?
**Answer:**
Both datasets/inputs must be partitioned using the same hashing function on the join keys, ensuring that all records that share the same join key land on the exact same physical partition.


## 📂 Category: Distributed Processing / Batch Processing (2 cards)

### 🟢 Junior Level

#### 1. What is data skew (hot spots) in MapReduce-style batch processing?
**Answer:**
Collecting all data related to a hot key in a single reducer leads to significant skew (hot spots), causing that specific reducer to process significantly more records than others and becoming a bottleneck.


### 🔴 Senior Level

#### 1. What is a broadcast hash join in distributed data processing?
**Answer:**
One of the two join inputs is small enough to be entirely loaded into a hash table and is not partitioned. Mappers are started for each partition of the large join input, the hash table for the small input is loaded into each mapper, and the large input is scanned one record at a time, querying the hash table for each record.


## 📂 Category: Distributed Query Processing (1 cards)

### 🟡 Mid Level

#### 1. How do Massively Parallel Processing (MPP) databases typically handle a node crash mid-query execution?
**Answer:**
The MPP database retries the entire query execution from scratch. This is acceptable because analytical MPP queries typically take only seconds or minutes.


## 📂 Category: Distributed Replication (1 cards)

### 🟢 Junior Level

#### 1. What are the 4 main reasons to replicate data across multiple machines?
**Answer:**
1. High availability: Keeping the system running even when nodes or entire datacenters fail.
2. Disconnected operation: Allowing applications to function during network interruptions.
3. Latency: Placing data geographically closer to users for faster interactions.
4. Scalability: Handling higher read volumes by distributing reads across replicas.

Replication introduces complexity due to concurrency, node unavailability, network partitions, and edge cases like silent data corruption.


## 📂 Category: Distributed Storage (3 cards)

### 🟢 Junior Level

#### 1. What distributed file system does Hadoop use?
**Answer:**
HDFS (Hadoop Distributed File System)

#### 2. What is the role of the HDFS daemon process running on each storage node?
**Answer:**
It exposes a network service that allows other nodes in the cluster to read and write files stored on that specific machine.

#### 3. What is the role of the NameNode in HDFS?
**Answer:**
It is a central master server that tracks filesystem metadata, specifically which file blocks are stored on which data nodes.


## 📂 Category: Distributed Streaming (1 cards)

### 🟡 Mid Level

#### 1. How do log-based message brokers achieve load balancing across consumers in a consumer group?
**Answer:**
By assigning entire partitions to nodes in the consumer group, where each client consumes all messages in its assigned partitions sequentially in a single thread.


## 📂 Category: Distributed Systems (48 cards)

### 🟢 Junior Level

#### 1. Besides returning a result, throwing an exception, or hanging indefinitely (infinite loop/crash), what is the additional possible outcome of a network request compared to a local function call?
**Answer:**
A network request may return without a result due to a timeout, meaning you cannot know whether the request reached the remote service or if it was processed.

#### 2. How does HDFS conceptually utilize network storage across machines?
**Answer:**
It acts as one big filesystem that uses the disk space of every machine in the network.

#### 3. T/F: A system can only be as reliable as its least reliable component (its weakest link). Provide architectural examples in distributed systems.
**Answer:**
False. You can build reliable systems from unreliable components. Examples: 1) Error-correcting codes over lossy physical channels, and 2) TCP (reliable transport) built on top of IP (unreliable packet delivery).

#### 4. What architectural principle is HDFS based on, eliminating the need for special hardware?
**Answer:**
Shared-nothing principle.

#### 5. What does a time-of-day clock return?
**Answer:**
A time-of-day clock returns wall-clock time (actual date and time according to UTC), which can be synchronized via NTP and is susceptible to sudden clock jumps (forward or backward).

#### 6. What is a quorum in distributed systems, and why is it used?
**Answer:**
A quorum is a voting mechanism among nodes where decisions require a minimum number of votes from several nodes to reduce dependence and failure vulnerability on any single node.

#### 7. What is a stream in the context of an RPC call?
**Answer:**
A communication pattern where a call consists of a series of requests and responses flowing over time rather than a single request-response pair.


### 🟡 Mid Level

#### 1. A network interruption forces a choice between linearizability and availability. What theorem does this describe?
**Answer:**
The CAP theorem (specifically, under a partition (P), you must choose between consistency/linearizability (C) and availability (A)).

#### 2. According to the CAP theorem, what trade-off does a network interruption force a distributed system to make?
**Answer:**
A network interruption (partition) forces a choice between linearizability (consistency) and availability.

#### 3. Can two operations be concurrent in computer systems even if physical time (speed of light) would have allowed one to affect the other?
**Answer:**
True. Operations are concurrent if they are mutually unaware of each other, regardless of physical overlap. Network delays, interruptions, or slow links can prevent an operation from knowing about a prior event, making them concurrent.

#### 4. How can an operation be made safe against retries in a distributed system?
**Answer:**
By making the operation idempotent, often achieved by tracking and suppressing duplicate requests using a unique request ID/token.

#### 5. How can distributed systems automatically adjust timeouts to handle variable network conditions?
**Answer:**
Systems can continuously measure response times and network variability (jitter) to dynamically calculate and adjust timeout thresholds.

#### 6. How can on-device state in client-server architectures be modeled?
**Answer:**
On-device state can be thought of as a cached replica of the state managed on the server, requiring synchronization and conflict resolution strategies.

#### 7. How do you definitively know a request was successful in the presence of network uncertainty, and what must you assume if no response arrives?
**Answer:**
You need a positive response from the application itself. If no response arrives, you must assume failure and use a timeout.

#### 8. How does a node know that it is the leader in a single-leader per partition database?
**Answer:**
It obtains a lease from the other nodes—which is a lock with a timeout where only one node can hold it at a time—and must periodically renew the lease before it expires.

#### 9. How is concurrency defined between two operations?
**Answer:**
Two operations are concurrent if neither happens before the other (i.e., neither operation has knowledge of or dependency on the other).

#### 10. Network partitions are inevitable, so CAP theorem states a system can choose either Consistency or Availability when Partitioned (PACELC refines this: else Consistency/Latency).
**Answer:**
CAP theorem highlights that in the presence of a network partition (P), a distributed system must choose between Consistency (C) and Availability (A).

#### 11. What is a hard real-time system?
**Answer:**
A software system that must respond within a strictly specified deadline, where missing the deadline constitutes total system failure.

#### 12. What is the core structural difference between logical clocks and physical clocks, and what primary problem does the former solve?
**Answer:**
Logical clocks use incrementing counters rather than quartz crystals to track the relative causal ordering of events (solving concurrent write detection), whereas physical clocks (time-of-day and monotonic) measure actual elapsed physical time.

#### 13. What is the fundamental trade-off when configuring network timeout thresholds in distributed systems?
**Answer:**
If the timeout is too long, the system waits a long time for a failed node to be declared dead. If the timeout is too short, the system risks prematurely declaring a node dead when it is only temporarily slowed down or experiencing a network spike.

#### 14. When should a monotonic clock be used instead of a time-of-day clock?
**Answer:**
A monotonic clock is suitable for measuring durations and elapsed time intervals (such as timeouts) because it is guaranteed never to jump backward or adjust due to NTP synchronization.

#### 15. Why are timestamps from time-of-day clocks considered a dangerous way to order events across distributed nodes?
**Answer:**
Time-of-day clocks are synchronized via NTP and can be forcibly reset, causing them to jump backwards in time and violate monotonicity.


### 🔴 Senior Level

#### 1. How can Last Write Wins (LWW) fail to correctly order concurrent operations in distributed data systems?
**Answer:**
LWW incorrectly loses Client B's operation if B's write is causally later than A's write, but B's write is assigned an earlier physical clock timestamp due to clock skew.

#### 2. How do highly variable network delays and timeouts impact consensus algorithms?
**Answer:**
In the case of highly variable network delays and because of the use of timeouts, frequent leader elections result in poor performance for consensus algorithms due to split votes and repeated timeout triggers.

#### 3. How does Google's Spanner Time API report time to handle clock uncertainty?
**Answer:**
It reports time as a time range of [earliest possible, latest possible], explicitly exposing clock uncertainty instead of returning a single point in time.

#### 4. How is a distributed lock usually implemented to handle client failures?
**Answer:**
A distributed lock is usually implemented as a lease, which includes an automatic expiry time in case the holding client crashes or becomes partitioned.

#### 5. How is the Bitcoin network Byzantine fault-tolerant?
**Answer:**
By allowing mutually untrusting participants to reach consensus on whether a transaction happened without relying on a trusted central authority, using cryptographic proof-of-work and economic incentives.

#### 6. In a distributed system where leaders are granted locks with leases, how can we solve a problem where a node "goes rogue" and continues using an expired lock?
**Answer:**
By using a "fencing token", which is a monotonically increasing number issued by the lock service that storage nodes can check to reject stale requests from expired leaders.

#### 7. Stronger consistency guarantees are easier to use correctly but may have worse performance or fault tolerance. Why do systems drop linearizability?
**Answer:**
The reason for dropping linearizability is primarily performance (latency), not fault tolerance. Attiya and Welch proved that linearizable reads and writes require response times proportional to network delay uncertainty, making them inherently slower in networks with variable delays.

#### 8. What are 6 classic distributed systems problems that are reducible to consensus?
**Answer:**
1. Linearizable compare-and-set registers, 2. Atomic transaction commit, 3. Total order broadcast, 4. Locks and leases, 5. Membership/coordination service, 6. Uniqueness constraint. What they have in common is that they are all straightforward if you only have a single node.

#### 9. What are Lamport timestamps, and how do they enforce total ordering consistent with causality?
**Answer:**
Lamport timestamps are pairs of (counter, node ID). Each node tracks the maximum counter it has seen, incrementing its own counter on requests. They provide a total ordering consistent with causality, where higher counter values (or higher node IDs on ties) take precedence, offering a more compact alternative to version vectors.

#### 10. What are the 3 common system models regarding timing assumptions and the 3 most common system models for node failures in distributed systems?
**Answer:**
Timing assumptions: 1. Synchronous model 2. Partially synchronous model 3. Asynchronous model. Node failures: 1. Crash-stop faults 2. Crash-recovery faults 3. Byzantine (arbitrary) faults.

#### 11. What are the equivalence relationships between a linearizable compare-and-set register, total order broadcast, and consensus?
**Answer:**
A linearizable compare-and-set (CAS) register and total order broadcast are mathematically equivalent to consensus.

#### 12. What consistency model is required to enforce a hard uniqueness constraint in a database?
**Answer:**
A hard uniqueness constraint requires linearizability because checking uniqueness across distributed nodes requires an up-to-date, single source of truth to prevent race conditions.

#### 13. What deeply ingrained database, framework, library, and protocol assumptions make it harder to extend the write path end-to-end between clients?
**Answer:**
Stateless clients and request/response interactions.

#### 14. What defines a hard real-time system and where is it typically used?
**Answer:**
A hard real-time system has a strict, specified deadline by which the software must respond. If the deadline is missed, it results in system failure. It is used in dangerous or physical environments, such as aircraft, medical devices, robots, and cars.

#### 15. What failure scenario occurs with an incorrectly implemented distributed lock where a client fails to respect lease expiration?
**Answer:**
Client 1 believes it still holds a valid lease even though it has expired (e.g., due to a long pause), and thus unsafely proceeds to write to and corrupt a file in shared storage.

#### 16. What fundamental behavioral rule of Linearizability governs read operations once a new value has been observed?
**Answer:**
After any single read has returned the new value, all subsequent reads (by the same or any other client) must also return the new value or an even newer one.

#### 17. What is a fencing token and what problem does it solve?
**Answer:**
A fencing token is a monotonically increasing number granted by a lock server. It prevents a node operating under a false belief of holding a lease or lock from disrupting the system, as the downstream storage service rejects writes with older tokens than one already processed.

#### 18. What is a sloppy quorum and hinted handoff, and what trade-off do they address?
**Answer:**
A sloppy quorum allows writes and reads to use available nodes outside the designated 'home' nodes when network partitions prevent reaching a standard quorum, prioritizing high write availability over strict consistency. Hinted handoff is the subsequent process of transferring those temporary writes back to their home nodes once normal connectivity returns.

#### 19. What safety technique uses monotonically increasing sequence numbers to prevent stale or delayed nodes from corrupting shared storage?
**Answer:**
Fencing tokens, which allow access to storage only when writes are presented in the order of strictly increasing token numbers.

#### 20. When is a system considered Byzantine fault-tolerant, and what are two common scenarios where this is relevant?
**Answer:**
A system is Byzantine fault-tolerant if it continues to operate correctly even if some nodes are malfunctioning and not obeying the protocol, or if malicious attackers are interfering with the network. Examples: 1. Aerospace environments where radiation can corrupt memory or CPU registers. 2. Peer-to-peer networks like Bitcoin/blockchains where untrusting parties must agree without a central authority.

#### 21. Which problem is generally harder in distributed data systems: federated read-only querying or keeping writes to several storage systems in sync?
**Answer:**
Keeping writes to several storage systems in sync is harder due to dual-write consistency issues and race conditions. Federated querying is more manageable as it only requires mapping one data model into another for reads.

#### 22. Why are variable network delays problematic across multiple machines?
**Answer:**
Variable delays make it extremely difficult to determine the absolute order of events or establish causal relationships without synchronization mechanisms like vector clocks or physical time with bounded drift.

#### 23. Why does enforcing a uniqueness constraint in a distributed setting require consensus?
**Answer:**
To ensure that two different nodes do not concurrently allocate the same unique value or insert conflicting records, requiring a globally agreed-upon linearizable check.

#### 24. Why have many distributed systems abandoned single-node transactions?
**Answer:**
Many distributed systems claim transactions are too expensive in terms of performance and availability, asserting that eventual consistency is inevitable for horizontal scalability (though this view is often overly simplistic).

#### 25. Why is it safer to write all changes to a single system of record and propagate them via Change Data Capture (CDC) rather than writing to multiple datastores concurrently?
**Answer:**
Concurrent dual-writes directly to multiple independent datastores frequently lead to race conditions, partial failures, and conflicting states due to network unreliability and out-of-order delivery.

#### 26. Why is there no 'correct' value for network timeouts in multi-tenant datacenters and public clouds, requiring them to be determined experimentally?
**Answer:**
Quality of service (throughput/timing guarantees) is currently not enabled in multi-tenant datacenters and public clouds, or across the internet. Ethernet and IP use packet switching rather than circuit switching, suffering from queueing and unbounded delays.


## 📂 Category: Distributed Systems & Clocks (3 cards)

### 🟡 Mid Level

#### 1. What are the two kinds of physical clocks on each machine, and how is each used?
**Answer:**
1. Time-of-day clock: Returns current date and time according to a calendar, synchronized via NTP, but may jump backwards due to re-sinks making it unsuitable for measuring durations.
2. Monotonic clock: Guaranteed to always move forward, used for measuring elapsed time/durations and timeouts. Cannot be compared across different machines, and NTP may adjust its frequency via slewing.

#### 2. What is a Lamport timestamp and how is it structured?
**Answer:**
A Lamport timestamp is a logical clock used to determine the partial ordering of events in a distributed system. Each node has a unique ID and keeps a counter of the operations it has processed. The Lamport timestamp is a tuple/pair of (counter, node ID).


### 🔴 Senior Level

#### 1. What are the primary flaws in relying on system clocks for distributed leader leases?
**Answer:**
- It relies on synchronized physical clocks: the expiry time on the lease is set by a different machine and compared to the local system clock.
- Even if using a monotonic clock, the code assumes negligible time passes between checking the time (System.currentTimeMillis()) and processing the request (process(request)).


## 📂 Category: Distributed Systems & Concurrency (1 cards)

### 🟡 Mid Level

#### 1. What are two examples of commutative atomic operations?
**Answer:**
- Incrementing a counter
- Adding an item to a set


## 📂 Category: Distributed Systems & Consensus (13 cards)

### 🟢 Junior Level

#### 1. Complete the sentence: Low-level features (like TCP duplicate suppression, Ethernet checksums, WiFi encryption) are useful, but they ________ provide desired end-to-end correctness features by themselves.
**Answer:**
cannot

#### 2. What core characteristics of distributed systems make them fundamentally hard to work with?
**Answer:**
The nondeterminism and the possibility of partial failures.

#### 3. What term describes the API exposed by a server across a network to clients?
**Answer:**
A service.


### 🟡 Mid Level

#### 1. What is the Actor Model, why does it avoid thread management issues, and what does each actor typically represent?
**Answer:**
The actor model is a programming model for concurrency within a single process. Each actor processes messages sequentially (one at a time), eliminating the need for explicit threads, locks, or mutexes. Each actor typically represents a single client or entity with isolated local state, communicating asynchronously via message passing.

#### 2. What is the basic idea of linearizability?
**Answer:**
To make a distributed system appear as if there is only a single copy of the data and all operations on it are atomic, shielding the application from the reality of underlying data replication.


### 🔴 Senior Level

#### 1. True or False: Even when w + r > n, database quorums guarantee that stale values will never be read.
**Answer:**
False. Edge cases where stale values can still be returned include: the use of sloppy quorums, concurrent writes requiring tie-breaking (like Last-Write-Wins with clock skew), a write happening concurrently with a read, a write succeeding on fewer than w replicas without rollback, or a node carrying a new value failing and being restored from a stale replica.

#### 2. True or False: Total order broadcast is a stronger guarantee than timestamp ordering.
**Answer:**
True. In total order broadcast, the message delivery order is fixed at delivery time; a node cannot retroactively insert a message into an earlier position once subsequent messages have been delivered. This forms the basis of a replicated log and provides monotonically increasing sequence numbers usable as fencing tokens (e.g., zxid in ZooKeeper).

#### 3. What are the primary operational costs and limitations associated with consensus algorithms?
**Answer:**
1. They require synchronous replication steps for node voting, risking failover data loss if misconfigured. 2. They require a strict majority (quorum) to operate, leaving minority partitions blocked. 3. They typically assume a fixed set of voting nodes, making dynamic membership changes complex. 4. They rely heavily on timeouts for failure detection, which can cause severe performance degradation during network jitter.

#### 4. What are three example scenarios where linearizability is an absolute requirement for correct system behavior?
**Answer:**
1. Locking and leader election (ensuring a single active leader and avoiding split-brain scenarios via coordination services like ZooKeeper or etcd).
2. Constraints and uniqueness guarantees (enforcing hard constraints like unique usernames or preventing bank account balances from going negative).
3. Cross-channel timing dependencies (preventing race conditions when multiple communication channels interact, such as a file storage update versus a message queue notification).

#### 5. What are three foundational database and distributed techniques that can be implemented using total order broadcast?
**Answer:**
1. State machine replication (database replication where every replica processes identical writes in the exact same order).
2. Serializable transactions (executing deterministic stored procedures in the exact same sequence across partitions/nodes).
3. Fencing tokens (generating monotonically increasing sequence numbers, such as ZooKeeper zxid, to fence off stale leaders).

#### 6. What are two examples of distributed systems that typically do not require global consensus?
**Answer:**
1. Leaderless replication systems
2. Multi-leader replication systems
These architectures handle write conflicts locally or via resolution mechanisms rather than demanding a globally synchronized consensus across all nodes before acknowledging a write.

#### 7. What is an alternative name for Total Order Broadcast?
**Answer:**
Total order broadcast is also known as atomic broadcast.

#### 8. What is the atomic commit problem, and how does it relate to consensus?
**Answer:**
The atomic commit problem is a specific instance of consensus where a distributed transaction may succeed on some nodes but fail on others. To maintain ACID atomicity across nodes, all nodes must reach consensus on the outcome: either all commit or all abort/roll back.


## 📂 Category: Distributed Systems & Consistency (1 cards)

### 🔴 Senior Level

#### 1. What does 'Timeliness' mean in the context of distributed data consistency requirements?
**Answer:**
Ensuring users observe the system in an up-to-date state. Reading a stale copy of data is a temporary inconsistency. While the CAP theorem uses 'consistency' to mean linearizability (strong timeliness), weaker timeliness guarantees include read-after-write consistency.


## 📂 Category: Distributed Systems & Coordination (1 cards)

### 🟡 Mid Level

#### 1. What does a membership service determine, and what is an example?
**Answer:**
A membership service determines which nodes are currently active and live members of a cluster.
Example: ZooKeeper (and similar coordination services)


## 📂 Category: Distributed Systems & Failure Detection (2 cards)

### 🔴 Senior Level

#### 1. Instead of using constant timeouts to detect failures, what dynamic approach can systems use, and what are some examples?
**Answer:**
Systems can continually measure response times and network variability (jitter) to automatically adjust timeouts using mechanisms like a Phi Accrual failure detector. Examples include Akka, Cassandra, and TCP retransmission timeouts.

#### 2. What are the trade-offs involved in choosing a timeout length for distributed failure detection, and what two major factors complicate this decision?
**Answer:**
Long timeouts cause slow failure detection and user delays; short timeouts risk false positives (declaring live nodes dead due to transient slowdowns). Complications include: 1) Unbounded network delays, and 2) 'Noisy neighbors' in shared/multi-tenant cloud environments.


## 📂 Category: Distributed Systems & Fault Tolerance (1 cards)

### 🟢 Junior Level

#### 1. What are two examples of systems that require automatically detecting faulty nodes?
**Answer:**
- A load balancer needs to know to stop sending requests to a dead node.
- If the leader fails in a single-leader replication database, a follower needs to be promoted to new leader.


## 📂 Category: Distributed Systems & Networking (2 cards)

### 🟢 Junior Level

#### 1. What is the primary cause of variability in packet delays on computer networks?
**Answer:**
Queueing (buffer bloat, network congestion, and router queue saturation).


### 🟡 Mid Level

#### 1. What characterizes a circuit-switched, synchronous network in terms of latency and queueing?
**Answer:**
A circuit-switched network establishes a dedicated fixed route with guaranteed bandwidth between callers (e.g., traditional fixed-line telephone networks). It is synchronous because data passes through routers without suffering from queueing delays (as transmission slots are pre-allocated), resulting in a bounded delay with a fixed maximum end-to-end latency.


## 📂 Category: Distributed Systems & Networks (2 cards)

### 🟢 Junior Level

#### 1. If you send a network request and do not receive a response, what are the three possible underlying faults?
**Answer:**
(a) The request was lost in transit
(b) The remote node is down/crashed
(c) The response was lost in transit

#### 2. When a network request receives no response, it is impossible to determine the exact cause. What is the standard mechanism used to handle this issue?
**Answer:**
A timeout.


## 📂 Category: Distributed Systems & Ordering (1 cards)

### 🟡 Mid Level

#### 1. What is the difference between a total order and a partial order?
**Answer:**
A total order allows any two elements to be compared directly to determine which is greater or smaller (e.g., integers). A partial order allows comparison only for certain elements while others are incomparable (e.g., mathematical sets where neither is a subset of the other).


## 📂 Category: Distributed Systems & Partitioning (1 cards)

### 🟡 Mid Level

#### 1. How do you identify hot spots or heavy keys in distributed data partitioning if you do not run a preliminary sampling job?
**Answer:**
Hot keys must often be specified explicitly by the application or algorithm configuration.


## 📂 Category: Distributed Systems & RPC (1 cards)

### 🟡 Mid Level

#### 1. What are 6 fundamental reasons why trying to make a remote network service look too much like a local object/function call (location transparency) is flawed?
**Answer:**
1. Unpredictability: Local calls are predictable; network requests are unpredictable due to common network problems and remote node degradation.
2. Timeouts: When a request times out, you cannot determine whether the request reached the remote service or if it was lost.
3. Idempotency requirement: Retrying a failed network request risks duplicate execution unless the protocol is explicitly idempotent.
4. Latency: Network requests are orders of magnitude slower than local function calls, with wildly variable latency.
5. Serialization overhead: Local calls pass memory pointers, whereas network parameters must be explicitly encoded into a sequence of bytes.
6. Type translation: Clients and services may use different programming languages and type systems, requiring complex translation logic.


## 📂 Category: Distributed Systems & Replication (3 cards)

### 🟡 Mid Level

#### 1. How do log-based architectures differ from synchronously-updated relational databases regarding failure containment?
**Answer:**
Unlike synchronously-updated systems, asynchrony in log-based architectures makes systems more robust: faults, lag, or failures in one downstream consumer or derived dataset are contained locally and do not block the primary write path.


### 🔴 Senior Level

#### 1. How do leaderless replication datastores handle consistency and write operations across nodes?
**Answer:**
They operate on a "best effort" basis: the database writes to as many replicas as possible (using quorum configurations like $W + R > N$), and if it encounters partial errors or node failures, it does not rollback previously successful writes, relying instead on read repair and anti-entropy background processes.

#### 2. Under what conditions can single-leader replication achieve linearizability?
**Answer:**
Single-leader replication can be linearizable as long as you make reads from the leader or synchronously-updated followers, and as long as you do not use snapshot isolation.


## 📂 Category: Distributed Systems / Consensus (1 cards)

### 🔴 Senior Level

#### 1. What foundational distributed primitive do consensus services like ZooKeeper implement?
**Answer:**
Total order broadcast (also known as atomic broadcast).


## 📂 Category: Distributed Systems / Consistency (2 cards)

### 🔴 Senior Level

#### 1. What is causal consistency and what order does it impose on events?
**Answer:**
Causality imposes an ordering on events where cause comes before effect (e.g., a message is sent before it is received, a question before an answer). A system is causally consistent if it preserves these chains of causally dependent operations across nodes.

#### 2. Why is phrasing the CAP theorem as 'Consistency, Availability, Partition tolerance: pick 2 out of 3' misleading, and how should it be stated instead?
**Answer:**
Network partitions are a type of fault that will occur regardless of choice. A better way of phrasing CAP is 'either Consistent or Available when Partitioned'. When the network works correctly, a system can provide both linearizability and total availability. During a network fault, a system must choose between linearizability or total availability.


## 📂 Category: Distributed Systems / Fault Tolerance (1 cards)

### 🟡 Mid Level

#### 1. How should network timeouts be chosen in distributed systems?
**Answer:**
Timeouts should be chosen experimentally by measuring network round-trip times and their variability over an extended period.


## 📂 Category: Distributed Systems Architecture (4 cards)

### 🟢 Junior Level

#### 1. What are the three primary reasons for distributing a database across multiple machines?
**Answer:**
1. Scalability: Spreading data volume, read throughput, and write load beyond the capacity of a single machine.
2. Fault tolerance / High availability: Providing redundancy so the system continues operating if individual machines, networks, or datacenters fail.
3. Latency: Placing regional replicas close to geographically distributed users to minimize round-trip network transit time.


### 🟡 Mid Level

#### 1. What is tail latency amplification and why is it problematic in distributed backend services?
**Answer:**
Tail latency amplification occurs when an end-user request requires multiple downstream backend calls. Because the request must wait for the slowest parallel call to finish, the probability of encountering a high latency (tail) request increases drastically as the number of dependencies grows.


### 🔴 Senior Level

#### 1. What are coordination-avoiding data systems?
**Answer:**
Data systems that provide strong data integrity (though typically falling short of strict linearizability) without requiring synchronous coordination across nodes. By avoiding coordination, they achieve significantly better performance and fault tolerance.

#### 2. What is an end-to-end write path in modern data-intensive applications?
**Answer:**
It is an architectural flow where state changes stream continuously from a user interaction on a device, through event logs, stream processors, and various derived data systems, all the way to the UI on another device.


## 📂 Category: Distributed Systems Foundations (6 cards)

### 🟢 Junior Level

#### 1. What is the core aphorism for building fault-tolerant mechanisms and accepting partial failures in distributed systems?
**Answer:**
"We need to build a reliable system from unreliable components."


### 🟡 Mid Level

#### 1. What is a partial failure in distributed systems, and why are they difficult to handle?
**Answer:**
A partial failure is when some parts of a system fail or break unpredictably while other parts continue working. They are difficult because they are nondeterministic: network actions and remote node states can intermittently succeed or fail without immediate clarity on the outcome.

#### 2. Why do datacenter networks and the internet rely on packet switching rather than circuit switching?
**Answer:**
They use packet switching because they are optimized for bursty traffic, allowing dynamic bandwidth allocation without tying up dedicated fixed-bandwidth channels like traditional telephone circuit switching.

#### 3. Why is optimizing the 99.99th percentile (slowest 1 in 10,000 requests) often deemed too expensive and of limited benefit?
**Answer:**
Reducing response times at extreme percentiles is exceedingly difficult because tail latencies are easily affected by random, uncontrollable background events (like garbage collection pauses, OS scheduling, or network jitter), and the business value of such optimization yields diminishing returns.


### 🔴 Senior Level

#### 1. How do Lamport timestamps ensure a total ordering across multiple nodes that is consistent with causality?
**Answer:**
As long as the maximum counter value is carried along with every operation message across nodes, every causal dependency results in an increased timestamp counter value, preserving causal consistency.

#### 2. How do system models relate to real-world faults?
**Answer:**
System models make theoretical assumptions about what faults can happen and what can never happen (e.g., synchronous vs. asynchronous networks, crash-stop vs. Byzantine faults). In reality, faults are a question of probabilities rather than absolute guarantees.


## 📂 Category: Distributed Systems Fundamentals (7 cards)

### 🟢 Junior Level

#### 1. What is an idempotent operation?
**Answer:**
An operation that can be performed multiple times with the exact same net effect as if it were performed only once.

#### 2. What is the difference between latency and response time, and what two main delays does response time include?
**Answer:**
Response time is what the client actually observes, including service time (actual processing time), network delays, and queueing delays. Latency is specifically the duration a request spends waiting in a queue to be handled, awaiting service (latent). While often used interchangeably, they are technically distinct.


### 🟡 Mid Level

#### 1. What characteristics make a dataset suitable for coordination services like ZooKeeper?
**Answer:**
ZooKeeper is designed to manage slow-changing configuration or coordination metadata (e.g., leader election mappings like 'the node running on 10.1.1.23 is the leader for partition 7') that changes on the order of minutes or hours rather than high-frequency transactional data workloads.

#### 2. What is a causal dependency between two events in a distributed system?
**Answer:**
A causal dependency occurs when one event chronologically and logically impacts another, meaning the first event must be known or processed before the second (e.g., unfriending someone and then posting on their wall).

#### 3. What is the exact formal scope and limitation of the CAP theorem regarding consistency models and system faults?
**Answer:**
The CAP theorem has a very narrow formal scope: it considers only one consistency model (linearizability/atomic consistency) and one specific fault type (network partitions, where nodes are alive but disconnected from each other). It does not account for network delays, node crashes, or other trade-offs. As a result, critics summarize its practical value for modern distributed systems design as limited.


### 🔴 Senior Level

#### 1. What are the trade-offs of dynamic resource partitioning (like dynamic bandwidth sharing or CPU time-sharing) versus static partitioning?
**Answer:**
Dynamic partitioning maximizes resource utilization of the underlying wire or CPU and lowers costs, but introduces the downside of queueing and variable delays. Static partitioning provides latency guarantees at the cost of reduced utilization and higher expense.

#### 2. What does the end-to-end argument state in system architecture?
**Answer:**
The end-to-end argument states that certain lower-level functions—such as duplicate suppression, security checks, or reliable data integrity verification—cannot be fully and reliably solved solely at the communication or intermediate system level (e.g., TCP, database transactions, or stream processors). They require an end-to-end implementation spanning all the way from the client to the database application layer.


## 📂 Category: Distributed Systems Networking (1 cards)

### 🟢 Junior Level

#### 1. What are common synonyms for TCP rate-limiting mechanisms designed to prevent network or receiver overload?
**Answer:**
Flow control, congestion avoidance, backpressure.


## 📂 Category: Distributed Transactions (16 cards)

### 🟢 Junior Level

#### 1. What is the two-phase commit (2PC) protocol analogous to, and what happens if a node aborts before the commit phase?
**Answer:**
2PC is analogous to a traditional wedding ceremony where the minister asks both parties 'I do' individually (the prepare phase) and only pronounces them married (commits) if both respond positively. If either party aborts or says 'no', the entire transaction is rolled back. Once committed, it cannot be retracted.


### 🟡 Mid Level

#### 1. What does a successful execution of a Two-Phase Commit (2PC) protocol show?
**Answer:**
A Two-phase commit (2PC) execution phase where multiple nodes reach a coordinated decision to commit or abort a distributed transaction under a coordinator.

#### 2. What two distinct requirements are often conflated under the term 'consistency' in database systems?
**Answer:**
1. Timeliness (e.g., read-after-write consistency, replication lag constraints)
2. Integrity (e.g., ACID consistency invariants, foreign key constraints, data validity)

#### 3. Why does Two-Phase Commit (2PC) amplify failures across a distributed system?
**Answer:**
Because all participants must respond and remain healthy during the protocol; if any single part of the system is broken or unreachable, the entire transaction fails.


### 🔴 Senior Level

#### 1. Can Two-Phase Commit guarantee that a transaction is executed exactly once?
**Answer:**
Even with Two-Phase Commit, we cannot be completely sure a transaction will only be executed once from the client's perspective (e.g., if a network timeout occurs and the end-user manually re-sends a POST request, idempotency mechanisms at the application layer are still required).

#### 2. Can a distributed system exhibit a nonlinearizable execution despite enforcing a strict quorum?
**Answer:**
Yes. Even with a strict quorum (e.g., $W + R > N$), network delays, clock drift, or timing anomalies in asynchronous networks can cause operational interleavings that violate linearizability (real-time ordering constraints).

#### 3. How can business applications handle situations where strict linearizability is violated for performance or availability, while maintaining data integrity?
**Answer:**
Applications can accept the violation in the short term and follow up with a compensating transaction (or apology) to reconcile the state asynchronously.

#### 4. What are the two critical 'points of no return' in Two-Phase Commit (2PC)?
**Answer:**
1. When a participant votes 'yes': It promises to definitely be able to commit later and surrenders its right to abort.
2. The commit point: The coordinator writes its final decision (commit or abort) to its transaction log on disk, making the decision irrevocable.

#### 5. What are the two types of distributed transactions?
**Answer:**
1. Database-internal distributed transactions: all participating nodes run the same database software.
2. Heterogeneous (XAT) distributed transactions: participants involve two or more different database technologies or systems.

#### 6. What constitutes the critical commit point in the Two-Phase Commit (2PC) protocol, and how does the coordinator handle crash recovery?
**Answer:**
The commit point of 2PC comes down to a regular single-node atomic commit on the coordinator when it writes its commit or abort decision to a transaction log on disk. If the coordinator crashes after sending prepare requests and gathering 'yes' votes, participants remain 'in-doubt' and must wait for recovery. Upon recovery, the coordinator reads its transaction log to resolve the state of all in-doubt transactions (aborting any without a explicit commit record) before dispatching final decisions.

#### 7. What critical failure vulnerability does Two-Phase Commit (2PC) exhibit if the coordinator crashes immediately after participants vote 'yes'?
**Answer:**
Participants (such as Database 1) are left blocked and uncertain, not knowing whether to commit or abort, holding locks indefinitely.

#### 8. What is linearizability, and why doesn't it prevent write skew on its own?
**Answer:**
Linearizability is a recency guarantee on reads and writes of a single individual object, making the system appear as if there is only one copy of data with atomic operations. Because it operates on individual objects rather than grouping operations into multi-object transactions, it does not prevent write skew without additional measures like materializing conflicts.

#### 9. What is the Two-Phase Commit (2PC) algorithm used for in distributed databases?
**Answer:**
Two-phase commit is an atomic commitment protocol (ACP) used to ensure that across multiple distributed nodes, either all nodes commit a transaction or all nodes abort it, guaranteeing cross-partition atomicity.

#### 10. What is the classic approach for keeping different data storage systems in sync, and why is it problematic?
**Answer:**
The classic approach is using distributed transactions via atomic commit protocols (like Two-Phase Locking / 2PC). It is problematic because it heavily reduces system availability, introduces high latency, and creates tight coupling across heterogeneous systems.

#### 11. What is the performance impact of distributed transactions implemented with Two-Phase Commit (2PC)?
**Answer:**
Distributed transactions, especially those implemented with 2PC, carry a heavy performance penalty due to coordination overhead, blocking behavior, and network round-trips.

#### 12. Why are atomic commits necessary in multi-node distributed systems?
**Answer:**
Atomic commits are required because allowing each node to commit independently can lead to partial failures (succeeding on some nodes and failing on others), which violates atomicity and leaves the distributed database in an inconsistent state.


## 📂 Category: Distributed Transactions & Clocks (1 cards)

### 🔴 Senior Level

#### 1. How can event ordering and snapshot isolation be maintained in a distributed system when clocks have uncertainty bounds (e.g., +/- 100 ms)?
**Answer:**
By explicitly exposing clock uncertainty bounds (confidence intervals representing earliest and latest possible times) and ensuring that confidence intervals do not overlap when establishing causal dependencies. For example, Google's TrueTime API in Spanner implements this by deliberately pausing a read-write transaction for the duration of the clock uncertainty interval before committing, guaranteeing that subsequent read timestamps fall strictly outside the confidence window.


## 📂 Category: Distributed Transactions & Consensus (8 cards)

### 🟢 Junior Level

#### 1. What are common examples of application features that require enforcing global uniqueness?
**Answer:**
A username or email address, and ensuring two people cannot book the same seat on a flight or in a theater.


### 🟡 Mid Level

#### 1. How can you achieve consensus to implement a uniqueness constraint in a distributed setting?
**Answer:**
By using single-leader replication.

#### 2. How can you scale the use of single-leader replication for enforcing a uniqueness constraint?
**Answer:**
Partition based on the value that needs to be unique: for example, by request ID routing to the same partition or a hash of the username.

#### 3. The term consistency is terribly overloaded. What are 4 different meanings, with examples?
**Answer:**
1. Replica consistency and the issue of eventual consistency that arises in asynchronously replicated systems (see 'Problems with Replication Lag').
2. Consistent hashing is an approach to partitioning that some systems use for rebalancing (see 'Consistent Hashing').
3. Consistency means linearizability wrt recency guarantees (eg: 'either consistent or available when partitioned').
4. In the context of ACID, consistency refers to an application-specific notion of the database being in a 'good state'.
It is unfortunate that the same word is used with at least four different meanings.

#### 4. What are the two phases in Two-Phase Commit (2PC)?
**Answer:**
Phase 1 (Prepare): The coordinator sends a prepare request to each participant node to track if they are ready to commit.
Phase 2 (Commit/Abort): The coordinator sends a commit request if all participants replied 'yes', or an abort request if any participant replied 'no'.


### 🔴 Senior Level

#### 1. How can we achieve an operation executed atomically across multiple partitions without an atomic commit?
**Answer:**
With partitioned logs. Exactly-once correctness is achieved by breaking down the multi-part transaction into two differently partitioned stages and using an end-to-end request ID.

#### 2. How do distributed transaction systems achieve exactly-once execution compared to log-based systems?
**Answer:**
Distributed transactions use atomic commits, whereas log-based systems rely on deterministic retries and idempotence.

#### 3. What does the FLP (Fischer, Lynch, and Paterson) result prove about consensus, and how do practical systems bypass it?
**Answer:**
The FLP result proves that deterministic consensus is impossible in an asynchronous system model even with a single unannounced process crash. Practical distributed systems bypass this impossibility by using randomized algorithms or failure detectors (such as timeouts and partial synchrony assumptions) to guarantee liveness.


## 📂 Category: Distributed Transactions & Consistency (1 cards)

### 🔴 Senior Level

#### 1. What is the fundamental difference between Serializability and Linearizability?
**Answer:**
Serializability is an isolation property of multi-object transactions ensuring they behave as if executed in some serial order. Linearizability is a recency guarantee and consistency model on reads and writes of a single register (individual object) without grouping into transactions.


## 📂 Category: Distributed Transactions & Partitioning (1 cards)

### 🔴 Senior Level

#### 1. How do partitioned databases typically maintain ordering, and what limitations does this impose across partitions?
**Answer:**
Partitioned databases with a single leader per partition typically maintain ordering only per partition. This means they cannot offer cross-partition consistency guarantees such as consistent snapshots or foreign key references across partitions without additional coordination (like total order broadcast).


## 📂 Category: Event Sourcing & Stream Processing (2 cards)

### 🟢 Junior Level

#### 1. In what decade was Complex Event Processing (CEP) invented?
**Answer:**
The 1990s.


### 🟡 Mid Level

#### 1. In an event-sourced system, how does a request transition from a command to an event and a fact?
**Answer:**
When a user request arrives, it is a 'command' that can still fail if it violates system constraints. Once validation succeeds, an 'immutable event' is generated, which then represents a historical 'fact'.


## 📂 Category: Event-Driven Architecture (2 cards)

### 🟡 Mid Level

#### 1. How does an explicit translation step from an event log to a database simplify application evolution?
**Answer:**
It allows you to use the event log to build and run a separate read-optimized view alongside the existing system. Running new and old systems side by side is much safer and easier than performing a complex in-place schema migration.

#### 2. How is event sourcing fundamentally different from change data capture (CDC)?
**Answer:**
Events are stored at a different abstraction layer: Event sourcing records domain-level business actions that happened at the application layer, whereas CDC captures low-level database-agnostic row changes (inserts, updates, deletes) from the storage engine level.


## 📂 Category: Foundations of Data Systems (2 cards)

### 🟢 Junior Level

#### 1. What are key tenets of the Unix Philosophy relevant to software and data systems design?
**Answer:**
- Design and build software to be tried early, ideally within weeks. Don't hesitate to throw away parts and rebuild them.
- Expect the output of one program to become the input to another program.
- Make each program do one thing well.
- Use tools to lighten a programming task.

#### 2. What are the three big ideas in designing data-intensive applications (the three 'abilities')?
**Answer:**
1. Reliability: Tolerating hardware/software faults and human error.
2. Scalability: Measuring load and performance via latency percentiles and throughput to remain performant under growth.
3. Maintainability: Operability, simplicity, and evolvability for engineering and operations teams.


## 📂 Category: Leader-Based Replication (3 cards)

### 🟡 Mid Level

#### 1. What is a semi-synchronous configuration in leader-based replication?
**Answer:**
A setup where exactly one follower is synchronous and the remaining followers are asynchronous. If the synchronous follower becomes slow or unavailable, one of the asynchronous followers is promoted to be synchronous. This guarantees that at least two nodes (the leader and one synchronous follower) possess an up-to-date copy of the data, balancing durability and availability.


### 🔴 Senior Level

#### 1. Regarding leader-based replication, what are 4 main difficulties and potential risks encountered when handling a failover?
**Answer:**
1. Unreplicated writes: If asynchronous replication is used, the new leader may not have received all writes from the old leader before failure. When the old leader rejoins, those writes are typically discarded, violating durability expectations.
2. External system coordination: Discarding writes can cause severe data inconsistencies with external systems (e.g., an out-of-date MySQL follower promoted to leader reusing auto-incrementing primary keys that were already synced to a Redis store).
3. Split brain: A scenario where two nodes both believe they are the leader and accept writes concurrently, leading to data loss or corruption unless fenced (e.g., via STONITH).
4. Timeout determination: Striking the right balance for the heartbeat/failure detection timeout—too long delays recovery; too short causes unnecessary, destabilizing failovers during temporary load spikes or network glitches.

#### 2. What is the 'split-brain' problem in leader-based replication, and what is a common mitigation strategy?
**Answer:**
Split-brain occurs when two nodes in a cluster both believe they are the active leader and accept writes independently, risking severe data corruption or loss. A common mitigation strategy is 'fencing' (also known as STONITH - 'Shoot The Other Node In The Head'), which ensures that a fenced node is safely shut down or isolated from the storage layer before a new leader takes over.


## 📂 Category: Messaging & Event Streaming (3 cards)

### 🟢 Junior Level

#### 1. What happens to a message in traditional message brokers after it is successfully delivered to its consumers?
**Answer:**
The message broker usually deletes the message from the queue or storage once successful delivery and acknowledgment occur.

#### 2. What is the publish/subscribe messaging model in distributed systems?
**Answer:**
It is a messaging pattern where multiple producer nodes send messages to a common channel or topic, and multiple consumer nodes subscribe to receive those messages asynchronously.


### 🟡 Mid Level

#### 1. If a message consumer drops its connection or times out, a message broker assumes failure and redelivers the message. What architectural pattern or protocol is required to handle cases where the message *was* successfully processed but the network dropped the acknowledgement?
**Answer:**
An atomic commit protocol or making message processing idempotent.


## 📂 Category: Messaging / Stream Processing (1 cards)

### 🟡 Mid Level

#### 1. What problem can occur when combining redelivery with load balancing in a message broker?
**Answer:**
Consumers may receive and process messages out of order.


## 📂 Category: Messaging Systems & Event Streaming (1 cards)

### 🟢 Junior Level

#### 1. What is an alternative way to implement a messaging system without a centralized broker? Provide an example.
**Answer:**
Direct messaging from producers to consumers without an intermediary broker. An example of this is webhooks, where an HTTP endpoint receives events directly.


## 📂 Category: Microservices & Architecture (1 cards)

### 🟡 Mid Level

#### 1. How do service APIs differ from database APIs regarding client querying, and what key design benefit does this restriction provide?
**Answer:**
Services expose an application-specific API that only allows inputs and outputs predetermined by business logic, unlike databases allowing arbitrary queries. This provides a degree of encapsulation and fine-grained access control.


## 📂 Category: Multi-Leader Replication (2 cards)

### 🟡 Mid Level

#### 1. In multi-leader replication, what is a 'replication topology', and what is the constraint on the topology when there are exactly two leaders?
**Answer:**
A replication topology describes the communication paths along which writes are propagated from one node to another. If there are exactly two leaders, there is only one plausible topology: leader 1 must send all its writes to leader 2, and vice versa (bidirectional replication). With more than two leaders, more complex topologies (such as circular, star, or all-to-all) become possible.


### 🔴 Senior Level

#### 1. What are 4 common approaches to achieving convergent conflict resolution in multi-leader replication configurations?
**Answer:**
1. Last Write Wins (LWW) / Timestamp-based: Attach a unique ID or timestamp to each write and pick the highest, discarding others (prone to data loss).
2. Replica ID precedence: Assign unique IDs to replicas and let writes originating from higher-numbered replicas take precedence.
3. Value merging: Programmatically merge conflicting values together (e.g., ordering strings alphabetically and concatenating them like 'B/C').
4. Explicit conflict recording: Store the conflicting states in a dedicated data structure and defer resolution to application code or user prompt.


## 📂 Category: Observability & Performance (1 cards)

### 🟡 Mid Level

#### 1. Why are percentiles better than averages when measuring system load and response times?
**Answer:**
Percentiles help track tail latencies (e.g., p99, p99.9), which directly affect power users and high-value customers who interact with the system the most. Averages mask outliers, whereas percentiles reveal performance degradation for heavy users.


## 📂 Category: Operating Systems (1 cards)

### 🟢 Junior Level

#### 1. What is the uniform interface used across Unix systems?
**Answer:**
A file (represented as a file descriptor).


## 📂 Category: Partitioning (5 cards)

### 🟢 Junior Level

#### 1. What is the primary downside of key-range partitioning, and what is a classic example that demonstrates it?
**Answer:**
The primary downside is that certain access patterns can create severe hot spots. For example, if the partition key is a timestamp (e.g., one partition per day for sensor measurements), all current writes will continuously target today's single partition while all other historical partitions sit completely idle.

#### 2. What terms describe a condition where partitioning is unfair, resulting in disproportionate load on certain partitions, and what is the heavily loaded partition called?
**Answer:**
The partitioning is 'skewed' (data or query skew), and a partition with disproportionately high load is called a 'hot spot'.


### 🔴 Senior Level

#### 1. How do partition count and partition size relate to dataset size and node count across dynamic, fixed, and proportional partitioning schemes?
**Answer:**
With dynamic partitioning, the number of partitions is proportional to the dataset size. With fixed partitioning, the size of each partition is proportional to the dataset size. In both cases, partition count is independent of node count. With proportional node partitioning, the number of partitions is proportional to the number of nodes (maintaining a fixed number of partitions per node).

#### 2. What is consistent hashing (hash partitioning) used for, and why is the term potentially confusing?
**Answer:**
Consistent hashing is a way of evenly distributing load across an internet-wide system of caches (like a CDN) using randomly chosen partition boundaries without central control. The term is confusing because 'consistent' has nothing to do with replica consistency or ACID consistency; thus, it is often better called hash partitioning. It is rarely used effectively for databases due to rebalancing complexities.

#### 3. Which partition rebalancing strategy requires consistent hashing (random partition boundaries)?
**Answer:**
Partitioning proportionally to nodes (e.g., a fixed number of partitions per node, as used in Cassandra and Ketama), where a new node splits a subset of existing partitions randomly.


## 📂 Category: Partitioning & Indexing (1 cards)

### 🔴 Senior Level

#### 1. What are the pros and cons of using a term-partitioned (global) secondary index versus a document-partitioned secondary index?
**Answer:**
Pro (Term-partitioned): Reads are much more efficient because a client only queries the specific partition holding the target term, avoiding scatter/gather queries across all partitions.
Con (Term-partitioned): Writes are slower and more complex. A single document write can modify terms located across multiple partitions on different nodes, often requiring asynchronous updates or distributed transactions.


## 📂 Category: Partitioning & Rebalancing (3 cards)

### 🟡 Mid Level

#### 1. What are the 3 minimum requirements expected of a database rebalancing process?
**Answer:**
1. Fair load distribution: After rebalancing, data storage, read throughput, and write throughput should be shared fairly among the nodes in the cluster.
2. Continuous availability: The database must continue accepting incoming reads and writes while rebalancing is actively taking place.
3. Minimal data movement: No more data than strictly necessary should be transferred between nodes to ensure fast rebalancing and minimize network/disk I/O overhead.


### 🔴 Senior Level

#### 1. What are the three primary strategies for assigning partitions to nodes during database rebalancing, and what is the fundamental flaw of the simple hash-mod-N approach?
**Answer:**
The three strategies are: (1) Fixed number of partitions (pre-splitting many more partitions than nodes and shifting partition assignments), (2) Dynamic partitioning (splitting and merging partitions dynamically based on size thresholds, similar to B-trees), and (3) Partitioning proportionally to nodes (maintaining a fixed number of partitions per node, splitting random partitions when a node joins). 

The flaw with the hash-mod-N approach is excessive data movement: whenever the node count N changes, nearly all keys hash to a different node, making cluster resizing computationally and network-prohibitive.

#### 2. What constitutes a skewed workload in a partitioned data system, what is a classic example, and how can applications compensate for it?
**Answer:**
A skewed workload occurs when read or write requests concentrate heavily on a single key, routing all traffic to one partition and creating a performance hot spot. A classic example is a celebrity user on a social media platform receiving millions of writes/reads on their user ID. Because data systems rarely handle this automatically, applications compensate by adding a random prefix or suffix (e.g., a two-digit random number) to hot keys to distribute writes across multiple partitions, subsequently combining results across those derived keys during reads.


## 📂 Category: Partitioning & Routing (1 cards)

### 🔴 Senior Level

#### 1. What are 3 high-level service discovery approaches for partition routing, and what key problem is shared across all of them?
**Answer:**
The 3 approaches are: (1) Clients contact any random node via a round-robin load balancer, which forwards the request to the correct node if it doesn't own the partition; (2) Clients send requests through a dedicated partition-aware routing tier (load balancer); (3) Clients are fully partition-aware and connect directly to the correct node.

The shared key problem across all approaches is ensuring that the component making the routing decision stays accurately synchronized with cluster metadata changes regarding partition-to-node assignments.


## 📂 Category: Partitioning & Sharding (4 cards)

### 🟡 Mid Level

#### 1. What is data skew and what is a hot spot in the context of database partitioning?
**Answer:**
Skew occurs when partitioning is unfair, resulting in some partitions holding disproportionately more data or request load than others. A hot spot is the specific partition experiencing that excessively high load, creating a system bottleneck.


### 🔴 Senior Level

#### 1. What are 2 major operational downsides of fully automated partition rebalancing?
**Answer:**
1. Unpredictability: Rebalancing is computationally and network-intensive, potentially overloading the cluster and severely degrading user request performance.
2. Cascading failures: Slow nodes might be falsely flagged as dead, triggering automated rebalancing that dumps extra load onto an already struggling node.

#### 2. What are the two primary methods for partitioning secondary indexes in a distributed database?
**Answer:**
1. Document-partitioned indexes (local indexes): Secondary indexes are stored in the same partition as the primary key and value. Writes only update a single partition, but reads require a scatter/gather query across all partitions.
2. Term-partitioned indexes (global indexes): Secondary indexes are partitioned separately based on the indexed values. Writes may update multiple secondary index partitions, but reads can be served efficiently from a single partition.

#### 3. What strategy is used for querying document-partitioned secondary indexes, what is its main drawback, and how can it be mitigated?
**Answer:**
Strategy: Scatter/gather (sending the query to all partitions concurrently and merging the results).
Drawback: Highly expensive read operations prone to tail latency amplification.
Mitigation: Structuring the partitioning scheme so secondary index queries fall within a single partition, though this is difficult when filtering across multiple secondary attributes simultaneously.


## 📂 Category: Performance & Metrics (1 cards)

### 🟡 Mid Level

#### 1. Why do high latency percentiles (e.g., p99) matter significantly in backend services, and what is tail latency amplification?
**Answer:**
Tail latency amplification occurs because a single end-user request often triggers multiple parallel backend calls; the end-user request must wait for the slowest call to complete. As the number of backend dependencies increases, the probability that an end-user experiences a slow request scales up dramatically.


## 📂 Category: Relational Databases (1 cards)

### 🟢 Junior Level

#### 1. What is a virtual view?
**Answer:**
A virtual view is a stored query shortcut (a named virtual table) that computes its results dynamically by running the underlying query whenever it is accessed.


## 📂 Category: Reliability & Fault Tolerance (2 cards)

### 🟢 Junior Level

#### 1. What is the difference between a fault and a failure, and what are the three high-level categories of faults?
**Answer:**
A fault is a component deviating from its spec, whereas a failure is the system as a whole failing to provide service. The three categories are: 1) Hardware faults (mitigated by redundancy and rolling upgrades), 2) Software errors (mitigated by process isolation, testing, and monitoring), and 3) Human errors (mitigated by good API design, sandboxes, and easy recovery).


### 🟡 Mid Level

#### 1. Why is it beneficial to deliberately induce faults in fault-tolerant systems (e.g., Netflix Chaos Monkey), and what is a notable exception where prevention is preferred?
**Answer:**
Deliberately inducing faults ensures that error-handling and fault-tolerance machinery are continually exercised, increasing confidence that the system will handle natural failures correctly. Prevention is preferred over cure when no cure exists, such as in security breaches where compromised sensitive data cannot be undone.


## 📂 Category: Replication (11 cards)

### 🟢 Junior Level

#### 1. What are the advantages and disadvantages of synchronous replication?
**Answer:**
Advantage: The follower is guaranteed to have an up-to-date, consistent copy of the data matching the leader, preventing data loss if the leader fails. Disadvantage: If the synchronous follower fails or lags, writes cannot proceed, and the leader must block all incoming write requests until the replica recovers.

#### 2. What are the three main approaches to leader/follower replication, and why is single-leader replication the most popular?
**Answer:**
1. Single-leader replication
2. Multi-leader replication
3. Leaderless replication
Single-leader replication is popular because it is fairly easy to understand and there is no conflict resolution to worry about.

#### 3. What does eventual consistency mean in the context of replicated databases?
**Answer:**
If no new updates are made, eventually all replicas will converge and return the same value.


### 🟡 Mid Level

#### 1. Is leader-based replication restricted solely to databases? Provide examples.
**Answer:**
False. Leader-based replication is used in relational databases (PostgreSQL, MySQL), non-relational databases (MongoDB), and distributed message brokers (Kafka, RabbitMQ high-availability queues), as well as network filesystems.

#### 2. What is a read-scaling architecture and why isn't synchronous replication reliable for it?
**Answer:**
A read-scaling architecture routes read requests across many followers to reduce leader load. Synchronous replication is unreliable here because a single node or network failure would block all writes; more nodes increase the probability that one is down, leading to tail latency amplification and unavailability.

#### 3. What is the main disadvantage of Write-Ahead Log (WAL) shipping replication, and what is the standard solution?
**Answer:**
WAL shipping is too low-level because it describes exact byte changes in disk blocks, tightly coupling replication to the storage engine internals. This prevents running different software or storage engine versions between leaders and followers, making zero-downtime upgrades difficult. The solution is to use logical (row-based) replication, which decouples the replication log from storage engine internals and maintains backward compatibility.

#### 4. What is the primary downside and main advantage of multi-leader replication?
**Answer:**
Advantage: Allows each datacenter/replica to accept writes independently without waiting for cross-network roundtrips. Downside: Concurrent modifications to the same data lead to write conflicts that require complex resolution strategies (e.g., conflict detection, convergence logic), making it a hazardous configuration prone to issues with auto-incrementing keys and constraints.

#### 5. Why doesn't it make sense to make multi-leader replication synchronous?
**Answer:**
Making multi-leader replication synchronous would destroy its core advantage: allowing each replica to accept writes independently without waiting on remote nodes. If synchronous conflict detection is required, single-leader replication should be used instead.

#### 6. Why is the term 'eventual consistency' deliberately vague in distributed data systems?
**Answer:**
The term 'eventually' specifies no time limit on how far a replica can fall behind. While normal replication lag is a fraction of a second, network partitions or system overload can stretch the lag to seconds, minutes, or longer.


### 🔴 Senior Level

#### 1. How does monitoring for replication staleness differ between leader-based and leaderless replication?
**Answer:**
In leader-based replication, metrics are derived by subtracting a follower's log position from the leader's log position. In leaderless replication, writes have no fixed order and no single log, making staleness harder to quantify without advanced research parameters (like n, w, r), though tracking is critical to quantify eventual consistency.

#### 2. What replication lag anomaly do consistent prefix reads prevent, and how do they work?
**Answer:**
Consistent prefix reads prevent violations of causality (e.g., hearing an answer before the question). The guarantee states that if a sequence of writes happens in a specific order, any reader will see them appear in that same order. In partitioned databases or systems with asynchronous followers, this is ensured by routing causally related writes to the same partition or explicitly tracking causal dependencies.


## 📂 Category: Replication & CDC (1 cards)

### 🟡 Mid Level

#### 1. What is Change Data Capture (CDC), and what type of replication logging technique does it typically rely on?
**Answer:**
CDC is the process of observing all data modifications and streaming them to external systems (e.g., data warehouses, search indexes, caches). It typically utilizes logical (row-based) replication logs, which are decoupled from storage engine internals to maintain backward compatibility across software versions.


## 📂 Category: Replication & Conflict Resolution (1 cards)

### 🟡 Mid Level

#### 1. When merging concurrently written values (siblings) in a shared database, what special marker is used to indicate a deletion?
**Answer:**
A tombstone.


## 📂 Category: Replication & Consensus (4 cards)

### 🟢 Junior Level

#### 1. How do leaders propagate data changes to followers in leader-based replication?
**Answer:**
Whenever the leader writes new data locally, it streams the change as part of a replication log or change stream to all followers, which apply the writes in the exact same order.


### 🔴 Senior Level

#### 1. How do leaderless replication configurations prevent returning stale values on reads, and what two mechanisms allow a recovered node to catch up on missed writes?
**Answer:**
Read requests are sent to multiple replicas in parallel, and version numbers are used to determine and return the newest value. The two mechanisms for a recovered node to catch up are: 1) Read repair (clients write newer values back to nodes responding with stale data) and 2) Anti-entropy processes (background sync processes between replicas).

#### 2. What are the three primary strategies for handling single-leader node failure or unreachability in systems requiring high availability?
**Answer:**
1. Wait for the leader to recover (accepting downtime/blocking).
2. Manually fail over using human intervention to choose a new leader and reconfigure the system.
3. Use an automated consensus algorithm (e.g., Raft, Paxos) to elect a new leader.

#### 3. What essential algebraic property must atomic operations possess to work effectively in a multi-leader or leaderless replicated context?
**Answer:**
They must be commutative, meaning operations can be applied in any order on different replicas and still yield the same final state.


## 📂 Category: Replication & Consistency (2 cards)

### 🔴 Senior Level

#### 1. What are the three consistency models used to help determine how an application should behave under replication lag?
**Answer:**
1. Read-after-write consistency: Users always see data that they submitted themselves.
2. Monotonic reads: After seeing data at one point in time, users will not subsequently see older data from an earlier point in time.
3. Consistent prefix reads: Users see data in a causally valid state (e.g., seeing a question and its reply in the correct chronological order).

#### 2. What are three primary trade-offs and benefits of choosing multi-leader replication over single-leader replication in multi-datacenter deployments?
**Answer:**
1. Performance: Writes are processed locally in each datacenter and replicated asynchronously, hiding high inter-datacenter network latencies from users.
2. Tolerance of datacenter outages: Individual datacenters can continue operating independently if network links fail or another datacenter goes down.
3. Tolerance of network problems: Asynchronous multi-leader setups can withstand temporary public internet or inter-datacenter communication interruptions without halting local writes.


## 📂 Category: Replication & Consistency Models (2 cards)

### 🔴 Senior Level

#### 1. What are two major complications that make implementing read-your-writes consistency harder in modern distributed architectures?
**Answer:**
1) Replicas distributed across multiple datacenters (requiring cross-datacenter routing to the leader). 2) Users accessing the service from multiple devices (such as a desktop and a mobile app), where metadata regarding the last write must be centralized across devices.

#### 2. What is read-your-writes consistency (read-after-write consistency) and what are three common ways to implement it in leader-based replication?
**Answer:**
Read-your-writes consistency guarantees that a user will always see any updates they personally submitted when reloading or querying. Implementation techniques include: 1) Reading from the leader if the user modified the data; 2) Reading from the leader for a short window (e.g., 1 minute) after any update while tracking the last update time; 3) Having the client remember the timestamp of its most recent write and ensuring the replica serving the read has caught up to at least that timestamp.


## 📂 Category: Replication & Distributed Data (2 cards)

### 🟡 Mid Level

#### 1. What are three fundamental limitations of a single-leader replication system?
**Answer:**
1. Inability to scale writes or partition write traffic when a single leader node becomes a bottleneck.
2. Inability to natively handle multi-datacenter deployments where each facility requires local low-latency write capabilities.
3. Architectural constraints in microservices where state and storage cannot rely on a single global durable state bottleneck.


### 🔴 Senior Level

#### 1. What are three replication topologies for multi-leader setups, what is the most general one, and what are the primary failure modes of each?
**Answer:**
Topologies: Circular, Star, and All-to-All.
- Most General: All-to-all topology.
- Circular & Star Failure Mode: If a single node fails, it completely interrupts the replication message flow between other connected nodes.
- All-to-All Failure Mode: Network congestion or variable link speeds can cause replication messages to overtake each other, creating causal ordering violations that require version vectors to resolve.


## 📂 Category: Replication & Quorums (1 cards)

### 🟡 Mid Level

#### 1. What 3 parameters establish a quorum, what mathematical condition must always hold, and what does it guarantee?
**Answer:**
Parameters: n (total replicas), w (write quorum size), r (read quorum size). 
Condition: w + r > n.
Guarantee: At least one overlapping node between the read and write sets ensures you will read the most up-to-date value.


## 📂 Category: Scalability & Load Parameters (1 cards)

### 🟡 Mid Level

#### 1. How often should an architecture be rethought as load increases, and what is the rule regarding a 'one-size-fits-all' scalable architecture?
**Answer:**
For fast-growing services, you typically need to rethink your architecture on every order of magnitude increase in load (or even more often), as an architecture suited for one load level rarely copes well with 10x that load. The guiding aphorism is that 'there is no such thing as a generic, one-size-fits-all scalable architecture' (informally known as magic scaling sauce); scalable architectures are highly specific to an application's specific access patterns, read/write ratios, and data volume constraints.


## 📂 Category: Storage Engines (76 cards)

### 🟢 Junior Level

#### 1. How are materialized views typically updated within a database?
**Answer:**
Materialized views are updated automatically by the underlying database engine upon writes to the base tables.

#### 2. How do sequential writes compare to random writes in terms of performance?
**Answer:**
Sequential writes are significantly faster than random writes, particularly on HDDs and SSDs, because sequential I/O minimizes head movement and avoids expensive disk seek operations or random page write amplification.

#### 3. How does ACID Durability work in single-node versus replicated databases?
**Answer:**
In a single-node database, durability is achieved by writing data and transaction metadata to disk (such as a write-ahead log). In a replicated database, durability requires that data is successfully persisted to more than a quorum threshold of nodes.

#### 4. How does a hash index store keys and values?
**Answer:**
A hash index keeps keys in memory along with the byte offset of the corresponding value stored on disk.

#### 5. In a B-Tree, how many places can a specific key exist?
**Answer:**
A key exists in exactly one place in a B-Tree.

#### 6. T/F: In document databases, many-to-many relationships fit naturally into the document model without application-level emulation.
**Answer:**
False. Many-to-many relationships do not fit nicely into tree-structured document models. If native join support is weak or absent, joins must be emulated manually in application code.

#### 7. T/F: Many database vendors now focus on supporting either transaction processing (OLTP) or analytics (OLAP) workloads, but not both.
**Answer:**
True. OLTP systems are optimized for low-latency random reads/writes, while OLAP systems are optimized for massive sequential scans across analytical queries, leading to specialized engine designs.

#### 8. What are the benefits of using an append-only log of immutable events (like a ledger)?
**Answer:**
It provides strong auditability for financial systems and makes it much easier to debug and trace historical state changes or diagnose code that writes erroneous data.

#### 9. What core data structure is required in a database to efficiently find the value for a particular key?
**Answer:**
An index.

#### 10. What dataset transformation function is built into relational databases to speed up reads at the cost of write overhead?
**Answer:**
CREATE INDEX

#### 11. What entity is used to identify a page within a B-Tree?
**Answer:**
An address (or page reference/disk pointer).

#### 12. What is a clustered index?
**Answer:**
A clustered index stores the actual data rows directly within the index structure itself (typically as a B-Tree), meaning the table data is ordered physically on disk by the indexed column.

#### 13. What is a concatenated (composite) index?
**Answer:**
A concatenated index combines several keys into one index key by appending one column to another in a specified order, enabling efficient lookups on queries filtering by a prefix of those columns.

#### 14. What is data locality regarding document schemas (like JSON), and what performance benefits does it provide over multi-table relational designs?
**Answer:**
Data locality refers to storing related entities together in physical storage. JSON representations achieve great locality because all nested attributes reside in a single document, avoiding the multiple queries or expensive multi-way joins required in normalized relational schemas.

#### 15. What is the fundamental purpose and mechanism of a database index?
**Answer:**
The general idea behind an index is to keep auxiliary metadata on the side, acting as a signpost to efficiently locate and access the primary data records without requiring full table scans.

#### 16. What is the fundamental structural difference between an SSTable (Sorted String Table) and a standard log-structured storage segment?
**Answer:**
The keys in an SSTable are sorted.

#### 17. What is typically the primary bottleneck for OLAP (Online Analytical Processing) systems?
**Answer:**
Disk bandwidth (the speed at which data can be read from disk), due to scanning large volumes of sequential data.

#### 18. What is typically the primary bottleneck for OLTP (Online Transaction Processing) systems?
**Answer:**
Disk seek time (random access latency), due to frequent random reads and writes.

#### 19. What schema template is most commonly used in OLAP data warehouses, and what is a variation of it called?
**Answer:**
Star schema (also known as dimensional modeling). A variation is the snowflake schema, where dimensions are further broken down into subdimensions.

#### 20. What structural similarity do B-trees and SSTables share regarding key organization?
**Answer:**
Both keep key-value pairs sorted by key, which enables efficient single key-value lookups and fast range queries.

#### 21. What workload operation are databases primarily optimized to handle when storing the current state of an application?
**Answer:**
Reads (as well as point lookups and transactional updates, contrasting with write-optimized analytical data stores).

#### 22. When does the advantage of unbundling and composing multiple storage technologies actually materialize?
**Answer:**
It only comes into the picture when there is no single piece of monolithic software that satisfies all of your application's requirements.

#### 23. Why are hash table indexes suboptimal for certain database query patterns?
**Answer:**
Hash table indexes do not provide efficient support for range queries because keys are not stored in a sorted order, meaning you cannot easily scan sequential keys.

#### 24. Why do SSTables support efficient range queries?
**Answer:**
SSTables support efficient range queries because the keys within each table file are stored in strict sorted order, allowing the engine to seek to the start key and sequentially read subsequent keys without random disk I/O.

#### 25. Why is encoding data very compactly important when reading a large number of rows?
**Answer:**
To minimize the amount of data that the query needs to read from disk and transfer over I/O channels.


### 🟡 Mid Level

#### 1. How can data warehouse queries over wide fact tables (e.g., 100+ columns) be executed efficiently when only a few columns are accessed?
**Answer:**
Using column-oriented storage, which stores columns separately rather than rows, allowing the database to only read the specific columns required by the query.

#### 2. How can you pack more keys into B-Tree pages to improve storage density?
**Answer:**
By abbreviating or truncating keys (storing only key prefixes rather than full keys), which allows branching factors to increase.

#### 3. How do storage engines provide a consistent snapshot while incurring minimal performance overhead?
**Answer:**
By never updating existing data values in place. Instead, they use append-only or multi-version concurrency control (MVCC) mechanics to create a new data version every time a value is changed, allowing readers to access older point-in-time snapshots concurrently without locking writers.

#### 4. How does an SSTable sparse index facilitate block-level compression?
**Answer:**
An SSTable sparse index contains keys pointing to specific data blocks rather than every individual record. Because only a subset of keys is indexed, the underlying blocks can be independently compressed (e.g., using Snappy or LZ4) to save space while keeping the index memory-resident.

#### 5. How does an SSTable use a sparse index to reduce the overall index size in memory?
**Answer:**
It indexes only one key for every few kilobytes of the segment file, relying on local scans between index entries.

#### 6. How does sorting data within columnar storage formats improve compression?
**Answer:**
Sorting groups similar values together, which significantly enhances compression efficiency when using encoding techniques like run-length encoding (RLE).

#### 7. How does the performance of appending to a file compare to random writes?
**Answer:**
Appending to a file is generally very efficient and fast because it typically involves sequential I/O operations rather than seeking across disk blocks.

#### 8. How is atomicity implemented for single objects on a single node?
**Answer:**
Atomicity can be implemented using a write-ahead log (WAL) for crash recovery.

#### 9. How is creating a database index similar to bootstrapping a follower replica or CDC stream?
**Answer:**
When creating an index, the database reprocesses the existing dataset via a snapshot and derives an index as a new view of the existing data, similar to how the initial snapshot of a CDC system works.

#### 10. How is snapshot isolation implemented at the storage engine level?
**Answer:**
The database maintains multiple committed versions of an object concurrently. This design pattern is known as Multi-Version Concurrency Control (MVCC).

#### 11. In LSM-storage engines utilizing size-tiered compaction, how are SSTables merged?
**Answer:**
Newer and smaller SSTables are successively merged into older and larger SSTables.

#### 12. In database storage engines, where is the actual data referred to by keys in a secondary index typically stored?
**Answer:**
A heap file (an unstructured append-only or unsorted file where records are stored and accessed via a record ID/pointer).

#### 13. True or False: The performance advantage of in-memory databases comes strictly from avoiding disk reads.
**Answer:**
False. Even disk-based storage engines can avoid reading from disk if there is enough RAM, as the OS caches recently used blocks. In-memory databases are faster primarily because they avoid the overhead of encoding and decoding in-memory data structures into formats suitable for on-disk layouts. Disk is typically used only as an append-only log for durability.

#### 14. What are materialized aggregates?
**Answer:**
Materialized aggregates are cached results of aggregation functions (like COUNT, SUM, AVG) that can be reused directly by multiple queries to improve read performance.

#### 15. What are the advantages of in-memory databases regarding data models?
**Answer:**
In-memory databases provide data structures and models that are difficult to implement efficiently with disk-based indexes, such as priority queues, sets, and complex graphs.

#### 16. What are the primary bottlenecks and typical solutions for OLTP vs OLAP storage engines?
**Answer:**
1. OLTP: Disk seek time is the bottleneck. Solution: minimize records touched per query using indexes. 2. OLAP: Disk bandwidth is the bottleneck. Solution: column-oriented storage, compression, and vectorization.

#### 17. What are the primary performance and storage trade-offs of LSM-Trees compared to B-Trees?
**Answer:**
LSM-trees are typically faster for writes and can sustain higher write throughput due to lower write amplification and reduced storage overhead (better compression, no page fragmentation). However, they can suffer from write amplification during compaction, are slower for missing keys, and B-trees are generally faster for reads.

#### 18. What are two non-document databases or models that offer data locality properties similar to document databases?
**Answer:**
1. Google Spanner (relational model) allows schemas to declare that table rows should be interleaved (nested) within a parent table.
2. The column-family concept in the Bigtable data model (used in Apache Cassandra and HBase) manages locality similarly.

#### 19. What data model does the Parquet storage format support?
**Answer:**
Parquet is a columnar storage format optimized for analytics that supports nested and document-style data models.

#### 20. What is a Log-Structured Merge-Tree (LSM-Tree)?
**Answer:**
An LSM-Tree is a data structure and storage engine design (used in systems like LevelDB, RocksDB, and Cassandra) optimized for high write throughput by maintaining sorted data files (SSTables) on disk through continuous background compaction and merging.

#### 21. What is a changelog and what does it represent in database architectures?
**Answer:**
An append-only log of immutable changes that represents the evolution of a mutable state over time.

#### 22. What is a clustered index, and what is a covering index as a compromise?
**Answer:**
A clustered index stores the entire row data directly within the index leaf nodes, avoiding an extra lookup hop. A covering index (or index with included columns) is a compromise that stores a subset of table columns inside the index to satisfy specific queries directly.

#### 23. What is a covering index?
**Answer:**
A covering index stores some or all of the table's requested columns directly within the index structure, allowing the query engine to satisfy queries entirely from the index without performing a secondary lookup to the main table data.

#### 24. What is a materialized view and why are they generally not recommended for OLTP databases?
**Answer:**
A materialized view is a precomputed copy of query results. They are poor choices for OLTP databases because they must be updated or recomputed on writes, severely impacting write performance and throughput.

#### 25. What is column-oriented storage, how does it optimize analytical queries, and how are individual rows reassembled?
**Answer:**
Instead of storing all row values contiguously, column-oriented storage groups values from each column into separate files. Analytical queries accessing only 4-5 out of 100+ columns only read the required files, saving massive I/O. Rows are reassembled by aligning entries by their positional index across column files.

#### 26. What is log compaction and how does it serve as an alternative to the snapshot process in Change Data Capture (CDC)?
**Answer:**
Log compaction is an alternative to taking a full snapshot. The storage engine periodically scans the log in the background, discards older duplicate log records for the same key, and retains only the most recent update. Deletions are represented via a tombstone, which can eventually be removed entirely once the compaction process cleans it up.

#### 27. What is space amplification in the context of SSTables and storage engines, and why does it require extra disk space?
**Answer:**
Space amplification refers to the phenomenon where the total disk space required by the storage engine is significantly larger than the actual raw data size due to overhead, outdated record versions, and compaction backlog. The disk needs to be provisioned with extra capacity to accommodate concurrent file rewrites during compaction processes.

#### 28. What is the primary purpose of a Bloom filter in database storage engines?
**Answer:**
A Bloom filter is a space-efficient probabilistic data structure that can definitively tell you if a key does not appear in the database, avoiding unnecessary disk reads (though it may occasionally yield false positives for presence).

#### 29. What is the write path in data systems?
**Answer:**
The write path is the process that occurs whenever a piece of information is written to the system, often involving precomputing or updating storage structures like memtables and commit logs.

#### 30. What is write amplification?
**Answer:**
Write amplification is a phenomenon where the physical number of bytes written to the storage medium is a multiple of the logical bytes written by the application, often caused by compaction, log-structured updates, or wear-leveling in SSDs.

#### 31. What operational benefit does snapshot isolation provide to a database?
**Answer:**
It allows the database to handle long-running read queries on a consistent point-in-time snapshot simultaneously with processing writes normally using MVCC.

#### 32. When merging multiple SSTable segments during compaction, how are duplicate keys handled?
**Answer:**
SSTable merging retains the value from the most recent segment (determined by sequence numbers or timestamps) and discards older overwritten or deleted values (tombstones).

#### 33. Why are ACID atomicity and isolation needed even for a single data object?
**Answer:**
To prevent corruption caused by concurrent reads or partial writes (faults occurring midway through writing a large object, such as a 20 KB JSON document).

#### 34. Why do database indexes typically slow down write operations?
**Answer:**
Because the index structures must also be updated every time data is written to the database.

#### 35. Why is a Write-Ahead Log (WAL) required in B-Tree storage engines?
**Answer:**
A WAL is required for crash recovery because B-Trees modify pages in-place by overwriting existing pages, which can leave the database in a corrupted state if a crash occurs mid-write.

#### 36. Why is paging/swapping to disk often disabled on database server machines?
**Answer:**
To avoid thrashing. If memory pressure is high and swapping is enabled, simple memory accesses can trigger page faults requiring slow disk I/O, causing the OS to spend most of its time swapping pages rather than executing work. Server engines prefer to crash or kill a process to free up memory rather than risk thrashing.

#### 37. Why is write amplification a critical concern on SSDs?
**Answer:**
SSDs cannot overwrite existing blocks directly; they must erase entire blocks before writing, causing internal rewrites (write amplification) that degrade performance and wear out flash memory cells.


### 🔴 Senior Level

#### 1. Describe the operational workflow and crash recovery mechanism of an LSM-Tree (Log-Structured Merge-Tree) storage engine.
**Answer:**
1. New writes are appended to an unformatted Write-Ahead Log (WAL) for crash recovery, then inserted into an in-memory balanced tree called a memtable.
2. When the memtable exceeds a size threshold, it is flushed to disk as a sorted SSTable segment.
3. Read requests check the memtable first, followed by the most recent SSTable segment file, down to older segment files (often aided by Bloom filters).
4. Background threads periodically run compaction and merging on segment files to discard obsolete data and maintain read performance.

#### 2. How can a compound primary key enable an elegant data model for partitioning and sorting?
**Answer:**
A compound key acts as a hybrid approach (alternative to pure key-range or hash partitioning). The first part is hashed to determine the partition, while subsequent columns are used as a concatenated index for sorting SSTables (e.g., (user_id, update_timestamp)).

#### 3. How can a two-dimensional geographic location be translated into a single comparable number for indexing?
**Answer:**
By using a space-filling curve, such as a Hilbert curve or Z-order curve (Morton code), which maps multi-dimensional data to a one-dimensional index while preserving locality.

#### 4. How do LSM-Tree storage engines use mergesort to handle segment files that exceed available memory?
**Answer:**
LSM-Trees use a multi-way mergesort algorithm to combine multiple sorted SSTable segment files. By streaming data sequentially from disk, reading blocks into small input buffers, and writing out a newly sorted file, the merge process operates independently of total dataset size and requires memory proportional only to the number of concurrent file streams being merged.

#### 5. How do storage engines implement snapshot isolation concurrently with writes?
**Answer:**
By using Multi-Version Concurrency Control (MVCC), where readers never block writers and writers never block readers by maintaining multiple committed versions of objects.

#### 6. How does Vectorized Processing optimize execution in columnar storage engines?
**Answer:**
Vectorized processing makes efficient use of CPU cycles by loading chunks of compressed columnar data into the L1 cache and running operations in a tight loop.

#### 7. What are the two main schools of thought for OLTP storage engines?
**Answer:**
1. The log-structured school: appends only, no in-place updates (e.g., LSM-trees, Bitcask, Cassandra, HBase, RocksDB). 2. The update-in-place school: treats disk as fixed-size pages that can be overwritten (e.g., B-trees in relational databases).

#### 8. What factors dictate SSTable compaction and merging strategies?
**Answer:**
SSTable compaction and merging strategies rely heavily on order (maintaining sorted key sequences via mergesort) and timing (such as size-tiered vs. leveled compaction policies to balance write amplification, read amplification, and space amplification).

#### 9. What file format and indexing structure are used for key-value stores like LevelDB, and what are the 5 core steps of its storage engine?
**Answer:**
Format: Sorted String Table (SSTable). Architecture: LSM-tree (Log-Structured Merge-tree).
1. Writes are appended to an in-memory balanced tree (memtable).
2. When the memtable exceeds a threshold, it is flushed to disk as a sorted SSTable file.
3. Reads check the memtable first, then fall back to newest-to-oldest on-disk SSTables using sparse indexes/Bloom filters.
4. Background compaction and merging processes combine SSTables and discard overwritten/deleted keys.
5. A sequential write-ahead log (WAL) on disk ensures durability and memtable recovery after crashes.

#### 10. What is a primary operational disadvantage of Leveled Compaction in LSM-tree storage engines?
**Answer:**
Write amplification, as data must be repeatedly read, sorted, and rewritten across multiple levels on disk.

#### 11. What major compaction disadvantage is associated with size-tiered compaction algorithms?
**Answer:**
Size-tiered compaction has the problem of high space amplification, as it requires extra disk space to rewrite larger SSTables during compaction runs.

#### 12. Why is it unlikely that a single piece of software can satisfy all read and write patterns for an application?
**Answer:**
Different access patterns (e.g., full-text search, analytical aggregations, low-latency point lookups) require vastly different storage layouts, indexing strategies, and underlying data structures, necessitating polyglot persistence.

#### 13. Why might an LSM-storage engine struggle with extreme write-heavy workloads despite having fast raw writes?
**Answer:**
Because of write amplification, which can saturate I/O throughput limits.

#### 14. With B-Trees, when a data update causes a record to exceed its leaf node space and move to a new location, what two strategies are used?
**Answer:**
Either all secondary indexes referencing the record are updated, or a forwarding pointer is left behind in the original location pointing to the new address.


## 📂 Category: Storage Engines & Architecture (5 cards)

### 🟢 Junior Level

#### 1. What are 5 core characteristic comparisons between OLTP (Online Transaction Processing) and OLAP (Online Analytical Processing)?
**Answer:**
1. Main read pattern: OLTP uses small numbers of records fetched by key; OLAP performs large-scale aggregations over massive record sets.
2. Main write pattern: OLTP handles random-access, low-latency writes from user input; OLAP relies on bulk imports (ETL) or continuous event streams.
3. Primary users: OLTP is used by end-users/customers via web apps; OLAP is used by internal analysts for business intelligence and decision support.
4. Data representation: OLTP captures the latest state at a current point in time; OLAP tracks historical time-series event logs.
5. Dataset size: OLTP ranges from gigabytes to terabytes; OLAP ranges from terabytes to petabytes.

#### 2. What are four primary driving forces behind the rise of NoSQL databases?
**Answer:**
1. A need for greater horizontal scalability than relational databases easily achieve, including massive datasets and high write throughput.
2. Specialized query operations and data structures poorly supported by the relational model (e.g., graphs, wide-column stores).
3. Frustration with rigid relational schemas, creating a desire for dynamic, schema-flexible data models.
4. A widespread preference for open-source software over commercial, proprietary database products.

#### 3. What are the left and right halves of a typical data system architecture figure representing in terms of data flow?
**Answer:**
The left half of the figure represents the write path (ingesting and storing writes), and the right half represents the read path (serving queries to clients).


### 🟡 Mid Level

#### 1. Does relying on strong database safety properties eliminate the risk of data loss from application bugs?
**Answer:**
Even with strong safety properties from a database, application bugs can occur that cause data loss or corruption. Immutable and append-only data architectures make it easier to recover from such mistakes, but they are not a complete cure-all.

#### 2. What is the primary architectural role of caches, indexes, and materialized views?
**Answer:**
Their role is to shift the boundary between the write path and the read path. They allow systems to do more work upfront on the write path (by precomputing results) in order to save computation and effort on the read path.


## 📂 Category: Storage Engines & Concurrency (1 cards)

### 🟡 Mid Level

#### 1. From a performance point of view, what is a key principle of snapshot isolation regarding readers and writers?
**Answer:**
Readers never block writers, and writers never block readers. This allows a database to handle long-running read queries on a consistent snapshot concurrently with normal write processing, eliminating lock contention between them.


## 📂 Category: Storage Engines & Data Layout (2 cards)

### 🟡 Mid Level

#### 1. Why does column-oriented storage lend itself very well to data compression?
**Answer:**
Column-oriented storage stores values of the same column contiguously on disk. Because values in the same column often share similar data types and repetitive patterns (low cardinality), compression algorithms (like run-length encoding and bit-packing) can achieve extremely high compression ratios compared to row-oriented storage.


### 🔴 Senior Level

#### 1. What storage engine scheme replaced traditional write-ahead logs (WAL) in some systems?
**Answer:**
A copy-on-write (or append-only / Bw-tree style) scheme, which avoids in-place updates by writing new versions of pages to new locations.


## 📂 Category: Storage Engines & Data Systems (4 cards)

### 🟢 Junior Level

#### 1. What is schema evolution in the context of storage formats?
**Answer:**
Schema evolution allows the entire database or data store to appear as if it was encoded with a single schema, even though the underlying storage may contain records encoded with various historical versions of the schema.


### 🟡 Mid Level

#### 1. How do traditional transaction systems and derived data systems differ regarding linearizability and asynchronous updates?
**Answer:**
Transaction systems usually provide linearizability (e.g., read-your-writes guarantees), whereas derived data systems and log consumers are typically updated asynchronously by design.

#### 2. What are the two common options for merging and compacting SSTables in LSM-tree storage engines?
**Answer:**
Size-tiered compaction and Leveled compaction.


### 🔴 Senior Level

#### 1. What is 'unbundling databases' (unifying writes) in modern data architectures?
**Answer:**
Unbundling refers to separating a database's monolithic index-maintenance and storage features to allow synchronized writes across disparate technologies (e.g., search indexes, caches, and relational stores), conceptually similar to composing Unix tools together via pipes.


## 📂 Category: Storage Engines & Database Architecture (1 cards)

### 🟡 Mid Level

#### 1. What are three common drawbacks of traditional database stored procedures, and how do modern platforms mitigate them?
**Answer:**
Drawbacks:
1. Proprietary vendor languages (e.g., PL/SQL, T-SQL, PL/pgSQL) lack modern programming ecosystems and libraries.
2. Code running inside a database is difficult to debug, version control, deploy, test, and monitor.
3. A badly written stored procedure can destabilize the shared database instance for all connecting applications.
Mitigations:
Modern systems allow general-purpose programming languages (e.g., VoltDB uses Java/Groovy, Datomic uses Clojure/Java, Redis uses Lua).


## 📂 Category: Storage Engines & Encodings (1 cards)

### 🟢 Junior Level

#### 1. Unlike standard Unix file pipelines, what structured file formats do big data engines like Hadoop frequently use?
**Answer:**
Structured and columnar file formats such as Apache Avro (for row-oriented storage and schema evolution) and Apache Parquet (for analytical columnar storage).


## 📂 Category: Storage Engines & Indexes (7 cards)

### 🟢 Junior Level

#### 1. How can crash recovery time be optimized in log-structured hash index engines, and what is the preferred file format for logs?
**Answer:**
Crash recovery time can be reduced by storing a snapshot of the in-memory hash table on disk. A binary format is typically the best file format to use for logs because length-prefixed binary encoding is faster and simpler than parsing text.

#### 2. When queries require sequentially scanning across a large number of rows, which data structure becomes much less relevant?
**Answer:**
Indexes.


### 🟡 Mid Level

#### 1. During compaction in log-structured engines, how are reads and writes handled concurrently, and how are partially written records ignored?
**Answer:**
Compaction runs in a background thread; read requests continue to be served from old segment files, while new write requests go to the latest segment file. Partially written records are ignored using file checksums.

#### 2. How are records deleted in log-structured storage engines, and what purpose does compaction serve regarding keys?
**Answer:**
Deletions are handled by appending a special deletion record called a 'tombstone'. Compaction merges segments, writes them to new files, and discards duplicate keys and overwritten values.

#### 3. What are 2 key advantages of LSM-trees over B-trees, and 2 key advantages of B-trees over LSM-trees?
**Answer:**
LSM-tree advantages: 1. Faster writes due to sequential logging and lower write amplification. 2. Better storage efficiency/compression (avoids page fragmentation).
B-tree advantages: 1. Faster reads because data resides in a single predictable location rather than multiple SSTables. 2. Better transactional semantics with range locking directly attached to tree pages.

#### 4. What are the primary structural characteristics and operational overheads of B-Trees in database storage engines?
**Answer:**
B-trees break the database down into fixed-size blocks or pages, overwrite pages on disk with new data, and incur the overhead of writing an entire page even if only a few bytes have changed. They use a write-ahead log (WAL) or redo log for crash resilience, use latches for concurrency control, and attempt to keep leaf pages in sequential order on disk.


### 🔴 Senior Level

#### 1. How does leveled compaction organize data in log-structured storage engines, and what are its benefits?
**Answer:**
The key range is split up into smaller SSTables, and older data is moved into separate 'levels'. This allows compaction to proceed more incrementally and use less disk space compared to size-tiered compaction.


## 📂 Category: Storage Engines & Indexing (5 cards)

### 🟢 Junior Level

#### 1. What is the data structure of the most basic search index?
**Answer:**
A term dictionary mapping each search term to a postings list of document IDs (term: [doc_id_1, doc_id_2, ...]).


### 🟡 Mid Level

#### 1. What are multi-dimensional indexes, and what are two common use cases where they are useful?
**Answer:**
Multi-dimensional indexes are a general way of querying several columns at once, essential for multi-attribute or geospatial data.
Use cases:
1. Searching for items within a range of colors using a 3D index on (red, green, blue).
2. Querying weather observations with a 2D index on (date, temperature) to efficiently filter by date range and temperature simultaneously without full table scans.

#### 2. What is a term dictionary in full-text search?
**Answer:**
An index structure mapping unique search terms to the list of document IDs containing those terms.


### 🔴 Senior Level

#### 1. Describe the architectural layout of a B-Tree storage engine and its write amplification profile.
**Answer:**
A B-Tree is a tree of fixed-size pages (typically 4KB or larger) containing continuous key ranges and pointers to child pages. All actual data values or row references reside in the leaf pages. If the storage engine implements a Write-Ahead Log (WAL) for crash recovery, every piece of data is effectively written twice: once to the append-only WAL on disk and once to the in-place B-Tree page structure.

#### 2. How does Lucene use SSTables for full-text search?
**Answer:**
Lucene maintains posting lists in SSTables, where a posting list contains key-value pairs mapping search terms to a list of document IDs.


## 📂 Category: Storage Engines & OLAP (2 cards)

### 🟢 Junior Level

#### 1. What is the standard industry term for an OLAP (Online Analytical Processing) database?
**Answer:**
A data warehouse.


### 🟡 Mid Level

#### 1. What is the difference between a materialized view and a standard (virtual) view? Which one is more useful for OLAP, why isn't it as useful for OLTP, and how does it relate to OLAP cubes?
**Answer:**
A materialized view is an actual copy of query results written to disk, whereas a virtual view is a shortcut that gets expanded into the underlying query on the fly by the SQL engine. Materialized views are useful in read-heavy OLAP data warehouses to precompute aggregates and speed up queries (such as data cubes, which are specialized multidimensional materialized views). They are rarely used in OLTP because data changes require automatic updates to denormalized copies, making writes significantly more expensive. However, data cubes lack the flexibility of querying raw data directly.


## 📂 Category: Storage Engines & OS Interaction (1 cards)

### 🟡 Mid Level

#### 1. What is OS thrashing?
**Answer:**
An OS performance state where virtual memory swapping (paging) consumes an excessive amount of system resources. A memory access results in a page fault requiring a page to be loaded from disk, and in extreme cases, the OS spends most of its time swapping pages in and out rather than executing useful work.


## 📂 Category: Storage Engines & Transactions (1 cards)

### 🟢 Junior Level

#### 1. What type of queries is snapshot isolation especially important for (cite 3 examples)?
**Answer:**
Long-running queries, such as:
- Taking backups
- Analytic queries
- Periodic integrity checks


## 📂 Category: Storage Engines / Transactions (1 cards)

### 🟡 Mid Level

#### 1. What is the key difference between snapshot isolation and two-phase locking (2PL) regarding reader-writer blocking?
**Answer:**
In 2PL, writers don't just block other writers; they also block readers, and readers block writers. Snapshot isolation follows the mantra: readers never block writers, and writers never block readers.


## 📂 Category: Stream & Batch Processing (1 cards)

### 🔴 Senior Level

#### 1. What 3 properties are required to unify batch and stream processing without the downsides of the Lambda Architecture?
**Answer:**
1. The ability to replay historical events through the same processing engine that handles the recent event stream.
2. Exactly-once semantics for stream processors (ensuring the output is identical to a failure-free execution).
3. Native tools for windowing by event time rather than processing time.


## 📂 Category: Stream Processing (63 cards)

### 🟢 Junior Level

#### 1. How are producers and consumers related in the context of stream processing events?
**Answer:**
An event is generated by a producer (aka publisher, sender) and processed by multiple consumers (subscribers, recipients).

#### 2. How are related events grouped together in stream processing?
**Answer:**
Related events are grouped together by a topic or a stream.

#### 3. How are statistics typically computed in stream analytics?
**Answer:**
Over a time interval, known as a window.

#### 4. How do message brokers handle consumer crashes to ensure messages are not lost during delivery?
**Answer:**
Message brokers use acknowledgements (acks): a client must explicitly inform the broker when it has finished processing a message so the broker can safely remove it from its queue/log.

#### 5. How is a topic defined in a partitioned log-based message broker?
**Answer:**
A topic is defined as a logical group of partitions that all carry messages of the same specific type or category.

#### 6. How is durability handled by log-based message brokers?
**Answer:**
The broker sequentially appends messages to disk storage so they are not lost in the event of a broker crash or restart.

#### 7. How is the input characterized in stream processing compared to batch processing?
**Answer:**
The input is unbounded—meaning the job runs continuously over a never-ending stream of incoming data.

#### 8. If a user adds an item to their shopping cart and then removes it, what type of system architecture captures this full lifecycle info, and what type loses it?
**Answer:**
This is captured in an event log (an append-only log of immutable events) and lost in a traditional database that simply deletes the item row.

#### 9. In a log-based messaging system, how can a consumer determine which messages have already been processed?
**Answer:**
All messages with an offset less than a consumer's current committed offset have already been processed.

#### 10. In stream processing, what is a record called, and how is it defined?
**Answer:**
A record is known as an event—a small, self-contained, immutable object containing details of something that happened at some point in time, with a timestamp according to a time-of-day clock.

#### 11. Is message loss acceptable in a pub-sub messaging system?
**Answer:**
It depends on the application requirements. For example, occasional message loss for sensor readings might be acceptable, whereas message loss for financial counting or transactional processing is not.

#### 12. What are Apache Storm, Spark Streaming, and Kafka Streams used for?
**Answer:**
Stream analytics

#### 13. What does a log-based message broker with partitions represent?
**Answer:**
Producers send messages by appending them sequentially to a topic-partition file, and consumers read these immutable files sequentially, allowing independent consumer offsets.

#### 14. What is a piece of code that processes a stream commonly known as?
**Answer:**
An operator or job.

#### 15. What is a tumbling window in stream processing?
**Answer:**
A tumbling window has a fixed, non-overlapping length where every event belongs to exactly one window. For example, in a 1-minute tumbling window, all events with timestamps between 10:03:00 and 10:03:59 are grouped together, and events between 10:04:00 and 10:04:59 form a separate window.

#### 16. What is stream analytics?
**Answer:**
The practice of computing statistical metrics, sliding-window aggregations, and patterns over a continuous, high-volume stream of real-time events.

#### 17. What is the classic use case for stream processing? Provide examples.
**Answer:**
Monitoring and immediate alerting when specific event patterns occur. Examples include fraud detection systems, real-time financial trading platforms, and industrial IoT manufacturing monitoring.


### 🟡 Mid Level

#### 1. How are databases and data streams closely related?
**Answer:**
An event can be considered a write to a database. For example, a replication log is a stream of database events produced by the leader and applied by followers. State machine replication in total order broadcast is another form of event streaming.

#### 2. How can you implement a feature to notify users when a new event (such as a real estate listing or news story) matches their pre-configured search criteria?
**Answer:**
Use search-on-streams (complex event processing / stream matching): formulate search queries in advance and continually match incoming event streams against these stored queries.

#### 3. How do log-based message brokers achieve parallelism and track consumer progress?
**Answer:**
The broker assigns all messages in a partition to the same consumer node and always delivers messages in the same order. Parallelism is achieved through partitioning, and consumers track progress by checkpointing the offset of the last processed message. Messages are retained on disk, allowing consumers to reread old messages.

#### 4. How do you estimate the clock offset between a device and a server using timestamps in stream processing?
**Answer:**
By subtracting the timestamp of when the event was sent (according to the device clock) from the time the event was received (according to the server clock), you can estimate the offset between the device and server clocks.

#### 5. How does consumer failover work in a log-based messaging system?
**Answer:**
If a consumer node fails, another node in the consumer group is reassigned to take over the failed consumer's partitions, and it resumes processing from the last recorded and committed offset.

#### 6. How does maintaining materialized views via streams differ from standard stream analytics?
**Answer:**
Stream analytics often operates over sliding or tumbling time windows of recent events. In contrast, maintaining a materialized view (like caches, search indexes, or data warehouses) requires processing the entire history of events to build a complete state.

#### 7. How is the relationship between queries and data reversed in Complex Event Processing (CEP)?
**Answer:**
Instead of executing a transient query against stored data, queries are stored long-term in the engine, and input event streams continuously flow past them. In a standard database, a query is discarded immediately after execution.

#### 8. In a log-based message queue system, how does a slow message affect the processing of subsequent messages within the same partition?
**Answer:**
Because log partitions are processed sequentially per consumer, a single slow message blocks the processing of subsequent messages in that same partition.

#### 9. What are the pitfalls of using 'processing time' based on the local system clock in stream processors?
**Answer:**
Stream processors often compute analytics over time windows. Relying on the local system clock of the processing machine (processing time) causes divergence and inaccuracy if there is processing lag, network delays, or out-of-order events, making 'event time' tracking preferable.

#### 10. What are the primary purposes of stream processing?
**Answer:**
1. Searching for event patterns (complex event processing).
2. Computing windowed aggregations (stream analytics).
3. Keeping derived data systems up to date (materialized views).

#### 11. What are the three options for handling situations where producers send messages faster than consumers can process them in a pub-sub system?
**Answer:**
1. Drop messages
2. Buffer messages in a queue
3. Apply backpressure (flow control) by blocking the producer from sending more messages

#### 12. What are the three primary options for the output destination and handling of processed streams?
**Answer:**
1. Write event data to a derived data system (e.g., database, cache, search index).
2. Push events to human users (e.g., email, push notification, live dashboard).
3. Process input streams to produce one or more output streams through a pipeline of processing stages.

#### 13. What core operational property do microbatching frameworks provide to streaming processors?
**Answer:**
Fault tolerance, by treating small time-bounded batches as discrete units of work that can be retried or replayed upon failure.

#### 14. What fault-tolerance mechanism does checkpointing provide in stream processing engines?
**Answer:**
It allows a crashed stream operator to recover and restart state from the most recent persistent checkpoint rather than reprocessing the entire stream from the beginning.

#### 15. What is Complex Event Processing (CEP)?
**Answer:**
A stream processing paradigm that uses high-level declarative query languages (like SQL) to define and detect specific patterns across incoming event streams, emitting a derived 'complex event' when a match occurs.

#### 16. What is a 'hopping window' in stream processing?
**Answer:**
A window with a fixed length that allows windows to overlap to provide smoothing (e.g., a 5-minute window with a hop size of 1 minute).

#### 17. What is a major operational advantage of consumer independence in log-based messaging systems?
**Answer:**
Consumers can independently read data at their own pace without affecting each other or the broker. This allows teams to safely consume production logs for offline dev/testing environments without disrupting live production services.

#### 18. What is a session window in stream processing?
**Answer:**
A session window has no fixed duration, but ends after a defined period of inactivity. For example, all events for the same user that occur closely together in time until the user has been inactive for 30 minutes.

#### 19. What is a sliding window in stream processing?
**Answer:**
A sliding window contains all the events that occur within a specific rolling time interval of each other (e.g., a 5-minute sliding window evaluated continuously).

#### 20. What is an alternative name for a stream-table join, and how does it function?
**Answer:**
A stream-table join is also known as stream enrichment. One input stream consists of activity events while the other is a database changelog that maintains a local, up-to-date replica. For each incoming activity event, the join operator queries the local database copy to enrich the event with contextual attributes.

#### 21. What is log compaction in stream processing systems (like Kafka)?
**Answer:**
Log compaction is a mechanism where the log retains only the most recent update for each key, allowing a stream to retain a full copy of the latest database state.

#### 22. What is microbatching in stream processing?
**Answer:**
A fault-tolerance and processing strategy that divides an unbounded continuous stream into tiny, discrete time-bounded blocks (micro-batches), processing each block using standard batch-processing execution engines.

#### 23. What is the upper limit on the number of consumer nodes sharing the work of consuming a topic in a log-based message broker?
**Answer:**
The maximum number of consumer nodes is at most the number of log partitions in that topic, because messages within the same partition are delivered to the same sequential consumer node.

#### 24. What message reordering or duplication issue can occur in a message broker utilizing consumer load balancing and redelivery?
**Answer:**
Consumer 2 crashes while processing message m3, causing the broker to redeliver m3 to Consumer 1 at a later time, potentially resulting in out-of-order processing.

#### 25. What operational advantages do log-based message systems have over traditional AMQP/JMS-style brokers regarding message reading?
**Answer:**
Reading messages does not have a destructive deletion side effect. Consumers can start reading at different points in time with different processing code, enabling easier experimentation and recovery from errors/bugs.

#### 26. What operational limitations do standard message brokers have regarding queue length and querying?
**Answer:**
Message brokers generally assume that queues are relatively short; throughput can degrade severely if the broker is forced to buffer a large volume of messages to disk or memory. Additionally, message brokers do not support arbitrary querying of queued messages.

#### 27. Why is defining windows in terms of event time tricky for stream processors regarding straggler events?
**Answer:**
A stream processor can never be completely sure when it has received all of the events for a particular window or whether there are straggler events still to come due to network delays or mobile device offline states.

#### 28. Why must an offset version of a device's local clock be used to determine event timing in stream processing?
**Answer:**
Events can be buffered locally on a device (e.g., a mobile app offline) before being sent to a server, meaning the local generation timestamp differs significantly from the ingestion timestamp.


### 🔴 Senior Level

#### 1. Describe how to enforce or claim a unique username using a stream processor backed by an append-only log.
**Answer:**
1. Each request for a username is appended as a message to a partition based on the hash of the username.
2. A stream processor reads the requests from the log, using a local database to track taken usernames, and emits success or rejection messages to an output stream.
3. The requesting client watches the output stream and waits for the success or rejection outcome.

#### 2. How can a stream processor maintain a per-user cache of their Twitter timeline (posts and deletes) along with follow/unfollow relationships?
**Answer:**
Ingest streams of tweets and follows/unfollows. The stream processor maintains an internal state database containing the current set of followers for each user to determine which specific timelines need to be updated upon a new tweet.

#### 3. How can read requests be handled directly as a stream of events?
**Answer:**
Route both read and write events through a stream processor. The processor responds to read events by emitting the read result to an output stream, functioning equivalently to a stream-table join between the read query stream and the database table.

#### 4. How can read requests be handled within a stream processing architecture?
**Answer:**
Read requests can be represented as streams of events and sent alongside write events through a stream processor. The processor responds to read events by emitting the result of the read to an output stream.

#### 5. How do REST/microservices versus dataflow approaches handle dependencies like a customer purchasing an item priced in one currency and paid in another?
**Answer:**
1. In a REST/microservices approach, the code processing the purchase queries an exchange-rate service/database at runtime to get the current rate.
2. In the dataflow approach, the code processing purchases subscribes to a stream of exchange rate updates ahead of time and records the current rate in a local database when it changes. Note that the dataflow approach must handle strict time dependencies between events.

#### 6. How do event-based dataflow systems decouple timeliness and integrity?
**Answer:**
When processing streams asynchronously, there is no guarantee of timeliness unless consumers explicitly wait for a message to arrive before returning, effectively decoupling the integrity of the stream processing from the real-time delivery guarantees (timeliness).

#### 7. How do you enrich streaming user activity events with profile information from a remote user database without querying it directly during stream processing?
**Answer:**
Load a local copy of the database into the stream processor so it can be queried with low latency. Keep this local database up to date asynchronously using Change Data Capture (CDC).

#### 8. How do you implement a stream processor that calculates search result click-through rate (CTR) by correlating search query events and click events within a time window?
**Answer:**
Maintain state in the stream processor (e.g., all events from the last hour indexed by session ID). When a search or click event arrives, add it to its index and check the complementary index for a match. Emit a click-through event if a match is found, or an unclicked result event if the search event expires without a matching click.

#### 9. How is the slowly changing dimension (SCD) problem solved in stream processing joins?
**Answer:**
By using a unique identifier for a specific version of a joined record. This makes the stream join deterministic, though it prevents log compaction from being safely used on that stream.

#### 10. What architectural advantage is gained by separating mutable state from the immutable event log?
**Answer:**
It allows you to derive several different read-oriented representations from the same log of events, functioning similarly to multiple consumers of a stream.

#### 11. What are exactly-once semantics, and what mechanism is usually required to achieve them?
**Answer:**
Exactly-once semantics mean the final effect of a computation is the same as if no faults had occurred. This usually requires idempotent operations or transaction coordination.

#### 12. What are three key differences between message-passing actor models and stream processing?
**Answer:**
1. Actor frameworks are primarily for managing concurrency, whereas stream processing is for data management.
2. Communication between actors is one-to-one and ephemeral vs. durable and multi-subscriber in streams.
3. Actors can communicate in arbitrary (including cyclic) ways vs. acyclic pipelines for stream processing.

#### 13. What are two examples of extending stream processing ideas out of the datacenter to end-user devices?
**Answer:**
1. Using the read path to fetch an initial state, then relying on a stream of state changes sent by the server.
2. Using consumer offsets to resume processing and catch up after being offline.

#### 14. What is a slowly changing dimension (SCD) in the context of stream processing?
**Answer:**
A slowly changing dimension refers to a time-dependent relationship where a stream event needs to be enriched or joined with dimension data that changes slowly over time, requiring temporal joins.

#### 15. What is a stream-stream join in stream processing?
**Answer:**
A stream-stream join involves two input streams consisting of activity events where the join operator searches for related events occurring within a specific sliding or tumbling time window (e.g., matching two actions by the same user within 30 minutes). This can also be performed as a self-join on a single stream.

#### 16. What is the Lambda architecture in data processing?
**Answer:**
A hybrid design that combines batch and stream processing: a stream processor consumes events to quickly produce approximate updates to a view, while a batch processor later consumes the same events to produce a corrected, authoritative version of the derived view.

#### 17. What is the problem called when an event stream must be joined with a slowly changing dimension (SCD) table whose records occasionally change, and how is it solved?
**Answer:**
This is known as a Slowly Changing Dimension (SCD) join problem. It is solved by using a unique identifier for a particular version of the joined record to make the join deterministic, though this typically prevents effective log compaction.

#### 18. Why does windowing by processing time in stream processing introduce metrics artifacts?
**Answer:**
Variations in processing rate cause artifacts. For example, if a stream processor is redeployed and shut down for a minute, processing the resulting backlog upon restart causes a sudden, anomalous spike in metrics if measured by processing time, even though the actual event rate was steady.


## 📂 Category: Stream Processing & Batch Processing (1 cards)

### 🔴 Senior Level

#### 1. How do dataflow engines handle intermediate state materialization and fault recovery compared to traditional MapReduce?
**Answer:**
Dataflow engines (like Apache Spark) perform less materialization of intermediate state to disk, keeping more data in memory across flexible operator chains instead of strict alternating map/reduce phases. Because less state is materialized, they must recompute more data from lineage if a node fails. Deterministic operators are used to minimize the amount of data that needs to be recomputed upon failure.


## 📂 Category: Stream Processing & CDC (1 cards)

### 🟡 Mid Level

#### 1. What is the biggest architectural downside of event sourcing and Change Data Capture (CDC)?
**Answer:**
Because event log consumers are typically asynchronous, clients suffer from replication lag, meaning they may not be able to 'read their own writes' immediately due to race conditions.


## 📂 Category: Stream Processing & Change Data Capture (1 cards)

### 🟡 Mid Level

#### 1. How can derived data systems like search indexes, caches, and analytics systems be kept continually up-to-date?
**Answer:**
By consuming the log of changes (change data capture or event logs) from the primary data store and applying them sequentially to the derived data system.


## 📂 Category: Stream Processing & Derived Data (5 cards)

### 🟢 Junior Level

#### 1. Which programming paradigm or data structure typically lacks native reactive change notification streams compared to modern databases?
**Answer:**
Traditional spreadsheets and simple variables, where readers are not automatically notified of value mutations unless change-stream abstractions are explicitly implemented.


### 🟡 Mid Level

#### 1. What is another common industry term for a table-table join in the context of stream processing and derived data?
**Answer:**
Materialized view maintenance.


### 🔴 Senior Level

#### 1. How do table-table joins operate in log-structured stream processing systems?
**Answer:**
Both input streams are treated as database changelogs. Every change on one side is joined with the latest state of the other side, producing an output stream of changes to the materialized view of the join between the two tables.

#### 2. What is the "database inside-out" approach in modern distributed data architectures?
**Answer:**
It is the unbundling of traditional monolithic databases by composing specialized storage, messaging, and stream processing systems to maintain derived datasets (such as caches, full-text search indexes, and ML models) from a primary changelog.

#### 3. What key features must stream processing and messaging systems provide to successfully unbundle databases and maintain derived datasets like secondary indexes?
**Answer:**
1. Stable message ordering per partition or key.
2. Fault tolerance guaranteeing at-least-once or exactly-once processing without lost messages.


## 📂 Category: Stream Processing & Event Sourcing (12 cards)

### 🟢 Junior Level

#### 1. In message queue architectures, what does the 'fan-out' pattern describe?
**Answer:**
Delivering each published message to multiple consumers or subscriber queues independently.

#### 2. In message queue architectures, what does the load-balancing pattern describe?
**Answer:**
Sharing the work of consuming a message topic among a pool of competing consumer instances so each message is processed only once by the group.


### 🟡 Mid Level

#### 1. How can writes to a database be conceptualized, and how is this history captured?
**Answer:**
Writes can be viewed as a stream: we can capture the changelog—i.e., the history of all changes made to a database—either implicitly through change data capture (CDC) or explicitly through event sourcing.

#### 2. How can you ensure an operation is end-to-end idempotent across browser requests and databases?
**Answer:**
Generate a unique identifier (e.g., UUID) or calculate a hash of all fields to derive an operation ID. Pass the operation ID through to the database and use a uniqueness constraint on the operation ID column to ensure it is only executed once.

#### 3. How can you make a non-naturally idempotent operation idempotent (e.g., in Kafka)?
**Answer:**
In Kafka, every message has a monotonically increasing offset. Including that offset in a write to an external database can tell you whether an update has already been applied.

#### 4. How do protocols like Server-Sent Events (SSE) and WebSockets relate to stream processing?
**Answer:**
Actively pushing state changes all the way to client devices extends the write path to the end user. Stream processing paradigms can thus be extended beyond the datacenter straight to end-user devices.

#### 5. What is the primary advantage of using an asynchronous event log with idempotent writes to keep multiple storage systems in sync?
**Answer:**
Loose coupling between services and systems, allowing them to evolve independently while maintaining eventual consistency.


### 🔴 Senior Level

#### 1. How can you implement linearizability using typically asynchronous stream processors?
**Answer:**
A client can wait for a message to appear on an output stream.

#### 2. How do atomic commits apply in a stream processing context to guarantee exactly-once processing?
**Answer:**
All outputs and side effects of processing an event (downstream messages, DB writes, external emails/push notifications, incoming message ACKs) take effect if and only if processing succeeds. These must happen atomically or not at all.

#### 3. What architectural pattern is represented by storing the event 'student cancelled their course enrollment' instead of side effects like deleting a row from the enrollments table and adding to feedback?
**Answer:**
Event Sourcing. This records user intent and state changes as immutable domain events rather than mutating current-state tables destructively.

#### 4. What potential benefit does representing read requests as a stream of events provide?
**Answer:**
It allows you to record, replay, and reconstruct historical system states (such as what a user observed at a specific time) for auditing and analytics purposes.

#### 5. Why is log compaction not possible in event sourcing the way it is in CDC?
**Answer:**
Because later events do not necessarily override earlier events (unlike database mutations in CDC), and events in event sourcing are modeled at a higher business domain level.


## 📂 Category: Stream Processing & Message Brokers (4 cards)

### 🟢 Junior Level

#### 1. What are Apache Kafka and Amazon Kinesis, and what are their primary architectural characteristics?
**Answer:**
They are log-based message brokers capable of achieving massive throughput (millions of messages per second) and fault tolerance via distributed replication.


### 🟡 Mid Level

#### 1. What three properties would lead you to choose a log-based message broker over a JMS/AMQP style message broker?
**Answer:**
1. High message throughput.
2. Each message is fast to process.
3. Message ordering is important.
(Log-based brokers use a circular or ring buffer limited by disk space, whereas JMS/AMQP brokers are preferred when messages are expensive to process, require parallelization on a message-by-message basis, and ordering is not important.)


### 🔴 Senior Level

#### 1. What three timestamps should you log to adjust for event time from a user-controlled device in a stream processing environment?
**Answer:**
1. The time at which the event occurred, according to the device clock.
2. The time at which the event was sent to the server, according to the device clock.
3. The time at which the event was received by the server, according to the server clock.

#### 2. What types of streaming joins are needed to maintain a user's Twitter timeline cache versus calculating search result click-through rates?
**Answer:**
- Twitter timeline cache: A table-table join of tweets and follows.
- Search result click-through rates: A stream-stream join (window join).


## 📂 Category: Stream Processing & Messaging (10 cards)

### 🟢 Junior Level

#### 1. What is a message broker (also known as a message queue)?
**Answer:**
A specialized database optimized for message streams. It acts as a server where producers write messages and consumers receive them.

#### 2. What is a messaging system, and what are its primary components regarding producers, topics, and consumers?
**Answer:**
A messaging system is an approach for notifying consumers about new events, allowing multiple producer nodes to send messages to the same topic and allowing multiple consumer nodes to receive messages from that topic.

#### 3. What is an acknowledgement in the context of message brokers?
**Answer:**
An explicit signal sent by a client to the message broker confirming that a message has been fully processed, allowing the broker to safely remove it from the queue.


### 🟡 Mid Level

#### 1. How does a log-based stream processor handle conflicting operations?
**Answer:**
A log-based stream processor can deterministically decide which of several conflicting operations came first based on their strict ordering within the log partition.

#### 2. What are the two architectural types of message brokers?
**Answer:**
- AMQP/JMS-style message broker
- Log-based message broker

#### 3. What are the two fundamental questions to ask about pub-sub and messaging systems?
**Answer:**
1. What happens if the producers send messages faster than the consumers can process them?
2. What happens if nodes crash or temporarily go offline - are any messages lost?

#### 4. What are the two main consumption patterns for message queues with multiple consumers on the same topic?
**Answer:**
Load balancing: send message to 1 consumer
Fan-out: send message to all consumers

#### 5. What is a stream-stream join also known as?
**Answer:**
A window join.


### 🔴 Senior Level

#### 1. What are the two ways to deal with straggler events in a stream processor?
**Answer:**
1. Ignore straggler events, as they are likely a small percentage of events (track and alert on dropped event metrics).
2. Publish a correction: an updated value for the window with stragglers included.

#### 2. What delivery guarantee does a log provide to consumers, and what is its equivalence in distributed systems?
**Answer:**
A log ensures that all consumers see messages in the exact same order—a guarantee known as total order broadcast, which is equivalent to consensus.


## 📂 Category: System Architecture (2 cards)

### 🟡 Mid Level

#### 1. What is a derived data system?
**Answer:**
A secondary data system built by transforming, indexing, or processing data from an authoritative source of truth. Examples include caches, search indexes, denormalized views, and materialized views.

#### 2. When pushing real-time state changes to a client via protocols like WebSockets, how does this impact the write and read paths?
**Answer:**
It extends the write path all the way to the end user.


## 📂 Category: System Architecture & Performance (2 cards)

### 🟡 Mid Level

#### 1. Why is it important to measure response times on the client rather than server-side latency alone, and what phenomenon does this reveal?
**Answer:**
Client-side metrics capture queueing delays and head-of-line blocking. Head-of-line blocking occurs when a small number of slow requests hold up subsequent requests, causing clients to experience high overall response times despite fast server-side processing.


### 🔴 Senior Level

#### 1. What defines a hard real-time system, and what system-level requirements are needed to provide these timing guarantees?
**Answer:**
Hard real-time systems have strict deadlines by which software must respond; missing a deadline causes total system failure. Requirements include a real-time operating system (RTOS) with guaranteed CPU time allocation, documented worst-case execution times for libraries, restricted or disallowed dynamic memory allocation, and extensive testing.


## 📂 Category: System Architecture & Scalability (1 cards)

### 🟢 Junior Level

#### 1. How can we describe load on our system to discuss growth questions (e.g., 'what happens if our load doubles?')?
**Answer:**
Load can be described with load parameters. The best choice depends on system architecture: requests per second to a web server, read-to-write ratio in a database, active chat users, cache hit rate, etc. Focus may be on the average case or extreme bottleneck cases.


## 📂 Category: Time, Clocks & Ordering (1 cards)

### 🟡 Mid Level

#### 1. What are the typical clock drift characteristics of imprecise quartz clocks when synchronized via local network NTP versus public internet NTP?
**Answer:**
With local network NTP synchronization every minute, clock drift can easily reach several milliseconds. With public internet NTP servers, the best possible accuracy is typically limited to tens of milliseconds, which can easily spike to over 100 ms during periods of network congestion.


## 📂 Category: Transactions (22 cards)

### 🟢 Junior Level

#### 1. How do relational databases versus non-relational databases group operations into transactions?
**Answer:**
Relational databases use client TCP connections where everything between BEGIN TRANSACTION and COMMIT belongs to the same transaction. Many non-relational databases lack transaction semantics, so even multi-put APIs may partially succeed and fail.

#### 2. In many relational and transactional databases, a transaction is tied directly to which client networking construct?
**Answer:**
A TCP connection.

#### 3. T/F: In OLTP applications, a database transaction typically spans multiple HTTP requests.
**Answer:**
False. Almost all OLTP applications keep transactions short to avoid waiting idly for user input. A transaction is committed within the same HTTP request, and a new HTTP request initiates a new transaction.

#### 4. What do the letters in ACID stand for?
**Answer:**
Atomicity, Consistency, Isolation, and Durability.

#### 5. What does Isolation mean in the context of ACID transactions?
**Answer:**
Concurrently executing transactions are isolated from each other to prevent race conditions and ensure that the end result mimics serial execution.


### 🟡 Mid Level

#### 1. Are serializable isolation and good database performance fundamentally at odds with each other?
**Answer:**
Not necessarily. Serializable Snapshot Isolation (SSI) provides full serializability with only a small performance penalty compared to snapshot isolation by using an optimistic concurrency control approach to detect serialization conflicts.

#### 2. Do popular ORM frameworks like ActiveRecord and Django automatically retry aborted transactions?
**Answer:**
False. Most popular ORM frameworks do not retry aborted transactions; instead, they bubble up exceptions, discard user input, and return error messages. Safe retries must be implemented explicitly by the application.

#### 3. Does using a data system with strong safety properties like serializable transactions guarantee absolute freedom from data loss or corruption?
**Answer:**
No. Application-level bugs, hardware failures outside the database scope, misconfigurations, or operator errors can still cause data loss or corruption even if the database provides strong safety guarantees.

#### 4. How are dirty reads prevented under Read Committed isolation?
**Answer:**
Dirty reads are prevented by returning the old committed value to other transactions reading the object, rather than using locks.

#### 5. How are dirty writes prevented under Read Committed isolation?
**Answer:**
Dirty writes are prevented using exclusive locks: a transaction holds a lock from start to commit/abort for each modified object so only one transaction can hold it.

#### 6. How is atomicity implemented on a single node by the storage engine?
**Answer:**
Atomicity is implemented by writing a commit record to disk. Even if the node crashes, if the commit record was successfully written and flushed to disk, the transaction is considered persistent and successful.

#### 7. In the context of ACID, what does the 'C' (Consistency) actually refer to?
**Answer:**
Consistency refers to an application-specific notion of the database being in a 'good state' satisfying specific invariants. Atomicity, isolation, and durability are properties of the database, whereas consistency is a property of the application.

#### 8. What does Serializable isolation guarantee?
**Answer:**
It guarantees that even though transactions may execute in parallel, the final state and effects are identical to executing them completely serially, one at a time.

#### 9. What is a stored procedure and what benefit does it provide?
**Answer:**
A stored procedure encapsulates transaction logic directly inside the database engine, avoiding the overhead of network roundtrips between application code and the database for multi-statement transactions.

#### 10. What is serializability in the context of database transactions?
**Answer:**
Serializability is an isolation property ensuring that multiple transactions operating concurrently across multiple objects behave exactly as if they were executed in some strict serial order, preventing anomalies.

#### 11. What is the definition of Isolation in ACID, and how is it traditionally formalized?
**Answer:**
ACID isolation means that concurrently executing transactions are isolated from each other and cannot step on each other's toes. Classical database textbooks formalize this as serializability, ensuring the result is identical to running transactions serially, though true serializability is rarely used in practice due to performance penalties.


### 🔴 Senior Level

#### 1. How can a database prevent lost updates without atomic operations or explicit locking?
**Answer:**
By automatically detecting lost updates (e.g., via Serializable Snapshot Isolation), aborting the affected transaction, and forcing a retry.

#### 2. How do ACID transactions encompass both facets of consistency?
**Answer:**
In DDIA terminology, ACID transactions provide two distinct features under the umbrella of 'consistency': (1) Timeliness/State constraints (e.g., linearizability, invariants maintained) and (2) Integrity (e.g., atomic commit, constraint enforcement).

#### 3. How do databases commonly prevent dirty writes and dirty reads under Read Committed isolation?
**Answer:**
Dirty writes are typically prevented using row-level write locks that must be held until the transaction commits or aborts. Dirty reads are usually prevented using multi-versioning (storing both the old committed value and the new uncommitted value) rather than read locks, ensuring that concurrent readers are served the older committed value and avoiding read-write lock contention.

#### 4. How does Serializable Snapshot Isolation (SSI) detect write skew and dependency anomalies?
**Answer:**
SSI detects when a transaction reads outdated values from an MVCC snapshot (anti-dependencies) or when one transaction modifies data that another concurrent transaction has previously read.

#### 5. What is a phantom read, and how does it relate to write skew and serializability?
**Answer:**
A phantom read occurs when a transaction reads objects matching a search condition, and another client makes a write that inserts, updates, or deletes objects affecting those search results. While snapshot isolation prevents straightforward phantoms for already-read data, phantoms causing write skew (e.g., meeting room double-booking) require index-range locks, materialized conflicts, or full serializable isolation (SSI).

#### 6. What is the last resort approach to avoid phantoms causing write skew when range locks are unavailable?
**Answer:**
Materializing conflicts by explicitly creating placeholder rows in a table to lock against.


## 📂 Category: Transactions & Concurrency (13 cards)

### 🟢 Junior Level

#### 1. What does the ACID property of atomicity ensure during a transaction failure?
**Answer:**
Atomicity ensures that if an error occurs, any prior writes from that transaction are undone/aborted to avoid leaving the database in an inconsistent state.

#### 2. What does weak (nonserializable) isolation protect against?
**Answer:**
Some specific concurrency anomalies (like dirty reads or non-repeatable reads depending on the level), but it does not protect against all concurrency issues (such as write skew or lost updates).

#### 3. What is a database transaction?
**Answer:**
An abstraction that groups multiple reads and writes into a logical unit of execution with ACID guarantees: either all operations succeed (commit) or the entire transaction is rolled back (abort).

#### 4. Why do we need multi-object transactions in Relational and Graph Databases?
**Answer:**
In Relational DBs, foreign key references must remain valid when inserting multiple related records. In Graph DBs, multi-object transactions ensure consistency when mutating multiple connected edges and vertices simultaneously.


### 🟡 Mid Level

#### 1. If two transactions run a read-modify-write cycle concurrently, what can happen to the updates?
**Answer:**
The later write can clobber the earlier write, resulting in a lost update anomaly.

#### 2. What is a compare-and-set (CAS) operation?
**Answer:**
A concurrency control primitive that prevents lost updates by allowing a write to succeed only if the target data's value matches the value previously read. If it does not match, the write fails and the read-modify-write cycle must be retried.

#### 3. Where must the data live in order for single-threaded serial execution to be viable?
**Answer:**
In memory.

#### 4. Why do not all databases implement Serializable isolation by default?
**Answer:**
Serializable isolation carries a significant performance cost (due to blocking, aborts, or coordination overhead), so systems often trade safety for speed using weaker isolation levels.

#### 5. Why is 'Consistency' best viewed as a property of the application rather than the database?
**Answer:**
Maintaining business invariants and domain rules is ultimately the responsibility of the application logic, which utilizes database constraints and transactions as tools to enforce them.


### 🔴 Senior Level

#### 1. If serializable isolation cannot be used, how can you handle phantoms that cause write skew?
**Answer:**
By materializing conflicts, which explicitly creates lockable database rows to represent the phantom search space.

#### 2. What is the standard 3-step pattern that all phantoms follow when causing write skew?
**Answer:**
1. A SELECT query checks if a requirement is satisfied by searching for rows matching a condition.
2. The application decides whether to proceed based on the query result.
3. The application executes a write (INSERT/UPDATE/DELETE) that alters the precondition. (Note: Steps can occur in different orders, and SELECT FOR UPDATE cannot lock non-existent rows).

#### 3. Why do most databases implement index-range locking instead of explicit predicate locks?
**Answer:**
For performance reasons. Predicate locks are computationally expensive to check against all existing locks and writes, whereas index-range locks simplify the conflict-detection overhead.

#### 4. Why doesn't an atomic single-object operation prevent write skew?
**Answer:**
Write skew involves multiple distinct objects being read and conditionally updated based on each other; single-object atomicity only protects one object at a time.


## 📂 Category: Transactions & Concurrency Control (97 cards)

### 🟢 Junior Level

#### 1. How can isolation be implemented for a single object on a single node?
**Answer:**
Isolation can be implemented using a lock on each object so only one thread can access an object at a time.

#### 2. How is a database transaction generally defined?
**Answer:**
A transaction is a mechanism for grouping multiple operations on multiple objects into one single unit of execution.

#### 3. In what common scenarios do lost updates occur?
**Answer:**
1. Incrementing a counter or updating an account balance (read-modify-write cycle).
2. Making a local change to a complex nested structure, such as adding an element to a list inside a JSON document.
3. Concurrent editing of a document or wiki page where users submit the entire payload, overwriting concurrent modifications.

#### 4. True or False: Read Committed and Snapshot Isolation primarily guarantee what concurrently writing transactions can see.
**Answer:**
False. These isolation levels primarily guarantee what a read-only transaction can see in the presence of concurrent writes. They do not prevent write-write conflicts like the lost update problem, which occur during read-modify-write cycles.

#### 5. What ACID property does a 'dirty read' violate, and what is its definition?
**Answer:**
It violates Isolation. A dirty read occurs when one transaction reads data that has been written by another concurrent transaction, but that write has not yet been committed.

#### 6. What abstraction layer do database transactions provide to applications, and how do they handle unrecoverable faults?
**Answer:**
Transactions act as an abstraction layer allowing applications to pretend that certain concurrency problems and hardware/software faults do not exist. A large class of errors is reduced down to a simple transaction abort, requiring the application to simply retry.

#### 7. What are multi-object transactions needed for?
**Answer:**
Keeping multiple pieces of data in sync.

#### 8. What are the two core data guarantees provided by the 'Read Committed' transaction isolation level?
**Answer:**
1. No dirty reads: When reading from the database, you will only see data that has been committed.
2. No dirty writes: When writing to the database, you will only overwrite data that has been committed.

#### 9. What are the two most basic levels of transaction isolation?
**Answer:**
1. Read uncommitted: No dirty writes allowed.
2. Read committed: No dirty writes and no dirty reads allowed.

#### 10. What benefit do the safety guarantees of Transactions provide to applications?
**Answer:**
Transactions allow you to simplify the programming model for applications accessing a database by hiding potential faults and concurrency issues.

#### 11. What concurrency anomaly occurs when two transactions execute a read-modify-write cycle concurrently, causing the later write to overwrite the updates of the earlier write?
**Answer:**
A lost update anomaly.

#### 12. What do atomicity and isolation describe in the context of database transactions regarding a client's writes?
**Answer:**
Atomicity and isolation describe what the database should do if a client makes several writes within the same transaction (atomicity grouping them together, and isolation ensuring they are hidden from or safely exposed to concurrent transactions).

#### 13. What does Atomicity mean in the context of ACID transactions?
**Answer:**
When making several writes grouped into an atomic transaction, if the transaction cannot commit due to a fault, it must be aborted and the database must discard or undo any writes made so far, allowing the operation to be safely retried.

#### 14. What does Durability mean in the context of ACID, and how does its implementation differ between single-node and replicated databases?
**Answer:**
Durability guarantees that once a transaction successfully commits, its writes will not be lost. In a single-node database, this means data is successfully flushed to non-volatile storage (disk/SSD). In a replicated database, it means the update has been successfully copied to a required quorum of nodes.

#### 15. What is a dirty read in database transactions, and how is it prevented?
**Answer:**
A dirty read occurs when one client reads another client's uncommitted writes. The Read Committed isolation level and stronger isolation levels prevent dirty reads.

#### 16. What is a dirty write in database transactions?
**Answer:**
A dirty write occurs when one client overwrites data that another client has written but not yet committed. Almost all transaction implementations prevent dirty writes to avoid data corruption.

#### 17. What is a dirty write?
**Answer:**
A dirty write is when an uncommitted value from part of an earlier transaction is overwritten by a write from a later transaction.

#### 18. What is a read-modify-write cycle?
**Answer:**
An application pattern where a transaction reads a value from the database, computes an updated value in application memory, and writes the modified value back to the database.

#### 19. What is explicit locking, and what specific concurrency anomaly does it prevent?
**Answer:**
Explicit locking occurs when an application programmatically locks specific database objects prior to reading and updating them. This prevents lost updates by serializing access to those objects.

#### 20. What is the lost update problem?
**Answer:**
The lost update problem occurs when two or more transactions read the exact same value from the database, locally modify it, and write back the modified value, causing one transaction's write to silently clobber and overwrite the other's modifications.

#### 21. What is the most widely used algorithm for achieving serializability in traditional relational databases?
**Answer:**
Two-Phase Locking (2PL).

#### 22. What is the primary performance principle of snapshot isolation?
**Answer:**
Readers never block writers, and writers never block readers.

#### 23. What is the simplest way to completely avoid concurrency problems in database transactions?
**Answer:**
Avoid concurrency entirely by executing only one transaction at a time, sequentially in a single thread.

#### 24. When can two transactions lead to concurrency issues?
**Answer:**
If they touch the same data.

#### 25. Where does Serializable isolation rank in terms of transaction isolation levels?
**Answer:**
Serializable isolation is the strongest isolation level provided by databases.

#### 26. Which isolation levels prevent dirty reads?
**Answer:**
Read Committed and all stronger isolation levels (e.g., Repeatable Read, Snapshot Isolation, Serializable) prevent dirty reads.


### 🟡 Mid Level

#### 1. A user reads an email and marks it as read, but the global unread count badge still shows the old count temporarily. What concurrency anomaly is this, and what isolation level prevents it?
**Answer:**
This is an example of a dirty read. It is prevented by Read Committed isolation.

#### 2. How do many relational databases know that several queries belong to the same transaction?
**Answer:**
They are executed over the same TCP connection.

#### 3. Is two-phase locking (2PL) an optimistic or pessimistic concurrency control mechanism, and how does it behave under contention?
**Answer:**
Two-phase locking is a pessimistic concurrency control mechanism: if anything might go wrong (e.g., a lock conflict), it forces transactions to wait until the situation is safe again.

#### 4. List widely used database isolation levels in order of increasing strength, and specify the primary race conditions they prevent.
**Answer:**
1. Read Committed: Prevents dirty reads and dirty writes.
2. Snapshot Isolation (Repeatable Read variant): Prevents read skew (non-repeatable reads) and some lost updates (often via MVCC).
3. Serializable: Prevents write skew, phantom reads, and all concurrency anomalies.

#### 5. True or False: The race condition between two concurrent counter increments (where T2 reads the value before T1 commits its write, and both write back incremented values) is an example of a dirty write.
**Answer:**
False. This is an example of a lost update. Read Committed isolation does not prevent concurrent counter increments. Since the second write happens after the first transaction commits, it is not a dirty write (which involves overwriting uncommitted data), but rather a read-modify-write conflict.

#### 6. What 2 long-running operations require snapshot isolation because read-committed isolation causes severe data anomalies?
**Answer:**
1. Backups: Making a consistent copy of a database while writes are continuously occurring.
2. Analytic queries and periodic integrity checks: Scanning large portions of the database and expecting a coherent point-in-time view rather than a mixed jumble of old and new data.

#### 7. What are common business logic examples that share the same underlying race condition challenges as uniqueness constraints?
**Answer:**
Examples include not selling more items than are currently in stock (inventory limits) or preventing the booking of overlapping meetings in the same room.

#### 8. What are five examples of write skew, and how is the first example (updating an on-call schedule) different from the subsequent four?
**Answer:**
The latter four examples (meeting room booking, multiplayer game, changing a username, preventing double-spending) check for the absence of rows matching a search condition and then add a row matching that same condition. The first example (updating an on-call schedule) differs by evaluating aggregate counts (e.g., ensuring at least 2 doctors remain on call) where concurrent transactions modify overlapping subsets without realizing another transaction is removing a resource.

#### 9. What are the roles of the database versus the application regarding ACID properties, and why is the letter 'C' often considered a misnomer?
**Answer:**
Atomicity, isolation, and durability are properties of the database engine, whereas consistency is a property of the application. The application relies on the database's atomicity and isolation features to maintain its domain-specific invariants (consistency), meaning the letter 'C' doesn't truly describe a database feature.

#### 10. What are the two primary reasons why preventing dirty reads is important?
**Answer:**
- Another transaction sees some object updates, but not others.
- A transaction sees a write that is later rolled back.

#### 11. What are three key examples demonstrating a need for multi-object transactions?
**Answer:**
1. Relational data models: Maintaining foreign key references across multiple tables when inserting or deleting related rows.
2. Document models: Updating denormalized information scattered across multiple documents to prevent data drift.
3. Secondary indexes: Updating separate index objects atomically alongside base records to avoid partial indexing states.

#### 12. What are two methods to prevent prolonged transaction runtime caused by network round-trips between the application and the database in interactive client/server transactions?
**Answer:**
1. Run transactions concurrently using database isolation levels so waiting on one application query does not block the entire database.
2. Submit the entire transaction code to the database ahead of time as a stored procedure to execute entirely in memory without network or disk I/O wait states.

#### 13. What concurrency anomaly does a compare-and-set (CAS) operation avoid?
**Answer:**
Lost update problem

#### 14. What database anomaly occurs when a write in one transaction changes the result set of a search query in another concurrent transaction?
**Answer:**
A phantom read.

#### 15. What does ACID describe and what are the practical implications of the term?
**Answer:**
ACID describes the safety guarantees provided by transactions (Atomicity, Consistency, Isolation, Durability). In practice, one database’s implementation of ACID does not equal another's due to ambiguity (especially around isolation). Today, 'ACID compliant' has largely become a marketing term.

#### 16. What does Consistency mean in the context of ACID transactions?
**Answer:**
Consistency means that you have certain invariants about your data that must always be true. If a transaction starts in a valid state containing valid data, a consistent transaction preserves that validity.

#### 17. What does serializable isolation guarantee, and why do many systems opt for weaker isolation levels instead?
**Answer:**
Serializable isolation guarantees that concurrent transactions have the same net effect as if they ran serially (one at a time, completely isolated). Systems often use weaker isolation to avoid the significant performance costs associated with serializability, despite the risk of subtle concurrency bugs.

#### 18. What is Serializability in the context of database transactions?
**Answer:**
Serializability is an isolation property of transactions across multiple objects that guarantees transactions behave as if they were executed in some serial order.

#### 19. What is a dirty read, and what are two reasons why preventing it is useful?
**Answer:**
A dirty read occurs when a transaction sees another transaction's uncommitted data. Preventing it is useful because: 1) If a transaction updates multiple objects, a dirty read exposes a partially updated, confusing state. 2) If a transaction aborts and rolls back, any data seen by the dirty read becomes invalid and never actually committed to the database.

#### 20. What is a dirty write, how is it typically prevented, and what kind of concurrency issues does it avoid?
**Answer:**
A dirty write occurs when a later write overwrites an uncommitted value from an earlier, ongoing transaction. It is prevented by delaying the second write until the first transaction commits or aborts. It avoids issues such as multi-object update anomalies (e.g., a car sale listing won by one user while the invoice is sent to another).

#### 21. What is a non-repeatable read (aka read skew) and what is the most common solution?
**Answer:**
Read skew occurs when a transaction observes parts of the database at different points in time, returning inconsistent results even under read-committed isolation. Snapshot isolation is the most common solution.

#### 22. What is a nonrepeatable read (aka read skew), and under what isolation level can it occur?
**Answer:**
A nonrepeatable read (aka read skew) is a timing anomaly that occurs when observing parts of the database at different points in time returns nonsensical results, even with read-committed isolation.

#### 23. What is a read-modify-write cycle, and how does it lead to the lost update problem?
**Answer:**
A read-modify-write cycle occurs when an application reads a value from the database, modifies it in application memory, and writes the modified value back. If two transactions execute this concurrently, one modification can be lost because the second write does not include the first modification, effectively clobbering the earlier write.

#### 24. What is another major architectural reason for requiring multi-object transactions in relational databases besides complex business workflows?
**Answer:**
Secondary indexes. When values in a table change, any associated secondary indexes must be updated atomically alongside the primary record to prevent data skew and index inconsistency.

#### 25. What is generally regarded as the strongest isolation level, and what are its guarantees?
**Answer:**
Serializable isolation is the strongest level. It guarantees that even though transactions execute in parallel, the end result is indistinguishable from a purely serial (one-at-a-time) execution, preventing all concurrency race conditions.

#### 26. What is read skew (nonrepeatable reads), and how is it most commonly prevented?
**Answer:**
Read skew is when a client sees different parts of the database at different points in time. It is most commonly prevented using snapshot isolation, usually implemented via multi-version concurrency control (MVCC).

#### 27. What is read skew and what is its alternative name?
**Answer:**
Read skew occurs when a transaction reads data from different points in time, resulting in an inconsistent view (e.g., seeing an account balance update midway through). It is also known as a nonrepeatable read.

#### 28. What is snapshot isolation and how does it prevent read skew?
**Answer:**
Snapshot isolation ensures that each transaction reads from a consistent snapshot of the database taken at the start of the transaction, meaning it sees all data committed up to that point and ignores concurrent uncommitted or later-committed changes, preventing read skew.

#### 29. What is the 'lost updates' anomaly, and how can it be prevented?
**Answer:**
Lost updates occur when two clients concurrently perform a read-modify-write cycle, and one overwrites the other's write without incorporating its changes, causing data loss. Some implementations of snapshot isolation prevent this automatically, while others require manual locking (e.g., SELECT FOR UPDATE).

#### 30. What is the definition of atomicity in general computing vs. ACID atomicity, and why is 'abortability' arguably a better term?
**Answer:**
In general, atomicity means an operation cannot be broken down into smaller parts (or viewed halfway). In ACID, atomicity describes what happens when a fault occurs mid-way through multiple writes: the transaction is aborted and all preceding writes are discarded/undone. 'Abortability' is a better term because the defining feature is the ability to abort on error and discard partial changes safely.

#### 31. What is the primary conceptual difference between transaction isolation and distributed consistency?
**Answer:**
Transaction isolation is primarily about avoiding race conditions due to concurrently executing transactions, whereas distributed consistency is mostly about coordinating the state of replicas in the face of network delays and faults.

#### 32. What is the primary purpose of Snapshot Isolation (Repeatable Read) in databases?
**Answer:**
Snapshot isolation allows small, fast read-write transactions and large, long-running read-only transactions (like backups or analytics) to run concurrently. It allows read-only transactions to see a consistent database state at a particular point in time without locking or interfering with read-write transactions.

#### 33. What mechanism prevents dirty writes across almost all modern transaction implementations?
**Answer:**
Exclusive locks on objects being written prevent two concurrent transactions from overwriting uncommitted data simultaneously (dirty writes).

#### 34. What problem does ACID atomicity simplify, and why might 'abortability' be a better term?
**Answer:**
Atomicity ensures that if a transaction aborts, all its writes are discarded, guaranteeing the application state remains unchanged so it can be safely retried without partial-write side effects. 'Abortability' is often considered a more descriptive term because the primary feature is the ability to abort and rollback on error.

#### 35. What transaction anomaly occurs when a user reads inconsistent data across multiple queries within the same transaction because another transaction modified the data in between?
**Answer:**
Read skew (non-repeatable read)

#### 36. What transaction isolation anomaly is demonstrated by a transaction overwriting uncommitted data written by another concurrent transaction?
**Answer:**
A dirty write.

#### 37. What two viewpoints regarding transactions in distributed databases are considered pure hyperbole?
**Answer:**
1. Transactions are the antithesis of scalability, and any large-scale system must abandon them for performance and availability.
2. Transactional guarantees are an absolute, essential requirement for any 'serious application' handling 'valuable data.'

#### 38. Which isolation level is required to prevent write skew?
**Answer:**
Only full Serializable isolation prevents write skew anomalies.

#### 39. Why is serializable isolation rarely used in practice, and what is typically used instead?
**Answer:**
Serializable isolation carries a heavy performance penalty due to strict coordination or abort/retry overhead. Snapshot isolation and other forms of weak isolation are used instead as a trade-off for higher throughput.


### 🔴 Senior Level

#### 1. Does perfect durability exist in database systems, and what risk-reduction techniques should be combined to mitigate data loss?
**Answer:**
Perfect durability does not exist due to firmware bugs, kernel issues, and hardware failures. Risk-reduction techniques that must be used together include writing to non-volatile storage (disk/SSD), replicating to remote nodes, and maintaining off-site backups.

#### 2. How can a query be used to implement Two-Phase Locking (2PL)?
**Answer:**
It could act as a predicate lock that matches the search condition.

#### 3. How do atomic operations and locks prevent lost updates, and what is the database-level alternative using transaction managers and automatic detection?
**Answer:**
Atomic operations and locks prevent lost updates by forcing read-modify-write cycles to happen sequentially. The alternative is to allow them to execute in parallel, and if the transaction manager detects a lost update, it aborts the transaction and forces it to retry the read-modify-write cycle. PostgreSQL, Oracle, and SQL Server automatically detect lost updates under repeatable read/snapshot isolation levels, whereas MySQL/InnoDB's repeatable read does not.

#### 4. How does Serializable Snapshot Isolation (SSI) achieve serializability without using heavy locking?
**Answer:**
SSI uses an optimistic concurrency control approach, allowing transactions to proceed concurrently without blocking. Upon commit, the transaction is validated for serializability anomalies (such as read-write conflicts); if an anomaly is detected, the transaction aborts.

#### 5. How does Serializable Snapshot Isolation (SSI) prevent serialization anomalies?
**Answer:**
SSI detects if a premise (a fact that was true earlier in the transaction) may no longer be up-to-date by the time the transaction commits or aborts.

#### 6. What are 5 solutions to the lost update problem, and what are their mechanisms or limitations?
**Answer:**
1. Atomic write operations: Avoid read-modify-write cycles using database-native increments or updates (e.g., UPDATE counters SET value = value + 1). Often implemented via exclusive locks or single-threaded execution.
2. Explicit locking: Explicitly lock objects to be updated (e.g., SELECT * FROM x WHERE ... FOR UPDATE) so concurrent read-modify-write cycles must wait.
3. Automatically detecting lost updates: Allow parallel execution, but have the transaction manager detect lost updates and abort/retry the offending transaction (supported by Snapshot Isolation in Postgres, Oracle, SQL Server, but not MySQL/InnoDB).
4. Compare-and-set: Allow an update only if the value has not changed since last read (e.g., UPDATE page SET content = 'new' WHERE id = 123 AND content = 'old'). Must be verified for safety against old snapshots.
5. Conflict resolution and replication: Used in multi-leader or leaderless replication where locks/CAS don't apply. Uses commutative data structures (like Riak CRDTs) or version/sibling merging. Last Write Wins (LWW) is prone to data loss.

#### 7. What are the 3 most common techniques databases use to provide serializable isolation?
**Answer:**
1. Actual serial execution (single-threaded execution loops, e.g., Redis, H-Store). 2. Two-phase locking (2PL). 3. Optimistic concurrency control techniques such asSerializable Snapshot Isolation (SSI).

#### 8. What are the 4 major constraints or operational limits of using single-threaded, serial execution of transactions to achieve serializable isolation?
**Answer:**
1. Every transaction must be small and fast (one slow transaction stalls all processing).
2. The active dataset must fit entirely in memory.
3. Write throughput must be low enough to be handled on a single CPU core.
4. Cross-partition transactions have a hard limit and introduce massive coordination overhead.

#### 9. What are the advantages and trade-offs of Serializable Snapshot Isolation (SSI) compared to Two-Phase Locking (2PL) and Snapshot Isolation?
**Answer:**
Compared to 2PL, SSI's major advantage is that transactions never block waiting for locks; readers don't block writers and vice versa, leading to predictable latencies. Compared to basic Snapshot Isolation, SSI automatically detects serialization conflicts (like write skew) and aborts conflicting transactions, incurring a small bookkeeping overhead and potential abort-rate tuning penalties.

#### 10. What are the downsides of predicate locks, and what is the standard alternative used by most databases implementing Two-Phase Locking (2PL)?
**Answer:**
Predicate locks perform poorly because checking for matching locks among many active transactions is very time-consuming. Most databases instead use index-range locks (next-key locking), attaching shared locks to index entries as a lower-overhead approximation.

#### 11. What are the key pitfalls and edge cases when retrying aborted transactions?
**Answer:**
1. Duplicate execution: If a transaction committed successfully but the network dropped the acknowledgment, retrying will execute it a second time unless application-level deduplication exists.
2. Feedback cycles / Cascading overloads: Retrying against an already overloaded system exacerbates resource exhaustion (mitigated by exponential backoff and jitter).
3. Non-transient errors: Retrying is pointless for permanent errors like constraint violations; it should be restricted to transient failures (deadlocks, isolation violations, failovers).
4. Side effects duplication: External side effects (e.g., sending an email) execute even if the database transaction aborts (solved via Two-Phase Commit / atomic commit).
5. Client failures: If the client process crashes during the retry loop, pending data writes are lost.

#### 12. What are the main problems with weak isolation levels, and what is the general recommendation to avoid them?
**Answer:**
1. Isolation levels are hard to understand and inconsistently implemented across different databases (e.g., 'repeatable read' varies).
2. It is difficult to statically determine if an application code path is safe from race conditions.
3. There are a lack of practical automated tools to detect race conditions.
Recommendation: Use serializable isolation to prevent all transaction anomalies.

#### 13. What are the primary strategies and solutions for preventing write skew?
**Answer:**
1. Use true serializable isolation (such as Serializable Snapshot Isolation - SSI), since weak snapshot isolation implementations do not automatically detect write skew.
2. Configure explicit multi-object database constraints (enforced via database features, triggers, or materialized views).
3. Explicitly lock dependent rows using locking reads (e.g., SELECT ... FOR UPDATE).

#### 14. What are the three core algorithmic approaches to implementing serializable transactions?
**Answer:**
1. Literally executing transactions in a serial order on a single thread.
2. Two-phase locking (2PL).
3. Serializable snapshot isolation (SSI).

#### 15. What concurrency issue can occur when a transaction checks a condition via a SELECT query, makes an application-level decision based on it, and then executes a write?
**Answer:**
Write skew.

#### 16. What is 'materializing conflicts' as a technique for handling write skew?
**Answer:**
A workaround for phantom reads or write skew where no matching rows exist to lock. The application artificially introduces lockable database objects—such as pre-allocating time slot rows for a meeting room booking system—so pessimistic concurrency control can lock them.

#### 17. What is Serializable Snapshot Isolation (SSI) in terms of concurrency control?
**Answer:**
SSI is an optimistic concurrency control mechanism where transactions continue instead of blocking, and the database checks for write conflicts or anomalies right before commit time.

#### 18. What is a 'premise' in the context of write skew and phantoms under snapshot isolation, and how does the database detect when a premise has changed?
**Answer:**
A premise is a fact that was true at the beginning of a transaction (e.g., 'There are currently two doctors on call'). Because snapshot isolation does not prevent transactions from reading query results that might be modified before commit, a write skew anomaly can occur if an action is taken based on an outdated premise. To provide serializable isolation, the database must detect when a premise has changed using two main mechanisms: 1) Detecting reads of a stale MVCC object version (where an uncommitted write occurred before the read), and 2) Detecting writes that affect prior reads (where the write occurs after the read).

#### 19. What is a phantom in database transactions, how can it be avoided in read-only queries, and what are two ways to handle it in read-write transactions?
**Answer:**
A phantom is an effect where a write in one transaction changes the result of a search query in another transaction. Phantoms can be avoided in read-only queries using snapshot isolation. In read-write transactions, we use a serializable isolation level or a materializing conflicts approach (as a last resort).

#### 20. What is a predicate lock and what problem does it solve?
**Answer:**
A predicate lock belongs to all objects that match a search condition (e.g., a WHERE clause). It applies even to objects that do not yet exist in the database, preventing phantoms and write skew to achieve serializable isolation.

#### 21. What is index-range locking in the context of Two-Phase Locking (2PL)?
**Answer:**
An efficient approximation of true predicate locks used in 2PL. Instead of locking a dynamic set of rows matching a query predicate, the database attaches the lock to an existing index or a range of index keys to prevent phantom reads.

#### 22. What is strict serializability (or strong one-copy serializability)?
**Answer:**
A database property providing both serializability and linearizability. Implementations based on Two-Phase Locking (2PL) or actual serial execution are typically linearizable, whereas Snapshot Isolation with Serializable Snapshot Isolation (SSI) is not linearizable by design.

#### 23. What is the 'materializing conflicts' approach to solving phantom write skew, why is it considered a last resort, and how does it apply to a meeting room schedule problem?
**Answer:**
Materializing conflicts takes a phantom (where no target row exists to lock) and artificially introduces a concrete lock object into the database. For example, in a meeting room booking system, you precreate rows for all combinations of rooms and time slots ahead of time, allowing transactions to use 'SELECT FOR UPDATE' to lock those specific time-slot rows. It is a last resort because it is error-prone to design and leaks database concurrency control mechanisms into the application data model.

#### 24. What is write skew and how does it happen?
**Answer:**
Write skew is a concurrency anomaly that can occur if two transactions read the same objects, evaluate some conditions, and then update mutually exclusive subsets of those objects (or different objects entirely). It is not a dirty read or lost update and typically requires Serializable Snapshot Isolation (SSI) or explicit locking (SELECT FOR UPDATE) to prevent.

#### 25. What is write skew, and how does it relate to the lost update problem?
**Answer:**
Write skew is a generalization of the lost update problem. It is an anomaly that can occur if two transactions read the same objects, and then update subsets of those objects based on the read data. In the special case where different transactions update the exact same object, it manifests as a dirty write or lost update anomaly depending on the timing.

#### 26. What is write skew, and which isolation level is required to prevent it?
**Answer:**
Write skew occurs when a transaction reads data, makes a business decision based on it, and writes a modification, but by the time the write completes, the underlying premise is no longer true. Only serializable isolation (or explicit constraints/locks) prevents this anomaly.

#### 27. What is write skew?
**Answer:**
A concurrency anomaly that occurs when two transactions read the same set of objects, make decisions based on those readings, and then update disjoint subsets of those objects (or different objects entirely) in a way that violates a global invariant or constraint.

#### 28. What isolation level prevents standard phantom reads, and what mechanism is required to prevent phantoms in the context of write skew?
**Answer:**
Snapshot isolation prevents standard phantom reads. However, phantoms that lead to write skew require special treatment, such as index-range locks or materialized conflicts.

#### 29. What level of isolation does Two-Phase Locking (2PL) provide, and what race conditions does it avoid?
**Answer:**
2PL provides full Serializability. It protects against all standard race conditions, including lost updates and write skew.

#### 30. What requirement must applications meet in order to execute transactions completely serially (single-threaded execution)?
**Answer:**
The application must submit the entire transaction code as a stored procedure rather than executing queries interactively over a network connection.

#### 31. Why is performance under Two-Phase Locking (2PL) significantly worse compared to weak isolation levels, and what are the primary concurrency/latency implications?
**Answer:**
Throughput and response times are significantly worse due to lock acquisition/release overhead and dramatically reduced concurrency. Transactions wait synchronously for conflicting locks to release. Because traditional relational DBs do not limit transaction duration (often waiting on interactive human input), queues can form quickly, causing highly unstable latencies at high percentiles (tail latency spikes). Additionally, deadlocks occur much more frequently under 2PL serializable isolation, causing transaction aborts and wasted CPU cycles on retries.

#### 32. Why is snapshot isolation often referred to as 'repeatable read' in databases like PostgreSQL and MySQL, and what causes this naming confusion?
**Answer:**
PostgreSQL and MySQL call snapshot isolation 'repeatable read' because the SQL standard (based on 1970s System R definitions) lacked the concept of snapshot isolation. By meeting the minimal criteria for the standard's 'repeatable read', they claim compliance. However, the SQL standard is famously ambiguous, and different DBs implement vastly different guarantees under these names.


## 📂 Category: Transactions & Consensus (2 cards)

### 🟡 Mid Level

#### 1. What is it called when nodes in a distributed system may exhibit arbitrary, malicious, or incorrect behavior (i.e., 'lying'), and what is the problem of reaching consensus in this environment called?
**Answer:**
This behavior is a 'Byzantine fault', and the problem of reaching consensus in this untrusting environment is known as the 'Byzantine Generals Problem'.


### 🔴 Senior Level

#### 1. In a Two-Phase Commit (2PC) protocol, what is the state of a client if it suffers a network interruption and times out after sending the COMMIT message but before receiving a response?
**Answer:**
The client does not know whether the transaction has ultimately committed or aborted, requiring external recovery mechanisms or inquiry into coordinator logs.

