# Final Consolidated SQL & Database Knowledge Base

A professionally structured study guide compiled from multiple Anki decks, deduplicated semantically, categorized, and graded by difficulty.

## Deck Metrics
- **Original Deck Cards**: 1903
- **Final Deduplicated Cards**: 1047

---

## 📂 Category: Advanced & Distributed Databases (50 cards)

### 🟢 Junior Level

#### 1. What is a Cloud Database?
**Answer:**
A database service created and maintained on a cloud infrastructure platform (such as Azure, AWS, or GCP) rather than on-premises hardware.


### 🟡 Mid Level

#### 1. Compare OLAP and OLTP.
**Answer:**
OLTP (Online Transactional Processing) is designed for fast, frequent, short-lived transactions. OLAP (Online Analytical Processing) is designed for complex, read-heavy analytical queries over large datasets, often utilizing aggregations and materialized views for performance.

#### 2. Define Drill-down and Roll-up operations in OLAP.
**Answer:**
Drill-down involves moving from summarized data to more granular levels by adding attributes to the GROUP BY clause. Roll-up moves from granular data to higher-level summaries by removing attributes from the GROUP BY clause.

#### 3. Explain Document, Graph, and Key/Value databases.
**Answer:**
Document (e.g., MongoDB): Stores semi-structured data in JSON/XML; flexible schema. Graph (e.g., Neo4j): Focuses on relationships between entities (nodes/edges). Key/Value (e.g., Redis): Simplest model; optimized for extremely fast reads/writes via a unique key.

#### 4. Explain the XPath expression //Book[@Price < 90].
**Answer:**
// selects all Book elements at any level in the document, and [@Price < 90] filters those elements where the Price attribute is less than 90.

#### 5. Explain the differences between Slicing and Dicing in OLAP cubes.
**Answer:**
Slicing constrains the analysis to a single dimension (e.g., filtering on one attribute). Dicing constrains the analysis to multiple dimensions, effectively extracting a sub-cube by applying multiple filtering criteria simultaneously.

#### 6. How can XML data be displayed using rule-based languages?
**Answer:**
XML can be transformed for display using Cascading Style Sheets (CSS) or Extensible Stylesheet Language (XSL).

#### 7. How does XML schema flexibility compare to the Relational model?
**Answer:**
XML schemas are significantly more flexible than the rigid, predefined schemas found in the Relational model.

#### 8. How does XML structure data?
**Answer:**
XML expresses data as a tree structure.

#### 9. How does XPath query data?
**Answer:**
XPath queries data using paths combined with predicates/conditions to filter elements (e.g., doc('file.xml')/root/element[condition=value]).

#### 10. In XSLT, how is the current element referenced?
**Answer:**
The current element is referenced using the '.' character.

#### 11. What are Cubes and OLAP?
**Answer:**
OLAP (Online Analytical Processing) is a category of software for multi-dimensional data analysis. An OLAP Cube is a data structure that allows for fast analysis of data by organizing it into dimensions (attributes) and measures (quantitative values) for rapid reporting.

#### 12. What are some common types of non-relational (NoSQL) databases?
**Answer:**
Common types include Key-value databases, Document databases, and Graph databases.

#### 13. What are the basic constructs of XML?
**Answer:**
XML consists of nested tagged elements, attributes, and text content.

#### 14. What are the basic constructs used in XPath?
**Answer:**
They include: '/' (root/separator), 'name' (match element), '*' (wildcard), '@attr' (attribute), '//' (descendant), '[condition]' (filtering), and '[index]' (positional index).

#### 15. What is the difference between 'well-formed' and 'valid' XML?
**Answer:**
A 'well-formed' XML file adheres to basic syntax constructs, while a 'valid' XML file must additionally adhere to a formal schema (DTD or XSD).

#### 16. What is the difference between data mining and data warehousing, and what are common warehouse application types?
**Answer:**
Data warehousing is the process of aggregating data from multiple sources into a common repository for analysis. Data mining is the process of extracting hidden predictive patterns from that data. Applications include Info Processing, Analytical Processing, and Data Mining.


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


## 📂 Category: Basic SQL & Syntax (301 cards)

### 🟢 Junior Level

#### 1. Analyze common SQL syntax errors regarding DDL and DML operations.
**Answer:**
Common errors include: omitting required keywords (e.g., 'TABLE' or 'INTO'), mismatching column counts during INSERT, inserting invalid data types into columns (e.g., string into date), or attempting to manipulate data in a table that has not been created or lacks the correct schema definition.

#### 2. Can a primary key consist of multiple attributes?
**Answer:**
Yes, a key can be composed of one or several attributes (columns), which is then referred to as a composite key.

#### 3. Can you query a table using only schema.name (e.g., HumanResources.Employee)?
**Answer:**
Yes, provided that the query window or session is already connected to the database containing that specific schema and table.

#### 4. Can you sort a column using a column alias?
**Answer:**
Yes, you can use the column alias in the ORDER BY clause to specify the sorting order of the result set.

#### 5. Define SQL.
**Answer:**
Structured Query Language (SQL) is the standard language for relational database management systems. It is used for data manipulation (CRUD), data definition (DDL), and data control (DCL).

#### 6. Define a 'Query' and 'Query Language' in the context of a DBMS.
**Answer:**
A Query is a request for data manipulation or information issued by a user or application. A Query Language is a declarative language (like SQL) used by the DBMS to interpret and execute these requests.

#### 7. Define the following SQL DDL and DML commands: CREATE DATABASE, CREATE TABLE, CREATE INDEX, DROP TABLE, SELECT, INSERT INTO, UPDATE, and ALTER DATABASE.
**Answer:**
CREATE DATABASE: Creates a new database. CREATE TABLE: Creates a new table. CREATE INDEX: Creates an index for faster lookups. DROP TABLE: Deletes a table. SELECT: Extracts data. INSERT INTO: Adds new data. UPDATE: Modifies existing data. ALTER DATABASE: Modifies database structure/settings.

#### 8. Define the relationship between a foreign key and a primary key.
**Answer:**
A foreign key is a field (or collection of fields) in one table that uniquely identifies a row of another table by pointing to its primary key.

#### 9. Define the terms 'data', 'information', 'database', and 'DBMS'.
**Answer:**
Data refers to raw facts. Information is data processed to have meaning. A database is a set of logically related data (including metadata). A DBMS is the software that manages database structures and controls data access.

#### 10. Describe the basic components of a relational database structure.
**Answer:**
A database contains a set of relations (tables), which are defined by a schema (name and columns). This schema is instantiated with a set of tuples (rows).

#### 11. Describe your experience as a SQL Server DBA.
**Answer:**
This is a behavioral interview question. You should discuss the specific SQL Server versions managed, your experience with instance administration (backups, security, disaster recovery), performance tuning, and how your responsibilities directly contributed to project goals and business stability.

#### 12. Explain date/time data types (date, datetime, datetime2) and ISO8601 formatting.
**Answer:**
ISO8601 format is YYYY-MM-DD HH:MM:SS.000. 'date' stores only the date. 'datetime' stores date and time with millisecond precision. 'datetime2' offers higher precision for date and time. Inserting an incompatible format (e.g., time into a date column) causes a conversion error.

#### 13. Explain the AND, OR, and NOT logical operators.
**Answer:**
AND displays a record if all conditions are true. OR displays a record if at least one condition is true. NOT displays a record if the specified condition is false.

#### 14. Explain the BETWEEN operator and provide an example.
**Answer:**
The BETWEEN operator selects values within a given range. The values are inclusive. Example: 'SELECT * FROM movies WHERE name BETWEEN 'A' AND 'J';' will return all movies starting with letters A through J, including those starting with exactly 'A' or 'J'.

#### 15. Explain the LIKE operator and provide an example.
**Answer:**
LIKE is an operator used in a WHERE clause to search for a specified pattern in a column. The '%' wildcard represents zero, one, or multiple characters, while '_' represents a single character. Example: 'SELECT * FROM movies WHERE name LIKE 'se_en';' finds names like 'seven' or 'semen'.

#### 16. Explain the comparison, null, pattern match, range, and set membership conditions in a WHERE clause.
**Answer:**
Comparison: Compares an expression to another. Null: Tests if a value is unknown. Pattern match: Checks if a string matches a specific format (e.g., LIKE). Range: Checks if a value falls within a specific span (e.g., BETWEEN). Set membership: Checks if a value exists within a provided set (e.g., IN).

#### 17. Explain the primary SQL clauses: SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY.
**Answer:**
SELECT: Specifies columns to return. FROM: Specifies tables. WHERE: Filters individual rows. GROUP BY: Groups rows by column values. HAVING: Filters groups. ORDER BY: Sorts the final result set.

#### 18. How are SQL comments implemented?
**Answer:**
Single-line comments are designated by '--'. Anything following these characters on the same line is ignored by the database engine.

#### 19. How are column concatenation and aliasing performed in SQL?
**Answer:**
You can combine column values using the concatenation operator (such as '+') and assign a new label to the resulting output column using the 'AS' keyword.

#### 20. How are multi-line comments written in SQL?
**Answer:**
Multi-line comments start with '/*' and end with '*/'. Any text placed between these delimiters is ignored by the SQL engine.

#### 21. How can you temporarily rename a table or a column heading?
**Answer:**
Using SQL Aliases (typically via the AS keyword).

#### 22. How can you validate if a string represents a valid date?
**Answer:**
Use the ISDATE(expression) function, which returns 1 if the expression is a valid date format and 0 otherwise.

#### 23. How do NOT BETWEEN and NOT IN operators work in SQL?
**Answer:**
These operators negate range or inclusion conditions. NOT BETWEEN excludes values in the defined range (inclusive of boundaries). NOT IN excludes all values matching the provided list. They are often combined with other logical operators to filter results.

#### 24. How do you add a new column to an existing table?
**Answer:**
Use the ALTER TABLE statement: ALTER TABLE table_name ADD COLUMN column_name data_type;

#### 25. How do you add a new row to a database table?
**Answer:**
Use the INSERT INTO statement: INSERT INTO table_name (col1, col2) VALUES (val1, val2);

#### 26. How do you calculate the difference between two dates and how do you add intervals to a date?
**Answer:**
Use DATEDIFF(interval, start_date, end_date) to find the difference between two dates in the specified interval. Use DATEADD(interval, number, date) to add a specified number of intervals to a date.

#### 27. How do you check for NULL values in SQL?
**Answer:**
Use the IS NULL operator in the WHERE clause: SELECT column_names FROM table_name WHERE column_name IS NULL;

#### 28. How do you check for non-null values in SQL?
**Answer:**
Use the IS NOT NULL operator in the WHERE clause: SELECT column_names FROM table_name WHERE column_name IS NOT NULL;

#### 29. How do you connect to a specific database in PostgreSQL?
**Answer:**
Use the command \c database_name.

#### 30. How do you create a table in SQL?
**Answer:**
The CREATE TABLE statement defines a table's structure with column names and data types. You can also create a new table based on the structure and data of an existing table using 'CREATE TABLE new_table AS SELECT ... FROM existing_table'.

#### 31. How do you create and drop databases in SQL?
**Answer:**
Use 'CREATE DATABASE databasename;' to create a new database. Use 'DROP DATABASE databasename;' to permanently remove an existing database. Be cautious, as dropping a database results in the loss of all data contained within it.

#### 32. How do you create and drop tables in SQL?
**Answer:**
Use 'CREATE TABLE table_name (column1 datatype, column2 datatype, ...);' to define a new table structure. Use 'DROP TABLE table_name;' to remove a table and its associated data entirely. Be cautious, as this action cannot be undone.

#### 33. How do you create tables with primary keys and foreign key constraints in SQL?
**Answer:**
Use the CREATE TABLE statement specifying the column types and PRIMARY KEY constraints. Foreign key constraints are added using the REFERENCES keyword, often defined at the table or column level.

#### 34. How do you define the database context for a query?
**Answer:**
Use the USE command (e.g., 'USE database_name;').

#### 35. How do you drop common database constraints?
**Answer:**
Constraints are removed using ALTER TABLE statements. For example: 'ALTER TABLE table_name DROP CONSTRAINT constraint_name' (Syntax varies by RDBMS; e.g., MySQL often uses 'DROP FOREIGN KEY' or 'DROP PRIMARY KEY').

#### 36. How do you exclude a character from your result set?
**Answer:**
Use the NOT operator within the LIKE clause and brackets. For example: SELECT * FROM Employee WHERE LastName LIKE 'O[^S]%'.

#### 37. How do you extract components (Year, Month, Day) from a date, and how do you reconstruct a date or datetime from those parts?
**Answer:**
Use functions like YEAR(), MONTH(), or DAY() to extract parts. Use DATEPART(part, date) for more flexible extraction. To reconstruct, use DATEFROMPARTS(year, month, day) or DATETIMEFROMPARTS(year, month, day, hour, min, sec, ms).

#### 38. How do you filter data using basic comparison, logical operators (AND/OR), and 'IN' clauses?
**Answer:**
Use the WHERE clause with operators like '=', '<>', '>', 'IN', 'AND', and 'OR'. Note that 'AND' requires both conditions to be true, while 'OR' requires at least one. Using 'IN' is a cleaner alternative to multiple OR statements (e.g., ID IN ('1', '2')).

#### 39. How do you filter records based on NULL values or empty spending (Samnt)?
**Answer:**
To find records with missing data, use 'IS NULL' or 'IS NOT NULL'. To identify customers who haven't spent money, use 'WHERE Samnt = 0 OR Samnt IS NULL'. To find those who have spent, use 'WHERE Samnt > 0' or 'WHERE NOT (Samnt = 0 OR Samnt IS NULL)'.

#### 40. How do you filter rows in a SQL table based on specific conditions for numeric values, null values, or patterns?
**Answer:**
Use the WHERE clause with operators: '=' for exact, '<', '>', '<=', '>=', '<>' for comparisons, 'LIKE' for pattern matching (e.g., % for wildcards), and 'IS NULL' or 'IS NOT NULL' to check for null values.

#### 41. How do you find employee names starting with 'A'?
**Answer:**
SELECT * FROM Table_name WHERE EmpName LIKE 'A%'

#### 42. How do you handle column names with spaces in SQL?
**Answer:**
Use double quotes ("alias") or square brackets ([alias]) to delimit the column name.

#### 43. How do you handle special characters like a single quote in a string literal?
**Answer:**
Use an escape character by doubling the single quote (e.g., 'Mc''Donald').

#### 44. How do you match characters not specified within brackets in a SQL pattern match?
**Answer:**
Use the [^charlist] or [!charlist] syntax within the LIKE operator to exclude specific characters.

#### 45. How do you modify existing data in a table?
**Answer:**
The UPDATE statement is used to change existing values in one or more columns of a table.

