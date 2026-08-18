# PostgreSQL Consolidated Study Guide

A professionally structured study guide compiled from PostgreSQL Anki decks, deduplicated semantically, categorized, and graded by difficulty.

## Deck Metrics
- **Original Deck Cards**: 202
- **Final Deduplicated Cards**: 119

---

## 📂 Category: Advanced & Distributed Databases (7 cards)

### 🟡 Mid Level

#### 1. How do SQL and NoSQL databases scale differently?
**Answer:**
SQL databases are vertically scalable, increasing performance on a single server (CPU, RAM, SSD). NoSQL databases are horizontally scalable, handling more traffic by sharding and adding more servers.

#### 2. What is the difference between SQL and NoSQL?
**Answer:**
SQL databases are relational, use predefined schemas, and focus on ACID compliance. NoSQL databases are non-relational, support dynamic schemas (documents/key-value), and are often optimized for horizontal scalability and large, unstructured datasets.


### 🔴 Senior Level

#### 1. How are NoSQL databases structured compared to relational databases?
**Answer:**
NoSQL databases are typically non-relational and structured as document-based, key-value pairs, graph databases, or wide-column stores.

#### 2. How do SQL and NoSQL databases differ in approach to structure?
**Answer:**
SQL requires predefined schemas, enforcing rigid, uniform structures for data integrity. NoSQL offers dynamic, flexible schemas for unstructured data, allowing unique document structures and easier schema evolution at the cost of strict relational consistency.

#### 3. What is an ORDBMS?
**Answer:**
An Object-Relational Database Management System (like PostgreSQL) that combines traditional relational database features (SQL tables) with object-oriented concepts (inheritance, user-defined types, functions).

#### 4. What is horizontal scalability?
**Answer:**
Increasing database capacity by adding more servers or nodes, often through a technique called sharding (partitioning data across multiple machines).

#### 5. What is vertical scalability?
**Answer:**
Vertical scalability (scaling up) involves increasing the capacity of a single server by adding resources like CPU, RAM, or faster storage (SSD).


## 📂 Category: Basic SQL & Syntax (49 cards)

### 🟢 Junior Level

#### 1. Explain the use of single and double quotation marks in SQL.
**Answer:**
Single quotes are used for string literals. Double quotes are generally used for identifiers (like table or column names) that contain special characters or need to be case-sensitive, though this behavior can vary by RDBMS.

#### 2. Find all records in the movie table with a title beginning with a letter A through J.
**Answer:**
SELECT * FROM movie WHERE title BETWEEN 'A' AND 'J'; or SELECT * FROM movie WHERE title LIKE '[A-J]%';

#### 3. Find the customer with the highest customer_id whose first_name starts with 'E' and has an address_id lower than 500.
**Answer:**
SELECT first_name, last_name FROM customers WHERE first_name LIKE 'E%' AND address_id < 500 ORDER BY customer_id DESC LIMIT 1;

#### 4. Find the number of employees in the employee table with the first_name Lisa or David. Do not use an OR statement.
**Answer:**
SELECT * FROM employee WHERE first_name IN ('Lisa', 'David');

#### 5. Find the three lowest rated movies from the movies table.
**Answer:**
SELECT * FROM movies ORDER BY rating ASC LIMIT 3;

#### 6. How do the LIKE operator and the underscore (_) wildcard function?
**Answer:**
The LIKE operator is used in a WHERE clause to perform pattern matching. The underscore (_) wildcard represents any single unspecified character in the pattern.

#### 7. How do you add a row to a database table and handle the primary key?
**Answer:**
Use 'INSERT INTO table_name (col1, col2) VALUES (val1, val2);'. It is not necessary to explicitly add an ID if you have defined a PRIMARY KEY (which is usually auto-incrementing in databases like PostgreSQL and SQLite).

#### 8. How do you add or remove a column from a table?
**Answer:**
Use the ALTER TABLE command: 'ALTER TABLE table_name ADD COLUMN column_name data_type;' to add a column, and 'ALTER TABLE table_name DROP COLUMN column_name;' to remove one.

