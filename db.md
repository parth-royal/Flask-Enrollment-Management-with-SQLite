sqlite3 instance/database.db
SELECT * FROM enrollment;


context of databases, ORM allows you to interact with a relational database using an object-oriented paradigm.


#  CRUD operations using ORM methods. 


Create Models:
Define ORM models to represent database tables. In this case, you might have models for Student, Course, and Enrollment.



An ORM (Object-Relational Mapping) model is a programming construct used in software development to represent and interact with data stored in a relational database using an object-oriented paradigm.

In traditional relational databases, data is organized into tables, rows, and columns. Each row represents a record, and each column represents a specific attribute of that record. 

However, in object-oriented programming (OOP), data is represented as objects with properties (attributes) and methods (functions).


ORM models bridge the gap between these two paradigms by mapping database tables to classes and rows to objects. Each table in the database corresponds to a class in the application code, and each row in the table corresponds to an instance of that class.

class represents a database table, with attributes mapping to table columns.


Methods in ORM classes 


```txt
Relationships: ORM models can represent relationships between different database tables, such as one-to-one, one-to-many, or many-to-many relationships. These relationships are defined using attributes and methods in the ORM classes.
```





postres Sql = opens  pure relational db 

store data in
table columns and rows 

#use to read/write data
sql language 

#Object realtion database 
can crate custom dtype 
```sql
CREATE TABLE  superhero (
powers TEXT[]
mutant BOOLEAN
)

INHERITS (human);

```
support inhetance and polymorphism 
