# SQL & Database Study Guide - Junior Level

- **Total Cards**: 353

---

## 📂 Category: Advanced & Distributed Databases (1 cards)

### 🟢 Junior Level

#### 1. What is a Cloud Database?
**Answer:**
A database service created and maintained on a cloud infrastructure platform (such as Azure, AWS, or GCP) rather than on-premises hardware.


## 📂 Category: Basic SQL & Syntax (256 cards)

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


## 📂 Category: Database Design & Normalization (55 cards)

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


## 📂 Category: Database Programmability (7 cards)

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


## 📂 Category: Joins & Set Operators (24 cards)

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


## 📂 Category: Performance & Indexing (3 cards)

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


## 📂 Category: Subqueries & Aggregations (6 cards)

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


## 📂 Category: Transactions & Concurrency (1 cards)

### 🟢 Junior Level

#### 1. TCL
**Answer:**
Transaction Control Language: A subset of SQL commands used to manage transactions in the database (e.g., COMMIT, ROLLBACK, SAVEPOINT).