#### 9. How do you count entries, filter by nulls, and query for unique values?
**Answer:**
Use 'SELECT COUNT(*) FROM table;' to count all entries. Use 'IS NULL' or 'IS NOT NULL' in a WHERE clause to filter for null values. Use 'SELECT DISTINCT column FROM table;' to retrieve only unique values.

#### 10. How do you edit a row in a table?
**Answer:**
Use the UPDATE command: 'UPDATE table_name SET col_name = new_value WHERE id = target_id;'

#### 11. How do you handle NULL values in SQL?
**Answer:**
NULL represents the absence of a value. To insert a NULL, use the literal NULL. To filter for NULLs, use 'IS NULL' or 'IS NOT NULL' because standard comparison operators (like '=') will fail against NULL.

#### 12. How do you manage output and session state in the SQLite CLI?
**Answer:**
.headers on/.mode column (formatting), .quit (exit). Note: SQL statements must end with a semicolon; if omitted, the CLI waits for further input until one is provided.

#### 13. How do you perform basic selection, sorting, and limiting of results?
**Answer:**
Use 'SELECT col1, col2 FROM table;' to select columns, 'ORDER BY col_name DESC;' to sort in descending order, and 'WHERE' clauses to filter data.

#### 14. Is the BETWEEN clause inclusive or exclusive?
**Answer:**
Inclusive. BETWEEN 'A' AND 'C' includes both A and C.

#### 15. What are common pattern matching and range operators in SQL?
**Answer:**
The LIKE operator uses '%' to match any sequence of characters and '_' to match exactly one character. The NOT LIKE operator negates the condition. The BETWEEN operator is used to filter values within a specific inclusive range.

#### 16. What are common psql utility commands for session management?
**Answer:**
\c (connect to database), \password (change user password), \conninfo (connection details), \q (quit), \? (list all commands).

#### 17. What are the common PostgreSQL CLI meta-commands?
**Answer:**
\h provides help, \c connects to a database, \x toggles expanded (vertical) display, \df lists functions (can be filtered, e.g., \df *name*), and \dn lists schemas.

#### 18. What are the common commands in the SQLite CLI to manage tables and schemas?
**Answer:**
.tables (list tables), .schema (show table/database structure).

#### 19. What are the core datatypes in SQLite?
**Answer:**
SQLite uses four primary storage classes: INTEGER (whole numbers), REAL (floating point/decimal), TEXT (alphanumeric strings), and BLOB (binary data). Other types (like INT or DOUBLE) are mapped to these four.

#### 20. What are the primary PostgreSQL command-line (psql) shortcuts to list database objects?
**Answer:**
\l (databases), \d or \d+ (tables), \dn or \dn+ (schemas), \df (functions), \du (users).

#### 21. What are the primary data types supported by PostgreSQL?
**Answer:**
Boolean, Character (CHAR, VARCHAR, TEXT), Numeric (INT, SERIAL, NUMERIC, REAL), Temporal (DATE, TIME, TIMESTAMP, INTERVAL), UUID, ARRAY, JSON, HSTORE, and specialized types (network/geometric).

#### 22. What does CRUD stand for in the context of database operations?
**Answer:**
CRUD stands for Create, Read, Update, and Delete. These are the four basic functions for persistent storage.

#### 23. What does SQL stand for?
**Answer:**
SQL stands for Structured Query Language.

#### 24. What does a SELECT statement do and what does it return?
**Answer:**
A SELECT statement is used to retrieve data from a database. Specifically, 'SELECT *' returns all columns from the specified table. The output of any SELECT statement is referred to as a result set.

#### 25. What does the BETWEEN clause do?
**Answer:**
The BETWEEN operator filters data within an inclusive range. It works with numeric, text, and date data types.

#### 26. What does the DISTINCT clause do?
**Answer:**
The DISTINCT clause is used with a SELECT statement to return only unique values, effectively removing duplicate rows from the result set.

