# SQL & Database Study Guide - Senior Level

- **Total Cards**: 362

---

## 📂 Category: Advanced & Distributed Databases (33 cards)

### 🔴 Senior Level

#### 1. Advanced SQL Tips
**Answer:**
To use a composite set of variables with the IN operator, concatenate them (e.g., WHERE (col1, col2) IN ((val1, val2), ...)).

#### 2. How are XQuery and XSLT defined in relation to XPath?
**Answer:**
XQuery is defined as XPath + a full-featured compositional query language (SQL-like). XSLT is defined as XPath + transformations, commonly used for converting XML to HTML.

#### 3. How do NoSQL databases compare to traditional relational (RDBMS) systems?
**Answer:**
NoSQL generally offers more flexibility (less schema/preprocessing), higher scalability, and efficiency, but typically lacks the complex query expressivity and strict ACID guarantees of RDBMS.

#### 4. How do you simulate universal quantification ('for all') in XPath?
**Answer:**
You can simulate it using the count() built-in function to compare the count of matching nodes against the total number of nodes.

#### 5. How is existential quantification ("there exists") handled in XQuery?
**Answer:**
Existential quantification is expressed using the 'some' keyword: 'where some $var in $collection satisfies condition'. It returns true if at least one item in the sequence satisfies the specified condition.

#### 6. How is universal quantification expressed in XQuery?
**Answer:**
Universal quantification ("for all") is expressed by checking if every item in a sequence satisfies a specific condition.

#### 7. How many navigation axes exist in XPath?
**Answer:**
There are 13 navigation axes in XPath (e.g., child, parent, descendant, ancestor, etc.).

#### 8. What are the common drawbacks of using XSLT?
**Answer:**
1. Ambiguity resolution: Priority is given to the most specific rule or the latest defined rule. 2. Weird whitespace handling (e.g., entity escaping requirements).

#### 9. What are the core characteristics of NoSQL databases?
**Answer:**
Document stores hold semi-structured data; Key-Value stores map unique keys to values (often used for fast lookups); Graph databases represent data as nodes and edges; MapReduce is a programming model for processing massive datasets in parallel, though joins are not natively supported and often require higher-level abstractions like Hive or Pig.

#### 10. What are the primary motivations behind NoSQL databases?
**Answer:**
The main motivations are to handle massive data storage and querying scale by highly parallelizing operations, often sacrificing the strict consistency/ACID guarantees of traditional relational DBMS for higher performance or availability.

#### 11. What do the SQL Server internal engines (Apolon, Hekaton, Relation) do?
**Answer:**
Apolon handles columnstore indexes for data warehousing; Hekaton manages memory-optimized objects; the Relational Engine handles general query processing tasks.

#### 12. What does HIERARCHICALID.GetDescendant return?
**Answer:**
It returns a child HIERARCHICALID node that is lower than a specified child, or a valid node between two existing child nodes.

#### 13. What does the CAP theorem describe regarding distributed systems?
**Answer:**
The CAP theorem describes the fundamental trade-off between three properties: Consistency (every read receives the most recent write), Availability (every request receives a response), and Partition tolerance (system continues to operate despite network failures).

#### 14. What does the CAP theorem describe?
**Answer:**
The CAP theorem states that a distributed data store cannot simultaneously provide more than two out of three guarantees: Consistency (all nodes see the same data at the same time), Availability (every request receives a response), and Partition tolerance (the system continues to operate despite network failures).

#### 15. What is ETL?
**Answer:**
ETL stands for Extract, Transform, and Load. It is the process of extracting data from sources, converting it into a structured format for analysis, and loading it into a target data warehouse.

#### 16. What is NoSQL and its relation to traditional relational databases?
**Answer:**
NoSQL stands for 'Not Only SQL'. It provides an alternative to the relational model for specific use cases. It typically offers lower expressivity than relational DBMS but provides higher efficiency and horizontal scalability. A key advantage is flexibility, as it often avoids the strict data preprocessing required by relational schemas, focusing processing only on the data portions actually being queried.

#### 17. What is SQL Injection and how can you prevent it?
**Answer:**
SQL Injection is a vulnerability where malicious SQL code is inserted into input fields to manipulate database queries, potentially leading to unauthorized data access or deletion. Prevention is achieved by using parameterized queries (prepared statements), which ensure that user input is treated as data, not as executable code.

#### 18. What is a Data Cube (multidimensional OLAP)?
**Answer:**
A Data Cube is an OLAP structure where dimension data forms the axes of the cube and fact (dependent) data exists in the cells. It allows for efficient retrieval of aggregated data across various dimensions.

#### 19. What is a Decision Support System (DSS)?
**Answer:**
A system that assists enterprise-wide decision-making by data processing and manipulation of existing data sets with the help of specialized tools.

#### 20. What is a Decision Support System (DSS)?
**Answer:**
A Decision Support System is an infrastructure, typically a data warehouse tuned for OLAP (Online Analytical Processing) analysis, used to store and process data for business intelligence and decision-making.

#### 21. What is a fact in data modeling?
**Answer:**
A central component of a multi-dimensional model containing measures for analysis. Types include Additive, Semi-additive, and Non-additive facts.

#### 22. What is causality tracking?
**Answer:**
A technique where causally connected events are assigned identical identifiers to track the sequence or dependency of operations in distributed systems.

#### 23. What is data warehousing?
**Answer:**
A system optimized for reporting and analysis, characterized as subject-oriented, time-variant, non-volatile, and integrated.

#### 24. What is the advantage of XSD over DTD regarding pointers?
**Answer:**
XSD supports typed pointers (specifying the target element type for IDREFS), whereas DTDs only support untyped ID/IDREF references.

#### 25. What is the difference between OLAP and OLTP databases?
**Answer:**
OLAP (Online Analytical Processing) is designed for complex, large-scale analytical queries on historical data for business intelligence. OLTP (Online Transaction Processing) is designed for high-concurrency, near real-time transactional processing like banking or e-commerce.

#### 26. What is the difference between OLTP and OLAP?
**Answer:**
OLTP (Online Transaction Processing) is optimized for short, frequent transactions and simple queries on small data sets. OLAP (Online Analytical Processing) is optimized for long-running, complex analytical queries across large data volumes. Data warehousing often involves moving data from OLTP sources to an OLAP warehouse for analysis.

#### 27. What is the purpose of an XSLT template for recursive element copying?
**Answer:**
It provides a mechanism to recursively traverse and process XML nodes, allowing for structural transformation or reformatting of the XML document.

#### 28. What is the relative power of XQuery compared to XPath and XSLT?
**Answer:**
XQuery offers the most expressive power because it is a full-featured, compositional query language.

#### 29. What quantification does XPath use by default for attribute comparisons?
**Answer:**
XPath relies on implicit existential quantification ('there exists') when comparing attributes (e.g., [attribute = value]).

#### 30. What were the main types of NoSQL systems as of November 2011?
**Answer:**
Key types included: MapReduce frameworks (OLAP), Key-value stores (OLTP), Document stores, Graph databases, and Column stores.

#### 31. When designing an application, how do you decide between a NoSQL system and a relational DBMS regarding data consistency and scalability?
**Answer:**
Choose a traditional relational DBMS when strict data consistency and transaction serializability are required. Choose a NoSQL system when massive scalability and efficiency are prioritized over strict consistency, acknowledging that relational databases are also highly scalable but offer stronger guarantees.

#### 32. Why is querying XML considered less mature than SQL?
**Answer:**
Querying XML is considered less mature because it lacks a standard underlying formal algebra equivalent to relational algebra and is a newer technology compared to SQL.

#### 33. Why must the correct ROUTE be set on both sides of a Service Broker DIALOG?
**Answer:**
The route must be configured on both sides to allow the initiator to send the initial message and the receiver to send back the necessary acknowledgement.


## 📂 Category: Basic SQL & Syntax (1 cards)

### 🔴 Senior Level

#### 1. What are two common SQL Injection payloads that evaluate to 'Always True'?
**Answer:**
1=1 and ''=''. These are used to bypass authentication by making a WHERE clause always evaluate to true.


## 📂 Category: Database Design & Normalization (37 cards)

### 🔴 Senior Level

#### 1. Can subqueries be used in constraints?
**Answer:**
Subqueries are generally not allowed in check constraints because they can lead to non-deterministic behavior. They are however widely used within triggers and other procedural code.

#### 2. Compare the strictness of Fourth Normal Form (4NF) and Boyce-Codd Normal Form (BCNF).
**Answer:**
Fourth Normal Form (4NF) is stricter than Boyce-Codd Normal Form (BCNF). While BCNF deals with functional dependencies, 4NF addresses multi-valued dependencies.

#### 3. Define Boyce-Codd Normal Form (BCNF).
**Answer:**
A table is in BCNF when it consists of atomic attributes, each non-key attribute is fully dependent on a candidate key, no non-key attribute depends on another non-key attribute, and every determinant is a candidate key.

#### 4. Define fifth normal form (5NF).
**Answer:**
A table is in 5NF if it is in 4NF and the relation cannot be reconstructed from simpler relations by a join (i.e., it is non-reducible).

#### 5. Define fourth normal form (4NF).
**Answer:**
A table is in 4NF if it is in 3NF and contains no multiple independent sets of multivalued dependencies.

#### 6. Explain the 4NF and BCNF decomposition algorithms.
**Answer:**
Both algorithms decompose relations to remove redundancies. BCNF (Boyce-Codd Normal Form) ensures that for every functional dependency X -> Y, X is a superkey. 4NF addresses multi-valued dependencies where a table contains two or more independent multi-valued facts about an entity.

#### 7. How are A->>B and A->B read in database theory?
**Answer:**
A->B is read as 'A determines B'. A->>B is read as 'A multi-determines B'.