#### 46. How do you modify table structure using the ALTER TABLE command?
**Answer:**
ALTER TABLE is used to modify the structure of an existing table. Common operations include: ADD COLUMN (to add a field), DROP COLUMN (to remove a field), and ALTER/MODIFY COLUMN (to change a field's data type). Syntax varies slightly by vendor (e.g., SQL Server vs. MySQL).

#### 47. How do you perform pattern matching in SQL?
**Answer:**
The LIKE clause is used with wildcard characters (like % or _) to search for a specific pattern in a string column.

#### 48. How do you query a subset of columns from a table?
**Answer:**
Specify the required column names in the SELECT clause: SELECT col1, col2 FROM table_name;

#### 49. How do you query for a single quote inside a string literal?
**Answer:**
You must escape the single quote by adding another single quote before it. Example: SELECT * FROM Grant WHERE GrantName LIKE '%' '%'.

#### 50. How do you query for multiple characters using wildcards?
**Answer:**
Use brackets to define character sets or ranges. Examples: LIKE '[ABCDE]%' or LIKE '[A-K]%'.

#### 51. How do you query for unique values in a specific column?
**Answer:**
Use the DISTINCT keyword: SELECT DISTINCT column_name FROM table_name;

#### 52. How do you rename columns when using SELECT INTO to create a new table?
**Answer:**
You can use the AS clause to alias column names in the output table.

#### 53. How do you retrieve the three lowest rated movies?
**Answer:**
SELECT * FROM movies ORDER BY imdb_rating ASC LIMIT 3;

#### 54. How do you retrieve unique values from a column?
**Answer:**
Use the 'DISTINCT' keyword before the column name (e.g., 'SELECT DISTINCT City FROM Clients'). This removes duplicate values from the result set, returning only unique entries for the specified column.

#### 55. How do you select values within a range in SQL?
**Answer:**
Using the BETWEEN operator.

#### 56. How do you store special characters (like Chinese or other non-Latin scripts) in a database table?
**Answer:**
You should use Unicode-aware data types, such as 'nvarchar' in MS SQL, which are specifically designed to store characters from any language.

#### 57. How do you switch the Postgres CLI to vertical output mode?
**Answer:**
Use the command \x to toggle the display format of query results to a vertical list of columns.

#### 58. How do you test for NULL values in SQL?
**Answer:**
You cannot use standard comparison operators (=). Instead, use the 'IS NULL' or 'IS NOT NULL' operators.

#### 59. How do you update an existing row in a database table?
**Answer:**
Use the UPDATE statement with a WHERE clause: UPDATE table_name SET col1 = val1 WHERE id = x;

#### 60. How do you use the SQL DELETE statement?
**Answer:**
The DELETE statement is used to remove records from a table using 'DELETE FROM table_name WHERE condition;'. Omitting the WHERE clause will delete all rows in the table. While it removes the data, the table structure and attributes remain intact.

#### 61. How do you write comments in SQL?
**Answer:**
Use double hyphens (--) for single-line comments.

#### 62. How does the BETWEEN operator work in a WHERE clause?
**Answer:**
The BETWEEN operator selects values within a given range (inclusive). For strings, it uses alphabetical order; for numbers, it uses numerical value. The NOT BETWEEN operator selects values outside that range.

#### 63. How does the LIKE operator use wildcards?
**Answer:**
The LIKE clause uses two primary wildcards: '%' (percent), which matches any sequence of characters (including zero characters), and '_' (underscore), which matches exactly one single character.

#### 64. How does the LIKE operator work for pattern matching in SQL?
**Answer:**
The LIKE operator is used for partial string matching. '%' acts as a wildcard representing zero or more characters. 'Herb%' matches strings starting with 'Herb', '%Simpson' matches strings ending with 'Simpson', and '%Bart%' matches strings containing 'Bart'. Omitting wildcards (e.g., LIKE 'Simpson') behaves like equality.

#### 65. How does the WHERE clause function in SQL?
**Answer:**
The WHERE clause is used to filter records that meet a specified condition. It supports operators such as =, <>, >, <, >=, <=, BETWEEN, LIKE, and IN, and can be combined using AND, OR, and NOT logical operators.

#### 66. How should you correctly identify NULL values in SQL?
**Answer:**
Always use the 'IS NULL' operator to check for null values (e.g., WHERE column IS NULL). Avoid using '= NULL' as it is not standard SQL syntax.

#### 67. How to delete records with empty values in a specific column?
**Answer:**
Use the DELETE statement with an IS NULL condition: DELETE FROM celebs WHERE twitter_handle IS NULL;

#### 68. How to enumerate over a set for multiple values in a query?
**Answer:**
Use the IN operator. For example: SELECT * FROM Employee WHERE FirstName IN ('Lisa', 'David').

#### 69. How to remove duplicates from a SELECT result set?
**Answer:**
Use the DISTINCT keyword: SELECT DISTINCT column_name FROM table_name.

#### 70. How to sort results by a specific column?
**Answer:**
Use the ORDER BY clause, optionally specifying ASC or DESC: SELECT * FROM movies ORDER BY imdb_rating DESC;

#### 71. In boolean logic, how do TRUE and FALSE compare, and what is the result of comparing a value with NULL or an UNKNOWN state?
**Answer:**
TRUE is greater than FALSE. Any comparison involving NULL or an UNKNOWN truth value results in an UNKNOWN result.

#### 72. In the relational model, what determines the domain of values for an attribute?
**Answer:**
Each attribute has an associated data type (e.g., INTEGER, VARCHAR, ENUM) which defines the domain of valid values for that attribute.

#### 73. Is the order of clauses in an SQL SELECT statement flexible?
**Answer:**
No, the order of clauses in a SELECT statement is strictly defined (e.g., SELECT, FROM, JOIN, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT) and cannot be changed.

#### 74. Jak se v SQL řadí výsledky?
**Answer:**
K seřazení výsledků se používá klauzule 'ORDER BY'. Pro sestupné řazení se přidává klíčové slovo 'DESC'.

#### 75. List 10 valid operators in SQL.
**Answer:**
The following are 10 valid SQL operators: =, !=, >, <, >=, <=, LIKE, BETWEEN, AND, OR.

#### 76. List common RDBMS that use SQL.
**Answer:**
Common RDBMS include MySQL, PostgreSQL, Microsoft SQL Server, Oracle Database, SQLite, and IBM Db2.

#### 77. Provide an example of a multiple filter BETWEEN statement in SQL.
**Answer:**
SELECT * FROM movies WHERE year BETWEEN 1990 AND 2000 AND genre = 'comedy';

#### 78. Provide examples of basic CRUD and schema modification operations using the Clients table.
**Answer:**
Filtering: 'SELECT * FROM Clients WHERE City = 'Springfield''; Updating: 'UPDATE Clients SET City = 'Springfield' WHERE Cname LIKE '%herb%';' (Note: Always use a WHERE clause to avoid mass updates); Altering: 'ALTER TABLE Clients ADD Comments nvarchar(400) NULL;'

#### 79. SQL INSERT INTO Statement
**Answer:**
The INSERT INTO statement adds new records to a table. You can specify columns: INSERT INTO table_name (col1, col2) VALUES (val1, val2); or insert into all columns by omitting names, provided the values follow the table's defined column order.

#### 80. SQL LIKE Operator and Wildcards
**Answer:**
The LIKE operator is used in a WHERE clause to search for patterns. Wildcards: '%' represents zero, one, or multiple characters; '_' represents a single character. Combined with LIKE, these allow for flexible string matching, such as starting/ending characters or containing substrings.

#### 81. SQL TOP/LIMIT/ROWNUM
**Answer:**
These clauses limit the number of records returned by a query. Syntax varies by vendor: SQL Server uses TOP, MySQL/PostgreSQL use LIMIT, and Oracle historically uses ROWNUM or FETCH FIRST.

#### 82. True or False: A PRIMARY KEY can consist of more than one column.
**Answer:**
True. This is known as a composite primary key.

#### 83. True or False: The BETWEEN operator behaves identically across all database systems.
**Answer:**
False. Implementations vary; some databases include both boundary values, while others may exclude one or both. Always check specific vendor documentation.

#### 84. What SQL commands are used to filter result sets?
**Answer:**
Common commands for filtering include: SELECT DISTINCT, WHERE, LIMIT, BETWEEN, LIKE, and ORDER BY.

#### 85. What are SQL Aliases?
**Answer:**
Aliases are temporary names assigned to tables or columns for the duration of a query. They are used to improve readability, handle column name conflicts in joins, or represent calculated fields.

#### 86. What are SQL Compound Operators?
**Answer:**
Compound operators perform a mathematical operation and an assignment simultaneously (e.g., += for addition, -= for subtraction, *= for multiplication, /= for division, %= for modulo, etc.).

#### 87. What are SQL Wildcards?
**Answer:**
Wildcards are used with the LIKE operator to search for specific patterns in strings. '%' represents zero or more characters, and '_' represents a single character. Specific implementations (like SQL Server or Access) also support character lists using square brackets like [a-c] or [!charlist].

#### 88. What are approximate numeric data types used for?
**Answer:**
Approximate numeric data types (like FLOAT or REAL) are used to store floating-point numbers that do not have an exact decimal representation, useful for scientific calculations where extreme precision is not required.

#### 89. What are database constraints and why are they used?
**Answer:**
Constraints are rules or types applied to table columns that restrict the data being entered. They are essential for ensuring data integrity and consistency within the database.

#### 90. What are precision and scale in the context of SQL data types?
**Answer:**
Precision and scale are characteristics of exact numeric data types (such as DECIMAL or NUMERIC). Precision is the total number of digits, while scale is the number of digits to the right of the decimal point.

#### 91. What are some standard SQL data types?
**Answer:**
Standard SQL data types include character strings (CHAR, VARCHAR), numeric types (INT, FLOAT, REAL, DECIMAL), and temporal types (DATE, TIME).

#### 92. What are tables in the context of a database?
**Answer:**
Tables are named database objects organized into rows and columns used to store data.

#### 93. What are the AND and OR operators in SQL?
**Answer:**
AND displays a record if both conditions are true. OR displays a record if either condition is true.

#### 94. What are the GRANT and REVOKE statements used for?
**Answer:**
The GRANT statement is used by an owner to grant specific privileges to a user, while the REVOKE statement is used to remove those privileges.

#### 95. What are the SQL statements used to modify table data?
**Answer:**
The three statements for modifying content are: INSERT, UPDATE, and DELETE.

#### 96. What are the SQL wildcards for pattern matching?
**Answer:**
The underscore (_) is a substitute for a single character, and the percent sign (%) is a substitute for zero or more characters.

#### 97. What are the basic CRUD operations in SQL?
**Answer:**
The basic operations are: INSERT (create/add rows), SELECT (retrieve/read rows), UPDATE (modify values in existing rows), and DELETE (remove rows).

#### 98. What are the characteristics of the decimal(p, s) data type in MS SQL?
**Answer:**
Decimal(p, s) defines precision (p) as the total number of digits and scale (s) as the number of digits to the right of the decimal point. For example, 22342.33 is decimal(18,2).

#### 99. What are the common SQL date and time types?
**Answer:**
The five common types are: DATE, TIME, DATETIME, TIMESTAMP, and YEAR.

#### 100. What are the common string manipulation functions in SQL (LEN, LEFT, RIGHT, SUBSTRING, CHARINDEX, CONCAT, REPLACE, STUFF, LTRIM, RTRIM)?
**Answer:**
These are essential string functions: LEN (length of string), LEFT/RIGHT (extract part from sides), SUBSTRING (extract part based on start and length), CHARINDEX (find starting position of a character/string), CONCAT (merge strings), REPLACE (find and replace substrings), STUFF (replace a part based on position), and LTRIM/RTRIM (remove whitespace).

#### 101. What are the core elements of SQL?
**Answer:**
SQL is categorized into: DDL (Data Definition Language - schema), DML (Data Manipulation Language - data), and DCL (Data Control Language - security).

#### 102. What are the fundamental CRUD statements for a table?
**Answer:**
CREATE TABLE (defines structure), INSERT INTO (adds rows), SELECT (retrieves data), UPDATE (modifies data), DELETE (removes data), and DROP TABLE (deletes the table structure).

#### 103. What are the fundamental characteristics of Relational databases?
**Answer:**
Relational databases store data in two-dimensional tables consisting of rows and columns. They are based on relational algebra and set theory, using formal operations to retrieve and manipulate information.

#### 104. What are the main string data types in MS SQL and their primary characteristics?
**Answer:**
The main string types are 'varchar' and 'nvarchar'. 'nvarchar' supports Unicode characters. The length (e.g., nvarchar(10), nvarchar(max)) defines the storage capacity. Length is determined by the number of characters, not bytes.

#### 105. What are the mandatory clauses in a SELECT statement?
**Answer:**
The SELECT and FROM clauses are mandatory.

#### 106. What are the most basic elements/objects of a relational database?
**Answer:**
Tables are the primary objects. Key components include: Column names (table headers), Rows (records), Values (conforming to defined data types), and NULL values (representing missing or empty information).

#### 107. What are the primary SQL DDL commands?
**Answer:**
DDL includes CREATE, ALTER, and DROP commands for Schemas, Tables, Views, and Domains.

#### 108. What are the primary SQL commands used to modify the contents of a database table?
**Answer:**
The commands INSERT (add new rows), UPDATE (modify existing rows), and DELETE (remove rows) are used to manipulate the data stored within a database table.

#### 109. What are the primary subsets of SQL?
**Answer:**
DDL (Data Definition Language) for structure (CREATE, ALTER, DROP); DML (Data Manipulation Language) for content (SELECT, INSERT, UPDATE, DELETE); and DCL (Data Control Language) for security (GRANT, REVOKE).

#### 110. What are the three main areas of SQL statements?
**Answer:**
1. Data Definition Language (DDL) for structure, 2. Data Manipulation Language (DML) for data access/modification, 3. Data Control Language (DCL) for access permissions.

#### 111. What are the three main categories of data types in relational databases?
**Answer:**
The three main categories are: 1. String (char, varchar, nvarchar), 2. Numeric (int, decimal, float), and 3. Date and Time (date, datetime, datetime2).

#### 112. What comes right after the WHERE clause?
**Answer:**
The predicate (a logical condition used to filter rows).

#### 113. What commands represent DCL?
**Answer:**
Data Control Language (DCL) commands control access to data stored in the database. Examples include GRANT and REVOKE.

#### 114. What commands represent DDL?
**Answer:**
Data Definition Language (DDL) commands define or change the database schema. Examples include CREATE, ALTER, and DROP.

#### 115. What commands represent DML?
**Answer:**
Data Manipulation Language (DML) commands are used for managing data within database objects. Examples include SELECT, INSERT, UPDATE, and DELETE.

#### 116. What data type do we use when we want to define points in time to a certain degree of accuracy?
**Answer:**
Date and Time data types (e.g., DATETIME, TIMESTAMP, DATE).

#### 117. What data type represents truth values?
**Answer:**
The Boolean data type, which holds the values TRUE and FALSE.

#### 118. What data types can be used with the BETWEEN operator?
**Answer:**
BETWEEN can be used to select a range of numbers, text, or dates.

#### 119. What do SQL commands INSERT, SELECT, UPDATE, and DELETE do?
**Answer:**
INSERT adds a new record, SELECT retrieves data, UPDATE modifies existing records, and DELETE removes records from a table.

#### 120. What do the 'data_type' and 'size' parameters specify in a CREATE TABLE statement?
**Answer:**
The data_type defines the category of data the column can hold (e.g., VARCHAR, INTEGER, DATE). The size parameter specifies the maximum length or storage capacity for that column (e.g., the number of characters for a string).

#### 121. What do the UPDATE, ALTER, CREATE, and DROP commands do?
**Answer:**
CREATE creates a new database object (table, view, etc.). ALTER modifies an existing database object. DROP removes an entire object from the database. UPDATE modifies existing data records within a table.

#### 122. What do you call the output returned from a SELECT statement?
**Answer:**
A result set.

#### 123. What do you mean by table and field in SQL?
**Answer:**
A table is a collection of data organized in rows and columns. A field refers to a specific column within that table.

#### 124. What does 'CREATE DATABASE my_db;' do?
**Answer:**
It initializes and creates a new database named 'my_db' within the SQL server instance.

#### 125. What does CRUD stand for in database operations?
**Answer:**
CRUD stands for Create (INSERT), Read (SELECT), Update (UPDATE), and Delete (DELETE). These are the four fundamental operations for persistent data management.

#### 126. What does GRANT and REVOKE do?
**Answer:**
GRANT gives a specific privilege to a user; REVOKE removes a previously granted privilege from a user.

#### 127. What does RDBMS stand for?
**Answer:**
Relational Database Management System.

#### 128. What does SCOPE_IDENTITY() return?
**Answer:**
It returns the last identity value generated in the current session and the current scope.

#### 129. What does SQL mainly allow us to do?
**Answer:**
SQL allows us to: 1. Execute queries and retrieve data from a database, 2. Insert rows into tables, 3. Update rows in tables, 4. Delete rows from tables, 5. Create new databases, 6. Create new tables, 7. Create stored procedures, 8. Create views, 9. Set permissions on tables, procedures, and views.

#### 130. What does SQL stand for?
**Answer:**
Structured Query Language.

#### 131. What does a bit string consist of?
**Answer:**
A sequence of binary digits, limited to the values 0 and 1.

#### 132. What does character data consist of?
**Answer:**
A sequence of characters from an implementation-defined character set (typically defined using CHAR or VARCHAR types).

#### 133. What does the LIMIT clause do in a SQL query?
**Answer:**
The LIMIT clause constrains the number of rows returned by a query.

#### 134. What does the acronym CRUD stand for?
**Answer:**
CRUD stands for Create, Read, Update, and Delete, representing the four basic operations for persistent data storage.

#### 135. What does the query 'SELECT * FROM Customers WHERE City LIKE 's%'' perform?
**Answer:**
It selects all columns from the Customers table for rows where the City column starts with the letter 's'.

#### 136. What does the query 'SELECT GETDATE();' return?
**Answer:**
It returns the current date and time from the database server.

#### 137. What happens if you omit columns during an INSERT INTO operation?
**Answer:**
The database will insert NULL values into the unspecified columns (provided they are not defined with NOT NULL or default values).

#### 138. What is CRUD?
**Answer:**
CRUD stands for the four basic database operations: Create, Read, Update, and Delete.

#### 139. What is DCL and its commands?
**Answer:**
DCL stands for Data Control Language. It is used to manage permissions and access control. Its primary commands are GRANT, DENY, and REVOKE.

#### 140. What is DML (Data Manipulation Language)?
**Answer:**
Data Manipulation Language (DML) is a subset of SQL used for managing and modifying data within database objects. Key commands include SELECT, INSERT, UPDATE, and DELETE.

#### 141. What is Data Control Language (DCL)?
**Answer:**
Data Control Language (DCL) comprises SQL commands used for transaction control (COMMIT, ROLLBACK), user management (CREATE/DROP/ALTER USER), and authorization (GRANT, REVOKE).

#### 142. What is Data Definition Language (DDL)?
**Answer:**
Data Definition Language (DDL) consists of SQL commands used to define and modify the database structure, such as CREATE, ALTER, and DROP statements for tables, indexes, and views.

#### 143. What is Data Management in the context of databases?
**Answer:**
Data Management is the practice of collecting, storing, and retrieving data. Core functions include CRUD operations: Create (addition), Read (listing), Update (modification), and Delete (deletion).

#### 144. What is Microsoft Access and when should it be used?
**Answer:**
Microsoft Access is a database solution for simple web sites or applications. It is not well-suited for high-traffic environments and lacks the power and scalability of RDBMS like MySQL, SQL Server, or Oracle.

#### 145. What is Microsoft SQL Server?
**Answer:**
Microsoft SQL Server is a powerful, robust, and full-featured relational database management system (RDBMS) commonly used for high-traffic, database-driven web applications.

#### 146. What is MySQL?
**Answer:**
MySQL is a popular, powerful, and robust open-source relational database management system often used as an inexpensive alternative to commercial solutions like Microsoft SQL Server or Oracle.

#### 147. What is Oracle Database?
**Answer:**
Oracle is a robust, full-featured, and powerful relational database management system often used for high-traffic, enterprise-level web applications.

#### 148. What is SELECT INTO?
**Answer:**
A command that selects data from one or more existing tables and inserts the resulting rows into a new, automatically created table.

#### 149. What is SQL Data Definition Language (DDL)?
**Answer:**
DDL is a subset of SQL used to define and manage database structures. It includes commands for schemas (CREATE/DROP SCHEMA), tables (CREATE/ALTER/DROP TABLE), domains (CREATE/ALTER/DROP DOMAIN), and views (CREATE/DROP VIEW).

#### 150. What is SQL?
**Answer:**
SQL stands for Structured Query Language. It is a standard language used to manage, manipulate, and query data stored in relational database management systems.

#### 151. What is SQL?
**Answer:**
SQL stands for Structured Query Language. It is the standard programming language designed for managing data held in a relational database management system (RDBMS) and is an implementation of Relational Algebra.

#### 152. What is SQL?
**Answer:**
SQL (Structured Query Language) is an ANSI-standard language designed to manage and manipulate relational databases. It supports operations such as database creation, row retrieval, data modification, and structure management.

#### 153. What is a BLOB?
**Answer:**
BLOB stands for Binary Large Object, used for storing large chunks of binary data (like images or media) in a database.

#### 154. What is a CHECK Constraint?
**Answer:**
The CHECK constraint ensures that all values in a column satisfy a specified boolean condition.

#### 155. What is a NULL value in SQL?
**Answer:**
A NULL value represents the absence of data, distinct from blank or zero. It signifies missing, not available, or not applicable information. Comparisons with NULL always result in NULL, leading to three-valued logic. Note: UNIQUE constraints typically allow multiple NULL values.

#### 156. What is a data dictionary?
**Answer:**
A data dictionary is a DBMS component that contains the metadata, logical structure, data definitions, characteristics, and relationships for the information in a database.

#### 157. What is a database Session?
**Answer:**
A session represents an active connection to the database server, acting as the internal state container for an external user or application connection.

#### 158. What is a database connection?
**Answer:**
A communication link established from an external source or application to the database management system.

#### 159. What is a database table and how do you perform basic queries on it?
**Answer:**
A table is a structure with named columns and rows where data is stored. Each row must contain values matching the defined column data types. Use 'SELECT * FROM TableName' to retrieve all columns and rows.

#### 160. What is a database table?
**Answer:**
A table is a database object where data is stored in a structured format with named columns and typed rows. All rows in a table must adhere to the same number of columns and data types, and the data is retrieved using SELECT statements.

#### 161. What is a database?
**Answer:**
A database is a set of logically related data. The way they relate is dependent on the data model used.

#### 162. What is a query result set?
**Answer:**
The query result set is the collection of data rows returned by a database query.

#### 163. What is a record or a row?
**Answer:**
A record, or row, represents an individual entry or a single instance of data stored within a table.

#### 164. What is a result-set?
**Answer:**
The temporary table or collection of rows returned by executing a SELECT statement.

#### 165. What is an Enum in SQL?
**Answer:**
An ENUM (Enumeration) is a data type that allows a column to store one value from a predefined list of string values.

#### 166. What is an ORM (Object-Relational Mapper)?
**Answer:**
An ORM is a programming technique that acts as an interface between object-oriented programming languages and relational databases, allowing developers to interact with database data using objects rather than raw SQL queries.

#### 167. What is an SQL clause?
**Answer:**
SQL clauses (commands) perform specific tasks such as defining, manipulating, or querying data. Examples include SELECT, INSERT, UPDATE, DELETE, CREATE TABLE, and ALTER TABLE.

#### 168. What is an expression language in the context of databases?
**Answer:**
An expression language (also called a compositional language) is a language used to express operations on data, such as relational algebra or XQuery.

#### 169. What is bit data used for?
**Answer:**
Bit data is used for defining and storing bit strings, often representing boolean values (0 or 1).

#### 170. What is the BETWEEN operator?
**Answer:**
The BETWEEN operator selects values within a given range, inclusive of the start and end values.

#### 171. What is the BETWEEN operator?
**Answer:**
The BETWEEN operator selects values within a specified range. It is inclusive, meaning both the start and end values are included in the results. It works with numbers, text, and dates.

#### 172. What is the DELETE command?
**Answer:**
The DELETE command is used to remove existing rows from a table, often constrained by a WHERE clause to target specific records.

#### 173. What is the DROP TABLE command?
**Answer:**
The DROP TABLE command is a DDL operation used to remove an entire table structure and all its associated data from the database.

#### 174. What is the IN operator in SQL?
**Answer:**
The IN operator allows you to specify multiple values in a WHERE clause, acting as shorthand for multiple OR conditions.

#### 175. What is the IN operator?
**Answer:**
The IN operator allows you to specify multiple values in a WHERE clause, acting as shorthand for multiple OR conditions. It can also be used to filter based on the results of a subquery.

#### 176. What is the INSERT INTO SELECT statement?
**Answer:**
The INSERT INTO SELECT statement copies data from one table and inserts it into an existing destination table.

#### 177. What is the LIKE operator?
**Answer:**
The LIKE operator is used in a WHERE clause to search for a specified pattern in a column, typically using wildcards like % or _.

#### 178. What is the NOT NULL constraint?
**Answer:**
The NOT NULL constraint ensures that a column cannot contain NULL values, forcing the application to provide a valid value during insertion or updates.

#### 179. What is the NOT predicate?
**Answer:**
The NOT operator is a logical operator used to negate a predicate. In SQL, it operates within three-valued logic (TRUE, FALSE, or UNKNOWN/NULL).

#### 180. What is the SQL AUTO INCREMENT property?
**Answer:**
It allows a unique numerical value to be generated automatically when a new record is inserted. In MySQL, this is done via the AUTO_INCREMENT keyword; in SQL Server, it uses the IDENTITY property.

#### 181. What is the SQL UPDATE command used for?
**Answer:**
The UPDATE command is used to modify existing data in one or more rows of a table based on a specified condition.

#### 182. What is the TRUNCATE TABLE statement?
**Answer:**
The TRUNCATE TABLE statement is used to remove all records from a table while keeping the table structure intact. Syntax: TRUNCATE TABLE table_name;

#### 183. What is the UPDATE statement?
**Answer:**
The UPDATE statement is used to modify existing data in a table. Syntax: UPDATE table_name SET col1 = val1 WHERE condition;. Warning: If the WHERE clause is omitted, all records in the table will be updated.

#### 184. What is the [charlist] syntax used for?
**Answer:**
The [charlist] syntax is used in pattern matching (typically with the LIKE operator) to specify a set or range of characters to match at a specific position in a string.

#### 185. What is the correct SQL statement to return the sum of the spent amount (Samnt) for clients whose name contains 'Simpson'?
**Answer:**
SELECT SUM(Samnt) as SimpsonsSpending FROM Clients WHERE Cname LIKE '%Simpson%';

#### 186. What is the correct SQL statement to return the sum of the spent amount (Samnt) for the client 'Herb Simpson'?
**Answer:**
SELECT SUM(Samnt) as HerbSpending FROM Clients WHERE Cname IN ('Herb Simpson'); OR SELECT SUM(Samnt) as HerbSpending FROM Clients WHERE Cname = 'Herb Simpson';

#### 187. What is the correct logical order of the main clauses in a SQL SELECT statement?
**Answer:**
The logical order is SELECT, FROM, WHERE.

#### 188. What is the correct syntax order when defining columns in a CREATE TABLE statement?
**Answer:**
The standard order is: column_name data_type(size) constraint_name.

#### 189. What is the default sort order for SQL records?
**Answer:**
The default order is ascending (ASC).

#### 190. What is the definition of the Character Data type?
**Answer:**
Character Data represents a sequence of characters from an implementation-defined character set, typically used for text strings (e.g., CHAR, VARCHAR).

#### 191. What is the difference between % and _ in a LIKE query?
**Answer:**
The '%' wildcard matches any number of characters (zero or more), whereas the '_' wildcard matches exactly one character.

#### 192. What is the difference between BETWEEN and IN operators?
**Answer:**
The BETWEEN operator selects values within a specified range (inclusive). The IN operator determines if a value matches any element in a provided list or set.

#### 193. What is the difference between CREATE TABLE, INSERT INTO, and SELECT DISTINCT?
**Answer:**
CREATE TABLE defines a new table structure. INSERT INTO adds new rows to a table. SELECT DISTINCT retrieves data while filtering out duplicate result rows.

#### 194. What is the difference between MS SQL and other database engines like Oracle or MySQL?
**Answer:**
They are different database management systems (RDBMS) developed by different companies (Microsoft, Oracle, etc.). While they share common SQL standards, each has proprietary extensions, syntax variations, and unique performance optimization features.

#### 195. What is the difference between NULL, zero, and blank space?
**Answer:**
A NULL value represents the absence of data ('unknown' or 'not applicable'). Zero is a numeric value, and a blank space is a character string (length 1). They are not equivalent.

#### 196. What is the difference between SQL, MySQL, and SQL Server?
**Answer:**
SQL is the standardized query language used to interact with databases. MySQL and SQL Server are specific Relational Database Management Systems (RDBMS) that implement the SQL language. MySQL is open-source, while SQL Server is a proprietary product from Microsoft.

#### 197. What is the difference between a DBMS and a database system?
**Answer:**
A Database Management System (DBMS) is the software used to manage data. A database system is an organization of components that defines and regulates the collection, storage, management, and use of data, consisting of the DBMS and the actual databases.

#### 198. What is the difference between nvarchar(100) and nvarchar(max) in MS SQL?
**Answer:**
nvarchar(100) restricts storage to a maximum of 100 Unicode characters. nvarchar(max) allows storage of up to 2GB (or 1 billion characters), making it suitable for large text fields.

#### 199. What is the difference between single quotes ('') and double quotes ("") in standard SQL?
**Answer:**
Single quotes are the standard for string literals. Double quotes are typically used for delimited identifiers (like table or column names containing spaces or reserved words) depending on the specific database engine (e.g., PostgreSQL, SQL Server).

#### 200. What is the difference between system and user databases?
**Answer:**
System databases (e.g., Master, MSDB, TempDB, Model) are default databases required for the SQL Server instance to function correctly and should generally not be modified. User databases are created by developers to store custom application data.

#### 201. What is the difference between the SELECT and WHERE clauses?
**Answer:**
The SELECT clause determines which columns (fields) are returned in the result, while the WHERE clause filters which rows (records) are included.

#### 202. What is the difference in categorization between '2002-01-25 20:20:01.001', '2002-01-25', and '22:10:15.3239999'?
**Answer:**
'2002-01-25 20:20:01.001' is a 'datetime' value. '2002-01-25' is a 'date' value. '22:10:15.3239999' is invalid as a standalone date/time type because it lacks date information.

#### 203. What is the function of the ALTER TABLE statement?
**Answer:**
The ALTER TABLE statement is used to add, delete, or modify columns in an existing table, as well as to add, modify, or drop various constraints on an existing table structure.

#### 204. What is the function of the DELETE statement?
**Answer:**
The DELETE statement is used to remove one or more rows from a specified table in the database.

#### 205. What is the function of the IN operator in a WHERE clause?
**Answer:**
The IN operator allows you to specify multiple values in a WHERE clause, acting as shorthand for multiple OR conditions (e.g., checking if a City is 'Paris' or 'London').

#### 206. What is the function of the INSERT statement?
**Answer:**
It is used to insert a single row into a table, or to insert an arbitrary number of rows from other tables using a sub-select.

#### 207. What is the function of the LIKE operator in SQL?
**Answer:**
The LIKE operator is a comparison operator used to check whether an attribute's text value matches a specified string pattern using wildcards (e.g., SELECT Name FROM Customer WHERE Name LIKE 'M%').

#### 208. What is the function of the ORDER BY clause in SQL?
**Answer:**
The ORDER BY clause specifies the column(s) used to sort the resulting data set.

#### 209. What is the objective of a Data Manipulation Language (DML)?
**Answer:**
DML contains commands used to manipulate data within the database structure, such as SELECT, INSERT, UPDATE, DELETE, COMMIT, and ROLLBACK.

#### 210. What is the objective of a query language?
**Answer:**
A query language provides a standard interface to a DBMS for expressing requests to retrieve, insert, update, delete data, and manage schema structures and access permissions.

#### 211. What is the opposite of LIKE?
**Answer:**
NOT LIKE. It is used in a WHERE clause to filter out records that do not match the specified pattern. Example: SELECT * FROM [Grant] WHERE GrantName NOT LIKE 'O%'

#### 212. What is the purpose of a UNIQUE constraint?
**Answer:**
It ensures that all values in a specific column (or set of columns) are different across all rows in the table.

#### 213. What is the purpose of an SQL Clause (e.g., WHERE, HAVING)?
**Answer:**
SQL clauses are used to filter rows from a result set based on specific conditions, thereby limiting the output to only the relevant records.

#### 214. What is the purpose of the 'DELETE' statement?
**Answer:**
The DELETE statement is used to remove existing records from a table that match the conditions specified in the WHERE clause.

#### 215. What is the purpose of the 'SELECT INTO' statement?
**Answer:**
The 'SELECT INTO' statement creates a new table and populates it with the result set of a query. To create an empty table with the schema of another, you can append a WHERE clause that evaluates to false (e.g., WHERE 1=0).

#### 216. What is the purpose of the 'UPDATE' statement?
**Answer:**
The UPDATE statement is used to modify existing records in a table based on specified conditions provided in the WHERE clause.

#### 217. What is the purpose of the DEFAULT constraint?
**Answer:**
The DEFAULT constraint provides a default value for a column automatically if no specific value is provided during an INSERT operation.

#### 218. What is the purpose of the DISTINCT keyword?
**Answer:**
The DISTINCT keyword is used in a SELECT statement to return only unique values, effectively eliminating duplicate rows from the result set.

#### 219. What is the purpose of the FROM and JOIN clauses?
**Answer:**
The FROM and JOIN clauses specify the table or tables from which to retrieve data.

#### 220. What is the purpose of the GO command?
**Answer:**
GO is a batch separator used in SQL Server to signal the end of a batch of SQL statements. It instructs the client tool to send the preceding statements to the server for execution before continuing with the code that follows.

#### 221. What is the purpose of the INSERT statement in SQL?
**Answer:**
The INSERT statement is used to add a single row of data into a named table, or to insert an arbitrary number of rows from one or more tables using a subquery (sub-select).

#### 222. What is the purpose of the SELECT statement?
**Answer:**
The SELECT statement is used to retrieve and display data from one or more database tables.

#### 223. What is the purpose of the SELECT statement?
**Answer:**
The SELECT statement is used to retrieve data from a database. Its components include SELECT (columns), FROM (tables), WHERE (filtering), GROUP BY (aggregation), HAVING (filter for groups), and ORDER BY (sorting).

#### 224. What is the purpose of the UNIQUE constraint?
**Answer:**
The UNIQUE constraint ensures that all values in a column or set of columns are distinct, preventing duplicate entries in those fields.

#### 225. What is the purpose of the WHERE clause?
**Answer:**
It is used to filter records that fulfill a specified criterion.

#### 226. What is the relational algebra select operator and what does it do?
**Answer:**
The select operator picks certain rows from a relation based on a condition. It is functionally similar to the WHERE clause in SQL.

#### 227. What is the standard order of clauses in a SELECT statement?
**Answer:**
The SELECT statement consists of the following clauses: SELECT, DISTINCT, FROM & JOIN, WHERE, GROUP BY, HAVING, ORDER BY, and LIMIT.

#### 228. What is the standard order of clauses in a comprehensive SELECT statement?
**Answer:**
The standard sequence is: SELECT, DISTINCT, FROM & JOIN, WHERE, GROUP BY, HAVING, ORDER BY, and LIMIT.

#### 229. What is the syntax for the SQL INSERT command?
**Answer:**
INSERT INTO table_name (column1, column2) VALUES (value1, value2); It allows the insertion of one or more rows into a table.

#### 230. What is the usage of the DISTINCT keyword?
**Answer:**
The DISTINCT keyword is used in a SELECT statement to return only unique (non-duplicate) values from the specified columns.

#### 231. What is the usage of the SIGN function?
**Answer:**
The SIGN function determines if a numeric value is positive, negative, or zero. It returns +1 for positive numbers, -1 for negative, and 0 for zero.

#### 232. What parameters can SELECT TOP use to limit records?
**Answer:**
SELECT TOP can limit records by a specific absolute number or by a percentage of the total result set.

#### 233. What statement is used to fetch data from a database?
**Answer:**
The SELECT statement is used. Example: 'SELECT * FROM table_name' (where * is a wildcard for all columns) or 'SELECT col1, col2 FROM table_name'.

#### 234. What values does the Boolean data type contain?
**Answer:**
Boolean data contains the truth values TRUE and FALSE.

#### 235. When are quotes required for values in SQL queries?
**Answer:**
Numeric fields generally do not require quotes around values, while text fields generally require single quotes.

#### 236. When defining a character string column, what does the specified length indicate?
**Answer:**
The specified length indicates the maximum number of characters that the column can hold.

#### 237. When is the exact numeric data type used?
**Answer:**
It is used when you need to store numbers with absolute precision, such as financial or inventory data where rounding errors are unacceptable.

#### 238. When is using a table alias useful?
**Answer:**
Aliases are useful when: joining multiple tables (to differentiate columns), using aggregate functions, shortening long or complex column names, or combining multiple columns into one output.

#### 239. When should you use date/time data types?
**Answer:**
Use date/time data types when you need to define a specific point in time with a required degree of accuracy.

#### 240. Which SQL clause is used to limit the number of records returned by a query?
**Answer:**
The SELECT TOP clause (or LIMIT/FETCH FIRST depending on the SQL dialect).

#### 241. Which SQL clause uses the logical operators AND, OR, and NOT, and in what order are they evaluated?
**Answer:**
These operators are used in the WHERE clause. The evaluation order is NOT, followed by AND, followed by OR.

#### 242. Which SQL statement is used to remove one or more rows from a named table?
**Answer:**
The DELETE statement.

#### 243. Which data type handles non-exact numbers?
**Answer:**
Approximate numeric data types (such as FLOAT or REAL).

#### 244. Which data type is used for bit strings?
**Answer:**
The BIT or BIT VARYING data type.

#### 245. Which data type is used for exact numeric representation?
**Answer:**
Exact numeric data types (such as DECIMAL or NUMERIC in many SQL dialects) are used when precision and scale must be guaranteed.

#### 246. Which data type should be used for monetary values like '1001.99'?
**Answer:**
The 'decimal(p,s)' or 'numeric(p,s)' data type (e.g., decimal(18,2)) should be used to ensure precision and prevent rounding errors associated with floating-point types.

#### 247. Which symbol is used to denote parameters in SQL statements?
**Answer:**
The '@' symbol is commonly used to denote parameters.

#### 248. Which temporal data type should you use to store '2002-01-25 22:10:15.3239999'?
**Answer:**
This value requires 'datetime2', as standard 'datetime' does not support that level of fractional second precision.

#### 249. Which two keywords are used to define key constraints in SQL?
**Answer:**
The two primary keywords for defining key constraints are 'PRIMARY KEY' (enforcing uniqueness and non-nullability, limited to one per table) and 'UNIQUE' (ensuring all values in a column are distinct, allowing multiple per table).

#### 250. Who invented RDBMS and when?
**Answer:**
The Relational Database Management System model was proposed in 1970 by Dr. Edgar Frank 'Tedd' Codd while working at IBM.

#### 251. Who is credited with the invention of SQL?
**Answer:**
Edgar F. Codd (the relational model) and later refinement by Donald Chamberlin and Raymond Boyce.

#### 252. Who is responsible for assigning authorization identifiers?
**Answer:**
The Database Administrator (DBA).

#### 253. Why are square brackets [ ] used with database objects?
**Answer:**
Brackets are used to delimit identifiers, which is necessary when an object name contains spaces, reserved SQL keywords, or special characters.

#### 254. Why does the statement 'CREATE TABLE Person (PersonName nvarchar());' fail and how can it be fixed?
**Answer:**
The statement fails because the length for the nvarchar data type is missing. It should specify a length (e.g., nvarchar(100)) or use 'nvarchar(max)' to store strings of variable length.

#### 255. Why is the SQL statement UPDATE used?
**Answer:**
The UPDATE statement is used to modify one or more values in specified columns of existing rows within a named table.

#### 256. Write a statement to add a column 'Comments' of data type nvarchar(4000) that allows null values to be inserted to table 'Clients'.
**Answer:**
ALTER TABLE Clients ADD Comments nvarchar(4000) NULL;


### 🟡 Mid Level

#### 1. Explain how filtering works with NULL values and inclusion lists.
**Answer:**
Use 'WHERE column IS NULL' or 'IS NOT NULL' to filter nulls. Use 'WHERE column IN (value1, value2)' or 'NOT IN (...)' to filter against a list of specific values.

#### 2. How are GRANT and REVOKE used in SQL?
**Answer:**
GRANT is issued by an owner or admin to pass specific privileges to another user. REVOKE is issued to remove those previously granted privileges.

#### 3. How are date and time handled in SQL?
**Answer:**
Date handling relies on specific data types like DATE, DATETIME, and TIMESTAMP. The primary challenge is ensuring the inserted format matches the database column format. Different RDBMS (MySQL, SQL Server) have slightly different formats and storage capabilities, so consulting documentation is essential.

#### 4. How can you test if a string value is a valid 'datetime' in SQL Server?
**Answer:**
You can use the TRY_CONVERT(datetime, 'your_value') function. If the conversion is unsuccessful, it returns NULL, preventing the query from crashing.

#### 5. How do you ensure data in a column is valid JSON?
**Answer:**
Use a CHECK constraint with the ISJSON() function, e.g., CHECK (ISJSON(column_name) = 1).

#### 6. How do you handle concatenation and data types in SQL functions?
**Answer:**
Functions like CONCAT join strings. When concatenating different data types (e.g., datetime and string), the non-string value must be converted explicitly using CONVERT or CAST to avoid errors. Example: CONCAT('Date: ', CONVERT(nvarchar, GETDATE())).

#### 7. How do you implement conditional logic in a SELECT statement?
**Answer:**
Use the CASE expression: CASE WHEN condition THEN result ELSE default END. It allows row-by-row categorization of data.

#### 8. How do you perform date and time comparisons in SQL queries?
**Answer:**
To compare dates, you often need to normalize values: use YEAR() to extract year parts, CONVERT() to reduce datetime to date, or DATEDIFF() to calculate durations between two dates. Example: 'SELECT Cname, DATEDIFF(year, Bdate, '1999-01-01') AS AgeIn99 FROM Clients'.

#### 9. How do you protect against SQL injection?
**Answer:**
Use parameterized queries (prepared statements). These treat inputs as data values rather than executable code, preventing the malicious alteration of the SQL command.

#### 10. How do you query for special characters like % and _ literally?
**Answer:**
Enclose the special character in brackets within the LIKE clause. Examples: LIKE '%[%%%]%' to find a literal percent sign, or LIKE '%[_]%' to find a literal underscore.

#### 11. How to handle NULL values in expressions using functions?
**Answer:**
Use IFNULL() or COALESCE() to return an alternative value if the input expression evaluates to NULL (e.g., COALESCE(column, 0)).

#### 12. SQL INSERT INTO SELECT Statement
**Answer:**
The INSERT INTO SELECT statement copies data from a source table and inserts it into a target table. It requires that data types match. Existing records in the target table are unaffected. You can apply filters with a WHERE clause to copy only specific subsets of data.

#### 13. SQL NULL Values and Handling
**Answer:**
A NULL value represents missing or unknown data. Arithmetic operations involving NULL usually result in NULL. To handle these, functions like ISNULL(), IFNULL(), COALESCE(), or NVL() are used to provide default values during query processing.

#### 14. SQL SELECT INTO Statement
**Answer:**
The SELECT INTO statement copies data from a source table into a new table. The new table is created with the schema (column names and types) of the source data. It is often used for backups or creating subsets of data.

#### 15. What are SQL parameters and why are they important?
**Answer:**
SQL parameters are values added to a query at execution time in a controlled manner. They are the primary defense against SQL injection attacks.

#### 16. What are common date and time functions for constructing or calculating dates?
**Answer:**
DATEFROMPARTS(y,m,d) constructs a date, DATETIMEFROMPARTS(...) constructs a datetime, DATEDIFF(part, start, end) calculates the difference between two dates, DATEADD(part, num, date) adds an interval to a date, and ISDATE(value) validates if a string is a valid date.

#### 17. What are common date and time functions for extracting parts of a date?
**Answer:**
Common functions include: GETDATE() (current timestamp), DATEPART(part, date) (returns specific part), DAY(date), MONTH(date), and YEAR(date).

#### 18. What are temporary tables and how do local differ from global ones?
**Answer:**
Temporary tables are storage structures for intermediate data. Local temp tables (#name) are private to the current connection and drop upon disconnection. Global temp tables (##name) are visible to all sessions and drop only when all referencing connections are closed.

#### 19. What are the commands to manage access privileges?
**Answer:**
Since database objects have an owner, privileges are managed using the GRANT (to provide access) and REVOKE (to remove access) statements.

#### 20. What are the common schema descriptor languages for XML?
**Answer:**
The most common are Document Type Definition (DTD) and XML Schema Definition (XSD), with XSD being the more powerful and feature-rich standard.

#### 21. What are the rules for a well-formed XML document?
**Answer:**
1. There must be exactly one single root element. 2. All tags must be properly closed and nested. 3. All attribute names must be unique within an element.

#### 22. What are the two primary goals of database authorization?
**Answer:**
1. Limit what the user can see (ensure users only access data they are authorized for). 2. Protect against malicious modifications by unauthorized users.

#### 23. What does an INSERT INTO ... SELECT statement do?
**Answer:**
It copies data from one or more source tables into a target table. For example, copying specific supplier records into the Customers table based on a condition.

#### 24. What does the COL_LENGTH() function do?
**Answer:**
It returns the defined maximum length (in bytes) of a specific table column.

#### 25. What does the expression '{...}' mean in XQuery?
**Answer:**
The curly brackets '{}' in XQuery signify 'evaluate me', meaning the expression contained inside the brackets will be executed as a query.

#### 26. What is 'Compositionality' in query languages?
**Answer:**
Compositionality is the ability to nest queries or combine multiple query results using relational algebra or SQL operators.

#### 27. What is Collation?
**Answer:**
Collation defines the rules for sorting and comparing character data, including settings for case sensitivity, accent sensitivity, and character width.

#### 28. What is SQL Injection?
**Answer:**
A technique where malicious users inject SQL commands into an SQL statement via user input on a web page to bypass security or manipulate data.

#### 29. What is a Collation?
**Answer:**
Collation defines the rules for storing, sorting, and comparing character data.

#### 30. What is a predicate in SQL?
**Answer:**
A predicate is a logical expression in a WHERE or HAVING clause that evaluates to TRUE, FALSE, or UNKNOWN for each record. It acts as a filter to determine which rows should be included in the result set.

#### 31. What is the NEWSEQUENTIALID() function?
**Answer:**
A SQL function that generates a sequential UniqueIdentifier, often used for primary keys to minimize fragmentation in clustered indexes compared to NEWID().

#### 32. What is the basic unit of time in SQL Server?
**Answer:**
The microsecond (μsecond).

#### 33. What is the danger of an UPDATE statement without a WHERE clause?
**Answer:**
An UPDATE statement without a WHERE clause will apply the change to every single row in the table, which is often an irreversible mistake. Always test the criteria using a SELECT statement first to verify which rows will be affected.

#### 34. What is the difference between well-formed XML and valid XML?
**Answer:**
Well-formed XML refers to XML that follows all the basic syntax rules (e.g., proper closing tags, single root element). Valid XML is well-formed XML that also adheres to a specific document type definition (DTD) or XML schema (XSD) to ensure structural compliance.

#### 35. What is the logical order of keywords in a SQL query?
**Answer:**
The order is: SELECT, FROM, JOIN, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT (or TOP).

#### 36. What is the purpose of the MERGE statement?
**Answer:**
The MERGE statement performs conditional DML operations. It checks if a source row exists in the target table; if it exists, it performs an UPDATE, otherwise, it performs an INSERT.

#### 37. What is the purpose of the WITH GRANT option?
**Answer:**
The WITH GRANT option allows a user who has been granted specific SQL privileges to pass those privileges on to other users.

#### 38. What is the smallest interval recordable by a datetime data type?
**Answer:**
The smallest interval is typically 3.33 milliseconds (based on the internal storage resolution of the datetime type).

#### 39. What is three-valued logic in SQL?
**Answer:**
SQL uses three-valued logic to handle NULL values, which can result in TRUE, FALSE, or UNKNOWN (NULL) outcomes when evaluating predicates.

#### 40. When does a comparison result in an 'UNKNOWN' truth value?
**Answer:**
An UNKNOWN result occurs when comparing against a NULL value, as NULL represents missing or inapplicable data.

#### 41. Which SQL privileges can be granted to other users?
**Answer:**
Privileges such as USAGE, SELECT, DELETE, INSERT, UPDATE, and REFERENCES can be granted to other users if the grantor has the appropriate permissions.

#### 42. Which privileges can be restricted to specific columns?
**Answer:**
INSERT, UPDATE, and REFERENCES can be restricted to specific columns rather than the entire table.

#### 43. Why does comparing dates with time components in SQL often fail?
**Answer:**
If a date column contains a time component (e.g., '2008-11-11 13:23:44'), a strict equality comparison against just the date ('2008-11-11') will fail because the database treats the time as part of the value. Always account for the time component or cast the value to a date type for accurate comparisons.

#### 44. Write a query to find URLs that start with any character, have '://', contain a character before and after, and end in '.org'.
**Answer:**
SELECT * FROM ApprovedWebsites WHERE URLName LIKE '_%://_%.org'


### 🔴 Senior Level

#### 1. What are two common SQL Injection payloads that evaluate to 'Always True'?
**Answer:**
1=1 and ''=''. These are used to bypass authentication by making a WHERE clause always evaluate to true.


## 📂 Category: Database Design & Normalization (186 cards)

### 🟢 Junior Level

#### 1. Define common SQL constraints: NOT NULL, UNIQUE, FOREIGN KEY, CHECK, PRIMARY KEY, and DEFAULT.
**Answer:**
NOT NULL: Column cannot store NULL; UNIQUE: Values must be distinct; FOREIGN KEY: Maintains referential integrity; CHECK: Column values must meet a condition; PRIMARY KEY: Unique identifier (NOT NULL + UNIQUE); DEFAULT: Provides a value if none is specified.

#### 2. Define first normal form (1NF).
**Answer:**
A relation is in 1NF if it consists of atomic, single-valued attributes, has no repeating groups, and has a primary key identified.

#### 3. How many primary and unique keys can a table have?
**Answer:**
A table can have only one primary key, but it can have one or more unique keys.

#### 4. How many tempdbs exist on one instance of SQL Server?
**Answer:**
Only one.

#### 5. In UML class modeling, what are the alternative terms for subclass and superclass?
**Answer:**
A subclass is also called a 'Specialization', and a superclass is also called a 'Generalization'.

#### 6. In the context of database system development, what does the functional/application area refer to?
**Answer:**
It refers to specific enterprise activities within an organization, such as marketing, personnel management, and stock control.

#### 7. SQL Constraints: PRIMARY KEY and NOT NULL
**Answer:**
PRIMARY KEY uniquely identifies each record, must contain UNIQUE values, and cannot be NULL. A table can have only one primary key, which can consist of multiple columns. NOT NULL ensures a column cannot hold NULL values, requiring a value for every entry.

#### 8. What are SQL constraints and why are they used?
**Answer:**
SQL constraints are rules applied to columns or tables that limit the type of data that can be stored. They ensure data accuracy, reliability, and integrity. Constraints can be defined during table creation (CREATE TABLE) or modified later (ALTER TABLE). If a data action violates a constraint, the action is aborted.

#### 9. What are SQL constraints and why are they used?
**Answer:**
Constraints enforce rules on data in a table, ensuring accuracy and reliability. Common types include NOT NULL, CHECK, DEFAULT, UNIQUE, PRIMARY KEY, and FOREIGN KEY. They can be applied at the column level or the table level.

#### 10. What are SQL data types?
**Answer:**
Data types define the kind of value a column can hold (e.g., integer, character, date, binary). They ensure that the database understands how to interpret and interact with the stored data. Developers must select appropriate data types during table creation, noting that syntax and storage size may vary between database systems.

#### 11. What are domain, field, and NULL constraints?
**Answer:**
A domain constraint defines the set of legal values for a column. A field (column) holds specific information for a record. A NULL value represents the absence of data, which is distinct from a zero or empty space.

#### 12. What are the common SQL constraints used to maintain data integrity?
**Answer:**
SQL constraints specify rules for data in a table. A Foreign Key is a specific constraint used to prevent actions that would destroy links between tables.

#### 13. What are the common categories of data?
**Answer:**
Common data categories include: Personally Identifiable Information (PII), Business data, Operational data, Geo/Spatial data, and Time-series data.

#### 14. What are the core components of a database table?
**Answer:**
A table consists of Column Names (the header), Rows (individual records), Values (data stored in cells), and NULL values (representing missing or unknown data).

#### 15. What are the core features of a Database Management System (DBMS)?
**Answer:**
Key features include data integrity, multi-user access control, backup and recovery, high availability, centralized data management, and standardized languages/APIs for data access.

#### 16. What are the main components of an ERD (Entity Relationship Diagram)?
**Answer:**
An ERD consists of Entities, their Attributes, and the relationships (often defined by foreign keys) between them.

#### 17. What are the main elements/components of a database?
**Answer:**
A database contains schemas. A schema is a container used to group database objects. Within a schema, there are Tables (with typed columns), Views (named stored queries), Stored Procedures (precompiled SQL code), and other objects.

#### 18. What are the main types of table relationships?
**Answer:**
One-to-One (1:1), where each record in Table A matches only one in Table B; One-to-Many (1:M), where one record in Table A matches multiple in Table B; and Many-to-Many (M:N), requiring a junction table.

#### 19. What are the options for maintaining Referential Integrity when a primary key is modified?
**Answer:**
Referential integrity actions include: CASCADE (updates/deletes changes in referenced rows), SET NULL (sets foreign keys to NULL), SET DEFAULT (sets foreign keys to a default value), RESTRICT (prevents the change), and NO ACTION (allows the change without cascading).

#### 20. What are the requirements for a Primary Key?
**Answer:**
A Primary Key must contain a unique value for every row and cannot contain NULL values.

#### 21. What are the two primary activities in database planning?
**Answer:**
Defining the mission statement and defining the mission objectives.

#### 22. What are the typical steps of database system development?
**Answer:**
1. Database planning, 2. System definition, 3. Requirements collection and analysis, 4. Database design, 5. DBMS selection.

#### 23. What does the association multiplicity 0..* mean?
**Answer:**
It means the relationship can exist between none or any number of objects (zero to many).

#### 24. What is a FOREIGN KEY constraint?
**Answer:**
A foreign key is a field in one table that links to the PRIMARY KEY of another table. It establishes a parent-child relationship between tables, ensuring referential integrity by preventing orphaned records.

#### 25. What is a Foreign Key?
**Answer:**
A Foreign Key is a field (or collection of fields) in a table that uniquely identifies a row or record in another database table. Recommended naming conventions use a combination of the referenced table name and the referenced field name.

#### 26. What is a Foreign Key?
**Answer:**
A Foreign Key is a field (or collection of fields) in one table that refers to the Primary Key in another table, establishing and enforcing a link between the data in the two tables.

#### 27. What is a PRIMARY KEY?
**Answer:**
A primary key is a column or a combination of columns that uniquely identifies each row in a database table. It enforces entity integrity by combining NOT NULL and UNIQUE constraints.

#### 28. What is a Primary Key?
**Answer:**
A Primary Key (PK) is a constraint that uniquely identifies each row in a table. It cannot contain NULL values, and each table can have only one PK. PKs are automatically indexed to improve data retrieval performance.

#### 29. What is a Relational Database?
**Answer:**
A type of database based on set theory that uses logically related two-dimensional tables (rows and columns) and operations based on relational calculus to store and manage information.

#### 30. What is a Unique key?
**Answer:**
A Unique key constraint ensures that all values in a column (or set of columns) are distinct across the table. Unlike a primary key, it allows for one NULL value (depending on the RDBMS implementation).

#### 31. What is a database system development feedback loop?
**Answer:**
The process of finalizing a database development through multiple iterations of trial and error.

#### 32. What is a domain constraint?
**Answer:**
A domain constraint limits the valid set of values that can be stored in an attribute (column). An example is defining a column as NOT NULL or providing a DEFAULT value constraint.

#### 33. What is a general constraint?
**Answer:**
A general constraint (e.g., CHECK constraint) defines a condition on the range of allowed values for specific attributes, such as requiring an age column to be between 16 and 100.

#### 34. What is a join table?
**Answer:**
A junction or associative table used to resolve many-to-many relationships by storing the primary keys of the two tables it links.

#### 35. What is a key in the relational model?
**Answer:**
A key is a set of attributes (or a single attribute) that defines all other attributes (functional dependency aspect) and serves as a unique identifier for each tuple, ensuring rows are never duplicated.

#### 36. What is a many-to-many relationship in database design?
**Answer:**
A many-to-many relationship exists when multiple records in one table are associated with multiple records in another table. In relational databases, this is implemented using a junction (or link) table that contains foreign keys referencing the primary keys of both related tables.

#### 37. What is a primary key and how many can a table have?
**Answer:**
A primary key is a constraint that uniquely identifies each row in a table. Each table can have only one primary key (though it may consist of multiple columns as a composite key).

#### 38. What is a relational database?
**Answer:**
A relational database organizes data into tables with predefined relationships between them, typically established through the use of unique identifiers (IDs) to link data across tables.

#### 39. What is an Identity column?
**Answer:**
An Identity column is a property applied to a column that allows the database to automatically generate sequential numeric values for each new row inserted. A start and increment value can be defined. Identity columns do not require manual indexing, as they are typically used for primary keys which are indexed by default.

#### 40. What is an Information System in the context of databases?
**Answer:**
An information system refers to the resources and processes that enable the collection, management, control, and dissemination of information.

#### 41. What is an association in UML?
**Answer:**
An association is a relationship between objects of two classes.

#### 42. What is entity integrity?
**Answer:**
Entity integrity ensures that each row in a table is uniquely identifiable, typically enforced by a PRIMARY KEY constraint, which prevents null values in key columns.

#### 43. What is the DEFAULT constraint?
**Answer:**
The DEFAULT constraint provides a default value for a column if no value is specified during an insert operation. It can be defined at table creation or added to an existing column using the ALTER TABLE statement.

#### 44. What is the UNIQUE constraint in SQL?
**Answer:**
The UNIQUE constraint ensures that all values in a column are distinct. Unlike the PRIMARY KEY constraint (which also enforces uniqueness), a table can have multiple UNIQUE constraints. It can be applied at the column level or the table level.

#### 45. What is the characteristic of a column where every row has a different value?
**Answer:**
This is the definition of a unique constraint or a primary key, ensuring entity integrity.

#### 46. What is the difference between Primary Keys and Foreign Keys?
**Answer:**
A Primary Key is a unique identifier for a specific row in a table. A Foreign Key is a column or set of columns that creates a link between two tables, ensuring referential integrity.

#### 47. What is the difference between a Primary Key and a Foreign Key?
**Answer:**
A Primary Key is a column or set of columns that uniquely identifies a row in a table (cannot be NULL). A Foreign Key is a field that references the primary key of another table to establish a relationship and ensure referential integrity.

#### 48. What is the difference between a Primary Key and a Unique Key?
**Answer:**
A Primary Key ensures uniqueness and does not allow NULL values. A Unique Key also ensures uniqueness but allows a single NULL value.

#### 49. What is the minimal information needed when defining a table?
**Answer:**
A table must have a unique Table Name, and at least one Column Name with an associated Data Type.

#### 50. What is the purpose of a CHECK constraint?
**Answer:**
A CHECK constraint limits the range of values that can be placed in a specific column, ensuring data integrity by enforcing boolean conditions.

#### 51. What is the purpose of a foreign key?
**Answer:**
A foreign key is a field (or collection of fields) in one table that uniquely identifies a row of another table or the same table, used to define and enforce referential integrity between tables.

#### 52. What is the purpose of a primary key and how does it relate to foreign keys?
**Answer:**
A primary key is a column (or set of columns) that uniquely identifies every row in a table. A foreign key is a column that refers to the primary key in another table, establishing a relationship between them.

#### 53. What is the purpose of the CHECK constraint?
**Answer:**
The CHECK constraint ensures that all values in a specific column satisfy a defined boolean condition.

#### 54. What is the recommended naming convention for database tables and views?
**Answer:**
Use singular nouns rather than plural (e.g., 'movie' instead of 'movies').

#### 55. Why are data types important in database design?
**Answer:**
1. Ensures data consistency (prevents mixing types). 2. Enables appropriate calculations and functions (e.g., math or date functions). 3. Allows for storage and performance optimization. 4. Ensures correct sorting/ordering behavior.


### 🟡 Mid Level

#### 1. Define 3rd Normal Form (3NF).
**Answer:**
A table is in 3rd Normal Form when it is in 2nd Normal Form and there are no transitive dependencies (i.e., non-key attributes must depend only on the primary key).

#### 2. Define Boyce-Codd normal form (BCNF).
**Answer:**
A table is in BCNF if it is in 3NF and every determinant is a candidate key. This prevents dependency issues between parts of candidate keys.

#### 3. Define Full Functional Dependency.
**Answer:**
A condition in which an attribute is functionally dependent on a composite key, but not on any proper subset of that key. If A determines B (A -> B), B is fully functionally dependent on A.

#### 4. Define Functional Dependency.
**Answer:**
An attribute B is functionally dependent on attribute A if knowing the value of A uniquely determines the value of B, denoted as A -> B.

#### 5. Define second normal form (2NF).
**Answer:**
A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the entire primary key (no partial dependencies).

#### 6. Define third normal form (3NF).
**Answer:**
A table is in 3NF if it is in 2NF and no non-key attribute is functionally dependent on another non-key attribute (no transitive dependencies).

#### 7. Do database privileges always reside within the database system itself?
**Answer:**
Privileges may not necessarily reside in the database, but in the software applications accessing the database. Consequently, an end-user might be granted access to the application while having no direct privileges within the database engine itself.

#### 8. Explain 'Complete' vs 'Incomplete' and 'Disjoint' vs 'Overlapping' subclassing.
**Answer:**
Complete subclassing means every instance of a superclass must belong to at least one subclass; Incomplete (partial) means it doesn't necessarily have to. Disjoint (exclusive) means an instance cannot belong to more than one subclass; Overlapping means an instance can belong to several subclasses simultaneously.

#### 9. Explain the different types of database Normalization (1NF, 2NF, 3NF).
**Answer:**
1NF: No repeating groups and atomic values. 2NF: Meets 1NF and all non-key attributes are fully functionally dependent on the primary key. 3NF: Meets 2NF and has no transitive dependencies (non-key attributes depend only on the primary key).

#### 10. Explain the normalization rules (1NF, 2NF, 3NF) using Codd's rule.
**Answer:**
The data depends on the key (1NF), the whole key (2NF), and nothing but the key (3NF).

#### 11. Functional dependencies are a generalization of what concept?
**Answer:**
Functional dependencies are a generalization of the notion of keys.

#### 12. How are Integrity Constraints classified in SQL?
**Answer:**
They are classified into: 1. Not Null constraints; 2. Key constraints (PRIMARY KEY, UNIQUE); 3. Referential integrity (FOREIGN KEY); 4. Attribute-based CHECK constraints; 5. Tuple-based CHECK constraints; 6. General assertions.

#### 13. How are computed columns implemented?
**Answer:**
Computed columns are expressions based on other columns. They can be 'virtual' (computed on the fly) or 'persisted' (stored on disk and updated whenever the underlying data changes).

#### 14. How do you define a custom data type with specific constraints?
**Answer:**
You use the CREATE DOMAIN statement (in standard SQL) to define a custom data type along with associated CHECK constraints that are applied whenever the type is used.

#### 15. How does XSD compare to DTD?
**Answer:**
XSD (XML Schema Definition) is more expressive than DTD (Document Type Definition), offering support for data types, namespaces, and complex hierarchical structures.

#### 16. How does relational algebra handle duplicates?
**Answer:**
In formal relational algebra, sets do not contain duplicates; therefore, duplicates are automatically eliminated unless the operation explicitly specifies otherwise (e.g., multiset operators).

#### 17. How is a one-to-one relationship implemented in database design?
**Answer:**
A one-to-one relationship occurs when an entity in one table relates to only one entity in another. It can be implemented as a single table or by using a foreign key that acts as a primary key in a related table.

#### 18. How is the closure of attributes computed in functional dependency theory?
**Answer:**
Computing the closure involves iteratively applying Armstrong's axioms (combining and transitive rules) to the set of attributes until no new attributes can be added to the set.

#### 19. If a functional dependency A -> all attributes exists, what is A?
**Answer:**
A is a candidate key for the relation.

#### 20. Jak klasifikovat funkční závislosti A->B?
**Answer:**
Triviální: B je podmnožinou A. Netriviální: B není podmnožinou A. Úplně netriviální: B není podmnožinou A a A a B nemají průnik.

#### 21. Pravidlo pro klíče v relaci
**Answer:**
Pokud je A klíčem relace R(A, B, C), pak každá nadmnožina A (např. AB, AC, ABC) je rovněž kandidátním klíčem.

#### 22. What anomalies occur in unnormalized relations?
**Answer:**
1. Insertion Anomaly: Cannot store data without other unrelated data. 2. Deletion Anomaly: Deleting one record causes unintended loss of other data. 3. Update Anomaly: Redundant data must be updated in multiple places, risking inconsistency.

#### 23. What are Integrity Constraints?
**Answer:**
Integrity constraints are rules used to impose semantic restrictions on data, ensuring data accuracy and consistency, rather than just basic type restrictions.

#### 24. What are common database design anomalies?
**Answer:**
Redundancy (storing data multiple times), Update anomaly (inconsistent data updates), and Deletion anomaly (inadvertently losing data when deleting unrelated attributes).

#### 25. What are common problems with file-based storage compared to databases?
**Answer:**
Common problems include: lack of data structure (chaos), redundant storage, difficulties with concurrent multi-user access, and gaps in data security or access management.

#### 26. What are critical considerations for a Business Intelligence (BI) project?
**Answer:**
Important factors include historical data availability, distribution methods (PDF, email), frequency of updates, data latency requirements, business logic/transformation rules, and security/access restrictions.

#### 27. What are the best practices for choosing database data types?
**Answer:**
Choose smaller data types where possible, keep types simple, and avoid NULL values if the business logic allows.

#### 28. What are the common anomalies that occur in unnormalized relations?
**Answer:**
The common anomalies are: Insert Anomaly (cannot add data without other required fields), Delete Anomaly (losing related data when deleting a record), and Change (Update) Anomaly (redundant data leading to inconsistency).

#### 29. What are the common referential actions for foreign keys?
**Answer:**
CASCADE: Deletes child rows when the parent row is deleted. NO ACTION: No operation is performed, potentially causing an error if constraints are violated. RESTRICT: Prevents deletion of a parent row if associated child rows exist. SET NULL: Sets foreign key columns in the child table to NULL when the parent row is deleted.

#### 30. What are the components of a referential action?
**Answer:**
A referential action is defined by two parts: an event (e.g., DELETE, UPDATE) and an action (e.g., CASCADE, SET NULL, RESTRICT).

#### 31. What are the desirable properties of decomposition?
**Answer:**
Attribute preservation, dependency preservation, and lossless decomposition.

#### 32. What are the disadvantages of failing to normalize a database?
**Answer:**
Failure to normalize leads to data redundancy (wasted space) and data inconsistency (update anomalies where changes are not applied across all duplicate records, violating integrity).

#### 33. What are the four main types of integrity constraints?
**Answer:**
The four main types are: Domain constraints, Entity integrity, Referential integrity, and General constraints (or check constraints).

#### 34. What are the phases of the Database Life Cycle in sequence?
**Answer:**
1. Scoping, 2. Conceptual Database Design, 3. Relational Database Design, 4. Normalization, 5. Physical Database Design.

#### 35. What are the phases of the Database Life Cycle?
**Answer:**
The phases are: 1. Scoping, 2. Conceptual Database Design, 3. Relational Database Design, 4. Normalization, and 5. Physical Database Design.

#### 36. What are the primary reasons for database normalization?
**Answer:**
Normalization is used to eliminate redundant data (reducing anomalies) and to ensure that data dependencies make logical sense.

#### 37. What are the primary targets of database normalization?
**Answer:**
The goals are to improve database design, eliminate redundancy, ensure data consistency, and allow for the loss-free decomposition of relations so that original data can be reconstructed through joins.

#### 38. What are the requirements for 1NF, 2NF, 3NF, and BCNF?
**Answer:**
1NF: All key attributes defined, no repeating groups, all attributes dependent on the primary key. 2NF: In 1NF and no partial dependencies (attributes depend on the whole primary key). 3NF: In 2NF and no transitive dependencies. BCNF: Every determinant must be a candidate key.

#### 39. What are the requirements for First Normal Form (1NF)?
**Answer:**
To be in 1NF: Define the data items required (columns), place related items in a table, ensure no repeating groups of data, and ensure a primary key is present.

#### 40. What are the rules for Normal Forms regarding dependencies?
**Answer:**
Functional dependencies alone are the primary concern for Boyce-Codd Normal Form (BCNF), while the combination of functional and multivalued dependencies determines 4th Normal Form (4NF).

#### 41. What are the three structured database approaches?
**Answer:**
The common approaches cited are ISCL (Information Systems Cycle/Life), SDLC (Software Development Life Cycle), and DSDLC (Database Software Development Life Cycle).

#### 42. What are the two ISO standard mechanisms for domain constraints?
**Answer:**
The CHECK clause and the CREATE DOMAIN statement.

#### 43. What defines the Second Normal Form (2NF)?
**Answer:**
A table is in 2NF if it meets all 1NF requirements and contains no partial functional dependencies, meaning all non-key attributes must be fully functionally dependent on the entire primary key.

#### 44. What do DSDLC, ISLC, and SDLC stand for?
**Answer:**
DSDLC: Database System Development LifeCycle; ISLC: Information Systems LifeCycle; SDLC: Software Development LifeCycle.

#### 45. What does it mean for columns to have integrity enhancement?
**Answer:**
It ensures data validity, specifically requiring that columns contain valid values and prohibiting NULLs where mandatory constraints are applied.

#### 46. What factors define a data model?
**Answer:**
Key factors include defining Dimensions and Facts, identifying Primary Keys for unique identification, determining Measures for calculation, and establishing the Granularity of the data (detail level).

#### 47. What is Design by Decomposition?
**Answer:**
A process of starting with a large, unnormalized relation and breaking it into smaller, logically sound relations that preserve all original dependencies and attributes without data loss.

#### 48. What is Normalization and what are its advantages?
**Answer:**
Normalization is the process of organizing a database to minimize data redundancy and dependency. By dividing tables and defining relationships between them, it helps reduce data anomalies, improve data integrity, and ensure consistency during updates. Common normal forms include 1NF, 2NF, 3NF, and BCNF.

#### 49. What is Physical Database Design?
**Answer:**
Physical Database Design defines the internal storage structures, file organizations, and access paths used by the DBMS to store and manage data efficiently.

#### 50. What is Scoping in the Database Life Cycle?
**Answer:**
Scoping involves analyzing the requirements domain and the user environment to determine the relevance, importance, and priorities for the resulting data model.

#### 51. What is a CHECK constraint?
**Answer:**
A CHECK constraint is used to enforce domain integrity by limiting the values that can be inserted into a column or ensuring that values across columns satisfy a specific condition.

#### 52. What is a DTD?
**Answer:**
DTD stands for Document Type Definition, used to define the structure and valid elements of an XML document.

#### 53. What is a Partial Dependency?
**Answer:**
A condition in database normalization where an attribute is functionally dependent on only a portion (subset) of a composite primary key.

#### 54. What is a Star Schema?
**Answer:**
A star schema is a relational database design for data warehouses consisting of a central 'Fact' table (containing metrics/measures) connected to multiple 'Dimension' tables (containing descriptive attributes).

#### 55. What is a data anomaly in a database?
**Answer:**
An anomaly is a condition where inconsistent changes exist in a database. It occurs when data redundancy leads to maintenance issues, such as failing to update an address in all locations where it is stored.

#### 56. What is a database staging area?
**Answer:**
A staging area is a temporary storage location used during the ETL process to hold data extracted from source systems. It allows for data transformation, cleansing, and validation before the data is loaded into the final production data warehouse.

#### 57. What is a partial dependency and which normal form is it associated with?
**Answer:**
A partial dependency occurs when a non-prime attribute is functionally dependent on only part of a composite primary key. This violates Second Normal Form (2NF).

#### 58. What is a star schema in the context of OLAP?
**Answer:**
A star schema is a type of relational schema used in OLAP applications, consisting of a central fact table surrounded by dimension tables.

#### 59. What is a transitive dependency in database normalization?
**Answer:**
A transitive dependency occurs when a non-prime attribute is dependent on another non-prime attribute, rather than directly on the primary key.

#### 60. What is a transitive dependency?
**Answer:**
A transitive dependency occurs when there are functional dependencies such that X→Y and Y→Z, where X is the primary key. Consequently, X→Z is a transitive dependency. A transitive dependency exists when a non-prime attribute determines another non-prime attribute, violating Third Normal Form (3NF).

#### 61. What is data inconsistency in a database?
**Answer:**
Inconsistency occurs when data does not comply with defined constraints or when multiple versions of the same data exist, leading to unreliable or conflicting results during processing.

#### 62. What is data integrity?
**Answer:**
Data integrity ensures accuracy and consistency: Entity (no duplicate rows), Domain (valid column values), Referential (consistent relationships between tables), and User-Defined (custom business rules).

#### 63. What is data redundancy?
**Answer:**
A condition where data is stored across several locations in a database, often intentionally implemented to improve performance or ensure consistency in distributed systems.

#### 64. What is database planning?
**Answer:**
The strategic process of determining how the database lifecycle stages can be realized most efficiently and effectively.

#### 65. What is referential integrity and how is it maintained?
**Answer:**
Referential integrity is a constraint that ensures a foreign key value must match an existing primary key value in the parent table. It is enforced via foreign key constraints or can be simulated using triggers.

#### 66. What is the Grain of Fact?
**Answer:**
The Grain of Fact (or Fact Granularity) refers to the lowest level of detail represented in a fact table in a data warehouse. It defines what a single row in the table represents (e.g., one transaction, one daily summary).

#### 67. What is the Transitive rule for Functional Dependencies (FD)?
**Answer:**
The Transitive rule for FD states that if A→B and B→C, then A→C.

#### 68. What is the Transitivity rule for Functional Dependencies (FD)?
**Answer:**
The Transitivity rule states that if A -> B and B -> C, then A -> C.

#### 69. What is the definition of Third Normal Form (3NF)?
**Answer:**
A table is in 3NF if it is already in Second Normal Form (2NF) and all non-primary fields are dependent only on the primary key (i.e., there are no transitive dependencies).

#### 70. What is the difference between Composition and Aggregation in UML?
**Answer:**
Composition (represented by a filled diamond) implies a strong ownership where the component cannot live without the container (typically 1..1). Aggregation (represented by an open diamond) implies a weaker association (typically 0..1) where the component can exist independently.

#### 71. What is the difference between a UNIQUE and non-UNIQUE clustered index?
**Answer:**
If a clustered index is non-UNIQUE, the engine automatically adds a hidden integer column (uniquifier) to ensure row uniqueness.

#### 72. What is the difference between a trivial and non-trivial functional dependency A -> B?
**Answer:**
A dependency is trivial if B is a subset of A. It is non-trivial if B is not a subset of A.

#### 73. What is the difference between attribute-based and tuple-based check constraints?
**Answer:**
Attribute-based constraints are applied to a single column (defined immediately after the attribute). Tuple-based constraints are applied to a set of columns (defined at the end of the table definition) to enforce relationships between attributes.

#### 74. What is the primary use of Normalization and how does it prevent data anomalies?
**Answer:**
Normalization is the process of structuring a database to reduce data redundancy and improve integrity. It eliminates insert, update, and delete anomalies by breaking tables into smaller, related partitions, ensuring that facts are stored in only one place.

#### 75. What is the purpose of Database Normalization?
**Answer:**
Normalization aims to organize data into relations to eliminate anomalies (insertion, update, deletion) and minimize data redundancy while ensuring no information loss occurs.

#### 76. What is the purpose of a mission statement and mission objectives in database planning?
**Answer:**
A mission statement defines the major aims of the database system, while mission objectives identify specific tasks that the system must support to achieve those aims.

#### 77. What is the purpose of functional dependencies in database systems?
**Answer:**
Functional dependencies define relationships between attributes, which are used for data integrity, storage efficiency/compression, and query optimization. A key property is the combining rule: if A->B1 and A->B2 and ... and A->Bn, then A -> B1, B2, ..., Bn.

#### 78. What is the purpose of the 'dbo' schema in Microsoft SQL Server, and why are schemas used?
**Answer:**
'dbo' stands for 'database owner' and is the default schema. Schemas are used to organize tables into logical subgroups and to facilitate permission management by allowing security policies to be applied to a group of objects at once.

#### 79. What is the purpose of the CHECK clause in domain constraints?
**Answer:**
It is used to verify that a value falls within a specified range or meets a defined boolean condition.

#### 80. What is the purpose of the CREATE DOMAIN statement?
**Answer:**
The CREATE DOMAIN statement is used to define a custom data type with specific constraints (such as CHECK constraints) that can be reused across multiple tables.

#### 81. What is the purpose of the model database in SQL Server?
**Answer:**
The model database acts as a template for all new databases created on the instance. Changes made to model are propagated to new databases. It is also the source used to recreate tempdb during server startup.

#### 82. What is the requirement for a foreign key in most current DBMS?
**Answer:**
Most modern DBMS require that a foreign key must reference a primary key or a unique constraint in the parent table, even if the SQL standard might allow references to non-unique columns.

#### 83. What is the rule for translating UML classes to relational schemas regarding primary keys?
**Answer:**
Every 'regular' class must have at least one primary key defined so that associations can be properly translated. Subclasses, association classes, and aggregated/composed classes may follow different rules based on their relationship type.

#### 84. What is the splitting rule for functional dependencies?
**Answer:**
The decomposition rule states: if A -> B1, B2, ..., Bn, then it is equivalent to A -> B1 and A -> B2 and ... and A -> Bn.

#### 85. What is the transitive property in functional dependencies (A ->> B, B ->> C implies A ->> C)?
**Answer:**
If attribute A determines B, and B determines C, then A also determines C (transitive dependency).

#### 86. What is vertical partitioning?
**Answer:**
Vertical partitioning is the process of splitting a table by moving some columns into a separate table to improve performance or security.

#### 87. What questions should you ask during a BI Stakeholder Analysis and Business Context review?
**Answer:**
Key questions include: Who are the user groups? How do they interact with data? Do they need self-service analysis or static reports? What business processes are critical to measure? Where does the source data originate? What are the data relationships and dependencies?

#### 88. What requirement must be met before adding a Primary Key to an existing table using ALTER TABLE?
**Answer:**
The target column(s) must have already been defined as NOT NULL.

#### 89. When are association classes considered unnecessary?
**Answer:**
Association classes are unnecessary if the multiplicity on both sides is 0..1 or 1..1, as the association can be folded into one of the participating classes.

#### 90. Which anomalies can persist in 2NF?
**Answer:**
Delete anomalies can still occur in 2NF, although Insert and Update anomalies are typically resolved.

#### 91. Why do we use integrity constraints?
**Answer:**
Integrity constraints are used to: 1) Prevent data-entry errors, 2) Enforce correctness criteria during updates, 3) Maintain data consistency, and 4) Inform the DBMS about the data's structure and rules.