#### 27. What does the LIMIT clause do?
**Answer:**
The LIMIT clause restricts the number of rows returned by a query to a specified maximum number.

#### 28. What does the ORDER BY clause do?
**Answer:**
The ORDER BY clause sorts the result set by one or more columns, either alphabetically or numerically. Sorting can be specified as ascending (ASC, default) or descending (DESC).

#### 29. What does the UPDATE statement do?
**Answer:**
The UPDATE statement is used to modify existing records in a table. It uses a SET clause to define the new values and a WHERE clause to specify which rows should be updated.

#### 30. What is a SQL clause?
**Answer:**
Clauses are commands that perform specific tasks in SQL and are conventionally written in capital letters. Common examples include CREATE TABLE, SELECT, INSERT INTO, VALUES, ALTER TABLE, DELETE FROM, and UPDATE.

#### 31. What is a database table?
**Answer:**
A table is a collection of data organized into rows and columns, also known as a relation.

#### 32. What is a row in a table?
**Answer:**
A row (or record) represents a single, complete data entry in a table, containing values for each of the table's defined columns.

#### 33. What is the Double Precision data type?
**Answer:**
A numeric data type that stores approximate floating-point values with up to 15-17 significant decimal digits of precision.

#### 34. What is the industry convention for naming SQL identifiers?
**Answer:**
Use lowercase letters for column names and table names to avoid issues with case-sensitivity and quoting in various environments.

#### 35. What is the purpose of the AS clause?
**Answer:**
The AS clause is used to assign an alias to a column or a table, effectively renaming them in the returned result set or query scope for better readability or to resolve ambiguities.

#### 36. What is the purpose of using brackets [ ] in database identifiers?
**Answer:**
Brackets are used to delimit identifiers, allowing the use of reserved keywords or special characters in column or table names. It is generally recommended to avoid such naming conventions, but brackets (or double quotes in standard PostgreSQL) are required to reference these objects.

#### 37. What is the syntax for the LIKE operator?
**Answer:**
The LIKE operator is used for pattern matching. Example: SELECT name FROM movies WHERE name LIKE 'Star%';

#### 38. What is the syntax for the LIMIT clause?
**Answer:**
The LIMIT clause restricts the number of rows returned by a query. Example: SELECT * FROM movies LIMIT 5;

#### 39. What is the syntax for the ORDER BY clause?
**Answer:**
The ORDER BY clause sorts the result set. Example: SELECT * FROM table1 ORDER BY column1 DESC;

#### 40. What is the syntax for writing comments in SQL?
**Answer:**
Use double dashes for single-line comments: -- This is a comment.

#### 41. What is the syntax to manipulate records (INSERT, UPDATE, DELETE)?
**Answer:**
INSERT: INSERT INTO table (col) VALUES (val); UPDATE: UPDATE table SET col = val WHERE condition; DELETE: DELETE FROM table WHERE condition;

#### 42. What is the syntax to reference columns from different tables when names overlap?
**Answer:**
Use table qualification syntax: table_name.column_name. Example: SELECT cats.name, dogs.name FROM cats, dogs;

#### 43. Which data types can be evaluated by the BETWEEN clause?
**Answer:**
The BETWEEN clause can be used with numbers, text (lexicographical order), and dates.

#### 44. Write a query filtering with BETWEEN and additional operators.
**Answer:**
Example: SELECT * FROM movies WHERE year BETWEEN 1990 AND 2000 AND genre = 'comedy';


### 🟡 Mid Level

#### 1. Find websites in the approved_websites table that match the pattern: starts with ftp:// or http://, ends in .org, and has at least one character before the :// and one character after.
**Answer:**
SELECT * FROM approved_websites WHERE url_name LIKE '_%://_%.org';