#### 8. How can you determine if a set of attributes A is a key for a relation R?
**Answer:**
Compute the attribute closure A+. If the resulting set includes all attributes in the relation R, then A is a key.

#### 9. How do you determine if a set of Functional Dependencies (FDs) S2 follows from S1?
**Answer:**
To check if S2 follows from S1, compute the attribute closure (A+) of the left-hand side of each dependency in S2 using the dependencies in S1. If the right-hand side attributes of the dependency in S2 are contained within the closure, then the dependency is implied by S1.

#### 10. How do you find all candidate keys given a set of functional dependencies (FDs)?
**Answer:**
Compute the closures of every subset of attributes in increasing size. If a subset is a superkey, any superset of it is also a superkey. This process also identifies all functional dependencies within the relation.

#### 11. How do you translate an association with 1..1 or 0..1 multiplicity into relations?
**Answer:**
When a 1..1 or 0..1 multiplicity exists, the key of the relation can be derived from the 'many' side of the association. We can either use a combined primary key or, preferably, transfer the primary key of the 'one' side to the 'many' side and remove the explicit association table.

#### 12. How is the NULL bitmap size calculated?
**Answer:**
It is 2 bytes plus 1 byte for every 8 nullable columns in the table.

#### 13. How large is the variable-length column array?
**Answer:**
It is 2 bytes plus 2 bytes for each variable-length column present.

#### 14. Is decomposing a relation into BCNF or 4NF always the best design choice?
**Answer:**
No. While higher normal forms reduce redundancy, they may induce excessive joins, which can be computationally expensive. The ideal design depends on the specific query workload and the trade-off between normalization and performance.

#### 15. Is the splitting rule valid for the left-hand side attributes of functional dependencies?
**Answer:**
No, the splitting rule (decomposition) applies only to the right-hand side of a functional dependency.

#### 16. What are the common strategies for translating UML subclasses into relations?
**Answer:**
1. Subclass relations contain superclass key + specialized attributes. 2. Subclass relations contain all attributes (including inherited ones). 3. One single relation containing all superclass and subclass attributes (using nulls for missing values).

#### 17. What are the core functions of a relational database as defined by Edgar Codd?
**Answer:**
These include non-redundant data management, CRUD operations, metadata catalogs, multi-user views, data consistency/integrity, security, transaction management, concurrency, and crash recovery.

#### 18. What are the rules for MVD (multi-valued dependencies)?
**Answer:**
The primary rule is the FD-is-an-MVD rule: every functional dependency (FD) is inherently an MVD, but not every MVD is an FD.

#### 19. What are trivial functional dependencies?
**Answer:**
If A->B and B is a subset of A, then the dependency is trivial. This implies A -> (A union B) and A -> (A intersect B).

#### 20. What defines a 'good' decomposition of a relation?
**Answer:**
A good decomposition is a set of tables that, when joined back together, produces the original data without loss of information; this is known as the lossless join property.

#### 21. What is 4th Normal Form (4NF) regarding Multivalued Dependencies (MVDs)?
**Answer:**
4NF requires that for every non-trivial MVD A ->> B, A must be a superkey. It is a specialization of BCNF that handles cases where one attribute is associated with a set of values.

#### 22. What is Relational Algebra?
**Answer:**
A formal mathematical definition and foundation of the relational model, providing a set of operations that act on relations (tables) to produce new relations.

#### 23. What is a deficiency of UML regarding object relationships?
**Answer:**
A slight deficiency of UML is that it can only capture at most one relationship between two objects (e.g., a student cannot apply to the same college twice for different majors using only standard association modeling).

#### 24. What is a multi-valued dependency (MVD)?
**Answer:**
A multi-valued dependency (MVD), or 'tuple-generating dependency', occurs when the presence of one or more rows in a table implies the presence of other rows to maintain consistency. If tuples (a, b, c) and (a, d, e) exist, (a, b, e) and (a, d, c) must also exist. MVDs identify data redundancy and are addressed during Fourth Normal Form (4NF) normalization.

#### 25. What is required to determine if a relational schema is in BCNF (Boyce-Codd Normal Form)?
**Answer:**
To determine BCNF compliance, you need the relational schema and the full set of functional dependencies.

#### 26. What is required to implement memory-optimized tables in SQL Server?
**Answer:**
You must create a Memory Optimized Filegroup and add a container of type Filestream to it.

#### 27. What is required when decomposing relations in BCNF or 4th Normal Form?
**Answer:**
It is necessary to calculate the closure of all functional dependencies and multivalued dependencies to ensure all dependencies are preserved and satisfied throughout the decomposition.

#### 28. What is the goal of a good database design regarding Functional Dependencies (FDs)?
**Answer:**
The goal is to obtain a minimal set of completely non-trivial Functional Dependencies such that all FDs of the relation follow from the dependencies in this set.

#### 29. What is the relationship between Functional Dependency (FD) and Multivalued Dependency (MVD)?
**Answer:**
A Functional Dependency is always a Multivalued Dependency (but the inverse is not necessarily true). This is known as the FD-is-an-MVD rule.

#### 30. What is the relationship between multi-valued dependencies and fourth normal form (4NF)?
**Answer:**
Multi-valued dependencies are often called tuple-generating dependencies. 4NF is stricter than BCNF, specifically addressing issues with multi-valued dependencies.

#### 31. What is the requirement for a table to be in BCNF (Boyce-Codd Normal Form)?
**Answer:**
For every non-trivial functional dependency A->B, A must be a superkey.

#### 32. When are two sets of functional dependencies (S1 and S2) considered equivalent?
**Answer:**
S2 is equivalent to S1 if exactly the same functional dependencies can be derived from both sets (i.e., their closures are equal).

#### 33. When does a set of functional dependencies S2 follow from S1?
**Answer:**
S2 follows from S1 if every relation instance that satisfies all dependencies in S1 also satisfies all dependencies in S2.

#### 34. Which Normal Form requires that all non-key fields are dependent only on the candidate key?
**Answer:**
BCNF (Boyce-Codd Normal Form) requires that for every functional dependency X -> Y, X must be a superkey.

#### 35. Which Normal Form validates functional and multivalued dependencies?
**Answer:**
Fourth Normal Form (4NF).

#### 36. Which Normal Form validates functional dependencies between key attributes?
**Answer:**
Boyce-Codd Normal Form (BCNF).

#### 37. Why can only relations with a composite candidate key violate 2NF?
**Answer:**
2NF requires that all non-key attributes be fully dependent on the *entire* primary key. If a table has a single-attribute primary key, there cannot be a partial dependency, as there are no 'parts' of the key to be partially dependent on. Partial dependencies can only exist when the primary key is composed of multiple columns.


## 📂 Category: Database Programmability (72 cards)

### 🔴 Senior Level

#### 1. Around which three main concepts is SQL access control built?
**Answer:**
SQL access control is built around authorization identifiers (users/roles), ownerships, and privileges (grant/revoke).

#### 2. Can triggers activate other triggers?
**Answer:**
Yes, triggers can activate themselves or other triggers in a chain, which can lead to nested or recursive execution.

#### 3. Can triggers be associated with a view?
**Answer:**
Yes, specifically 'INSTEAD OF' triggers are commonly used on views to handle modifications that cannot be automatically mapped to base tables.

#### 4. Compare EXEC(SQL) and sp_executesql.
**Answer:**
EXEC(SQL) is typically used for ad-hoc queries and does not easily allow for parameterization, which can lead to recompilation and security risks. sp_executesql allows for parameterization, which enables the SQL engine to reuse execution plans, improving performance and security.

#### 5. Explain HIERARCHYID functions: GetAncestor, GetDescendant, GetLevel, GetReparentedValue, ToString, GetRoot, and Parse.
**Answer:**
These functions manage hierarchical data: GetAncestor returns a parent node; GetDescendant returns child nodes between two siblings; GetLevel returns depth; GetReparentedValue moves a subtree; ToString/Parse convert between human-readable strings and the HIERARCHYID binary type; GetRoot returns the hierarchy apex.

#### 6. Explain the effect of CASCADE and RESTRICT in authorization revocation.
**Answer:**
RESTRICT prevents the revocation if other privileges depend on it. CASCADE removes the privilege from the target user and recursively removes any other privileges that were granted based on the revoked privilege.

#### 7. Granting and Revoking Privileges
**Answer:**
GRANT [privileges] ON [relation] TO [user] [WITH GRANT OPTION] grants specific permissions (select, update, delete). REVOKE [privileges] ON [relation] FROM [user] [CASCADE] removes those permissions. The 'CASCADE' option ensures that dependent privileges granted by the user are also revoked.

#### 8. How are variables assigned in a PL/SQL block?
**Answer:**
Variables can be assigned using the assignment operator (:=) or via the result of a SQL SELECT INTO or FETCH statement.

#### 9. How do DBMS handle queries against virtual views?
**Answer:**
While views conceptually act like temporary tables, in practice, the DBMS rewrites the query referencing the view into a query that references the underlying base tables (or recursive views) directly.

#### 10. How do constraints relate to triggers?
**Answer:**
Constraints are static and can be simulated by triggers. Triggers are dynamic, more powerful, and cannot be fully simulated by constraints.

#### 11. How does SQL Server Service Broker handle failed message delivery?
**Answer:**
It implements an exponential backoff retry strategy, attempting delivery at intervals of 4s, 8s, 16s, 32s, and then repeatedly every 60s.

#### 12. In MySQL, what keyword allows an automatic view update to ensure modifications appear within the view constraints?
**Answer:**
The 'WITH CHECK OPTION' clause is used in MySQL to ensure that updates or inserts performed through a view remain within the criteria defined by the view's WHERE clause.

#### 13. In SQL Service Broker, what happens if a ROUTE does not define a BROKER_INSTANCE and multiple services share the same name?
**Answer:**
The message is delivered to one of the services randomly, a behavior often used for scaling out.

