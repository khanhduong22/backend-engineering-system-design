# SQL & Database Study Guide - Mid Level

- **Total Cards**: 338

---

## 📂 Category: Advanced & Distributed Databases (16 cards)

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


## 📂 Category: Basic SQL & Syntax (44 cards)

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


## 📂 Category: Database Design & Normalization (94 cards)

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


## 📂 Category: Database Programmability (52 cards)

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


## 📂 Category: Joins & Set Operators (22 cards)

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


## 📂 Category: Performance & Indexing (45 cards)

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


## 📂 Category: Subqueries & Aggregations (48 cards)

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


## 📂 Category: Transactions & Concurrency (17 cards)

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