#### 2. How do you handle special characters (like quotes or wildcards) in SQL queries?
**Answer:**
For single quotes, escape them by adding another single quote (e.g., 'WHERE name LIKE ''%'''). To treat wildcards like % or _ as literals, use brackets in the pattern: 'LIKE ''%[%]%''' or 'LIKE ''%[_]%'''.

#### 3. What does the ONLY clause do in PostgreSQL queries?
**Answer:**
The ONLY keyword restricts a query to the target table specifically, ignoring any descendant tables that might exist due to table inheritance. It is used with SELECT, UPDATE, and DELETE.

#### 4. What is a predicate in SQL?
**Answer:**
A predicate is a boolean expression in a clause (like WHERE or HAVING) that evaluates to TRUE, FALSE, or UNKNOWN for each row, determining if the row should be included in the result set.

#### 5. What is the logical order of clauses in a SQL SELECT statement?
**Answer:**
SELECT -> FROM -> WHERE -> GROUP BY -> HAVING -> ORDER BY -> LIMIT.


## 📂 Category: Database Design & Normalization (27 cards)

### 🟢 Junior Level

#### 1. How should words in a column name be separated?
**Answer:**
Use underscores (snake_case). While brackets can be used for spaces, it is generally considered a bad practice in database design.

#### 2. What are primary and foreign keys?
**Answer:**
A primary key is a column or set of columns that uniquely identifies a row in a table (must be unique and non-NULL). A foreign key is a column or set of columns that establishes a link between data in two tables by referencing the primary key of another table.

#### 3. What does it mean to 'type' a table?
**Answer:**
Typing refers to the process of assigning specific data types (e.g., INTEGER, TEXT, TIMESTAMP) to row definitions when creating or altering a table schema.

#### 4. What is a column in a relational database?
**Answer:**
A column is a structural component of a table that represents a specific set of data values of a particular data type for every row.

#### 5. What is a relational database?
**Answer:**
A relational database is a digital database based on the relational model of data, which organizes information into one or more tables (relations) with rows and columns.

#### 6. What is the syntax to modify database structures (CREATE, ALTER, DROP)?
**Answer:**
To create: CREATE TABLE table_name (id INTEGER PRIMARY KEY, name TEXT); To add a column: ALTER TABLE table_name ADD column_name TEXT; To delete: DROP TABLE table_name;

#### 7. Why is strict data typing important in database design?
**Answer:**
Typing enforces data integrity and provides schema-level control, ensuring only valid data formats are stored in specific columns.


### 🟡 Mid Level

#### 1. Explain the difference between Conceptual, Logical, and Physical data models.
**Answer:**
Conceptual models define the highest-level scope and master entities. Logical models include operational and transactional entities, defined independently of any specific DBMS. Physical models are technology-dependent schemas used to instantiate the actual database.

#### 2. Explain the differences between Conceptual, Logical, and Physical data models.
**Answer:**
Conceptual: High-level business constructs. Logical: Entities, attributes, and relationships, platform-independent. Physical: Concrete implementation details like tables, columns, constraints, data types, indexes, and triggers.

#### 3. How are relationships represented in a join table?
**Answer:**
Each row in a join table represents a single association between records in two other tables, often containing the primary keys of both to map the relationship.

#### 4. How do ER models map to natural language and database structure?
**Answer:**
Entities map to nouns (things/objects), relationships map to verbs (actions between entities), and attributes are details about entities or relationships. Every entity must have a primary key for unique identification.

#### 5. How do you create a many-to-many relationship in a relational database?
**Answer:**
A many-to-many relationship is implemented using a join table (also known as a junction table or associative entity). This table contains foreign keys referencing the primary keys of the two tables being linked.

#### 6. How is cardinality represented in database design?
**Answer:**
Cardinality describes the numerical relationship between entities (e.g., 1:1, 1:N, M:N). It is often visualized in UML or ER diagrams using symbols or numeric ranges (e.g., 0..*, 1..1) to denote optionality and participation constraints.