#### 14. In XQuery, what is the difference between 'For' and 'Let'?
**Answer:**
'For' iterates over each element in an expression (like a loop), whereas 'Let' binds the entire result of an expression to a variable at once without iteration.

#### 15. Is it always possible to propagate data modifications from a view to the underlying base tables?
**Answer:**
Propagating modifications (inserts, updates, deletes) through a view is only sometimes possible. It is often restricted when the system cannot determine a unique or correct mapping to the underlying rows, leading to ambiguity in how the original relations should be updated.

#### 16. Jaký protokol využívá dialog service brokeru?
**Answer:**
TCP/IP pro interdatabázovou komunikaci a přímý insert pro intradatabázovou komunikaci.

#### 17. Je potřeba u SERVICE specifikovat CONTRACT?
**Answer:**
Ne, není to nutné, ale bez definovaného kontraktu může služba sloužit pouze jako iniciátor dialogu.

#### 18. Kolik je sys.transmission_queue?
**Answer:**
Existuje jedna tabulka sys.transmission_queue na každou databázi.

#### 19. Kolik konverzací se vejde na stránku v sys.sysdesend?
**Answer:**
Na jednu stránku v systémové tabulce sys.sysdesend se vejde 144 konverzací.

#### 20. Která tabulka způsobuje contention při odesílání zpráv přes Service Broker?
**Answer:**
Zvýšený contention (spor o prostředky) způsobuje systémová tabulka sys.sysdesend.

#### 21. SQL Programmability: Views and Triggers
**Answer:**
Views: 'CREATE [MATERIALIZED] VIEW [name] AS [query]' creates a virtual table. Triggers: 'CREATE TRIGGER [name] ...' defines procedural logic that executes automatically in response to specific events (INSERT, UPDATE, DELETE) on a table.

#### 22. What are DBCC commands in T-SQL?
**Answer:**
DBCC stands for Database Console Command. It is a suite of diagnostic and maintenance commands used to check database integrity, manage query plan caches, and debug performance via trace flags.

#### 23. What are INSTEAD OF triggers?
**Answer:**
INSTEAD OF triggers are executed in place of the original DML statement (INSERT, UPDATE, or DELETE). They are commonly used to update views that are not directly updatable.

#### 24. What are Magic Tables (Inserted/Deleted) in SQL Server?
**Answer:**
Magic tables are virtual tables available only within triggers. The 'INSERTED' table holds the new values during INSERT or UPDATE, and the 'DELETED' table holds the old values during DELETE or UPDATE operations.

#### 25. What are general database assertions?
**Answer:**
General assertions are a SQL standard feature used to enforce integrity constraints across the database. They can be assimilated to materialized views but are notably not implemented in most modern DBMS.

#### 26. What are the advantages of non-linear recursion versus linear recursion?
**Answer:**
Non-linear recursion can produce cleaner queries and converges faster (logarithmic vs linear). However, it is harder to implement, and many DBMS (including standard SQL) primarily support linear recursion.

#### 27. What are the advantages of using Cursors?
**Answer:**
Cursors allow for row-by-row processing, which is useful for complex row-wise validation or logic. They can return the first few rows before a full result set is assembled, potentially improving perceived response time, and they can offer better concurrency control in specific scenarios where manual updates are required, though they often come with higher performance overhead compared to set-based operations.

#### 28. What are the common tricky issues associated with database triggers?
**Answer:**
Key issues include: the chaining and termination problem (infinite loops), ambiguity in order of execution for multiple triggers, complexity of conditions (WHEN vs. inside the action), and the difference between row-level vs. statement-level execution.

#### 29. What are the disadvantages of using Cursors in SQL?
**Answer:**
Cursors are memory-intensive as they create a temporary work area in system memory. They often lead to performance degradation due to iterative row-by-row processing, which causes excessive network round trips compared to set-based operations (SELECT/UPDATE/DELETE).

#### 30. What are the four possible referencing-variables available in database triggers?
**Answer:**
The four referencing-variables are: old row (only in row-level statements), old table, new row (only in row-level statements), and new table. Row-level statements are defined as 'FOR EACH ROW'.

#### 31. What are the parts of a PL/SQL block?
**Answer:**
A PL/SQL block consists of an optional declaration part, a mandatory executable part, and an optional exceptions (handling) part.

#### 32. What are the pros and cons of using Materialized Views?
**Answer:**
Pros: Dramatically improve query performance by pre-calculating results. Cons: They consume significant storage space and may become out-of-sync with the base tables, requiring maintenance.

#### 33. What are the requirements for a view to be automatically updatable under the SQL standard?
**Answer:**
To be updatable, a view must: have only one table in its top-level FROM clause, not use SELECT DISTINCT, not refer to that table in subqueries, and not use GROUP BY or aggregate functions. Additionally, it should include all attributes from the base table that do not permit NULL values.

#### 34. What are the sql:column() and sql:variable() functions?
**Answer:**
These are XQuery functions used within SQL Server to interact with XML data. sql:column() extracts values from a SQL column into an XQuery context, while sql:variable() retrieves the value of a SQL variable for use within XQuery expressions.

#### 35. What are the steps to execute a cursor?
**Answer:**
1. Declare cursor, 2. Open cursor, 3. Fetch row, 4. Process row, 5. Close cursor, 6. Deallocate cursor.

#### 36. What are the two primary approaches for managing view modifications in a DBMS?
**Answer:**
1. Rewriting process: Uses INSTEAD-OF triggers or rules to define how updates are handled. It is flexible but requires careful implementation. 2. Restrictive approach: Limits views (e.g., no DISTINCT, no GROUP BY, single table only) to ensure modifications to base tables are unambiguous and automatically handled by the engine.

#### 37. What are the two types of PL/SQL subprograms?
**Answer:**
PL/SQL supports Stored Procedures and Functions.

#### 38. What are the two types of database triggers?
**Answer:**
Triggers can be Row-level triggers (executing once per modified row) or Statement-level triggers (executing once per SQL statement).

#### 39. What does an algebraizer do with a View?
**Answer:**
The algebraizer expands the view definition into the base query during the parsing and binding phase.

#### 40. What does the SQL keyword 'BEFORE' indicate in a trigger?
**Answer:**
It specifies that the trigger code should execute before the triggering event (such as an INSERT) is actually applied to the table.

#### 41. What does the UPDATE(column) function do within a trigger?
**Answer:**
It returns a boolean value indicating whether the specified column was modified in the SET clause of a DML statement.

#### 42. What does the command ALTER DATABASE SET ENABLE_BROKER do?
**Answer:**
It enables the Service Broker feature for the specified SQL Server database, which allows for asynchronous message processing.

#### 43. What happens if a Service Broker route is only configured on the initiator?
**Answer:**
The initiator sends the message, but the receiver will likely drop duplicate messages if it cannot return an acknowledgment correctly.

#### 44. What is Parameter Sniffing?
**Answer:**
A phenomenon in SQL Server where the query optimizer creates an execution plan for a stored procedure based on the parameter values provided during the very first execution, which may not be optimal for subsequent executions with different parameters.

#### 45. What is Scalar UDF inlining?
**Answer:**
It is a process where the SQL engine attempts to convert a scalar User Defined Function into a relational expression, allowing it to be integrated into the main query plan for better performance.

#### 46. What is a 'poison message' in the context of SQL Server Service Broker?
**Answer:**
A message that causes a transaction to fail repeatedly, specifically a message where processing has triggered a rollback five times.

#### 47. What is a Cursor in a database?
**Answer:**
A cursor is a database object that allows applications to process data on a row-by-row basis, moving away from the typical set-based operations of SQL.

#### 48. What is a Plan Guide in SQL Server?
**Answer:**
A component that allows database administrators to influence query optimization by attaching query hints to specific queries based on text matching, even when the application code cannot be changed.

#### 49. What is a database Trigger?
**Answer:**
A special type of stored procedure that executes automatically in response to specific events (like INSERT, UPDATE, or DELETE) on a particular table.

#### 50. What is a database trigger?
**Answer:**
A trigger is a database object that automatically executes a defined set of actions in response to specific events (like INSERT, UPDATE, or DELETE) occurring on a particular table or view.

#### 51. What is a database trigger?
**Answer:**
A stored program that automatically executes (or 'fires') in response to specific events (like INSERT, UPDATE, or DELETE) on a particular table or view.

#### 52. What is a recursive stored procedure in SQL Server?
**Answer:**
A recursive stored procedure is a procedure that calls itself either directly or indirectly (mutual recursion). It is used for repetitive problem-solving and can nest up to 32 levels in SQL Server.

#### 53. What is a recursive stored procedure?
**Answer:**
A stored procedure that calls itself until it reaches a defined boundary condition. This allows for repeated execution of logic.

#### 54. What is a trigger?
**Answer:**
A trigger is a specialized stored procedure that automatically executes ('fires') in response to specific events on a table or view, such as INSERT, UPDATE, or DELETE operations.

#### 55. What is an 'Extended Event' in SQL Server?
**Answer:**
An extended event is an event triggered by a specific circumstance that provides access to a large amount of event data. They generally do not log sensitive SQL text keywords like 'password' or 'session_id'.

#### 56. What is mutual recursion in SQL?
**Answer:**
Mutual recursion occurs when a recursive relation refers to another recursive relation, which then refers back to the first, forming a recursive ring. This is typically used to traverse directed graphs, such as in the Hub and Authority ranking algorithm. Note: Non-deterministic recursion is generally not allowed in SQL standards.

#### 57. What is rpc_completed?
**Answer:**
It is an Extended Event triggered when a Remote Procedure Call (RPC) operation has completed.

#### 58. What is the FLOWR expression syntax in XQuery?
**Answer:**
FLOWR stands for: For (iteration), Let (variable assignment), Where (filtering), Order by (sorting), and Return (output). For and Let can be interleaved/repeated; only Return is mandatory.