#### 92. Why is a relation not in 2NF if a non-key attribute depends on only a subset of the candidate key?
**Answer:**
It fails 2NF because 2NF requires full functional dependency on the entire primary key. If an attribute depends only on part of the key (a proper subset), it is a partial dependency, which is prohibited in 2NF.

#### 93. Why is a table with a single-attribute primary key automatically in 2NF if it is in 1NF?
**Answer:**
Second Normal Form (2NF) requires the absence of partial dependencies. A partial dependency occurs only when a non-key attribute depends on part of a composite primary key. With a single-attribute PK, partial dependency is impossible.

#### 94. Why would a relation fail 3NF?
**Answer:**
A relation fails 3NF if it contains transitive dependencies, where non-key attributes depend on other non-key attributes, which in turn depend on the primary key. To reach 3NF, these must be decomposed.


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


## 📂 Category: Database Programmability (131 cards)

### 🟢 Junior Level

#### 1. Are variables and constants required to be declared?
**Answer:**
Yes, variables and constants must be declared before they can be referenced in other statements.

#### 2. How much space do views consume?
**Answer:**
Views consume very little space because the database only stores the definition of the view, not the data it presents.

#### 3. What are the core characteristics of a parameter in SQL?
**Answer:**
A parameter in SQL is defined by its name and its specific data type.