#### 7. In a relationship between fruit_table and apple_table where fruit_table is the parent: (1) Which table needs a foreign key? (2) What does it correspond to? (3) Which is the child? (4) How is the relationship described?
**Answer:**
(1,2) apple_table must have a foreign key (e.g., fruit_type) that corresponds to the primary key (id) in fruit_table. (3) apple_table is the child; fruit_table is the parent. (4) fruit_table 'has many' apple_table records.

#### 8. What are column constraints and common examples?
**Answer:**
Column constraints are rules enforced on data values. Examples include: PRIMARY KEY (uniqueness/identity), UNIQUE (no duplicates), NOT NULL (required value), and DEFAULT (fallback value).

#### 9. What are insertion, update, and deletion anomalies?
**Answer:**
These occur due to poor schema design (redundancy). Insertion: cannot add data without other data. Update: redundant data requires multiple updates. Deletion: removing a record accidentally deletes unrelated information. Normalization helps resolve these.

#### 10. What happens when you violate referential integrity?
**Answer:**
The database will throw a foreign key constraint violation error. This prevents orphaned records by ensuring that a value inserted into a foreign key column must already exist in the referenced primary key column.

#### 11. What is DDL (Data Definition Language)?
**Answer:**
DDL is a subset of SQL used to define and manage database structures (schema). Commands include CREATE, ALTER, DROP, and TRUNCATE.

#### 12. What is UML in the context of database design?
**Answer:**
Unified Modeling Language (UML) is a standard visual modeling language used to design and document database schemas and system architectures.

#### 13. What is a join table?
**Answer:**
A join table is a table specifically designed to manage relationships between two or more other tables, commonly used to implement many-to-many relationships.

#### 14. What is a many-to-many relationship?
**Answer:**
A many-to-many relationship occurs when multiple records in one table relate to multiple records in another table. These are implemented using a junction (join) table.

#### 15. What is an entity-relationship (ER) model?
**Answer:**
An ER model is an abstract representation of a data schema, typically visualized as a diagram (ERD) showing entities as boxes and relationships as connecting lines, defining the associations and dependencies between different data objects.

#### 16. What is cardinality in a database?
**Answer:**
Cardinality refers to the numerical relationship between rows in two related tables. Common types include one-to-one, one-to-many, and many-to-many.

#### 17. What is crow's foot notation?
**Answer:**
A diagramming standard for ER models where symbols on the ends of relationship lines represent minimum and maximum cardinality. Symbols include the ring (zero), dash (one), and the crow's foot (many).

#### 18. What is referential integrity?
**Answer:**
The mechanism ensuring that relationships between tables remain consistent. It prevents the insertion of rows with foreign keys that do not have a corresponding record in the referenced primary table.

#### 19. What is the syntax to create a join table?
**Answer:**
A join table facilitates many-to-many relationships by storing foreign keys. Example: CREATE TABLE cats_owners (cat_id INTEGER, owner_id INTEGER);


### 🔴 Senior Level

#### 1. What is table inheritance?
**Answer:**
A feature in some ORDBMS (like PostgreSQL) allowing one table to inherit columns and characteristics from a parent table. Child tables also contain the data defined in the parent, supporting object-oriented database design patterns.


## 📂 Category: Database Programmability (1 cards)

### 🟡 Mid Level

#### 1. What is a VIEW?
**Answer:**
A VIEW is a saved SQL query that you can refer to like an ordinary table. It provides a way to abstract complex queries or represent specific subsets of data without having to rewrite the query each time.


## 📂 Category: Joins & Set Operators (8 cards)

### 🟢 Junior Level

#### 1. Find each employee's first_name, last_name, city, and state from the employee and location tables using the location_id field.
**Answer:**
SELECT employee.first_name, employee.last_name, location.city, location.state FROM employee INNER JOIN location ON employee.location_id = location.location_id;

#### 2. How do you perform joins in SQL?
**Answer:**
Joins are used to combine rows from two or more tables based on a related column. Common types include INNER JOIN, LEFT JOIN, and CROSS JOIN. Note that some systems (like SQLite) do not support RIGHT or FULL OUTER JOINs natively.

