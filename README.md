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

##Python usecases:</br>
SQLite3 can be integrated with Python using sqlite3 module, which was written by Gerhard Haring. It provides an SQL interface compliant with the DB-API 2.0 specification described by PEP 249. You do not need to install this module separately because it is shipped by default along with Python version 2.5.x onwards.

To use sqlite3 module, you must first create a connection object that represents the database and then optionally you can create a cursor object, which will help you in executing all the SQL statements.</br>
##Python sqlite3 module APIs
These are few sqlite modules from whic sqlite is controlled through python:
|Sr.No.|API & Description|
| :----: | :----: |
|1|sqlite3.connect(database [,timeout ,other optional arguments])|
|2|connection.cursor([cursorClass])|
|3|cursor.execute(sql [, optional parameters])|
|4|connection.execute(sql [, optional parameters])|
|5|cursor.executemany(sql, seq_of_parameters)|
|6|connection.executemany(sql[, parameters])|
|7|cursor.executescript(sql_script)|
|8|connection.executescript(sql_script)|
|9|connection.total_changes()|
|10|connection.commit()|
|11|connection.rollback()|
|12|connection.close()|
|13|cursor.fetchone()|
|14|cursor.fetchmany([size = cursor.arraysize])|
|15|cursor.fetchall()|
</br>
For a more in depth study you can go [here](www.tutorialspoint.com/sqlite/sqlite_python.htm)
Wait a minute this isn't over yet.

###pandas and sqlite
You know there is a easy way by which you can convert a sqlite database into panda dataframe for easy data manupulation
```
import sqlite3
import pandas as pd

cnx = sqlite3.connect('file.db')

df = pd.read_sql_query("SELECT * FROM table_name", cnx)
```

##Few Tips
While using sqlite in python or in any other language
###use this
![use this](images/3g.jpg?raw=true "Use this")
###and not this
![do not use this](images/4.jpg?raw=true "Do not use this")

##Few problems
Sqlite is susceptible to request overloading. By this I mean to say that if two users try to do same thing thing then only one request will be accepted and other will be ignored. But in few other database language requests are queued so that it can be handled properly.
![request overloaded](images/problem.jpg?raw=true "Title")

## Exercise for SQLite:
This is the link to exercise 
https://github.com/kushansuk2/sqlite3/blob/main/SQLite-Excercise.md