#### 4. What are the three SQL keywords used for procedure/function parameters?
**Answer:**
IN (input only), OUT (output only), and IN OUT (input and output).

#### 5. What is the CALL statement used for?
**Answer:**
The CALL statement is used to execute a stored procedure in databases that support it (such as MySQL or Oracle).

#### 6. What is the code inside a trigger called?
**Answer:**
The code within a trigger is referred to as the trigger body or the trigger action.

#### 7. What is the naming convention 'sp' (e.g., spXXX) in SQL procedures?
**Answer:**
It stands for 'stored procedure'.


### 🟡 Mid Level

#### 1. Are Views and tables in the same namespace?
**Answer:**
In MySQL, Views and tables share the same namespace.

#### 2. Are all database views updateable?
**Answer:**
No, not all views are updateable. Views that involve complex aggregations, joins, or certain set operators may be read-only because the database engine cannot map changes back to the underlying base tables unambiguously.

#### 3. Can CTEs be used for data modification operations like INSERT, UPDATE, or DELETE?
**Answer:**
Yes, Common Table Expressions (CTEs) can be used to perform data modification operations on the underlying tables.

#### 4. Generally, when a view includes aggregation (such as avg), does it make sense to allow modifications over this view?
**Answer:**
Generally, when a view includes aggregation (such as avg), it usually does not make sense to allow modifications (INSERT, UPDATE, DELETE) over this view because the underlying result set is not mapped 1:1 to the base table rows.