#### 59. What is the delivery order of messages in Service Broker?
**Answer:**
Ordering is guaranteed within a single conversation. If multiple conversations exist, selection is managed by priorities.

#### 60. What is the difference between SQL and PL/SQL?
**Answer:**
SQL is a declarative query language for set-based operations. PL/SQL (Procedural Language/SQL) is an extension of SQL that adds procedural features like loops, variables, and conditional logic to build full programs.

#### 61. What is the difference between row-level and statement-level triggers?
**Answer:**
A row-level trigger executes once for each row affected by the triggering event (e.g., INSERT, UPDATE, DELETE). A statement-level trigger executes only once for the entire SQL statement, regardless of how many rows are affected.

#### 62. What is the function of sp_recompile?
**Answer:**
A built-in system stored procedure in SQL Server that marks the execution plan of a specific procedure or trigger as invalid, forcing a re-compilation the next time it is executed.

#### 63. What is the function of the 'WITH ENCRYPTION' option in database programmability?
**Answer:**
The 'WITH ENCRYPTION' option hides the execution plans and source text of stored procedures, functions, or triggers from all users and system logs.

#### 64. What is the purpose of the DBCC TRACEON command?
**Answer:**
DBCC TRACEON is a command used to enable specific trace flags within a database session to help diagnose performance issues or track internal server activity.

#### 65. What is the purpose of the TRIGGER_NESTLEVEL function?
**Answer:**
It is a function that returns the nesting level of a trigger execution. It accepts parameters: object_id (specific trigger to track), trigger_type (AFTER or INSTEAD OF), and trigger_event_category (DDL or DML).

#### 66. What items are contained within an SQL package, and what are its two main parts?
**Answer:**
An SQL package consists of procedures, functions, variables, and SQL statements. It is divided into two parts: the 'specification' (which declares public constructs) and the 'body' (which defines the implementation of all public and private constructs).

#### 67. What types of triggers exist in SQL Server?
**Answer:**
There are AFTER triggers (which fire after the DML operation) and INSTEAD OF triggers (which fire before or in place of the DML operation).

#### 68. When and why should you use a database cursor?
**Answer:**
Cursors are used when you need to process data row-by-row to perform complex logic (like conditional updates or inserts) that cannot be easily achieved with set-based SQL queries. They function similarly to for/while loops.

#### 69. When is it appropriate to use a Cursor?
**Answer:**
Cursors are generally inefficient but may be necessary for procedural logic within triggers or stored procedures when you need to iterate through a specific set of rows (e.g., processing individual rows in the 'INSERTED' table during a trigger).

#### 70. Where can one check if a scalar function is inlineable in SQL Server?
**Answer:**
In the sys.sql_modules system catalog view.

#### 71. Why are materialized views often used in OLAP?
**Answer:**
Materialized views are used in OLAP to store precomputed query results. This improves performance for complex analytical queries by avoiding re-aggregation, similar to how OLAP cubes function, as both scenarios feature infrequent data updates and high read volume.

#### 72. Why is modification via views not always systematically automated?
**Answer:**
Modifications through views are not always automated because the mapping between the view's result set and the underlying base tables can be ambiguous, especially when joins, aggregations, or distinct clauses are involved.


## 📂 Category: Performance & Indexing (182 cards)

### 🔴 Senior Level

#### 1. Co je to Language parser?
**Answer:**
Součást relačního enginu zodpovědná za syntaktickou analýzu SQL dotazu a vytvoření stromu dotazu (parser tree).

#### 2. Define the Query Executor (QE) in a database engine.
**Answer:**
The Query Executor is the part of the relational engine that takes a generated execution plan and executes it by interacting with the storage engine.

#### 3. Define the Query Optimizer (QO) and its objective.
**Answer:**
The Query Optimizer is a part of the relational engine that takes an algebraizer tree and produces an execution plan. It aims to produce a 'good enough' plan rather than necessarily the absolute fastest or smallest one.

#### 4. Difference between actual and estimated execution plan in SSMS?
**Answer:**
An estimated execution plan is generated without executing the query and does not recompile outdated statistics, whereas an actual plan is generated by executing the query, reflecting real-time performance data and current statistics.

#### 5. Difference between execution plan and query plan?
**Answer:**
A query plan is the abstract logical/physical strategy generated by the optimizer. An execution plan includes the query plan combined with the actual execution context, such as runtime statistics, parameter values, and literal constants.

#### 6. Do Hash Match, Merge Join, and Nested Loop operators require a memory grant?
**Answer:**
Hash Match requires a memory grant. Nested Loop does not. Merge Join generally does not, unless it involves a many-to-many relationship requiring tempdb worktables.

#### 7. Do execution plans have priority in server memory?
**Answer:**
Yes, execution plans are stored in the plan cache within the buffer pool. The SQL Server query optimizer treats them as high-priority memory consumers, and they are managed by an algorithm that determines which plans to evict based on frequency of use and cost.

#### 8. Does a row have to fit on one page?
**Answer:**
Generally, rows are designed to fit on a single page, but if variable-length data causes the row size to exceed page limits, the engine moves that data to an overflow page.

#### 9. How are Extended Events results stored?
**Answer:**
Extended Events results can be configured to be stored in various targets, including live logging buffers, files on disk, or SQL tables.

#### 10. How are PFS pages allocated in SQL Server?
**Answer:**
Every 8,088th page is a Page Free Space (PFS) page.

#### 11. How are pages connected within the same level of an index?
**Answer:**
Pages within the same index level are connected via a doubly linked list.

#### 12. How are row offsets stored on a page?
**Answer:**
They are stored at the end of the data page in a slot array, ordered backwards.

#### 13. How can NOT NULL columns save space in an index?
**Answer:**
In nonclustered indexes, if all columns are defined as NOT NULL, the leaf nodes do not need to include a NULL bitmap, reducing storage overhead.

#### 14. How can ad hoc queries reuse execution plans?
**Answer:**
Query plans can be reused via identical SQL text, auto-parameterization, or the use of Plan Guides.

#### 15. How can one handle null bitmaps in indexes?
**Answer:**
In a clustered index, null bitmap behavior is fixed by the structure. In a non-clustered index, it is possible to optimize index storage to handle nulls more efficiently.

#### 16. How do implicit data type mismatches impact index performance?
**Answer:**
If an indexed column is compared against a value of a different data type requiring implicit conversion, the DB automatically converts the column value for every row, leading to a Full Table Scan.

- ❌ `WHERE user_id = 123` (without quotes when `user_id` is `VARCHAR`) -> Full Table Scan!

- ✅ `WHERE user_id = '123'` (with string quotes) -> Index Used!

#### 17. How do indexes affect AND versus OR operators?
**Answer:**
For an AND operator, it is typically more efficient to have one composite index. For an OR operator, it is often better to have separate indexes on the involved columns.

#### 18. How do materialized views improve database performance?
**Answer:**
Materialized views improve performance by physically caching the result of a query, effectively acting like an index on a complex result set. The query optimizer can automatically rewrite queries to access this precomputed data rather than executing the original complex joins/aggregations.

#### 19. How do rows in intermediate pages differ between UNIQUE and non-UNIQUE indexes?
**Answer:**
In non-UNIQUE indexes, intermediate pages must include either the Row ID (RID) or the Clustered Key (CK) alongside the Index Key (IK) to uniquely identify entries.

#### 20. How do you force the SQL optimizer to consider indexes on a view?
**Answer:**
Use the WITH (NOEXPAND) table hint in the query.

#### 21. How do you trace the traffic hitting a SQL Server?
**Answer:**
SQL Profiler is the utility used to trace traffic. Traces can be filtered to capture specific transactions, reducing overhead, and saved/replayed for troubleshooting.

#### 22. How does a database fetch data after jumping to a secondary index vs. a covering index?
**Answer:**
- **Secondary Index:** Stores indexed columns + Primary Key ID. For `SELECT * FROM comments WHERE path LIKE '001%'`, the DB searches `idx_path` to find matching IDs (1st jump), then looks up those IDs in the Primary Key table to fetch full row data (2nd jump — "Bookmark Lookup").

- **Covering Index:** If a query selects ONLY columns that are present inside the index (e.g. `SELECT id, status FROM users WHERE tenant_id = 5` when index is `(tenant_id, status)`), the DB returns data directly from index memory without touching the main table (Covering Index Scan).

#### 23. How does a filtered index behave in a stored procedure?
**Answer:**
It is not used if the query uses a variable (parameter) in the predicate, because the optimizer cannot guarantee the filter condition. It must be explicitly used with OPTION (RECOMPILE).

#### 24. How does parameter sniffing occur with variables in SQL queries?
**Answer:**
Using a local variable in a query causes the SQL Server optimizer to ignore the specific value provided at execution time and instead compile a plan based on an 'average' distribution of data, which may lead to suboptimal performance.

#### 25. How does the Query Optimizer improve a trivial execution plan?
**Answer:**
It uses internal transformation rules to rewrite and optimize the plan.

#### 26. How does the cardinality estimator order multiple predicates?
**Answer:**
It orders them based on selectivity, which is the fraction of rows that satisfy a predicate.

#### 27. How is cache space for query plans managed?
**Answer:**
It is segmented into tiered levels where the system allocates different percentages of memory based on specific size thresholds.

#### 28. How is the duration of an operator calculated in query plans?
**Answer:**
It is calculated as: Time of Close() call - Time of Init() call.

#### 29. How is the level numbering system structured in an index tree?
**Answer:**
The leaf level is defined as level 0, and the root page is assigned the maximum number.

#### 30. How is the variable array stored in a record?
**Answer:**
It stores 2 bytes for the total number of variable columns and includes the end offsets for each non-null variable-length column.

#### 31. How large is a Record Identifier (RID)?
**Answer:**
8 bytes.

