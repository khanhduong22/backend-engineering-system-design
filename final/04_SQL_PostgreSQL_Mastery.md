# 04_SQL_PostgreSQL_Mastery - SQL & PostgreSQL Mastery Study Guide

- **Total Cards**: 1172

---

## 📂 Category: SQL & PostgreSQL (1172 cards)

### 🟡 Mid Level

#### 1. 1. Advanced SQL Tips
**Answer:**
To use a composite set of variables with the IN operator, concatenate them (e.g., WHERE (col1, col2) IN ((val1, val2), ...)).

#### 2. 10. Can column aliases or aggregate functions be used in WHERE or HAVING clauses?
**Answer:**
No. WHERE filters raw rows before aggregation, and HAVING filters grouped results. Because of the query execution order, aliases defined in the SELECT clause are not yet available in the WHERE/HAVING stages. Use the original column or expression.

#### 3. 100. Find the sum of all amounts in the payment table.
**Answer:**
SELECT SUM(amount) FROM payment;





### 🟡 Mid Level

#### 4. 1000. What is the purpose of the CREATE INDEX statement and how do you create a unique index?
**Answer:**
CREATE INDEX creates an index on specified table columns to improve query performance (e.g., 'CREATE INDEX idx_lastname ON Persons (LastName);'). A unique index, created with 'CREATE UNIQUE INDEX', prevents duplicate values in the indexed columns. Syntax varies by database system.

#### 5. 1001. What is the purpose of the DBCC TRACEON command?
**Answer:**
DBCC TRACEON is a command used to enable specific trace flags within a database session to help diagnose performance issues or track internal server activity.

#### 6. 1002. What is the purpose of the DEFAULT constraint?
**Answer:**
The DEFAULT constraint provides a default value for a column automatically if no specific value is provided during an INSERT operation.

#### 7. 1003. What is the purpose of the DISTINCT keyword?
**Answer:**
The DISTINCT keyword is used in a SELECT statement to return only unique values, effectively eliminating duplicate rows from the result set.

#### 8. 1004. What is the purpose of the EXISTS operator?
**Answer:**
The EXISTS operator tests for the presence of records in a subquery. It returns TRUE if the subquery returns one or more records, and is often used in filtering result sets based on the presence of related data in another table.

#### 9. 1005. What is the purpose of the FIRST_VALUE() window function?
**Answer:**
FIRST_VALUE(...) OVER (...) is a window function that returns the value of the first row within a defined group/partition.

#### 10. 1006. What is the purpose of the FROM and JOIN clauses?
**Answer:**
The FROM and JOIN clauses specify the table or tables from which to retrieve data.

#### 11. 1007. What is the purpose of the GO command?
**Answer:**
GO is a batch separator used in SQL Server to signal the end of a batch of SQL statements. It instructs the client tool to send the preceding statements to the server for execution before continuing with the code that follows.

#### 12. 1008. What is the purpose of the INSERT statement in SQL?
**Answer:**
The INSERT statement is used to add a single row of data into a named table, or to insert an arbitrary number of rows from one or more tables using a subquery (sub-select).

#### 13. 1009. What is the purpose of the Init() method in SQL execution operators?
**Answer:**
It serves as the operator's initialization phase, preparing the necessary resources for execution.

#### 14. 101. Find the three lowest rated movies from the movies table.
**Answer:**
SELECT * FROM movies ORDER BY rating ASC LIMIT 3;

#### 15. 1010. What is the purpose of the JOIN operation in SQL?
**Answer:**
JOIN is used to combine columns from multiple tables into a single result set based on a related column between them.

#### 16. 1011. What is the purpose of the LOCK_TIMEOUT variable?
**Answer:**
LOCK_TIMEOUT defines the period (in milliseconds) that a session will wait for a blocked resource before returning an error.

#### 17. 1012. What is the purpose of the Lookup Transformation?
**Answer:**
The Lookup Transformation is used to retrieve data from a reference table based on a match from an input stream. It is commonly used for dimension attribute retrieval in Data Warehousing, identifying existing records for SCD (Slowly Changing Dimension) updates, or validating data integrity.

#### 18. 1013. What is the purpose of the MAX_GRANT_PERCENT query hint?
**Answer:**
MAX_GRANT_PERCENT is a query hint that sets the maximum allowable memory grant (as a percentage of total buffer pool memory) for a specific query execution.

#### 19. 1014. What is the purpose of the MERGE statement?
**Answer:**
The MERGE statement performs conditional DML operations. It checks if a source row exists in the target table; if it exists, it performs an UPDATE, otherwise, it performs an INSERT.

#### 20. 1015. What is the purpose of the SELECT statement?
**Answer:**
The SELECT statement is used to retrieve and display data from one or more database tables.

#### 21. 1016. What is the purpose of the SELECT statement?
**Answer:**
The SELECT statement is used to retrieve data from a database. Its components include SELECT (columns), FROM (tables), WHERE (filtering), GROUP BY (aggregation), HAVING (filter for groups), and ORDER BY (sorting).

#### 22. 1017. What is the purpose of the SQL ROLLBACK statement?
**Answer:**
The ROLLBACK statement is used to abort a transaction and revert any uncommitted changes made to the database by that transaction.

#### 23. 1018. What is the purpose of the TRIGGER_NESTLEVEL function?
**Answer:**
It is a function that returns the nesting level of a trigger execution. It accepts parameters: object_id (specific trigger to track), trigger_type (AFTER or INSTEAD OF), and trigger_event_category (DDL or DML).

#### 24. 1019. What is the purpose of the UNIQUE constraint?
**Answer:**
The UNIQUE constraint ensures that all values in a column or set of columns are distinct, preventing duplicate entries in those fields.

#### 25. 102. Find websites in the approved_websites table that match the pattern: starts with ftp:// or http://, ends in .org, and has at least one character before the :// and one character after.
**Answer:**
SELECT * FROM approved_websites WHERE url_name LIKE '_%://_%.org';

#### 26. 1020. What is the purpose of the WHERE clause?
**Answer:**
It is used to filter records that fulfill a specified criterion.

#### 27. 1021. What is the purpose of the WITH GRANT option?
**Answer:**
The WITH GRANT option allows a user who has been granted specific SQL privileges to pass those privileges on to other users.

#### 28. 1022. What is the purpose of the model database in SQL Server?
**Answer:**
The model database acts as a template for all new databases created on the instance. Changes made to model are propagated to new databases. It is also the source used to recreate tempdb during server startup.

#### 29. 1023. What is the purpose of trace flag 8780 in SQL Server?
**Answer:**
Trace flag 8780 is used to generate XML for use in a USE PLAN hint, often for the purpose of comparing query plans or forcing a specific execution plan.

#### 30. 1024. What is the purpose of using brackets [ ] in database identifiers?
**Answer:**
Brackets are used to delimit identifiers, allowing the use of reserved keywords or special characters in column or table names. It is generally recommended to avoid such naming conventions, but brackets (or double quotes in standard PostgreSQL) are required to reference these objects.

#### 31. 1025. What is the recommended naming convention for database tables and views?
**Answer:**
Use singular nouns rather than plural (e.g., 'movie' instead of 'movies').

#### 32. 1026. What is the relational algebra select operator and what does it do?
**Answer:**
The select operator picks certain rows from a relation based on a condition. It is functionally similar to the WHERE clause in SQL.

#### 33. 1027. What is the relationship between Functional Dependency (FD) and Multivalued Dependency (MVD)?
**Answer:**
A Functional Dependency is always a Multivalued Dependency (but the inverse is not necessarily true). This is known as the FD-is-an-MVD rule.

#### 34. 1028. What is the relationship between a trigger and a procedure or function?
**Answer:**
A procedure or function can be activated by a trigger. A procedure/function represents a single call or execution unit initiated by the trigger event.

#### 35. 1029. What is the relationship between multi-valued dependencies and fourth normal form (4NF)?
**Answer:**
Multi-valued dependencies are often called tuple-generating dependencies. 4NF is stricter than BCNF, specifically addressing issues with multi-valued dependencies.

#### 36. 103. For a fact table with attributes D1, D2, and D3, what are the row count formulas for GROUP BY, CUBE, and ROLLUP?
**Answer:**
Q1 (GROUP BY): n1*n2*n3. Q2 (WITH CUBE): (n1+1)*(n2+1)*(n3+1). Q3 (WITH ROLLUP): (n1*n2*n3) + (n1*n2) + n1 + 1.

#### 37. 1030. What is the relative power of XQuery compared to XPath and XSLT?
**Answer:**
XQuery offers the most expressive power because it is a full-featured, compositional query language.

#### 38. 1031. What is the requirement for a foreign key in most current DBMS?
**Answer:**
Most modern DBMS require that a foreign key must reference a primary key or a unique constraint in the parent table, even if the SQL standard might allow references to non-unique columns.

#### 39. 1032. What is the requirement for a table to be in BCNF (Boyce-Codd Normal Form)?
**Answer:**
For every non-trivial functional dependency A->B, A must be a superkey.

#### 40. 1033. What is the result of an INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL OUTER JOIN?
**Answer:**
INNER JOIN: Returns rows with matches in both tables. LEFT JOIN: Returns all rows from the left, plus matches from the right. RIGHT JOIN: Returns all rows from the right, plus matches from the left. FULL OUTER JOIN: Returns all rows from both tables, filling with NULL where matches don't exist.

#### 41. 1034. What is the role of Consistency in database transactions?
**Answer:**
Consistency ensures that all constraints and rules are satisfied before and after a transaction, maintaining valid data states throughout.

#### 42. 1035. What is the role of the Algebraizer in the SQL Server relational engine?
**Answer:**
The Algebraizer is the component that resolves names (like table and column names) into internal object IDs and creates the initial query tree structure.

#### 43. 1036. What is the role of the row offsets table?
**Answer:**
The row offsets table is a part of the data page that stores the starting byte addresses (offsets) of the rows stored on that page.

#### 44. 1037. What is the rule for translating UML classes to relational schemas regarding primary keys?
**Answer:**
Every 'regular' class must have at least one primary key defined so that associations can be properly translated. Subclasses, association classes, and aggregated/composed classes may follow different rules based on their relationship type.

#### 45. 1038. What is the scope of an aggregate function?
**Answer:**
Aggregate functions (like SUM, AVG, COUNT) operate on the values of a single column across multiple rows to produce a single scalar result.

#### 46. 1039. What is the size of a database page header?
**Answer:**
The standard size of a database page header in many systems like SQL Server is 96 bytes.

#### 47. 104. Functional dependencies are a generalization of what concept?
**Answer:**
Functional dependencies are a generalization of the notion of keys.

#### 48. 1040. What is the size of a row header?
**Answer:**
The row header is 4 bytes in size.

#### 49. 1041. What is the smallest interval recordable by a datetime data type?
**Answer:**
The smallest interval is typically 3.33 milliseconds (based on the internal storage resolution of the datetime type).

#### 50. 1042. What is the splitting rule for functional dependencies?
**Answer:**
The decomposition rule states: if A -> B1, B2, ..., Bn, then it is equivalent to A -> B1 and A -> B2 and ... and A -> Bn.

#### 51. 1043. What is the standard data page size in SQL Server?
**Answer:**
The standard page size is 8 kB.

#### 52. 1044. What is the standard order of clauses in a SELECT statement?
**Answer:**
The SELECT statement consists of the following clauses: SELECT, DISTINCT, FROM & JOIN, WHERE, GROUP BY, HAVING, ORDER BY, and LIMIT.

#### 53. 1045. What is the standard order of clauses in a comprehensive SELECT statement?
**Answer:**
The standard sequence is: SELECT, DISTINCT, FROM & JOIN, WHERE, GROUP BY, HAVING, ORDER BY, and LIMIT.

#### 54. 1046. What is the subtree cost of an operator in an execution plan?
**Answer:**
The subtree cost represents the total estimated cost of an operator plus the accumulated cost of all its child nodes in the execution plan tree.

#### 55. 1047. What is the syntax and purpose of a window function?
**Answer:**
A window function performs calculations across a set of table rows that are related to the current row. Syntactically, it requires an OVER clause. Example: SELECT depname, salary, avg(salary) OVER (PARTITION BY depname) FROM empsalary; The OVER clause determines the window, while PARTITION BY divides rows into groups.





## 📂 Category: Transactions & Concurrency (3 cards)



### 🔴 Senior Level

#### 56. 1048. What is the syntax for the AVG() function?
**Answer:**
SELECT AVG(column_name) FROM table_name WHERE condition;





## 📂 Category: Transactions & Concurrency (1 cards)



### 🟢 Junior Level

#### 57. 1049. What is the syntax for the HAVING clause?
**Answer:**
The HAVING clause is used to filter group rows after aggregations are computed. Example: SELECT year, COUNT(*) FROM movies GROUP BY year HAVING COUNT(*) > 5;

#### 58. 105. Funkce LAG(), LEAD() a LAST_VALUE()
**Answer:**
LAG() vrací hodnotu předcházejícího řádku; LEAD() vrací hodnotu následujícího řádku; LAST_VALUE() vrací poslední hodnotu v definovaném okně (group).

#### 59. 1050. What is the syntax for the LIKE operator?
**Answer:**
The LIKE operator is used for pattern matching. Example: SELECT name FROM movies WHERE name LIKE 'Star%';

#### 60. 1051. What is the syntax for the LIMIT clause?
**Answer:**
The LIMIT clause restricts the number of rows returned by a query. Example: SELECT * FROM movies LIMIT 5;

#### 61. 1052. What is the syntax for the ORDER BY clause?
**Answer:**
The ORDER BY clause sorts the result set. Example: SELECT * FROM table1 ORDER BY column1 DESC;

#### 62. 1053. What is the syntax for the SQL INSERT command?
**Answer:**
INSERT INTO table_name (column1, column2) VALUES (value1, value2); It allows the insertion of one or more rows into a table.

#### 63. 1054. What is the syntax for the UNION clause?
**Answer:**
The UNION operator is used to combine the result sets of two or more SELECT statements. Example: SELECT name FROM first_names UNION SELECT name FROM last_names;





## 📂 Category: Subqueries & Aggregations (24 cards)



### 🟢 Junior Level

#### 64. 1055. What is the syntax for writing comments in SQL?
**Answer:**
Use double dashes for single-line comments: -- This is a comment.

#### 65. 1056. What is the syntax to create a join table?
**Answer:**
A join table facilitates many-to-many relationships by storing foreign keys. Example: CREATE TABLE cats_owners (cat_id INTEGER, owner_id INTEGER);





### 🔴 Senior Level

#### 66. 1057. What is the syntax to manipulate records (INSERT, UPDATE, DELETE)?
**Answer:**
INSERT: INSERT INTO table (col) VALUES (val); UPDATE: UPDATE table SET col = val WHERE condition; DELETE: DELETE FROM table WHERE condition;

#### 67. 1058. What is the syntax to modify database structures (CREATE, ALTER, DROP)?
**Answer:**
To create: CREATE TABLE table_name (id INTEGER PRIMARY KEY, name TEXT); To add a column: ALTER TABLE table_name ADD column_name TEXT; To delete: DROP TABLE table_name;

#### 68. 1059. What is the syntax to reference columns from different tables when names overlap?
**Answer:**
Use table qualification syntax: table_name.column_name. Example: SELECT cats.name, dogs.name FROM cats, dogs;

#### 69. 106. Generally, when a view includes aggregation (such as avg), does it make sense to allow modifications over this view?
**Answer:**
Generally, when a view includes aggregation (such as avg), it usually does not make sense to allow modifications (INSERT, UPDATE, DELETE) over this view because the underlying result set is not mapped 1:1 to the base table rows.

#### 70. 1060. What is the theta-join operator in relational algebra?
**Answer:**
A theta-join performs a join of two relations based on specific conditions. It is a shortcut for a cross product followed by a select, similar to a SQL JOIN with an ON condition.

#### 71. 1061. What is the trade-off when using weaker transaction isolation levels?
**Answer:**
Weaker isolation levels (e.g., Read Uncommitted, Read Committed, Repeatable Read) reduce overhead and increase concurrency, but at the cost of reduced consistency and lower data guarantees.

#### 72. 1062. What is the transitive property in functional dependencies (A ->> B, B ->> C implies A ->> C)?
**Answer:**
If attribute A determines B, and B determines C, then A also determines C (transitive dependency).

#### 73. 1063. What is the usage of the DISTINCT keyword?
**Answer:**
The DISTINCT keyword is used in a SELECT statement to return only unique (non-duplicate) values from the specified columns.

#### 74. 1064. What is the usage of the SIGN function?
**Answer:**
The SIGN function determines if a numeric value is positive, negative, or zero. It returns +1 for positive numbers, -1 for negative, and 0 for zero.

#### 75. 1065. What is three-valued logic in SQL?
**Answer:**
SQL uses three-valued logic to handle NULL values, which can result in TRUE, FALSE, or UNKNOWN (NULL) outcomes when evaluating predicates.

#### 76. 1066. What is vertical partitioning?
**Answer:**
Vertical partitioning is the process of splitting a table by moving some columns into a separate table to improve performance or security.

#### 77. 1067. What is vertical scalability?
**Answer:**
Vertical scalability (scaling up) involves increasing the capacity of a single server by adding resources like CPU, RAM, or faster storage (SSD).





## 📂 Category: Basic SQL & Syntax (49 cards)



### 🟢 Junior Level

#### 78. 1068. What issue can occur when comparing char and nchar columns with SQL_* collations?
**Answer:**
Collation mismatches or data type precedence issues (like Unicode vs non-Unicode) can prevent efficient index usage, often leading to full table scans or conversion errors.

#### 79. 1069. What items are contained within an SQL package, and what are its two main parts?
**Answer:**
An SQL package consists of procedures, functions, variables, and SQL statements. It is divided into two parts: the 'specification' (which declares public constructs) and the 'body' (which defines the implementation of all public and private constructs).

#### 80. 107. Granting and Revoking Privileges
**Answer:**
GRANT [privileges] ON [relation] TO [user] [WITH GRANT OPTION] grants specific permissions (select, update, delete). REVOKE [privileges] ON [relation] FROM [user] [CASCADE] removes those permissions. The 'CASCADE' option ensures that dependent privileges granted by the user are also revoked.

#### 81. 1070. What latching issue is associated with identity primary keys?
**Answer:**
Identity primary keys often cause 'last-page' contention, where multiple concurrent inserts attempt to write to the same last page of the B-tree index, creating latch contention on the data page.

#### 82. 1071. What limitations exist for creating an updateable view?
**Answer:**
To be updateable, views should generally avoid complex operations like aggregate functions, DISTINCT, GROUP BY, HAVING, or subqueries, as the database engine cannot reliably map changes back to the underlying base table rows.

#### 83. 1072. What methods can be used to update a table via SSIS?
**Answer:**
Common methods include using a SQL command, a staging table, a cache, the Script Task, or using the fully qualified database name.

#### 84. 1073. What must subqueries in a SELECT list return?
**Answer:**
Subqueries used as scalar expressions in a SELECT list must return only one single value (a scalar).

#### 85. 1074. What must the HAVING clause always include?
**Answer:**
The condition in a HAVING clause must always include one or more aggregate functions.

#### 86. 1075. What occurs during the Init() and GetNext() phases of a Hash Match operator?
**Answer:**
Init() builds a hash table from the 'build' input. GetNext() calls the probe operator and searches for matches within that built hash table.

#### 87. 1076. What parameters can SELECT TOP use to limit records?
**Answer:**
SELECT TOP can limit records by a specific absolute number or by a percentage of the total result set.

#### 88. 1077. What quantification does XPath use by default for attribute comparisons?
**Answer:**
XPath relies on implicit existential quantification ('there exists') when comparing attributes (e.g., [attribute = value]).

#### 89. 1078. What questions should you ask during a BI Stakeholder Analysis and Business Context review?
**Answer:**
Key questions include: Who are the user groups? How do they interact with data? Do they need self-service analysis or static reports? What business processes are critical to measure? Where does the source data originate? What are the data relationships and dependencies?

#### 90. 1079. What requirement must be met before adding a Primary Key to an existing table using ALTER TABLE?
**Answer:**
The target column(s) must have already been defined as NOT NULL.

#### 91. 108. How are A->>B and A->B read in database theory?
**Answer:**
A->B is read as 'A determines B'. A->>B is read as 'A multi-determines B'.

#### 92. 1080. What set operators are used to process logical 'only', 'and', and 'or' relationships across result sets?
**Answer:**
EXCEPT (\diff) is used for 'only' or exclusion, INTERSECT for 'and' (intersection), and UNION for 'or' (merging ensembles).

#### 93. 1081. What statement is used to fetch data from a database?
**Answer:**
The SELECT statement is used. Example: 'SELECT * FROM table_name' (where * is a wildcard for all columns) or 'SELECT col1, col2 FROM table_name'.

#### 94. 1082. What two mechanisms define how transactions are handled in standard SQL?
**Answer:**
The two primary mechanisms are: 'COMMIT', which explicitly ends a transaction and triggers the start of a new one, and 'AUTOCOMMIT', where every individual SQL statement is treated as its own atomic transaction.

#### 95. 1083. What types of indexes are available in SQL Server?
**Answer:**
Clustered: Stores data rows in order based on the index key. Nonclustered: Contains the key value and a row locator pointing to the data. Unique: Ensures no duplicate values in the index key. Full-text: Used for searching character-based data.

#### 96. 1084. What types of triggers exist in SQL Server?
**Answer:**
There are AFTER triggers (which fire after the DML operation) and INSTEAD OF triggers (which fire before or in place of the DML operation).

#### 97. 1085. What values does the Boolean data type contain?
**Answer:**
Boolean data contains the truth values TRUE and FALSE.

#### 98. 1086. What were the main types of NoSQL systems as of November 2011?
**Answer:**
Key types included: MapReduce frameworks (OLAP), Key-value stores (OLTP), Document stores, Graph databases, and Column stores.

#### 99. 1087. When and why should you use a database cursor?
**Answer:**
Cursors are used when you need to process data row-by-row to perform complex logic (like conditional updates or inserts) that cannot be easily achieved with set-based SQL queries. They function similarly to for/while loops.

#### 100. 1088. When are association classes considered unnecessary?
**Answer:**
Association classes are unnecessary if the multiplicity on both sides is 0..1 or 1..1, as the association can be folded into one of the participating classes.

#### 101. 1089. When are quotes required for values in SQL queries?
**Answer:**
Numeric fields generally do not require quotes around values, while text fields generally require single quotes.

#### 102. 109. How are Extended Events results stored?
**Answer:**
Extended Events results can be configured to be stored in various targets, including live logging buffers, files on disk, or SQL tables.

#### 103. 1090. When are two sets of functional dependencies (S1 and S2) considered equivalent?
**Answer:**
S2 is equivalent to S1 if exactly the same functional dependencies can be derived from both sets (i.e., their closures are equal).

#### 104. 1091. When defining a character string column, what does the specified length indicate?
**Answer:**
The specified length indicates the maximum number of characters that the column can hold.

#### 105. 1092. When designing an application, how do you decide between a NoSQL system and a relational DBMS regarding data consistency and scalability?
**Answer:**
Choose a traditional relational DBMS when strict data consistency and transaction serializability are required. Choose a NoSQL system when massive scalability and efficiency are prioritized over strict consistency, acknowledging that relational databases are also highly scalable but offer stronger guarantees.

#### 106. 1093. When does SQL Server use 'density' in query optimization?
**Answer:**
SQL Server uses density statistics when an equality predicate is used in the WHERE clause with a variable, or when the 'OPTIMIZE FOR UNKNOWN' hint is provided, as it estimates selectivity based on the average distribution of data.

#### 107. 1094. When does a comparison result in an 'UNKNOWN' truth value?
**Answer:**
An UNKNOWN result occurs when comparing against a NULL value, as NULL represents missing or inapplicable data.

#### 108. 1095. When does a deadlock occur in SQL Server?
**Answer:**
A deadlock occurs when two or more processes hold locks on resources the other process requires, creating a circular dependency where no process can proceed. The SQL Server engine typically detects this and terminates one of the processes as a deadlock victim.

#### 109. 1096. When does a set of functional dependencies S2 follow from S1?
**Answer:**
S2 follows from S1 if every relation instance that satisfies all dependencies in S1 also satisfies all dependencies in S2.

#### 110. 1097. When is an execution plan built in relation to variable substitution?
**Answer:**
The execution plan is compiled and built before the local variables are substituted with actual values. This is why parameter sniffing can occur, as the plan is optimized based on the structure rather than the specific data distribution of the parameters at the time of initial compilation.

#### 111. 1098. When is it appropriate to use a Cursor?
**Answer:**
Cursors are generally inefficient but may be necessary for procedural logic within triggers or stored procedures when you need to iterate through a specific set of rows (e.g., processing individual rows in the 'INSERTED' table during a trigger).

#### 112. 1099. When is the exact numeric data type used?
**Answer:**
It is used when you need to store numbers with absolute precision, such as financial or inventory data where rounding errors are unacceptable.

#### 113. 11. Can subqueries be used in constraints?
**Answer:**
Subqueries are generally not allowed in check constraints because they can lead to non-deterministic behavior. They are however widely used within triggers and other procedural code.

#### 114. 110. How are GRANT and REVOKE used in SQL?
**Answer:**
GRANT is issued by an owner or admin to pass specific privileges to another user. REVOKE is issued to remove those previously granted privileges.

#### 115. 1100. When is using a table alias useful?
**Answer:**
Aliases are useful when: joining multiple tables (to differentiate columns), using aggregate functions, shortening long or complex column names, or combining multiple columns into one output.

#### 116. 1101. When should you use a view instead of a base table?
**Answer:**
A view is useful when you need a calculation or a specific projection of data performed every time a record is accessed without duplicating data, or to simplify complex queries for the end-user.

#### 117. 1102. When should you use date/time data types?
**Answer:**
Use date/time data types when you need to define a specific point in time with a required degree of accuracy.

#### 118. 1103. Where can aggregate functions be used in an SQL query?
**Answer:**
Aggregate functions can be used in the SELECT list and the HAVING clause.

#### 119. 1104. Where can information about SQL Server wait types be found?
**Answer:**
Wait types are documented in the system view sys.dm_os_wait_stats.

#### 120. 1105. Where can one check if a scalar function is inlineable in SQL Server?
**Answer:**
In the sys.sql_modules system catalog view.

#### 121. 1106. Which Normal Form requires that all non-key fields are dependent only on the candidate key?
**Answer:**
BCNF (Boyce-Codd Normal Form) requires that for every functional dependency X -> Y, X must be a superkey.

#### 122. 1107. Which Normal Form validates functional and multivalued dependencies?
**Answer:**
Fourth Normal Form (4NF).

#### 123. 1108. Which Normal Form validates functional dependencies between key attributes?
**Answer:**
Boyce-Codd Normal Form (BCNF).

#### 124. 1109. Which SQL clause is used to limit the number of records returned by a query?
**Answer:**
The SELECT TOP clause (or LIMIT/FETCH FIRST depending on the SQL dialect).

#### 125. 111. How are Integrity Constraints classified in SQL?
**Answer:**
They are classified into: 1. Not Null constraints; 2. Key constraints (PRIMARY KEY, UNIQUE); 3. Referential integrity (FOREIGN KEY); 4. Attribute-based CHECK constraints; 5. Tuple-based CHECK constraints; 6. General assertions.

#### 126. 1110. Which SQL clause uses the logical operators AND, OR, and NOT, and in what order are they evaluated?
**Answer:**
These operators are used in the WHERE clause. The evaluation order is NOT, followed by AND, followed by OR.

#### 127. 1111. Which SQL clauses are disallowed in updateable views?
**Answer:**
The clauses DISTINCT, GROUP BY, HAVING, and UNION are generally not allowed in updateable views.

#### 128. 1112. Which SQL privileges can be granted to other users?
**Answer:**
Privileges such as USAGE, SELECT, DELETE, INSERT, UPDATE, and REFERENCES can be granted to other users if the grantor has the appropriate permissions.

#### 129. 1113. Which SQL statement is used to remove one or more rows from a named table?
**Answer:**
The DELETE statement.

#### 130. 1114. Which SQL statement is used when we want to abort a transaction?
**Answer:**
The ROLLBACK statement.

#### 131. 1115. Which actions prevent the caching of temporary objects in SQL Server?
**Answer:**
Actions such as creating an index, running ALTER TABLE, or defining a named constraint prevent caching.

#### 132. 1116. Which aggregate functions ignore NULL values?
**Answer:**
SUM, AVG, MIN, and MAX ignore NULL values during calculation.

#### 133. 1117. Which anomalies can persist in 2NF?
**Answer:**
Delete anomalies can still occur in 2NF, although Insert and Update anomalies are typically resolved.

#### 134. 1118. Which data type handles non-exact numbers?
**Answer:**
Approximate numeric data types (such as FLOAT or REAL).

#### 135. 1119. Which data type is used for bit strings?
**Answer:**
The BIT or BIT VARYING data type.

#### 136. 112. How are NoSQL databases structured compared to relational databases?
**Answer:**
NoSQL databases are typically non-relational and structured as document-based, key-value pairs, graph databases, or wide-column stores.

#### 137. 1120. Which data type is used for exact numeric representation?
**Answer:**
Exact numeric data types (such as DECIMAL or NUMERIC in many SQL dialects) are used when precision and scale must be guaranteed.

#### 138. 1121. Which data type should be used for monetary values like '1001.99'?
**Answer:**
The 'decimal(p,s)' or 'numeric(p,s)' data type (e.g., decimal(18,2)) should be used to ensure precision and prevent rounding errors associated with floating-point types.

#### 139. 1122. Which data types can be evaluated by the BETWEEN clause?
**Answer:**
The BETWEEN clause can be used with numbers, text (lexicographical order), and dates.

#### 140. 1123. Which isolation level allows for 'dirty reads'?
**Answer:**
The Read Uncommitted isolation level allows transactions to perform dirty reads.

#### 141. 1124. Which privileges can be restricted to specific columns?
**Answer:**
INSERT, UPDATE, and REFERENCES can be restricted to specific columns rather than the entire table.

#### 142. 1125. Which symbol is used to denote parameters in SQL statements?
**Answer:**
The '@' symbol is commonly used to denote parameters.

#### 143. 1126. Which temporal data type should you use to store '2002-01-25 22:10:15.3239999'?
**Answer:**
This value requires 'datetime2', as standard 'datetime' does not support that level of fractional second precision.

#### 144. 1127. Which two keywords are used to define key constraints in SQL?
**Answer:**
The two primary keywords for defining key constraints are 'PRIMARY KEY' (enforcing uniqueness and non-nullability, limited to one per table) and 'UNIQUE' (ensuring all values in a column are distinct, allowing multiple per table).

#### 145. 1128. Who invented RDBMS and when?
**Answer:**
The Relational Database Management System model was proposed in 1970 by Dr. Edgar Frank 'Tedd' Codd while working at IBM.

#### 146. 1129. Who is credited with the invention of SQL?
**Answer:**
Edgar F. Codd (the relational model) and later refinement by Donald Chamberlin and Raymond Boyce.

#### 147. 113. How are PFS pages allocated in SQL Server?
**Answer:**
Every 8,088th page is a Page Free Space (PFS) page.

#### 148. 1130. Who is responsible for assigning authorization identifiers?
**Answer:**
The Database Administrator (DBA).

#### 149. 1131. Why are data types important in database design?
**Answer:**
1. Ensures data consistency (prevents mixing types). 2. Enables appropriate calculations and functions (e.g., math or date functions). 3. Allows for storage and performance optimization. 4. Ensures correct sorting/ordering behavior.





## 📂 Category: Database Programmability (7 cards)



### 🟢 Junior Level

#### 150. 1132. Why are low cardinality columns poor candidates for solo indexing?
**Answer:**
- **High Cardinality** (many unique values: `email`, `user_id`, `created_at`): Ideal for indexing.



- **Low Cardinality** (few unique values: `gender`, `is_active`, `status`): Unsuitable for solo indexing. If 90% of rows have `is_active = true`, the DB query optimizer calculates that scanning the table directly is cheaper than doing 900,000 double-lookups via a secondary index.