#### 5. How are database functions invoked?
**Answer:**
Functions can be invoked within SELECT, INSERT, or UPDATE statements.

#### 6. How are queries and modifications handled in virtual views?
**Answer:**
Since virtual views are logical constructs and not stored tables, queries are rewritten by the DBMS to reference the underlying base tables. Modifications can be ambiguous and are not always supported or automatic.

#### 7. How are stored procedures executed?
**Answer:**
Stored procedures are typically executed using an explicit CALL statement or the EXEC/EXECUTE command depending on the SQL dialect.

#### 8. How are triggers defined conceptually?
**Answer:**
Triggers are Event-Condition-Action (ECA) rules.

#### 9. How can stored procedures or functions improve application performance?
**Answer:**
They reduce network traffic by sending a single command rather than multiple, and they allow the database to pre-compile execution plans, reducing the parsing overhead for repetitive tasks.

#### 10. How can the order of execution be defined for AFTER triggers in SQL Server?
**Answer:**
By using sp_settriggerorder to specify 'FIRST', 'LAST', or 'NONE' (undefined).

#### 11. How can you reduce network traffic between applications and the database?
**Answer:**
By encapsulating logic within Functions and Stored Procedures, which allows the database to process data locally and return only the final result sets.

#### 12. How do you define and use functions in SQL?
**Answer:**
A function accepts zero or more parameters and returns a single value. Examples include: GETDATE() (no params), STR(numeric) (one param), CONVERT(type, val) (two params), and CONCAT('a', 'b', 'c') (multiple params).

#### 13. How do you manage views in SQL?
**Answer:**
A view is a virtual table based on a SELECT query. You can create one using 'CREATE VIEW view_name AS SELECT...', update it using 'CREATE OR REPLACE VIEW', and delete it using 'DROP VIEW view_name'. Views provide a way to simplify complex queries and restrict data access.

#### 14. How do you perform text manipulation like extraction and replacement in MS SQL?
**Answer:**
Use string functions: LEFT() or RIGHT() to extract from edges, SUBSTRING() with CHARINDEX() for middle segments, and STUFF() to replace or delete characters within a string.

#### 15. How does using stored procedures or functions improve security?
**Answer:**
They allow for the abstraction and isolation of underlying data tables, enabling fine-grained control over user access by granting permissions to the procedure rather than the table itself.

#### 16. How many values can be returned by a user-defined function?
**Answer:**
A scalar user-defined function returns exactly one value.

#### 17. What are DMVs (Dynamic Management Views)?
**Answer:**
DMVs are internal server objects (views and functions) used to monitor the current state of the database engine, perform diagnostics, and troubleshoot performance issues.

#### 18. What are the advantages and disadvantages of using Stored Procedures?
**Answer:**
Advantages: They support modular programming, allow code reuse, reduce network traffic, and provide better security. Disadvantages: They can only be executed within the database engine and consume additional memory on the database server.

#### 19. What are the benefits of using a database view?
**Answer:**
Views protect columns/rows to enhance security, simplify complex database structures to make queries easier to write, allow for different data representations, and provide data independence (logical decoupling from base tables). Views may be virtual and recreated each time they are referenced.

#### 20. What are the primary motivations for using database views?
**Answer:**
Views are used to: 1) Hide sensitive data from unauthorized users, 2) Simplify complex queries for end-users, and 3) Provide modularity to database access by decoupling the interface from the physical storage.

#### 21. What are the primary use cases for triggers?
**Answer:**
Triggers are used to enforce referential integrity constraints, implement complex business logic/constraints, and audit data changes.

#### 22. What are the roles of IN, OUT, and IN/OUT parameters in SQL stored procedures?
**Answer:**
IN: Input only; OUT: Output only (return value); IN OUT: Used for both input and returning a modified value.

#### 23. What are the three core parts of a PL/SQL block?
**Answer:**
1. Declaration (optional): Where variables, constants, cursors, and exceptions are defined. 2. Executable (mandatory): Where logic and variable manipulation occur. 3. Exception (optional): Where errors raised during execution are handled.

#### 24. What condition must be met for a view to be updateable?
**Answer:**
The view must be based on a single table; it cannot contain joins, aggregations, or unions if you intend to perform INSERT, UPDATE, or DELETE operations through it.

#### 25. What does ETL testing include?
**Answer:**
ETL testing involves: 1. Data Transformation: Ensuring business rules are applied correctly. 2. Data Integrity: Checking for truncation or loss during load. 3. Data Cleansing: Verifying invalid data is caught or replaced. 4. Performance: Ensuring load times meet SLAs.

#### 26. What does the 'WITH CHECK OPTION' do in a view?
**Answer:**
It ensures that any INSERT or UPDATE performed through the view must satisfy the criteria defined in the view's WHERE clause, preventing the creation of rows that would fall outside the view's definition.

#### 27. What does the FLOWR acronym stand for in XQuery?
**Answer:**
FLOWR stands for: For, Let, Order, Where, Return.

#### 28. What happens if a stored procedure expecting a Table-Valued Parameter (TVP) is called without one?
**Answer:**
The parameter will be treated as an empty table.

#### 29. What is SSIS?
**Answer:**
SSIS stands for SQL Server Integration Services. It is a platform for building enterprise-level data integration and data transformations solutions.

#### 30. What is a Stored Procedure?
**Answer:**
A Stored Procedure is a collection of SQL statements grouped together and stored in the database. It can be executed as a single unit, which improves performance, reusability, and maintainability by avoiding redundant code.

#### 31. What is a database View and how do you use it?
**Answer:**
A view is a virtual table based on the result-set of an SQL statement. It allows you to simplify complex queries, enforce security by restricting column access, and provide consistent data representations. You create one using 'CREATE VIEW view_name AS SELECT ...' and query it like a regular table.

#### 32. What is a database View?
**Answer:**
A View is a virtual table defined by a SELECT query. It extracts data from physical tables and presents it as a dynamic result set; it is non-persistent and does not store data itself.

#### 33. What is a database package?
**Answer:**
A package is a collection of procedures, functions, variables, and SQL statements that are grouped together and stored as a single program unit in the database.

#### 34. What is a temporary table in SQL Server, how is it created, and when is it deleted?
**Answer:**
A temporary table is stored in the 'tempdb' system database. Session-level temporary tables (prefix '#') are deleted when the creating session ends. Global temporary tables (prefix '##') are available to all sessions and are deleted when the last session referencing them closes. They are created using 'SELECT INTO #TempName' or 'CREATE TABLE #TempName'.

#### 35. What is a view, and what is the 'WITH CHECK OPTION' clause?
**Answer:**
A view is a virtual table representing a subset of columns or rows from one or more base tables. The 'WITH CHECK OPTION' clause ensures that any data modified or inserted through the view must satisfy the criteria defined in the view's WHERE clause.

#### 36. What is the difference between a Function and a Stored Procedure?
**Answer:**
Functions must return a value and are typically used in SELECT/WHERE clauses. Stored Procedures do not have to return a value, support input/output parameters, and can contain complex logic like try-catch blocks and DML operations that functions cannot perform.

#### 37. What is the difference between using a Function and a View?
**Answer:**
A view is typically used for virtual tables that may be queried frequently, whereas a function is often used when the data is not required every time the query executes or requires logic/parameters.

#### 38. What is the effect of creating a stored procedure with a '#' prefix?
**Answer:**
The procedure is created as a temporary object stored in tempdb.

#### 39. What is the lifecycle behavior of temporary objects in stored procedures?
**Answer:**
Upon procedure termination, temporary tables are truncated to one extent, but their statistics are retained.

#### 40. What is the primary motivation behind the use of triggers?
**Answer:**
The primary motivation is to move monitoring, business logic, or audit requirements from the application layer into the database management system itself.

#### 41. What is the primary role of XSLT and what does the acronym stand for?
**Answer:**
XSLT stands for Extensible Stylesheet Language Transformations. It is a language used to transform XML documents into other formats by matching and replacing templates of data.

#### 42. What is the purpose of Views in a database?
**Answer:**
Views extend database modularity and provide security by limiting the columns/rows a user can see. They are part of the three-level database architecture: Physical (disk), Conceptual (tables), and Logical (views).

#### 43. What is the purpose of procedures and functions in a database?
**Answer:**
Procedures and functions accept parameters from a calling program to perform a specific set of actions, including modifying and returning data. They promote modularity, extensibility, reusability, maintainability, and abstraction.

#### 44. What is the purpose of square brackets [..] in XPath?
**Answer:**
Square brackets [..] allow for the specification of a condition (predicates) to filter nodes.

#### 45. What is the purpose of the := operator in SQL?
**Answer:**
The := operator is used to assign a value to a variable, typically within the executable part of a PL/SQL block or procedural SQL environment.

#### 46. What is the purpose of the Lookup Transformation?
**Answer:**
The Lookup Transformation is used to retrieve data from a reference table based on a match from an input stream. It is commonly used for dimension attribute retrieval in Data Warehousing, identifying existing records for SCD (Slowly Changing Dimension) updates, or validating data integrity.

#### 47. What is the relationship between a trigger and a procedure or function?
**Answer:**
A procedure or function can be activated by a trigger. A procedure/function represents a single call or execution unit initiated by the trigger event.

#### 48. What limitations exist for creating an updateable view?
**Answer:**
To be updateable, views should generally avoid complex operations like aggregate functions, DISTINCT, GROUP BY, HAVING, or subqueries, as the database engine cannot reliably map changes back to the underlying base table rows.

#### 49. What methods can be used to update a table via SSIS?
**Answer:**
Common methods include using a SQL command, a staging table, a cache, the Script Task, or using the fully qualified database name.

#### 50. When should you use a view instead of a base table?
**Answer:**
A view is useful when you need a calculation or a specific projection of data performed every time a record is accessed without duplicating data, or to simplify complex queries for the end-user.

#### 51. Which SQL clauses are disallowed in updateable views?
**Answer:**
The clauses DISTINCT, GROUP BY, HAVING, and UNION are generally not allowed in updateable views.

#### 52. Why is it often preferable to use constraints instead of triggers?
**Answer:**
Constraints are more optimized by the database engine and avoid complex issues like chaining, termination problems, and non-deterministic execution order that can occur with triggers.


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


## 📂 Category: Joins & Set Operators (46 cards)

### 🟢 Junior Level

#### 1. Co je to JOIN operace v SQL?
**Answer:**
Operace umožňující kombinovat záznamy z více tabulek na základě společných atributů. Typy zahrnují: Natural Join (shodné názvy sloupců), Equijoin (rovnost hodnot) a Outer Join (zahrnuje i neshodné řádky s NULL hodnotami).

#### 2. Describe the different types of SQL Joins.
**Answer:**
INNER JOIN: Returns rows when there is a match in both tables. LEFT JOIN: Returns all rows from the left table and matched rows from the right. RIGHT JOIN: Returns all rows from the right table and matched rows from the left. FULL JOIN: Returns all rows when there is a match in either of the tables.

#### 3. Explain the UNION and UNION ALL operators.
**Answer:**
The UNION operator combines the result sets of two or more SELECT statements into a single result set. By default, UNION removes duplicate rows. UNION ALL keeps all rows, including duplicates. Requirements: Both queries must have the same number of columns, in the same order, with compatible data types.

#### 4. Explain the common types of joins in SQL.
**Answer:**
INNER JOIN returns rows with matches in both tables. LEFT JOIN returns all rows from the left table plus matching rows from the right. RIGHT JOIN returns all rows from the right table plus matching rows from the left. FULL JOIN returns all rows when there is a match in either table.

#### 5. How are multiple tables combined into a single result set?
**Answer:**
The JOIN operation is used to combine columns from multiple tables based on a related column between them.

#### 6. How are rows from two or more tables combined based on a common field?
**Answer:**
Using SQL Joins.

#### 7. How do you include duplicate rows when using a UNION operator?
**Answer:**
Use UNION ALL instead of UNION (which defaults to distinct values only).

#### 8. How do you join tables to retrieve related data?
**Answer:**
Use an INNER JOIN on the common key: SELECT FirstName, LastName, City FROM Employee INNER JOIN Location ON Employee.LocationID = Location.LocationID.

#### 9. How do you perform a LEFT JOIN and when is it typically used?
**Answer:**
A LEFT JOIN returns all rows from the left table and matching rows from the right table. If no match exists, the right side columns return NULL. It is used to expand a primary table with auxiliary information without losing data from the primary table.

#### 10. How do you query data from multiple tables simultaneously?
**Answer:**
Use a JOIN clause (INNER, LEFT, RIGHT, or FULL).

#### 11. In Relational Algebra, what is the difference between joining/cross-product and union operators?
**Answer:**
Cross-product and Join operators combine relations horizontally by adding columns/attributes. The Union operator combines relations vertically by adding rows/tuples, requiring compatible schemas.

#### 12. SQL JOINs: INNER, LEFT, RIGHT, and FULL
**Answer:**
A JOIN clause is used to combine rows from two or more tables based on a related column between them. (INNER) JOIN: Returns records with matching values in both tables. LEFT (OUTER) JOIN: Returns all records from the left table and matched records from the right. RIGHT (OUTER) JOIN: Returns all records from the right table and matched records from the left. FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table.

