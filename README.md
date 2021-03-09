# SQLite and it's python application - an Overview
We discussed about the SQLite database, which is a serverless software library that provides a relational database management system. The recording of the session demonstrations is available [here](link)

## SQLite
SQLite is a software library that provides a relational database management system. The lite in SQLite means lightweight in terms of setup, database administration, and required resources.

It is abundantly used in small sized android applications to store data locally.

### Basic commands used in SQLite:
1. `.databases`
   - List names and files of attached databases

2. `.mode MODE`</br>

     Set output mode where MODE is one of -
   - csv − Comma-separated values
   - column − Left-aligned columns 

3. `.schema`
   - Show the CREATE statements.

4. `.tables`
   - List tables name

### SQLite Storage Classes:
1. **NULL**:    The value is a NULL value.                                     
2. **INTEGER**: The value is a signed integer.                                 
3. **TEXT**:    The value is a text string.                               
4. **REAL**:    The value is a floating point value.                           
5. **BLOB**:    The value is a blob of data, stored exactly as it was input. 

### Basic Statements:
1. **CREATE** **TABLE**:</br>
 It is used to create new table.

   - **Syntax**:</br>
```
CREATE TABLE table_name(
   column1 datatype,
   column2 datatype,
   column3 datatype,
   .....
   columnN datatype,
   PRIMARY KEY( one or more columns )
);
```
2. **SELECT**:</br>
The `SELECT` statement is one of the most commonly used statements in SQL. The SQLite `SELECT` statement provides all features of the `SELECT` statement in SQL standard.
It is used to query data from single table.</br>
You can refer all the uses of `SELECT` statement from [here](https://www.sqlitetutorial.net/sqlite-select/).

These was the basic knowledge of SQLite. To know more about the topics like sorting, filtering, grouping the data and many more you can refer this website https://www.sqlitetutorial.net/
## Exercise for SQLite:
This is the link to exercise 
https://github.com/kushansuk2/sqlite3/blob/main/SQLite-Excercise.md