#### 151. 1133. Why are materialized views often used in OLAP?
**Answer:**
Materialized views are used in OLAP to store precomputed query results. This improves performance for complex analytical queries by avoiding re-aggregation, similar to how OLAP cubes function, as both scenarios feature infrequent data updates and high read volume.

#### 152. 1134. Why are square brackets [ ] used with database objects?
**Answer:**
Brackets are used to delimit identifiers, which is necessary when an object name contains spaces, reserved SQL keywords, or special characters.

#### 153. 1135. Why can only relations with a composite candidate key violate 2NF?
**Answer:**
2NF requires that all non-key attributes be fully dependent on the *entire* primary key. If a table has a single-attribute primary key, there cannot be a partial dependency, as there are no 'parts' of the key to be partially dependent on. Partial dependencies can only exist when the primary key is composed of multiple columns.





## 📂 Category: Database Programmability (72 cards)



### 🔴 Senior Level

#### 154. 1136. Why do SQL functions on indexed columns disable index usage?
**Answer:**
Wrapping an indexed column inside a SQL function disables the index because the DB must compute the function for every single row, resulting in a Full Table Scan.



- ❌ `WHERE YEAR(created_at) = 2026` -> Index Bypassed!



- ✅ `WHERE created_at >= '2026-01-01' AND created_at < '2027-01-01'` -> Index Used!



- ❌ `WHERE LOWER(email) = 'user@test.com'` -> Index Bypassed!



- ✅ `WHERE email = 'user@test.com'` -> Index Used!

#### 155. 1137. Why do we need joins, and what is the syntax for a basic INNER JOIN?
**Answer:**
Joins are used to combine rows from two or more tables based on a related column between them. Syntax: SELECT columns FROM table1 INNER JOIN table2 ON table1.column = table2.column.





## 📂 Category: Performance & Indexing (3 cards)



### 🟢 Junior Level

#### 156. 1138. Why do we use integrity constraints?
**Answer:**
Integrity constraints are used to: 1) Prevent data-entry errors, 2) Enforce correctness criteria during updates, 3) Maintain data consistency, and 4) Inform the DBMS about the data's structure and rules.

#### 157. 1139. Why does comparing dates with time components in SQL often fail?
**Answer:**
If a date column contains a time component (e.g., '2008-11-11 13:23:44'), a strict equality comparison against just the date ('2008-11-11') will fail because the database treats the time as part of the value. Always account for the time component or cast the value to a date type for accurate comparisons.

#### 158. 114. How are SQL comments implemented?
**Answer:**
Single-line comments are designated by '--'. Anything following these characters on the same line is ignored by the database engine.

#### 159. 1140. Why does the statement 'CREATE TABLE Person (PersonName nvarchar());' fail and how can it be fixed?
**Answer:**
The statement fails because the length for the nvarchar data type is missing. It should specify a length (e.g., nvarchar(100)) or use 'nvarchar(max)' to store strings of variable length.

#### 160. 1141. Why is a relation not in 2NF if a non-key attribute depends on only a subset of the candidate key?
**Answer:**
It fails 2NF because 2NF requires full functional dependency on the entire primary key. If an attribute depends only on part of the key (a proper subset), it is a partial dependency, which is prohibited in 2NF.

#### 161. 1142. Why is a table with a single-attribute primary key automatically in 2NF if it is in 1NF?
**Answer:**
Second Normal Form (2NF) requires the absence of partial dependencies. A partial dependency occurs only when a non-key attribute depends on part of a composite primary key. With a single-attribute PK, partial dependency is impossible.

#### 162. 1143. Why is it often preferable to use constraints instead of triggers?
**Answer:**
Constraints are more optimized by the database engine and avoid complex issues like chaining, termination problems, and non-deterministic execution order that can occur with triggers.





## 📂 Category: Joins & Set Operators (22 cards)



### 🟡 Mid Level

#### 163. 1144. Why is modification via views not always systematically automated?
**Answer:**
Modifications through views are not always automated because the mapping between the view's result set and the underlying base tables can be ambiguous, especially when joins, aggregations, or distinct clauses are involved.





## 📂 Category: Performance & Indexing (182 cards)



### 🔴 Senior Level

#### 164. 1145. Why is querying XML considered less mature than SQL?
**Answer:**
Querying XML is considered less mature because it lacks a standard underlying formal algebra equivalent to relational algebra and is a newer technology compared to SQL.

#### 165. 1146. Why is strict data typing important in database design?
**Answer:**
Typing enforces data integrity and provides schema-level control, ensuring only valid data formats are stored in specific columns.





### 🟡 Mid Level

#### 166. 1147. Why is the SQL statement UPDATE used?
**Answer:**
The UPDATE statement is used to modify one or more values in specified columns of existing rows within a named table.

#### 167. 1148. Why is there a distinction between WHERE and HAVING?
**Answer:**
The WHERE clause filters rows before aggregation (input rows), whereas HAVING filters result groups after aggregation (group rows). Aggregate functions are generally not allowed in WHERE unless inside a subquery.





### 🔴 Senior Level

#### 168. 1149. Why might a predicate in an index seek operator be inefficient?
**Answer:**
A predicate in a seek operator might be considered inefficient or 'bad' if it hides an underlying index scan, meaning the engine is doing more work than a precise seek should entail.

#### 169. 115. How are XQuery and XSLT defined in relation to XPath?
**Answer:**
XQuery is defined as XPath + a full-featured compositional query language (SQL-like). XSLT is defined as XPath + transformations, commonly used for converting XML to HTML.

#### 170. 1150. Why must the correct ROUTE be set on both sides of a Service Broker DIALOG?
**Answer:**
The route must be configured on both sides to allow the initiator to send the initial message and the receiver to send back the necessary acknowledgement.





## 📂 Category: Basic SQL & Syntax (1 cards)



### 🔴 Senior Level

#### 171. 1151. Why would a relation fail 3NF?
**Answer:**
A relation fails 3NF if it contains transitive dependencies, where non-key attributes depend on other non-key attributes, which in turn depend on the primary key. To reach 3NF, these must be decomposed.





## 📂 Category: Database Programmability (52 cards)



### 🟡 Mid Level

#### 172. 1152. Write a query filtering with BETWEEN and additional operators.
**Answer:**
Example: SELECT * FROM movies WHERE year BETWEEN 1990 AND 2000 AND genre = 'comedy';





### 🟡 Mid Level

#### 173. 1153. Write a query joining Invoices and Customers to retrieve invoice details and referrer names.
**Answer:**
SELECT i.Id, i.BillingDate, c.Name, r.Name AS ReferredByName FROM Invoices i JOIN Customers c ON i.CustomerId = c.Id LEFT JOIN Customers r ON c.ReferredBy = r.Id ORDER BY i.BillingDate;





## 📂 Category: Performance & Indexing (45 cards)



### 🟡 Mid Level

#### 174. 1154. Write a query to calculate the total score of hackers based on the maximum score of their submissions, excluding those with a total score of 0, ordered by score (desc) and hacker_id (asc).
**Answer:**
SELECT h.hacker_id, h.name, SUM(max_scores.Max_Score) FROM (SELECT hacker_id, challenge_id, MAX(score) AS Max_Score FROM Submissions GROUP BY hacker_id, challenge_id) max_scores INNER JOIN Hackers h ON max_scores.hacker_id = h.hacker_id GROUP BY h.hacker_id, h.name HAVING SUM(max_scores.Max_Score) > 0 ORDER BY 3 DESC, 1 ASC





## 📂 Category: Transactions & Concurrency (17 cards)



### 🟡 Mid Level

#### 175. 1155. Write a query to find URLs that start with any character, have '://', contain a character before and after, and end in '.org'.
**Answer:**
SELECT * FROM ApprovedWebsites WHERE URLName LIKE '_%://_%.org'





## 📂 Category: Database Design & Normalization (94 cards)



### 🟡 Mid Level

#### 176. 1156. Write a statement to add a column 'Comments' of data type nvarchar(4000) that allows null values to be inserted to table 'Clients'.
**Answer:**
ALTER TABLE Clients ADD Comments nvarchar(4000) NULL;





## 📂 Category: Database Design & Normalization (55 cards)



### 🟢 Junior Level

#### 177. 1157. sys.dm_db_index_operational_stats
**Answer:**
A Dynamic Management Object (DMO) that returns low-level, detailed statistics regarding index access, locking, and latching activity.

#### 178. 1158. sys.dm_db_index_physical_stats
**Answer:**
A system function that returns size and fragmentation information about indexes, supporting varying levels of detail (LIMITED, SAMPLED, or DETAILED).

#### 179. 1159. sys.dm_db_index_usage_stats
**Answer:**
A Dynamic Management Object (DMO) that returns information about how frequently indexes are used and the specific types of operations performed (seeks, scans, lookups, updates).

#### 180. 116. How are column concatenation and aliasing performed in SQL?
**Answer:**
You can combine column values using the concatenation operator (such as '+') and assign a new label to the resulting output column using the 'AS' keyword.

#### 181. 1160. sys.dm_exec_cached_plans
**Answer:**
A system view that returns information about all query execution plans that are currently stored in the plan cache.

#### 182. 1161. sys.dm_exec_plan_attributes
**Answer:**
A system function that returns information about specific attributes (such as SET options or database context) of a particular plan that influenced its compilation.

#### 183. 1162. sys.dm_exec_query_optimizer_info
**Answer:**
A system table providing detailed statistics and information about the Query Optimizer's behavior and operations since the last server restart.

#### 184. 1163. sys.dm_exec_query_plan
**Answer:**
A system function that retrieves the XML representation of a specific execution plan based on a given plan handle.

#### 185. 1164. sys.dm_exec_query_stats
**Answer:**
A system function that returns aggregate performance statistics (CPU, duration, reads, writes) for cached query plans.

#### 186. 1165. sys.dm_exec_requests
**Answer:**
A Dynamic Management Object (DMO) used to view all currently executing requests or tasks within the SQL Server instance.

#### 187. 1166. sys.dm_exec_sql_text
**Answer:**
A system table function that returns the text of the SQL batch corresponding to a specific query plan handle.

#### 188. 1167. sys.dm_exec_transformation_stats
**Answer:**
A system table containing statistics regarding the usage of specific transformation rules applied by the Query Optimizer.

#### 189. 1168. sys.dm_os_wait_stats
**Answer:**
A system function that returns information about all wait types encountered by threads during the execution of tasks.

#### 190. 1169. sys.dm_os_waiting_tasks
**Answer:**
A Dynamic Management Object (DMO) that returns information about all tasks currently in a 'waiting' state, including the resource they are waiting for.

#### 191. 117. How are computed columns implemented?
**Answer:**
Computed columns are expressions based on other columns. They can be 'virtual' (computed on the fly) or 'persisted' (stored on disk and updated whenever the underlying data changes).

#### 192. 1170. sys.fn_PhysLocFormatter
**Answer:**
A function that parses and formats the output of the %%physloc%% virtual column into a human-readable format (FileID:PageID:SlotID).

#### 193. 1171. sys.indexes
**Answer:**
A catalog view that contains a row for every index or heap in the database.





## 📂 Category: Subqueries & Aggregations (48 cards)



### 🟡 Mid Level

#### 194. 1172. sys.system_internals_allocation_units
**Answer:**
An undocumented system table that provides low-level information about allocation units, including pointers to IAM pages, root index pages, and the first leaf pages.





## 📂 Category: Subqueries & Aggregations (9 cards)



### 🔴 Senior Level

#### 195. 118. How are data records ordered in index leaves?
**Answer:**
Data in index leaf nodes is ordered by the Clustered Key (CK).

#### 196. 119. How are database functions invoked?
**Answer:**
Functions can be invoked within SELECT, INSERT, or UPDATE statements.

#### 197. 12. Can triggers activate other triggers?
**Answer:**
Yes, triggers can activate themselves or other triggers in a chain, which can lead to nested or recursive execution.

#### 198. 120. How are date and time handled in SQL?
**Answer:**
Date handling relies on specific data types like DATE, DATETIME, and TIMESTAMP. The primary challenge is ensuring the inserted format matches the database column format. Different RDBMS (MySQL, SQL Server) have slightly different formats and storage capabilities, so consulting documentation is essential.

#### 199. 121. How are multi-line comments written in SQL?
**Answer:**
Multi-line comments start with '/*' and end with '*/'. Any text placed between these delimiters is ignored by the SQL engine.

#### 200. 122. How are multiple tables combined into a single result set?
**Answer:**
The JOIN operation is used to combine columns from multiple tables based on a related column between them.

#### 201. 123. How are pages connected within the same level of an index?
**Answer:**
Pages within the same index level are connected via a doubly linked list.

#### 202. 124. How are queries and modifications handled in virtual views?
**Answer:**
Since virtual views are logical constructs and not stored tables, queries are rewritten by the DBMS to reference the underlying base tables. Modifications can be ambiguous and are not always supported or automatic.

#### 203. 125. How are relationships represented in a join table?
**Answer:**
Each row in a join table represents a single association between records in two other tables, often containing the primary keys of both to map the relationship.

#### 204. 126. How are row offsets stored on a page?
**Answer:**
They are stored at the end of the data page in a slot array, ordered backwards.

#### 205. 127. How are rows from two or more tables combined based on a common field?
**Answer:**
Using SQL Joins.

#### 206. 128. How are stored procedures executed?
**Answer:**
Stored procedures are typically executed using an explicit CALL statement or the EXEC/EXECUTE command depending on the SQL dialect.

#### 207. 129. How are triggers defined conceptually?
**Answer:**
Triggers are Event-Condition-Action (ECA) rules.

#### 208. 13. Can triggers be associated with a view?
**Answer:**
Yes, specifically 'INSTEAD OF' triggers are commonly used on views to handle modifications that cannot be automatically mapped to base tables.

#### 209. 130. How are variables assigned in a PL/SQL block?
**Answer:**
Variables can be assigned using the assignment operator (:=) or via the result of a SQL SELECT INTO or FETCH statement.

#### 210. 131. How can NOT NULL columns save space in an index?
**Answer:**
In nonclustered indexes, if all columns are defined as NOT NULL, the leaf nodes do not need to include a NULL bitmap, reducing storage overhead.

#### 211. 132. How can XML data be displayed using rule-based languages?
**Answer:**
XML can be transformed for display using Cascading Style Sheets (CSS) or Extensible Stylesheet Language (XSL).

#### 212. 133. How can ad hoc queries reuse execution plans?
**Answer:**
Query plans can be reused via identical SQL text, auto-parameterization, or the use of Plan Guides.

#### 213. 134. How can infinite cycles be prevented when using recursive WITH statements?
**Answer:**
Infinite cycles can be prevented by: 1) Setting a recursion limit via a WHERE clause (e.g., stopping when a path length reaches a maximum), 2) Using a LIMIT clause outside the recursion (though this may not work for all aggregate operations), or 3) Using a subquery in the WHERE clause to prune redundant or costlier paths, which is the most robust standard-compliant approach.

#### 214. 135. How can one handle null bitmaps in indexes?
**Answer:**
In a clustered index, null bitmap behavior is fixed by the structure. In a non-clustered index, it is possible to optimize index storage to handle nulls more efficiently.

#### 215. 136. How can stored procedures or functions improve application performance?
**Answer:**
They reduce network traffic by sending a single command rather than multiple, and they allow the database to pre-compile execution plans, reducing the parsing overhead for repetitive tasks.

#### 216. 137. How can the order of execution be defined for AFTER triggers in SQL Server?
**Answer:**
By using sp_settriggerorder to specify 'FIRST', 'LAST', or 'NONE' (undefined).

#### 217. 138. How can you aggregate multiple rows into a single comma-separated string?
**Answer:**
In modern SQL (2017+), use the STRING_AGG(column, ',') function. For older versions, use the 'FOR XML PATH' trick combined with the STUFF() function to remove the leading comma.

#### 218. 139. How can you count rows meeting specific criteria?
**Answer:**
Use the COUNT aggregate function combined with a WHERE clause: e.g., SELECT COUNT(*) FROM table WHERE condition = value;

#### 219. 14. Can you query a table using only schema.name (e.g., HumanResources.Employee)?
**Answer:**
Yes, provided that the query window or session is already connected to the database containing that specific schema and table.

#### 220. 140. How can you determine if a set of attributes A is a key for a relation R?
**Answer:**
Compute the attribute closure A+. If the resulting set includes all attributes in the relation R, then A is a key.

#### 221. 141. How can you identify projects by finding consecutive start and end dates in a task table?
**Answer:**
To identify consecutive projects, you can use row numbering on sets of start dates (those not existing as end dates) and end dates (those not existing as start dates). Joining these two sets on the assigned row IDs aligns the start and end of each unique project sequence.

#### 222. 142. How can you identify rows in one table that have no matching records in another?
**Answer:**
Perform a LEFT JOIN between the two tables and add a WHERE clause filtering for NULL values on the right-side join key (e.g., WHERE Table2.ID IS NULL).

#### 223. 143. How can you reduce network traffic between applications and the database?
**Answer:**
By encapsulating logic within Functions and Stored Procedures, which allows the database to process data locally and return only the final result sets.

#### 224. 144. How can you simulate a MAX() function using set operators?
**Answer:**
You can simulate the MAX() function by using the EXCEPT operator to remove all values that are not the maximum. Example: SELECT * FROM rel EXCEPT SELECT * FROM rel WHERE attr < (SELECT MAX(attr) FROM rel). Alternatively, selecting all tuples except those that are smaller than at least one other tuple will leave only the maximum.

#### 225. 145. How can you temporarily rename a table or a column heading?
**Answer:**
Using SQL Aliases (typically via the AS keyword).

#### 226. 146. How can you test if a string value is a valid 'datetime' in SQL Server?
**Answer:**
You can use the TRY_CONVERT(datetime, 'your_value') function. If the conversion is unsuccessful, it returns NULL, preventing the query from crashing.

#### 227. 147. How can you validate if a string represents a valid date?
**Answer:**
Use the ISDATE(expression) function, which returns 1 if the expression is a valid date format and 0 otherwise.

#### 228. 148. How do B-trees and Hash tables compare as indexing structures?
**Answer:**
Hash tables offer O(1) time complexity for exact equality lookups (A=V) but do not support range queries. B-trees (B+ trees) have logarithmic O(log n) complexity but are versatile, supporting both equality and range queries (e.g., A > V, A < V).

#### 229. 149. How do DBMS handle queries against virtual views?
**Answer:**
While views conceptually act like temporary tables, in practice, the DBMS rewrites the query referencing the view into a query that references the underlying base tables (or recursive views) directly.

#### 230. 15. Can you sort a column using a column alias?
**Answer:**
Yes, you can use the column alias in the ORDER BY clause to specify the sorting order of the result set.

#### 231. 150. How do ER models map to natural language and database structure?
**Answer:**
Entities map to nouns (things/objects), relationships map to verbs (actions between entities), and attributes are details about entities or relationships. Every entity must have a primary key for unique identification.

#### 232. 151. How do GROUP BY and HAVING clauses work in aggregation?
**Answer:**
GROUP BY aggregates rows that have the same values into summary rows. HAVING is used to filter the groups created by the GROUP BY clause based on a condition (unlike WHERE, which filters individual rows).

#### 233. 152. How do Hash tables compare to Balanced Trees in database indexing?
**Answer:**
Hash tables provide faster lookup performance (constant time O(1)) compared to Balanced Trees (logarithmic time O(log n)), though they are generally only useful for equality matches rather than range queries.

#### 234. 153. How do NOT BETWEEN and NOT IN operators work in SQL?
**Answer:**
These operators negate range or inclusion conditions. NOT BETWEEN excludes values in the defined range (inclusive of boundaries). NOT IN excludes all values matching the provided list. They are often combined with other logical operators to filter results.

#### 235. 154. How do NoSQL databases compare to traditional relational (RDBMS) systems?
**Answer:**
NoSQL generally offers more flexibility (less schema/preprocessing), higher scalability, and efficiency, but typically lacks the complex query expressivity and strict ACID guarantees of RDBMS.

#### 236. 155. How do SQL and NoSQL databases differ in approach to structure?
**Answer:**
SQL requires predefined schemas, enforcing rigid, uniform structures for data integrity. NoSQL offers dynamic, flexible schemas for unstructured data, allowing unique document structures and easier schema evolution at the cost of strict relational consistency.

#### 237. 156. How do SQL and NoSQL databases scale differently?
**Answer:**
SQL databases are vertically scalable, increasing performance on a single server (CPU, RAM, SSD). NoSQL databases are horizontally scalable, handling more traffic by sharding and adding more servers.

#### 238. 157. How do aggregate functions handle NULL values?
**Answer:**
Aggregate functions ignore NULL values in their calculations, with the notable exception of COUNT(*), which counts rows regardless of nullability.

#### 239. 158. How do constraints relate to triggers?
**Answer:**
Constraints are static and can be simulated by triggers. Triggers are dynamic, more powerful, and cannot be fully simulated by constraints.

#### 240. 159. How do implicit data type mismatches impact index performance?
**Answer:**
If an indexed column is compared against a value of a different data type requiring implicit conversion, the DB automatically converts the column value for every row, leading to a Full Table Scan.



- ❌ `WHERE user_id = 123` (without quotes when `user_id` is `VARCHAR`) -> Full Table Scan!



- ✅ `WHERE user_id = '123'` (with string quotes) -> Index Used!

#### 241. 16. Co je to JOIN operace v SQL?
**Answer:**
Operace umožňující kombinovat záznamy z více tabulek na základě společných atributů. Typy zahrnují: Natural Join (shodné názvy sloupců), Equijoin (rovnost hodnot) a Outer Join (zahrnuje i neshodné řádky s NULL hodnotami).

#### 242. 160. How do indexes affect AND versus OR operators?
**Answer:**
For an AND operator, it is typically more efficient to have one composite index. For an OR operator, it is often better to have separate indexes on the involved columns.

#### 243. 161. How do materialized views improve database performance?
**Answer:**
Materialized views improve performance by physically caching the result of a query, effectively acting like an index on a complex result set. The query optimizer can automatically rewrite queries to access this precomputed data rather than executing the original complex joins/aggregations.

#### 244. 162. How do rows in intermediate pages differ between UNIQUE and non-UNIQUE indexes?
**Answer:**
In non-UNIQUE indexes, intermediate pages must include either the Row ID (RID) or the Clustered Key (CK) alongside the Index Key (IK) to uniquely identify entries.

#### 245. 163. How do table variables behave within a transaction in SQL Server?
**Answer:**
They do not participate in or respect the transactional rollback mechanism.

#### 246. 164. How do the LIKE operator and the underscore (_) wildcard function?
**Answer:**
The LIKE operator is used in a WHERE clause to perform pattern matching. The underscore (_) wildcard represents any single unspecified character in the pattern.

#### 247. 165. How do you add a new column to an existing table?
**Answer:**
Use the ALTER TABLE statement: ALTER TABLE table_name ADD COLUMN column_name data_type;

#### 248. 166. How do you add a new row to a database table?
**Answer:**
Use the INSERT INTO statement: INSERT INTO table_name (col1, col2) VALUES (val1, val2);

#### 249. 167. How do you add a row to a database table and handle the primary key?
**Answer:**
Use 'INSERT INTO table_name (col1, col2) VALUES (val1, val2);'. It is not necessary to explicitly add an ID if you have defined a PRIMARY KEY (which is usually auto-incrementing in databases like PostgreSQL and SQLite).

#### 250. 168. How do you add or remove a column from a table?
**Answer:**
Use the ALTER TABLE command: 'ALTER TABLE table_name ADD COLUMN column_name data_type;' to add a column, and 'ALTER TABLE table_name DROP COLUMN column_name;' to remove one.

#### 251. 169. How do you add up the number of items per category?
**Answer:**
SELECT category, SUM(column_name) FROM table_name GROUP BY category;

#### 252. 17. Co je to Language parser?
**Answer:**
Součást relačního enginu zodpovědná za syntaktickou analýzu SQL dotazu a vytvoření stromu dotazu (parser tree).

#### 253. 170. How do you alias columns and count rows in SQL?
**Answer:**
Column aliases are created using the 'AS' keyword (e.g., 'SELECT City AS CityName'). The 'COUNT(*)' function returns the total number of rows that satisfy a filter condition. Unlike 'SELECT *', which returns all columns, aggregate functions reduce result sets to a single value.

#### 254. 171. How do you calculate the difference between two dates and how do you add intervals to a date?
**Answer:**
Use DATEDIFF(interval, start_date, end_date) to find the difference between two dates in the specified interval. Use DATEADD(interval, number, date) to add a specified number of intervals to a date.

#### 255. 172. How do you calculate the sum of an integer column?
**Answer:**
Use the SUM() aggregate function: SELECT SUM(column_name) FROM table_name;

#### 256. 173. How do you check for NULL values in SQL?
**Answer:**
Use the IS NULL operator in the WHERE clause: SELECT column_names FROM table_name WHERE column_name IS NULL;

#### 257. 174. How do you check for non-null values in SQL?
**Answer:**
Use the IS NOT NULL operator in the WHERE clause: SELECT column_names FROM table_name WHERE column_name IS NOT NULL;

#### 258. 175. How do you combine a LEFT JOIN and a RIGHT JOIN?
**Answer:**
The FULL OUTER JOIN returns all rows from both tables, filling with NULLs when there is no match in one of the sides.

#### 259. 176. How do you concatenate strings (like e-mails) grouped by a specific column (like Department)?
**Answer:**
Use the STRING_AGG function: SELECT Dep, STRING_AGG(email, '; ') WITHIN GROUP (ORDER BY email) AS DepEmails FROM Emails GROUP BY Dep. This function is available in modern SQL dialects like MS SQL Server 2017+.

#### 260. 177. How do you connect to a specific database in PostgreSQL?
**Answer:**
Use the command \c database_name.

#### 261. 178. How do you count entries, filter by nulls, and query for unique values?
**Answer:**
Use 'SELECT COUNT(*) FROM table;' to count all entries. Use 'IS NULL' or 'IS NOT NULL' in a WHERE clause to filter for null values. Use 'SELECT DISTINCT column FROM table;' to retrieve only unique values.

#### 262. 179. How do you count the number of entries in a table?
**Answer:**
Use the COUNT() function: SELECT COUNT(*) FROM table_name;

#### 263. 18. Co je to latch?
**Answer:**
Mechanismus fyzického zamykání stránek v paměti pro zajištění konzistentního přístupu více vláken vykonávacího enginu.

#### 264. 180. How do you count the number of items per category?
**Answer:**
Use the COUNT() aggregate function combined with a GROUP BY clause: SELECT price, COUNT(*) FROM fake_apps GROUP BY price;

#### 265. 181. How do you create a many-to-many relationship in a relational database?
**Answer:**
A many-to-many relationship is implemented using a join table (also known as a junction table or associative entity). This table contains foreign keys referencing the primary keys of the two tables being linked.

#### 266. 182. How do you create a table in SQL?
**Answer:**
The CREATE TABLE statement defines a table's structure with column names and data types. You can also create a new table based on the structure and data of an existing table using 'CREATE TABLE new_table AS SELECT ... FROM existing_table'.

#### 267. 183. How do you create and drop databases in SQL?
**Answer:**
Use 'CREATE DATABASE databasename;' to create a new database. Use 'DROP DATABASE databasename;' to permanently remove an existing database. Be cautious, as dropping a database results in the loss of all data contained within it.

#### 268. 184. How do you create and drop tables in SQL?
**Answer:**
Use 'CREATE TABLE table_name (column1 datatype, column2 datatype, ...);' to define a new table structure. Use 'DROP TABLE table_name;' to remove a table and its associated data entirely. Be cautious, as this action cannot be undone.

#### 269. 185. How do you create statistics for computed values (e.g., A*B)?
**Answer:**
Create a persisted computed column with the exact same formula, or use a column with the identical expression; the text representation must match exactly.

#### 270. 186. How do you create tables with primary keys and foreign key constraints in SQL?
**Answer:**
Use the CREATE TABLE statement specifying the column types and PRIMARY KEY constraints. Foreign key constraints are added using the REFERENCES keyword, often defined at the table or column level.

#### 271. 187. How do you define a custom data type with specific constraints?
**Answer:**
You use the CREATE DOMAIN statement (in standard SQL) to define a custom data type along with associated CHECK constraints that are applied whenever the type is used.

#### 272. 188. How do you define and use functions in SQL?
**Answer:**
A function accepts zero or more parameters and returns a single value. Examples include: GETDATE() (no params), STR(numeric) (one param), CONVERT(type, val) (two params), and CONCAT('a', 'b', 'c') (multiple params).

#### 273. 189. How do you define the database context for a query?
**Answer:**
Use the USE command (e.g., 'USE database_name;').

#### 274. 19. Compare EXEC(SQL) and sp_executesql.
**Answer:**
EXEC(SQL) is typically used for ad-hoc queries and does not easily allow for parameterization, which can lead to recompilation and security risks. sp_executesql allows for parameterization, which enables the SQL engine to reuse execution plans, improving performance and security.

#### 275. 190. How do you determine if a set of Functional Dependencies (FDs) S2 follows from S1?
**Answer:**
To check if S2 follows from S1, compute the attribute closure (A+) of the left-hand side of each dependency in S2 using the dependencies in S1. If the right-hand side attributes of the dependency in S2 are contained within the closure, then the dependency is implied by S1.

#### 276. 191. How do you drop common database constraints?
**Answer:**
Constraints are removed using ALTER TABLE statements. For example: 'ALTER TABLE table_name DROP CONSTRAINT constraint_name' (Syntax varies by RDBMS; e.g., MySQL often uses 'DROP FOREIGN KEY' or 'DROP PRIMARY KEY').

#### 277. 192. How do you edit a row in a table?
**Answer:**
Use the UPDATE command: 'UPDATE table_name SET col_name = new_value WHERE id = target_id;'

#### 278. 193. How do you ensure data in a column is valid JSON?
**Answer:**
Use a CHECK constraint with the ISJSON() function, e.g., CHECK (ISJSON(column_name) = 1).

#### 279. 194. How do you exclude a character from your result set?
**Answer:**
Use the NOT operator within the LIKE clause and brackets. For example: SELECT * FROM Employee WHERE LastName LIKE 'O[^S]%'.

#### 280. 195. How do you expose statistics for table variables to the query optimizer?
**Answer:**
Use the OPTION(RECOMPILE) query hint.

#### 281. 196. How do you extract components (Year, Month, Day) from a date, and how do you reconstruct a date or datetime from those parts?
**Answer:**
Use functions like YEAR(), MONTH(), or DAY() to extract parts. Use DATEPART(part, date) for more flexible extraction. To reconstruct, use DATEFROMPARTS(year, month, day) or DATETIMEFROMPARTS(year, month, day, hour, min, sec, ms).

#### 282. 197. How do you filter data using basic comparison, logical operators (AND/OR), and 'IN' clauses?
**Answer:**
Use the WHERE clause with operators like '=', '<>', '>', 'IN', 'AND', and 'OR'. Note that 'AND' requires both conditions to be true, while 'OR' requires at least one. Using 'IN' is a cleaner alternative to multiple OR statements (e.g., ID IN ('1', '2')).

#### 283. 198. How do you filter records based on NULL values or empty spending (Samnt)?
**Answer:**
To find records with missing data, use 'IS NULL' or 'IS NOT NULL'. To identify customers who haven't spent money, use 'WHERE Samnt = 0 OR Samnt IS NULL'. To find those who have spent, use 'WHERE Samnt > 0' or 'WHERE NOT (Samnt = 0 OR Samnt IS NULL)'.

#### 284. 199. How do you filter rows in a SQL table based on specific conditions for numeric values, null values, or patterns?
**Answer:**
Use the WHERE clause with operators: '=' for exact, '<', '>', '<=', '>=', '<>' for comparisons, 'LIKE' for pattern matching (e.g., % for wildcards), and 'IS NULL' or 'IS NOT NULL' to check for null values.