#### 13. What are the common types of SQL joins and how do they function?
**Answer:**
Inner Join: Returns rows where there is a match in both tables. Left Join: Returns all rows from the left table and the matched rows from the right table (unmatched right rows result in NULL). Right Join: Returns all rows from the right table and the matched rows from the left table (unmatched left rows result in NULL). Full Join: Returns all rows when there is a match in either the left or right table; non-matching side results in NULL.

#### 14. What are the various Join types available in T-SQL?
**Answer:**
Join types include: Inner Join, Outer Joins (Left, Right, Full), and Cross Joins. These can be further filtered using exclusion logic (e.g., LEFT OUTER JOIN where the right side is NULL).

#### 15. What condition is required for an INNER JOIN?
**Answer:**
An INNER JOIN requires at least two tables that share a common column or overlapping field to serve as the basis for the join relationship.

#### 16. What happens when an INNER JOIN is executed?
**Answer:**
An INNER JOIN returns only the records that have matching values in both tables being joined.

#### 17. What is an Equijoin?
**Answer:**
An Equijoin is a type of join that links tables based on the equality operator ('=') between columns, typically involving the primary key of one table and the foreign key of another.

#### 18. What is an Outer Join?
**Answer:**
An Outer Join retrieves rows that match the join condition as well as rows that do not match, returning NULL for columns of the table that lacks a match. Types include LEFT, RIGHT, and FULL joins.

#### 19. What is the difference between FULL OUTER JOIN and UNION?
**Answer:**
FULL OUTER JOIN combines result sets horizontally based on join predicates, whereas UNION combines result sets vertically by stacking rows from two or more SELECT statements.

#### 20. What is the difference between UNION and UNION ALL?
**Answer:**
UNION combines result sets from multiple SELECT statements and removes duplicate rows. UNION ALL combines results but preserves all rows, including duplicates, making it more performant.

#### 21. What is the difference between UNION and UNION ALL?
**Answer:**
UNION merges result sets from two structurally compatible tables and removes duplicate records from the final output. UNION ALL also merges the results but includes all duplicate records, making it more performant.

#### 22. What is the purpose of the JOIN operation in SQL?
**Answer:**
JOIN is used to combine columns from multiple tables into a single result set based on a related column between them.

#### 23. What is the result of an INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL OUTER JOIN?
**Answer:**
INNER JOIN: Returns rows with matches in both tables. LEFT JOIN: Returns all rows from the left, plus matches from the right. RIGHT JOIN: Returns all rows from the right, plus matches from the left. FULL OUTER JOIN: Returns all rows from both tables, filling with NULL where matches don't exist.

#### 24. Why do we need joins, and what is the syntax for a basic INNER JOIN?
**Answer:**
Joins are used to combine rows from two or more tables based on a related column between them. Syntax: SELECT columns FROM table1 INNER JOIN table2 ON table1.column = table2.column.


### 🟡 Mid Level

#### 1. Explain the difference between FULL JOIN and CROSS JOIN.
**Answer:**
FULL JOIN returns all rows for which there is a match in either table (combining LEFT and RIGHT outer joins). CROSS JOIN returns the Cartesian product of the two tables, pairing every row of the first table with every row of the second.

#### 2. Explain the difference between JOIN types (e.g., INNER, LEFT, RIGHT) using the Invoices/Customers scenario.
**Answer:**
INNER JOIN returns only rows with matches in both tables. LEFT JOIN returns all rows from the left table and matched rows from the right (or NULL if no match). RIGHT JOIN returns all rows from the right table and matched rows from the left (or NULL if no match). Using RIGHT JOIN with WHERE column IS NULL identifies rows in the right table that do not have a corresponding record in the left table.

#### 3. How can you identify rows in one table that have no matching records in another?
**Answer:**
Perform a LEFT JOIN between the two tables and add a WHERE clause filtering for NULL values on the right-side join key (e.g., WHERE Table2.ID IS NULL).

#### 4. How do you combine a LEFT JOIN and a RIGHT JOIN?
**Answer:**
The FULL OUTER JOIN returns all rows from both tables, filling with NULLs when there is no match in one of the sides.

#### 5. How does multiple INNER JOIN syntax work, and what should you watch out for?
**Answer:**
INNER JOIN correlates tables based on a link key, returning only rows where matches exist in both tables. Points to note: 1. Rows without matches are excluded. 2. If link keys are not unique, a Cartesian product effect occurs, duplicating rows based on matches. 3. Linking multiple tables requires each join to satisfy the join condition for the resulting set. 4. Data may appear multiple times if the join keys have one-to-many relationships.

#### 6. Jakým způsobem musí být data uspořádaná pro použití merge join?
**Answer:**
Data musí být seřazená podle spojovacích sloupců.

#### 7. SQL Self JOIN
**Answer:**
A self-join is a regular join where a table is joined with itself. It is often used to compare rows within the same table. To avoid cross-product duplicates (e.g., Amy/Doris and Doris/Amy), use an inequality operator (e.g., '<' or '>') in the WHERE clause instead of '<>'.

#### 8. The EXCEPT operator can be practically replaced by what?
**Answer:**
The EXCEPT operator can be replaced using subqueries with the 'IN' or 'NOT IN' operators, or by using 'LEFT JOIN' combined with a 'WHERE...IS NULL' filter to identify records present in one set but not the other.

#### 9. What are the common Relational Algebra operators?
**Answer:**
Projection: selects specific columns; Rename (Rho): changes names of relations or attributes; Cross-product: combines all rows from both relations; Natural Join: combines relations based on equality of all common attribute names.

#### 10. What are the requirements for using UNION in SQL?
**Answer:**
Each SELECT statement within a UNION must: 1) have the same number of columns, 2) have compatible data types for corresponding columns, and 3) return columns in the same order.

#### 11. What is a FULL OUTER JOIN?
**Answer:**
A FULL OUTER JOIN returns all records when there is a match in either the left or the right table. If a row in the left table does not have a match in the right table (or vice versa), the result set includes those rows with NULL values for the missing data.

#### 12. What is a Natural Join?
**Answer:**
A Natural Join is an equijoin that automatically joins tables based on columns with the same name in both relations.

#### 13. What is a self-join and how is it used?
**Answer:**
A self-join occurs when a table is joined with itself. It is commonly used to query hierarchical data, such as an Employee table where a column references the Manager's ID within the same table.

#### 14. What is a semi-join?
**Answer:**
A logical operation that returns rows from the first table only if there is at least one match in the second table, without producing duplicates from the second table.

#### 15. What is a theta-join?
**Answer:**
A theta-join is a join operation where the predicate uses comparison operators other than equality (i.e., it does not use '=').

#### 16. What is an anti semi join?
**Answer:**
An anti semi join is a logical operation that returns rows from the first table only when there is no matching row in the second table.

#### 17. What is the behavior of a FULL OUTER JOIN?
**Answer:**
A FULL OUTER JOIN returns all rows from both joined tables. If there is no match in one of the tables, the result set contains NULL values for the columns of the table that lacked a match.

#### 18. What is the difference between Hash Match joins and Merge joins?
**Answer:**
Hash match joins can handle unsorted data by building a hash table in memory. Merge joins require inputs to be pre-sorted on the join keys to perform efficiently.

#### 19. What is the difference between a Cross Join and a Natural Join?
**Answer:**
A Cross Join returns the Cartesian product of two tables (all possible combinations). A Natural Join automatically joins tables based on all columns with the same name and data type.

#### 20. What is the theta-join operator in relational algebra?
**Answer:**
A theta-join performs a join of two relations based on specific conditions. It is a shortcut for a cross product followed by a select, similar to a SQL JOIN with an ON condition.

#### 21. What set operators are used to process logical 'only', 'and', and 'or' relationships across result sets?
**Answer:**
EXCEPT (\diff) is used for 'only' or exclusion, INTERSECT for 'and' (intersection), and UNION for 'or' (merging ensembles).

#### 22. Write a query joining Invoices and Customers to retrieve invoice details and referrer names.
**Answer:**
SELECT i.Id, i.BillingDate, c.Name, r.Name AS ReferredByName FROM Invoices i JOIN Customers c ON i.CustomerId = c.Id LEFT JOIN Customers r ON c.ReferredBy = r.Id ORDER BY i.BillingDate;


## 📂 Category: Performance & Indexing (223 cards)

### 🟢 Junior Level

#### 1. How is the DROP INDEX statement used?
**Answer:**
The DROP INDEX statement removes an existing index from a table. Syntax varies by engine: 'DROP INDEX index_name ON table_name' (SQL Server) or 'ALTER TABLE table_name DROP INDEX index_name' (MySQL).

#### 2. What is IK?
**Answer:**
IK stands for Index Key.

#### 3. What is the Table Scan operator?
**Answer:**
An operator that retrieves all rows by scanning the entire table data (heap) without using an index.


### 🟡 Mid Level

#### 1. Difference between index rebuild and reorganize?
**Answer:**
An index rebuild drops and creates the index from scratch, defragmenting all pages. An index reorganize is an online operation that simply rearranges the existing leaf-level pages into a logical order.

#### 2. Explain the different types of indexes in SQL.
**Answer:**
1. Unique Index: Ensures no two rows have the same value in the indexed column. 2. Clustered Index: Determines the physical order of data in a table; there can be only one per table. 3. Non-Clustered Index: Stores the index in a separate structure from the data, containing pointers to the actual rows; a table can have many.

#### 3. How are data records ordered in index leaves?
**Answer:**
Data in index leaf nodes is ordered by the Clustered Key (CK).

#### 4. How do B-trees and Hash tables compare as indexing structures?
**Answer:**
Hash tables offer O(1) time complexity for exact equality lookups (A=V) but do not support range queries. B-trees (B+ trees) have logarithmic O(log n) complexity but are versatile, supporting both equality and range queries (e.g., A > V, A < V).

#### 5. How do Hash tables compare to Balanced Trees in database indexing?
**Answer:**
Hash tables provide faster lookup performance (constant time O(1)) compared to Balanced Trees (logarithmic time O(log n)), though they are generally only useful for equality matches rather than range queries.

#### 6. How do you create statistics for computed values (e.g., A*B)?
**Answer:**
Create a persisted computed column with the exact same formula, or use a column with the identical expression; the text representation must match exactly.

#### 7. How do you expose statistics for table variables to the query optimizer?
**Answer:**
Use the OPTION(RECOMPILE) query hint.

#### 8. How does a covering index improve performance compared to a full table scan?
**Answer:**
A covering index contains all the columns required by the query, allowing the database to satisfy the request using only the index pages, which are smaller and fewer than the full table pages.

#### 9. How many pages fit in one Megabyte?
**Answer:**
128 pages (since each page is 8KB).

#### 10. How many rows are in an intermediate index level?
**Answer:**
One for each page of the next lower level in the index tree.

#### 11. How much data fits on one standard SQL Server data page?
**Answer:**
8,060 bytes.

#### 12. Is it possible to index LOB columns?
**Answer:**
LOB columns cannot be indexed directly as a key column, but they may be included in non-clustered indexes using an 'INCLUDE' clause.

#### 13. What are Physical Design Advisors?
**Answer:**
They are automated tools used to analyze query workloads and suggest the optimal set of indexes to improve database performance.

#### 14. What are the downsides of using indexes?
**Answer:**
Indexes require additional storage space and impose overhead during data modifications (INSERT, UPDATE, DELETE) because the index must be maintained. High-frequency updates can significantly degrade write performance.

#### 15. What are the trade-offs of using indexes on a table?
**Answer:**
Indexes improve the performance of SELECT queries but increase the overhead for data modification operations (INSERT, UPDATE, DELETE) because the index must be reconstructed or maintained alongside the base data.

#### 16. What does it mean for a query to be 'Sargable'?
**Answer:**
Sargable (Search ARGument ABLE) refers to an expression that is structured in a way that allows the query optimizer to utilize an index for data retrieval.

#### 17. What does the 'impact' value in a missing index hint signify?
**Answer:**
It represents the estimated percentage improvement in query performance if the recommended index were created.

#### 18. What factors determine the effectiveness of an index?
**Answer:**
Effectiveness depends on the size of the table, data distribution, and the ratio of query read load versus update/write load.

#### 19. What is Denormalization?
**Answer:**
Denormalization is the process of moving from a higher normal form to a lower one, usually to reduce join complexity and increase read performance, at the risk of introducing data anomalies.

#### 20. What is a Clustered Key (CK)?
**Answer:**
A Clustered Key is the unique identifier or set of columns that determines the physical order of data rows in a table.

#### 21. What is a logical read in database performance monitoring?
**Answer:**
A logical read is a query statistic representing the process of reading a data page from the database buffer cache (RAM) rather than from the physical disk.

#### 22. What is a physical read in database performance monitoring?
**Answer:**
A query statistic indicating that a data page was retrieved directly from disk (I/O) rather than from the memory cache (buffer pool).

#### 23. What is an 'extent' in SQL Server?
**Answer:**
An extent consists of 8 physically contiguous pages.

#### 24. What is an Index?
**Answer:**
An index is a performance tuning structure that allows for faster retrieval of data by creating a sorted pointer structure for specific columns, reducing the need to scan entire tables.

#### 25. What is column selectivity?
**Answer:**
Selectivity is a property of a column indicating the ratio of unique values to total rows; higher selectivity means fewer rows share the same value, making it more efficient for index usage.

#### 26. What is external index fragmentation?
**Answer:**
External index fragmentation occurs when index pages do not follow each other logically/physically on an HDD, which can impact performance (though this is less severe on SSDs).

#### 27. What is internal index fragmentation?
**Answer:**
It occurs when index pages are not completely filled (less than 100% full), leading to inefficient storage and potential performance degradation.

#### 28. What is the Hash Aggregate operator?
**Answer:**
An aggregation operator that uses a hash table to group data when the input is not pre-sorted.

#### 29. What is the Key Lookup operator?
**Answer:**
An operator that retrieves non-indexed columns by looking up the clustered index (or base table) using a pointer from a non-clustered index.

#### 30. What is the Nested Loop operator?
**Answer:**
A join operator that iterates through the outer input and, for each row, performs a scan or lookup on the inner input.

#### 31. What is the Pareto Principle (80/20 rule) in the context of databases?
**Answer:**
A concept stating that approximately 80% of effects come from 20% of causes. In databases, this is often applied to performance tuning, where 80% of system performance issues are caused by 20% of the queries.

#### 32. What is the RID Lookup operator?
**Answer:**
An operator used to retrieve row data from a heap (non-clustered table) using a Row Identifier (RID).

#### 33. What is the SPARSE column property?
**Answer:**
A column property where NULL values consume zero space. Non-null values occupy slightly more space than a standard column (typically an additional 4 bytes) to manage the storage mapping.

#### 34. What is the Stream Aggregate operator?
**Answer:**
An aggregation operator that groups data by streaming, requiring the input to be pre-sorted by the grouping columns.

#### 35. What is the difference between CPU time and Elapsed time?
**Answer:**
CPU time is the duration the request was actively running on the processor. Elapsed time is the total wall-clock time from start to finish, including wait times, processing, and data transfer.

#### 36. What is the difference between Clustered and Non-Clustered Indexes?
**Answer:**
A Clustered Index determines the physical order of data in a table; a table can have only one. Non-Clustered Indexes are separate structures containing pointers to the data rows; a table can have multiple. Clustered indexes are generally faster for range retrievals.

#### 37. What is the impact of using indexes on frequently queried attributes?
**Answer:**
Using indexes on frequently queried attributes can provide a massive improvement in query performance.

#### 38. What is the limitation on row size in SQL Server?
**Answer:**
A single row must fit within a single page, which is 8,060 bytes.

#### 39. What is the purpose of CREATE INDEX and the 'DROP_EXISTING = ON' option?
**Answer:**
CREATE INDEX generates an index for efficient data retrieval. 'DROP_EXISTING = ON' is a specific command (e.g., in SQL Server) used to overwrite an existing index of the same name.

#### 40. What is the purpose of an SQL index and how do you create one?
**Answer:**
Indexes are used to speed up data retrieval/searches. They are created with 'CREATE INDEX index_name ON table_name (column_name);'. Note that indexes can slow down data modification (INSERT/UPDATE/DELETE) because the index itself must be updated, so they should be used judiciously on frequently queried columns.

#### 41. What is the purpose of an index in a database?
**Answer:**
An index is a persistent data structure used to significantly accelerate the retrieval of data by allowing the database engine to locate tuples directly without scanning an entire table.

#### 42. What is the purpose of the CREATE INDEX statement and how do you create a unique index?
**Answer:**
CREATE INDEX creates an index on specified table columns to improve query performance (e.g., 'CREATE INDEX idx_lastname ON Persons (LastName);'). A unique index, created with 'CREATE UNIQUE INDEX', prevents duplicate values in the indexed columns. Syntax varies by database system.

#### 43. What is the standard data page size in SQL Server?
**Answer:**
The standard page size is 8 kB.

#### 44. What types of indexes are available in SQL Server?
**Answer:**
Clustered: Stores data rows in order based on the index key. Nonclustered: Contains the key value and a row locator pointing to the data. Unique: Ensures no duplicate values in the index key. Full-text: Used for searching character-based data.

#### 45. sys.indexes
**Answer:**
A catalog view that contains a row for every index or heap in the database.


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

#### 16. How do indexes affect AND versus OR operators?
**Answer:**
For an AND operator, it is typically more efficient to have one composite index. For an OR operator, it is often better to have separate indexes on the involved columns.

#### 17. How do materialized views improve database performance?
**Answer:**
Materialized views improve performance by physically caching the result of a query, effectively acting like an index on a complex result set. The query optimizer can automatically rewrite queries to access this precomputed data rather than executing the original complex joins/aggregations.

#### 18. How do rows in intermediate pages differ between UNIQUE and non-UNIQUE indexes?
**Answer:**
In non-UNIQUE indexes, intermediate pages must include either the Row ID (RID) or the Clustered Key (CK) alongside the Index Key (IK) to uniquely identify entries.

#### 19. How do you force the SQL optimizer to consider indexes on a view?
**Answer:**
Use the WITH (NOEXPAND) table hint in the query.

#### 20. How do you trace the traffic hitting a SQL Server?
**Answer:**
SQL Profiler is the utility used to trace traffic. Traces can be filtered to capture specific transactions, reducing overhead, and saved/replayed for troubleshooting.

#### 21. How does a filtered index behave in a stored procedure?
**Answer:**
It is not used if the query uses a variable (parameter) in the predicate, because the optimizer cannot guarantee the filter condition. It must be explicitly used with OPTION (RECOMPILE).

#### 22. How does parameter sniffing occur with variables in SQL queries?
**Answer:**
Using a local variable in a query causes the SQL Server optimizer to ignore the specific value provided at execution time and instead compile a plan based on an 'average' distribution of data, which may lead to suboptimal performance.

#### 23. How does the Query Optimizer improve a trivial execution plan?
**Answer:**
It uses internal transformation rules to rewrite and optimize the plan.

#### 24. How does the cardinality estimator order multiple predicates?
**Answer:**
It orders them based on selectivity, which is the fraction of rows that satisfy a predicate.

#### 25. How is cache space for query plans managed?
**Answer:**
It is segmented into tiered levels where the system allocates different percentages of memory based on specific size thresholds.

#### 26. How is the duration of an operator calculated in query plans?
**Answer:**
It is calculated as: Time of Close() call - Time of Init() call.

#### 27. How is the level numbering system structured in an index tree?
**Answer:**
The leaf level is defined as level 0, and the root page is assigned the maximum number.

#### 28. How is the variable array stored in a record?
**Answer:**
It stores 2 bytes for the total number of variable columns and includes the end offsets for each non-null variable-length column.

#### 29. How large is a Record Identifier (RID)?
**Answer:**
8 bytes.

#### 30. How large is a forwarding pointer?
**Answer:**
16 bytes.

#### 31. How large is one quantum in SQL Server scheduling?
**Answer:**
4 ms.

#### 32. How many IAM pages exist in SQL Server?
**Answer:**
At least one per GAM extent containing pages of a tracked entity, and at least one per file containing pages of the entity.

#### 33. How many values are tracked in a standard SQL histogram?
**Answer:**
200 steps (values).

#### 34. How much I/O overhead does a RID lookup cost?
**Answer:**
One I/O normally, or two if a forwarding pointer must be followed.

#### 35. How much memory does SQL Server grant for a variable-length column?
**Answer:**
It typically grants 50% of the declared size.

#### 36. In which version was the Cardinality Estimator first changed in SQL Server?
**Answer:**
It was updated in SQL Server 2014 (compatibility level 120).

#### 37. Jaký cardinality estimator se použije bez traceflagů?
**Answer:**
Použije se podle nastaveného compatibility levelu databáze.

#### 38. Jaký operátor ochrání UPDATE před Halloween problémem?
**Answer:**
Spool operátor, který vytvoří dočasnou kopii dat.

#### 39. K čemu potřebují spool operátory memory grant nebo tempdb?
**Answer:**
K uložení mezivýsledku (datasetu) pro jeho opakované čtení nebo zpracování.

#### 40. K čemu využívá hash match operátor memory grant?
**Answer:**
Memory grant se využívá pro vytvoření hash tabulky z tzv. 'build' vstupu. 'Probe' vstup paměť pro operaci nepotřebuje.

#### 41. Kdy mohou být hodnoty rebind a rewind různé od 0?
**Answer:**
Tento stav nastává u vnitřního vstupu operátoru nested loop join.

#### 42. Kdy se použije triviální plán?
**Answer:**
Triviální plán se použije v momentě, kdy optimalizátor vyhodnotí existující plán jako 'good enough' (dostatečně efektivní bez nutnosti hlubokého hledání).

#### 43. Kolik je minimální memory grant?
**Answer:**
Minimální alokace paměti (memory grant) je 1 MB.

#### 44. Kolik je v SQL serveru (S)GAM stránek?
**Answer:**
(S)GAM stránky se nacházejí jednou za 64 000 extentů (cca 4 GB), minimálně však jednou pro každý soubor databáze.

#### 45. Která část Query Optimizeru nahrazuje komplikovanější operátory za základní (např. between na >= a <=)?
**Answer:**
Tuto transformaci provádí tzv. Algebraizer.