#### 32. How large is a forwarding pointer?
**Answer:**
16 bytes.

#### 33. How large is one quantum in SQL Server scheduling?
**Answer:**
4 ms.

#### 34. How many IAM pages exist in SQL Server?
**Answer:**
At least one per GAM extent containing pages of a tracked entity, and at least one per file containing pages of the entity.

#### 35. How many values are tracked in a standard SQL histogram?
**Answer:**
200 steps (values).

#### 36. How much I/O overhead does a RID lookup cost?
**Answer:**
One I/O normally, or two if a forwarding pointer must be followed.

#### 37. How much memory does SQL Server grant for a variable-length column?
**Answer:**
It typically grants 50% of the declared size.

#### 38. In which version was the Cardinality Estimator first changed in SQL Server?
**Answer:**
It was updated in SQL Server 2014 (compatibility level 120).

#### 39. Jaký cardinality estimator se použije bez traceflagů?
**Answer:**
Použije se podle nastaveného compatibility levelu databáze.

#### 40. Jaký operátor ochrání UPDATE před Halloween problémem?
**Answer:**
Spool operátor, který vytvoří dočasnou kopii dat.

#### 41. K čemu potřebují spool operátory memory grant nebo tempdb?
**Answer:**
K uložení mezivýsledku (datasetu) pro jeho opakované čtení nebo zpracování.

#### 42. K čemu využívá hash match operátor memory grant?
**Answer:**
Memory grant se využívá pro vytvoření hash tabulky z tzv. 'build' vstupu. 'Probe' vstup paměť pro operaci nepotřebuje.

#### 43. Kdy mohou být hodnoty rebind a rewind různé od 0?
**Answer:**
Tento stav nastává u vnitřního vstupu operátoru nested loop join.

#### 44. Kdy se použije triviální plán?
**Answer:**
Triviální plán se použije v momentě, kdy optimalizátor vyhodnotí existující plán jako 'good enough' (dostatečně efektivní bez nutnosti hlubokého hledání).

#### 45. Kolik je minimální memory grant?
**Answer:**
Minimální alokace paměti (memory grant) je 1 MB.

#### 46. Kolik je v SQL serveru (S)GAM stránek?
**Answer:**
(S)GAM stránky se nacházejí jednou za 64 000 extentů (cca 4 GB), minimálně však jednou pro každý soubor databáze.

#### 47. Která část Query Optimizeru nahrazuje komplikovanější operátory za základní (např. between na >= a <=)?
**Answer:**
Tuto transformaci provádí tzv. Algebraizer.

#### 48. Které jsou tzv. 'Stop & Go' operátory?
**Answer:**
Jedná se o operátory Hash Match (částečně) a Sort, které musí načíst všechna data předtím, než mohou vydat první řádek.

#### 49. Který proces způsobuje náhlé zpomalení procedury, která dříve běžela rychle?
**Answer:**
Jde o 'Parameter Sniffing', kdy dojde k rekompilaci plánu na základě specifických (a nevýhodných) parametrů volání.

#### 50. On what type of pages is the PFS (Page Free Space) byte applicable?
**Answer:**
PFS pages track page allocation and free space, primarily applicable to heap table pages in SQL Server.

#### 51. S čím souvisí rozhodnutí použít materializované pohledy (materialized views)?
**Answer:**
Rozhodnutí je otázkou kompromisu mezi rychlostí čtení (query) a režií při zápisu (update), podobně jako u indexů.

#### 52. What are LOBs (Large Objects) and LOB pages in a database?
**Answer:**
LOBs (Large Objects) are data types used to store large amounts of data (e.g., text, images). LOB pages are internal storage pages specifically allocated for variable-length data types marked as MAX.

#### 53. What are common DBCC commands for query tuning and debugging?
**Answer:**
Key commands include: 'DBCC FREEPROCCACHE' to clear the plan cache; 'DBCC TRACEON(XYZ)' to enable specific trace flags (add '-1' to apply globally); 'DBCC TRACEON(3604)' to route output to the session window; 'DBCC HELP' to view documentation; and 'DBCC OPTIMIZER_WHAT_IF' to test optimizer behavior under hypothetical conditions.

#### 54. What are common SQL Server trace flags for performance tuning?
**Answer:**
Traceflag 174: Increases cached plan count. 2312: Forces current cardinality estimator. 3604: Sends output to session window. 7471: Uses UPD lock for UPDATE STATISTICS. 8649: Forces parallelism. 8780: Increases query compilation transformation limits. 9481: Forces legacy cardinality estimator.

#### 55. What are incremental statistics?
**Answer:**
Incremental statistics refer to a performance optimization where database statistics are updated only for the newest partition of a partitioned table rather than re-scanning the entire table.

#### 56. What are non-page latches typically used for?
**Answer:**
Non-page latches are typically used to protect metadata pages or other internal memory structures in a database engine.

#### 57. What are sql_statement_starting/completed/recompile in Extended Events?
**Answer:**
These are events used in SQL Server's Extended Events framework to track the lifecycle of ad-hoc queries or stored procedure executions, useful for performance monitoring and debugging.

#### 58. What are the core components of the Relational Engine?
**Answer:**
The relational engine is comprised of the Query Processor, which includes the Language Processing/Parser, the Query Optimizer (which determines the execution plan), and the Query Executor (which runs the plan).

#### 59. What are the ideal conditions for a Nested Loop join operator?
**Answer:**
It is most efficient when the outer input has a small number of rows and the inner input has a low-cost subtree (often indexed).

#### 60. What are the inputs of a Hash Match operator?
**Answer:**
The top input is the 'build' input, and the bottom input is the 'probe' input.

#### 61. What are the key best practice guidelines for database index design?
**Answer:**
- **Search by text prefix:** Use trailing wildcard `LIKE 'text%'`.

- **Multi-column queries:** Follow the ESR Rule (`Equality -> Sort -> Range`).

- **High-performance APIs:** Use Covering Indexes for frequent `SELECT` queries.

- **Avoid N+1 DB roundtrips:** Use Materialized Path or Eager Loading.

#### 62. What are the maximum limits for index keys in SQL Server?
**Answer:**
The maximum index key size is 900 bytes for versions before SQL Server 2016, and 1700 bytes for 2016 and later. The maximum number of columns is 16 and 32, respectively.

#### 63. What are the physical implications of data modification on indexes and pages?
**Answer:**
When a row in a clustered index is updated and exceeds page space, a page split occurs. If a row with a forwarding pointer is moved again, the forwarding pointer is updated to reflect the new location. Additionally, non-clustered indexes are typically not rebuilt when the underlying clustered index is rebuilt.

#### 64. What are the primary underlying data structures for database indexes?
**Answer:**
The two main structures are B-Trees (B-Trees or B+Trees), which support equality and range comparisons, and Hash Tables, which are optimized for constant-time equality lookups.

#### 65. What are the reasons for early statement termination during plan compilation?
**Answer:**
Time Out (limit on transformations reached), Memory (insufficient memory), or 'Good Enough' (an optimal or sufficient plan was found).

#### 66. What are the storage characteristics and statistical differences between temporary tables and table variables?
**Answer:**
Temporary tables are stored in tempdb on disk and support statistics. Table variables are also stored in tempdb, but do not maintain histograms or updateable statistics, which can impact query optimizer performance.

#### 67. What causes the 'ERROR 666' in SQL Server?
**Answer:**
This error is emitted when the internal hidden integer column used to manage non-unique clustered keys overflows its allocated storage limit.

#### 68. What condition is required for a Merge Join?
**Answer:**
A Merge Join requires an equijoin condition and sorted inputs on the join keys.

#### 69. What do common SQL Server wait types signify: CX_PACKET, CXCONSUMER, and RESOURCE_SEMAPHORE?
**Answer:**
CX_PACKET: Parallelism wait (thread waiting on other threads/processor). CXCONSUMER: Parallelism wait (parent waiting on child). RESOURCE_SEMAPHORE: Waiting for a memory grant.

#### 70. What do sys.indexes.index_id values represent?
**Answer:**
0 indicates a heap (table with no clustered index), 1 indicates a clustered index, and values greater than 1 indicate nonclustered indexes.

#### 71. What does "cost" in an execution plan mean?
**Answer:**
It is an estimate of the processing time an operator will take, relative to the total cost of the query plan.

#### 72. What does 'number of rows to be read' (residual reads) mean in query statistics?
**Answer:**
This refers to the number of pages/rows that had to be physically read by the storage engine to retrieve columns not covered by the index (often called key lookups or residual reads).

#### 73. What does an RID contain?
**Answer:**
A Record Identifier (RID) typically contains references to the file ID, page ID, and row number.

#### 74. What does sys.dm_exec_query_statistic_XML(session_id) do?
**Answer:**
Returns information about currently running query in a selected session, typically used for troubleshooting execution plans. Note that it often requires specific trace flags enabled.

#### 75. What happens if you disable a clustered index?
**Answer:**
Access to the entire table is disabled in most SQL implementations.

#### 76. What is %%physloc%% in SQL Server?
**Answer:**
%%physloc%% is a virtual column that contains the physical address (RID - Row Identifier) of a row in a table.

#### 77. What is 'cache bloat' in a SQL server context?
**Answer:**
Cache bloat is the exhaustion of memory caused by storing an excessive number of unique query plans, often due to lack of parameterization.

#### 78. What is 'hole-filling optimization' in the context of MERGE statements?
**Answer:**
An optimization where, if a MERGE statement only inserts rows into the gaps in a clustered key, it can avoid HALLOWEEN protection logic.

#### 79. What is DBCC?
**Answer:**
DBCC (Database Console Commands) are administrative tools used to perform maintenance, validation (like CHECKDB), information gathering, and miscellaneous tasks in SQL Server.