#### 285. 2. Analyze common SQL syntax errors regarding DDL and DML operations.
**Answer:**
Common errors include: omitting required keywords (e.g., 'TABLE' or 'INTO'), mismatching column counts during INSERT, inserting invalid data types into columns (e.g., string into date), or attempting to manipulate data in a table that has not been created or lacks the correct schema definition.

#### 286. 20. Compare OLAP and OLTP.
**Answer:**
OLTP (Online Transactional Processing) is designed for fast, frequent, short-lived transactions. OLAP (Online Analytical Processing) is designed for complex, read-heavy analytical queries over large datasets, often utilizing aggregations and materialized views for performance.

#### 287. 200. How do you find all candidate keys given a set of functional dependencies (FDs)?
**Answer:**
Compute the closures of every subset of attributes in increasing size. If a subset is a superkey, any superset of it is also a superkey. This process also identifies all functional dependencies within the relation.

#### 288. 201. How do you find employee names starting with 'A'?
**Answer:**
SELECT * FROM Table_name WHERE EmpName LIKE 'A%'

#### 289. 202. How do you force the SQL optimizer to consider indexes on a view?
**Answer:**
Use the WITH (NOEXPAND) table hint in the query.

#### 290. 203. How do you handle NULL values in SQL?
**Answer:**
NULL represents the absence of a value. To insert a NULL, use the literal NULL. To filter for NULLs, use 'IS NULL' or 'IS NOT NULL' because standard comparison operators (like '=') will fail against NULL.

#### 291. 204. How do you handle column names with spaces in SQL?
**Answer:**
Use double quotes ("alias") or square brackets ([alias]) to delimit the column name.

#### 292. 205. How do you handle concatenation and data types in SQL functions?
**Answer:**
Functions like CONCAT join strings. When concatenating different data types (e.g., datetime and string), the non-string value must be converted explicitly using CONVERT or CAST to avoid errors. Example: CONCAT('Date: ', CONVERT(nvarchar, GETDATE())).

#### 293. 206. How do you handle special characters (like quotes or wildcards) in SQL queries?
**Answer:**
For single quotes, escape them by adding another single quote (e.g., 'WHERE name LIKE ''%'''). To treat wildcards like % or _ as literals, use brackets in the pattern: 'LIKE ''%[%]%''' or 'LIKE ''%[_]%'''.

#### 294. 207. How do you handle special characters like a single quote in a string literal?
**Answer:**
Use an escape character by doubling the single quote (e.g., 'Mc''Donald').

#### 295. 208. How do you implement conditional logic in a SELECT statement?
**Answer:**
Use the CASE expression: CASE WHEN condition THEN result ELSE default END. It allows row-by-row categorization of data.

#### 296. 209. How do you include duplicate rows when using a UNION operator?
**Answer:**
Use UNION ALL instead of UNION (which defaults to distinct values only).

#### 297. 21. Compare the strictness of Fourth Normal Form (4NF) and Boyce-Codd Normal Form (BCNF).
**Answer:**
Fourth Normal Form (4NF) is stricter than Boyce-Codd Normal Form (BCNF). While BCNF deals with functional dependencies, 4NF addresses multi-valued dependencies.

#### 298. 210. How do you join tables to retrieve related data?
**Answer:**
Use an INNER JOIN on the common key: SELECT FirstName, LastName, City FROM Employee INNER JOIN Location ON Employee.LocationID = Location.LocationID.

#### 299. 211. How do you make changes permanent in a database?
**Answer:**
The COMMIT statement is used to finalize and persist all changes made during the current transaction.

#### 300. 212. How do you manage output and session state in the SQLite CLI?
**Answer:**
.headers on/.mode column (formatting), .quit (exit). Note: SQL statements must end with a semicolon; if omitted, the CLI waits for further input until one is provided.

#### 301. 213. How do you manage transactions in PostgreSQL?
**Answer:**
Transactions are wrapped in 'BEGIN' and 'COMMIT'. If an error occurs or logic dictates, 'ROLLBACK' cancels the changes. 'SAVEPOINT' allows for partial rollbacks within a transaction.

#### 302. 214. How do you manage views in SQL?
**Answer:**
A view is a virtual table based on a SELECT query. You can create one using 'CREATE VIEW view_name AS SELECT...', update it using 'CREATE OR REPLACE VIEW', and delete it using 'DROP VIEW view_name'. Views provide a way to simplify complex queries and restrict data access.

#### 303. 215. How do you match characters not specified within brackets in a SQL pattern match?
**Answer:**
Use the [^charlist] or [!charlist] syntax within the LIKE operator to exclude specific characters.

#### 304. 216. How do you modify existing data in a table?
**Answer:**
The UPDATE statement is used to change existing values in one or more columns of a table.