#### 46. Které jsou tzv. 'Stop & Go' operátory?
**Answer:**
Jedná se o operátory Hash Match (částečně) a Sort, které musí načíst všechna data předtím, než mohou vydat první řádek.

#### 47. Který proces způsobuje náhlé zpomalení procedury, která dříve běžela rychle?
**Answer:**
Jde o 'Parameter Sniffing', kdy dojde k rekompilaci plánu na základě specifických (a nevýhodných) parametrů volání.

#### 48. On what type of pages is the PFS (Page Free Space) byte applicable?
**Answer:**
PFS pages track page allocation and free space, primarily applicable to heap table pages in SQL Server.

#### 49. S čím souvisí rozhodnutí použít materializované pohledy (materialized views)?
**Answer:**
Rozhodnutí je otázkou kompromisu mezi rychlostí čtení (query) a režií při zápisu (update), podobně jako u indexů.

#### 50. What are LOBs (Large Objects) and LOB pages in a database?
**Answer:**
LOBs (Large Objects) are data types used to store large amounts of data (e.g., text, images). LOB pages are internal storage pages specifically allocated for variable-length data types marked as MAX.

#### 51. What are common DBCC commands for query tuning and debugging?
**Answer:**
Key commands include: 'DBCC FREEPROCCACHE' to clear the plan cache; 'DBCC TRACEON(XYZ)' to enable specific trace flags (add '-1' to apply globally); 'DBCC TRACEON(3604)' to route output to the session window; 'DBCC HELP' to view documentation; and 'DBCC OPTIMIZER_WHAT_IF' to test optimizer behavior under hypothetical conditions.

#### 52. What are common SQL Server trace flags for performance tuning?
**Answer:**
Traceflag 174: Increases cached plan count. 2312: Forces current cardinality estimator. 3604: Sends output to session window. 7471: Uses UPD lock for UPDATE STATISTICS. 8649: Forces parallelism. 8780: Increases query compilation transformation limits. 9481: Forces legacy cardinality estimator.

#### 53. What are incremental statistics?
**Answer:**
Incremental statistics refer to a performance optimization where database statistics are updated only for the newest partition of a partitioned table rather than re-scanning the entire table.

#### 54. What are non-page latches typically used for?
**Answer:**
Non-page latches are typically used to protect metadata pages or other internal memory structures in a database engine.

#### 55. What are sql_statement_starting/completed/recompile in Extended Events?
**Answer:**
These are events used in SQL Server's Extended Events framework to track the lifecycle of ad-hoc queries or stored procedure executions, useful for performance monitoring and debugging.

#### 56. What are the core components of the Relational Engine?
**Answer:**
The relational engine is comprised of the Query Processor, which includes the Language Processing/Parser, the Query Optimizer (which determines the execution plan), and the Query Executor (which runs the plan).

#### 57. What are the ideal conditions for a Nested Loop join operator?
**Answer:**
It is most efficient when the outer input has a small number of rows and the inner input has a low-cost subtree (often indexed).

#### 58. What are the inputs of a Hash Match operator?
**Answer:**
The top input is the 'build' input, and the bottom input is the 'probe' input.

#### 59. What are the maximum limits for index keys in SQL Server?
**Answer:**
The maximum index key size is 900 bytes for versions before SQL Server 2016, and 1700 bytes for 2016 and later. The maximum number of columns is 16 and 32, respectively.

#### 60. What are the physical implications of data modification on indexes and pages?
**Answer:**
When a row in a clustered index is updated and exceeds page space, a page split occurs. If a row with a forwarding pointer is moved again, the forwarding pointer is updated to reflect the new location. Additionally, non-clustered indexes are typically not rebuilt when the underlying clustered index is rebuilt.

#### 61. What are the primary underlying data structures for database indexes?
**Answer:**
The two main structures are B-Trees (B-Trees or B+Trees), which support equality and range comparisons, and Hash Tables, which are optimized for constant-time equality lookups.

#### 62. What are the reasons for early statement termination during plan compilation?
**Answer:**
Time Out (limit on transformations reached), Memory (insufficient memory), or 'Good Enough' (an optimal or sufficient plan was found).

#### 63. What are the storage characteristics and statistical differences between temporary tables and table variables?
**Answer:**
Temporary tables are stored in tempdb on disk and support statistics. Table variables are also stored in tempdb, but do not maintain histograms or updateable statistics, which can impact query optimizer performance.

#### 64. What causes the 'ERROR 666' in SQL Server?
**Answer:**
This error is emitted when the internal hidden integer column used to manage non-unique clustered keys overflows its allocated storage limit.

#### 65. What condition is required for a Merge Join?
**Answer:**
A Merge Join requires an equijoin condition and sorted inputs on the join keys.

#### 66. What do common SQL Server wait types signify: CX_PACKET, CXCONSUMER, and RESOURCE_SEMAPHORE?
**Answer:**
CX_PACKET: Parallelism wait (thread waiting on other threads/processor). CXCONSUMER: Parallelism wait (parent waiting on child). RESOURCE_SEMAPHORE: Waiting for a memory grant.

#### 67. What do sys.indexes.index_id values represent?
**Answer:**
0 indicates a heap (table with no clustered index), 1 indicates a clustered index, and values greater than 1 indicate nonclustered indexes.

#### 68. What does "cost" in an execution plan mean?
**Answer:**
It is an estimate of the processing time an operator will take, relative to the total cost of the query plan.

#### 69. What does 'number of rows to be read' (residual reads) mean in query statistics?
**Answer:**
This refers to the number of pages/rows that had to be physically read by the storage engine to retrieve columns not covered by the index (often called key lookups or residual reads).

#### 70. What does an RID contain?
**Answer:**
A Record Identifier (RID) typically contains references to the file ID, page ID, and row number.

#### 71. What does sys.dm_exec_query_statistic_XML(session_id) do?
**Answer:**
Returns information about currently running query in a selected session, typically used for troubleshooting execution plans. Note that it often requires specific trace flags enabled.

#### 72. What happens if you disable a clustered index?
**Answer:**
Access to the entire table is disabled in most SQL implementations.

#### 73. What is %%physloc%% in SQL Server?
**Answer:**
%%physloc%% is a virtual column that contains the physical address (RID - Row Identifier) of a row in a table.

#### 74. What is 'cache bloat' in a SQL server context?
**Answer:**
Cache bloat is the exhaustion of memory caused by storing an excessive number of unique query plans, often due to lack of parameterization.

#### 75. What is 'hole-filling optimization' in the context of MERGE statements?
**Answer:**
An optimization where, if a MERGE statement only inserts rows into the gaps in a clustered key, it can avoid HALLOWEEN protection logic.

#### 76. What is DBCC?
**Answer:**
DBCC (Database Console Commands) are administrative tools used to perform maintenance, validation (like CHECKDB), information gathering, and miscellaneous tasks in SQL Server.

#### 77. What is Fill Factor?
**Answer:**
Fill Factor is an index setting that determines the percentage of space to be filled with data on each leaf-level index page. It helps manage page splits in frequently updated tables.

#### 78. What is LPE in the context of database engine operations?
**Answer:**
LPE stands for Language Processing and Execution, referring to the stages where a SQL statement is parsed, optimized, and executed.

#### 79. What is Page Free Space (PFS) in SQL Server?
**Answer:**
PFS pages are specific pages in the database that track the amount of free space available on data pages (using one byte per page).

#### 80. What is SGAM?
**Answer:**
SGAM stands for Shared Global Allocation Map. It is a system page used in SQL Server to track which extents in a database are currently mixed and have at least one free page available.

#### 81. What is a 'Rebind' operation in query execution?
**Answer:**
A process where the conditions of a spool operator are re-evaluated or re-initialized before the operator begins reading the rows again.

#### 82. What is a 'Rewind' operation in query execution?
**Answer:**
An operation where the database restarts reading a spool or table from the beginning.

#### 83. What is a 'read-ahead read' in database performance?
**Answer:**
A performance optimization where the database engine loads consecutive data pages into memory before they are explicitly requested, reducing I/O wait times.

#### 84. What is a 'stub' query plan?
**Answer:**
A stub query plan refers to a cached hash of an execution plan that does not contain the actual compiled plan details, often seen when memory pressure or specific cache settings prevent full plan storage.

#### 85. What is a 'trivial plan' in query optimization?
**Answer:**
A trivial plan is a simple execution plan consisting only of basic scans or seeks, created without applying complex algebraic transformations or optimization rules.

#### 86. What is a GAM page?
**Answer:**
GAM stands for Global Allocation Map, which tracks which extents have been allocated in a SQL Server data file.

#### 87. What is a Global Allocation Map (GAM) in database storage?
**Answer:**
A GAM page is a specialized storage page that tracks extent allocation. It uses a bitmask where 'true' indicates an unallocated extent and 'false' indicates an allocated extent.

#### 88. What is a Nested Loop join?
**Answer:**
A Nested Loop join is an algorithm suitable for joining a small dataset with a larger one. It iterates through each row of the outer table and performs a lookup in the inner table, making it very effective when the inner table is indexed.

#### 89. What is a Physical Design Advisor and how does it function?
**Answer:**
It is a tool that analyzes database statistics and workload to recommend optimal indexes. It functions by testing various index combinations against the Query Optimizer to estimate execution costs, selecting the configuration where performance benefits outweigh maintenance overhead.

#### 90. What is a RID (Row Identifier)?
**Answer:**
A Row Identifier (RID) is a unique pointer to a specific row within a table, typically used by SQL Server to locate a row on a data page.

#### 91. What is a SQL-OS Scheduler?
**Answer:**
A component of SQL Server's operating system abstraction layer that manages the execution and scheduling of tasks on a single logical processor.

#### 92. What is a cardinality estimator?
**Answer:**
A cardinality estimator is a component of the SQL query optimizer that predicts the number of rows that will result from a specific query operator or plan.

#### 93. What is a database worker?
**Answer:**
A worker is a thread or process directed by the scheduler to perform specific tasks or queries.

#### 94. What is a forwarding pointer?
**Answer:**
A forwarding pointer is a pointer used in a heap-organized table to redirect to a row's new location if it has moved (e.g., due to an update that caused row migration).

#### 95. What is a hash_warning in SQL Server?
**Answer:**
A hash_warning is an extended event triggered when a hash join or hash aggregation operation exceeds the available memory grant, forcing the operation to spill data to tempdb (disk).

#### 96. What is a potential issue with (S)GAM pages in tempdb?
**Answer:**
They can become a contention bottleneck (latching) in high-concurrency environments because tempdb frequently allocates and deallocates pages for temporary objects.

#### 97. What is a query_hash?
**Answer:**
A hash value representing the structure of a query, excluding literals, used to identify identical queries even if parameter values differ.

#### 98. What is a row overflow page?
**Answer:**
A row overflow page stores variable-length data (such as varchar or nvarchar) that exceeds the storage capacity of a single data page (typically when it exceeds 8000 bytes).

#### 99. What is a sort_warning?
**Answer:**
An extended event triggered by the SQL Server engine when a sort operation (such as during a join or order by) exceeds the allocated memory, forcing it to spill to TempDB.

#### 100. What is a transformation rule in the context of database query processing?
**Answer:**
A transformation rule is a rule that maps logical or physical operations into other equivalent operations, often used by query optimizers to find more efficient execution plans.

#### 101. What is an 'exchange_spill' in SQL Server?
**Answer:**
An 'exchange_spill' is an Extended Event that occurs when parallel query execution processes run out of allocated memory (specifically in the exchange buffers) and are forced to spill data to the tempdb.

#### 102. What is an IAM and an IAM chain?
**Answer:**
IAM stands for Index Allocation Map. An IAM chain is a linked list of IAM pages that track the extents allocated to a single database entity (table or index).

#### 103. What is an index spool?
**Answer:**
An index spool is an execution operator that builds a temporary index over a dataset during query execution to optimize performance for that specific query.

#### 104. What is auto-parameterization in an SQL engine?
**Answer:**
It is a process where the SQL server treats ad-hoc queries as if they were stored procedures by automatically replacing constant values with parameters to improve plan reuse.

#### 105. What is data flow in the context of query execution plans?
**Answer:**
Data flow refers to the directional movement of data rows through an execution plan, typically visualized as reading the plan from right to left (the direction of data processing).

#### 106. What is density in database statistics?
**Answer:**
Density is a statistic computed as 1 / count(distinct), used by the query optimizer to estimate the selectivity of column values.

#### 107. What is forced automatic parametrization in SQL Server?
**Answer:**
Forced automatic parametrization is a setting in SQL Server where the query optimizer attempts to parameterize every query to improve plan reuse.

#### 108. What is interleaved execution in the context of query optimization?
**Answer:**
It is a process where the query optimizer executes a multi-statement Table-Valued Function (TVF) during the optimization phase to obtain a more accurate execution plan.

#### 109. What is meant by 'control flow' in query execution?
**Answer:**
It refers to the process of reading the execution plan by tracing the actual method calls of the operators during query execution.

#### 110. What is osstress.exe?
**Answer:**
A Microsoft tool used to perform stress testing on database systems.

#### 111. What is simple auto-parameterization?
**Answer:**
A server setting that allows the DBMS to automatically parameterize trivial queries, which helps in reusing execution plans and reducing compilation overhead.

#### 112. What is the 'OPTIMIZE FOR UNKNOWN' query hint?
**Answer:**
A query hint that instructs the query optimizer to use a plan based on average statistics rather than parameter-specific values.

#### 113. What is the 'cost threshold for parallelism' in SQL Server?
**Answer:**
A server-level setting that specifies the minimum cost required for a query plan to be considered for parallel execution.

#### 114. What is the 'optimize for ad hoc workloads' setting?
**Answer:**
A SQL Server configuration that stores only a small compiled plan stub on the first execution of a batch, reducing plan cache bloat.

#### 115. What is the 'tipping point' in SQL Server indexing?
**Answer:**
The tipping point is the specific threshold of I/O operations (percentage of rows) at which the query optimizer decides that performing an index seek is less efficient than performing a full table scan.

#### 116. What is the 'tipping point' in database page estimation?
**Answer:**
The tipping point is generally between 30% and 33% of table pages. For extremely small rows (such as many-to-many link tables), it is closer to 25%.

#### 117. What is the Adaptive Join operator?
**Answer:**
An operator that dynamically chooses between a nested loop or a hash match join based on the actual number of rows processed during execution.

#### 118. What is the Algebraizer and the Algebraizer Tree?
**Answer:**
The Algebraizer is a component of the relational engine that transforms a parser tree into an algebraizer tree. The algebraizer tree represents the structural plan of data joins and data sources for a query.

#### 119. What is the Bitmap operator?
**Answer:**
An operator used for efficient multi-threaded filtering, often used to improve join performance in parallel plans.

#### 120. What is the CXCONSUMER wait type in SQL Server?
**Answer:**
CXCONSUMER is a wait type introduced in SQL Server 2017 to track threads waiting for parallel process data from a producer thread in a parallel query plan.

#### 121. What is the Eager Spool operator?
**Answer:**
A spool operator that reads and stores all input rows from its child operator upon the first GetNext() call.

#### 122. What is the Global Allocation Map (GAM) page?
**Answer:**
The GAM page manages extent allocation. It contains flags: 'true' indicates mixed extents with at least one unallocated page, and 'false' indicates uniform extents or completely full mixed extents.

#### 123. What is the Lazy Spool operator?
**Answer:**
A spool operator that reads rows from its input only as they are requested by the parent operator.

#### 124. What is the MIN_GRANT_PERCENT query hint?
**Answer:**
A hint that sets the minimum desired memory grant percentage for a query.

#### 125. What is the OPTION (FAST N) query hint?
**Answer:**
A hint that tells the query optimizer to optimize for retrieving the first N rows as quickly as possible.

#### 126. What is the OPTION (NO_PERFORMANCE_SPOOL) hint?
**Answer:**
A hint that instructs the query optimizer to avoid using a performance spool operator in the query execution plan.

#### 127. What is the OPTION (QUERYRULEOFF) hint?
**Answer:**
A hint used to disable specific transformation rules used by the Query Optimizer during plan generation.

#### 128. What is the OPTION (QUERYTRACEON XYZ) hint?
**Answer:**
A hint used to enable a specific trace flag only for the scope of the individual query.

#### 129. What is the SQL Server Query Store?
**Answer:**
A SQL Server feature that logs SQL queries, their execution plans, and performance metrics over time to assist in troubleshooting and performance tuning.

#### 130. What is the compilation cost of the MERGE statement compared to standard DML?
**Answer:**
The compilation cost of MERGE is significantly higher than that of equivalent individual INSERT, UPDATE, or DELETE statements.

#### 131. What is the default maximum memory grant for a SQL Server query?
**Answer:**
The default maximum memory grant is typically 20% of the total available server memory.

#### 132. What is the difference between a 'predicate' and a 'seek predicate' in an execution plan?
**Answer:**
A 'seek predicate' is used by the engine to navigate the index tree to find specific data. A 'predicate' (or residual predicate) is a filter applied to the rows after they have been retrieved, used for columns not covered by the index key.

#### 133. What is the difference between a Page IO latch and a Page latch?
**Answer:**
A Page IO latch manages access to a data page while it is being transferred from or to disk. A Page latch is used to manage access to a page already residing in memory.

#### 134. What is the difference between a logical and a physical operator?
**Answer:**
Logical operators describe the algebraic operation to be performed (e.g., Join, Group). Physical operators are the actual algorithms used by the engine to execute these operations (e.g., Hash Match, Nested Loops).

#### 135. What is the difference between forward and backward index scans?
**Answer:**
Forward index scans can be parallelized, whereas backward index scans generally cannot.

#### 136. What is the fastest collation?
**Answer:**
The binary collation (e.g., XY_BIN2) is typically the fastest, as it sorts data based on character code values rather than linguistic rules.

#### 137. What is the function of GAM and SGAM pages in SQL Server?
**Answer:**
GAM (Global Allocation Map) and SGAM (Shared Global Allocation Map) pages are used to track and manage the allocation of extents within a database file, helping the engine find available pages for new objects.

#### 138. What is the function of the Close() method in query execution operators?
**Answer:**
Close() is a method of physical query operators used to terminate processing and release associated resources.

#### 139. What is the function of the GetNext() method in physical database operators?
**Answer:**
GetNext() is a method of a physical query operator that iterates through and returns the next single row from the operator's input source.

#### 140. What is the nature of a WHERE predicate in a filtered index?
**Answer:**
The WHERE predicate in a filtered index is limited; it only allows simple comparisons and cannot contain subqueries, complex functions, or user-defined logic.

#### 141. What is the output of the SQL Parser?
**Answer:**
The output is a parse tree representing the logical structure of the SQL statement.

#### 142. What is the potential performance issue when using a filtered index with an IS NULL predicate?
**Answer:**
If the column in the predicate is NULL and is not included in the index key (IK), the query engine may resort to a lookup instead of an index seek, even if the index should ideally be covering. To achieve a seek, the nullable column must be part of the index key.

#### 143. What is the primary objective of Query Planning/Optimization?
**Answer:**
The main objective is to implement the most efficient use of indexes and execution paths to retrieve data.

#### 144. What is the purpose of DBCC PAGE?
**Answer:**
DBCC PAGE is an undocumented/internal command used to inspect the raw contents of a database data page, typically used for low-level troubleshooting or educational analysis of how data is stored on disk.

#### 145. What is the purpose of the Init() method in SQL execution operators?
**Answer:**
It serves as the operator's initialization phase, preparing the necessary resources for execution.

#### 146. What is the purpose of the MAX_GRANT_PERCENT query hint?
**Answer:**
MAX_GRANT_PERCENT is a query hint that sets the maximum allowable memory grant (as a percentage of total buffer pool memory) for a specific query execution.

#### 147. What is the purpose of trace flag 8780 in SQL Server?
**Answer:**
Trace flag 8780 is used to generate XML for use in a USE PLAN hint, often for the purpose of comparing query plans or forcing a specific execution plan.

#### 148. What is the role of the Algebraizer in the SQL Server relational engine?
**Answer:**
The Algebraizer is the component that resolves names (like table and column names) into internal object IDs and creates the initial query tree structure.

#### 149. What is the role of the row offsets table?
**Answer:**
The row offsets table is a part of the data page that stores the starting byte addresses (offsets) of the rows stored on that page.

#### 150. What is the size of a database page header?
**Answer:**
The standard size of a database page header in many systems like SQL Server is 96 bytes.

#### 151. What is the size of a row header?
**Answer:**
The row header is 4 bytes in size.

#### 152. What is the subtree cost of an operator in an execution plan?
**Answer:**
The subtree cost represents the total estimated cost of an operator plus the accumulated cost of all its child nodes in the execution plan tree.

#### 153. What issue can occur when comparing char and nchar columns with SQL_* collations?
**Answer:**
Collation mismatches or data type precedence issues (like Unicode vs non-Unicode) can prevent efficient index usage, often leading to full table scans or conversion errors.

#### 154. What latching issue is associated with identity primary keys?
**Answer:**
Identity primary keys often cause 'last-page' contention, where multiple concurrent inserts attempt to write to the same last page of the B-tree index, creating latch contention on the data page.

#### 155. What occurs during the Init() and GetNext() phases of a Hash Match operator?
**Answer:**
Init() builds a hash table from the 'build' input. GetNext() calls the probe operator and searches for matches within that built hash table.

#### 156. When does SQL Server use 'density' in query optimization?
**Answer:**
SQL Server uses density statistics when an equality predicate is used in the WHERE clause with a variable, or when the 'OPTIMIZE FOR UNKNOWN' hint is provided, as it estimates selectivity based on the average distribution of data.

#### 157. When is an execution plan built in relation to variable substitution?
**Answer:**
The execution plan is compiled and built before the local variables are substituted with actual values. This is why parameter sniffing can occur, as the plan is optimized based on the structure rather than the specific data distribution of the parameters at the time of initial compilation.

#### 158. Where can information about SQL Server wait types be found?
**Answer:**
Wait types are documented in the system view sys.dm_os_wait_stats.

#### 159. Which actions prevent the caching of temporary objects in SQL Server?
**Answer:**
Actions such as creating an index, running ALTER TABLE, or defining a named constraint prevent caching.