#### 80. What is Fill Factor?
**Answer:**
Fill Factor is an index setting that determines the percentage of space to be filled with data on each leaf-level index page. It helps manage page splits in frequently updated tables.

#### 81. What is LPE in the context of database engine operations?
**Answer:**
LPE stands for Language Processing and Execution, referring to the stages where a SQL statement is parsed, optimized, and executed.

#### 82. What is Page Free Space (PFS) in SQL Server?
**Answer:**
PFS pages are specific pages in the database that track the amount of free space available on data pages (using one byte per page).

#### 83. What is SGAM?
**Answer:**
SGAM stands for Shared Global Allocation Map. It is a system page used in SQL Server to track which extents in a database are currently mixed and have at least one free page available.

#### 84. What is a 'Rebind' operation in query execution?
**Answer:**
A process where the conditions of a spool operator are re-evaluated or re-initialized before the operator begins reading the rows again.

#### 85. What is a 'Rewind' operation in query execution?
**Answer:**
An operation where the database restarts reading a spool or table from the beginning.

#### 86. What is a 'read-ahead read' in database performance?
**Answer:**
A performance optimization where the database engine loads consecutive data pages into memory before they are explicitly requested, reducing I/O wait times.

#### 87. What is a 'stub' query plan?
**Answer:**
A stub query plan refers to a cached hash of an execution plan that does not contain the actual compiled plan details, often seen when memory pressure or specific cache settings prevent full plan storage.

#### 88. What is a 'trivial plan' in query optimization?
**Answer:**
A trivial plan is a simple execution plan consisting only of basic scans or seeks, created without applying complex algebraic transformations or optimization rules.

#### 89. What is a GAM page?
**Answer:**
GAM stands for Global Allocation Map, which tracks which extents have been allocated in a SQL Server data file.

#### 90. What is a Global Allocation Map (GAM) in database storage?
**Answer:**
A GAM page is a specialized storage page that tracks extent allocation. It uses a bitmask where 'true' indicates an unallocated extent and 'false' indicates an allocated extent.

#### 91. What is a Nested Loop join?
**Answer:**
A Nested Loop join is an algorithm suitable for joining a small dataset with a larger one. It iterates through each row of the outer table and performs a lookup in the inner table, making it very effective when the inner table is indexed.

#### 92. What is a Physical Design Advisor and how does it function?
**Answer:**
It is a tool that analyzes database statistics and workload to recommend optimal indexes. It functions by testing various index combinations against the Query Optimizer to estimate execution costs, selecting the configuration where performance benefits outweigh maintenance overhead.

#### 93. What is a RID (Row Identifier)?
**Answer:**
A Row Identifier (RID) is a unique pointer to a specific row within a table, typically used by SQL Server to locate a row on a data page.

#### 94. What is a SQL-OS Scheduler?
**Answer:**
A component of SQL Server's operating system abstraction layer that manages the execution and scheduling of tasks on a single logical processor.

#### 95. What is a cardinality estimator?
**Answer:**
A cardinality estimator is a component of the SQL query optimizer that predicts the number of rows that will result from a specific query operator or plan.

#### 96. What is a database worker?
**Answer:**
A worker is a thread or process directed by the scheduler to perform specific tasks or queries.

#### 97. What is a forwarding pointer?
**Answer:**
A forwarding pointer is a pointer used in a heap-organized table to redirect to a row's new location if it has moved (e.g., due to an update that caused row migration).

#### 98. What is a hash_warning in SQL Server?
**Answer:**
A hash_warning is an extended event triggered when a hash join or hash aggregation operation exceeds the available memory grant, forcing the operation to spill data to tempdb (disk).

#### 99. What is a potential issue with (S)GAM pages in tempdb?
**Answer:**
They can become a contention bottleneck (latching) in high-concurrency environments because tempdb frequently allocates and deallocates pages for temporary objects.

#### 100. What is a query_hash?
**Answer:**
A hash value representing the structure of a query, excluding literals, used to identify identical queries even if parameter values differ.

#### 101. What is a row overflow page?
**Answer:**
A row overflow page stores variable-length data (such as varchar or nvarchar) that exceeds the storage capacity of a single data page (typically when it exceeds 8000 bytes).

#### 102. What is a sort_warning?
**Answer:**
An extended event triggered by the SQL Server engine when a sort operation (such as during a join or order by) exceeds the allocated memory, forcing it to spill to TempDB.

#### 103. What is a transformation rule in the context of database query processing?
**Answer:**
A transformation rule is a rule that maps logical or physical operations into other equivalent operations, often used by query optimizers to find more efficient execution plans.

#### 104. What is an 'exchange_spill' in SQL Server?
**Answer:**
An 'exchange_spill' is an Extended Event that occurs when parallel query execution processes run out of allocated memory (specifically in the exchange buffers) and are forced to spill data to the tempdb.

#### 105. What is an IAM and an IAM chain?
**Answer:**
IAM stands for Index Allocation Map. An IAM chain is a linked list of IAM pages that track the extents allocated to a single database entity (table or index).

#### 106. What is an index spool?
**Answer:**
An index spool is an execution operator that builds a temporary index over a dataset during query execution to optimize performance for that specific query.

#### 107. What is auto-parameterization in an SQL engine?
**Answer:**
It is a process where the SQL server treats ad-hoc queries as if they were stored procedures by automatically replacing constant values with parameters to improve plan reuse.

#### 108. What is data flow in the context of query execution plans?
**Answer:**
Data flow refers to the directional movement of data rows through an execution plan, typically visualized as reading the plan from right to left (the direction of data processing).

#### 109. What is density in database statistics?
**Answer:**
Density is a statistic computed as 1 / count(distinct), used by the query optimizer to estimate the selectivity of column values.

#### 110. What is forced automatic parametrization in SQL Server?
**Answer:**
Forced automatic parametrization is a setting in SQL Server where the query optimizer attempts to parameterize every query to improve plan reuse.

#### 111. What is interleaved execution in the context of query optimization?
**Answer:**
It is a process where the query optimizer executes a multi-statement Table-Valued Function (TVF) during the optimization phase to obtain a more accurate execution plan.

#### 112. What is meant by 'control flow' in query execution?
**Answer:**
It refers to the process of reading the execution plan by tracing the actual method calls of the operators during query execution.

#### 113. What is osstress.exe?
**Answer:**
A Microsoft tool used to perform stress testing on database systems.

#### 114. What is simple auto-parameterization?
**Answer:**
A server setting that allows the DBMS to automatically parameterize trivial queries, which helps in reusing execution plans and reducing compilation overhead.

#### 115. What is the 'OPTIMIZE FOR UNKNOWN' query hint?
**Answer:**
A query hint that instructs the query optimizer to use a plan based on average statistics rather than parameter-specific values.

#### 116. What is the 'cost threshold for parallelism' in SQL Server?
**Answer:**
A server-level setting that specifies the minimum cost required for a query plan to be considered for parallel execution.

#### 117. What is the 'optimize for ad hoc workloads' setting?
**Answer:**
A SQL Server configuration that stores only a small compiled plan stub on the first execution of a batch, reducing plan cache bloat.

#### 118. What is the 'tipping point' in SQL Server indexing?
**Answer:**
The tipping point is the specific threshold of I/O operations (percentage of rows) at which the query optimizer decides that performing an index seek is less efficient than performing a full table scan.

#### 119. What is the 'tipping point' in database page estimation?
**Answer:**
The tipping point is generally between 30% and 33% of table pages. For extremely small rows (such as many-to-many link tables), it is closer to 25%.

#### 120. What is the Adaptive Join operator?
**Answer:**
An operator that dynamically chooses between a nested loop or a hash match join based on the actual number of rows processed during execution.

#### 121. What is the Algebraizer and the Algebraizer Tree?
**Answer:**
The Algebraizer is a component of the relational engine that transforms a parser tree into an algebraizer tree. The algebraizer tree represents the structural plan of data joins and data sources for a query.

#### 122. What is the Bitmap operator?
**Answer:**
An operator used for efficient multi-threaded filtering, often used to improve join performance in parallel plans.

#### 123. What is the CXCONSUMER wait type in SQL Server?
**Answer:**
CXCONSUMER is a wait type introduced in SQL Server 2017 to track threads waiting for parallel process data from a producer thread in a parallel query plan.

#### 124. What is the ESR (Equality, Sort, Range) Rule for composite index design?
**Answer:**
When designing a composite index for complex queries, order the columns by:

1. **Equality (`=`):** Put exact match columns first (e.g. `tenant_id = 5`).

2. **Sort (`ORDER BY`):** Put ordering columns next (e.g. `ORDER BY created_at DESC`).

3. **Range (`>`, `<`, `LIKE 'abc%'`):** Put range or wildcard columns last.

**Why?** Once an index encounters a range condition (`LIKE` or `>`), it cannot use subsequent columns in the index for exact sorting.

#### 125. What is the Eager Spool operator?
**Answer:**
A spool operator that reads and stores all input rows from its child operator upon the first GetNext() call.

#### 126. What is the Global Allocation Map (GAM) page?
**Answer:**
The GAM page manages extent allocation. It contains flags: 'true' indicates mixed extents with at least one unallocated page, and 'false' indicates uniform extents or completely full mixed extents.

#### 127. What is the Lazy Spool operator?
**Answer:**
A spool operator that reads rows from its input only as they are requested by the parent operator.

#### 128. What is the Leftmost Prefix Rule in composite indexing?
**Answer:**
When using a composite index on multiple columns, e.g. `(A, B, C)` (`CREATE INDEX idx_abc ON users (tenant_id, status, created_at)`):

- **Works for:** `WHERE tenant_id = 1`, `WHERE tenant_id = 1 AND status = 'active'`, etc.

- **Fails (skips index):** `WHERE status = 'active'` (because column `A` is skipped).