#### 305. 217. How do you modify table structure using the ALTER TABLE command?
**Answer:**
ALTER TABLE is used to modify the structure of an existing table. Common operations include: ADD COLUMN (to add a field), DROP COLUMN (to remove a field), and ALTER/MODIFY COLUMN (to change a field's data type). Syntax varies slightly by vendor (e.g., SQL Server vs. MySQL).

#### 306. 218. How do you perform a LEFT JOIN and when is it typically used?
**Answer:**
A LEFT JOIN returns all rows from the left table and matching rows from the right table. If no match exists, the right side columns return NULL. It is used to expand a primary table with auxiliary information without losing data from the primary table.

#### 307. 219. How do you perform basic aggregations on a table?
**Answer:**
Use aggregate functions: SUM(column) to add values, MAX(column) to find the largest value, and COUNT(*) to find the number of rows.

#### 308. 22. Define 3rd Normal Form (3NF).
**Answer:**
A table is in 3rd Normal Form when it is in 2nd Normal Form and there are no transitive dependencies (i.e., non-key attributes must depend only on the primary key).

#### 309. 220. How do you perform basic selection, sorting, and limiting of results?
**Answer:**
Use 'SELECT col1, col2 FROM table;' to select columns, 'ORDER BY col_name DESC;' to sort in descending order, and 'WHERE' clauses to filter data.

#### 310. 221. How do you perform date and time comparisons in SQL queries?
**Answer:**
To compare dates, you often need to normalize values: use YEAR() to extract year parts, CONVERT() to reduce datetime to date, or DATEDIFF() to calculate durations between two dates. Example: 'SELECT Cname, DATEDIFF(year, Bdate, '1999-01-01') AS AgeIn99 FROM Clients'.

#### 311. 222. How do you perform joins in SQL?
**Answer:**
Joins are used to combine rows from two or more tables based on a related column. Common types include INNER JOIN, LEFT JOIN, and CROSS JOIN. Note that some systems (like SQLite) do not support RIGHT or FULL OUTER JOINs natively.

#### 312. 223. How do you perform pattern matching in SQL?
**Answer:**
The LIKE clause is used with wildcard characters (like % or _) to search for a specific pattern in a string column.

#### 313. 224. How do you perform text manipulation like extraction and replacement in MS SQL?
**Answer:**
Use string functions: LEFT() or RIGHT() to extract from edges, SUBSTRING() with CHARINDEX() for middle segments, and STUFF() to replace or delete characters within a string.

#### 314. 225. How do you pivot data in SQL?
**Answer:**
Use the PIVOT operator. It rotates rows into columns by aggregating values (e.g., SUM) based on a specific category column.

#### 315. 226. How do you protect against SQL injection?
**Answer:**
Use parameterized queries (prepared statements). These treat inputs as data values rather than executable code, preventing the malicious alteration of the SQL command.

#### 316. 227. How do you query a subset of columns from a table?
**Answer:**
Specify the required column names in the SELECT clause: SELECT col1, col2 FROM table_name;

#### 317. 228. How do you query an alphabetically ordered list of names with their profession first letter in parentheses, and a count of occurrences for each occupation in SQL?
**Answer:**
To get names: SELECT CONCAT(name, '(', LEFT(occupation, 1), ')') FROM OCCUPATIONS ORDER BY name ASC; To get counts: SELECT CONCAT('There are a total of ', COUNT(occupation), ' ', LOWER(occupation), 's.') FROM OCCUPATIONS GROUP BY occupation ORDER BY COUNT(occupation), occupation ASC;

#### 318. 229. How do you query data from multiple tables simultaneously?
**Answer:**
Use a JOIN clause (INNER, LEFT, RIGHT, or FULL).

#### 319. 23. Define Boyce-Codd Normal Form (BCNF).
**Answer:**
A table is in BCNF when it consists of atomic attributes, each non-key attribute is fully dependent on a candidate key, no non-key attribute depends on another non-key attribute, and every determinant is a candidate key.

#### 320. 230. How do you query for a single quote inside a string literal?
**Answer:**
You must escape the single quote by adding another single quote before it. Example: SELECT * FROM Grant WHERE GrantName LIKE '%' '%'.

#### 321. 231. How do you query for multiple characters using wildcards?
**Answer:**
Use brackets to define character sets or ranges. Examples: LIKE '[ABCDE]%' or LIKE '[A-K]%'.

#### 322. 232. How do you query for special characters like % and _ literally?
**Answer:**
Enclose the special character in brackets within the LIKE clause. Examples: LIKE '%[%%%]%' to find a literal percent sign, or LIKE '%[_]%' to find a literal underscore.

#### 323. 233. How do you query for unique values in a specific column?
**Answer:**
Use the DISTINCT keyword: SELECT DISTINCT column_name FROM table_name;

#### 324. 234. How do you remove duplicate values when performing an aggregation?
**Answer:**
The DISTINCT keyword is used inside aggregate functions (e.g., COUNT(DISTINCT column_name)) to consider only unique values.

#### 325. 235. How do you rename columns when using SELECT INTO to create a new table?
**Answer:**
You can use the AS clause to alias column names in the output table.

#### 326. 236. How do you retrieve the third-highest salary from an employee table?
**Answer:**
SELECT TOP 1 salary FROM (SELECT TOP 3 salary FROM employee_table ORDER BY salary DESC) AS emp ORDER BY salary ASC;

#### 327. 237. How do you retrieve the three lowest rated movies?
**Answer:**
SELECT * FROM movies ORDER BY imdb_rating ASC LIMIT 3;

#### 328. 238. How do you retrieve unique values from a column?
**Answer:**
Use the 'DISTINCT' keyword before the column name (e.g., 'SELECT DISTINCT City FROM Clients'). This removes duplicate values from the result set, returning only unique entries for the specified column.

#### 329. 239. How do you select values within a range in SQL?
**Answer:**
Using the BETWEEN operator.

#### 330. 24. Define Boyce-Codd normal form (BCNF).
**Answer:**
A table is in BCNF if it is in 3NF and every determinant is a candidate key. This prevents dependency issues between parts of candidate keys.

#### 331. 240. How do you simulate universal quantification ('for all') in XPath?
**Answer:**
You can simulate it using the count() built-in function to compare the count of matching nodes against the total number of nodes.

#### 332. 241. How do you store special characters (like Chinese or other non-Latin scripts) in a database table?
**Answer:**
You should use Unicode-aware data types, such as 'nvarchar' in MS SQL, which are specifically designed to store characters from any language.

#### 333. 242. How do you switch the Postgres CLI to vertical output mode?
**Answer:**
Use the command \x to toggle the display format of query results to a vertical list of columns.

#### 334. 243. How do you test for NULL values in SQL?
**Answer:**
You cannot use standard comparison operators (=). Instead, use the 'IS NULL' or 'IS NOT NULL' operators.

#### 335. 244. How do you trace the traffic hitting a SQL Server?
**Answer:**
SQL Profiler is the utility used to trace traffic. Traces can be filtered to capture specific transactions, reducing overhead, and saved/replayed for troubleshooting.

#### 336. 245. How do you translate an association with 1..1 or 0..1 multiplicity into relations?
**Answer:**
When a 1..1 or 0..1 multiplicity exists, the key of the relation can be derived from the 'many' side of the association. We can either use a combined primary key or, preferably, transfer the primary key of the 'one' side to the 'many' side and remove the explicit association table.

#### 337. 246. How do you update an existing row in a database table?
**Answer:**
Use the UPDATE statement with a WHERE clause: UPDATE table_name SET col1 = val1 WHERE id = x;

#### 338. 247. How do you use the SQL DELETE statement?
**Answer:**
The DELETE statement is used to remove records from a table using 'DELETE FROM table_name WHERE condition;'. Omitting the WHERE clause will delete all rows in the table. While it removes the data, the table structure and attributes remain intact.

#### 339. 248. How do you write comments in SQL?
**Answer:**
Use double hyphens (--) for single-line comments.

#### 340. 249. How does COUNT(*) differ from COUNT(column_name)?
**Answer:**
COUNT(*) counts every row in the result set including rows with NULLs. COUNT(column_name) ignores NULL values in that specific column.

#### 341. 25. Define Drill-down and Roll-up operations in OLAP.
**Answer:**
Drill-down involves moving from summarized data to more granular levels by adding attributes to the GROUP BY clause. Roll-up moves from granular data to higher-level summaries by removing attributes from the GROUP BY clause.

#### 342. 250. How does ROLLUP aggregation work?
**Answer:**
ROLLUP creates subtotals and a grand total. The last attribute in the GROUP BY clause is the most granular level of aggregation, and the hierarchy moves toward higher-level totals as attributes are dropped from the right.

#### 343. 251. How does SQL Server Service Broker handle failed message delivery?
**Answer:**
It implements an exponential backoff retry strategy, attempting delivery at intervals of 4s, 8s, 16s, 32s, and then repeatedly every 60s.

#### 344. 252. How does XML schema flexibility compare to the Relational model?
**Answer:**
XML schemas are significantly more flexible than the rigid, predefined schemas found in the Relational model.

#### 345. 253. How does XML structure data?
**Answer:**
XML expresses data as a tree structure.

#### 346. 254. How does XPath query data?
**Answer:**
XPath queries data using paths combined with predicates/conditions to filter elements (e.g., doc('file.xml')/root/element[condition=value]).

#### 347. 255. How does XSD compare to DTD?
**Answer:**
XSD (XML Schema Definition) is more expressive than DTD (Document Type Definition), offering support for data types, namespaces, and complex hierarchical structures.

#### 348. 256. How does a covering index improve performance compared to a full table scan?
**Answer:**
A covering index contains all the columns required by the query, allowing the database to satisfy the request using only the index pages, which are smaller and fewer than the full table pages.

#### 349. 257. How does a database fetch data after jumping to a secondary index vs. a covering index?
**Answer:**
- **Secondary Index:** Stores indexed columns + Primary Key ID. For `SELECT * FROM comments WHERE path LIKE '001%'`, the DB searches `idx_path` to find matching IDs (1st jump), then looks up those IDs in the Primary Key table to fetch full row data (2nd jump — "Bookmark Lookup").



- **Covering Index:** If a query selects ONLY columns that are present inside the index (e.g. `SELECT id, status FROM users WHERE tenant_id = 5` when index is `(tenant_id, status)`), the DB returns data directly from index memory without touching the main table (Covering Index Scan).

#### 350. 258. How does a filtered index behave in a stored procedure?
**Answer:**
It is not used if the query uses a variable (parameter) in the predicate, because the optimizer cannot guarantee the filter condition. It must be explicitly used with OPTION (RECOMPILE).

#### 351. 259. How does multiple INNER JOIN syntax work, and what should you watch out for?
**Answer:**
INNER JOIN correlates tables based on a link key, returning only rows where matches exist in both tables. Points to note: 1. Rows without matches are excluded. 2. If link keys are not unique, a Cartesian product effect occurs, duplicating rows based on matches. 3. Linking multiple tables requires each join to satisfy the join condition for the resulting set. 4. Data may appear multiple times if the join keys have one-to-many relationships.

#### 352. 26. Define Full Functional Dependency.
**Answer:**
A condition in which an attribute is functionally dependent on a composite key, but not on any proper subset of that key. If A determines B (A -> B), B is fully functionally dependent on A.

#### 353. 260. How does parameter sniffing occur with variables in SQL queries?
**Answer:**
Using a local variable in a query causes the SQL Server optimizer to ignore the specific value provided at execution time and instead compile a plan based on an 'average' distribution of data, which may lead to suboptimal performance.

#### 354. 261. How does relational algebra handle duplicates?
**Answer:**
In formal relational algebra, sets do not contain duplicates; therefore, duplicates are automatically eliminated unless the operation explicitly specifies otherwise (e.g., multiset operators).

#### 355. 262. How does the BETWEEN operator work in a WHERE clause?
**Answer:**
The BETWEEN operator selects values within a given range (inclusive). For strings, it uses alphabetical order; for numbers, it uses numerical value. The NOT BETWEEN operator selects values outside that range.

#### 356. 263. How does the LIKE operator use wildcards?
**Answer:**
The LIKE clause uses two primary wildcards: '%' (percent), which matches any sequence of characters (including zero characters), and '_' (underscore), which matches exactly one single character.

#### 357. 264. How does the LIKE operator work for pattern matching in SQL?
**Answer:**
The LIKE operator is used for partial string matching. '%' acts as a wildcard representing zero or more characters. 'Herb%' matches strings starting with 'Herb', '%Simpson' matches strings ending with 'Simpson', and '%Bart%' matches strings containing 'Bart'. Omitting wildcards (e.g., LIKE 'Simpson') behaves like equality.

#### 358. 265. How does the Query Optimizer improve a trivial execution plan?
**Answer:**
It uses internal transformation rules to rewrite and optimize the plan.

#### 359. 266. How does the WHERE clause function in SQL?
**Answer:**
The WHERE clause is used to filter records that meet a specified condition. It supports operators such as =, <>, >, <, >=, <=, BETWEEN, LIKE, and IN, and can be combined using AND, OR, and NOT logical operators.

#### 360. 267. How does the cardinality estimator order multiple predicates?
**Answer:**
It orders them based on selectivity, which is the fraction of rows that satisfy a predicate.

#### 361. 268. How does using stored procedures or functions improve security?
**Answer:**
They allow for the abstraction and isolation of underlying data tables, enabling fine-grained control over user access by granting permissions to the procedure rather than the table itself.

#### 362. 269. How is a one-to-one relationship implemented in database design?
**Answer:**
A one-to-one relationship occurs when an entity in one table relates to only one entity in another. It can be implemented as a single table or by using a foreign key that acts as a primary key in a related table.

#### 363. 27. Define Functional Dependency.
**Answer:**
An attribute B is functionally dependent on attribute A if knowing the value of A uniquely determines the value of B, denoted as A -> B.

#### 364. 270. How is cache space for query plans managed?
**Answer:**
It is segmented into tiered levels where the system allocates different percentages of memory based on specific size thresholds.

#### 365. 271. How is cardinality represented in database design?
**Answer:**
Cardinality describes the numerical relationship between entities (e.g., 1:1, 1:N, M:N). It is often visualized in UML or ER diagrams using symbols or numeric ranges (e.g., 0..*, 1..1) to denote optionality and participation constraints.

#### 366. 272. How is existential quantification ("there exists") handled in XQuery?
**Answer:**
Existential quantification is expressed using the 'some' keyword: 'where some $var in $collection satisfies condition'. It returns true if at least one item in the sequence satisfies the specified condition.

#### 367. 273. How is the DROP INDEX statement used?
**Answer:**
The DROP INDEX statement removes an existing index from a table. Syntax varies by engine: 'DROP INDEX index_name ON table_name' (SQL Server) or 'ALTER TABLE table_name DROP INDEX index_name' (MySQL).

#### 368. 274. How is the NULL bitmap size calculated?
**Answer:**
It is 2 bytes plus 1 byte for every 8 nullable columns in the table.

#### 369. 275. How is the closure of attributes computed in functional dependency theory?
**Answer:**
Computing the closure involves iteratively applying Armstrong's axioms (combining and transitive rules) to the set of attributes until no new attributes can be added to the set.

#### 370. 276. How is the duration of an operator calculated in query plans?
**Answer:**
It is calculated as: Time of Close() call - Time of Init() call.

#### 371. 277. How is the level numbering system structured in an index tree?
**Answer:**
The leaf level is defined as level 0, and the root page is assigned the maximum number.

#### 372. 278. How is the variable array stored in a record?
**Answer:**
It stores 2 bytes for the total number of variable columns and includes the end offsets for each non-null variable-length column.

#### 373. 279. How is transaction isolation level scope defined?
**Answer:**
The isolation level is defined per transaction and operates under the 'eye of the beholder' principle, meaning each transaction's read operations must strictly adhere to its specific isolation level requirements.

#### 374. 28. Define SQL.
**Answer:**
Structured Query Language (SQL) is the standard language for relational database management systems. It is used for data manipulation (CRUD), data definition (DDL), and data control (DCL).

#### 375. 280. How is universal quantification expressed in XQuery?
**Answer:**
Universal quantification ("for all") is expressed by checking if every item in a sequence satisfies a specific condition.

#### 376. 281. How large is a Record Identifier (RID)?
**Answer:**
8 bytes.

#### 377. 282. How large is a forwarding pointer?
**Answer:**
16 bytes.

#### 378. 283. How large is a lock structure?
**Answer:**
96 bytes.

#### 379. 284. How large is one quantum in SQL Server scheduling?
**Answer:**
4 ms.

#### 380. 285. How large is the variable-length column array?
**Answer:**
It is 2 bytes plus 2 bytes for each variable-length column present.

#### 381. 286. How many IAM pages exist in SQL Server?
**Answer:**
At least one per GAM extent containing pages of a tracked entity, and at least one per file containing pages of the entity.

#### 382. 287. How many navigation axes exist in XPath?
**Answer:**
There are 13 navigation axes in XPath (e.g., child, parent, descendant, ancestor, etc.).

#### 383. 288. How many pages fit in one Megabyte?
**Answer:**
128 pages (since each page is 8KB).

#### 384. 289. How many primary and unique keys can a table have?
**Answer:**
A table can have only one primary key, but it can have one or more unique keys.

#### 385. 29. Define a 'Query' and 'Query Language' in the context of a DBMS.
**Answer:**
A Query is a request for data manipulation or information issued by a user or application. A Query Language is a declarative language (like SQL) used by the DBMS to interpret and execute these requests.

#### 386. 290. How many rows are in an intermediate index level?
**Answer:**
One for each page of the next lower level in the index tree.

#### 387. 291. How many tempdbs exist on one instance of SQL Server?
**Answer:**
Only one.

#### 388. 292. How many values are tracked in a standard SQL histogram?
**Answer:**
200 steps (values).

#### 389. 293. How many values can be returned by a user-defined function?
**Answer:**
A scalar user-defined function returns exactly one value.

#### 390. 294. How much I/O overhead does a RID lookup cost?
**Answer:**
One I/O normally, or two if a forwarding pointer must be followed.

#### 391. 295. How much data fits on one standard SQL Server data page?
**Answer:**
8,060 bytes.

#### 392. 296. How much memory does SQL Server grant for a variable-length column?
**Answer:**
It typically grants 50% of the declared size.

#### 393. 297. How much overhead does the 'read committed snapshot' isolation option add per row?
**Answer:**
14 bytes per row for the version pointer.

#### 394. 298. How much space do views consume?
**Answer:**
Views consume very little space because the database only stores the definition of the view, not the data it presents.

#### 395. 299. How should database transactions be designed regarding locks?
**Answer:**
Transactions should be designed to execute as quickly as possible to minimize holding locks, thereby reducing contention and preventing deadlocks. They should avoid waiting for human input.

#### 396. 3. Are Views and tables in the same namespace?
**Answer:**
In MySQL, Views and tables share the same namespace.

#### 397. 30. Define a database transaction.
**Answer:**
A transaction is a sequence of one or more SQL operations treated as an atomic unit. It follows ACID properties: changes appear to run in isolation, and if the system fails, all changes are rolled back or committed entirely.

#### 398. 300. How should words in a column name be separated?
**Answer:**
Use underscores (snake_case). While brackets can be used for spaces, it is generally considered a bad practice in database design.

#### 399. 301. How should you correctly identify NULL values in SQL?
**Answer:**
Always use the 'IS NULL' operator to check for null values (e.g., WHERE column IS NULL). Avoid using '= NULL' as it is not standard SQL syntax.

#### 400. 302. How to delete records with empty values in a specific column?
**Answer:**
Use the DELETE statement with an IS NULL condition: DELETE FROM celebs WHERE twitter_handle IS NULL;

#### 401. 303. How to enumerate over a set for multiple values in a query?
**Answer:**
Use the IN operator. For example: SELECT * FROM Employee WHERE FirstName IN ('Lisa', 'David').

#### 402. 304. How to handle NULL values in expressions using functions?
**Answer:**
Use IFNULL() or COALESCE() to return an alternative value if the input expression evaluates to NULL (e.g., COALESCE(column, 0)).

#### 403. 305. How to remove duplicates from a SELECT result set?
**Answer:**
Use the DISTINCT keyword: SELECT DISTINCT column_name FROM table_name.

#### 404. 306. How to sort results by a specific column?
**Answer:**
Use the ORDER BY clause, optionally specifying ASC or DESC: SELECT * FROM movies ORDER BY imdb_rating DESC;

#### 405. 307. If a functional dependency A -> all attributes exists, what is A?
**Answer:**
A is a candidate key for the relation.

#### 406. 308. In MySQL, what keyword allows an automatic view update to ensure modifications appear within the view constraints?
**Answer:**
The 'WITH CHECK OPTION' clause is used in MySQL to ensure that updates or inserts performed through a view remain within the criteria defined by the view's WHERE clause.

#### 407. 309. In Relational Algebra, what is the difference between joining/cross-product and union operators?
**Answer:**
Cross-product and Join operators combine relations horizontally by adding columns/attributes. The Union operator combines relations vertically by adding rows/tuples, requiring compatible schemas.

#### 408. 31. Define common SQL constraints: NOT NULL, UNIQUE, FOREIGN KEY, CHECK, PRIMARY KEY, and DEFAULT.
**Answer:**
NOT NULL: Column cannot store NULL; UNIQUE: Values must be distinct; FOREIGN KEY: Maintains referential integrity; CHECK: Column values must meet a condition; PRIMARY KEY: Unique identifier (NOT NULL + UNIQUE); DEFAULT: Provides a value if none is specified.

#### 409. 310. In SQL Service Broker, what happens if a ROUTE does not define a BROKER_INSTANCE and multiple services share the same name?
**Answer:**
The message is delivered to one of the services randomly, a behavior often used for scaling out.

#### 410. 311. In UML class modeling, what are the alternative terms for subclass and superclass?
**Answer:**
A subclass is also called a 'Specialization', and a superclass is also called a 'Generalization'.

#### 411. 312. In XQuery, what is the difference between 'For' and 'Let'?
**Answer:**
'For' iterates over each element in an expression (like a loop), whereas 'Let' binds the entire result of an expression to a variable at once without iteration.

#### 412. 313. In XSLT, how is the current element referenced?
**Answer:**
The current element is referenced using the '.' character.

#### 413. 314. In a relationship between fruit_table and apple_table where fruit_table is the parent: (1) Which table needs a foreign key? (2) What does it correspond to? (3) Which is the child? (4) How is the relationship described?
**Answer:**
(1,2) apple_table must have a foreign key (e.g., fruit_type) that corresponds to the primary key (id) in fruit_table. (3) apple_table is the child; fruit_table is the parent. (4) fruit_table 'has many' apple_table records.

#### 414. 315. In boolean logic, how do TRUE and FALSE compare, and what is the result of comparing a value with NULL or an UNKNOWN state?
**Answer:**
TRUE is greater than FALSE. Any comparison involving NULL or an UNKNOWN truth value results in an UNKNOWN result.

#### 415. 316. In the context of database system development, what does the functional/application area refer to?
**Answer:**
It refers to specific enterprise activities within an organization, such as marketing, personnel management, and stock control.

#### 416. 317. In the relational model, what determines the domain of values for an attribute?
**Answer:**
Each attribute has an associated data type (e.g., INTEGER, VARCHAR, ENUM) which defines the domain of valid values for that attribute.

#### 417. 318. In which clause can a subquery be used?
**Answer:**
A subquery can be used in many places, most commonly in the WHERE clause, but also in the SELECT, FROM, and HAVING clauses.

#### 418. 319. In which version was the Cardinality Estimator first changed in SQL Server?
**Answer:**
It was updated in SQL Server 2014 (compatibility level 120).

#### 419. 32. Define fifth normal form (5NF).
**Answer:**
A table is in 5NF if it is in 4NF and the relation cannot be reconstructed from simpler relations by a join (i.e., it is non-reducible).

#### 420. 320. Is decomposing a relation into BCNF or 4NF always the best design choice?
**Answer:**
No. While higher normal forms reduce redundancy, they may induce excessive joins, which can be computationally expensive. The ideal design depends on the specific query workload and the trade-off between normalization and performance.

#### 421. 321. Is it always possible to propagate data modifications from a view to the underlying base tables?
**Answer:**
Propagating modifications (inserts, updates, deletes) through a view is only sometimes possible. It is often restricted when the system cannot determine a unique or correct mapping to the underlying rows, leading to ambiguity in how the original relations should be updated.

#### 422. 322. Is it possible to index LOB columns?
**Answer:**
LOB columns cannot be indexed directly as a key column, but they may be included in non-clustered indexes using an 'INCLUDE' clause.

#### 423. 323. Is recursion with aggregation allowed in the SQL standard?
**Answer:**
No, recursion with aggregation is generally disallowed in the SQL standard because it creates ambiguity regarding what the resulting statement should return.

#### 424. 324. Is the BETWEEN clause inclusive or exclusive?
**Answer:**
Inclusive. BETWEEN 'A' AND 'C' includes both A and C.

#### 425. 325. Is the order of clauses in an SQL SELECT statement flexible?
**Answer:**
No, the order of clauses in a SELECT statement is strictly defined (e.g., SELECT, FROM, JOIN, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT) and cannot be changed.

#### 426. 326. Is the splitting rule valid for the left-hand side attributes of functional dependencies?
**Answer:**
No, the splitting rule (decomposition) applies only to the right-hand side of a functional dependency.

#### 427. 327. Jak klasifikovat funkční závislosti A->B?
**Answer:**
Triviální: B je podmnožinou A. Netriviální: B není podmnožinou A. Úplně netriviální: B není podmnožinou A a A a B nemají průnik.

#### 428. 328. Jak se v SQL řadí výsledky?
**Answer:**
K seřazení výsledků se používá klauzule 'ORDER BY'. Pro sestupné řazení se přidává klíčové slovo 'DESC'.

#### 429. 329. Jaký cardinality estimator se použije bez traceflagů?
**Answer:**
Použije se podle nastaveného compatibility levelu databáze.

#### 430. 33. Define first normal form (1NF).
**Answer:**
A relation is in 1NF if it consists of atomic, single-valued attributes, has no repeating groups, and has a primary key identified.

#### 431. 330. Jaký operátor ochrání UPDATE před Halloween problémem?
**Answer:**
Spool operátor, který vytvoří dočasnou kopii dat.

#### 432. 331. Jaký protokol využívá dialog service brokeru?
**Answer:**
TCP/IP pro interdatabázovou komunikaci a přímý insert pro intradatabázovou komunikaci.

#### 433. 332. Jakým způsobem musí být data uspořádaná pro použití merge join?
**Answer:**
Data musí být seřazená podle spojovacích sloupců.

#### 434. 333. Je potřeba u SERVICE specifikovat CONTRACT?
**Answer:**
Ne, není to nutné, ale bez definovaného kontraktu může služba sloužit pouze jako iniciátor dialogu.

#### 435. 334. K čemu potřebují spool operátory memory grant nebo tempdb?
**Answer:**
K uložení mezivýsledku (datasetu) pro jeho opakované čtení nebo zpracování.

#### 436. 335. K čemu využívá hash match operátor memory grant?
**Answer:**
Memory grant se využívá pro vytvoření hash tabulky z tzv. 'build' vstupu. 'Probe' vstup paměť pro operaci nepotřebuje.

#### 437. 336. Kdy mohou být hodnoty rebind a rewind různé od 0?
**Answer:**
Tento stav nastává u vnitřního vstupu operátoru nested loop join.

#### 438. 337. Kdy se použije triviální plán?
**Answer:**
Triviální plán se použije v momentě, kdy optimalizátor vyhodnotí existující plán jako 'good enough' (dostatečně efektivní bez nutnosti hlubokého hledání).

#### 439. 338. Kolik je minimální memory grant?
**Answer:**
Minimální alokace paměti (memory grant) je 1 MB.

#### 440. 339. Kolik je sys.transmission_queue?
**Answer:**
Existuje jedna tabulka sys.transmission_queue na každou databázi.

#### 441. 34. Define fourth normal form (4NF).
**Answer:**
A table is in 4NF if it is in 3NF and contains no multiple independent sets of multivalued dependencies.

#### 442. 340. Kolik je v SQL serveru (S)GAM stránek?
**Answer:**
(S)GAM stránky se nacházejí jednou za 64 000 extentů (cca 4 GB), minimálně však jednou pro každý soubor databáze.

#### 443. 341. Kolik konverzací se vejde na stránku v sys.sysdesend?
**Answer:**
Na jednu stránku v systémové tabulce sys.sysdesend se vejde 144 konverzací.

#### 444. 342. Která tabulka způsobuje contention při odesílání zpráv přes Service Broker?
**Answer:**
Zvýšený contention (spor o prostředky) způsobuje systémová tabulka sys.sysdesend.

#### 445. 343. Která část Query Optimizeru nahrazuje komplikovanější operátory za základní (např. between na >= a <=)?
**Answer:**
Tuto transformaci provádí tzv. Algebraizer.

#### 446. 344. Které jsou tzv. 'Stop & Go' operátory?
**Answer:**
Jedná se o operátory Hash Match (částečně) a Sort, které musí načíst všechna data předtím, než mohou vydat první řádek.

#### 447. 345. Který proces způsobuje náhlé zpomalení procedury, která dříve běžela rychle?
**Answer:**
Jde o 'Parameter Sniffing', kdy dojde k rekompilaci plánu na základě specifických (a nevýhodných) parametrů volání.

#### 448. 346. List 10 valid operators in SQL.
**Answer:**
The following are 10 valid SQL operators: =, !=, >, <, >=, <=, LIKE, BETWEEN, AND, OR.

#### 449. 347. List common RDBMS that use SQL.
**Answer:**
Common RDBMS include MySQL, PostgreSQL, Microsoft SQL Server, Oracle Database, SQLite, and IBM Db2.

#### 450. 348. Name the five aggregate functions.
**Answer:**
The standard aggregate functions are: COUNT(), SUM(), AVG(), MIN(), and MAX().

#### 451. 349. On what type of pages is the PFS (Page Free Space) byte applicable?
**Answer:**
PFS pages track page allocation and free space, primarily applicable to heap table pages in SQL Server.

#### 452. 35. Define linear vs. non-linear recursion in SQL.
**Answer:**
Linear recursion refers to a recursive CTE where there is only one reference to the recursive relation R within the definition. Non-linear recursion occurs when there is more than one reference to the recursive relation R, such as joining R with itself.

#### 453. 350. Pravidlo pro klíče v relaci
**Answer:**
Pokud je A klíčem relace R(A, B, C), pak každá nadmnožina A (např. AB, AC, ABC) je rovněž kandidátním klíčem.

#### 454. 351. Provide an example of a multiple filter BETWEEN statement in SQL.
**Answer:**
SELECT * FROM movies WHERE year BETWEEN 1990 AND 2000 AND genre = 'comedy';

#### 455. 352. Provide examples for aggregate functions COUNT(), AVG(), and SUM().
**Answer:**
SELECT COUNT(ProductID) FROM Products; SELECT AVG(Price) FROM Products; SELECT SUM(Quantity) FROM OrderDetails;

#### 456. 353. Provide examples of basic CRUD and schema modification operations using the Clients table.
**Answer:**
Filtering: 'SELECT * FROM Clients WHERE City = 'Springfield''; Updating: 'UPDATE Clients SET City = 'Springfield' WHERE Cname LIKE '%herb%';' (Note: Always use a WHERE clause to avoid mass updates); Altering: 'ALTER TABLE Clients ADD Comments nvarchar(400) NULL;'

#### 457. 354. S čím souvisí rozhodnutí použít materializované pohledy (materialized views)?
**Answer:**
Rozhodnutí je otázkou kompromisu mezi rychlostí čtení (query) a režií při zápisu (update), podobně jako u indexů.

#### 458. 355. SQL Aggregation Functions (MIN, MAX)
**Answer:**
MIN() returns the smallest value in a column, while MAX() returns the largest value. These functions are typically used in SELECT statements to perform calculations on datasets, often paired with GROUP BY.

#### 459. 356. SQL Constraints: PRIMARY KEY and NOT NULL
**Answer:**
PRIMARY KEY uniquely identifies each record, must contain UNIQUE values, and cannot be NULL. A table can have only one primary key, which can consist of multiple columns. NOT NULL ensures a column cannot hold NULL values, requiring a value for every entry.

#### 460. 357. SQL INSERT INTO SELECT Statement
**Answer:**
The INSERT INTO SELECT statement copies data from a source table and inserts it into a target table. It requires that data types match. Existing records in the target table are unaffected. You can apply filters with a WHERE clause to copy only specific subsets of data.

#### 461. 358. SQL INSERT INTO Statement
**Answer:**
The INSERT INTO statement adds new records to a table. You can specify columns: INSERT INTO table_name (col1, col2) VALUES (val1, val2); or insert into all columns by omitting names, provided the values follow the table's defined column order.

#### 462. 359. SQL JOINs: INNER, LEFT, RIGHT, and FULL
**Answer:**
A JOIN clause is used to combine rows from two or more tables based on a related column between them. (INNER) JOIN: Returns records with matching values in both tables. LEFT (OUTER) JOIN: Returns all records from the left table and matched records from the right. RIGHT (OUTER) JOIN: Returns all records from the right table and matched records from the left. FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table.

#### 463. 36. Define second normal form (2NF).
**Answer:**
A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the entire primary key (no partial dependencies).

#### 464. 360. SQL LIKE Operator and Wildcards
**Answer:**
The LIKE operator is used in a WHERE clause to search for patterns. Wildcards: '%' represents zero, one, or multiple characters; '_' represents a single character. Combined with LIKE, these allow for flexible string matching, such as starting/ending characters or containing substrings.

#### 465. 361. SQL NULL Values and Handling
**Answer:**
A NULL value represents missing or unknown data. Arithmetic operations involving NULL usually result in NULL. To handle these, functions like ISNULL(), IFNULL(), COALESCE(), or NVL() are used to provide default values during query processing.

#### 466. 362. SQL Programmability: Views and Triggers
**Answer:**
Views: 'CREATE [MATERIALIZED] VIEW [name] AS [query]' creates a virtual table. Triggers: 'CREATE TRIGGER [name] ...' defines procedural logic that executes automatically in response to specific events (INSERT, UPDATE, DELETE) on a table.

#### 467. 363. SQL Recursive Queries (WITH)
**Answer:**
Recursive CTEs (using WITH RECURSIVE) allow for unbounded computations, such as traversing hierarchical data (e.g., org charts or ancestor trees). They stop when an iteration produces no new results. Negatively dependent recursion and aggregation within recursion are generally disallowed in standard SQL.

#### 468. 364. SQL SELECT INTO Statement
**Answer:**
The SELECT INTO statement copies data from a source table into a new table. The new table is created with the schema (column names and types) of the source data. It is often used for backups or creating subsets of data.

#### 469. 365. SQL Self JOIN
**Answer:**
A self-join is a regular join where a table is joined with itself. It is often used to compare rows within the same table. To avoid cross-product duplicates (e.g., Amy/Doris and Doris/Amy), use an inequality operator (e.g., '<' or '>') in the WHERE clause instead of '<>'.

#### 470. 366. SQL TOP/LIMIT/ROWNUM
**Answer:**
These clauses limit the number of records returned by a query. Syntax varies by vendor: SQL Server uses TOP, MySQL/PostgreSQL use LIMIT, and Oracle historically uses ROWNUM or FETCH FIRST.

#### 471. 367. TCL
**Answer:**
Transaction Control Language: A subset of SQL commands used to manage transactions in the database (e.g., COMMIT, ROLLBACK, SAVEPOINT).

#### 472. 368. Tell me the top downloaded app.
**Answer:**
SELECT MAX(downloads) FROM fake_apps;

#### 473. 369. The EXCEPT operator can be practically replaced by what?
**Answer:**
The EXCEPT operator can be replaced using subqueries with the 'IN' or 'NOT IN' operators, or by using 'LEFT JOIN' combined with a 'WHERE...IS NULL' filter to identify records present in one set but not the other.

#### 474. 37. Define the Query Executor (QE) in a database engine.
**Answer:**
The Query Executor is the part of the relational engine that takes a generated execution plan and executes it by interacting with the storage engine.

#### 475. 370. True or False: A PRIMARY KEY can consist of more than one column.
**Answer:**
True. This is known as a composite primary key.

#### 476. 371. True or False: The BETWEEN operator behaves identically across all database systems.
**Answer:**
False. Implementations vary; some databases include both boundary values, while others may exclude one or both. Always check specific vendor documentation.

#### 477. 372. What SQL clause hosts set operators like IN, ANY/ALL, and (NOT) EXISTS?
**Answer:**
These operators are used within the WHERE clause to perform comparisons against sets of values or results of subqueries.

#### 478. 373. What SQL commands are used to filter result sets?
**Answer:**
Common commands for filtering include: SELECT DISTINCT, WHERE, LIMIT, BETWEEN, LIKE, and ORDER BY.

#### 479. 374. What anomalies occur in unnormalized relations?
**Answer:**
1. Insertion Anomaly: Cannot store data without other unrelated data. 2. Deletion Anomaly: Deleting one record causes unintended loss of other data. 3. Update Anomaly: Redundant data must be updated in multiple places, risking inconsistency.

#### 480. 375. What are Cubes and OLAP?
**Answer:**
OLAP (Online Analytical Processing) is a category of software for multi-dimensional data analysis. An OLAP Cube is a data structure that allows for fast analysis of data by organizing it into dimensions (attributes) and measures (quantitative values) for rapid reporting.

#### 481. 376. What are DBCC commands in T-SQL?
**Answer:**
DBCC stands for Database Console Command. It is a suite of diagnostic and maintenance commands used to check database integrity, manage query plan caches, and debug performance via trace flags.

#### 482. 377. What are DMVs (Dynamic Management Views)?
**Answer:**
DMVs are internal server objects (views and functions) used to monitor the current state of the database engine, perform diagnostics, and troubleshoot performance issues.

#### 483. 378. What are INSTEAD OF triggers?
**Answer:**
INSTEAD OF triggers are executed in place of the original DML statement (INSERT, UPDATE, or DELETE). They are commonly used to update views that are not directly updatable.

#### 484. 379. What are Integrity Constraints?
**Answer:**
Integrity constraints are rules used to impose semantic restrictions on data, ensuring data accuracy and consistency, rather than just basic type restrictions.

#### 485. 38. Define the Query Optimizer (QO) and its objective.
**Answer:**
The Query Optimizer is a part of the relational engine that takes an algebraizer tree and produces an execution plan. It aims to produce a 'good enough' plan rather than necessarily the absolute fastest or smallest one.

#### 486. 380. What are LOBs (Large Objects) and LOB pages in a database?
**Answer:**
LOBs (Large Objects) are data types used to store large amounts of data (e.g., text, images). LOB pages are internal storage pages specifically allocated for variable-length data types marked as MAX.

#### 487. 381. What are Magic Tables (Inserted/Deleted) in SQL Server?
**Answer:**
Magic tables are virtual tables available only within triggers. The 'INSERTED' table holds the new values during INSERT or UPDATE, and the 'DELETED' table holds the old values during DELETE or UPDATE operations.

#### 488. 382. What are Physical Design Advisors?
**Answer:**
They are automated tools used to analyze query workloads and suggest the optimal set of indexes to improve database performance.

#### 489. 383. What are ROLLUP and CUBE in T-SQL?
**Answer:**
ROLLUP and CUBE are grouping set extensions used with the GROUP BY clause to generate summarized aggregations, hierarchical totals, and multi-dimensional analysis for auditing and reports.

#### 490. 384. What are SQL Aliases?
**Answer:**
Aliases are temporary names assigned to tables or columns for the duration of a query. They are used to improve readability, handle column name conflicts in joins, or represent calculated fields.

#### 491. 385. What are SQL Compound Operators?
**Answer:**
Compound operators perform a mathematical operation and an assignment simultaneously (e.g., += for addition, -= for subtraction, *= for multiplication, /= for division, %= for modulo, etc.).

#### 492. 386. What are SQL Wildcards?
**Answer:**
Wildcards are used with the LIKE operator to search for specific patterns in strings. '%' represents zero or more characters, and '_' represents a single character. Specific implementations (like SQL Server or Access) also support character lists using square brackets like [a-c] or [!charlist].

#### 493. 387. What are SQL constraints and why are they used?
**Answer:**
SQL constraints are rules applied to columns or tables that limit the type of data that can be stored. They ensure data accuracy, reliability, and integrity. Constraints can be defined during table creation (CREATE TABLE) or modified later (ALTER TABLE). If a data action violates a constraint, the action is aborted.

#### 494. 388. What are SQL constraints and why are they used?
**Answer:**
Constraints enforce rules on data in a table, ensuring accuracy and reliability. Common types include NOT NULL, CHECK, DEFAULT, UNIQUE, PRIMARY KEY, and FOREIGN KEY. They can be applied at the column level or the table level.

#### 495. 389. What are SQL data types?
**Answer:**
Data types define the kind of value a column can hold (e.g., integer, character, date, binary). They ensure that the database understands how to interpret and interact with the stored data. Developers must select appropriate data types during table creation, noting that syntax and storage size may vary between database systems.

#### 496. 39. Define the following SQL DDL and DML commands: CREATE DATABASE, CREATE TABLE, CREATE INDEX, DROP TABLE, SELECT, INSERT INTO, UPDATE, and ALTER DATABASE.
**Answer:**
CREATE DATABASE: Creates a new database. CREATE TABLE: Creates a new table. CREATE INDEX: Creates an index for faster lookups. DROP TABLE: Deletes a table. SELECT: Extracts data. INSERT INTO: Adds new data. UPDATE: Modifies existing data. ALTER DATABASE: Modifies database structure/settings.

#### 497. 390. What are SQL parameters and why are they important?
**Answer:**
SQL parameters are values added to a query at execution time in a controlled manner. They are the primary defense against SQL injection attacks.

#### 498. 391. What are approximate numeric data types used for?
**Answer:**
Approximate numeric data types (like FLOAT or REAL) are used to store floating-point numbers that do not have an exact decimal representation, useful for scientific calculations where extreme precision is not required.

#### 499. 392. What are column constraints and common examples?
**Answer:**
Column constraints are rules enforced on data values. Examples include: PRIMARY KEY (uniqueness/identity), UNIQUE (no duplicates), NOT NULL (required value), and DEFAULT (fallback value).

#### 500. 393. What are common DBCC commands for query tuning and debugging?
**Answer:**
Key commands include: 'DBCC FREEPROCCACHE' to clear the plan cache; 'DBCC TRACEON(XYZ)' to enable specific trace flags (add '-1' to apply globally); 'DBCC TRACEON(3604)' to route output to the session window; 'DBCC HELP' to view documentation; and 'DBCC OPTIMIZER_WHAT_IF' to test optimizer behavior under hypothetical conditions.

#### 501. 394. What are common SQL Server trace flags for performance tuning?
**Answer:**
Traceflag 174: Increases cached plan count. 2312: Forces current cardinality estimator. 3604: Sends output to session window. 7471: Uses UPD lock for UPDATE STATISTICS. 8649: Forces parallelism. 8780: Increases query compilation transformation limits. 9481: Forces legacy cardinality estimator.

#### 502. 395. What are common database design anomalies?
**Answer:**
Redundancy (storing data multiple times), Update anomaly (inconsistent data updates), and Deletion anomaly (inadvertently losing data when deleting unrelated attributes).

#### 503. 396. What are common date and time functions for constructing or calculating dates?
**Answer:**
DATEFROMPARTS(y,m,d) constructs a date, DATETIMEFROMPARTS(...) constructs a datetime, DATEDIFF(part, start, end) calculates the difference between two dates, DATEADD(part, num, date) adds an interval to a date, and ISDATE(value) validates if a string is a valid date.

#### 504. 397. What are common date and time functions for extracting parts of a date?
**Answer:**
Common functions include: GETDATE() (current timestamp), DATEPART(part, date) (returns specific part), DAY(date), MONTH(date), and YEAR(date).

#### 505. 398. What are common pattern matching and range operators in SQL?
**Answer:**
The LIKE operator uses '%' to match any sequence of characters and '_' to match exactly one character. The NOT LIKE operator negates the condition. The BETWEEN operator is used to filter values within a specific inclusive range.

#### 506. 399. What are common problems with file-based storage compared to databases?
**Answer:**
Common problems include: lack of data structure (chaos), redundant storage, difficulties with concurrent multi-user access, and gaps in data security or access management.

#### 507. 4. Are all database views updateable?
**Answer:**
No, not all views are updateable. Views that involve complex aggregations, joins, or certain set operators may be read-only because the database engine cannot map changes back to the underlying base tables unambiguously.

#### 508. 40. Define the relationship between a foreign key and a primary key.
**Answer:**
A foreign key is a field (or collection of fields) in one table that uniquely identifies a row of another table by pointing to its primary key.

#### 509. 400. What are common psql utility commands for session management?
**Answer:**
\c (connect to database), \password (change user password), \conninfo (connection details), \q (quit), \? (list all commands).

#### 510. 401. What are critical considerations for a Business Intelligence (BI) project?
**Answer:**
Important factors include historical data availability, distribution methods (PDF, email), frequency of updates, data latency requirements, business logic/transformation rules, and security/access restrictions.

#### 511. 402. What are database constraints and why are they used?
**Answer:**
Constraints are rules or types applied to table columns that restrict the data being entered. They are essential for ensuring data integrity and consistency within the database.

#### 512. 403. What are domain, field, and NULL constraints?
**Answer:**
A domain constraint defines the set of legal values for a column. A field (column) holds specific information for a record. A NULL value represents the absence of data, which is distinct from a zero or empty space.

#### 513. 404. What are general database assertions?
**Answer:**
General assertions are a SQL standard feature used to enforce integrity constraints across the database. They can be assimilated to materialized views but are notably not implemented in most modern DBMS.

#### 514. 405. What are incremental statistics?
**Answer:**
Incremental statistics refer to a performance optimization where database statistics are updated only for the newest partition of a partitioned table rather than re-scanning the entire table.

#### 515. 406. What are insertion, update, and deletion anomalies?
**Answer:**
These occur due to poor schema design (redundancy). Insertion: cannot add data without other data. Update: redundant data requires multiple updates. Deletion: removing a record accidentally deletes unrelated information. Normalization helps resolve these.

#### 516. 407. What are non-page latches typically used for?
**Answer:**
Non-page latches are typically used to protect metadata pages or other internal memory structures in a database engine.

#### 517. 408. What are precision and scale in the context of SQL data types?
**Answer:**
Precision and scale are characteristics of exact numeric data types (such as DECIMAL or NUMERIC). Precision is the total number of digits, while scale is the number of digits to the right of the decimal point.

#### 518. 409. What are primary and foreign keys?
**Answer:**
A primary key is a column or set of columns that uniquely identifies a row in a table (must be unique and non-NULL). A foreign key is a column or set of columns that establishes a link between data in two tables by referencing the primary key of another table.

#### 519. 41. Define the terms 'data', 'information', 'database', and 'DBMS'.
**Answer:**
Data refers to raw facts. Information is data processed to have meaning. A database is a set of logically related data (including metadata). A DBMS is the software that manages database structures and controls data access.

#### 520. 410. What are some common types of non-relational (NoSQL) databases?
**Answer:**
Common types include Key-value databases, Document databases, and Graph databases.

#### 521. 411. What are some standard SQL data types?
**Answer:**
Standard SQL data types include character strings (CHAR, VARCHAR), numeric types (INT, FLOAT, REAL, DECIMAL), and temporal types (DATE, TIME).

#### 522. 412. What are sql_statement_starting/completed/recompile in Extended Events?
**Answer:**
These are events used in SQL Server's Extended Events framework to track the lifecycle of ad-hoc queries or stored procedure executions, useful for performance monitoring and debugging.

#### 523. 413. What are tables in the context of a database?
**Answer:**
Tables are named database objects organized into rows and columns used to store data.

#### 524. 414. What are temporary tables and how do local differ from global ones?
**Answer:**
Temporary tables are storage structures for intermediate data. Local temp tables (#name) are private to the current connection and drop upon disconnection. Global temp tables (##name) are visible to all sessions and drop only when all referencing connections are closed.

#### 525. 415. What are the ACID properties in a database?
**Answer:**
ACID properties ensure reliable transaction processing: Atomicity (all or nothing), Consistency (maintains integrity rules), Isolation (prevents concurrent transaction interference), and Durability (committed data survives crashes).

#### 526. 416. What are the ACID properties in a database?
**Answer:**
ACID is an acronym for the four key properties of a transaction: Atomicity (all operations succeed or the entire transaction is rolled back), Consistency (the database remains in a valid state), Isolation (transactions occur independently), and Durability (committed changes persist despite system failures).

#### 527. 417. What are the ACID properties of database transactions?
**Answer:**
ACID stands for Atomicity (all or nothing), Consistency (valid state transitions), Isolation (independent transactions), and Durability (persisted after commitment).

#### 528. 418. What are the ACID properties of database transactions?
**Answer:**
Atomicity (all or nothing), Consistency (maintaining valid state), Isolation (transactions don't interfere), and Durability (permanent changes once committed).

#### 529. 419. What are the AND and OR operators in SQL?
**Answer:**
AND displays a record if both conditions are true. OR displays a record if either condition is true.

#### 530. 42. Define third normal form (3NF).
**Answer:**
A table is in 3NF if it is in 2NF and no non-key attribute is functionally dependent on another non-key attribute (no transitive dependencies).

#### 531. 420. What are the GRANT and REVOKE statements used for?
**Answer:**
The GRANT statement is used by an owner to grant specific privileges to a user, while the REVOKE statement is used to remove those privileges.

#### 532. 421. What are the SQL statements used to modify table data?
**Answer:**
The three statements for modifying content are: INSERT, UPDATE, and DELETE.

#### 533. 422. What are the SQL wildcards for pattern matching?
**Answer:**
The underscore (_) is a substitute for a single character, and the percent sign (%) is a substitute for zero or more characters.

#### 534. 423. What are the advantages and disadvantages of using Stored Procedures?
**Answer:**
Advantages: They support modular programming, allow code reuse, reduce network traffic, and provide better security. Disadvantages: They can only be executed within the database engine and consume additional memory on the database server.

#### 535. 424. What are the advantages of non-linear recursion versus linear recursion?
**Answer:**
Non-linear recursion can produce cleaner queries and converges faster (logarithmic vs linear). However, it is harder to implement, and many DBMS (including standard SQL) primarily support linear recursion.

#### 536. 425. What are the advantages of using Cursors?
**Answer:**
Cursors allow for row-by-row processing, which is useful for complex row-wise validation or logic. They can return the first few rows before a full result set is assembled, potentially improving perceived response time, and they can offer better concurrency control in specific scenarios where manual updates are required, though they often come with higher performance overhead compared to set-based operations.

#### 537. 426. What are the basic CRUD operations in SQL?
**Answer:**
The basic operations are: INSERT (create/add rows), SELECT (retrieve/read rows), UPDATE (modify values in existing rows), and DELETE (remove rows).

#### 538. 427. What are the basic constructs of XML?
**Answer:**
XML consists of nested tagged elements, attributes, and text content.

#### 539. 428. What are the basic constructs used in XPath?
**Answer:**
They include: '/' (root/separator), 'name' (match element), '*' (wildcard), '@attr' (attribute), '//' (descendant), '[condition]' (filtering), and '[index]' (positional index).

#### 540. 429. What are the benefits of using a database view?
**Answer:**
Views protect columns/rows to enhance security, simplify complex database structures to make queries easier to write, allow for different data representations, and provide data independence (logical decoupling from base tables). Views may be virtual and recreated each time they are referenced.

#### 541. 43. Describe the basic components of a relational database structure.
**Answer:**
A database contains a set of relations (tables), which are defined by a schema (name and columns). This schema is instantiated with a set of tuples (rows).

#### 542. 430. What are the best practices for choosing database data types?
**Answer:**
Choose smaller data types where possible, keep types simple, and avoid NULL values if the business logic allows.

#### 543. 431. What are the characteristics of the decimal(p, s) data type in MS SQL?
**Answer:**
Decimal(p, s) defines precision (p) as the total number of digits and scale (s) as the number of digits to the right of the decimal point. For example, 22342.33 is decimal(18,2).

#### 544. 432. What are the commands to manage access privileges?
**Answer:**
Since database objects have an owner, privileges are managed using the GRANT (to provide access) and REVOKE (to remove access) statements.

#### 545. 433. What are the common PostgreSQL CLI meta-commands?
**Answer:**
\h provides help, \c connects to a database, \x toggles expanded (vertical) display, \df lists functions (can be filtered, e.g., \df *name*), and \dn lists schemas.

#### 546. 434. What are the common Relational Algebra operators?
**Answer:**
Projection: selects specific columns; Rename (Rho): changes names of relations or attributes; Cross-product: combines all rows from both relations; Natural Join: combines relations based on equality of all common attribute names.

#### 547. 435. What are the common SQL aggregate functions?
**Answer:**
AVG: returns the average value of a column. COUNT: counts the number of rows. MAX: returns the highest value. MIN: returns the lowest value. SUM: returns the total sum of values.

#### 548. 436. What are the common SQL constraints used to maintain data integrity?
**Answer:**
SQL constraints specify rules for data in a table. A Foreign Key is a specific constraint used to prevent actions that would destroy links between tables.

#### 549. 437. What are the common SQL date and time types?
**Answer:**
The five common types are: DATE, TIME, DATETIME, TIMESTAMP, and YEAR.

#### 550. 438. What are the common anomalies that occur in unnormalized relations?
**Answer:**
The common anomalies are: Insert Anomaly (cannot add data without other required fields), Delete Anomaly (losing related data when deleting a record), and Change (Update) Anomaly (redundant data leading to inconsistency).

#### 551. 439. What are the common categories of data?
**Answer:**
Common data categories include: Personally Identifiable Information (PII), Business data, Operational data, Geo/Spatial data, and Time-series data.

#### 552. 44. Describe the different types of SQL Joins.
**Answer:**
INNER JOIN: Returns rows when there is a match in both tables. LEFT JOIN: Returns all rows from the left table and matched rows from the right. RIGHT JOIN: Returns all rows from the right table and matched rows from the left. FULL JOIN: Returns all rows when there is a match in either of the tables.

#### 553. 440. What are the common commands in the SQLite CLI to manage tables and schemas?
**Answer:**
.tables (list tables), .schema (show table/database structure).

#### 554. 441. What are the common complications and constraints associated with using aggregations in SQL?
**Answer:**
Aggregation can cause complications such as introducing ambiguity (e.g., in recursive CTEs) and making views non-updatable if they contain aggregate functions.

#### 555. 442. What are the common drawbacks of using XSLT?
**Answer:**
1. Ambiguity resolution: Priority is given to the most specific rule or the latest defined rule. 2. Weird whitespace handling (e.g., entity escaping requirements).

#### 556. 443. What are the common referential actions for foreign keys?
**Answer:**
CASCADE: Deletes child rows when the parent row is deleted. NO ACTION: No operation is performed, potentially causing an error if constraints are violated. RESTRICT: Prevents deletion of a parent row if associated child rows exist. SET NULL: Sets foreign key columns in the child table to NULL when the parent row is deleted.

#### 557. 444. What are the common schema descriptor languages for XML?
**Answer:**
The most common are Document Type Definition (DTD) and XML Schema Definition (XSD), with XSD being the more powerful and feature-rich standard.

#### 558. 445. What are the common strategies for translating UML subclasses into relations?
**Answer:**
1. Subclass relations contain superclass key + specialized attributes. 2. Subclass relations contain all attributes (including inherited ones). 3. One single relation containing all superclass and subclass attributes (using nulls for missing values).

#### 559. 446. What are the common string manipulation functions in SQL (LEN, LEFT, RIGHT, SUBSTRING, CHARINDEX, CONCAT, REPLACE, STUFF, LTRIM, RTRIM)?
**Answer:**
These are essential string functions: LEN (length of string), LEFT/RIGHT (extract part from sides), SUBSTRING (extract part based on start and length), CHARINDEX (find starting position of a character/string), CONCAT (merge strings), REPLACE (find and replace substrings), STUFF (replace a part based on position), and LTRIM/RTRIM (remove whitespace).

#### 560. 447. What are the common transaction isolation levels?
**Answer:**
The standard isolation levels include Read Uncommitted, Read Committed, Repeatable Read, and Serializable. Additionally, some systems implement Read Only for optimization purposes.

#### 561. 448. What are the common tricky issues associated with database triggers?
**Answer:**
Key issues include: the chaining and termination problem (infinite loops), ambiguity in order of execution for multiple triggers, complexity of conditions (WHEN vs. inside the action), and the difference between row-level vs. statement-level execution.

#### 562. 449. What are the common types of SQL joins and how do they function?
**Answer:**
Inner Join: Returns rows where there is a match in both tables. Left Join: Returns all rows from the left table and the matched rows from the right table (unmatched right rows result in NULL). Right Join: Returns all rows from the right table and the matched rows from the left table (unmatched left rows result in NULL). Full Join: Returns all rows when there is a match in either the left or right table; non-matching side results in NULL.

#### 563. 45. Describe your experience as a SQL Server DBA.
**Answer:**
This is a behavioral interview question. You should discuss the specific SQL Server versions managed, your experience with instance administration (backups, security, disaster recovery), performance tuning, and how your responsibilities directly contributed to project goals and business stability.

#### 564. 450. What are the components of a referential action?
**Answer:**
A referential action is defined by two parts: an event (e.g., DELETE, UPDATE) and an action (e.g., CASCADE, SET NULL, RESTRICT).

#### 565. 451. What are the core characteristics of NoSQL databases?
**Answer:**
Document stores hold semi-structured data; Key-Value stores map unique keys to values (often used for fast lookups); Graph databases represent data as nodes and edges; MapReduce is a programming model for processing massive datasets in parallel, though joins are not natively supported and often require higher-level abstractions like Hive or Pig.

#### 566. 452. What are the core characteristics of a parameter in SQL?
**Answer:**
A parameter in SQL is defined by its name and its specific data type.

#### 567. 453. What are the core components of a database table?
**Answer:**
A table consists of Column Names (the header), Rows (individual records), Values (data stored in cells), and NULL values (representing missing or unknown data).

#### 568. 454. What are the core components of the Relational Engine?
**Answer:**
The relational engine is comprised of the Query Processor, which includes the Language Processing/Parser, the Query Optimizer (which determines the execution plan), and the Query Executor (which runs the plan).

#### 569. 455. What are the core datatypes in SQLite?
**Answer:**
SQLite uses four primary storage classes: INTEGER (whole numbers), REAL (floating point/decimal), TEXT (alphanumeric strings), and BLOB (binary data). Other types (like INT or DOUBLE) are mapped to these four.

#### 570. 456. What are the core elements of SQL?
**Answer:**
SQL is categorized into: DDL (Data Definition Language - schema), DML (Data Manipulation Language - data), and DCL (Data Control Language - security).

#### 571. 457. What are the core features of a Database Management System (DBMS)?
**Answer:**
Key features include data integrity, multi-user access control, backup and recovery, high availability, centralized data management, and standardized languages/APIs for data access.

#### 572. 458. What are the core functions of a relational database as defined by Edgar Codd?
**Answer:**
These include non-redundant data management, CRUD operations, metadata catalogs, multi-user views, data consistency/integrity, security, transaction management, concurrency, and crash recovery.

#### 573. 459. What are the desirable properties of decomposition?
**Answer:**
Attribute preservation, dependency preservation, and lossless decomposition.

#### 574. 46. Difference between actual and estimated execution plan in SSMS?
**Answer:**
An estimated execution plan is generated without executing the query and does not recompile outdated statistics, whereas an actual plan is generated by executing the query, reflecting real-time performance data and current statistics.

#### 575. 460. What are the disadvantages of failing to normalize a database?
**Answer:**
Failure to normalize leads to data redundancy (wasted space) and data inconsistency (update anomalies where changes are not applied across all duplicate records, violating integrity).

#### 576. 461. What are the disadvantages of using Cursors in SQL?
**Answer:**
Cursors are memory-intensive as they create a temporary work area in system memory. They often lead to performance degradation due to iterative row-by-row processing, which causes excessive network round trips compared to set-based operations (SELECT/UPDATE/DELETE).

#### 577. 462. What are the downsides of using indexes?
**Answer:**
Indexes require additional storage space and impose overhead during data modifications (INSERT, UPDATE, DELETE) because the index must be maintained. High-frequency updates can significantly degrade write performance.

#### 578. 463. What are the four main types of integrity constraints?
**Answer:**
The four main types are: Domain constraints, Entity integrity, Referential integrity, and General constraints (or check constraints).

#### 579. 464. What are the four possible referencing-variables available in database triggers?
**Answer:**
The four referencing-variables are: old row (only in row-level statements), old table, new row (only in row-level statements), and new table. Row-level statements are defined as 'FOR EACH ROW'.

#### 580. 465. What are the fundamental CRUD statements for a table?
**Answer:**
CREATE TABLE (defines structure), INSERT INTO (adds rows), SELECT (retrieves data), UPDATE (modifies data), DELETE (removes data), and DROP TABLE (deletes the table structure).

#### 581. 466. What are the fundamental characteristics of Relational databases?
**Answer:**
Relational databases store data in two-dimensional tables consisting of rows and columns. They are based on relational algebra and set theory, using formal operations to retrieve and manipulate information.

#### 582. 467. What are the ideal conditions for a Nested Loop join operator?
**Answer:**
It is most efficient when the outer input has a small number of rows and the inner input has a low-cost subtree (often indexed).

#### 583. 468. What are the inputs of a Hash Match operator?
**Answer:**
The top input is the 'build' input, and the bottom input is the 'probe' input.

#### 584. 469. What are the key best practice guidelines for database index design?
**Answer:**
- **Search by text prefix:** Use trailing wildcard `LIKE 'text%'`.



- **Multi-column queries:** Follow the ESR Rule (`Equality -> Sort -> Range`).



- **High-performance APIs:** Use Covering Indexes for frequent `SELECT` queries.



- **Avoid N+1 DB roundtrips:** Use Materialized Path or Eager Loading.

#### 585. 47. Difference between execution plan and query plan?
**Answer:**
A query plan is the abstract logical/physical strategy generated by the optimizer. An execution plan includes the query plan combined with the actual execution context, such as runtime statistics, parameter values, and literal constants.

#### 586. 470. What are the main components of an ERD (Entity Relationship Diagram)?
**Answer:**
An ERD consists of Entities, their Attributes, and the relationships (often defined by foreign keys) between them.

#### 587. 471. What are the main elements/components of a database?
**Answer:**
A database contains schemas. A schema is a container used to group database objects. Within a schema, there are Tables (with typed columns), Views (named stored queries), Stored Procedures (precompiled SQL code), and other objects.

#### 588. 472. What are the main string data types in MS SQL and their primary characteristics?
**Answer:**
The main string types are 'varchar' and 'nvarchar'. 'nvarchar' supports Unicode characters. The length (e.g., nvarchar(10), nvarchar(max)) defines the storage capacity. Length is determined by the number of characters, not bytes.

#### 589. 473. What are the main types of table relationships?
**Answer:**
One-to-One (1:1), where each record in Table A matches only one in Table B; One-to-Many (1:M), where one record in Table A matches multiple in Table B; and Many-to-Many (M:N), requiring a junction table.

#### 590. 474. What are the mandatory clauses in a SELECT statement?
**Answer:**
The SELECT and FROM clauses are mandatory.

#### 591. 475. What are the maximum limits for index keys in SQL Server?
**Answer:**
The maximum index key size is 900 bytes for versions before SQL Server 2016, and 1700 bytes for 2016 and later. The maximum number of columns is 16 and 32, respectively.

#### 592. 476. What are the most basic elements/objects of a relational database?
**Answer:**
Tables are the primary objects. Key components include: Column names (table headers), Rows (records), Values (conforming to defined data types), and NULL values (representing missing or empty information).

#### 593. 477. What are the options for maintaining Referential Integrity when a primary key is modified?
**Answer:**
Referential integrity actions include: CASCADE (updates/deletes changes in referenced rows), SET NULL (sets foreign keys to NULL), SET DEFAULT (sets foreign keys to a default value), RESTRICT (prevents the change), and NO ACTION (allows the change without cascading).

#### 594. 478. What are the parts of a PL/SQL block?
**Answer:**
A PL/SQL block consists of an optional declaration part, a mandatory executable part, and an optional exceptions (handling) part.

#### 595. 479. What are the phases of the Database Life Cycle in sequence?
**Answer:**
1. Scoping, 2. Conceptual Database Design, 3. Relational Database Design, 4. Normalization, 5. Physical Database Design.

#### 596. 48. Difference between index rebuild and reorganize?
**Answer:**
An index rebuild drops and creates the index from scratch, defragmenting all pages. An index reorganize is an online operation that simply rearranges the existing leaf-level pages into a logical order.

#### 597. 480. What are the phases of the Database Life Cycle?
**Answer:**
The phases are: 1. Scoping, 2. Conceptual Database Design, 3. Relational Database Design, 4. Normalization, and 5. Physical Database Design.

#### 598. 481. What are the physical implications of data modification on indexes and pages?
**Answer:**
When a row in a clustered index is updated and exceeds page space, a page split occurs. If a row with a forwarding pointer is moved again, the forwarding pointer is updated to reflect the new location. Additionally, non-clustered indexes are typically not rebuilt when the underlying clustered index is rebuilt.

#### 599. 482. What are the possible states of a worker thread in a database engine?
**Answer:**
The typical states for a worker thread are: running, runnable (waiting for a processor), and suspended (waiting for a resource).

#### 600. 483. What are the primary PostgreSQL command-line (psql) shortcuts to list database objects?
**Answer:**
\l (databases), \d or \d+ (tables), \dn or \dn+ (schemas), \df (functions), \du (users).

#### 601. 484. What are the primary SQL DDL commands?
**Answer:**
DDL includes CREATE, ALTER, and DROP commands for Schemas, Tables, Views, and Domains.

#### 602. 485. What are the primary SQL commands used to modify the contents of a database table?
**Answer:**
The commands INSERT (add new rows), UPDATE (modify existing rows), and DELETE (remove rows) are used to manipulate the data stored within a database table.

#### 603. 486. What are the primary data types supported by PostgreSQL?
**Answer:**
Boolean, Character (CHAR, VARCHAR, TEXT), Numeric (INT, SERIAL, NUMERIC, REAL), Temporal (DATE, TIME, TIMESTAMP, INTERVAL), UUID, ARRAY, JSON, HSTORE, and specialized types (network/geometric).

#### 604. 487. What are the primary motivations behind NoSQL databases?
**Answer:**
The main motivations are to handle massive data storage and querying scale by highly parallelizing operations, often sacrificing the strict consistency/ACID guarantees of traditional relational DBMS for higher performance or availability.

#### 605. 488. What are the primary motivations for using database views?
**Answer:**
Views are used to: 1) Hide sensitive data from unauthorized users, 2) Simplify complex queries for end-users, and 3) Provide modularity to database access by decoupling the interface from the physical storage.