#### 3. What is a JOIN and what are the main types?
**Answer:**
A JOIN combines columns from one or more tables by using common values. Main types include: INNER, LEFT OUTER, RIGHT OUTER, FULL OUTER, and CROSS. A table can also join to itself in a self-join.

#### 4. What is the difference between INNER JOIN and OUTER JOIN?
**Answer:**
An INNER JOIN returns only rows where there is a match in both tables based on the join condition. An OUTER JOIN (LEFT, RIGHT, or FULL) returns matched rows plus unmatched rows from one or both tables, filling missing side values with NULL.


### 🟡 Mid Level

#### 1. Explain CROSS, LEFT, RIGHT, and FULL OUTER JOINS.
**Answer:**
A CROSS JOIN returns the Cartesian product of two tables. A LEFT JOIN returns all rows from the left table and matches from the right, with NULLs for missing matches. A RIGHT JOIN does the inverse. A FULL OUTER JOIN returns all rows from both tables, filling with NULLs where matches do not exist.

#### 2. Find the names of the owners of the cat with id 3, using tables cat, owner, and join table cat_owner.
**Answer:**
SELECT owner.name FROM owner INNER JOIN cat_owner ON owner.id = cat_owner.owner_id WHERE cat_owner.cat_id = 3;

#### 3. What does the UNION clause do?
**Answer:**
The UNION clause combines the result sets of multiple SELECT statements into a single result set while automatically removing duplicate rows.

#### 4. What is the syntax for the UNION clause?
**Answer:**
The UNION operator is used to combine the result sets of two or more SELECT statements. Example: SELECT name FROM first_names UNION SELECT name FROM last_names;


## 📂 Category: Subqueries & Aggregations (24 cards)

### 🟢 Junior Level

#### 1. Find how many films begin with the letter 'J'.
**Answer:**
SELECT COUNT(*) FROM films WHERE title LIKE 'J%';

#### 2. Find the app in the app table with the most downloads.
**Answer:**
SELECT MAX(downloads) FROM app;

#### 3. Find the sum of all amounts in the payment table.
**Answer:**
SELECT SUM(amount) FROM payment;


### 🟡 Mid Level

#### 1. Can column aliases or aggregate functions be used in WHERE or HAVING clauses?
**Answer:**
No. WHERE filters raw rows before aggregation, and HAVING filters grouped results. Because of the query execution order, aliases defined in the SELECT clause are not yet available in the WHERE/HAVING stages. Use the original column or expression.

#### 2. Does COUNT(myCol) count all rows in a column? What happens with NULLs?
**Answer:**
No. COUNT(column_name) ignores NULL values in that column. Use COUNT(*) to count all rows regardless of NULLs.

#### 3. Find in the payments table the customer_id of customers who have spent (amount) at least $110 with the staff_id of 2, grouped by customer.
**Answer:**
SELECT customer_id, SUM(amount) FROM payment WHERE staff_id = 2 GROUP BY customer_id HAVING SUM(amount) > 110; We group by customer_id to get totals and use HAVING to filter the aggregated results.

#### 4. Find the number of apps at each price in the apps table.
**Answer:**
SELECT price, COUNT(*) FROM apps GROUP BY price;

#### 5. Find the number of downloads per category.
**Answer:**
SELECT category, SUM(downloads) FROM app GROUP BY category;

#### 6. Find the number of records in the app table that have a price of 0.
**Answer:**
SELECT COUNT(*) FROM app WHERE price = 0;

#### 7. How does COUNT(*) differ from COUNT(column_name)?
**Answer:**
COUNT(*) counts every row in the result set including rows with NULLs. COUNT(column_name) ignores NULL values in that specific column.

#### 8. What does the COUNT aggregate function do?
**Answer:**
COUNT() is an aggregate function that returns the number of rows where the specified column contains a non-NULL value.