- **Rule:** Always put the most frequently filtered column or tenant/parent ID first in composite indexes.

#### 129. What is the MIN_GRANT_PERCENT query hint?
**Answer:**
A hint that sets the minimum desired memory grant percentage for a query.

#### 130. What is the OPTION (FAST N) query hint?
**Answer:**
A hint that tells the query optimizer to optimize for retrieving the first N rows as quickly as possible.

#### 131. What is the OPTION (NO_PERFORMANCE_SPOOL) hint?
**Answer:**
A hint that instructs the query optimizer to avoid using a performance spool operator in the query execution plan.

#### 132. What is the OPTION (QUERYRULEOFF) hint?
**Answer:**
A hint used to disable specific transformation rules used by the Query Optimizer during plan generation.

#### 133. What is the OPTION (QUERYTRACEON XYZ) hint?
**Answer:**
A hint used to enable a specific trace flag only for the scope of the individual query.

#### 134. What is the SQL Server Query Store?
**Answer:**
A SQL Server feature that logs SQL queries, their execution plans, and performance metrics over time to assist in troubleshooting and performance tuning.

#### 135. What is the compilation cost of the MERGE statement compared to standard DML?
**Answer:**
The compilation cost of MERGE is significantly higher than that of equivalent individual INSERT, UPDATE, or DELETE statements.

#### 136. What is the default maximum memory grant for a SQL Server query?
**Answer:**
The default maximum memory grant is typically 20% of the total available server memory.

#### 137. What is the difference between a 'predicate' and a 'seek predicate' in an execution plan?
**Answer:**
A 'seek predicate' is used by the engine to navigate the index tree to find specific data. A 'predicate' (or residual predicate) is a filter applied to the rows after they have been retrieved, used for columns not covered by the index key.

#### 138. What is the difference between a Page IO latch and a Page latch?
**Answer:**
A Page IO latch manages access to a data page while it is being transferred from or to disk. A Page latch is used to manage access to a page already residing in memory.

#### 139. What is the difference between a logical and a physical operator?
**Answer:**
Logical operators describe the algebraic operation to be performed (e.g., Join, Group). Physical operators are the actual algorithms used by the engine to execute these operations (e.g., Hash Match, Nested Loops).

#### 140. What is the difference between forward and backward index scans?
**Answer:**
Forward index scans can be parallelized, whereas backward index scans generally cannot.

#### 141. What is the fastest collation?
**Answer:**
The binary collation (e.g., XY_BIN2) is typically the fastest, as it sorts data based on character code values rather than linguistic rules.

#### 142. What is the function of GAM and SGAM pages in SQL Server?
**Answer:**
GAM (Global Allocation Map) and SGAM (Shared Global Allocation Map) pages are used to track and manage the allocation of extents within a database file, helping the engine find available pages for new objects.

#### 143. What is the function of the Close() method in query execution operators?
**Answer:**
Close() is a method of physical query operators used to terminate processing and release associated resources.

#### 144. What is the function of the GetNext() method in physical database operators?
**Answer:**
GetNext() is a method of a physical query operator that iterates through and returns the next single row from the operator's input source.

#### 145. What is the nature of a WHERE predicate in a filtered index?
**Answer:**
The WHERE predicate in a filtered index is limited; it only allows simple comparisons and cannot contain subqueries, complex functions, or user-defined logic.

#### 146. What is the output of the SQL Parser?
**Answer:**
The output is a parse tree representing the logical structure of the SQL statement.

#### 147. What is the potential performance issue when using a filtered index with an IS NULL predicate?
**Answer:**
If the column in the predicate is NULL and is not included in the index key (IK), the query engine may resort to a lookup instead of an index seek, even if the index should ideally be covering. To achieve a seek, the nullable column must be part of the index key.

#### 148. What is the primary objective of Query Planning/Optimization?
**Answer:**
The main objective is to implement the most efficient use of indexes and execution paths to retrieve data.

#### 149. What is the purpose of DBCC PAGE?
**Answer:**
DBCC PAGE is an undocumented/internal command used to inspect the raw contents of a database data page, typically used for low-level troubleshooting or educational analysis of how data is stored on disk.

#### 150. What is the purpose of the Init() method in SQL execution operators?
**Answer:**
It serves as the operator's initialization phase, preparing the necessary resources for execution.

#### 151. What is the purpose of the MAX_GRANT_PERCENT query hint?
**Answer:**
MAX_GRANT_PERCENT is a query hint that sets the maximum allowable memory grant (as a percentage of total buffer pool memory) for a specific query execution.

#### 152. What is the purpose of trace flag 8780 in SQL Server?
**Answer:**
Trace flag 8780 is used to generate XML for use in a USE PLAN hint, often for the purpose of comparing query plans or forcing a specific execution plan.

#### 153. What is the role of the Algebraizer in the SQL Server relational engine?
**Answer:**
The Algebraizer is the component that resolves names (like table and column names) into internal object IDs and creates the initial query tree structure.

#### 154. What is the role of the row offsets table?
**Answer:**
The row offsets table is a part of the data page that stores the starting byte addresses (offsets) of the rows stored on that page.

#### 155. What is the size of a database page header?
**Answer:**
The standard size of a database page header in many systems like SQL Server is 96 bytes.

#### 156. What is the size of a row header?
**Answer:**
The row header is 4 bytes in size.

#### 157. What is the subtree cost of an operator in an execution plan?
**Answer:**
The subtree cost represents the total estimated cost of an operator plus the accumulated cost of all its child nodes in the execution plan tree.

#### 158. What issue can occur when comparing char and nchar columns with SQL_* collations?
**Answer:**
Collation mismatches or data type precedence issues (like Unicode vs non-Unicode) can prevent efficient index usage, often leading to full table scans or conversion errors.

#### 159. What latching issue is associated with identity primary keys?
**Answer:**
Identity primary keys often cause 'last-page' contention, where multiple concurrent inserts attempt to write to the same last page of the B-tree index, creating latch contention on the data page.

#### 160. What occurs during the Init() and GetNext() phases of a Hash Match operator?
**Answer:**
Init() builds a hash table from the 'build' input. GetNext() calls the probe operator and searches for matches within that built hash table.

#### 161. When does SQL Server use 'density' in query optimization?
**Answer:**
SQL Server uses density statistics when an equality predicate is used in the WHERE clause with a variable, or when the 'OPTIMIZE FOR UNKNOWN' hint is provided, as it estimates selectivity based on the average distribution of data.

#### 162. When is an execution plan built in relation to variable substitution?
**Answer:**
The execution plan is compiled and built before the local variables are substituted with actual values. This is why parameter sniffing can occur, as the plan is optimized based on the structure rather than the specific data distribution of the parameters at the time of initial compilation.

#### 163. Where can information about SQL Server wait types be found?
**Answer:**
Wait types are documented in the system view sys.dm_os_wait_stats.

#### 164. Which actions prevent the caching of temporary objects in SQL Server?
**Answer:**
Actions such as creating an index, running ALTER TABLE, or defining a named constraint prevent caching.

#### 165. Why are low cardinality columns poor candidates for solo indexing?
**Answer:**
- **High Cardinality** (many unique values: `email`, `user_id`, `created_at`): Ideal for indexing.

- **Low Cardinality** (few unique values: `gender`, `is_active`, `status`): Unsuitable for solo indexing. If 90% of rows have `is_active = true`, the DB query optimizer calculates that scanning the table directly is cheaper than doing 900,000 double-lookups via a secondary index.

#### 166. Why do SQL functions on indexed columns disable index usage?
**Answer:**
Wrapping an indexed column inside a SQL function disables the index because the DB must compute the function for every single row, resulting in a Full Table Scan.

- ❌ `WHERE YEAR(created_at) = 2026` -> Index Bypassed!

- ✅ `WHERE created_at >= '2026-01-01' AND created_at < '2027-01-01'` -> Index Used!

- ❌ `WHERE LOWER(email) = 'user@test.com'` -> Index Bypassed!

- ✅ `WHERE email = 'user@test.com'` -> Index Used!

#### 167. Why might a predicate in an index seek operator be inefficient?
**Answer:**
A predicate in a seek operator might be considered inefficient or 'bad' if it hides an underlying index scan, meaning the engine is doing more work than a precise seek should entail.

#### 168. sys.dm_db_index_operational_stats
**Answer:**
A Dynamic Management Object (DMO) that returns low-level, detailed statistics regarding index access, locking, and latching activity.

#### 169. sys.dm_db_index_physical_stats
**Answer:**
A system function that returns size and fragmentation information about indexes, supporting varying levels of detail (LIMITED, SAMPLED, or DETAILED).

#### 170. sys.dm_db_index_usage_stats
**Answer:**
A Dynamic Management Object (DMO) that returns information about how frequently indexes are used and the specific types of operations performed (seeks, scans, lookups, updates).

#### 171. sys.dm_exec_cached_plans
**Answer:**
A system view that returns information about all query execution plans that are currently stored in the plan cache.

#### 172. sys.dm_exec_plan_attributes
**Answer:**
A system function that returns information about specific attributes (such as SET options or database context) of a particular plan that influenced its compilation.

#### 173. sys.dm_exec_query_optimizer_info
**Answer:**
A system table providing detailed statistics and information about the Query Optimizer's behavior and operations since the last server restart.

#### 174. sys.dm_exec_query_plan
**Answer:**
A system function that retrieves the XML representation of a specific execution plan based on a given plan handle.

#### 175. sys.dm_exec_query_stats
**Answer:**
A system function that returns aggregate performance statistics (CPU, duration, reads, writes) for cached query plans.

#### 176. sys.dm_exec_requests
**Answer:**
A Dynamic Management Object (DMO) used to view all currently executing requests or tasks within the SQL Server instance.

#### 177. sys.dm_exec_sql_text
**Answer:**
A system table function that returns the text of the SQL batch corresponding to a specific query plan handle.