#### 606. 489. What are the primary reasons for database normalization?
**Answer:**
Normalization is used to eliminate redundant data (reducing anomalies) and to ensure that data dependencies make logical sense.

#### 607. 49. Do Hash Match, Merge Join, and Nested Loop operators require a memory grant?
**Answer:**
Hash Match requires a memory grant. Nested Loop does not. Merge Join generally does not, unless it involves a many-to-many relationship requiring tempdb worktables.

#### 608. 490. What are the primary subsets of SQL?
**Answer:**
DDL (Data Definition Language) for structure (CREATE, ALTER, DROP); DML (Data Manipulation Language) for content (SELECT, INSERT, UPDATE, DELETE); and DCL (Data Control Language) for security (GRANT, REVOKE).

#### 609. 491. What are the primary targets of database normalization?
**Answer:**
The goals are to improve database design, eliminate redundancy, ensure data consistency, and allow for the loss-free decomposition of relations so that original data can be reconstructed through joins.

#### 610. 492. What are the primary underlying data structures for database indexes?
**Answer:**
The two main structures are B-Trees (B-Trees or B+Trees), which support equality and range comparisons, and Hash Tables, which are optimized for constant-time equality lookups.

#### 611. 493. What are the primary use cases for triggers?
**Answer:**
Triggers are used to enforce referential integrity constraints, implement complex business logic/constraints, and audit data changes.

#### 612. 494. What are the properties of the 'Read Committed' isolation level?
**Answer:**
It prevents dirty reads, but allows non-repeatable reads. A row read multiple times might change value if another transaction commits an update in between.

#### 613. 495. What are the properties of the 'Repeatable Read' isolation level?
**Answer:**
It prevents dirty reads and ensures that an item read multiple times within the same transaction will not change value. However, it allows 'phantom reads' where new rows inserted by other transactions can appear.

#### 614. 496. What are the pros and cons of using Materialized Views?
**Answer:**
Pros: Dramatically improve query performance by pre-calculating results. Cons: They consume significant storage space and may become out-of-sync with the base tables, requiring maintenance.

#### 615. 497. What are the reasons for early statement termination during plan compilation?
**Answer:**
Time Out (limit on transformations reached), Memory (insufficient memory), or 'Good Enough' (an optimal or sufficient plan was found).

#### 616. 498. What are the requirements for 1NF, 2NF, 3NF, and BCNF?
**Answer:**
1NF: All key attributes defined, no repeating groups, all attributes dependent on the primary key. 2NF: In 1NF and no partial dependencies (attributes depend on the whole primary key). 3NF: In 2NF and no transitive dependencies. BCNF: Every determinant must be a candidate key.

#### 617. 499. What are the requirements for First Normal Form (1NF)?
**Answer:**
To be in 1NF: Define the data items required (columns), place related items in a table, ensure no repeating groups of data, and ensure a primary key is present.

#### 618. 5. Are variables and constants required to be declared?
**Answer:**
Yes, variables and constants must be declared before they can be referenced in other statements.

#### 619. 50. Do database privileges always reside within the database system itself?
**Answer:**
Privileges may not necessarily reside in the database, but in the software applications accessing the database. Consequently, an end-user might be granted access to the application while having no direct privileges within the database engine itself.

#### 620. 500. What are the requirements for a Primary Key?
**Answer:**
A Primary Key must contain a unique value for every row and cannot contain NULL values.

#### 621. 501. What are the requirements for a view to be automatically updatable under the SQL standard?
**Answer:**
To be updatable, a view must: have only one table in its top-level FROM clause, not use SELECT DISTINCT, not refer to that table in subqueries, and not use GROUP BY or aggregate functions. Additionally, it should include all attributes from the base table that do not permit NULL values.

#### 622. 502. What are the requirements for using UNION in SQL?
**Answer:**
Each SELECT statement within a UNION must: 1) have the same number of columns, 2) have compatible data types for corresponding columns, and 3) return columns in the same order.

#### 623. 503. What are the roles of IN, OUT, and IN/OUT parameters in SQL stored procedures?
**Answer:**
IN: Input only; OUT: Output only (return value); IN OUT: Used for both input and returning a modified value.

#### 624. 504. What are the rules for MVD (multi-valued dependencies)?
**Answer:**
The primary rule is the FD-is-an-MVD rule: every functional dependency (FD) is inherently an MVD, but not every MVD is an FD.

#### 625. 505. What are the rules for Normal Forms regarding dependencies?
**Answer:**
Functional dependencies alone are the primary concern for Boyce-Codd Normal Form (BCNF), while the combination of functional and multivalued dependencies determines 4th Normal Form (4NF).

#### 626. 506. What are the rules for a well-formed XML document?
**Answer:**
1. There must be exactly one single root element. 2. All tags must be properly closed and nested. 3. All attribute names must be unique within an element.

#### 627. 507. What are the sql:column() and sql:variable() functions?
**Answer:**
These are XQuery functions used within SQL Server to interact with XML data. sql:column() extracts values from a SQL column into an XQuery context, while sql:variable() retrieves the value of a SQL variable for use within XQuery expressions.

#### 628. 508. What are the standard SQL aggregate functions?
**Answer:**
Aggregate functions perform operations over multiple values in rows. The standard functions are: COUNT (number of non-null values), MIN (minimum value), MAX (maximum value), SUM (sum of values), and AVG (average value).

#### 629. 509. What are the steps to execute a cursor?
**Answer:**
1. Declare cursor, 2. Open cursor, 3. Fetch row, 4. Process row, 5. Close cursor, 6. Deallocate cursor.

#### 630. 51. Do execution plans have priority in server memory?
**Answer:**
Yes, execution plans are stored in the plan cache within the buffer pool. The SQL Server query optimizer treats them as high-priority memory consumers, and they are managed by an algorithm that determines which plans to evict based on frequency of use and cost.

#### 631. 510. What are the storage characteristics and statistical differences between temporary tables and table variables?
**Answer:**
Temporary tables are stored in tempdb on disk and support statistics. Table variables are also stored in tempdb, but do not maintain histograms or updateable statistics, which can impact query optimizer performance.

#### 632. 511. What are the three SQL keywords used for procedure/function parameters?
**Answer:**
IN (input only), OUT (output only), and IN OUT (input and output).

#### 633. 512. What are the three core parts of a PL/SQL block?
**Answer:**
1. Declaration (optional): Where variables, constants, cursors, and exceptions are defined. 2. Executable (mandatory): Where logic and variable manipulation occur. 3. Exception (optional): Where errors raised during execution are handled.

#### 634. 513. What are the three main areas of SQL statements?
**Answer:**
1. Data Definition Language (DDL) for structure, 2. Data Manipulation Language (DML) for data access/modification, 3. Data Control Language (DCL) for access permissions.

#### 635. 514. What are the three main categories of data types in relational databases?
**Answer:**
The three main categories are: 1. String (char, varchar, nvarchar), 2. Numeric (int, decimal, float), and 3. Date and Time (date, datetime, datetime2).

#### 636. 515. What are the three structured database approaches?
**Answer:**
The common approaches cited are ISCL (Information Systems Cycle/Life), SDLC (Software Development Life Cycle), and DSDLC (Database Software Development Life Cycle).

#### 637. 516. What are the trade-offs of using indexes on a table?
**Answer:**
Indexes improve the performance of SELECT queries but increase the overhead for data modification operations (INSERT, UPDATE, DELETE) because the index must be reconstructed or maintained alongside the base data.

#### 638. 517. What are the two ISO standard mechanisms for domain constraints?
**Answer:**
The CHECK clause and the CREATE DOMAIN statement.

#### 639. 518. What are the two primary activities in database planning?
**Answer:**
Defining the mission statement and defining the mission objectives.

#### 640. 519. What are the two primary approaches for managing view modifications in a DBMS?
**Answer:**
1. Rewriting process: Uses INSTEAD-OF triggers or rules to define how updates are handled. It is flexible but requires careful implementation. 2. Restrictive approach: Limits views (e.g., no DISTINCT, no GROUP BY, single table only) to ensure modifications to base tables are unambiguous and automatically handled by the engine.

#### 641. 52. Does COUNT(myCol) count all rows in a column? What happens with NULLs?
**Answer:**
No. COUNT(column_name) ignores NULL values in that column. Use COUNT(*) to count all rows regardless of NULLs.

#### 642. 520. What are the two primary goals of database authorization?
**Answer:**
1. Limit what the user can see (ensure users only access data they are authorized for). 2. Protect against malicious modifications by unauthorized users.

#### 643. 521. What are the two primary motivations for implementing database transactions?
**Answer:**
Transactions are motivated by two independent concepts: Concurrency control and Resilience against system failure.

#### 644. 522. What are the two types of PL/SQL subprograms?
**Answer:**
PL/SQL supports Stored Procedures and Functions.

#### 645. 523. What are the two types of database triggers?
**Answer:**
Triggers can be Row-level triggers (executing once per modified row) or Statement-level triggers (executing once per SQL statement).

#### 646. 524. What are the typical steps of database system development?
**Answer:**
1. Database planning, 2. System definition, 3. Requirements collection and analysis, 4. Database design, 5. DBMS selection.

#### 647. 525. What are the various Join types available in T-SQL?
**Answer:**
Join types include: Inner Join, Outer Joins (Left, Right, Full), and Cross Joins. These can be further filtered using exclusion logic (e.g., LEFT OUTER JOIN where the right side is NULL).

#### 648. 526. What are trivial functional dependencies?
**Answer:**
If A->B and B is a subset of A, then the dependency is trivial. This implies A -> (A union B) and A -> (A intersect B).

#### 649. 527. What are two common SQL Injection payloads that evaluate to 'Always True'?
**Answer:**
1=1 and ''=''. These are used to bypass authentication by making a WHERE clause always evaluate to true.





## 📂 Category: Database Design & Normalization (37 cards)



### 🔴 Senior Level

#### 650. 528. What causes the 'ERROR 666' in SQL Server?
**Answer:**
This error is emitted when the internal hidden integer column used to manage non-unique clustered keys overflows its allocated storage limit.

#### 651. 529. What comes right after the WHERE clause?
**Answer:**
The predicate (a logical condition used to filter rows).

#### 652. 53. Does a row have to fit on one page?
**Answer:**
Generally, rows are designed to fit on a single page, but if variable-length data causes the row size to exceed page limits, the engine moves that data to an overflow page.

#### 653. 530. What commands represent DCL?
**Answer:**
Data Control Language (DCL) commands control access to data stored in the database. Examples include GRANT and REVOKE.

#### 654. 531. What commands represent DDL?
**Answer:**
Data Definition Language (DDL) commands define or change the database schema. Examples include CREATE, ALTER, and DROP.

#### 655. 532. What commands represent DML?
**Answer:**
Data Manipulation Language (DML) commands are used for managing data within database objects. Examples include SELECT, INSERT, UPDATE, and DELETE.

#### 656. 533. What commands represent TCL?
**Answer:**
Transaction Control Language (TCL) commands manage transactions within the database. Examples include COMMIT and ROLLBACK.

#### 657. 534. What condition is required for a Merge Join?
**Answer:**
A Merge Join requires an equijoin condition and sorted inputs on the join keys.

#### 658. 535. What condition is required for an INNER JOIN?
**Answer:**
An INNER JOIN requires at least two tables that share a common column or overlapping field to serve as the basis for the join relationship.

#### 659. 536. What condition must be met for a view to be updateable?
**Answer:**
The view must be based on a single table; it cannot contain joins, aggregations, or unions if you intend to perform INSERT, UPDATE, or DELETE operations through it.

#### 660. 537. What data type do we use when we want to define points in time to a certain degree of accuracy?
**Answer:**
Date and Time data types (e.g., DATETIME, TIMESTAMP, DATE).

#### 661. 538. What data type represents truth values?
**Answer:**
The Boolean data type, which holds the values TRUE and FALSE.

#### 662. 539. What data types can be used with the BETWEEN operator?
**Answer:**
BETWEEN can be used to select a range of numbers, text, or dates.

#### 663. 54. Does serializability guarantee a specific execution order?
**Answer:**
No, serializability guarantees that the final state is equivalent to some serial order of execution, but it does not dictate which specific order. If a specific order is required, it must be handled by the application logic.

#### 664. 540. What defines a 'good' decomposition of a relation?
**Answer:**
A good decomposition is a set of tables that, when joined back together, produces the original data without loss of information; this is known as the lossless join property.

#### 665. 541. What defines the Second Normal Form (2NF)?
**Answer:**
A table is in 2NF if it meets all 1NF requirements and contains no partial functional dependencies, meaning all non-key attributes must be fully functionally dependent on the entire primary key.

#### 666. 542. What do DSDLC, ISLC, and SDLC stand for?
**Answer:**
DSDLC: Database System Development LifeCycle; ISLC: Information Systems LifeCycle; SDLC: Software Development LifeCycle.

#### 667. 543. What do LOCK_TIMEOUT settings of -1 and 0 mean in SQL Server?
**Answer:**
LOCK_TIMEOUT = -1 means the session will wait indefinitely for a lock. LOCK_TIMEOUT = 0 means the session will immediately return an error if a lock cannot be acquired without waiting.

#### 668. 544. What do SQL commands INSERT, SELECT, UPDATE, and DELETE do?
**Answer:**
INSERT adds a new record, SELECT retrieves data, UPDATE modifies existing records, and DELETE removes records from a table.

#### 669. 545. What do common SQL Server wait types signify: CX_PACKET, CXCONSUMER, and RESOURCE_SEMAPHORE?
**Answer:**
CX_PACKET: Parallelism wait (thread waiting on other threads/processor). CXCONSUMER: Parallelism wait (parent waiting on child). RESOURCE_SEMAPHORE: Waiting for a memory grant.

#### 670. 546. What do sys.indexes.index_id values represent?
**Answer:**
0 indicates a heap (table with no clustered index), 1 indicates a clustered index, and values greater than 1 indicate nonclustered indexes.

#### 671. 547. What do the 'data_type' and 'size' parameters specify in a CREATE TABLE statement?
**Answer:**
The data_type defines the category of data the column can hold (e.g., VARCHAR, INTEGER, DATE). The size parameter specifies the maximum length or storage capacity for that column (e.g., the number of characters for a string).

#### 672. 548. What do the SQL Server internal engines (Apolon, Hekaton, Relation) do?
**Answer:**
Apolon handles columnstore indexes for data warehousing; Hekaton manages memory-optimized objects; the Relational Engine handles general query processing tasks.

#### 673. 549. What do the UPDATE, ALTER, CREATE, and DROP commands do?
**Answer:**
CREATE creates a new database object (table, view, etc.). ALTER modifies an existing database object. DROP removes an entire object from the database. UPDATE modifies existing data records within a table.

#### 674. 55. Explain 'Complete' vs 'Incomplete' and 'Disjoint' vs 'Overlapping' subclassing.
**Answer:**
Complete subclassing means every instance of a superclass must belong to at least one subclass; Incomplete (partial) means it doesn't necessarily have to. Disjoint (exclusive) means an instance cannot belong to more than one subclass; Overlapping means an instance can belong to several subclasses simultaneously.

#### 675. 550. What do you call the output returned from a SELECT statement?
**Answer:**
A result set.

#### 676. 551. What do you mean by table and field in SQL?
**Answer:**
A table is a collection of data organized in rows and columns. A field refers to a specific column within that table.

#### 677. 552. What does "cost" in an execution plan mean?
**Answer:**
It is an estimate of the processing time an operator will take, relative to the total cost of the query plan.

#### 678. 553. What does 'CREATE DATABASE my_db;' do?
**Answer:**
It initializes and creates a new database named 'my_db' within the SQL server instance.

#### 679. 554. What does 'number of rows to be read' (residual reads) mean in query statistics?
**Answer:**
This refers to the number of pages/rows that had to be physically read by the storage engine to retrieve columns not covered by the index (often called key lookups or residual reads).

#### 680. 555. What does CRUD stand for in database operations?
**Answer:**
CRUD stands for Create (INSERT), Read (SELECT), Update (UPDATE), and Delete (DELETE). These are the four fundamental operations for persistent data management.

#### 681. 556. What does CRUD stand for in the context of database operations?
**Answer:**
CRUD stands for Create, Read, Update, and Delete. These are the four basic functions for persistent storage.

#### 682. 557. What does ETL testing include?
**Answer:**
ETL testing involves: 1. Data Transformation: Ensuring business rules are applied correctly. 2. Data Integrity: Checking for truncation or loss during load. 3. Data Cleansing: Verifying invalid data is caught or replaced. 4. Performance: Ensuring load times meet SLAs.

#### 683. 558. What does GRANT and REVOKE do?
**Answer:**
GRANT gives a specific privilege to a user; REVOKE removes a previously granted privilege from a user.

#### 684. 559. What does HIERARCHICALID.GetDescendant return?
**Answer:**
It returns a child HIERARCHICALID node that is lower than a specified child, or a valid node between two existing child nodes.

#### 685. 56. Explain CROSS, LEFT, RIGHT, and FULL OUTER JOINS.
**Answer:**
A CROSS JOIN returns the Cartesian product of two tables. A LEFT JOIN returns all rows from the left table and matches from the right, with NULLs for missing matches. A RIGHT JOIN does the inverse. A FULL OUTER JOIN returns all rows from both tables, filling with NULLs where matches do not exist.

#### 686. 560. What does RDBMS stand for?
**Answer:**
Relational Database Management System.

#### 687. 561. What does SCOPE_IDENTITY() return?
**Answer:**
It returns the last identity value generated in the current session and the current scope.

#### 688. 562. What does SQL mainly allow us to do?
**Answer:**
SQL allows us to: 1. Execute queries and retrieve data from a database, 2. Insert rows into tables, 3. Update rows in tables, 4. Delete rows from tables, 5. Create new databases, 6. Create new tables, 7. Create stored procedures, 8. Create views, 9. Set permissions on tables, procedures, and views.

#### 689. 563. What does SQL stand for?
**Answer:**
Structured Query Language.

#### 690. 564. What does SQL stand for?
**Answer:**
SQL stands for Structured Query Language.

#### 691. 565. What does a COMMIT statement do?
**Answer:**
It permanently saves the changes made during the current transaction to the database.

#### 692. 566. What does a SELECT statement do and what does it return?
**Answer:**
A SELECT statement is used to retrieve data from a database. Specifically, 'SELECT *' returns all columns from the specified table. The output of any SELECT statement is referred to as a result set.

#### 693. 567. What does a bit string consist of?
**Answer:**
A sequence of binary digits, limited to the values 0 and 1.

#### 694. 568. What does an INSERT INTO ... SELECT statement do?
**Answer:**
It copies data from one or more source tables into a target table. For example, copying specific supplier records into the Customers table based on a condition.

#### 695. 569. What does an RID contain?
**Answer:**
A Record Identifier (RID) typically contains references to the file ID, page ID, and row number.

#### 696. 57. Explain Document, Graph, and Key/Value databases.
**Answer:**
Document (e.g., MongoDB): Stores semi-structured data in JSON/XML; flexible schema. Graph (e.g., Neo4j): Focuses on relationships between entities (nodes/edges). Key/Value (e.g., Redis): Simplest model; optimized for extremely fast reads/writes via a unique key.

#### 697. 570. What does an algebraizer do with a View?
**Answer:**
The algebraizer expands the view definition into the base query during the parsing and binding phase.

#### 698. 571. What does character data consist of?
**Answer:**
A sequence of characters from an implementation-defined character set (typically defined using CHAR or VARCHAR types).

#### 699. 572. What does it mean for a query to be 'Sargable'?
**Answer:**
Sargable (Search ARGument ABLE) refers to an expression that is structured in a way that allows the query optimizer to utilize an index for data retrieval.

#### 700. 573. What does it mean for a transaction to be atomic?
**Answer:**
Atomicity means that a transaction is treated as a single unit of work. Either all operations within the transaction are committed, or none of them are. To external observers, the transaction is all-or-nothing (opaque).

#### 701. 574. What does it mean for columns to have integrity enhancement?
**Answer:**
It ensures data validity, specifically requiring that columns contain valid values and prohibiting NULLs where mandatory constraints are applied.

#### 702. 575. What does it mean to 'type' a table?
**Answer:**
Typing refers to the process of assigning specific data types (e.g., INTEGER, TEXT, TIMESTAMP) to row definitions when creating or altering a table schema.

#### 703. 576. What does sys.dm_exec_query_statistic_XML(session_id) do?
**Answer:**
Returns information about currently running query in a selected session, typically used for troubleshooting execution plans. Note that it often requires specific trace flags enabled.

#### 704. 577. What does the 'WITH CHECK OPTION' do in a view?
**Answer:**
It ensures that any INSERT or UPDATE performed through the view must satisfy the criteria defined in the view's WHERE clause, preventing the creation of rows that would fall outside the view's definition.

#### 705. 578. What does the 'impact' value in a missing index hint signify?
**Answer:**
It represents the estimated percentage improvement in query performance if the recommended index were created.

#### 706. 579. What does the ACID acronym stand for in transaction management?
**Answer:**
ACID stands for Atomicity, Consistency, Isolation, and Durability; these are the standard properties that guarantee reliable database transactions.

#### 707. 58. Explain HIERARCHYID functions: GetAncestor, GetDescendant, GetLevel, GetReparentedValue, ToString, GetRoot, and Parse.
**Answer:**
These functions manage hierarchical data: GetAncestor returns a parent node; GetDescendant returns child nodes between two siblings; GetLevel returns depth; GetReparentedValue moves a subtree; ToString/Parse convert between human-readable strings and the HIERARCHYID binary type; GetRoot returns the hierarchy apex.

#### 708. 580. What does the Atomicity property guarantee in a database transaction?
**Answer:**
Atomicity guarantees an 'all-or-nothing' approach: the entire transaction completes successfully, or if it fails, the database rolls back to the state before the transaction began.

#### 709. 581. What does the BETWEEN clause do?
**Answer:**
The BETWEEN operator filters data within an inclusive range. It works with numeric, text, and date data types.

#### 710. 582. What does the CAP theorem describe regarding distributed systems?
**Answer:**
The CAP theorem describes the fundamental trade-off between three properties: Consistency (every read receives the most recent write), Availability (every request receives a response), and Partition tolerance (system continues to operate despite network failures).

#### 711. 583. What does the CAP theorem describe?
**Answer:**
The CAP theorem states that a distributed data store cannot simultaneously provide more than two out of three guarantees: Consistency (all nodes see the same data at the same time), Availability (every request receives a response), and Partition tolerance (the system continues to operate despite network failures).

#### 712. 584. What does the COL_LENGTH() function do?
**Answer:**
It returns the defined maximum length (in bytes) of a specific table column.

#### 713. 585. What does the COUNT aggregate function do?
**Answer:**
COUNT() is an aggregate function that returns the number of rows where the specified column contains a non-NULL value.

#### 714. 586. What does the DISTINCT clause do?
**Answer:**
The DISTINCT clause is used with a SELECT statement to return only unique values, effectively removing duplicate rows from the result set.

#### 715. 587. What does the FLOWR acronym stand for in XQuery?
**Answer:**
FLOWR stands for: For, Let, Order, Where, Return.

#### 716. 588. What does the LIMIT clause do in a SQL query?
**Answer:**
The LIMIT clause constrains the number of rows returned by a query.

#### 717. 589. What does the LIMIT clause do?
**Answer:**
The LIMIT clause restricts the number of rows returned by a query to a specified maximum number.

#### 718. 59. Explain date/time data types (date, datetime, datetime2) and ISO8601 formatting.
**Answer:**
ISO8601 format is YYYY-MM-DD HH:MM:SS.000. 'date' stores only the date. 'datetime' stores date and time with millisecond precision. 'datetime2' offers higher precision for date and time. Inserting an incompatible format (e.g., time into a date column) causes a conversion error.

#### 719. 590. What does the ONLY clause do in PostgreSQL queries?
**Answer:**
The ONLY keyword restricts a query to the target table specifically, ignoring any descendant tables that might exist due to table inheritance. It is used with SELECT, UPDATE, and DELETE.

#### 720. 591. What does the ORDER BY clause do?
**Answer:**
The ORDER BY clause sorts the result set by one or more columns, either alphabetically or numerically. Sorting can be specified as ascending (ASC, default) or descending (DESC).

#### 721. 592. What does the ROUND function do?
**Answer:**
The ROUND() function rounds a numeric value to a specified number of decimal places. It is often used in conjunction with aggregate functions.

#### 722. 593. What does the SQL keyword 'BEFORE' indicate in a trigger?
**Answer:**
It specifies that the trigger code should execute before the triggering event (such as an INSERT) is actually applied to the table.