#### 160. Why might a predicate in an index seek operator be inefficient?
**Answer:**
A predicate in a seek operator might be considered inefficient or 'bad' if it hides an underlying index scan, meaning the engine is doing more work than a precise seek should entail.

#### 161. sys.dm_db_index_operational_stats
**Answer:**
A Dynamic Management Object (DMO) that returns low-level, detailed statistics regarding index access, locking, and latching activity.

#### 162. sys.dm_db_index_physical_stats
**Answer:**
A system function that returns size and fragmentation information about indexes, supporting varying levels of detail (LIMITED, SAMPLED, or DETAILED).

#### 163. sys.dm_db_index_usage_stats
**Answer:**
A Dynamic Management Object (DMO) that returns information about how frequently indexes are used and the specific types of operations performed (seeks, scans, lookups, updates).

#### 164. sys.dm_exec_cached_plans
**Answer:**
A system view that returns information about all query execution plans that are currently stored in the plan cache.

#### 165. sys.dm_exec_plan_attributes
**Answer:**
A system function that returns information about specific attributes (such as SET options or database context) of a particular plan that influenced its compilation.

#### 166. sys.dm_exec_query_optimizer_info
**Answer:**
A system table providing detailed statistics and information about the Query Optimizer's behavior and operations since the last server restart.

#### 167. sys.dm_exec_query_plan
**Answer:**
A system function that retrieves the XML representation of a specific execution plan based on a given plan handle.

#### 168. sys.dm_exec_query_stats
**Answer:**
A system function that returns aggregate performance statistics (CPU, duration, reads, writes) for cached query plans.

#### 169. sys.dm_exec_requests
**Answer:**
A Dynamic Management Object (DMO) used to view all currently executing requests or tasks within the SQL Server instance.

#### 170. sys.dm_exec_sql_text
**Answer:**
A system table function that returns the text of the SQL batch corresponding to a specific query plan handle.

#### 171. sys.dm_exec_transformation_stats
**Answer:**
A system table containing statistics regarding the usage of specific transformation rules applied by the Query Optimizer.

#### 172. sys.dm_os_wait_stats
**Answer:**
A system function that returns information about all wait types encountered by threads during the execution of tasks.

#### 173. sys.dm_os_waiting_tasks
**Answer:**
A Dynamic Management Object (DMO) that returns information about all tasks currently in a 'waiting' state, including the resource they are waiting for.

#### 174. sys.fn_PhysLocFormatter
**Answer:**
A function that parses and formats the output of the %%physloc%% virtual column into a human-readable format (FileID:PageID:SlotID).

#### 175. sys.system_internals_allocation_units
**Answer:**
An undocumented system table that provides low-level information about allocation units, including pointers to IAM pages, root index pages, and the first leaf pages.

#### 176. What is the Leftmost Prefix Rule in composite indexing?
**Answer:**
When using a composite index on multiple columns, e.g. `(A, B, C)` (`CREATE INDEX idx_abc ON users (tenant_id, status, created_at)`):
- **Works for:** `WHERE tenant_id = 1`, `WHERE tenant_id = 1 AND status = 'active'`, etc.
- **Fails (skips index):** `WHERE status = 'active'` (because column `A` is skipped).
- **Rule:** Always put the most frequently filtered column or tenant/parent ID first in composite indexes.

#### 177. What is the ESR (Equality, Sort, Range) Rule for composite index design?
**Answer:**
When designing a composite index for complex queries, order the columns by:
1. **Equality (`=`):** Put exact match columns first (e.g. `tenant_id = 5`).
2. **Sort (`ORDER BY`):** Put ordering columns next (e.g. `ORDER BY created_at DESC`).
3. **Range (`>`, `<`, `LIKE 'abc%'`):** Put range or wildcard columns last.
**Why?** Once an index encounters a range condition (`LIKE` or `>`), it cannot use subsequent columns in the index for exact sorting.

#### 178. How does a database fetch data after jumping to a secondary index vs. a covering index?
**Answer:**
- **Secondary Index:** Stores indexed columns + Primary Key ID. For `SELECT * FROM comments WHERE path LIKE '001%'`, the DB searches `idx_path` to find matching IDs (1st jump), then looks up those IDs in the Primary Key table to fetch full row data (2nd jump — "Bookmark Lookup").
- **Covering Index:** If a query selects ONLY columns that are present inside the index (e.g. `SELECT id, status FROM users WHERE tenant_id = 5` when index is `(tenant_id, status)`), the DB returns data directly from index memory without touching the main table (Covering Index Scan).

#### 179. Why do SQL functions on indexed columns disable index usage?
**Answer:**
Wrapping an indexed column inside a SQL function disables the index because the DB must compute the function for every single row, resulting in a Full Table Scan.
- ❌ `WHERE YEAR(created_at) = 2026` -> Index Bypassed!
- ✅ `WHERE created_at >= '2026-01-01' AND created_at < '2027-01-01'` -> Index Used!
- ❌ `WHERE LOWER(email) = 'user@test.com'` -> Index Bypassed!
- ✅ `WHERE email = 'user@test.com'` -> Index Used!

#### 180. How do implicit data type mismatches impact index performance?
**Answer:**
If an indexed column is compared against a value of a different data type requiring implicit conversion, the DB automatically converts the column value for every row, leading to a Full Table Scan.
- ❌ `WHERE user_id = 123` (without quotes when `user_id` is `VARCHAR`) -> Full Table Scan!
- ✅ `WHERE user_id = '123'` (with string quotes) -> Index Used!

#### 181. Why are low cardinality columns poor candidates for solo indexing?
**Answer:**
- **High Cardinality** (many unique values: `email`, `user_id`, `created_at`): Ideal for indexing.
- **Low Cardinality** (few unique values: `gender`, `is_active`, `status`): Unsuitable for solo indexing. If 90% of rows have `is_active = true`, the DB query optimizer calculates that scanning the table directly is cheaper than doing 900,000 double-lookups via a secondary index.

#### 182. What are the key best practice guidelines for database index design?
**Answer:**
- **Search by text prefix:** Use trailing wildcard `LIKE 'text%'`.
- **Multi-column queries:** Follow the ESR Rule (`Equality -> Sort -> Range`).
- **High-performance APIs:** Use Covering Indexes for frequent `SELECT` queries.
- **Avoid N+1 DB roundtrips:** Use Materialized Path or Eager Loading.




## 📂 Category: Subqueries & Aggregations (64 cards)

### 🟢 Junior Level

#### 1. Explain the COUNT aggregate function.
**Answer:**
COUNT() returns the number of rows that match a specified criterion. 'COUNT(*)' counts all rows including NULLs, while 'COUNT(column_name)' counts only rows where the specified column is not NULL.

#### 2. How do you count the number of entries in a table?
**Answer:**
Use the COUNT() function: SELECT COUNT(*) FROM table_name;

#### 3. Tell me the top downloaded app.
**Answer:**
SELECT MAX(downloads) FROM fake_apps;

#### 4. What are the common SQL aggregate functions?
**Answer:**
AVG: returns the average value of a column. COUNT: counts the number of rows. MAX: returns the highest value. MIN: returns the lowest value. SUM: returns the total sum of values.

#### 5. What is the SUM() function?
**Answer:**
SUM() is an aggregate function that returns the total sum of a numeric column. Syntax: SELECT SUM(column_name) FROM table_name WHERE condition;

#### 6. What is the syntax for the AVG() function?
**Answer:**
SELECT AVG(column_name) FROM table_name WHERE condition;


### 🟡 Mid Level

#### 1. Can 'ALL' and 'ANY' SQL operators be replaced?
**Answer:**
Yes, 'ALL' and 'ANY' operators can always be replaced by 'EXISTS' and 'NOT EXISTS' clauses.

#### 2. Explain the ANY and ALL operators.
**Answer:**
ANY returns true if any subquery values meet the condition. ALL returns true only if all subquery values meet the condition. They are used in conjunction with standard comparison operators.

#### 3. Explain the GROUP BY and HAVING clauses.
**Answer:**
GROUP BY is used to group result sets by one or more columns, typically in combination with aggregate functions. The HAVING clause is used to filter groups created by GROUP BY, as the standard WHERE clause cannot be used with aggregate functions.

#### 4. Explain the SQL COUNT(), AVG(), and SUM() functions.
**Answer:**
These are aggregate functions used for calculations on result sets: COUNT() returns the number of rows matching criteria; AVG() returns the average value of a numeric column; SUM() returns the total sum of values in a numeric column.

#### 5. Explain the difference between COUNT(*), COUNT(column_name), and COUNT(DISTINCT column_name).
**Answer:**
COUNT(*) counts all rows including those with NULLs. COUNT(column_name) counts all non-null values in that column. COUNT(DISTINCT column_name) counts only the unique, non-null values in that column.

#### 6. Funkce LAG(), LEAD() a LAST_VALUE()
**Answer:**
LAG() vrací hodnotu předcházejícího řádku; LEAD() vrací hodnotu následujícího řádku; LAST_VALUE() vrací poslední hodnotu v definovaném okně (group).

#### 7. How can you count rows meeting specific criteria?
**Answer:**
Use the COUNT aggregate function combined with a WHERE clause: e.g., SELECT COUNT(*) FROM table WHERE condition = value;

#### 8. How can you simulate a MAX() function using set operators?
**Answer:**
You can simulate the MAX() function by using the EXCEPT operator to remove all values that are not the maximum. Example: SELECT * FROM rel EXCEPT SELECT * FROM rel WHERE attr < (SELECT MAX(attr) FROM rel). Alternatively, selecting all tuples except those that are smaller than at least one other tuple will leave only the maximum.

#### 9. How do GROUP BY and HAVING clauses work in aggregation?
**Answer:**
GROUP BY aggregates rows that have the same values into summary rows. HAVING is used to filter the groups created by the GROUP BY clause based on a condition (unlike WHERE, which filters individual rows).

#### 10. How do aggregate functions handle NULL values?
**Answer:**
Aggregate functions ignore NULL values in their calculations, with the notable exception of COUNT(*), which counts rows regardless of nullability.

#### 11. How do you add up the number of items per category?
**Answer:**
SELECT category, SUM(column_name) FROM table_name GROUP BY category;

#### 12. How do you alias columns and count rows in SQL?
**Answer:**
Column aliases are created using the 'AS' keyword (e.g., 'SELECT City AS CityName'). The 'COUNT(*)' function returns the total number of rows that satisfy a filter condition. Unlike 'SELECT *', which returns all columns, aggregate functions reduce result sets to a single value.

#### 13. How do you calculate the sum of an integer column?
**Answer:**
Use the SUM() aggregate function: SELECT SUM(column_name) FROM table_name;

#### 14. How do you concatenate strings (like e-mails) grouped by a specific column (like Department)?
**Answer:**
Use the STRING_AGG function: SELECT Dep, STRING_AGG(email, '; ') WITHIN GROUP (ORDER BY email) AS DepEmails FROM Emails GROUP BY Dep. This function is available in modern SQL dialects like MS SQL Server 2017+.

#### 15. How do you count the number of items per category?
**Answer:**
Use the COUNT() aggregate function combined with a GROUP BY clause: SELECT price, COUNT(*) FROM fake_apps GROUP BY price;

#### 16. How do you perform basic aggregations on a table?
**Answer:**
Use aggregate functions: SUM(column) to add values, MAX(column) to find the largest value, and COUNT(*) to find the number of rows.

#### 17. How do you query an alphabetically ordered list of names with their profession first letter in parentheses, and a count of occurrences for each occupation in SQL?
**Answer:**
To get names: SELECT CONCAT(name, '(', LEFT(occupation, 1), ')') FROM OCCUPATIONS ORDER BY name ASC; To get counts: SELECT CONCAT('There are a total of ', COUNT(occupation), ' ', LOWER(occupation), 's.') FROM OCCUPATIONS GROUP BY occupation ORDER BY COUNT(occupation), occupation ASC;

#### 18. How do you remove duplicate values when performing an aggregation?
**Answer:**
The DISTINCT keyword is used inside aggregate functions (e.g., COUNT(DISTINCT column_name)) to consider only unique values.

#### 19. How do you retrieve the third-highest salary from an employee table?
**Answer:**
SELECT TOP 1 salary FROM (SELECT TOP 3 salary FROM employee_table ORDER BY salary DESC) AS emp ORDER BY salary ASC;

#### 20. How does ROLLUP aggregation work?
**Answer:**
ROLLUP creates subtotals and a grand total. The last attribute in the GROUP BY clause is the most granular level of aggregation, and the hierarchy moves toward higher-level totals as attributes are dropped from the right.

#### 21. In which clause can a subquery be used?
**Answer:**
A subquery can be used in many places, most commonly in the WHERE clause, but also in the SELECT, FROM, and HAVING clauses.

#### 22. Name the five aggregate functions.
**Answer:**
The standard aggregate functions are: COUNT(), SUM(), AVG(), MIN(), and MAX().

#### 23. Provide examples for aggregate functions COUNT(), AVG(), and SUM().
**Answer:**
SELECT COUNT(ProductID) FROM Products; SELECT AVG(Price) FROM Products; SELECT SUM(Quantity) FROM OrderDetails;

#### 24. SQL Aggregation Functions (MIN, MAX)
**Answer:**
MIN() returns the smallest value in a column, while MAX() returns the largest value. These functions are typically used in SELECT statements to perform calculations on datasets, often paired with GROUP BY.

#### 25. What SQL clause hosts set operators like IN, ANY/ALL, and (NOT) EXISTS?
**Answer:**
These operators are used within the WHERE clause to perform comparisons against sets of values or results of subqueries.

#### 26. What are ROLLUP and CUBE in T-SQL?
**Answer:**
ROLLUP and CUBE are grouping set extensions used with the GROUP BY clause to generate summarized aggregations, hierarchical totals, and multi-dimensional analysis for auditing and reports.

#### 27. What are the common complications and constraints associated with using aggregations in SQL?
**Answer:**
Aggregation can cause complications such as introducing ambiguity (e.g., in recursive CTEs) and making views non-updatable if they contain aggregate functions.

#### 28. What are the standard SQL aggregate functions?
**Answer:**
Aggregate functions perform operations over multiple values in rows. The standard functions are: COUNT (number of non-null values), MIN (minimum value), MAX (maximum value), SUM (sum of values), and AVG (average value).

#### 29. What is a Common Table Expression (CTE)?
**Answer:**
A temporary, named result set defined using the WITH clause. It exists only for the scope of the single statement it is attached to and is often used to simplify complex joins or recursive logic.

#### 30. What is a correlated subquery?
**Answer:**
A subquery that references columns from the outer query. It is evaluated once for each row processed by the outer query, often used with EXISTS or NOT EXISTS to check for relational conditions.

#### 31. What is a nested query (subquery) in SQL?
**Answer:**
A subquery is a query embedded within another query. The innermost query is evaluated first. It can be used in WHERE, FROM, or SELECT clauses. Example: SELECT CustomerNumber FROM Customer WHERE EXISTS (SELECT * FROM Purchase WHERE Customer.CustomerNumber = Purchase.CustomerNumber AND ArticleNumber = (SELECT ArticleNumber FROM Article WHERE Description = 'HIFI-Anlage'));

#### 32. What is a subquery in SQL?
**Answer:**
A subquery is an inner SELECT statement whose results are used by the outer query to help determine the final result set.

#### 33. What is a subquery, where can it be used, and what are its common use cases?
**Answer:**
A subquery is a query nested within another SQL statement. They can reside in the SELECT clause (often for correlated calculations), the FROM clause (as a derived table), or the WHERE clause (filtering). They are useful when you need to perform calculations with aggregates (like MAX, SUM) without applying them to the entire result set, or to filter data based on results from another table.

#### 34. What is a subquery?
**Answer:**
A subquery is a complete SELECT statement nested within another SQL query (such as SELECT, INSERT, UPDATE, or DELETE).

#### 35. What is an aggregate function?
**Answer:**
Aggregate functions perform calculations on multiple values to return a single result. Examples include COUNT(), SUM(), AVG(), MIN(), and MAX(). They are often used to group data.

#### 36. What is the STRING_AGG function?
**Answer:**
STRING_AGG is an aggregate function that concatenates string values from multiple rows into a single string, separated by a specified delimiter.

#### 37. What is the difference between WHERE and HAVING clauses?
**Answer:**
The WHERE clause filters individual rows before any grouping occurs. The HAVING clause is used to filter groups of rows after the GROUP BY operation has been performed.

#### 38. What is the difference between aggregate and scalar functions?
**Answer:**
Aggregate functions evaluate mathematical calculations across multiple rows to return a single result (e.g., MAX(), COUNT(), SUM()). Scalar functions return a single value for each single input value (e.g., UCASE(), NOW()).

#### 39. What is the function of the SUM aggregate function in SQL?
**Answer:**
The SUM() function returns the total sum of all numerical values for a given column or expression.

#### 40. What is the function of the WITH statement in SQL?
**Answer:**
The WITH statement (Common Table Expression or CTE) defines a temporary result set that can be referenced within a subsequent SELECT, INSERT, UPDATE, or DELETE statement. It is often used to simplify complex, nested queries or to perform recursive operations.

#### 41. What is the purpose of the EXISTS operator?
**Answer:**
The EXISTS operator tests for the presence of records in a subquery. It returns TRUE if the subquery returns one or more records, and is often used in filtering result sets based on the presence of related data in another table.

#### 42. What is the purpose of the FIRST_VALUE() window function?
**Answer:**
FIRST_VALUE(...) OVER (...) is a window function that returns the value of the first row within a defined group/partition.

#### 43. What is the scope of an aggregate function?
**Answer:**
Aggregate functions (like SUM, AVG, COUNT) operate on the values of a single column across multiple rows to produce a single scalar result.

#### 44. What must subqueries in a SELECT list return?
**Answer:**
Subqueries used as scalar expressions in a SELECT list must return only one single value (a scalar).

#### 45. What must the HAVING clause always include?
**Answer:**
The condition in a HAVING clause must always include one or more aggregate functions.

#### 46. Where can aggregate functions be used in an SQL query?
**Answer:**
Aggregate functions can be used in the SELECT list and the HAVING clause.

#### 47. Which aggregate functions ignore NULL values?
**Answer:**
SUM, AVG, MIN, and MAX ignore NULL values during calculation.

#### 48. Write a query to calculate the total score of hackers based on the maximum score of their submissions, excluding those with a total score of 0, ordered by score (desc) and hacker_id (asc).
**Answer:**
SELECT h.hacker_id, h.name, SUM(max_scores.Max_Score) FROM (SELECT hacker_id, challenge_id, MAX(score) AS Max_Score FROM Submissions GROUP BY hacker_id, challenge_id) max_scores INNER JOIN Hackers h ON max_scores.hacker_id = h.hacker_id GROUP BY h.hacker_id, h.name HAVING SUM(max_scores.Max_Score) > 0 ORDER BY 3 DESC, 1 ASC


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


## 📂 Category: Transactions & Concurrency (46 cards)

### 🟢 Junior Level

#### 1. TCL
**Answer:**
Transaction Control Language: A subset of SQL commands used to manage transactions in the database (e.g., COMMIT, ROLLBACK, SAVEPOINT).


### 🟡 Mid Level

#### 1. Define a database transaction.
**Answer:**
A transaction is a sequence of one or more SQL operations treated as an atomic unit. It follows ACID properties: changes appear to run in isolation, and if the system fails, all changes are rolled back or committed entirely.

#### 2. How do table variables behave within a transaction in SQL Server?
**Answer:**
They do not participate in or respect the transactional rollback mechanism.

#### 3. How do you make changes permanent in a database?
**Answer:**
The COMMIT statement is used to finalize and persist all changes made during the current transaction.

#### 4. What are the ACID properties of database transactions?
**Answer:**
ACID stands for Atomicity (all or nothing), Consistency (valid state transitions), Isolation (independent transactions), and Durability (persisted after commitment).

#### 5. What are the ACID properties of database transactions?
**Answer:**
Atomicity (all or nothing), Consistency (maintaining valid state), Isolation (transactions don't interfere), and Durability (permanent changes once committed).

#### 6. What commands represent TCL?
**Answer:**
Transaction Control Language (TCL) commands manage transactions within the database. Examples include COMMIT and ROLLBACK.

#### 7. What does a COMMIT statement do?
**Answer:**
It permanently saves the changes made during the current transaction to the database.

#### 8. What does the ACID acronym stand for in transaction management?
**Answer:**
ACID stands for Atomicity, Consistency, Isolation, and Durability; these are the standard properties that guarantee reliable database transactions.

#### 9. What does the acronym ACID stand for?
**Answer:**
Atomicity, Consistency, Isolation, Durability. These are the fundamental properties that ensure reliable database transactions.

#### 10. What is Durability in ACID?
**Answer:**
Durability guarantees that once a transaction has been committed, it will remain persisted in the database even in the event of a system crash, typically ensured by transaction logs.

#### 11. What is the default access mode for transactions if not specified?
**Answer:**
READ WRITE is the default access mode.

#### 12. What is the function of the READ ONLY transaction state?
**Answer:**
It is used to allow transactions on a temporary table or read-only access to data, ensuring no modifications occur during the transaction.

#### 13. What is the purpose of database transactions and how are they used?
**Answer:**
Transactions group SQL commands into a single atomic unit. They ensure data integrity by either committing all changes or rolling back if an error occurs. Key statements include BEGIN TRANSACTION, COMMIT TRANSACTION, and ROLLBACK TRANSACTION.

#### 14. What is the purpose of the LOCK_TIMEOUT variable?
**Answer:**
LOCK_TIMEOUT defines the period (in milliseconds) that a session will wait for a blocked resource before returning an error.

#### 15. What is the purpose of the SQL ROLLBACK statement?
**Answer:**
The ROLLBACK statement is used to abort a transaction and revert any uncommitted changes made to the database by that transaction.

#### 16. What two mechanisms define how transactions are handled in standard SQL?
**Answer:**
The two primary mechanisms are: 'COMMIT', which explicitly ends a transaction and triggers the start of a new one, and 'AUTOCOMMIT', where every individual SQL statement is treated as its own atomic transaction.

#### 17. Which SQL statement is used when we want to abort a transaction?
**Answer:**
The ROLLBACK statement.


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