#### 9. What does the ROUND function do?
**Answer:**
The ROUND() function rounds a numeric value to a specified number of decimal places. It is often used in conjunction with aggregate functions.

#### 10. What does the WITH clause (Common Table Expression) do?
**Answer:**
The WITH clause allows you to define a temporary result set (or 'subquery') that can be referenced within the main query. Multiple temporary tables can be defined in a single WITH statement to improve query readability and structure.

#### 11. What is a CTE (Common Table Expression)?
**Answer:**
A CTE is defined using the WITH clause. It creates a temporary result set that can be referenced within a single SELECT, INSERT, UPDATE, or DELETE statement, improving readability and organization of complex queries.

#### 12. What is a window function?
**Answer:**
A window function performs a calculation across a set of table rows related to the current row. Unlike regular aggregate functions, window functions do not collapse rows into a single output row; each row retains its separate identity while still accessing result data from the defined 'window'.

#### 13. What is an aggregate function?
**Answer:**
Aggregate functions process a set of values and return a single scalar value. Examples include COUNT, SUM, AVG, MAX, and MIN, which are often used with the GROUP BY clause to summarize data.

#### 14. What is the difference between WHERE and HAVING clauses?
**Answer:**
The WHERE clause filters rows before grouping occurs. The HAVING clause is used to filter the result set after rows have been grouped by the GROUP BY clause, typically used to filter based on aggregate function results.

#### 15. What is the syntax for the HAVING clause?
**Answer:**
The HAVING clause is used to filter group rows after aggregations are computed. Example: SELECT year, COUNT(*) FROM movies GROUP BY year HAVING COUNT(*) > 5;

#### 16. Why is there a distinction between WHERE and HAVING?
**Answer:**
The WHERE clause filters rows before aggregation (input rows), whereas HAVING filters result groups after aggregation (group rows). Aggregate functions are generally not allowed in WHERE unless inside a subquery.


### 🔴 Senior Level

#### 1. Find employees by department, displaying department, employee_id, salary, and the calculated average_salary_by_department using a window function.
**Answer:**
SELECT depname, empno, salary, AVG(salary) OVER (PARTITION BY depname) AS average_salary_by_department FROM empsalary;

#### 2. Find the salary of each employee and the running total of salaries in ascending order.
**Answer:**
SELECT salary, SUM(salary) OVER (ORDER BY salary) AS running_total FROM empsalary;

#### 3. Find the salary of each employee and the total sum of all salaries, displaying both in every row.
**Answer:**
SELECT salary, SUM(salary) OVER () FROM empsalary;

#### 4. Find the salary rank by department of each employee using a window function.
**Answer:**
SELECT depname, empno, salary, RANK() OVER (PARTITION BY depname ORDER BY salary DESC) FROM empsalary;

#### 5. What is the syntax and purpose of a window function?
**Answer:**
A window function performs calculations across a set of table rows that are related to the current row. Syntactically, it requires an OVER clause. Example: SELECT depname, salary, avg(salary) OVER (PARTITION BY depname) FROM empsalary; The OVER clause determines the window, while PARTITION BY divides rows into groups.


## 📂 Category: Transactions & Concurrency (3 cards)

### 🔴 Senior Level

#### 1. How do you manage transactions in PostgreSQL?
**Answer:**
Transactions are wrapped in 'BEGIN' and 'COMMIT'. If an error occurs or logic dictates, 'ROLLBACK' cancels the changes. 'SAVEPOINT' allows for partial rollbacks within a transaction.

#### 2. What does it mean for a transaction to be atomic?
**Answer:**
Atomicity means that a transaction is treated as a single unit of work. Either all operations within the transaction are committed, or none of them are. To external observers, the transaction is all-or-nothing (opaque).

#### 3. What is a transaction?
**Answer:**
A transaction bundles multiple operations into a single, atomic unit. It ensures the ACID property: either all operations within the transaction succeed, or none of them do. Concurrent transactions are isolated, meaning they cannot see the incomplete, intermediate states of other ongoing transactions.