#### 723. 594. What does the UNION clause do?
**Answer:**
The UNION clause combines the result sets of multiple SELECT statements into a single result set while automatically removing duplicate rows.

#### 724. 595. What does the UPDATE statement do?
**Answer:**
The UPDATE statement is used to modify existing records in a table. It uses a SET clause to define the new values and a WHERE clause to specify which rows should be updated.

#### 725. 596. What does the UPDATE(column) function do within a trigger?
**Answer:**
It returns a boolean value indicating whether the specified column was modified in the SET clause of a DML statement.

#### 726. 597. What does the WITH clause (Common Table Expression) do?
**Answer:**
The WITH clause allows you to define a temporary result set (or 'subquery') that can be referenced within the main query. Multiple temporary tables can be defined in a single WITH statement to improve query readability and structure.

#### 727. 598. What does the acronym ACID stand for?
**Answer:**
Atomicity, Consistency, Isolation, Durability. These are the fundamental properties that ensure reliable database transactions.

#### 728. 599. What does the acronym CRUD stand for?
**Answer:**
CRUD stands for Create, Read, Update, and Delete, representing the four basic operations for persistent data storage.

#### 729. 6. Around which three main concepts is SQL access control built?
**Answer:**
SQL access control is built around authorization identifiers (users/roles), ownerships, and privileges (grant/revoke).

#### 730. 60. Explain how filtering works with NULL values and inclusion lists.
**Answer:**
Use 'WHERE column IS NULL' or 'IS NOT NULL' to filter nulls. Use 'WHERE column IN (value1, value2)' or 'NOT IN (...)' to filter against a list of specific values.

#### 731. 600. What does the association multiplicity 0..* mean?
**Answer:**
It means the relationship can exist between none or any number of objects (zero to many).

#### 732. 601. What does the command ALTER DATABASE SET ENABLE_BROKER do?
**Answer:**
It enables the Service Broker feature for the specified SQL Server database, which allows for asynchronous message processing.

#### 733. 602. What does the expression '{...}' mean in XQuery?
**Answer:**
The curly brackets '{}' in XQuery signify 'evaluate me', meaning the expression contained inside the brackets will be executed as a query.

#### 734. 603. What does the query 'SELECT * FROM Customers WHERE City LIKE 's%'' perform?
**Answer:**
It selects all columns from the Customers table for rows where the City column starts with the letter 's'.

#### 735. 604. What does the query 'SELECT GETDATE();' return?
**Answer:**
It returns the current date and time from the database server.

#### 736. 605. What factors define a data model?
**Answer:**
Key factors include defining Dimensions and Facts, identifying Primary Keys for unique identification, determining Measures for calculation, and establishing the Granularity of the data (detail level).

#### 737. 606. What factors determine the effectiveness of an index?
**Answer:**
Effectiveness depends on the size of the table, data distribution, and the ratio of query read load versus update/write load.

#### 738. 607. What happens if a Service Broker route is only configured on the initiator?
**Answer:**
The initiator sends the message, but the receiver will likely drop duplicate messages if it cannot return an acknowledgment correctly.

#### 739. 608. What happens if a stored procedure expecting a Table-Valued Parameter (TVP) is called without one?
**Answer:**
The parameter will be treated as an empty table.

#### 740. 609. What happens if you disable a clustered index?
**Answer:**
Access to the entire table is disabled in most SQL implementations.

#### 741. 61. Explain the 4NF and BCNF decomposition algorithms.
**Answer:**
Both algorithms decompose relations to remove redundancies. BCNF (Boyce-Codd Normal Form) ensures that for every functional dependency X -> Y, X is a superkey. 4NF addresses multi-valued dependencies where a table contains two or more independent multi-valued facts about an entity.

#### 742. 610. What happens if you omit columns during an INSERT INTO operation?
**Answer:**
The database will insert NULL values into the unspecified columns (provided they are not defined with NOT NULL or default values).

#### 743. 611. What happens when an INNER JOIN is executed?
**Answer:**
An INNER JOIN returns only the records that have matching values in both tables being joined.

#### 744. 612. What happens when you violate referential integrity?
**Answer:**
The database will throw a foreign key constraint violation error. This prevents orphaned records by ensuring that a value inserted into a foreign key column must already exist in the referenced primary key column.

#### 745. 613. What is %%physloc%% in SQL Server?
**Answer:**
%%physloc%% is a virtual column that contains the physical address (RID - Row Identifier) of a row in a table.

#### 746. 614. What is 'Compositionality' in query languages?
**Answer:**
Compositionality is the ability to nest queries or combine multiple query results using relational algebra or SQL operators.

#### 747. 615. What is 'cache bloat' in a SQL server context?
**Answer:**
Cache bloat is the exhaustion of memory caused by storing an excessive number of unique query plans, often due to lack of parameterization.

#### 748. 616. What is 'hole-filling optimization' in the context of MERGE statements?
**Answer:**
An optimization where, if a MERGE statement only inserts rows into the gaps in a clustered key, it can avoid HALLOWEEN protection logic.

#### 749. 617. What is 4th Normal Form (4NF) regarding Multivalued Dependencies (MVDs)?
**Answer:**
4NF requires that for every non-trivial MVD A ->> B, A must be a superkey. It is a specialization of BCNF that handles cases where one attribute is associated with a set of values.

#### 750. 618. What is CRUD?
**Answer:**
CRUD stands for the four basic database operations: Create, Read, Update, and Delete.

#### 751. 619. What is Collation?
**Answer:**
Collation defines the rules for sorting and comparing character data, including settings for case sensitivity, accent sensitivity, and character width.

#### 752. 62. Explain the AND, OR, and NOT logical operators.
**Answer:**
AND displays a record if all conditions are true. OR displays a record if at least one condition is true. NOT displays a record if the specified condition is false.

#### 753. 620. What is DBCC?
**Answer:**
DBCC (Database Console Commands) are administrative tools used to perform maintenance, validation (like CHECKDB), information gathering, and miscellaneous tasks in SQL Server.

#### 754. 621. What is DCL and its commands?
**Answer:**
DCL stands for Data Control Language. It is used to manage permissions and access control. Its primary commands are GRANT, DENY, and REVOKE.

#### 755. 622. What is DDL (Data Definition Language)?
**Answer:**
DDL is a subset of SQL used to define and manage database structures (schema). Commands include CREATE, ALTER, DROP, and TRUNCATE.

#### 756. 623. What is DML (Data Manipulation Language)?
**Answer:**
Data Manipulation Language (DML) is a subset of SQL used for managing and modifying data within database objects. Key commands include SELECT, INSERT, UPDATE, and DELETE.

#### 757. 624. What is Data Control Language (DCL)?
**Answer:**
Data Control Language (DCL) comprises SQL commands used for transaction control (COMMIT, ROLLBACK), user management (CREATE/DROP/ALTER USER), and authorization (GRANT, REVOKE).

#### 758. 625. What is Data Definition Language (DDL)?
**Answer:**
Data Definition Language (DDL) consists of SQL commands used to define and modify the database structure, such as CREATE, ALTER, and DROP statements for tables, indexes, and views.

#### 759. 626. What is Data Management in the context of databases?
**Answer:**
Data Management is the practice of collecting, storing, and retrieving data. Core functions include CRUD operations: Create (addition), Read (listing), Update (modification), and Delete (deletion).

#### 760. 627. What is Denormalization?
**Answer:**
Denormalization is the process of moving from a higher normal form to a lower one, usually to reduce join complexity and increase read performance, at the risk of introducing data anomalies.

#### 761. 628. What is Design by Decomposition?
**Answer:**
A process of starting with a large, unnormalized relation and breaking it into smaller, logically sound relations that preserve all original dependencies and attributes without data loss.

#### 762. 629. What is Durability in ACID?
**Answer:**
Durability guarantees that once a transaction has been committed, it will remain persisted in the database even in the event of a system crash, typically ensured by transaction logs.

#### 763. 63. Explain the ANY and ALL operators.
**Answer:**
ANY returns true if any subquery values meet the condition. ALL returns true only if all subquery values meet the condition. They are used in conjunction with standard comparison operators.

#### 764. 630. What is ETL?
**Answer:**
ETL stands for Extract, Transform, and Load. It is the process of extracting data from sources, converting it into a structured format for analysis, and loading it into a target data warehouse.

#### 765. 631. What is Fill Factor?
**Answer:**
Fill Factor is an index setting that determines the percentage of space to be filled with data on each leaf-level index page. It helps manage page splits in frequently updated tables.

#### 766. 632. What is IK?
**Answer:**
IK stands for Index Key.

#### 767. 633. What is LPE in the context of database engine operations?
**Answer:**
LPE stands for Language Processing and Execution, referring to the stages where a SQL statement is parsed, optimized, and executed.

#### 768. 634. What is Microsoft Access and when should it be used?
**Answer:**
Microsoft Access is a database solution for simple web sites or applications. It is not well-suited for high-traffic environments and lacks the power and scalability of RDBMS like MySQL, SQL Server, or Oracle.

#### 769. 635. What is Microsoft SQL Server?
**Answer:**
Microsoft SQL Server is a powerful, robust, and full-featured relational database management system (RDBMS) commonly used for high-traffic, database-driven web applications.

#### 770. 636. What is MySQL?
**Answer:**
MySQL is a popular, powerful, and robust open-source relational database management system often used as an inexpensive alternative to commercial solutions like Microsoft SQL Server or Oracle.

#### 771. 637. What is NoSQL and its relation to traditional relational databases?
**Answer:**
NoSQL stands for 'Not Only SQL'. It provides an alternative to the relational model for specific use cases. It typically offers lower expressivity than relational DBMS but provides higher efficiency and horizontal scalability. A key advantage is flexibility, as it often avoids the strict data preprocessing required by relational schemas, focusing processing only on the data portions actually being queried.

#### 772. 638. What is Normalization and what are its advantages?
**Answer:**
Normalization is the process of organizing a database to minimize data redundancy and dependency. By dividing tables and defining relationships between them, it helps reduce data anomalies, improve data integrity, and ensure consistency during updates. Common normal forms include 1NF, 2NF, 3NF, and BCNF.

#### 773. 639. What is Oracle Database?
**Answer:**
Oracle is a robust, full-featured, and powerful relational database management system often used for high-traffic, enterprise-level web applications.

#### 774. 64. Explain the BETWEEN operator and provide an example.
**Answer:**
The BETWEEN operator selects values within a given range. The values are inclusive. Example: 'SELECT * FROM movies WHERE name BETWEEN 'A' AND 'J';' will return all movies starting with letters A through J, including those starting with exactly 'A' or 'J'.

#### 775. 640. What is Page Free Space (PFS) in SQL Server?
**Answer:**
PFS pages are specific pages in the database that track the amount of free space available on data pages (using one byte per page).

#### 776. 641. What is Parameter Sniffing?
**Answer:**
A phenomenon in SQL Server where the query optimizer creates an execution plan for a stored procedure based on the parameter values provided during the very first execution, which may not be optimal for subsequent executions with different parameters.

#### 777. 642. What is Physical Database Design?
**Answer:**
Physical Database Design defines the internal storage structures, file organizations, and access paths used by the DBMS to store and manage data efficiently.

#### 778. 643. What is Relational Algebra?
**Answer:**
A formal mathematical definition and foundation of the relational model, providing a set of operations that act on relations (tables) to produce new relations.

#### 779. 644. What is SELECT INTO?
**Answer:**
A command that selects data from one or more existing tables and inserts the resulting rows into a new, automatically created table.

#### 780. 645. What is SGAM?
**Answer:**
SGAM stands for Shared Global Allocation Map. It is a system page used in SQL Server to track which extents in a database are currently mixed and have at least one free page available.

#### 781. 646. What is SQL Data Definition Language (DDL)?
**Answer:**
DDL is a subset of SQL used to define and manage database structures. It includes commands for schemas (CREATE/DROP SCHEMA), tables (CREATE/ALTER/DROP TABLE), domains (CREATE/ALTER/DROP DOMAIN), and views (CREATE/DROP VIEW).

#### 782. 647. What is SQL Injection and how can you prevent it?
**Answer:**
SQL Injection is a vulnerability where malicious SQL code is inserted into input fields to manipulate database queries, potentially leading to unauthorized data access or deletion. Prevention is achieved by using parameterized queries (prepared statements), which ensure that user input is treated as data, not as executable code.

#### 783. 648. What is SQL Injection?
**Answer:**
A technique where malicious users inject SQL commands into an SQL statement via user input on a web page to bypass security or manipulate data.

#### 784. 649. What is SQL?
**Answer:**
SQL stands for Structured Query Language. It is a standard language used to manage, manipulate, and query data stored in relational database management systems.

#### 785. 65. Explain the COUNT aggregate function.
**Answer:**
COUNT() returns the number of rows that match a specified criterion. 'COUNT(*)' counts all rows including NULLs, while 'COUNT(column_name)' counts only rows where the specified column is not NULL.

#### 786. 650. What is SQL?
**Answer:**
SQL stands for Structured Query Language. It is the standard programming language designed for managing data held in a relational database management system (RDBMS) and is an implementation of Relational Algebra.

#### 787. 651. What is SQL?
**Answer:**
SQL (Structured Query Language) is an ANSI-standard language designed to manage and manipulate relational databases. It supports operations such as database creation, row retrieval, data modification, and structure management.

#### 788. 652. What is SSIS?
**Answer:**
SSIS stands for SQL Server Integration Services. It is a platform for building enterprise-level data integration and data transformations solutions.

#### 789. 653. What is Scalar UDF inlining?
**Answer:**
It is a process where the SQL engine attempts to convert a scalar User Defined Function into a relational expression, allowing it to be integrated into the main query plan for better performance.

#### 790. 654. What is Scoping in the Database Life Cycle?
**Answer:**
Scoping involves analyzing the requirements domain and the user environment to determine the relevance, importance, and priorities for the resulting data model.

#### 791. 655. What is UML in the context of database design?
**Answer:**
Unified Modeling Language (UML) is a standard visual modeling language used to design and document database schemas and system architectures.

#### 792. 656. What is a 'Rebind' operation in query execution?
**Answer:**
A process where the conditions of a spool operator are re-evaluated or re-initialized before the operator begins reading the rows again.

#### 793. 657. What is a 'Rewind' operation in query execution?
**Answer:**
An operation where the database restarts reading a spool or table from the beginning.

#### 794. 658. What is a 'dirty read' in database transactions?
**Answer:**
A dirty read occurs when a transaction reads data that has been modified by another concurrent transaction but has not yet been committed.

#### 795. 659. What is a 'poison message' in the context of SQL Server Service Broker?
**Answer:**
A message that causes a transaction to fail repeatedly, specifically a message where processing has triggered a rollback five times.

#### 796. 66. Explain the GROUP BY and HAVING clauses.
**Answer:**
GROUP BY is used to group result sets by one or more columns, typically in combination with aggregate functions. The HAVING clause is used to filter groups created by GROUP BY, as the standard WHERE clause cannot be used with aggregate functions.

#### 797. 660. What is a 'quantum' in the context of database engine scheduling?
**Answer:**
A quantum is the largest amount of time (typically 4 ms) that one worker thread can consecutively run on a single processor before being preempted.

#### 798. 661. What is a 'read-ahead read' in database performance?
**Answer:**
A performance optimization where the database engine loads consecutive data pages into memory before they are explicitly requested, reducing I/O wait times.

#### 799. 662. What is a 'stub' query plan?
**Answer:**
A stub query plan refers to a cached hash of an execution plan that does not contain the actual compiled plan details, often seen when memory pressure or specific cache settings prevent full plan storage.

#### 800. 663. What is a 'trivial plan' in query optimization?
**Answer:**
A trivial plan is a simple execution plan consisting only of basic scans or seeks, created without applying complex algebraic transformations or optimization rules.

#### 801. 664. What is a BLOB?
**Answer:**
BLOB stands for Binary Large Object, used for storing large chunks of binary data (like images or media) in a database.

#### 802. 665. What is a CHECK Constraint?
**Answer:**
The CHECK constraint ensures that all values in a column satisfy a specified boolean condition.

#### 803. 666. What is a CHECK constraint?
**Answer:**
A CHECK constraint is used to enforce domain integrity by limiting the values that can be inserted into a column or ensuring that values across columns satisfy a specific condition.

#### 804. 667. What is a CTE (Common Table Expression)?
**Answer:**
A CTE is defined using the WITH clause. It creates a temporary result set that can be referenced within a single SELECT, INSERT, UPDATE, or DELETE statement, improving readability and organization of complex queries.

#### 805. 668. What is a Cloud Database?
**Answer:**
A database service created and maintained on a cloud infrastructure platform (such as Azure, AWS, or GCP) rather than on-premises hardware.





## 📂 Category: Basic SQL & Syntax (256 cards)



### 🟢 Junior Level

#### 806. 669. What is a Clustered Key (CK)?
**Answer:**
A Clustered Key is the unique identifier or set of columns that determines the physical order of data rows in a table.

#### 807. 67. Explain the LIKE operator and provide an example.
**Answer:**
LIKE is an operator used in a WHERE clause to search for a specified pattern in a column. The '%' wildcard represents zero, one, or multiple characters, while '_' represents a single character. Example: 'SELECT * FROM movies WHERE name LIKE 'se_en';' finds names like 'seven' or 'semen'.

#### 808. 670. What is a Collation?
**Answer:**
Collation defines the rules for storing, sorting, and comparing character data.

#### 809. 671. What is a Common Table Expression (CTE)?
**Answer:**
A temporary, named result set defined using the WITH clause. It exists only for the scope of the single statement it is attached to and is often used to simplify complex joins or recursive logic.

#### 810. 672. What is a Cursor in a database?
**Answer:**
A cursor is a database object that allows applications to process data on a row-by-row basis, moving away from the typical set-based operations of SQL.

#### 811. 673. What is a DTD?
**Answer:**
DTD stands for Document Type Definition, used to define the structure and valid elements of an XML document.

#### 812. 674. What is a Data Cube (multidimensional OLAP)?
**Answer:**
A Data Cube is an OLAP structure where dimension data forms the axes of the cube and fact (dependent) data exists in the cells. It allows for efficient retrieval of aggregated data across various dimensions.

#### 813. 675. What is a Decision Support System (DSS)?
**Answer:**
A system that assists enterprise-wide decision-making by data processing and manipulation of existing data sets with the help of specialized tools.

#### 814. 676. What is a Decision Support System (DSS)?
**Answer:**
A Decision Support System is an infrastructure, typically a data warehouse tuned for OLAP (Online Analytical Processing) analysis, used to store and process data for business intelligence and decision-making.

#### 815. 677. What is a FOREIGN KEY constraint?
**Answer:**
A foreign key is a field in one table that links to the PRIMARY KEY of another table. It establishes a parent-child relationship between tables, ensuring referential integrity by preventing orphaned records.

#### 816. 678. What is a FULL OUTER JOIN?
**Answer:**
A FULL OUTER JOIN returns all records when there is a match in either the left or the right table. If a row in the left table does not have a match in the right table (or vice versa), the result set includes those rows with NULL values for the missing data.

#### 817. 679. What is a Foreign Key?
**Answer:**
A Foreign Key is a field (or collection of fields) in a table that uniquely identifies a row or record in another database table. Recommended naming conventions use a combination of the referenced table name and the referenced field name.

#### 818. 68. Explain the SQL COUNT(), AVG(), and SUM() functions.
**Answer:**
These are aggregate functions used for calculations on result sets: COUNT() returns the number of rows matching criteria; AVG() returns the average value of a numeric column; SUM() returns the total sum of values in a numeric column.

#### 819. 680. What is a Foreign Key?
**Answer:**
A Foreign Key is a field (or collection of fields) in one table that refers to the Primary Key in another table, establishing and enforcing a link between the data in the two tables.

#### 820. 681. What is a GAM page?
**Answer:**
GAM stands for Global Allocation Map, which tracks which extents have been allocated in a SQL Server data file.

#### 821. 682. What is a Global Allocation Map (GAM) in database storage?
**Answer:**
A GAM page is a specialized storage page that tracks extent allocation. It uses a bitmask where 'true' indicates an unallocated extent and 'false' indicates an allocated extent.

#### 822. 683. What is a JOIN and what are the main types?
**Answer:**
A JOIN combines columns from one or more tables by using common values. Main types include: INNER, LEFT OUTER, RIGHT OUTER, FULL OUTER, and CROSS. A table can also join to itself in a self-join.

#### 823. 684. What is a NULL value in SQL?
**Answer:**
A NULL value represents the absence of data, distinct from blank or zero. It signifies missing, not available, or not applicable information. Comparisons with NULL always result in NULL, leading to three-valued logic. Note: UNIQUE constraints typically allow multiple NULL values.

#### 824. 685. What is a Natural Join?
**Answer:**
A Natural Join is an equijoin that automatically joins tables based on columns with the same name in both relations.

#### 825. 686. What is a Nested Loop join?
**Answer:**
A Nested Loop join is an algorithm suitable for joining a small dataset with a larger one. It iterates through each row of the outer table and performs a lookup in the inner table, making it very effective when the inner table is indexed.

#### 826. 687. What is a PRIMARY KEY?
**Answer:**
A primary key is a column or a combination of columns that uniquely identifies each row in a database table. It enforces entity integrity by combining NOT NULL and UNIQUE constraints.

#### 827. 688. What is a Partial Dependency?
**Answer:**
A condition in database normalization where an attribute is functionally dependent on only a portion (subset) of a composite primary key.

#### 828. 689. What is a Physical Design Advisor and how does it function?
**Answer:**
It is a tool that analyzes database statistics and workload to recommend optimal indexes. It functions by testing various index combinations against the Query Optimizer to estimate execution costs, selecting the configuration where performance benefits outweigh maintenance overhead.

#### 829. 69. Explain the UNION and UNION ALL operators.
**Answer:**
The UNION operator combines the result sets of two or more SELECT statements into a single result set. By default, UNION removes duplicate rows. UNION ALL keeps all rows, including duplicates. Requirements: Both queries must have the same number of columns, in the same order, with compatible data types.

#### 830. 690. What is a Plan Guide in SQL Server?
**Answer:**
A component that allows database administrators to influence query optimization by attaching query hints to specific queries based on text matching, even when the application code cannot be changed.

#### 831. 691. What is a Primary Key?
**Answer:**
A Primary Key (PK) is a constraint that uniquely identifies each row in a table. It cannot contain NULL values, and each table can have only one PK. PKs are automatically indexed to improve data retrieval performance.

#### 832. 692. What is a RID (Row Identifier)?
**Answer:**
A Row Identifier (RID) is a unique pointer to a specific row within a table, typically used by SQL Server to locate a row on a data page.

#### 833. 693. What is a Relational Database?
**Answer:**
A type of database based on set theory that uses logically related two-dimensional tables (rows and columns) and operations based on relational calculus to store and manage information.

#### 834. 694. What is a SQL clause?
**Answer:**
Clauses are commands that perform specific tasks in SQL and are conventionally written in capital letters. Common examples include CREATE TABLE, SELECT, INSERT INTO, VALUES, ALTER TABLE, DELETE FROM, and UPDATE.

#### 835. 695. What is a SQL-OS Scheduler?
**Answer:**
A component of SQL Server's operating system abstraction layer that manages the execution and scheduling of tasks on a single logical processor.

#### 836. 696. What is a Star Schema?
**Answer:**
A star schema is a relational database design for data warehouses consisting of a central 'Fact' table (containing metrics/measures) connected to multiple 'Dimension' tables (containing descriptive attributes).

#### 837. 697. What is a Stored Procedure?
**Answer:**
A Stored Procedure is a collection of SQL statements grouped together and stored in the database. It can be executed as a single unit, which improves performance, reusability, and maintainability by avoiding redundant code.

#### 838. 698. What is a Unique key?
**Answer:**
A Unique key constraint ensures that all values in a column (or set of columns) are distinct across the table. Unlike a primary key, it allows for one NULL value (depending on the RDBMS implementation).

#### 839. 699. What is a VIEW?
**Answer:**
A VIEW is a saved SQL query that you can refer to like an ordinary table. It provides a way to abstract complex queries or represent specific subsets of data without having to rewrite the query each time.





## 📂 Category: Joins & Set Operators (8 cards)



### 🟢 Junior Level

#### 840. 7. Can 'ALL' and 'ANY' SQL operators be replaced?
**Answer:**
Yes, 'ALL' and 'ANY' operators can always be replaced by 'EXISTS' and 'NOT EXISTS' clauses.

#### 841. 70. Explain the XPath expression //Book[@Price < 90].
**Answer:**
// selects all Book elements at any level in the document, and [@Price < 90] filters those elements where the Price attribute is less than 90.

#### 842. 700. What is a cardinality estimator?
**Answer:**
A cardinality estimator is a component of the SQL query optimizer that predicts the number of rows that will result from a specific query operator or plan.

#### 843. 701. What is a column in a relational database?
**Answer:**
A column is a structural component of a table that represents a specific set of data values of a particular data type for every row.

#### 844. 702. What is a correlated subquery?
**Answer:**
A subquery that references columns from the outer query. It is evaluated once for each row processed by the outer query, often used with EXISTS or NOT EXISTS to check for relational conditions.

#### 845. 703. What is a data anomaly in a database?
**Answer:**
An anomaly is a condition where inconsistent changes exist in a database. It occurs when data redundancy leads to maintenance issues, such as failing to update an address in all locations where it is stored.

#### 846. 704. What is a data dictionary?
**Answer:**
A data dictionary is a DBMS component that contains the metadata, logical structure, data definitions, characteristics, and relationships for the information in a database.

#### 847. 705. What is a database Session?
**Answer:**
A session represents an active connection to the database server, acting as the internal state container for an external user or application connection.

#### 848. 706. What is a database Trigger?
**Answer:**
A special type of stored procedure that executes automatically in response to specific events (like INSERT, UPDATE, or DELETE) on a particular table.

#### 849. 707. What is a database View and how do you use it?
**Answer:**
A view is a virtual table based on the result-set of an SQL statement. It allows you to simplify complex queries, enforce security by restricting column access, and provide consistent data representations. You create one using 'CREATE VIEW view_name AS SELECT ...' and query it like a regular table.

#### 850. 708. What is a database View?
**Answer:**
A View is a virtual table defined by a SELECT query. It extracts data from physical tables and presents it as a dynamic result set; it is non-persistent and does not store data itself.

#### 851. 709. What is a database connection?
**Answer:**
A communication link established from an external source or application to the database management system.

#### 852. 71. Explain the common types of joins in SQL.
**Answer:**
INNER JOIN returns rows with matches in both tables. LEFT JOIN returns all rows from the left table plus matching rows from the right. RIGHT JOIN returns all rows from the right table plus matching rows from the left. FULL JOIN returns all rows when there is a match in either table.

#### 853. 710. What is a database package?
**Answer:**
A package is a collection of procedures, functions, variables, and SQL statements that are grouped together and stored as a single program unit in the database.

#### 854. 711. What is a database staging area?
**Answer:**
A staging area is a temporary storage location used during the ETL process to hold data extracted from source systems. It allows for data transformation, cleansing, and validation before the data is loaded into the final production data warehouse.

#### 855. 712. What is a database system development feedback loop?
**Answer:**
The process of finalizing a database development through multiple iterations of trial and error.

#### 856. 713. What is a database table and how do you perform basic queries on it?
**Answer:**
A table is a structure with named columns and rows where data is stored. Each row must contain values matching the defined column data types. Use 'SELECT * FROM TableName' to retrieve all columns and rows.

#### 857. 714. What is a database table?
**Answer:**
A table is a database object where data is stored in a structured format with named columns and typed rows. All rows in a table must adhere to the same number of columns and data types, and the data is retrieved using SELECT statements.

#### 858. 715. What is a database table?
**Answer:**
A table is a collection of data organized into rows and columns, also known as a relation.

#### 859. 716. What is a database trigger?
**Answer:**
A trigger is a database object that automatically executes a defined set of actions in response to specific events (like INSERT, UPDATE, or DELETE) occurring on a particular table or view.

#### 860. 717. What is a database trigger?
**Answer:**
A stored program that automatically executes (or 'fires') in response to specific events (like INSERT, UPDATE, or DELETE) on a particular table or view.

#### 861. 718. What is a database worker?
**Answer:**
A worker is a thread or process directed by the scheduler to perform specific tasks or queries.

#### 862. 719. What is a database?
**Answer:**
A database is a set of logically related data. The way they relate is dependent on the data model used.

#### 863. 72. Explain the comparison, null, pattern match, range, and set membership conditions in a WHERE clause.
**Answer:**
Comparison: Compares an expression to another. Null: Tests if a value is unknown. Pattern match: Checks if a string matches a specific format (e.g., LIKE). Range: Checks if a value falls within a specific span (e.g., BETWEEN). Set membership: Checks if a value exists within a provided set (e.g., IN).

#### 864. 720. What is a deficiency of UML regarding object relationships?
**Answer:**
A slight deficiency of UML is that it can only capture at most one relationship between two objects (e.g., a student cannot apply to the same college twice for different majors using only standard association modeling).

#### 865. 721. What is a domain constraint?
**Answer:**
A domain constraint limits the valid set of values that can be stored in an attribute (column). An example is defining a column as NOT NULL or providing a DEFAULT value constraint.

#### 866. 722. What is a fact in data modeling?
**Answer:**
A central component of a multi-dimensional model containing measures for analysis. Types include Additive, Semi-additive, and Non-additive facts.

#### 867. 723. What is a forwarding pointer?
**Answer:**
A forwarding pointer is a pointer used in a heap-organized table to redirect to a row's new location if it has moved (e.g., due to an update that caused row migration).

#### 868. 724. What is a general constraint?
**Answer:**
A general constraint (e.g., CHECK constraint) defines a condition on the range of allowed values for specific attributes, such as requiring an age column to be between 16 and 100.

#### 869. 725. What is a hash_warning in SQL Server?
**Answer:**
A hash_warning is an extended event triggered when a hash join or hash aggregation operation exceeds the available memory grant, forcing the operation to spill data to tempdb (disk).

#### 870. 726. What is a join table?
**Answer:**
A junction or associative table used to resolve many-to-many relationships by storing the primary keys of the two tables it links.

#### 871. 727. What is a join table?
**Answer:**
A join table is a table specifically designed to manage relationships between two or more other tables, commonly used to implement many-to-many relationships.

#### 872. 728. What is a key in the relational model?
**Answer:**
A key is a set of attributes (or a single attribute) that defines all other attributes (functional dependency aspect) and serves as a unique identifier for each tuple, ensuring rows are never duplicated.

#### 873. 729. What is a logical read in database performance monitoring?
**Answer:**
A logical read is a query statistic representing the process of reading a data page from the database buffer cache (RAM) rather than from the physical disk.

#### 874. 73. Explain the difference between COUNT(*), COUNT(column_name), and COUNT(DISTINCT column_name).
**Answer:**
COUNT(*) counts all rows including those with NULLs. COUNT(column_name) counts all non-null values in that column. COUNT(DISTINCT column_name) counts only the unique, non-null values in that column.

#### 875. 730. What is a many-to-many relationship in database design?
**Answer:**
A many-to-many relationship exists when multiple records in one table are associated with multiple records in another table. In relational databases, this is implemented using a junction (or link) table that contains foreign keys referencing the primary keys of both related tables.

#### 876. 731. What is a many-to-many relationship?
**Answer:**
A many-to-many relationship occurs when multiple records in one table relate to multiple records in another table. These are implemented using a junction (join) table.

#### 877. 732. What is a multi-valued dependency (MVD)?
**Answer:**
A multi-valued dependency (MVD), or 'tuple-generating dependency', occurs when the presence of one or more rows in a table implies the presence of other rows to maintain consistency. If tuples (a, b, c) and (a, d, e) exist, (a, b, e) and (a, d, c) must also exist. MVDs identify data redundancy and are addressed during Fourth Normal Form (4NF) normalization.