#### 178. sys.dm_exec_transformation_stats
**Answer:**
A system table containing statistics regarding the usage of specific transformation rules applied by the Query Optimizer.

#### 179. sys.dm_os_wait_stats
**Answer:**
A system function that returns information about all wait types encountered by threads during the execution of tasks.

#### 180. sys.dm_os_waiting_tasks
**Answer:**
A Dynamic Management Object (DMO) that returns information about all tasks currently in a 'waiting' state, including the resource they are waiting for.

#### 181. sys.fn_PhysLocFormatter
**Answer:**
A function that parses and formats the output of the %%physloc%% virtual column into a human-readable format (FileID:PageID:SlotID).

#### 182. sys.system_internals_allocation_units
**Answer:**
An undocumented system table that provides low-level information about allocation units, including pointers to IAM pages, root index pages, and the first leaf pages.


## 📂 Category: Subqueries & Aggregations (9 cards)

### 🔴 Senior Level

#### 1. Define linear vs. non-linear recursion in SQL.
**Answer:**
Linear recursion refers to a recursive CTE where there is only one reference to the recursive relation R within the definition. Non-linear recursion occurs when there is more than one reference to the recursive relation R, such as joining R with itself.

#### 2. For a fact table with attributes D1, D2, and D3, what are the row count formulas for GROUP BY, CUBE, and ROLLUP?
**Answer:**
Q1 (GROUP BY): n1*n2*n3. Q2 (WITH CUBE): (n1+1)*(n2+1)*(n3+1). Q3 (WITH ROLLUP): (n1*n2*n3) + (n1*n2) + n1 + 1.

#### 3. How can infinite cycles be prevented when using recursive WITH statements?
**Answer:**
Infinite cycles can be prevented by: 1) Setting a recursion limit via a WHERE clause (e.g., stopping when a path length reaches a maximum), 2) Using a LIMIT clause outside the recursion (though this may not work for all aggregate operations), or 3) Using a subquery in the WHERE clause to prune redundant or costlier paths, which is the most robust standard-compliant approach.

#### 4. How can you aggregate multiple rows into a single comma-separated string?
**Answer:**
In modern SQL (2017+), use the STRING_AGG(column, ',') function. For older versions, use the 'FOR XML PATH' trick combined with the STUFF() function to remove the leading comma.

#### 5. How can you identify projects by finding consecutive start and end dates in a task table?
**Answer:**
To identify consecutive projects, you can use row numbering on sets of start dates (those not existing as end dates) and end dates (those not existing as start dates). Joining these two sets on the assigned row IDs aligns the start and end of each unique project sequence.

#### 6. How do you pivot data in SQL?
**Answer:**
Use the PIVOT operator. It rotates rows into columns by aggregating values (e.g., SUM) based on a specific category column.

#### 7. Is recursion with aggregation allowed in the SQL standard?
**Answer:**
No, recursion with aggregation is generally disallowed in the SQL standard because it creates ambiguity regarding what the resulting statement should return.

#### 8. SQL Recursive Queries (WITH)
**Answer:**
Recursive CTEs (using WITH RECURSIVE) allow for unbounded computations, such as traversing hierarchical data (e.g., org charts or ancestor trees). They stop when an iteration produces no new results. Negatively dependent recursion and aggregation within recursion are generally disallowed in standard SQL.

#### 9. What is the difference between 'WITH CUBE' and 'WITH ROLLUP' in SQL data warehousing?
**Answer:**
WITH CUBE generates all possible sub-total combinations for the specified attributes. WITH ROLLUP creates hierarchical subtotals, which is more efficient for data with a natural functional dependency (e.g., City -> County -> State).


## 📂 Category: Transactions & Concurrency (28 cards)

### 🔴 Senior Level

#### 1. Co je to latch?
**Answer:**
Mechanismus fyzického zamykání stránek v paměti pro zajištění konzistentního přístupu více vláken vykonávacího enginu.

#### 2. Does serializability guarantee a specific execution order?
**Answer:**
No, serializability guarantees that the final state is equivalent to some serial order of execution, but it does not dictate which specific order. If a specific order is required, it must be handled by the application logic.

#### 3. How is transaction isolation level scope defined?
**Answer:**
The isolation level is defined per transaction and operates under the 'eye of the beholder' principle, meaning each transaction's read operations must strictly adhere to its specific isolation level requirements.

#### 4. How large is a lock structure?
**Answer:**
96 bytes.

#### 5. How much overhead does the 'read committed snapshot' isolation option add per row?
**Answer:**
14 bytes per row for the version pointer.

#### 6. How should database transactions be designed regarding locks?
**Answer:**
Transactions should be designed to execute as quickly as possible to minimize holding locks, thereby reducing contention and preventing deadlocks. They should avoid waiting for human input.

#### 7. What are the ACID properties in a database?
**Answer:**
ACID properties ensure reliable transaction processing: Atomicity (all or nothing), Consistency (maintains integrity rules), Isolation (prevents concurrent transaction interference), and Durability (committed data survives crashes).

#### 8. What are the ACID properties in a database?
**Answer:**
ACID is an acronym for the four key properties of a transaction: Atomicity (all operations succeed or the entire transaction is rolled back), Consistency (the database remains in a valid state), Isolation (transactions occur independently), and Durability (committed changes persist despite system failures).

#### 9. What are the common transaction isolation levels?
**Answer:**
The standard isolation levels include Read Uncommitted, Read Committed, Repeatable Read, and Serializable. Additionally, some systems implement Read Only for optimization purposes.

#### 10. What are the possible states of a worker thread in a database engine?
**Answer:**
The typical states for a worker thread are: running, runnable (waiting for a processor), and suspended (waiting for a resource).

#### 11. What are the properties of the 'Read Committed' isolation level?
**Answer:**
It prevents dirty reads, but allows non-repeatable reads. A row read multiple times might change value if another transaction commits an update in between.

#### 12. What are the properties of the 'Repeatable Read' isolation level?
**Answer:**
It prevents dirty reads and ensures that an item read multiple times within the same transaction will not change value. However, it allows 'phantom reads' where new rows inserted by other transactions can appear.

#### 13. What are the two primary motivations for implementing database transactions?
**Answer:**
Transactions are motivated by two independent concepts: Concurrency control and Resilience against system failure.

#### 14. What do LOCK_TIMEOUT settings of -1 and 0 mean in SQL Server?
**Answer:**
LOCK_TIMEOUT = -1 means the session will wait indefinitely for a lock. LOCK_TIMEOUT = 0 means the session will immediately return an error if a lock cannot be acquired without waiting.

#### 15. What does the Atomicity property guarantee in a database transaction?
**Answer:**
Atomicity guarantees an 'all-or-nothing' approach: the entire transaction completes successfully, or if it fails, the database rolls back to the state before the transaction began.

#### 16. What is a 'dirty read' in database transactions?
**Answer:**
A dirty read occurs when a transaction reads data that has been modified by another concurrent transaction but has not yet been committed.

#### 17. What is a 'quantum' in the context of database engine scheduling?
**Answer:**
A quantum is the largest amount of time (typically 4 ms) that one worker thread can consecutively run on a single processor before being preempted.

#### 18. What is lock escalation and how can it be managed?
**Answer:**
Lock escalation occurs when the number of locks on an object exceeds a threshold (e.g., 5000 in SQL Server), causing the engine to convert fine-grained locks (row or page) into a coarser-grained lock (table). This can be managed by keeping transactions short or using query hints like ROWLOCK or PAGLOCK.

#### 19. What is the 'Read Committed Snapshot' isolation level?
**Answer:**
In this isolation level, data is copied to tempdb before being read, allowing for consistent reads without blocking write operations.

#### 20. What is the difference between DELETE+OUTPUT and SELECT+DELETE?
**Answer:**
DELETE+OUTPUT is an atomic operation that returns the deleted rows within a single statement. SELECT+DELETE requires a manual transaction to ensure consistency, which can lead to row locking and blocking issues.

#### 21. What is the difference between READ ONLY and READ WRITE transaction qualifiers?
**Answer:**
These qualifiers indicate the nature of a transaction: READ ONLY specifies that the transaction will only perform read operations, while READ WRITE indicates that the transaction involves both read and write operations.

#### 22. What is the difference between the SQL standard transaction level and actual DBMS default implementations?
**Answer:**
While 'Serializable' is the SQL standard default, most modern DBMS implementations use weaker isolation levels by default for performance (e.g., Oracle uses Read Committed, MySQL uses Repeatable Read).

#### 23. What is the formal definition of Isolation/Serializability in transactions?
**Answer:**
Serializability guarantees that even if operations are interleaved, the final outcome must be equivalent to some sequential (serial) order of transactions. It ensures transactions appear to execute atomically and in isolation.

#### 24. What is the function of the command: ALTER DATABASE ... WITH ROLLBACK IMMEDIATE?
**Answer:**
This command kills all currently running transactions/queries in a database and prevents new ones from starting until the requested database operation is completed.

#### 25. What is the role of Consistency in database transactions?
**Answer:**
Consistency ensures that all constraints and rules are satisfied before and after a transaction, maintaining valid data states throughout.

#### 26. What is the trade-off when using weaker transaction isolation levels?
**Answer:**
Weaker isolation levels (e.g., Read Uncommitted, Read Committed, Repeatable Read) reduce overhead and increase concurrency, but at the cost of reduced consistency and lower data guarantees.

#### 27. When does a deadlock occur in SQL Server?
**Answer:**
A deadlock occurs when two or more processes hold locks on resources the other process requires, creating a circular dependency where no process can proceed. The SQL Server engine typically detects this and terminates one of the processes as a deadlock victim.

#### 28. Which isolation level allows for 'dirty reads'?
**Answer:**
The Read Uncommitted isolation level allows transactions to perform dirty reads.

