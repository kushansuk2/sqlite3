# SQLite-Exercise
## Task
Hello potterheads, professor Dumbledore has given Ron Weasley a task to make an database, which contains list of all the spells used in wizarding world with thier short description, which will help Harry to defeat voldemort. Since Ron is busy with Hermione, he is asking help from his muggle friends to add some spells in the database. ( In case you haven't watched harry Potter movies you can add any magical word in the spell column like 
'Aabra Ka Daabra' ).
### Steps:
* Fork this repository.
* Clone the forked repository to your local device.
* Open windows terminal in the folder, where you cloned the forked repository.
* now type the given SQL code:
```
sqlite3 spell_list.db  /* to open the database */

.databases        /* it will display the current database which is spell_list.db */

.mode column      /* to view data column wise */
.header on 

/*  now to view the data in the table */
select * from spells;

/* to insert data in the table */
insert into spells values ('your name','spell name','description');
/* remember to insert values in same order */

/* to view entered data */
select * from spells;

.quit
```
* Commit the changes and push them to your forked repository.
* Create a pull request.

Congrats the excercise is finished!!