#### 878. 733. What is a nested query (subquery) in SQL?
**Answer:**
A subquery is a query embedded within another query. The innermost query is evaluated first. It can be used in WHERE, FROM, or SELECT clauses. Example: SELECT CustomerNumber FROM Customer WHERE EXISTS (SELECT * FROM Purchase WHERE Customer.CustomerNumber = Purchase.CustomerNumber AND ArticleNumber = (SELECT ArticleNumber FROM Article WHERE Description = 'HIFI-Anlage'));

#### 879. 734. What is a partial dependency and which normal form is it associated with?
**Answer:**
A partial dependency occurs when a non-prime attribute is functionally dependent on only part of a composite primary key. This violates Second Normal Form (2NF).

#### 880. 735. What is a physical read in database performance monitoring?
**Answer:**
A query statistic indicating that a data page was retrieved directly from disk (I/O) rather than from the memory cache (buffer pool).

#### 881. 736. What is a potential issue with (S)GAM pages in tempdb?
**Answer:**
They can become a contention bottleneck (latching) in high-concurrency environments because tempdb frequently allocates and deallocates pages for temporary objects.

#### 882. 737. What is a predicate in SQL?
**Answer:**
A predicate is a logical expression in a WHERE or HAVING clause that evaluates to TRUE, FALSE, or UNKNOWN for each record. It acts as a filter to determine which rows should be included in the result set.

#### 883. 738. What is a predicate in SQL?
**Answer:**
A predicate is a boolean expression in a clause (like WHERE or HAVING) that evaluates to TRUE, FALSE, or UNKNOWN for each row, determining if the row should be included in the result set.

#### 884. 739. What is a primary key and how many can a table have?
**Answer:**
A primary key is a constraint that uniquely identifies each row in a table. Each table can have only one primary key (though it may consist of multiple columns as a composite key).

#### 885. 74. Explain the difference between Conceptual, Logical, and Physical data models.
**Answer:**
Conceptual models define the highest-level scope and master entities. Logical models include operational and transactional entities, defined independently of any specific DBMS. Physical models are technology-dependent schemas used to instantiate the actual database.

#### 886. 740. What is a query result set?
**Answer:**
The query result set is the collection of data rows returned by a database query.

#### 887. 741. What is a query_hash?
**Answer:**
A hash value representing the structure of a query, excluding literals, used to identify identical queries even if parameter values differ.

#### 888. 742. What is a record or a row?
**Answer:**
A record, or row, represents an individual entry or a single instance of data stored within a table.

#### 889. 743. What is a recursive stored procedure in SQL Server?
**Answer:**
A recursive stored procedure is a procedure that calls itself either directly or indirectly (mutual recursion). It is used for repetitive problem-solving and can nest up to 32 levels in SQL Server.

#### 890. 744. What is a recursive stored procedure?
**Answer:**
A stored procedure that calls itself until it reaches a defined boundary condition. This allows for repeated execution of logic.

#### 891. 745. What is a relational database?
**Answer:**
A relational database organizes data into tables with predefined relationships between them, typically established through the use of unique identifiers (IDs) to link data across tables.

#### 892. 746. What is a relational database?
**Answer:**
A relational database is a digital database based on the relational model of data, which organizes information into one or more tables (relations) with rows and columns.

#### 893. 747. What is a result-set?
**Answer:**
The temporary table or collection of rows returned by executing a SELECT statement.

#### 894. 748. What is a row in a table?
**Answer:**
A row (or record) represents a single, complete data entry in a table, containing values for each of the table's defined columns.

#### 895. 749. What is a row overflow page?
**Answer:**
A row overflow page stores variable-length data (such as varchar or nvarchar) that exceeds the storage capacity of a single data page (typically when it exceeds 8000 bytes).

#### 896. 75. Explain the difference between FULL JOIN and CROSS JOIN.
**Answer:**
FULL JOIN returns all rows for which there is a match in either table (combining LEFT and RIGHT outer joins). CROSS JOIN returns the Cartesian product of the two tables, pairing every row of the first table with every row of the second.

#### 897. 750. What is a self-join and how is it used?
**Answer:**
A self-join occurs when a table is joined with itself. It is commonly used to query hierarchical data, such as an Employee table where a column references the Manager's ID within the same table.

#### 898. 751. What is a semi-join?
**Answer:**
A logical operation that returns rows from the first table only if there is at least one match in the second table, without producing duplicates from the second table.

#### 899. 752. What is a sort_warning?
**Answer:**
An extended event triggered by the SQL Server engine when a sort operation (such as during a join or order by) exceeds the allocated memory, forcing it to spill to TempDB.

#### 900. 753. What is a star schema in the context of OLAP?
**Answer:**
A star schema is a type of relational schema used in OLAP applications, consisting of a central fact table surrounded by dimension tables.

#### 901. 754. What is a subquery in SQL?
**Answer:**
A subquery is an inner SELECT statement whose results are used by the outer query to help determine the final result set.

#### 902. 755. What is a subquery, where can it be used, and what are its common use cases?
**Answer:**
A subquery is a query nested within another SQL statement. They can reside in the SELECT clause (often for correlated calculations), the FROM clause (as a derived table), or the WHERE clause (filtering). They are useful when you need to perform calculations with aggregates (like MAX, SUM) without applying them to the entire result set, or to filter data based on results from another table.

#### 903. 756. What is a subquery?
**Answer:**
A subquery is a complete SELECT statement nested within another SQL query (such as SELECT, INSERT, UPDATE, or DELETE).

#### 904. 757. What is a temporary table in SQL Server, how is it created, and when is it deleted?
**Answer:**
A temporary table is stored in the 'tempdb' system database. Session-level temporary tables (prefix '#') are deleted when the creating session ends. Global temporary tables (prefix '##') are available to all sessions and are deleted when the last session referencing them closes. They are created using 'SELECT INTO #TempName' or 'CREATE TABLE #TempName'.

#### 905. 758. What is a theta-join?
**Answer:**
A theta-join is a join operation where the predicate uses comparison operators other than equality (i.e., it does not use '=').

#### 906. 759. What is a transaction?
**Answer:**
A transaction bundles multiple operations into a single, atomic unit. It ensures the ACID property: either all operations within the transaction succeed, or none of them do. Concurrent transactions are isolated, meaning they cannot see the incomplete, intermediate states of other ongoing transactions.

#### 907. 76. Explain the difference between JOIN types (e.g., INNER, LEFT, RIGHT) using the Invoices/Customers scenario.
**Answer:**
INNER JOIN returns only rows with matches in both tables. LEFT JOIN returns all rows from the left table and matched rows from the right (or NULL if no match). RIGHT JOIN returns all rows from the right table and matched rows from the left (or NULL if no match). Using RIGHT JOIN with WHERE column IS NULL identifies rows in the right table that do not have a corresponding record in the left table.

#### 908. 760. What is a transformation rule in the context of database query processing?
**Answer:**
A transformation rule is a rule that maps logical or physical operations into other equivalent operations, often used by query optimizers to find more efficient execution plans.

#### 909. 761. What is a transitive dependency in database normalization?
**Answer:**
A transitive dependency occurs when a non-prime attribute is dependent on another non-prime attribute, rather than directly on the primary key.

#### 910. 762. What is a transitive dependency?
**Answer:**
A transitive dependency occurs when there are functional dependencies such that X→Y and Y→Z, where X is the primary key. Consequently, X→Z is a transitive dependency. A transitive dependency exists when a non-prime attribute determines another non-prime attribute, violating Third Normal Form (3NF).

#### 911. 763. What is a trigger?
**Answer:**
A trigger is a specialized stored procedure that automatically executes ('fires') in response to specific events on a table or view, such as INSERT, UPDATE, or DELETE operations.

#### 912. 764. What is a view, and what is the 'WITH CHECK OPTION' clause?
**Answer:**
A view is a virtual table representing a subset of columns or rows from one or more base tables. The 'WITH CHECK OPTION' clause ensures that any data modified or inserted through the view must satisfy the criteria defined in the view's WHERE clause.

#### 913. 765. What is a window function?
**Answer:**
A window function performs a calculation across a set of table rows related to the current row. Unlike regular aggregate functions, window functions do not collapse rows into a single output row; each row retains its separate identity while still accessing result data from the defined 'window'.

#### 914. 766. What is an 'Extended Event' in SQL Server?
**Answer:**
An extended event is an event triggered by a specific circumstance that provides access to a large amount of event data. They generally do not log sensitive SQL text keywords like 'password' or 'session_id'.

#### 915. 767. What is an 'exchange_spill' in SQL Server?
**Answer:**
An 'exchange_spill' is an Extended Event that occurs when parallel query execution processes run out of allocated memory (specifically in the exchange buffers) and are forced to spill data to the tempdb.

#### 916. 768. What is an 'extent' in SQL Server?
**Answer:**
An extent consists of 8 physically contiguous pages.

#### 917. 769. What is an Enum in SQL?
**Answer:**
An ENUM (Enumeration) is a data type that allows a column to store one value from a predefined list of string values.

#### 918. 77. Explain the differences between Conceptual, Logical, and Physical data models.
**Answer:**
Conceptual: High-level business constructs. Logical: Entities, attributes, and relationships, platform-independent. Physical: Concrete implementation details like tables, columns, constraints, data types, indexes, and triggers.

#### 919. 770. What is an Equijoin?
**Answer:**
An Equijoin is a type of join that links tables based on the equality operator ('=') between columns, typically involving the primary key of one table and the foreign key of another.

#### 920. 771. What is an IAM and an IAM chain?
**Answer:**
IAM stands for Index Allocation Map. An IAM chain is a linked list of IAM pages that track the extents allocated to a single database entity (table or index).

#### 921. 772. What is an Identity column?
**Answer:**
An Identity column is a property applied to a column that allows the database to automatically generate sequential numeric values for each new row inserted. A start and increment value can be defined. Identity columns do not require manual indexing, as they are typically used for primary keys which are indexed by default.

#### 922. 773. What is an Index?
**Answer:**
An index is a performance tuning structure that allows for faster retrieval of data by creating a sorted pointer structure for specific columns, reducing the need to scan entire tables.

#### 923. 774. What is an Information System in the context of databases?
**Answer:**
An information system refers to the resources and processes that enable the collection, management, control, and dissemination of information.

#### 924. 775. What is an ORDBMS?
**Answer:**
An Object-Relational Database Management System (like PostgreSQL) that combines traditional relational database features (SQL tables) with object-oriented concepts (inheritance, user-defined types, functions).

#### 925. 776. What is an ORM (Object-Relational Mapper)?
**Answer:**
An ORM is a programming technique that acts as an interface between object-oriented programming languages and relational databases, allowing developers to interact with database data using objects rather than raw SQL queries.

#### 926. 777. What is an Outer Join?
**Answer:**
An Outer Join retrieves rows that match the join condition as well as rows that do not match, returning NULL for columns of the table that lacks a match. Types include LEFT, RIGHT, and FULL joins.

#### 927. 778. What is an SQL clause?
**Answer:**
SQL clauses (commands) perform specific tasks such as defining, manipulating, or querying data. Examples include SELECT, INSERT, UPDATE, DELETE, CREATE TABLE, and ALTER TABLE.

#### 928. 779. What is an aggregate function?
**Answer:**
Aggregate functions perform calculations on multiple values to return a single result. Examples include COUNT(), SUM(), AVG(), MIN(), and MAX(). They are often used to group data.

#### 929. 78. Explain the differences between Slicing and Dicing in OLAP cubes.
**Answer:**
Slicing constrains the analysis to a single dimension (e.g., filtering on one attribute). Dicing constrains the analysis to multiple dimensions, effectively extracting a sub-cube by applying multiple filtering criteria simultaneously.

#### 930. 780. What is an aggregate function?
**Answer:**
Aggregate functions process a set of values and return a single scalar value. Examples include COUNT, SUM, AVG, MAX, and MIN, which are often used with the GROUP BY clause to summarize data.

#### 931. 781. What is an anti semi join?
**Answer:**
An anti semi join is a logical operation that returns rows from the first table only when there is no matching row in the second table.

#### 932. 782. What is an association in UML?
**Answer:**
An association is a relationship between objects of two classes.

#### 933. 783. What is an entity-relationship (ER) model?
**Answer:**
An ER model is an abstract representation of a data schema, typically visualized as a diagram (ERD) showing entities as boxes and relationships as connecting lines, defining the associations and dependencies between different data objects.

#### 934. 784. What is an expression language in the context of databases?
**Answer:**
An expression language (also called a compositional language) is a language used to express operations on data, such as relational algebra or XQuery.

#### 935. 785. What is an index spool?
**Answer:**
An index spool is an execution operator that builds a temporary index over a dataset during query execution to optimize performance for that specific query.

#### 936. 786. What is auto-parameterization in an SQL engine?
**Answer:**
It is a process where the SQL server treats ad-hoc queries as if they were stored procedures by automatically replacing constant values with parameters to improve plan reuse.

#### 937. 787. What is bit data used for?
**Answer:**
Bit data is used for defining and storing bit strings, often representing boolean values (0 or 1).

#### 938. 788. What is cardinality in a database?
**Answer:**
Cardinality refers to the numerical relationship between rows in two related tables. Common types include one-to-one, one-to-many, and many-to-many.

#### 939. 789. What is causality tracking?
**Answer:**
A technique where causally connected events are assigned identical identifiers to track the sequence or dependency of operations in distributed systems.

#### 940. 79. Explain the different types of database Normalization (1NF, 2NF, 3NF).
**Answer:**
1NF: No repeating groups and atomic values. 2NF: Meets 1NF and all non-key attributes are fully functionally dependent on the primary key. 3NF: Meets 2NF and has no transitive dependencies (non-key attributes depend only on the primary key).

#### 941. 790. What is column selectivity?
**Answer:**
Selectivity is a property of a column indicating the ratio of unique values to total rows; higher selectivity means fewer rows share the same value, making it more efficient for index usage.

#### 942. 791. What is crow's foot notation?
**Answer:**
A diagramming standard for ER models where symbols on the ends of relationship lines represent minimum and maximum cardinality. Symbols include the ring (zero), dash (one), and the crow's foot (many).

#### 943. 792. What is data flow in the context of query execution plans?
**Answer:**
Data flow refers to the directional movement of data rows through an execution plan, typically visualized as reading the plan from right to left (the direction of data processing).

#### 944. 793. What is data inconsistency in a database?
**Answer:**
Inconsistency occurs when data does not comply with defined constraints or when multiple versions of the same data exist, leading to unreliable or conflicting results during processing.

#### 945. 794. What is data integrity?
**Answer:**
Data integrity ensures accuracy and consistency: Entity (no duplicate rows), Domain (valid column values), Referential (consistent relationships between tables), and User-Defined (custom business rules).

#### 946. 795. What is data redundancy?
**Answer:**
A condition where data is stored across several locations in a database, often intentionally implemented to improve performance or ensure consistency in distributed systems.

#### 947. 796. What is data warehousing?
**Answer:**
A system optimized for reporting and analysis, characterized as subject-oriented, time-variant, non-volatile, and integrated.

#### 948. 797. What is database planning?
**Answer:**
The strategic process of determining how the database lifecycle stages can be realized most efficiently and effectively.

#### 949. 798. What is density in database statistics?
**Answer:**
Density is a statistic computed as 1 / count(distinct), used by the query optimizer to estimate the selectivity of column values.

#### 950. 799. What is entity integrity?
**Answer:**
Entity integrity ensures that each row in a table is uniquely identifiable, typically enforced by a PRIMARY KEY constraint, which prevents null values in key columns.

#### 951. 8. Can CTEs be used for data modification operations like INSERT, UPDATE, or DELETE?
**Answer:**
Yes, Common Table Expressions (CTEs) can be used to perform data modification operations on the underlying tables.

#### 952. 80. Explain the different types of indexes in SQL.
**Answer:**
1. Unique Index: Ensures no two rows have the same value in the indexed column. 2. Clustered Index: Determines the physical order of data in a table; there can be only one per table. 3. Non-Clustered Index: Stores the index in a separate structure from the data, containing pointers to the actual rows; a table can have many.

#### 953. 800. What is external index fragmentation?
**Answer:**
External index fragmentation occurs when index pages do not follow each other logically/physically on an HDD, which can impact performance (though this is less severe on SSDs).

#### 954. 801. What is forced automatic parametrization in SQL Server?
**Answer:**
Forced automatic parametrization is a setting in SQL Server where the query optimizer attempts to parameterize every query to improve plan reuse.

#### 955. 802. What is horizontal scalability?
**Answer:**
Increasing database capacity by adding more servers or nodes, often through a technique called sharding (partitioning data across multiple machines).

#### 956. 803. What is interleaved execution in the context of query optimization?
**Answer:**
It is a process where the query optimizer executes a multi-statement Table-Valued Function (TVF) during the optimization phase to obtain a more accurate execution plan.

#### 957. 804. What is internal index fragmentation?
**Answer:**
It occurs when index pages are not completely filled (less than 100% full), leading to inefficient storage and potential performance degradation.

#### 958. 805. What is lock escalation and how can it be managed?
**Answer:**
Lock escalation occurs when the number of locks on an object exceeds a threshold (e.g., 5000 in SQL Server), causing the engine to convert fine-grained locks (row or page) into a coarser-grained lock (table). This can be managed by keeping transactions short or using query hints like ROWLOCK or PAGLOCK.

#### 959. 806. What is meant by 'control flow' in query execution?
**Answer:**
It refers to the process of reading the execution plan by tracing the actual method calls of the operators during query execution.

#### 960. 807. What is mutual recursion in SQL?
**Answer:**
Mutual recursion occurs when a recursive relation refers to another recursive relation, which then refers back to the first, forming a recursive ring. This is typically used to traverse directed graphs, such as in the Hub and Authority ranking algorithm. Note: Non-deterministic recursion is generally not allowed in SQL standards.

#### 961. 808. What is osstress.exe?
**Answer:**
A Microsoft tool used to perform stress testing on database systems.

#### 962. 809. What is referential integrity and how is it maintained?
**Answer:**
Referential integrity is a constraint that ensures a foreign key value must match an existing primary key value in the parent table. It is enforced via foreign key constraints or can be simulated using triggers.

#### 963. 81. Explain the effect of CASCADE and RESTRICT in authorization revocation.
**Answer:**
RESTRICT prevents the revocation if other privileges depend on it. CASCADE removes the privilege from the target user and recursively removes any other privileges that were granted based on the revoked privilege.

#### 964. 810. What is referential integrity?
**Answer:**
The mechanism ensuring that relationships between tables remain consistent. It prevents the insertion of rows with foreign keys that do not have a corresponding record in the referenced primary table.

#### 965. 811. What is required to determine if a relational schema is in BCNF (Boyce-Codd Normal Form)?
**Answer:**
To determine BCNF compliance, you need the relational schema and the full set of functional dependencies.

#### 966. 812. What is required to implement memory-optimized tables in SQL Server?
**Answer:**
You must create a Memory Optimized Filegroup and add a container of type Filestream to it.

#### 967. 813. What is required when decomposing relations in BCNF or 4th Normal Form?
**Answer:**
It is necessary to calculate the closure of all functional dependencies and multivalued dependencies to ensure all dependencies are preserved and satisfied throughout the decomposition.

#### 968. 814. What is rpc_completed?
**Answer:**
It is an Extended Event triggered when a Remote Procedure Call (RPC) operation has completed.

#### 969. 815. What is simple auto-parameterization?
**Answer:**
A server setting that allows the DBMS to automatically parameterize trivial queries, which helps in reusing execution plans and reducing compilation overhead.

#### 970. 816. What is table inheritance?
**Answer:**
A feature in some ORDBMS (like PostgreSQL) allowing one table to inherit columns and characteristics from a parent table. Child tables also contain the data defined in the parent, supporting object-oriented database design patterns.





## 📂 Category: Database Programmability (1 cards)



### 🟡 Mid Level

#### 971. 817. What is the 'OPTIMIZE FOR UNKNOWN' query hint?
**Answer:**
A query hint that instructs the query optimizer to use a plan based on average statistics rather than parameter-specific values.

#### 972. 818. What is the 'Read Committed Snapshot' isolation level?
**Answer:**
In this isolation level, data is copied to tempdb before being read, allowing for consistent reads without blocking write operations.

#### 973. 819. What is the 'cost threshold for parallelism' in SQL Server?
**Answer:**
A server-level setting that specifies the minimum cost required for a query plan to be considered for parallel execution.

#### 974. 82. Explain the normalization rules (1NF, 2NF, 3NF) using Codd's rule.
**Answer:**
The data depends on the key (1NF), the whole key (2NF), and nothing but the key (3NF).

#### 975. 820. What is the 'optimize for ad hoc workloads' setting?
**Answer:**
A SQL Server configuration that stores only a small compiled plan stub on the first execution of a batch, reducing plan cache bloat.

#### 976. 821. What is the 'tipping point' in SQL Server indexing?
**Answer:**
The tipping point is the specific threshold of I/O operations (percentage of rows) at which the query optimizer decides that performing an index seek is less efficient than performing a full table scan.

#### 977. 822. What is the 'tipping point' in database page estimation?
**Answer:**
The tipping point is generally between 30% and 33% of table pages. For extremely small rows (such as many-to-many link tables), it is closer to 25%.

#### 978. 823. What is the Adaptive Join operator?
**Answer:**
An operator that dynamically chooses between a nested loop or a hash match join based on the actual number of rows processed during execution.

#### 979. 824. What is the Algebraizer and the Algebraizer Tree?
**Answer:**
The Algebraizer is a component of the relational engine that transforms a parser tree into an algebraizer tree. The algebraizer tree represents the structural plan of data joins and data sources for a query.

#### 980. 825. What is the BETWEEN operator?
**Answer:**
The BETWEEN operator selects values within a given range, inclusive of the start and end values.

#### 981. 826. What is the BETWEEN operator?
**Answer:**
The BETWEEN operator selects values within a specified range. It is inclusive, meaning both the start and end values are included in the results. It works with numbers, text, and dates.

#### 982. 827. What is the Bitmap operator?
**Answer:**
An operator used for efficient multi-threaded filtering, often used to improve join performance in parallel plans.

#### 983. 828. What is the CALL statement used for?
**Answer:**
The CALL statement is used to execute a stored procedure in databases that support it (such as MySQL or Oracle).

#### 984. 829. What is the CXCONSUMER wait type in SQL Server?
**Answer:**
CXCONSUMER is a wait type introduced in SQL Server 2017 to track threads waiting for parallel process data from a producer thread in a parallel query plan.

#### 985. 83. Explain the primary SQL clauses: SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY.
**Answer:**
SELECT: Specifies columns to return. FROM: Specifies tables. WHERE: Filters individual rows. GROUP BY: Groups rows by column values. HAVING: Filters groups. ORDER BY: Sorts the final result set.

#### 986. 830. What is the DEFAULT constraint?
**Answer:**
The DEFAULT constraint provides a default value for a column if no value is specified during an insert operation. It can be defined at table creation or added to an existing column using the ALTER TABLE statement.

#### 987. 831. What is the DELETE command?
**Answer:**
The DELETE command is used to remove existing rows from a table, often constrained by a WHERE clause to target specific records.

#### 988. 832. What is the DROP TABLE command?
**Answer:**
The DROP TABLE command is a DDL operation used to remove an entire table structure and all its associated data from the database.

#### 989. 833. What is the Double Precision data type?
**Answer:**
A numeric data type that stores approximate floating-point values with up to 15-17 significant decimal digits of precision.

#### 990. 834. What is the ESR (Equality, Sort, Range) Rule for composite index design?
**Answer:**
When designing a composite index for complex queries, order the columns by:



1. **Equality (`=`):** Put exact match columns first (e.g. `tenant_id = 5`).



2. **Sort (`ORDER BY`):** Put ordering columns next (e.g. `ORDER BY created_at DESC`).



3. **Range (`>`, `<`, `LIKE 'abc%'`):** Put range or wildcard columns last.



**Why?** Once an index encounters a range condition (`LIKE` or `>`), it cannot use subsequent columns in the index for exact sorting.

#### 991. 835. What is the Eager Spool operator?
**Answer:**
A spool operator that reads and stores all input rows from its child operator upon the first GetNext() call.

#### 992. 836. What is the FLOWR expression syntax in XQuery?
**Answer:**
FLOWR stands for: For (iteration), Let (variable assignment), Where (filtering), Order by (sorting), and Return (output). For and Let can be interleaved/repeated; only Return is mandatory.

#### 993. 837. What is the Global Allocation Map (GAM) page?
**Answer:**
The GAM page manages extent allocation. It contains flags: 'true' indicates mixed extents with at least one unallocated page, and 'false' indicates uniform extents or completely full mixed extents.

#### 994. 838. What is the Grain of Fact?
**Answer:**
The Grain of Fact (or Fact Granularity) refers to the lowest level of detail represented in a fact table in a data warehouse. It defines what a single row in the table represents (e.g., one transaction, one daily summary).

#### 995. 839. What is the Hash Aggregate operator?
**Answer:**
An aggregation operator that uses a hash table to group data when the input is not pre-sorted.

#### 996. 84. Explain the use of single and double quotation marks in SQL.
**Answer:**
Single quotes are used for string literals. Double quotes are generally used for identifiers (like table or column names) that contain special characters or need to be case-sensitive, though this behavior can vary by RDBMS.

#### 997. 840. What is the IN operator in SQL?
**Answer:**
The IN operator allows you to specify multiple values in a WHERE clause, acting as shorthand for multiple OR conditions.

#### 998. 841. What is the IN operator?
**Answer:**
The IN operator allows you to specify multiple values in a WHERE clause, acting as shorthand for multiple OR conditions. It can also be used to filter based on the results of a subquery.

#### 999. 842. What is the INSERT INTO SELECT statement?
**Answer:**
The INSERT INTO SELECT statement copies data from one table and inserts it into an existing destination table.

#### 1000. 843. What is the Key Lookup operator?
**Answer:**
An operator that retrieves non-indexed columns by looking up the clustered index (or base table) using a pointer from a non-clustered index.

#### 1001. 844. What is the LIKE operator?
**Answer:**
The LIKE operator is used in a WHERE clause to search for a specified pattern in a column, typically using wildcards like % or _.

#### 1002. 845. What is the Lazy Spool operator?
**Answer:**
A spool operator that reads rows from its input only as they are requested by the parent operator.

#### 1003. 846. What is the Leftmost Prefix Rule in composite indexing?
**Answer:**
When using a composite index on multiple columns, e.g. `(A, B, C)` (`CREATE INDEX idx_abc ON users (tenant_id, status, created_at)`):



- **Works for:** `WHERE tenant_id = 1`, `WHERE tenant_id = 1 AND status = 'active'`, etc.



- **Fails (skips index):** `WHERE status = 'active'` (because column `A` is skipped).



- **Rule:** Always put the most frequently filtered column or tenant/parent ID first in composite indexes.

#### 1004. 847. What is the MIN_GRANT_PERCENT query hint?
**Answer:**
A hint that sets the minimum desired memory grant percentage for a query.

#### 1005. 848. What is the NEWSEQUENTIALID() function?
**Answer:**
A SQL function that generates a sequential UniqueIdentifier, often used for primary keys to minimize fragmentation in clustered indexes compared to NEWID().

#### 1006. 849. What is the NOT NULL constraint?
**Answer:**
The NOT NULL constraint ensures that a column cannot contain NULL values, forcing the application to provide a valid value during insertion or updates.

#### 1007. 85. Find all records in the movie table with a title beginning with a letter A through J.
**Answer:**
SELECT * FROM movie WHERE title BETWEEN 'A' AND 'J'; or SELECT * FROM movie WHERE title LIKE '[A-J]%';

#### 1008. 850. What is the NOT predicate?
**Answer:**
The NOT operator is a logical operator used to negate a predicate. In SQL, it operates within three-valued logic (TRUE, FALSE, or UNKNOWN/NULL).

#### 1009. 851. What is the Nested Loop operator?
**Answer:**
A join operator that iterates through the outer input and, for each row, performs a scan or lookup on the inner input.

#### 1010. 852. What is the OPTION (FAST N) query hint?
**Answer:**
A hint that tells the query optimizer to optimize for retrieving the first N rows as quickly as possible.

#### 1011. 853. What is the OPTION (NO_PERFORMANCE_SPOOL) hint?
**Answer:**
A hint that instructs the query optimizer to avoid using a performance spool operator in the query execution plan.

#### 1012. 854. What is the OPTION (QUERYRULEOFF) hint?
**Answer:**
A hint used to disable specific transformation rules used by the Query Optimizer during plan generation.

#### 1013. 855. What is the OPTION (QUERYTRACEON XYZ) hint?
**Answer:**
A hint used to enable a specific trace flag only for the scope of the individual query.

#### 1014. 856. What is the Pareto Principle (80/20 rule) in the context of databases?
**Answer:**
A concept stating that approximately 80% of effects come from 20% of causes. In databases, this is often applied to performance tuning, where 80% of system performance issues are caused by 20% of the queries.

#### 1015. 857. What is the RID Lookup operator?
**Answer:**
An operator used to retrieve row data from a heap (non-clustered table) using a Row Identifier (RID).

#### 1016. 858. What is the SPARSE column property?
**Answer:**
A column property where NULL values consume zero space. Non-null values occupy slightly more space than a standard column (typically an additional 4 bytes) to manage the storage mapping.

#### 1017. 859. What is the SQL AUTO INCREMENT property?
**Answer:**
It allows a unique numerical value to be generated automatically when a new record is inserted. In MySQL, this is done via the AUTO_INCREMENT keyword; in SQL Server, it uses the IDENTITY property.

#### 1018. 86. Find each employee's first_name, last_name, city, and state from the employee and location tables using the location_id field.
**Answer:**
SELECT employee.first_name, employee.last_name, location.city, location.state FROM employee INNER JOIN location ON employee.location_id = location.location_id;

#### 1019. 860. What is the SQL Server Query Store?
**Answer:**
A SQL Server feature that logs SQL queries, their execution plans, and performance metrics over time to assist in troubleshooting and performance tuning.

#### 1020. 861. What is the SQL UPDATE command used for?
**Answer:**
The UPDATE command is used to modify existing data in one or more rows of a table based on a specified condition.

#### 1021. 862. What is the STRING_AGG function?
**Answer:**
STRING_AGG is an aggregate function that concatenates string values from multiple rows into a single string, separated by a specified delimiter.

#### 1022. 863. What is the SUM() function?
**Answer:**
SUM() is an aggregate function that returns the total sum of a numeric column. Syntax: SELECT SUM(column_name) FROM table_name WHERE condition;

#### 1023. 864. What is the Stream Aggregate operator?
**Answer:**
An aggregation operator that groups data by streaming, requiring the input to be pre-sorted by the grouping columns.

#### 1024. 865. What is the TRUNCATE TABLE statement?
**Answer:**
The TRUNCATE TABLE statement is used to remove all records from a table while keeping the table structure intact. Syntax: TRUNCATE TABLE table_name;

#### 1025. 866. What is the Table Scan operator?
**Answer:**
An operator that retrieves all rows by scanning the entire table data (heap) without using an index.





## 📂 Category: Subqueries & Aggregations (6 cards)



### 🟢 Junior Level

#### 1026. 867. What is the Transitive rule for Functional Dependencies (FD)?
**Answer:**
The Transitive rule for FD states that if A→B and B→C, then A→C.

#### 1027. 868. What is the Transitivity rule for Functional Dependencies (FD)?
**Answer:**
The Transitivity rule states that if A -> B and B -> C, then A -> C.

#### 1028. 869. What is the UNIQUE constraint in SQL?
**Answer:**
The UNIQUE constraint ensures that all values in a column are distinct. Unlike the PRIMARY KEY constraint (which also enforces uniqueness), a table can have multiple UNIQUE constraints. It can be applied at the column level or the table level.

#### 1029. 87. Find employees by department, displaying department, employee_id, salary, and the calculated average_salary_by_department using a window function.
**Answer:**
SELECT depname, empno, salary, AVG(salary) OVER (PARTITION BY depname) AS average_salary_by_department FROM empsalary;

#### 1030. 870. What is the UPDATE statement?
**Answer:**
The UPDATE statement is used to modify existing data in a table. Syntax: UPDATE table_name SET col1 = val1 WHERE condition;. Warning: If the WHERE clause is omitted, all records in the table will be updated.

#### 1031. 871. What is the [charlist] syntax used for?
**Answer:**
The [charlist] syntax is used in pattern matching (typically with the LIKE operator) to specify a set or range of characters to match at a specific position in a string.

#### 1032. 872. What is the advantage of XSD over DTD regarding pointers?
**Answer:**
XSD supports typed pointers (specifying the target element type for IDREFS), whereas DTDs only support untyped ID/IDREF references.

#### 1033. 873. What is the basic unit of time in SQL Server?
**Answer:**
The microsecond (μsecond).

#### 1034. 874. What is the behavior of a FULL OUTER JOIN?
**Answer:**
A FULL OUTER JOIN returns all rows from both joined tables. If there is no match in one of the tables, the result set contains NULL values for the columns of the table that lacked a match.

#### 1035. 875. What is the characteristic of a column where every row has a different value?
**Answer:**
This is the definition of a unique constraint or a primary key, ensuring entity integrity.

#### 1036. 876. What is the code inside a trigger called?
**Answer:**
The code within a trigger is referred to as the trigger body or the trigger action.

#### 1037. 877. What is the compilation cost of the MERGE statement compared to standard DML?
**Answer:**
The compilation cost of MERGE is significantly higher than that of equivalent individual INSERT, UPDATE, or DELETE statements.

#### 1038. 878. What is the correct SQL statement to return the sum of the spent amount (Samnt) for clients whose name contains 'Simpson'?
**Answer:**
SELECT SUM(Samnt) as SimpsonsSpending FROM Clients WHERE Cname LIKE '%Simpson%';

#### 1039. 879. What is the correct SQL statement to return the sum of the spent amount (Samnt) for the client 'Herb Simpson'?
**Answer:**
SELECT SUM(Samnt) as HerbSpending FROM Clients WHERE Cname IN ('Herb Simpson'); OR SELECT SUM(Samnt) as HerbSpending FROM Clients WHERE Cname = 'Herb Simpson';

#### 1040. 88. Find how many films begin with the letter 'J'.
**Answer:**
SELECT COUNT(*) FROM films WHERE title LIKE 'J%';

#### 1041. 880. What is the correct logical order of the main clauses in a SQL SELECT statement?
**Answer:**
The logical order is SELECT, FROM, WHERE.

#### 1042. 881. What is the correct syntax order when defining columns in a CREATE TABLE statement?
**Answer:**
The standard order is: column_name data_type(size) constraint_name.

#### 1043. 882. What is the danger of an UPDATE statement without a WHERE clause?
**Answer:**
An UPDATE statement without a WHERE clause will apply the change to every single row in the table, which is often an irreversible mistake. Always test the criteria using a SELECT statement first to verify which rows will be affected.

#### 1044. 883. What is the default access mode for transactions if not specified?
**Answer:**
READ WRITE is the default access mode.

#### 1045. 884. What is the default maximum memory grant for a SQL Server query?
**Answer:**
The default maximum memory grant is typically 20% of the total available server memory.

#### 1046. 885. What is the default sort order for SQL records?
**Answer:**
The default order is ascending (ASC).

#### 1047. 886. What is the definition of Third Normal Form (3NF)?
**Answer:**
A table is in 3NF if it is already in Second Normal Form (2NF) and all non-primary fields are dependent only on the primary key (i.e., there are no transitive dependencies).

#### 1048. 887. What is the definition of the Character Data type?
**Answer:**
Character Data represents a sequence of characters from an implementation-defined character set, typically used for text strings (e.g., CHAR, VARCHAR).

#### 1049. 888. What is the delivery order of messages in Service Broker?
**Answer:**
Ordering is guaranteed within a single conversation. If multiple conversations exist, selection is managed by priorities.

#### 1050. 889. What is the difference between % and _ in a LIKE query?
**Answer:**
The '%' wildcard matches any number of characters (zero or more), whereas the '_' wildcard matches exactly one character.

#### 1051. 89. Find in the payments table the customer_id of customers who have spent (amount) at least $110 with the staff_id of 2, grouped by customer.
**Answer:**
SELECT customer_id, SUM(amount) FROM payment WHERE staff_id = 2 GROUP BY customer_id HAVING SUM(amount) > 110; We group by customer_id to get totals and use HAVING to filter the aggregated results.

#### 1052. 890. What is the difference between 'WITH CUBE' and 'WITH ROLLUP' in SQL data warehousing?
**Answer:**
WITH CUBE generates all possible sub-total combinations for the specified attributes. WITH ROLLUP creates hierarchical subtotals, which is more efficient for data with a natural functional dependency (e.g., City -> County -> State).





## 📂 Category: Transactions & Concurrency (28 cards)



### 🔴 Senior Level

#### 1053. 891. What is the difference between 'well-formed' and 'valid' XML?
**Answer:**
A 'well-formed' XML file adheres to basic syntax constructs, while a 'valid' XML file must additionally adhere to a formal schema (DTD or XSD).

#### 1054. 892. What is the difference between BETWEEN and IN operators?
**Answer:**
The BETWEEN operator selects values within a specified range (inclusive). The IN operator determines if a value matches any element in a provided list or set.

#### 1055. 893. What is the difference between CPU time and Elapsed time?
**Answer:**
CPU time is the duration the request was actively running on the processor. Elapsed time is the total wall-clock time from start to finish, including wait times, processing, and data transfer.

#### 1056. 894. What is the difference between CREATE TABLE, INSERT INTO, and SELECT DISTINCT?
**Answer:**
CREATE TABLE defines a new table structure. INSERT INTO adds new rows to a table. SELECT DISTINCT retrieves data while filtering out duplicate result rows.

#### 1057. 895. What is the difference between Clustered and Non-Clustered Indexes?
**Answer:**
A Clustered Index determines the physical order of data in a table; a table can have only one. Non-Clustered Indexes are separate structures containing pointers to the data rows; a table can have multiple. Clustered indexes are generally faster for range retrievals.

#### 1058. 896. What is the difference between Composition and Aggregation in UML?
**Answer:**
Composition (represented by a filled diamond) implies a strong ownership where the component cannot live without the container (typically 1..1). Aggregation (represented by an open diamond) implies a weaker association (typically 0..1) where the component can exist independently.

#### 1059. 897. What is the difference between DELETE+OUTPUT and SELECT+DELETE?
**Answer:**
DELETE+OUTPUT is an atomic operation that returns the deleted rows within a single statement. SELECT+DELETE requires a manual transaction to ensure consistency, which can lead to row locking and blocking issues.

#### 1060. 898. What is the difference between FULL OUTER JOIN and UNION?
**Answer:**
FULL OUTER JOIN combines result sets horizontally based on join predicates, whereas UNION combines result sets vertically by stacking rows from two or more SELECT statements.

#### 1061. 899. What is the difference between Hash Match joins and Merge joins?
**Answer:**
Hash match joins can handle unsorted data by building a hash table in memory. Merge joins require inputs to be pre-sorted on the join keys to perform efficiently.

#### 1062. 9. Can a primary key consist of multiple attributes?
**Answer:**
Yes, a key can be composed of one or several attributes (columns), which is then referred to as a composite key.

#### 1063. 90. Find the app in the app table with the most downloads.
**Answer:**
SELECT MAX(downloads) FROM app;

#### 1064. 900. What is the difference between INNER JOIN and OUTER JOIN?
**Answer:**
An INNER JOIN returns only rows where there is a match in both tables based on the join condition. An OUTER JOIN (LEFT, RIGHT, or FULL) returns matched rows plus unmatched rows from one or both tables, filling missing side values with NULL.





### 🟡 Mid Level

#### 1065. 901. What is the difference between MS SQL and other database engines like Oracle or MySQL?
**Answer:**
They are different database management systems (RDBMS) developed by different companies (Microsoft, Oracle, etc.). While they share common SQL standards, each has proprietary extensions, syntax variations, and unique performance optimization features.

#### 1066. 902. What is the difference between NULL, zero, and blank space?
**Answer:**
A NULL value represents the absence of data ('unknown' or 'not applicable'). Zero is a numeric value, and a blank space is a character string (length 1). They are not equivalent.

#### 1067. 903. What is the difference between OLAP and OLTP databases?
**Answer:**
OLAP (Online Analytical Processing) is designed for complex, large-scale analytical queries on historical data for business intelligence. OLTP (Online Transaction Processing) is designed for high-concurrency, near real-time transactional processing like banking or e-commerce.

#### 1068. 904. What is the difference between OLTP and OLAP?
**Answer:**
OLTP (Online Transaction Processing) is optimized for short, frequent transactions and simple queries on small data sets. OLAP (Online Analytical Processing) is optimized for long-running, complex analytical queries across large data volumes. Data warehousing often involves moving data from OLTP sources to an OLAP warehouse for analysis.

#### 1069. 905. What is the difference between Primary Keys and Foreign Keys?
**Answer:**
A Primary Key is a unique identifier for a specific row in a table. A Foreign Key is a column or set of columns that creates a link between two tables, ensuring referential integrity.

#### 1070. 906. What is the difference between READ ONLY and READ WRITE transaction qualifiers?
**Answer:**
These qualifiers indicate the nature of a transaction: READ ONLY specifies that the transaction will only perform read operations, while READ WRITE indicates that the transaction involves both read and write operations.

#### 1071. 907. What is the difference between SQL and NoSQL?
**Answer:**
SQL databases are relational, use predefined schemas, and focus on ACID compliance. NoSQL databases are non-relational, support dynamic schemas (documents/key-value), and are often optimized for horizontal scalability and large, unstructured datasets.





### 🔴 Senior Level

#### 1072. 908. What is the difference between SQL and PL/SQL?
**Answer:**
SQL is a declarative query language for set-based operations. PL/SQL (Procedural Language/SQL) is an extension of SQL that adds procedural features like loops, variables, and conditional logic to build full programs.

#### 1073. 909. What is the difference between SQL, MySQL, and SQL Server?
**Answer:**
SQL is the standardized query language used to interact with databases. MySQL and SQL Server are specific Relational Database Management Systems (RDBMS) that implement the SQL language. MySQL is open-source, while SQL Server is a proprietary product from Microsoft.

#### 1074. 91. Find the customer with the highest customer_id whose first_name starts with 'E' and has an address_id lower than 500.
**Answer:**
SELECT first_name, last_name FROM customers WHERE first_name LIKE 'E%' AND address_id < 500 ORDER BY customer_id DESC LIMIT 1;

#### 1075. 910. What is the difference between UNION and UNION ALL?
**Answer:**
UNION combines result sets from multiple SELECT statements and removes duplicate rows. UNION ALL combines results but preserves all rows, including duplicates, making it more performant.

#### 1076. 911. What is the difference between UNION and UNION ALL?
**Answer:**
UNION merges result sets from two structurally compatible tables and removes duplicate records from the final output. UNION ALL also merges the results but includes all duplicate records, making it more performant.

#### 1077. 912. What is the difference between WHERE and HAVING clauses?
**Answer:**
The WHERE clause filters individual rows before any grouping occurs. The HAVING clause is used to filter groups of rows after the GROUP BY operation has been performed.

#### 1078. 913. What is the difference between WHERE and HAVING clauses?
**Answer:**
The WHERE clause filters rows before grouping occurs. The HAVING clause is used to filter the result set after rows have been grouped by the GROUP BY clause, typically used to filter based on aggregate function results.

#### 1079. 914. What is the difference between a 'predicate' and a 'seek predicate' in an execution plan?
**Answer:**
A 'seek predicate' is used by the engine to navigate the index tree to find specific data. A 'predicate' (or residual predicate) is a filter applied to the rows after they have been retrieved, used for columns not covered by the index key.

#### 1080. 915. What is the difference between a Cross Join and a Natural Join?
**Answer:**
A Cross Join returns the Cartesian product of two tables (all possible combinations). A Natural Join automatically joins tables based on all columns with the same name and data type.

#### 1081. 916. What is the difference between a DBMS and a database system?
**Answer:**
A Database Management System (DBMS) is the software used to manage data. A database system is an organization of components that defines and regulates the collection, storage, management, and use of data, consisting of the DBMS and the actual databases.

#### 1082. 917. What is the difference between a Function and a Stored Procedure?
**Answer:**
Functions must return a value and are typically used in SELECT/WHERE clauses. Stored Procedures do not have to return a value, support input/output parameters, and can contain complex logic like try-catch blocks and DML operations that functions cannot perform.

#### 1083. 918. What is the difference between a Page IO latch and a Page latch?
**Answer:**
A Page IO latch manages access to a data page while it is being transferred from or to disk. A Page latch is used to manage access to a page already residing in memory.

#### 1084. 919. What is the difference between a Primary Key and a Foreign Key?
**Answer:**
A Primary Key is a column or set of columns that uniquely identifies a row in a table (cannot be NULL). A Foreign Key is a field that references the primary key of another table to establish a relationship and ensure referential integrity.

#### 1085. 92. Find the names of the owners of the cat with id 3, using tables cat, owner, and join table cat_owner.
**Answer:**
SELECT owner.name FROM owner INNER JOIN cat_owner ON owner.id = cat_owner.owner_id WHERE cat_owner.cat_id = 3;

#### 1086. 920. What is the difference between a Primary Key and a Unique Key?
**Answer:**
A Primary Key ensures uniqueness and does not allow NULL values. A Unique Key also ensures uniqueness but allows a single NULL value.

#### 1087. 921. What is the difference between a UNIQUE and non-UNIQUE clustered index?
**Answer:**
If a clustered index is non-UNIQUE, the engine automatically adds a hidden integer column (uniquifier) to ensure row uniqueness.

#### 1088. 922. What is the difference between a logical and a physical operator?
**Answer:**
Logical operators describe the algebraic operation to be performed (e.g., Join, Group). Physical operators are the actual algorithms used by the engine to execute these operations (e.g., Hash Match, Nested Loops).

#### 1089. 923. What is the difference between a trivial and non-trivial functional dependency A -> B?
**Answer:**
A dependency is trivial if B is a subset of A. It is non-trivial if B is not a subset of A.

#### 1090. 924. What is the difference between aggregate and scalar functions?
**Answer:**
Aggregate functions evaluate mathematical calculations across multiple rows to return a single result (e.g., MAX(), COUNT(), SUM()). Scalar functions return a single value for each single input value (e.g., UCASE(), NOW()).

#### 1091. 925. What is the difference between attribute-based and tuple-based check constraints?
**Answer:**
Attribute-based constraints are applied to a single column (defined immediately after the attribute). Tuple-based constraints are applied to a set of columns (defined at the end of the table definition) to enforce relationships between attributes.

#### 1092. 926. What is the difference between data mining and data warehousing, and what are common warehouse application types?
**Answer:**
Data warehousing is the process of aggregating data from multiple sources into a common repository for analysis. Data mining is the process of extracting hidden predictive patterns from that data. Applications include Info Processing, Analytical Processing, and Data Mining.





## 📂 Category: Basic SQL & Syntax (44 cards)



### 🟡 Mid Level

#### 1093. 927. What is the difference between forward and backward index scans?
**Answer:**
Forward index scans can be parallelized, whereas backward index scans generally cannot.

#### 1094. 928. What is the difference between nvarchar(100) and nvarchar(max) in MS SQL?
**Answer:**
nvarchar(100) restricts storage to a maximum of 100 Unicode characters. nvarchar(max) allows storage of up to 2GB (or 1 billion characters), making it suitable for large text fields.

#### 1095. 929. What is the difference between row-level and statement-level triggers?
**Answer:**
A row-level trigger executes once for each row affected by the triggering event (e.g., INSERT, UPDATE, DELETE). A statement-level trigger executes only once for the entire SQL statement, regardless of how many rows are affected.

#### 1096. 93. Find the number of apps at each price in the apps table.
**Answer:**
SELECT price, COUNT(*) FROM apps GROUP BY price;

#### 1097. 930. What is the difference between single quotes ('') and double quotes ("") in standard SQL?
**Answer:**
Single quotes are the standard for string literals. Double quotes are typically used for delimited identifiers (like table or column names containing spaces or reserved words) depending on the specific database engine (e.g., PostgreSQL, SQL Server).

#### 1098. 931. What is the difference between system and user databases?
**Answer:**
System databases (e.g., Master, MSDB, TempDB, Model) are default databases required for the SQL Server instance to function correctly and should generally not be modified. User databases are created by developers to store custom application data.

#### 1099. 932. What is the difference between the SELECT and WHERE clauses?
**Answer:**
The SELECT clause determines which columns (fields) are returned in the result, while the WHERE clause filters which rows (records) are included.

#### 1100. 933. What is the difference between the SQL standard transaction level and actual DBMS default implementations?
**Answer:**
While 'Serializable' is the SQL standard default, most modern DBMS implementations use weaker isolation levels by default for performance (e.g., Oracle uses Read Committed, MySQL uses Repeatable Read).

#### 1101. 934. What is the difference between using a Function and a View?
**Answer:**
A view is typically used for virtual tables that may be queried frequently, whereas a function is often used when the data is not required every time the query executes or requires logic/parameters.

#### 1102. 935. What is the difference between well-formed XML and valid XML?
**Answer:**
Well-formed XML refers to XML that follows all the basic syntax rules (e.g., proper closing tags, single root element). Valid XML is well-formed XML that also adheres to a specific document type definition (DTD) or XML schema (XSD) to ensure structural compliance.

#### 1103. 936. What is the difference in categorization between '2002-01-25 20:20:01.001', '2002-01-25', and '22:10:15.3239999'?
**Answer:**
'2002-01-25 20:20:01.001' is a 'datetime' value. '2002-01-25' is a 'date' value. '22:10:15.3239999' is invalid as a standalone date/time type because it lacks date information.

#### 1104. 937. What is the effect of creating a stored procedure with a '#' prefix?
**Answer:**
The procedure is created as a temporary object stored in tempdb.

#### 1105. 938. What is the fastest collation?
**Answer:**
The binary collation (e.g., XY_BIN2) is typically the fastest, as it sorts data based on character code values rather than linguistic rules.

#### 1106. 939. What is the formal definition of Isolation/Serializability in transactions?
**Answer:**
Serializability guarantees that even if operations are interleaved, the final outcome must be equivalent to some sequential (serial) order of transactions. It ensures transactions appear to execute atomically and in isolation.

#### 1107. 94. Find the number of downloads per category.
**Answer:**
SELECT category, SUM(downloads) FROM app GROUP BY category;

#### 1108. 940. What is the function of GAM and SGAM pages in SQL Server?
**Answer:**
GAM (Global Allocation Map) and SGAM (Shared Global Allocation Map) pages are used to track and manage the allocation of extents within a database file, helping the engine find available pages for new objects.

#### 1109. 941. What is the function of sp_recompile?
**Answer:**
A built-in system stored procedure in SQL Server that marks the execution plan of a specific procedure or trigger as invalid, forcing a re-compilation the next time it is executed.

#### 1110. 942. What is the function of the 'WITH ENCRYPTION' option in database programmability?
**Answer:**
The 'WITH ENCRYPTION' option hides the execution plans and source text of stored procedures, functions, or triggers from all users and system logs.

#### 1111. 943. What is the function of the ALTER TABLE statement?
**Answer:**
The ALTER TABLE statement is used to add, delete, or modify columns in an existing table, as well as to add, modify, or drop various constraints on an existing table structure.

#### 1112. 944. What is the function of the Close() method in query execution operators?
**Answer:**
Close() is a method of physical query operators used to terminate processing and release associated resources.

#### 1113. 945. What is the function of the DELETE statement?
**Answer:**
The DELETE statement is used to remove one or more rows from a specified table in the database.

#### 1114. 946. What is the function of the GetNext() method in physical database operators?
**Answer:**
GetNext() is a method of a physical query operator that iterates through and returns the next single row from the operator's input source.

#### 1115. 947. What is the function of the IN operator in a WHERE clause?
**Answer:**
The IN operator allows you to specify multiple values in a WHERE clause, acting as shorthand for multiple OR conditions (e.g., checking if a City is 'Paris' or 'London').

#### 1116. 948. What is the function of the INSERT statement?
**Answer:**
It is used to insert a single row into a table, or to insert an arbitrary number of rows from other tables using a sub-select.

#### 1117. 949. What is the function of the LIKE operator in SQL?
**Answer:**
The LIKE operator is a comparison operator used to check whether an attribute's text value matches a specified string pattern using wildcards (e.g., SELECT Name FROM Customer WHERE Name LIKE 'M%').

#### 1118. 95. Find the number of employees in the employee table with the first_name Lisa or David. Do not use an OR statement.
**Answer:**
SELECT * FROM employee WHERE first_name IN ('Lisa', 'David');

#### 1119. 950. What is the function of the ORDER BY clause in SQL?
**Answer:**
The ORDER BY clause specifies the column(s) used to sort the resulting data set.

#### 1120. 951. What is the function of the READ ONLY transaction state?
**Answer:**
It is used to allow transactions on a temporary table or read-only access to data, ensuring no modifications occur during the transaction.

#### 1121. 952. What is the function of the SUM aggregate function in SQL?
**Answer:**
The SUM() function returns the total sum of all numerical values for a given column or expression.

#### 1122. 953. What is the function of the WITH statement in SQL?
**Answer:**
The WITH statement (Common Table Expression or CTE) defines a temporary result set that can be referenced within a subsequent SELECT, INSERT, UPDATE, or DELETE statement. It is often used to simplify complex, nested queries or to perform recursive operations.

#### 1123. 954. What is the function of the command: ALTER DATABASE ... WITH ROLLBACK IMMEDIATE?
**Answer:**
This command kills all currently running transactions/queries in a database and prevents new ones from starting until the requested database operation is completed.

#### 1124. 955. What is the goal of a good database design regarding Functional Dependencies (FDs)?
**Answer:**
The goal is to obtain a minimal set of completely non-trivial Functional Dependencies such that all FDs of the relation follow from the dependencies in this set.

#### 1125. 956. What is the impact of using indexes on frequently queried attributes?
**Answer:**
Using indexes on frequently queried attributes can provide a massive improvement in query performance.

#### 1126. 957. What is the industry convention for naming SQL identifiers?
**Answer:**
Use lowercase letters for column names and table names to avoid issues with case-sensitivity and quoting in various environments.

#### 1127. 958. What is the lifecycle behavior of temporary objects in stored procedures?
**Answer:**
Upon procedure termination, temporary tables are truncated to one extent, but their statistics are retained.

#### 1128. 959. What is the limitation on row size in SQL Server?
**Answer:**
A single row must fit within a single page, which is 8,060 bytes.

#### 1129. 96. Find the number of records in the app table that have a price of 0.
**Answer:**
SELECT COUNT(*) FROM app WHERE price = 0;

#### 1130. 960. What is the logical order of clauses in a SQL SELECT statement?
**Answer:**
SELECT -> FROM -> WHERE -> GROUP BY -> HAVING -> ORDER BY -> LIMIT.





## 📂 Category: Database Design & Normalization (27 cards)



### 🟢 Junior Level

#### 1131. 961. What is the logical order of keywords in a SQL query?
**Answer:**
The order is: SELECT, FROM, JOIN, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT (or TOP).

#### 1132. 962. What is the minimal information needed when defining a table?
**Answer:**
A table must have a unique Table Name, and at least one Column Name with an associated Data Type.

#### 1133. 963. What is the naming convention 'sp' (e.g., spXXX) in SQL procedures?
**Answer:**
It stands for 'stored procedure'.





## 📂 Category: Joins & Set Operators (24 cards)



### 🟢 Junior Level

#### 1134. 964. What is the nature of a WHERE predicate in a filtered index?
**Answer:**
The WHERE predicate in a filtered index is limited; it only allows simple comparisons and cannot contain subqueries, complex functions, or user-defined logic.

#### 1135. 965. What is the objective of a Data Manipulation Language (DML)?
**Answer:**
DML contains commands used to manipulate data within the database structure, such as SELECT, INSERT, UPDATE, DELETE, COMMIT, and ROLLBACK.

#### 1136. 966. What is the objective of a query language?
**Answer:**
A query language provides a standard interface to a DBMS for expressing requests to retrieve, insert, update, delete data, and manage schema structures and access permissions.

#### 1137. 967. What is the opposite of LIKE?
**Answer:**
NOT LIKE. It is used in a WHERE clause to filter out records that do not match the specified pattern. Example: SELECT * FROM [Grant] WHERE GrantName NOT LIKE 'O%'

#### 1138. 968. What is the output of the SQL Parser?
**Answer:**
The output is a parse tree representing the logical structure of the SQL statement.

#### 1139. 969. What is the potential performance issue when using a filtered index with an IS NULL predicate?
**Answer:**
If the column in the predicate is NULL and is not included in the index key (IK), the query engine may resort to a lookup instead of an index seek, even if the index should ideally be covering. To achieve a seek, the nullable column must be part of the index key.

#### 1140. 97. Find the salary of each employee and the running total of salaries in ascending order.
**Answer:**
SELECT salary, SUM(salary) OVER (ORDER BY salary) AS running_total FROM empsalary;

#### 1141. 970. What is the primary motivation behind the use of triggers?
**Answer:**
The primary motivation is to move monitoring, business logic, or audit requirements from the application layer into the database management system itself.

#### 1142. 971. What is the primary objective of Query Planning/Optimization?
**Answer:**
The main objective is to implement the most efficient use of indexes and execution paths to retrieve data.

#### 1143. 972. What is the primary role of XSLT and what does the acronym stand for?
**Answer:**
XSLT stands for Extensible Stylesheet Language Transformations. It is a language used to transform XML documents into other formats by matching and replacing templates of data.

#### 1144. 973. What is the primary use of Normalization and how does it prevent data anomalies?
**Answer:**
Normalization is the process of structuring a database to reduce data redundancy and improve integrity. It eliminates insert, update, and delete anomalies by breaking tables into smaller, related partitions, ensuring that facts are stored in only one place.

#### 1145. 974. What is the purpose of CREATE INDEX and the 'DROP_EXISTING = ON' option?
**Answer:**
CREATE INDEX generates an index for efficient data retrieval. 'DROP_EXISTING = ON' is a specific command (e.g., in SQL Server) used to overwrite an existing index of the same name.

#### 1146. 975. What is the purpose of DBCC PAGE?
**Answer:**
DBCC PAGE is an undocumented/internal command used to inspect the raw contents of a database data page, typically used for low-level troubleshooting or educational analysis of how data is stored on disk.

#### 1147. 976. What is the purpose of Database Normalization?
**Answer:**
Normalization aims to organize data into relations to eliminate anomalies (insertion, update, deletion) and minimize data redundancy while ensuring no information loss occurs.

#### 1148. 977. What is the purpose of Views in a database?
**Answer:**
Views extend database modularity and provide security by limiting the columns/rows a user can see. They are part of the three-level database architecture: Physical (disk), Conceptual (tables), and Logical (views).

#### 1149. 978. What is the purpose of a CHECK constraint?
**Answer:**
A CHECK constraint limits the range of values that can be placed in a specific column, ensuring data integrity by enforcing boolean conditions.

#### 1150. 979. What is the purpose of a UNIQUE constraint?
**Answer:**
It ensures that all values in a specific column (or set of columns) are different across all rows in the table.

#### 1151. 98. Find the salary of each employee and the total sum of all salaries, displaying both in every row.
**Answer:**
SELECT salary, SUM(salary) OVER () FROM empsalary;

#### 1152. 980. What is the purpose of a foreign key?
**Answer:**
A foreign key is a field (or collection of fields) in one table that uniquely identifies a row of another table or the same table, used to define and enforce referential integrity between tables.

#### 1153. 981. What is the purpose of a mission statement and mission objectives in database planning?
**Answer:**
A mission statement defines the major aims of the database system, while mission objectives identify specific tasks that the system must support to achieve those aims.

#### 1154. 982. What is the purpose of a primary key and how does it relate to foreign keys?
**Answer:**
A primary key is a column (or set of columns) that uniquely identifies every row in a table. A foreign key is a column that refers to the primary key in another table, establishing a relationship between them.

#### 1155. 983. What is the purpose of an SQL Clause (e.g., WHERE, HAVING)?
**Answer:**
SQL clauses are used to filter rows from a result set based on specific conditions, thereby limiting the output to only the relevant records.

#### 1156. 984. What is the purpose of an SQL index and how do you create one?
**Answer:**
Indexes are used to speed up data retrieval/searches. They are created with 'CREATE INDEX index_name ON table_name (column_name);'. Note that indexes can slow down data modification (INSERT/UPDATE/DELETE) because the index itself must be updated, so they should be used judiciously on frequently queried columns.

#### 1157. 985. What is the purpose of an XSLT template for recursive element copying?
**Answer:**
It provides a mechanism to recursively traverse and process XML nodes, allowing for structural transformation or reformatting of the XML document.

#### 1158. 986. What is the purpose of an index in a database?
**Answer:**
An index is a persistent data structure used to significantly accelerate the retrieval of data by allowing the database engine to locate tuples directly without scanning an entire table.

#### 1159. 987. What is the purpose of database transactions and how are they used?
**Answer:**
Transactions group SQL commands into a single atomic unit. They ensure data integrity by either committing all changes or rolling back if an error occurs. Key statements include BEGIN TRANSACTION, COMMIT TRANSACTION, and ROLLBACK TRANSACTION.

#### 1160. 988. What is the purpose of functional dependencies in database systems?
**Answer:**
Functional dependencies define relationships between attributes, which are used for data integrity, storage efficiency/compression, and query optimization. A key property is the combining rule: if A->B1 and A->B2 and ... and A->Bn, then A -> B1, B2, ..., Bn.

#### 1161. 989. What is the purpose of procedures and functions in a database?
**Answer:**
Procedures and functions accept parameters from a calling program to perform a specific set of actions, including modifying and returning data. They promote modularity, extensibility, reusability, maintainability, and abstraction.

#### 1162. 99. Find the salary rank by department of each employee using a window function.
**Answer:**
SELECT depname, empno, salary, RANK() OVER (PARTITION BY depname ORDER BY salary DESC) FROM empsalary;

#### 1163. 990. What is the purpose of square brackets [..] in XPath?
**Answer:**
Square brackets [..] allow for the specification of a condition (predicates) to filter nodes.

#### 1164. 991. What is the purpose of the 'DELETE' statement?
**Answer:**
The DELETE statement is used to remove existing records from a table that match the conditions specified in the WHERE clause.

#### 1165. 992. What is the purpose of the 'SELECT INTO' statement?
**Answer:**
The 'SELECT INTO' statement creates a new table and populates it with the result set of a query. To create an empty table with the schema of another, you can append a WHERE clause that evaluates to false (e.g., WHERE 1=0).

#### 1166. 993. What is the purpose of the 'UPDATE' statement?
**Answer:**
The UPDATE statement is used to modify existing records in a table based on specified conditions provided in the WHERE clause.

#### 1167. 994. What is the purpose of the 'dbo' schema in Microsoft SQL Server, and why are schemas used?
**Answer:**
'dbo' stands for 'database owner' and is the default schema. Schemas are used to organize tables into logical subgroups and to facilitate permission management by allowing security policies to be applied to a group of objects at once.

#### 1168. 995. What is the purpose of the := operator in SQL?
**Answer:**
The := operator is used to assign a value to a variable, typically within the executable part of a PL/SQL block or procedural SQL environment.

#### 1169. 996. What is the purpose of the AS clause?
**Answer:**
The AS clause is used to assign an alias to a column or a table, effectively renaming them in the returned result set or query scope for better readability or to resolve ambiguities.

#### 1170. 997. What is the purpose of the CHECK clause in domain constraints?
**Answer:**
It is used to verify that a value falls within a specified range or meets a defined boolean condition.

#### 1171. 998. What is the purpose of the CHECK constraint?
**Answer:**
The CHECK constraint ensures that all values in a specific column satisfy a defined boolean condition.

#### 1172. 999. What is the purpose of the CREATE DOMAIN statement?
**Answer:**
The CREATE DOMAIN statement is used to define a custom data type with specific constraints (such as CHECK constraints) that can be reused across multiple tables.

