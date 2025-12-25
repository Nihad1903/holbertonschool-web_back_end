## Resources

**Read or watch**:

*   [MySQL cheatsheet](/rltoken/XCHG-pgtifYRSw8ILB6DEw "MySQL cheatsheet")
*   [MySQL Performance: How To Leverage MySQL Database Indexing](/rltoken/VXAPISdkpKg3YD3HmVQXlw "MySQL Performance: How To Leverage MySQL Database Indexing")
*   [Stored Procedure](/rltoken/C37E-NvP8KxpI5Ds5w1oAQ "Stored Procedure")
*   [Triggers](/rltoken/0xFZu5AK0imLk70dxxcODA "Triggers")
*   [Views](/rltoken/Q8butAms3BthfCFhXuQSPA "Views")
*   [Functions and Operators](/rltoken/0ezATipRSpz1K8MixrD2Rg "Functions and Operators")
*   [Trigger Syntax and Examples](/rltoken/rc8oho9n7LAjtffC584tgA "Trigger Syntax and Examples")
*   [CREATE TABLE Statement](/rltoken/F1SUJgWz-4YNNYLPkL9tPw "CREATE TABLE Statement")
*   [CREATE PROCEDURE and CREATE FUNCTION Statements](/rltoken/XhYdXik2tTMK2k81WxulpA "CREATE PROCEDURE and CREATE FUNCTION Statements")
*   [CREATE INDEX Statement](/rltoken/K90KZ3z4gL5mPpHROlEOcg "CREATE INDEX Statement")
*   [CREATE VIEW Statement](/rltoken/VJESVxV2V7jGqrR-50903A "CREATE VIEW Statement")

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/j63kEGfU7eLokEipk6jQCA "explain to anyone"), **without the help of Google**:

### General

*   How to create tables with constraints
*   How to optimize queries by adding indexes
*   What is and how to implement stored procedures and functions in MySQL
*   What is and how to implement views in MySQL
*   What is and how to implement triggers in MySQL

## Requirements

### General

*   All your files will be executed on Ubuntu 20.04 LTS using `MySQL 8.0`
*   All your files should end with a new line
*   All your SQL queries should have a comment just before (i.e. syntax above)
*   All your files should start by a comment describing the task
*   All SQL keywords should be in uppercase (`SELECT`, `WHERE`…)
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   The length of your files will be tested using `wc`

## Tasks

### 1.

Write a SQL script that creates a table `users` following these requirements:

*   With these attributes:
    *   `id`, integer, never null, auto increment and primary key
    *   `email`, string (255 characters), never null and unique
    *   `name`, string (255 characters)
*   If the table already exists, your script should not fail
*   Your script can be executed on any database

**Context:** _Make an attribute unique directly in the table schema will enforced your business rules and avoid bugs in your application_
```
bob@dylan:~$ echo "SELECT \* FROM users;" | mysql -uroot -p holberton
Enter password:
ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
bob@dylan:~$
bob@dylan:~$ cat 0-uniq\_users.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");' | mysql -uroot -p holberton
Enter password:
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("sylvie@dylan.com", "Sylvie");' | mysql -uroot -p holberton
Enter password:
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Jean");' | mysql -uroot -p holberton
Enter password:
ERROR 1062 (23000) at line 1: Duplicate entry 'bob@dylan.com' for key 'email'
bob@dylan:~$
bob@dylan:~$ echo "SELECT \* FROM users;" | mysql -uroot -p holberton
Enter password:
id  email   name
1   bob@dylan.com   Bob
2   sylvie@dylan.com    Sylvie
bob@dylan:~$
```


### 2.

Write a SQL script that creates a table `users` following these requirements:

*   With these attributes:
    *   `id`, integer, never null, auto increment and primary key
    *   `email`, string (255 characters), never null and unique
    *   `name`, string (255 characters)
    *   `country`, enumeration of countries: `US`, `CO` and `TN`, never null (= default will be the first element of the enumeration, here `US`)
*   If the table already exists, your script should not fail
*   Your script can be executed on any database
```
bob@dylan:~$ echo "SELECT \* FROM users;" | mysql -uroot -p holberton
Enter password:
ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
bob@dylan:~$
bob@dylan:~$ cat 1-country\_users.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("bob@dylan.com", "Bob", "US");' | mysql -uroot -p holberton
Enter password:
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("sylvie@dylan.com", "Sylvie", "CO");' | mysql -uroot -p holberton
Enter password:
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("jean@dylan.com", "Jean", "FR");' | mysql -uroot -p holberton
Enter password:
ERROR 1265 (01000) at line 1: Data truncated for column 'country' at row 1
bob@dylan:~$
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("john@dylan.com", "John");' | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ echo "SELECT \* FROM users;" | mysql -uroot -p holberton
Enter password:
id  email   name    country
1   bob@dylan.com   Bob US
2   sylvie@dylan.com    Sylvie  CO
3   john@dylan.com  John    US
bob@dylan:~$
```


### 3.

Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans

**Requirements:**

*   Import this table dump: [metal\_bands.sql.zip](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2020/6/ab2979f058de215f0f2ae5b052739e76d3c02ac5.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20250317%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20250317T092325Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&X-Amz-Signature=da8f062e3725afd4932b14e500ce9844c7e6facec446c8379d76352383138742 "metal_bands.sql.zip")
*   Column names must be: `origin` and `nb_fans`
*   Your script can be executed on any database

**Context:** _Calculate/compute something is always power intensive… better to distribute the load!_
```
bob@dylan:~$ cat metal\_bands.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 2-fans.sql | mysql -uroot -p holberton > tmp\_res ; head tmp\_res
Enter password:
origin  nb\_fans
USA 99349
Sweden  47169
Finland 32878
United Kingdom  32518
Germany 29486
Norway  22405
Canada  8874
The Netherlands 8819
Italy   7178
bob@dylan:~$
```


### 4.

Write a SQL script that lists all bands with `Glam rock` as their main style, ranked by their longevity

**Requirements:**

*   Import this table dump: [metal\_bands.sql.zip](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2020/6/ab2979f058de215f0f2ae5b052739e76d3c02ac5.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20250317%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20250317T092325Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&X-Amz-Signature=da8f062e3725afd4932b14e500ce9844c7e6facec446c8379d76352383138742 "metal_bands.sql.zip")
*   Column names must be: `band_name` and `lifespan` (in years)
*   You should use attributes `formed` and `split` for computing the `lifespan`
*   Your script can be executed on any database
```
bob@dylan:~$ cat metal\_bands.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 3-glam\_rock.sql | mysql -uroot -p holberton
Enter password:
band\_name   lifespan
Alice Cooper    60
Mötley Crüe   34
Marilyn Manson  35
The 69 Eyes 34
Hardcore Superstar  27
Nasty Idols 0
Hanoi Rocks 0
bob@dylan:~$
```


### 5.

Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

Quantity in the table `items` can be negative.

**Context:** _Updating multiple tables for one action from your application can generate issue: network disconnection, crash, etc… to keep your data in a good shape, let MySQL do it for you!_
```
bob@dylan:~$ cat 4-init.sql
-- Initial
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS orders;

CREATE TABLE IF NOT EXISTS items (
    name VARCHAR(255) NOT NULL,
    quantity int NOT NULL DEFAULT 10
);

CREATE TABLE IF NOT EXISTS orders (
    item\_name VARCHAR(255) NOT NULL,
    number int NOT NULL
);

INSERT INTO items (name) VALUES ("apple"), ("pineapple"), ("pear");

bob@dylan:~$
bob@dylan:~$ cat 4-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 4-store.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 4-main.sql
Enter password:
-- Show and add orders
SELECT \* FROM items;
SELECT \* FROM orders;

INSERT INTO orders (item\_name, number) VALUES ('apple', 1);
INSERT INTO orders (item\_name, number) VALUES ('apple', 3);
INSERT INTO orders (item\_name, number) VALUES ('pear', 2);

SELECT "--";

SELECT \* FROM items;
SELECT \* FROM orders;

bob@dylan:~$
bob@dylan:~$ cat 4-main.sql | mysql -uroot -p holberton
Enter password:
name    quantity
apple   10
pineapple   10
pear    10
--
--
name    quantity
apple   6
pineapple   10
pear    8
item\_name   number
apple   1
apple   3
pear    2
bob@dylan:~$
```


### 6.

Write a SQL script that creates a trigger that resets the attribute `valid_email` only when the `email` has been changed.

**Context:** _Nothing related to MySQL, but perfect for user email validation - distribute the logic to the database itself!_
```
bob@dylan:~$ cat 5-init.sql
-- Initial
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO\_INCREMENT,
    email varchar(255) not null,
    name varchar(255),
    valid\_email boolean not null default 0,
    PRIMARY KEY (id)
);

INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");
INSERT INTO users (email, name, valid\_email) VALUES ("sylvie@dylan.com", "Sylvie", 1);
INSERT INTO users (email, name, valid\_email) VALUES ("jeanne@dylan.com", "Jeanne", 1);

bob@dylan:~$
bob@dylan:~$ cat 5-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 5-valid\_email.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 5-main.sql
Enter password:
-- Show users and update (or not) email
SELECT \* FROM users;

UPDATE users SET valid\_email = 1 WHERE email = "bob@dylan.com";
UPDATE users SET email = "sylvie+new@dylan.com" WHERE email = "sylvie@dylan.com";
UPDATE users SET name = "Jannis" WHERE email = "jeanne@dylan.com";

SELECT "--";
SELECT \* FROM users;

UPDATE users SET email = "bob@dylan.com" WHERE email = "bob@dylan.com";

SELECT "--";
SELECT \* FROM users;

bob@dylan:~$
bob@dylan:~$ cat 5-main.sql | mysql -uroot -p holberton
Enter password:
id  email   name    valid\_email
1   bob@dylan.com   Bob 0
2   sylvie@dylan.com    Sylvie  1
3   jeanne@dylan.com    Jeanne  1
--
--
id  email   name    valid\_email
1   bob@dylan.com   Bob 1
2   sylvie+new@dylan.com    Sylvie  0
3   jeanne@dylan.com    Jannis  1
--
--
id  email   name    valid\_email
1   bob@dylan.com   Bob 1
2   sylvie+new@dylan.com    Sylvie  0
3   jeanne@dylan.com    Jannis  1
bob@dylan:~$
```


### 7.

Write a SQL script that creates a stored procedure `AddBonus` that adds a new correction for a student.

**Requirements:**

*   Procedure `AddBonus` is taking 3 inputs (in this order):
    *   `user_id`, a `users.id` value (you can assume `user_id` is linked to an existing `users`)
    *   `project_name`, a new or already exists `projects` - if no `projects.name` found in the table, you should create it
    *   `score`, the score value for the correction

**Context:** _Write code in SQL is a nice level up!_
```
bob@dylan:~$ cat 6-init.sql
-- Initial
DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO\_INCREMENT,
    name varchar(255) not null,
    average\_score float default 0,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS projects (
    id int not null AUTO\_INCREMENT,
    name varchar(255) not null,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS corrections (
    user\_id int not null,
    project\_id int not null,
    score int default 0,
    KEY \`user\_id\` (\`user\_id\`),
    KEY \`project\_id\` (\`project\_id\`),
    CONSTRAINT fk\_user\_id FOREIGN KEY (\`user\_id\`) REFERENCES \`users\` (\`id\`) ON DELETE CASCADE,
    CONSTRAINT fk\_project\_id FOREIGN KEY (\`project\_id\`) REFERENCES \`projects\` (\`id\`) ON DELETE CASCADE
);

INSERT INTO users (name) VALUES ("Bob");
SET @user\_bob = LAST\_INSERT\_ID();

INSERT INTO users (name) VALUES ("Jeanne");
SET @user\_jeanne = LAST\_INSERT\_ID();

INSERT INTO projects (name) VALUES ("C is fun");
SET @project\_c = LAST\_INSERT\_ID();

INSERT INTO projects (name) VALUES ("Python is cool");
SET @project\_py = LAST\_INSERT\_ID();

INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_bob, @project\_c, 80);
INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_bob, @project\_py, 96);

INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_jeanne, @project\_c, 91);
INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_jeanne, @project\_py, 73);

bob@dylan:~$
bob@dylan:~$ cat 6-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 6-bonus.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 6-main.sql
Enter password:
-- Show and add bonus correction
SELECT \* FROM projects;
SELECT \* FROM corrections;

SELECT "--";

CALL AddBonus((SELECT id FROM users WHERE name = "Jeanne"), "Python is cool", 100);

CALL AddBonus((SELECT id FROM users WHERE name = "Jeanne"), "Bonus project", 100);
CALL AddBonus((SELECT id FROM users WHERE name = "Bob"), "Bonus project", 10);

CALL AddBonus((SELECT id FROM users WHERE name = "Jeanne"), "New bonus", 90);

SELECT "--";

SELECT \* FROM projects;
SELECT \* FROM corrections;

bob@dylan:~$
bob@dylan:~$ cat 6-main.sql | mysql -uroot -p holberton
Enter password:
id  name
1   C is fun
2   Python is cool
user\_id project\_id  score
1   1   80
1   2   96
2   1   91
2   2   73
--
--
--
--
id  name
1   C is fun
2   Python is cool
3   Bonus project
4   New bonus
user\_id project\_id  score
1   1   80
1   2   96
2   1   91
2   2   73
2   2   100
2   3   100
1   3   10
2   4   90
bob@dylan:~$
```


### 8.

Write a SQL script that creates a stored procedure `ComputeAverageScoreForUser` that computes and store the average score for a student. Note: An average score can be a decimal

**Requirements:**

*   Procedure `ComputeAverageScoreForUser` is taking 1 input:
    *   `user_id`, a `users.id` value (you can assume `user_id` is linked to an existing `users`)
```
bob@dylan:~$ cat 7-init.sql
-- Initial
DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO\_INCREMENT,
    name varchar(255) not null,
    average\_score float default 0,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS projects (
    id int not null AUTO\_INCREMENT,
    name varchar(255) not null,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS corrections (
    user\_id int not null,
    project\_id int not null,
    score int default 0,
    KEY \`user\_id\` (\`user\_id\`),
    KEY \`project\_id\` (\`project\_id\`),
    CONSTRAINT fk\_user\_id FOREIGN KEY (\`user\_id\`) REFERENCES \`users\` (\`id\`) ON DELETE CASCADE,
    CONSTRAINT fk\_project\_id FOREIGN KEY (\`project\_id\`) REFERENCES \`projects\` (\`id\`) ON DELETE CASCADE
);

INSERT INTO users (name) VALUES ("Bob");
SET @user\_bob = LAST\_INSERT\_ID();

INSERT INTO users (name) VALUES ("Jeanne");
SET @user\_jeanne = LAST\_INSERT\_ID();

INSERT INTO projects (name) VALUES ("C is fun");
SET @project\_c = LAST\_INSERT\_ID();

INSERT INTO projects (name) VALUES ("Python is cool");
SET @project\_py = LAST\_INSERT\_ID();

INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_bob, @project\_c, 80);
INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_bob, @project\_py, 96);

INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_jeanne, @project\_c, 91);
INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_jeanne, @project\_py, 73);

bob@dylan:~$
bob@dylan:~$ cat 7-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 7-average\_score.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 7-main.sql
-- Show and compute average score
SELECT \* FROM users;
SELECT \* FROM corrections;

SELECT "--";
CALL ComputeAverageScoreForUser((SELECT id FROM users WHERE name = "Jeanne"));

SELECT "--";
SELECT \* FROM users;

bob@dylan:~$
bob@dylan:~$ cat 7-main.sql | mysql -uroot -p holberton
Enter password:
id  name    average\_score
1   Bob 0
2   Jeanne  0
user\_id project\_id  score
1   1   80
1   2   96
2   1   91
2   2   73
--
--
--
--
id  name    average\_score
1   Bob 0
2   Jeanne  82
bob@dylan:~$
```


### 9.

Write a SQL script that creates an index `idx_name_first` on the table `names` and the first letter of `name`.

**Requirements:**

*   Import this table dump: [names.sql.zip](https://intranet-projects-files.s3.amazonaws.com/holbertonschool-webstack/632/names.sql.zip "names.sql.zip")
*   Only the first letter of `name` must be indexed

**Context:** _Index is not the solution for any performance issue, but well used, it’s really powerful!_
```
bob@dylan:~$ cat names.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ mysql -uroot -p holberton
Enter password:
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%';
+-------------+
| COUNT(name) |
+-------------+
|      302936 |
+-------------+
1 row in set (2.19 sec)
mysql>
mysql> exit
bye
bob@dylan:~$
bob@dylan:~$ cat 8-index\_my\_names.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ mysql -uroot -p holberton
Enter password:
mysql> SHOW index FROM names;
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non\_unique | Key\_name       | Seq\_in\_index | Column\_name | Collation | Cardinality | Sub\_part | Packed | Null | Index\_type | Comment | Index\_comment |
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| names |          1 | idx\_name\_first |            1 | name        | A         |          25 |        1 | NULL   | YES  | BTREE      |         |               |
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
1 row in set (0.00 sec)
mysql>
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%';
+-------------+
| COUNT(name) |
+-------------+
|      302936 |
+-------------+
1 row in set (0.82 sec)
mysql>
mysql> exit
bye
bob@dylan:~$
```


### 10.

Write a SQL script that creates an index `idx_name_first_score` on the table `names` and the first letter of `name` and the `score`.

**Requirements:**

*   Import this table dump: [names.sql.zip](https://intranet-projects-files.s3.amazonaws.com/holbertonschool-webstack/632/names.sql.zip "names.sql.zip")
*   Only the first letter of `name` AND `score` must be indexed
```
bob@dylan:~$ cat names.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ mysql -uroot -p holberton
Enter password:
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%' AND score < 80;
+-------------+
| count(name) |
+-------------+
|       60717 |
+-------------+
1 row in set (2.40 sec)
mysql>
mysql> exit
bye
bob@dylan:~$
bob@dylan:~$ cat 9-index\_name\_score.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ mysql -uroot -p holberton
Enter password:
mysql> SHOW index FROM names;
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non\_unique | Key\_name             | Seq\_in\_index | Column\_name | Collation | Cardinality | Sub\_part | Packed | Null | Index\_type | Comment | Index\_comment |
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| names |          1 | idx\_name\_first\_score |            1 | name        | A         |          25 |        1 | NULL   | YES  | BTREE      |         |               |
| names |          1 | idx\_name\_first\_score |            2 | score       | A         |        3901 |     NULL | NULL   | YES  | BTREE      |         |               |
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
2 rows in set (0.00 sec)
mysql>
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%' AND score < 80;
+-------------+
| COUNT(name) |
+-------------+
|       60717 |
+-------------+
1 row in set (0.48 sec)
mysql>
mysql> exit
bye
bob@dylan:~$
```


### 11.

Write a SQL script that creates a function `SafeDiv` that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

**Requirements:**

*   You must create a function
*   The function `SafeDiv` takes 2 arguments:
    *   `a`, INT
    *   `b`, INT
*   And returns `a / b` or 0 if `b == 0`
```
bob@dylan:~$ cat 10-init.sql
-- Initial
DROP TABLE IF EXISTS numbers;

CREATE TABLE IF NOT EXISTS numbers (
    a int default 0,
    b int default 0
);

INSERT INTO numbers (a, b) VALUES (10, 2);
INSERT INTO numbers (a, b) VALUES (4, 5);
INSERT INTO numbers (a, b) VALUES (2, 3);
INSERT INTO numbers (a, b) VALUES (6, 3);
INSERT INTO numbers (a, b) VALUES (7, 0);
INSERT INTO numbers (a, b) VALUES (6, 8);

bob@dylan:~$ cat 10-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 10-div.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ echo "SELECT (a / b) FROM numbers;" | mysql -uroot -p holberton
Enter password:
(a / b)
5.0000
0.8000
0.6667
2.0000
NULL
0.7500
bob@dylan:~$
bob@dylan:~$ echo "SELECT SafeDiv(a, b) FROM numbers;" | mysql -uroot -p holberton
Enter password:
SafeDiv(a, b)
5
0.800000011920929
0.6666666865348816
2
0
0.75
bob@dylan:~$
```


### 12.

Write a SQL script that creates a view `need_meeting` that lists all students that have a score under 80 (strict) and no `last_meeting` or more than 1 month.

**Requirements:**

*   The view `need_meeting` should return all students name when:
    *   They score are under (strict) to 80
    *   **AND** no `last_meeting` date **OR** more than a month
```
bob@dylan:~$ cat 11-init.sql
-- Initial
DROP TABLE IF EXISTS students;

CREATE TABLE IF NOT EXISTS students (
    name VARCHAR(255) NOT NULL,
    score INT default 0,
    last\_meeting DATE NULL
);

INSERT INTO students (name, score) VALUES ("Bob", 80);
INSERT INTO students (name, score) VALUES ("Sylvia", 120);
INSERT INTO students (name, score) VALUES ("Jean", 60);
INSERT INTO students (name, score) VALUES ("Steeve", 50);
INSERT INTO students (name, score) VALUES ("Camilia", 80);
INSERT INTO students (name, score) VALUES ("Alexa", 130);

bob@dylan:~$ cat 11-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 11-need\_meeting.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 11-main.sql
-- Test view
SELECT \* FROM need\_meeting;

SELECT "--";

UPDATE students SET score = 40 WHERE name = 'Bob';
SELECT \* FROM need\_meeting;

SELECT "--";

UPDATE students SET score = 80 WHERE name = 'Steeve';
SELECT \* FROM need\_meeting;

SELECT "--";

UPDATE students SET last\_meeting = CURDATE() WHERE name = 'Jean';
SELECT \* FROM need\_meeting;

SELECT "--";

UPDATE students SET last\_meeting = ADDDATE(CURDATE(), INTERVAL -2 MONTH) WHERE name = 'Jean';
SELECT \* FROM need\_meeting;

SELECT "--";

SHOW CREATE TABLE need\_meeting;

SELECT "--";

SHOW CREATE TABLE students;

bob@dylan:~$
bob@dylan:~$ cat 11-main.sql | mysql -uroot -p holberton
Enter password:
name
Jean
Steeve
--
--
name
Bob
Jean
Steeve
--
--
name
Bob
Jean
--
--
name
Bob
--
--
name
Bob
Jean
--
--
View    Create View character\_set\_client    collation\_connection
XXXXXX<yes, here it will display the View SQL statement :-) >XXXXXX
--
--
Table   Create Table
students    CREATE TABLE \`students\` (\\n  \`name\` varchar(255) NOT NULL,\\n  \`score\` int(11) DEFAULT '0',\\n  \`last\_meeting\` date DEFAULT NULL\\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
bob@dylan:~$
```## Resources

**Read or watch**:

*   [MySQL cheatsheet](/rltoken/XCHG-pgtifYRSw8ILB6DEw "MySQL cheatsheet")
*   [MySQL Performance: How To Leverage MySQL Database Indexing](/rltoken/VXAPISdkpKg3YD3HmVQXlw "MySQL Performance: How To Leverage MySQL Database Indexing")
*   [Stored Procedure](/rltoken/C37E-NvP8KxpI5Ds5w1oAQ "Stored Procedure")
*   [Triggers](/rltoken/0xFZu5AK0imLk70dxxcODA "Triggers")
*   [Views](/rltoken/Q8butAms3BthfCFhXuQSPA "Views")
*   [Functions and Operators](/rltoken/0ezATipRSpz1K8MixrD2Rg "Functions and Operators")
*   [Trigger Syntax and Examples](/rltoken/rc8oho9n7LAjtffC584tgA "Trigger Syntax and Examples")
*   [CREATE TABLE Statement](/rltoken/F1SUJgWz-4YNNYLPkL9tPw "CREATE TABLE Statement")
*   [CREATE PROCEDURE and CREATE FUNCTION Statements](/rltoken/XhYdXik2tTMK2k81WxulpA "CREATE PROCEDURE and CREATE FUNCTION Statements")
*   [CREATE INDEX Statement](/rltoken/K90KZ3z4gL5mPpHROlEOcg "CREATE INDEX Statement")
*   [CREATE VIEW Statement](/rltoken/VJESVxV2V7jGqrR-50903A "CREATE VIEW Statement")

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/j63kEGfU7eLokEipk6jQCA "explain to anyone"), **without the help of Google**:

### General

*   How to create tables with constraints
*   How to optimize queries by adding indexes
*   What is and how to implement stored procedures and functions in MySQL
*   What is and how to implement views in MySQL
*   What is and how to implement triggers in MySQL

## Requirements

### General

*   All your files will be executed on Ubuntu 20.04 LTS using `MySQL 8.0`
*   All your files should end with a new line
*   All your SQL queries should have a comment just before (i.e. syntax above)
*   All your files should start by a comment describing the task
*   All SQL keywords should be in uppercase (`SELECT`, `WHERE`…)
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   The length of your files will be tested using `wc`

## Tasks

### 1.

Write a SQL script that creates a table `users` following these requirements:

*   With these attributes:
    *   `id`, integer, never null, auto increment and primary key
    *   `email`, string (255 characters), never null and unique
    *   `name`, string (255 characters)
*   If the table already exists, your script should not fail
*   Your script can be executed on any database

**Context:** _Make an attribute unique directly in the table schema will enforced your business rules and avoid bugs in your application_
```
bob@dylan:~$ echo "SELECT \* FROM users;" | mysql -uroot -p holberton
Enter password:
ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
bob@dylan:~$
bob@dylan:~$ cat 0-uniq\_users.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");' | mysql -uroot -p holberton
Enter password:
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("sylvie@dylan.com", "Sylvie");' | mysql -uroot -p holberton
Enter password:
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Jean");' | mysql -uroot -p holberton
Enter password:
ERROR 1062 (23000) at line 1: Duplicate entry 'bob@dylan.com' for key 'email'
bob@dylan:~$
bob@dylan:~$ echo "SELECT \* FROM users;" | mysql -uroot -p holberton
Enter password:
id  email   name
1   bob@dylan.com   Bob
2   sylvie@dylan.com    Sylvie
bob@dylan:~$
```


### 2.

Write a SQL script that creates a table `users` following these requirements:

*   With these attributes:
    *   `id`, integer, never null, auto increment and primary key
    *   `email`, string (255 characters), never null and unique
    *   `name`, string (255 characters)
    *   `country`, enumeration of countries: `US`, `CO` and `TN`, never null (= default will be the first element of the enumeration, here `US`)
*   If the table already exists, your script should not fail
*   Your script can be executed on any database
```
bob@dylan:~$ echo "SELECT \* FROM users;" | mysql -uroot -p holberton
Enter password:
ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
bob@dylan:~$
bob@dylan:~$ cat 1-country\_users.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("bob@dylan.com", "Bob", "US");' | mysql -uroot -p holberton
Enter password:
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("sylvie@dylan.com", "Sylvie", "CO");' | mysql -uroot -p holberton
Enter password:
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("jean@dylan.com", "Jean", "FR");' | mysql -uroot -p holberton
Enter password:
ERROR 1265 (01000) at line 1: Data truncated for column 'country' at row 1
bob@dylan:~$
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("john@dylan.com", "John");' | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ echo "SELECT \* FROM users;" | mysql -uroot -p holberton
Enter password:
id  email   name    country
1   bob@dylan.com   Bob US
2   sylvie@dylan.com    Sylvie  CO
3   john@dylan.com  John    US
bob@dylan:~$
```


### 3.

Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans

**Requirements:**

*   Import this table dump: [metal\_bands.sql.zip](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2020/6/ab2979f058de215f0f2ae5b052739e76d3c02ac5.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20250317%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20250317T092325Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&X-Amz-Signature=da8f062e3725afd4932b14e500ce9844c7e6facec446c8379d76352383138742 "metal_bands.sql.zip")
*   Column names must be: `origin` and `nb_fans`
*   Your script can be executed on any database

**Context:** _Calculate/compute something is always power intensive… better to distribute the load!_
```
bob@dylan:~$ cat metal\_bands.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 2-fans.sql | mysql -uroot -p holberton > tmp\_res ; head tmp\_res
Enter password:
origin  nb\_fans
USA 99349
Sweden  47169
Finland 32878
United Kingdom  32518
Germany 29486
Norway  22405
Canada  8874
The Netherlands 8819
Italy   7178
bob@dylan:~$
```


### 4.

Write a SQL script that lists all bands with `Glam rock` as their main style, ranked by their longevity

**Requirements:**

*   Import this table dump: [metal\_bands.sql.zip](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2020/6/ab2979f058de215f0f2ae5b052739e76d3c02ac5.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20250317%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20250317T092325Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&X-Amz-Signature=da8f062e3725afd4932b14e500ce9844c7e6facec446c8379d76352383138742 "metal_bands.sql.zip")
*   Column names must be: `band_name` and `lifespan` (in years)
*   You should use attributes `formed` and `split` for computing the `lifespan`
*   Your script can be executed on any database
```
bob@dylan:~$ cat metal\_bands.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 3-glam\_rock.sql | mysql -uroot -p holberton
Enter password:
band\_name   lifespan
Alice Cooper    60
Mötley Crüe   34
Marilyn Manson  35
The 69 Eyes 34
Hardcore Superstar  27
Nasty Idols 0
Hanoi Rocks 0
bob@dylan:~$
```


### 5.

Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

Quantity in the table `items` can be negative.

**Context:** _Updating multiple tables for one action from your application can generate issue: network disconnection, crash, etc… to keep your data in a good shape, let MySQL do it for you!_
```
bob@dylan:~$ cat 4-init.sql
-- Initial
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS orders;

CREATE TABLE IF NOT EXISTS items (
    name VARCHAR(255) NOT NULL,
    quantity int NOT NULL DEFAULT 10
);

CREATE TABLE IF NOT EXISTS orders (
    item\_name VARCHAR(255) NOT NULL,
    number int NOT NULL
);

INSERT INTO items (name) VALUES ("apple"), ("pineapple"), ("pear");

bob@dylan:~$
bob@dylan:~$ cat 4-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 4-store.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 4-main.sql
Enter password:
-- Show and add orders
SELECT \* FROM items;
SELECT \* FROM orders;

INSERT INTO orders (item\_name, number) VALUES ('apple', 1);
INSERT INTO orders (item\_name, number) VALUES ('apple', 3);
INSERT INTO orders (item\_name, number) VALUES ('pear', 2);

SELECT "--";

SELECT \* FROM items;
SELECT \* FROM orders;

bob@dylan:~$
bob@dylan:~$ cat 4-main.sql | mysql -uroot -p holberton
Enter password:
name    quantity
apple   10
pineapple   10
pear    10
--
--
name    quantity
apple   6
pineapple   10
pear    8
item\_name   number
apple   1
apple   3
pear    2
bob@dylan:~$
```


### 6.

Write a SQL script that creates a trigger that resets the attribute `valid_email` only when the `email` has been changed.

**Context:** _Nothing related to MySQL, but perfect for user email validation - distribute the logic to the database itself!_
```
bob@dylan:~$ cat 5-init.sql
-- Initial
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO\_INCREMENT,
    email varchar(255) not null,
    name varchar(255),
    valid\_email boolean not null default 0,
    PRIMARY KEY (id)
);

INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");
INSERT INTO users (email, name, valid\_email) VALUES ("sylvie@dylan.com", "Sylvie", 1);
INSERT INTO users (email, name, valid\_email) VALUES ("jeanne@dylan.com", "Jeanne", 1);

bob@dylan:~$
bob@dylan:~$ cat 5-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 5-valid\_email.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 5-main.sql
Enter password:
-- Show users and update (or not) email
SELECT \* FROM users;

UPDATE users SET valid\_email = 1 WHERE email = "bob@dylan.com";
UPDATE users SET email = "sylvie+new@dylan.com" WHERE email = "sylvie@dylan.com";
UPDATE users SET name = "Jannis" WHERE email = "jeanne@dylan.com";

SELECT "--";
SELECT \* FROM users;

UPDATE users SET email = "bob@dylan.com" WHERE email = "bob@dylan.com";

SELECT "--";
SELECT \* FROM users;

bob@dylan:~$
bob@dylan:~$ cat 5-main.sql | mysql -uroot -p holberton
Enter password:
id  email   name    valid\_email
1   bob@dylan.com   Bob 0
2   sylvie@dylan.com    Sylvie  1
3   jeanne@dylan.com    Jeanne  1
--
--
id  email   name    valid\_email
1   bob@dylan.com   Bob 1
2   sylvie+new@dylan.com    Sylvie  0
3   jeanne@dylan.com    Jannis  1
--
--
id  email   name    valid\_email
1   bob@dylan.com   Bob 1
2   sylvie+new@dylan.com    Sylvie  0
3   jeanne@dylan.com    Jannis  1
bob@dylan:~$
```


### 7.

Write a SQL script that creates a stored procedure `AddBonus` that adds a new correction for a student.

**Requirements:**

*   Procedure `AddBonus` is taking 3 inputs (in this order):
    *   `user_id`, a `users.id` value (you can assume `user_id` is linked to an existing `users`)
    *   `project_name`, a new or already exists `projects` - if no `projects.name` found in the table, you should create it
    *   `score`, the score value for the correction

**Context:** _Write code in SQL is a nice level up!_
```
bob@dylan:~$ cat 6-init.sql
-- Initial
DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO\_INCREMENT,
    name varchar(255) not null,
    average\_score float default 0,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS projects (
    id int not null AUTO\_INCREMENT,
    name varchar(255) not null,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS corrections (
    user\_id int not null,
    project\_id int not null,
    score int default 0,
    KEY \`user\_id\` (\`user\_id\`),
    KEY \`project\_id\` (\`project\_id\`),
    CONSTRAINT fk\_user\_id FOREIGN KEY (\`user\_id\`) REFERENCES \`users\` (\`id\`) ON DELETE CASCADE,
    CONSTRAINT fk\_project\_id FOREIGN KEY (\`project\_id\`) REFERENCES \`projects\` (\`id\`) ON DELETE CASCADE
);

INSERT INTO users (name) VALUES ("Bob");
SET @user\_bob = LAST\_INSERT\_ID();

INSERT INTO users (name) VALUES ("Jeanne");
SET @user\_jeanne = LAST\_INSERT\_ID();

INSERT INTO projects (name) VALUES ("C is fun");
SET @project\_c = LAST\_INSERT\_ID();

INSERT INTO projects (name) VALUES ("Python is cool");
SET @project\_py = LAST\_INSERT\_ID();

INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_bob, @project\_c, 80);
INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_bob, @project\_py, 96);

INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_jeanne, @project\_c, 91);
INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_jeanne, @project\_py, 73);

bob@dylan:~$
bob@dylan:~$ cat 6-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 6-bonus.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 6-main.sql
Enter password:
-- Show and add bonus correction
SELECT \* FROM projects;
SELECT \* FROM corrections;

SELECT "--";

CALL AddBonus((SELECT id FROM users WHERE name = "Jeanne"), "Python is cool", 100);

CALL AddBonus((SELECT id FROM users WHERE name = "Jeanne"), "Bonus project", 100);
CALL AddBonus((SELECT id FROM users WHERE name = "Bob"), "Bonus project", 10);

CALL AddBonus((SELECT id FROM users WHERE name = "Jeanne"), "New bonus", 90);

SELECT "--";

SELECT \* FROM projects;
SELECT \* FROM corrections;

bob@dylan:~$
bob@dylan:~$ cat 6-main.sql | mysql -uroot -p holberton
Enter password:
id  name
1   C is fun
2   Python is cool
user\_id project\_id  score
1   1   80
1   2   96
2   1   91
2   2   73
--
--
--
--
id  name
1   C is fun
2   Python is cool
3   Bonus project
4   New bonus
user\_id project\_id  score
1   1   80
1   2   96
2   1   91
2   2   73
2   2   100
2   3   100
1   3   10
2   4   90
bob@dylan:~$
```


### 8.

Write a SQL script that creates a stored procedure `ComputeAverageScoreForUser` that computes and store the average score for a student. Note: An average score can be a decimal

**Requirements:**

*   Procedure `ComputeAverageScoreForUser` is taking 1 input:
    *   `user_id`, a `users.id` value (you can assume `user_id` is linked to an existing `users`)
```
bob@dylan:~$ cat 7-init.sql
-- Initial
DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO\_INCREMENT,
    name varchar(255) not null,
    average\_score float default 0,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS projects (
    id int not null AUTO\_INCREMENT,
    name varchar(255) not null,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS corrections (
    user\_id int not null,
    project\_id int not null,
    score int default 0,
    KEY \`user\_id\` (\`user\_id\`),
    KEY \`project\_id\` (\`project\_id\`),
    CONSTRAINT fk\_user\_id FOREIGN KEY (\`user\_id\`) REFERENCES \`users\` (\`id\`) ON DELETE CASCADE,
    CONSTRAINT fk\_project\_id FOREIGN KEY (\`project\_id\`) REFERENCES \`projects\` (\`id\`) ON DELETE CASCADE
);

INSERT INTO users (name) VALUES ("Bob");
SET @user\_bob = LAST\_INSERT\_ID();

INSERT INTO users (name) VALUES ("Jeanne");
SET @user\_jeanne = LAST\_INSERT\_ID();

INSERT INTO projects (name) VALUES ("C is fun");
SET @project\_c = LAST\_INSERT\_ID();

INSERT INTO projects (name) VALUES ("Python is cool");
SET @project\_py = LAST\_INSERT\_ID();

INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_bob, @project\_c, 80);
INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_bob, @project\_py, 96);

INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_jeanne, @project\_c, 91);
INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_jeanne, @project\_py, 73);

bob@dylan:~$
bob@dylan:~$ cat 7-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 7-average\_score.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 7-main.sql
-- Show and compute average score
SELECT \* FROM users;
SELECT \* FROM corrections;

SELECT "--";
CALL ComputeAverageScoreForUser((SELECT id FROM users WHERE name = "Jeanne"));

SELECT "--";
SELECT \* FROM users;

bob@dylan:~$
bob@dylan:~$ cat 7-main.sql | mysql -uroot -p holberton
Enter password:
id  name    average\_score
1   Bob 0
2   Jeanne  0
user\_id project\_id  score
1   1   80
1   2   96
2   1   91
2   2   73
--
--
--
--
id  name    average\_score
1   Bob 0
2   Jeanne  82
bob@dylan:~$
```


### 9.

Write a SQL script that creates an index `idx_name_first` on the table `names` and the first letter of `name`.

**Requirements:**

*   Import this table dump: [names.sql.zip](https://intranet-projects-files.s3.amazonaws.com/holbertonschool-webstack/632/names.sql.zip "names.sql.zip")
*   Only the first letter of `name` must be indexed

**Context:** _Index is not the solution for any performance issue, but well used, it’s really powerful!_
```
bob@dylan:~$ cat names.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ mysql -uroot -p holberton
Enter password:
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%';
+-------------+
| COUNT(name) |
+-------------+
|      302936 |
+-------------+
1 row in set (2.19 sec)
mysql>
mysql> exit
bye
bob@dylan:~$
bob@dylan:~$ cat 8-index\_my\_names.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ mysql -uroot -p holberton
Enter password:
mysql> SHOW index FROM names;
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non\_unique | Key\_name       | Seq\_in\_index | Column\_name | Collation | Cardinality | Sub\_part | Packed | Null | Index\_type | Comment | Index\_comment |
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| names |          1 | idx\_name\_first |            1 | name        | A         |          25 |        1 | NULL   | YES  | BTREE      |         |               |
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
1 row in set (0.00 sec)
mysql>
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%';
+-------------+
| COUNT(name) |
+-------------+
|      302936 |
+-------------+
1 row in set (0.82 sec)
mysql>
mysql> exit
bye
bob@dylan:~$
```


### 10.

Write a SQL script that creates an index `idx_name_first_score` on the table `names` and the first letter of `name` and the `score`.

**Requirements:**

*   Import this table dump: [names.sql.zip](https://intranet-projects-files.s3.amazonaws.com/holbertonschool-webstack/632/names.sql.zip "names.sql.zip")
*   Only the first letter of `name` AND `score` must be indexed
```
bob@dylan:~$ cat names.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ mysql -uroot -p holberton
Enter password:
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%' AND score < 80;
+-------------+
| count(name) |
+-------------+
|       60717 |
+-------------+
1 row in set (2.40 sec)
mysql>
mysql> exit
bye
bob@dylan:~$
bob@dylan:~$ cat 9-index\_name\_score.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ mysql -uroot -p holberton
Enter password:
mysql> SHOW index FROM names;
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non\_unique | Key\_name             | Seq\_in\_index | Column\_name | Collation | Cardinality | Sub\_part | Packed | Null | Index\_type | Comment | Index\_comment |
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| names |          1 | idx\_name\_first\_score |            1 | name        | A         |          25 |        1 | NULL   | YES  | BTREE      |         |               |
| names |          1 | idx\_name\_first\_score |            2 | score       | A         |        3901 |     NULL | NULL   | YES  | BTREE      |         |               |
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
2 rows in set (0.00 sec)
mysql>
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%' AND score < 80;
+-------------+
| COUNT(name) |
+-------------+
|       60717 |
+-------------+
1 row in set (0.48 sec)
mysql>
mysql> exit
bye
bob@dylan:~$
```


### 11.

Write a SQL script that creates a function `SafeDiv` that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

**Requirements:**

*   You must create a function
*   The function `SafeDiv` takes 2 arguments:
    *   `a`, INT
    *   `b`, INT
*   And returns `a / b` or 0 if `b == 0`
```
bob@dylan:~$ cat 10-init.sql
-- Initial
DROP TABLE IF EXISTS numbers;

CREATE TABLE IF NOT EXISTS numbers (
    a int default 0,
    b int default 0
);

INSERT INTO numbers (a, b) VALUES (10, 2);
INSERT INTO numbers (a, b) VALUES (4, 5);
INSERT INTO numbers (a, b) VALUES (2, 3);
INSERT INTO numbers (a, b) VALUES (6, 3);
INSERT INTO numbers (a, b) VALUES (7, 0);
INSERT INTO numbers (a, b) VALUES (6, 8);

bob@dylan:~$ cat 10-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 10-div.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ echo "SELECT (a / b) FROM numbers;" | mysql -uroot -p holberton
Enter password:
(a / b)
5.0000
0.8000
0.6667
2.0000
NULL
0.7500
bob@dylan:~$
bob@dylan:~$ echo "SELECT SafeDiv(a, b) FROM numbers;" | mysql -uroot -p holberton
Enter password:
SafeDiv(a, b)
5
0.800000011920929
0.6666666865348816
2
0
0.75
bob@dylan:~$
```


### 12.

Write a SQL script that creates a view `need_meeting` that lists all students that have a score under 80 (strict) and no `last_meeting` or more than 1 month.

**Requirements:**

*   The view `need_meeting` should return all students name when:
    *   They score are under (strict) to 80
    *   **AND** no `last_meeting` date **OR** more than a month
```
bob@dylan:~$ cat 11-init.sql
-- Initial
DROP TABLE IF EXISTS students;

CREATE TABLE IF NOT EXISTS students (
    name VARCHAR(255) NOT NULL,
    score INT default 0,
    last\_meeting DATE NULL
);

INSERT INTO students (name, score) VALUES ("Bob", 80);
INSERT INTO students (name, score) VALUES ("Sylvia", 120);
INSERT INTO students (name, score) VALUES ("Jean", 60);
INSERT INTO students (name, score) VALUES ("Steeve", 50);
INSERT INTO students (name, score) VALUES ("Camilia", 80);
INSERT INTO students (name, score) VALUES ("Alexa", 130);

bob@dylan:~$ cat 11-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 11-need\_meeting.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 11-main.sql
-- Test view
SELECT \* FROM need\_meeting;

SELECT "--";

UPDATE students SET score = 40 WHERE name = 'Bob';
SELECT \* FROM need\_meeting;

SELECT "--";

UPDATE students SET score = 80 WHERE name = 'Steeve';
SELECT \* FROM need\_meeting;

SELECT "--";

UPDATE students SET last\_meeting = CURDATE() WHERE name = 'Jean';
SELECT \* FROM need\_meeting;

SELECT "--";

UPDATE students SET last\_meeting = ADDDATE(CURDATE(), INTERVAL -2 MONTH) WHERE name = 'Jean';
SELECT \* FROM need\_meeting;

SELECT "--";

SHOW CREATE TABLE need\_meeting;

SELECT "--";

SHOW CREATE TABLE students;

bob@dylan:~$
bob@dylan:~$ cat 11-main.sql | mysql -uroot -p holberton
Enter password:
name
Jean
Steeve
--
--
name
Bob
Jean
Steeve
--
--
name
Bob
Jean
--
--
name
Bob
--
--
name
Bob
Jean
--
--
View    Create View character\_set\_client    collation\_connection
XXXXXX<yes, here it will display the View SQL statement :-) >XXXXXX
--
--
Table   Create Table
students    CREATE TABLE \`students\` (\\n  \`name\` varchar(255) NOT NULL,\\n  \`score\` int(11) DEFAULT '0',\\n  \`last\_meeting\` date DEFAULT NULL\\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
bob@dylan:~$
## Resources

**Read or watch**:

*   [MySQL cheatsheet](/rltoken/XCHG-pgtifYRSw8ILB6DEw "MySQL cheatsheet")
*   [MySQL Performance: How To Leverage MySQL Database Indexing](/rltoken/VXAPISdkpKg3YD3HmVQXlw "MySQL Performance: How To Leverage MySQL Database Indexing")
*   [Stored Procedure](/rltoken/C37E-NvP8KxpI5Ds5w1oAQ "Stored Procedure")
*   [Triggers](/rltoken/0xFZu5AK0imLk70dxxcODA "Triggers")
*   [Views](/rltoken/Q8butAms3BthfCFhXuQSPA "Views")
*   [Functions and Operators](/rltoken/0ezATipRSpz1K8MixrD2Rg "Functions and Operators")
*   [Trigger Syntax and Examples](/rltoken/rc8oho9n7LAjtffC584tgA "Trigger Syntax and Examples")
*   [CREATE TABLE Statement](/rltoken/F1SUJgWz-4YNNYLPkL9tPw "CREATE TABLE Statement")
*   [CREATE PROCEDURE and CREATE FUNCTION Statements](/rltoken/XhYdXik2tTMK2k81WxulpA "CREATE PROCEDURE and CREATE FUNCTION Statements")
*   [CREATE INDEX Statement](/rltoken/K90KZ3z4gL5mPpHROlEOcg "CREATE INDEX Statement")
*   [CREATE VIEW Statement](/rltoken/VJESVxV2V7jGqrR-50903A "CREATE VIEW Statement")

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/j63kEGfU7eLokEipk6jQCA "explain to anyone"), **without the help of Google**:

### General

*   How to create tables with constraints
*   How to optimize queries by adding indexes
*   What is and how to implement stored procedures and functions in MySQL
*   What is and how to implement views in MySQL
*   What is and how to implement triggers in MySQL

## Requirements

### General

*   All your files will be executed on Ubuntu 20.04 LTS using `MySQL 8.0`
*   All your files should end with a new line
*   All your SQL queries should have a comment just before (i.e. syntax above)
*   All your files should start by a comment describing the task
*   All SQL keywords should be in uppercase (`SELECT`, `WHERE`…)
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   The length of your files will be tested using `wc`

## Tasks

### 1.

Write a SQL script that creates a table `users` following these requirements:

*   With these attributes:
    *   `id`, integer, never null, auto increment and primary key
    *   `email`, string (255 characters), never null and unique
    *   `name`, string (255 characters)
*   If the table already exists, your script should not fail
*   Your script can be executed on any database

**Context:** _Make an attribute unique directly in the table schema will enforced your business rules and avoid bugs in your application_
```
bob@dylan:~$ echo "SELECT \* FROM users;" | mysql -uroot -p holberton
Enter password:
ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
bob@dylan:~$
bob@dylan:~$ cat 0-uniq\_users.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");' | mysql -uroot -p holberton
Enter password:
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("sylvie@dylan.com", "Sylvie");' | mysql -uroot -p holberton
Enter password:
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Jean");' | mysql -uroot -p holberton
Enter password:
ERROR 1062 (23000) at line 1: Duplicate entry 'bob@dylan.com' for key 'email'
bob@dylan:~$
bob@dylan:~$ echo "SELECT \* FROM users;" | mysql -uroot -p holberton
Enter password:
id  email   name
1   bob@dylan.com   Bob
2   sylvie@dylan.com    Sylvie
bob@dylan:~$
```


### 2.

Write a SQL script that creates a table `users` following these requirements:

*   With these attributes:
    *   `id`, integer, never null, auto increment and primary key
    *   `email`, string (255 characters), never null and unique
    *   `name`, string (255 characters)
    *   `country`, enumeration of countries: `US`, `CO` and `TN`, never null (= default will be the first element of the enumeration, here `US`)
*   If the table already exists, your script should not fail
*   Your script can be executed on any database
```
bob@dylan:~$ echo "SELECT \* FROM users;" | mysql -uroot -p holberton
Enter password:
ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
bob@dylan:~$
bob@dylan:~$ cat 1-country\_users.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("bob@dylan.com", "Bob", "US");' | mysql -uroot -p holberton
Enter password:
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("sylvie@dylan.com", "Sylvie", "CO");' | mysql -uroot -p holberton
Enter password:
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("jean@dylan.com", "Jean", "FR");' | mysql -uroot -p holberton
Enter password:
ERROR 1265 (01000) at line 1: Data truncated for column 'country' at row 1
bob@dylan:~$
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("john@dylan.com", "John");' | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ echo "SELECT \* FROM users;" | mysql -uroot -p holberton
Enter password:
id  email   name    country
1   bob@dylan.com   Bob US
2   sylvie@dylan.com    Sylvie  CO
3   john@dylan.com  John    US
bob@dylan:~$
```


### 3.

Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans

**Requirements:**

*   Import this table dump: [metal\_bands.sql.zip](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2020/6/ab2979f058de215f0f2ae5b052739e76d3c02ac5.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20250317%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20250317T092325Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&X-Amz-Signature=da8f062e3725afd4932b14e500ce9844c7e6facec446c8379d76352383138742 "metal_bands.sql.zip")
*   Column names must be: `origin` and `nb_fans`
*   Your script can be executed on any database

**Context:** _Calculate/compute something is always power intensive… better to distribute the load!_
```
bob@dylan:~$ cat metal\_bands.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 2-fans.sql | mysql -uroot -p holberton > tmp\_res ; head tmp\_res
Enter password:
origin  nb\_fans
USA 99349
Sweden  47169
Finland 32878
United Kingdom  32518
Germany 29486
Norway  22405
Canada  8874
The Netherlands 8819
Italy   7178
bob@dylan:~$
```


### 4.

Write a SQL script that lists all bands with `Glam rock` as their main style, ranked by their longevity

**Requirements:**

*   Import this table dump: [metal\_bands.sql.zip](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2020/6/ab2979f058de215f0f2ae5b052739e76d3c02ac5.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20250317%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20250317T092325Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&X-Amz-Signature=da8f062e3725afd4932b14e500ce9844c7e6facec446c8379d76352383138742 "metal_bands.sql.zip")
*   Column names must be: `band_name` and `lifespan` (in years)
*   You should use attributes `formed` and `split` for computing the `lifespan`
*   Your script can be executed on any database
```
bob@dylan:~$ cat metal\_bands.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 3-glam\_rock.sql | mysql -uroot -p holberton
Enter password:
band\_name   lifespan
Alice Cooper    60
Mötley Crüe   34
Marilyn Manson  35
The 69 Eyes 34
Hardcore Superstar  27
Nasty Idols 0
Hanoi Rocks 0
bob@dylan:~$
```


### 5.

Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

Quantity in the table `items` can be negative.

**Context:** _Updating multiple tables for one action from your application can generate issue: network disconnection, crash, etc… to keep your data in a good shape, let MySQL do it for you!_
```
bob@dylan:~$ cat 4-init.sql
-- Initial
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS orders;

CREATE TABLE IF NOT EXISTS items (
    name VARCHAR(255) NOT NULL,
    quantity int NOT NULL DEFAULT 10
);

CREATE TABLE IF NOT EXISTS orders (
    item\_name VARCHAR(255) NOT NULL,
    number int NOT NULL
);

INSERT INTO items (name) VALUES ("apple"), ("pineapple"), ("pear");

bob@dylan:~$
bob@dylan:~$ cat 4-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 4-store.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 4-main.sql
Enter password:
-- Show and add orders
SELECT \* FROM items;
SELECT \* FROM orders;

INSERT INTO orders (item\_name, number) VALUES ('apple', 1);
INSERT INTO orders (item\_name, number) VALUES ('apple', 3);
INSERT INTO orders (item\_name, number) VALUES ('pear', 2);

SELECT "--";

SELECT \* FROM items;
SELECT \* FROM orders;

bob@dylan:~$
bob@dylan:~$ cat 4-main.sql | mysql -uroot -p holberton
Enter password:
name    quantity
apple   10
pineapple   10
pear    10
--
--
name    quantity
apple   6
pineapple   10
pear    8
item\_name   number
apple   1
apple   3
pear    2
bob@dylan:~$
```


### 6.

Write a SQL script that creates a trigger that resets the attribute `valid_email` only when the `email` has been changed.

**Context:** _Nothing related to MySQL, but perfect for user email validation - distribute the logic to the database itself!_
```
bob@dylan:~$ cat 5-init.sql
-- Initial
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO\_INCREMENT,
    email varchar(255) not null,
    name varchar(255),
    valid\_email boolean not null default 0,
    PRIMARY KEY (id)
);

INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");
INSERT INTO users (email, name, valid\_email) VALUES ("sylvie@dylan.com", "Sylvie", 1);
INSERT INTO users (email, name, valid\_email) VALUES ("jeanne@dylan.com", "Jeanne", 1);

bob@dylan:~$
bob@dylan:~$ cat 5-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 5-valid\_email.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 5-main.sql
Enter password:
-- Show users and update (or not) email
SELECT \* FROM users;

UPDATE users SET valid\_email = 1 WHERE email = "bob@dylan.com";
UPDATE users SET email = "sylvie+new@dylan.com" WHERE email = "sylvie@dylan.com";
UPDATE users SET name = "Jannis" WHERE email = "jeanne@dylan.com";

SELECT "--";
SELECT \* FROM users;

UPDATE users SET email = "bob@dylan.com" WHERE email = "bob@dylan.com";

SELECT "--";
SELECT \* FROM users;

bob@dylan:~$
bob@dylan:~$ cat 5-main.sql | mysql -uroot -p holberton
Enter password:
id  email   name    valid\_email
1   bob@dylan.com   Bob 0
2   sylvie@dylan.com    Sylvie  1
3   jeanne@dylan.com    Jeanne  1
--
--
id  email   name    valid\_email
1   bob@dylan.com   Bob 1
2   sylvie+new@dylan.com    Sylvie  0
3   jeanne@dylan.com    Jannis  1
--
--
id  email   name    valid\_email
1   bob@dylan.com   Bob 1
2   sylvie+new@dylan.com    Sylvie  0
3   jeanne@dylan.com    Jannis  1
bob@dylan:~$
```


### 7.

Write a SQL script that creates a stored procedure `AddBonus` that adds a new correction for a student.

**Requirements:**

*   Procedure `AddBonus` is taking 3 inputs (in this order):
    *   `user_id`, a `users.id` value (you can assume `user_id` is linked to an existing `users`)
    *   `project_name`, a new or already exists `projects` - if no `projects.name` found in the table, you should create it
    *   `score`, the score value for the correction

**Context:** _Write code in SQL is a nice level up!_
```
bob@dylan:~$ cat 6-init.sql
-- Initial
DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO\_INCREMENT,
    name varchar(255) not null,
    average\_score float default 0,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS projects (
    id int not null AUTO\_INCREMENT,
    name varchar(255) not null,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS corrections (
    user\_id int not null,
    project\_id int not null,
    score int default 0,
    KEY \`user\_id\` (\`user\_id\`),
    KEY \`project\_id\` (\`project\_id\`),
    CONSTRAINT fk\_user\_id FOREIGN KEY (\`user\_id\`) REFERENCES \`users\` (\`id\`) ON DELETE CASCADE,
    CONSTRAINT fk\_project\_id FOREIGN KEY (\`project\_id\`) REFERENCES \`projects\` (\`id\`) ON DELETE CASCADE
);

INSERT INTO users (name) VALUES ("Bob");
SET @user\_bob = LAST\_INSERT\_ID();

INSERT INTO users (name) VALUES ("Jeanne");
SET @user\_jeanne = LAST\_INSERT\_ID();

INSERT INTO projects (name) VALUES ("C is fun");
SET @project\_c = LAST\_INSERT\_ID();

INSERT INTO projects (name) VALUES ("Python is cool");
SET @project\_py = LAST\_INSERT\_ID();

INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_bob, @project\_c, 80);
INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_bob, @project\_py, 96);

INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_jeanne, @project\_c, 91);
INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_jeanne, @project\_py, 73);

bob@dylan:~$
bob@dylan:~$ cat 6-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 6-bonus.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 6-main.sql
Enter password:
-- Show and add bonus correction
SELECT \* FROM projects;
SELECT \* FROM corrections;

SELECT "--";

CALL AddBonus((SELECT id FROM users WHERE name = "Jeanne"), "Python is cool", 100);

CALL AddBonus((SELECT id FROM users WHERE name = "Jeanne"), "Bonus project", 100);
CALL AddBonus((SELECT id FROM users WHERE name = "Bob"), "Bonus project", 10);

CALL AddBonus((SELECT id FROM users WHERE name = "Jeanne"), "New bonus", 90);

SELECT "--";

SELECT \* FROM projects;
SELECT \* FROM corrections;

bob@dylan:~$
bob@dylan:~$ cat 6-main.sql | mysql -uroot -p holberton
Enter password:
id  name
1   C is fun
2   Python is cool
user\_id project\_id  score
1   1   80
1   2   96
2   1   91
2   2   73
--
--
--
--
id  name
1   C is fun
2   Python is cool
3   Bonus project
4   New bonus
user\_id project\_id  score
1   1   80
1   2   96
2   1   91
2   2   73
2   2   100
2   3   100
1   3   10
2   4   90
bob@dylan:~$
```


### 8.

Write a SQL script that creates a stored procedure `ComputeAverageScoreForUser` that computes and store the average score for a student. Note: An average score can be a decimal

**Requirements:**

*   Procedure `ComputeAverageScoreForUser` is taking 1 input:
    *   `user_id`, a `users.id` value (you can assume `user_id` is linked to an existing `users`)
```
bob@dylan:~$ cat 7-init.sql
-- Initial
DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO\_INCREMENT,
    name varchar(255) not null,
    average\_score float default 0,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS projects (
    id int not null AUTO\_INCREMENT,
    name varchar(255) not null,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS corrections (
    user\_id int not null,
    project\_id int not null,
    score int default 0,
    KEY \`user\_id\` (\`user\_id\`),
    KEY \`project\_id\` (\`project\_id\`),
    CONSTRAINT fk\_user\_id FOREIGN KEY (\`user\_id\`) REFERENCES \`users\` (\`id\`) ON DELETE CASCADE,
    CONSTRAINT fk\_project\_id FOREIGN KEY (\`project\_id\`) REFERENCES \`projects\` (\`id\`) ON DELETE CASCADE
);

INSERT INTO users (name) VALUES ("Bob");
SET @user\_bob = LAST\_INSERT\_ID();

INSERT INTO users (name) VALUES ("Jeanne");
SET @user\_jeanne = LAST\_INSERT\_ID();

INSERT INTO projects (name) VALUES ("C is fun");
SET @project\_c = LAST\_INSERT\_ID();

INSERT INTO projects (name) VALUES ("Python is cool");
SET @project\_py = LAST\_INSERT\_ID();

INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_bob, @project\_c, 80);
INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_bob, @project\_py, 96);

INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_jeanne, @project\_c, 91);
INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_jeanne, @project\_py, 73);

bob@dylan:~$
bob@dylan:~$ cat 7-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 7-average\_score.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 7-main.sql
-- Show and compute average score
SELECT \* FROM users;
SELECT \* FROM corrections;

SELECT "--";
CALL ComputeAverageScoreForUser((SELECT id FROM users WHERE name = "Jeanne"));

SELECT "--";
SELECT \* FROM users;

bob@dylan:~$
bob@dylan:~$ cat 7-main.sql | mysql -uroot -p holberton
Enter password:
id  name    average\_score
1   Bob 0
2   Jeanne  0
user\_id project\_id  score
1   1   80
1   2   96
2   1   91
2   2   73
--
--
--
--
id  name    average\_score
1   Bob 0
2   Jeanne  82
bob@dylan:~$
```


### 9.

Write a SQL script that creates an index `idx_name_first` on the table `names` and the first letter of `name`.

**Requirements:**

*   Import this table dump: [names.sql.zip](https://intranet-projects-files.s3.amazonaws.com/holbertonschool-webstack/632/names.sql.zip "names.sql.zip")
*   Only the first letter of `name` must be indexed

**Context:** _Index is not the solution for any performance issue, but well used, it’s really powerful!_
```
bob@dylan:~$ cat names.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ mysql -uroot -p holberton
Enter password:
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%';
+-------------+
| COUNT(name) |
+-------------+
|      302936 |
+-------------+
1 row in set (2.19 sec)
mysql>
mysql> exit
bye
bob@dylan:~$
bob@dylan:~$ cat 8-index\_my\_names.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ mysql -uroot -p holberton
Enter password:
mysql> SHOW index FROM names;
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non\_unique | Key\_name       | Seq\_in\_index | Column\_name | Collation | Cardinality | Sub\_part | Packed | Null | Index\_type | Comment | Index\_comment |
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| names |          1 | idx\_name\_first |            1 | name        | A         |          25 |        1 | NULL   | YES  | BTREE      |         |               |
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
1 row in set (0.00 sec)
mysql>
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%';
+-------------+
| COUNT(name) |
+-------------+
|      302936 |
+-------------+
1 row in set (0.82 sec)
mysql>
mysql> exit
bye
bob@dylan:~$
```


### 10.

Write a SQL script that creates an index `idx_name_first_score` on the table `names` and the first letter of `name` and the `score`.

**Requirements:**

*   Import this table dump: [names.sql.zip](https://intranet-projects-files.s3.amazonaws.com/holbertonschool-webstack/632/names.sql.zip "names.sql.zip")
*   Only the first letter of `name` AND `score` must be indexed
```
bob@dylan:~$ cat names.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ mysql -uroot -p holberton
Enter password:
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%' AND score < 80;
+-------------+
| count(name) |
+-------------+
|       60717 |
+-------------+
1 row in set (2.40 sec)
mysql>
mysql> exit
bye
bob@dylan:~$
bob@dylan:~$ cat 9-index\_name\_score.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ mysql -uroot -p holberton
Enter password:
mysql> SHOW index FROM names;
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non\_unique | Key\_name             | Seq\_in\_index | Column\_name | Collation | Cardinality | Sub\_part | Packed | Null | Index\_type | Comment | Index\_comment |
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| names |          1 | idx\_name\_first\_score |            1 | name        | A         |          25 |        1 | NULL   | YES  | BTREE      |         |               |
| names |          1 | idx\_name\_first\_score |            2 | score       | A         |        3901 |     NULL | NULL   | YES  | BTREE      |         |               |
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
2 rows in set (0.00 sec)
mysql>
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%' AND score < 80;
+-------------+
| COUNT(name) |
+-------------+
|       60717 |
+-------------+
1 row in set (0.48 sec)
mysql>
mysql> exit
bye
bob@dylan:~$
```


### 11.

Write a SQL script that creates a function `SafeDiv` that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

**Requirements:**

*   You must create a function
*   The function `SafeDiv` takes 2 arguments:
    *   `a`, INT
    *   `b`, INT
*   And returns `a / b` or 0 if `b == 0`
```
bob@dylan:~$ cat 10-init.sql
-- Initial
DROP TABLE IF EXISTS numbers;

CREATE TABLE IF NOT EXISTS numbers (
    a int default 0,
    b int default 0
);

INSERT INTO numbers (a, b) VALUES (10, 2);
INSERT INTO numbers (a, b) VALUES (4, 5);
INSERT INTO numbers (a, b) VALUES (2, 3);
INSERT INTO numbers (a, b) VALUES (6, 3);
INSERT INTO numbers (a, b) VALUES (7, 0);
INSERT INTO numbers (a, b) VALUES (6, 8);

bob@dylan:~$ cat 10-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 10-div.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ echo "SELECT (a / b) FROM numbers;" | mysql -uroot -p holberton
Enter password:
(a / b)
5.0000
0.8000
0.6667
2.0000
NULL
0.7500
bob@dylan:~$
bob@dylan:~$ echo "SELECT SafeDiv(a, b) FROM numbers;" | mysql -uroot -p holberton
Enter password:
SafeDiv(a, b)
5
0.800000011920929
0.6666666865348816
2
0
0.75
bob@dylan:~$
```


### 12.

Write a SQL script that creates a view `need_meeting` that lists all students that have a score under 80 (strict) and no `last_meeting` or more than 1 month.

**Requirements:**

*   The view `need_meeting` should return all students name when:
    *   They score are under (strict) to 80
    *   **AND** no `last_meeting` date **OR** more than a month
```
bob@dylan:~$ cat 11-init.sql
-- Initial
DROP TABLE IF EXISTS students;

CREATE TABLE IF NOT EXISTS students (
    name VARCHAR(255) NOT NULL,
    score INT default 0,
    last\_meeting DATE NULL
);

INSERT INTO students (name, score) VALUES ("Bob", 80);
INSERT INTO students (name, score) VALUES ("Sylvia", 120);
INSERT INTO students (name, score) VALUES ("Jean", 60);
INSERT INTO students (name, score) VALUES ("Steeve", 50);
INSERT INTO students (name, score) VALUES ("Camilia", 80);
INSERT INTO students (name, score) VALUES ("Alexa", 130);

bob@dylan:~$ cat 11-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 11-need\_meeting.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 11-main.sql
-- Test view
SELECT \* FROM need\_meeting;

SELECT "--";

UPDATE students SET score = 40 WHERE name = 'Bob';
SELECT \* FROM need\_meeting;

SELECT "--";

UPDATE students SET score = 80 WHERE name = 'Steeve';
SELECT \* FROM need\_meeting;

SELECT "--";

UPDATE students SET last\_meeting = CURDATE() WHERE name = 'Jean';
SELECT \* FROM need\_meeting;

SELECT "--";

UPDATE students SET last\_meeting = ADDDATE(CURDATE(), INTERVAL -2 MONTH) WHERE name = 'Jean';
SELECT \* FROM need\_meeting;

SELECT "--";

SHOW CREATE TABLE need\_meeting;

SELECT "--";

SHOW CREATE TABLE students;

bob@dylan:~$
bob@dylan:~$ cat 11-main.sql | mysql -uroot -p holberton
Enter password:
name
Jean
Steeve
--
--
name
Bob
Jean
Steeve
--
--
name
Bob
Jean
--
--
name
Bob
--
--
name
Bob
Jean
--
--
View    Create View character\_set\_client    collation\_connection
XXXXXX<yes, here it will display the View SQL statement :-) >XXXXXX
--
--
Table   Create Table
students    CREATE TABLE \`students\` (\\n  \`name\` varchar(255) NOT NULL,\\n  \`score\` int(11) DEFAULT '0',\\n  \`last\_meeting\` date DEFAULT NULL\\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
bob@dylan:~$

## Resources

**Read or watch**:

*   [MySQL cheatsheet](/rltoken/XCHG-pgtifYRSw8ILB6DEw "MySQL cheatsheet")
*   [MySQL Performance: How To Leverage MySQL Database Indexing](/rltoken/VXAPISdkpKg3YD3HmVQXlw "MySQL Performance: How To Leverage MySQL Database Indexing")
*   [Stored Procedure](/rltoken/C37E-NvP8KxpI5Ds5w1oAQ "Stored Procedure")
*   [Triggers](/rltoken/0xFZu5AK0imLk70dxxcODA "Triggers")
*   [Views](/rltoken/Q8butAms3BthfCFhXuQSPA "Views")
*   [Functions and Operators](/rltoken/0ezATipRSpz1K8MixrD2Rg "Functions and Operators")
*   [Trigger Syntax and Examples](/rltoken/rc8oho9n7LAjtffC584tgA "Trigger Syntax and Examples")
*   [CREATE TABLE Statement](/rltoken/F1SUJgWz-4YNNYLPkL9tPw "CREATE TABLE Statement")
*   [CREATE PROCEDURE and CREATE FUNCTION Statements](/rltoken/XhYdXik2tTMK2k81WxulpA "CREATE PROCEDURE and CREATE FUNCTION Statements")
*   [CREATE INDEX Statement](/rltoken/K90KZ3z4gL5mPpHROlEOcg "CREATE INDEX Statement")
*   [CREATE VIEW Statement](/rltoken/VJESVxV2V7jGqrR-50903A "CREATE VIEW Statement")

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/j63kEGfU7eLokEipk6jQCA "explain to anyone"), **without the help of Google**:

### General

*   How to create tables with constraints
*   How to optimize queries by adding indexes
*   What is and how to implement stored procedures and functions in MySQL
*   What is and how to implement views in MySQL
*   What is and how to implement triggers in MySQL

## Requirements

### General

*   All your files will be executed on Ubuntu 20.04 LTS using `MySQL 8.0`
*   All your files should end with a new line
*   All your SQL queries should have a comment just before (i.e. syntax above)
*   All your files should start by a comment describing the task
*   All SQL keywords should be in uppercase (`SELECT`, `WHERE`…)
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   The length of your files will be tested using `wc`

## Tasks

### 1.

Write a SQL script that creates a table `users` following these requirements:

*   With these attributes:
    *   `id`, integer, never null, auto increment and primary key
    *   `email`, string (255 characters), never null and unique
    *   `name`, string (255 characters)
*   If the table already exists, your script should not fail
*   Your script can be executed on any database

**Context:** _Make an attribute unique directly in the table schema will enforced your business rules and avoid bugs in your application_
```
bob@dylan:~$ echo "SELECT \* FROM users;" | mysql -uroot -p holberton
Enter password:
ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
bob@dylan:~$
bob@dylan:~$ cat 0-uniq\_users.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");' | mysql -uroot -p holberton
Enter password:
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("sylvie@dylan.com", "Sylvie");' | mysql -uroot -p holberton
Enter password:
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Jean");' | mysql -uroot -p holberton
Enter password:
ERROR 1062 (23000) at line 1: Duplicate entry 'bob@dylan.com' for key 'email'
bob@dylan:~$
bob@dylan:~$ echo "SELECT \* FROM users;" | mysql -uroot -p holberton
Enter password:
id  email   name
1   bob@dylan.com   Bob
2   sylvie@dylan.com    Sylvie
bob@dylan:~$
```


### 2.

Write a SQL script that creates a table `users` following these requirements:

*   With these attributes:
    *   `id`, integer, never null, auto increment and primary key
    *   `email`, string (255 characters), never null and unique
    *   `name`, string (255 characters)
    *   `country`, enumeration of countries: `US`, `CO` and `TN`, never null (= default will be the first element of the enumeration, here `US`)
*   If the table already exists, your script should not fail
*   Your script can be executed on any database
```
bob@dylan:~$ echo "SELECT \* FROM users;" | mysql -uroot -p holberton
Enter password:
ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
bob@dylan:~$
bob@dylan:~$ cat 1-country\_users.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("bob@dylan.com", "Bob", "US");' | mysql -uroot -p holberton
Enter password:
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("sylvie@dylan.com", "Sylvie", "CO");' | mysql -uroot -p holberton
Enter password:
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("jean@dylan.com", "Jean", "FR");' | mysql -uroot -p holberton
Enter password:
ERROR 1265 (01000) at line 1: Data truncated for column 'country' at row 1
bob@dylan:~$
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("john@dylan.com", "John");' | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ echo "SELECT \* FROM users;" | mysql -uroot -p holberton
Enter password:
id  email   name    country
1   bob@dylan.com   Bob US
2   sylvie@dylan.com    Sylvie  CO
3   john@dylan.com  John    US
bob@dylan:~$
```


### 3.

Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans

**Requirements:**

*   Import this table dump: [metal\_bands.sql.zip](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2020/6/ab2979f058de215f0f2ae5b052739e76d3c02ac5.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20250317%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20250317T092325Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&X-Amz-Signature=da8f062e3725afd4932b14e500ce9844c7e6facec446c8379d76352383138742 "metal_bands.sql.zip")
*   Column names must be: `origin` and `nb_fans`
*   Your script can be executed on any database

**Context:** _Calculate/compute something is always power intensive… better to distribute the load!_
```
bob@dylan:~$ cat metal\_bands.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 2-fans.sql | mysql -uroot -p holberton > tmp\_res ; head tmp\_res
Enter password:
origin  nb\_fans
USA 99349
Sweden  47169
Finland 32878
United Kingdom  32518
Germany 29486
Norway  22405
Canada  8874
The Netherlands 8819
Italy   7178
bob@dylan:~$
```


### 4.

Write a SQL script that lists all bands with `Glam rock` as their main style, ranked by their longevity

**Requirements:**

*   Import this table dump: [metal\_bands.sql.zip](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2020/6/ab2979f058de215f0f2ae5b052739e76d3c02ac5.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20250317%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20250317T092325Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&X-Amz-Signature=da8f062e3725afd4932b14e500ce9844c7e6facec446c8379d76352383138742 "metal_bands.sql.zip")
*   Column names must be: `band_name` and `lifespan` (in years)
*   You should use attributes `formed` and `split` for computing the `lifespan`
*   Your script can be executed on any database
```
bob@dylan:~$ cat metal\_bands.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 3-glam\_rock.sql | mysql -uroot -p holberton
Enter password:
band\_name   lifespan
Alice Cooper    60
Mötley Crüe   34
Marilyn Manson  35
The 69 Eyes 34
Hardcore Superstar  27
Nasty Idols 0
Hanoi Rocks 0
bob@dylan:~$
```


### 5.

Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

Quantity in the table `items` can be negative.

**Context:** _Updating multiple tables for one action from your application can generate issue: network disconnection, crash, etc… to keep your data in a good shape, let MySQL do it for you!_
```
bob@dylan:~$ cat 4-init.sql
-- Initial
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS orders;

CREATE TABLE IF NOT EXISTS items (
    name VARCHAR(255) NOT NULL,
    quantity int NOT NULL DEFAULT 10
);

CREATE TABLE IF NOT EXISTS orders (
    item\_name VARCHAR(255) NOT NULL,
    number int NOT NULL
);

INSERT INTO items (name) VALUES ("apple"), ("pineapple"), ("pear");

bob@dylan:~$
bob@dylan:~$ cat 4-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 4-store.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 4-main.sql
Enter password:
-- Show and add orders
SELECT \* FROM items;
SELECT \* FROM orders;

INSERT INTO orders (item\_name, number) VALUES ('apple', 1);
INSERT INTO orders (item\_name, number) VALUES ('apple', 3);
INSERT INTO orders (item\_name, number) VALUES ('pear', 2);

SELECT "--";

SELECT \* FROM items;
SELECT \* FROM orders;

bob@dylan:~$
bob@dylan:~$ cat 4-main.sql | mysql -uroot -p holberton
Enter password:
name    quantity
apple   10
pineapple   10
pear    10
--
--
name    quantity
apple   6
pineapple   10
pear    8
item\_name   number
apple   1
apple   3
pear    2
bob@dylan:~$
```


### 6.

Write a SQL script that creates a trigger that resets the attribute `valid_email` only when the `email` has been changed.

**Context:** _Nothing related to MySQL, but perfect for user email validation - distribute the logic to the database itself!_
```
bob@dylan:~$ cat 5-init.sql
-- Initial
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO\_INCREMENT,
    email varchar(255) not null,
    name varchar(255),
    valid\_email boolean not null default 0,
    PRIMARY KEY (id)
);

INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");
INSERT INTO users (email, name, valid\_email) VALUES ("sylvie@dylan.com", "Sylvie", 1);
INSERT INTO users (email, name, valid\_email) VALUES ("jeanne@dylan.com", "Jeanne", 1);

bob@dylan:~$
bob@dylan:~$ cat 5-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 5-valid\_email.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 5-main.sql
Enter password:
-- Show users and update (or not) email
SELECT \* FROM users;

UPDATE users SET valid\_email = 1 WHERE email = "bob@dylan.com";
UPDATE users SET email = "sylvie+new@dylan.com" WHERE email = "sylvie@dylan.com";
UPDATE users SET name = "Jannis" WHERE email = "jeanne@dylan.com";

SELECT "--";
SELECT \* FROM users;

UPDATE users SET email = "bob@dylan.com" WHERE email = "bob@dylan.com";

SELECT "--";
SELECT \* FROM users;

bob@dylan:~$
bob@dylan:~$ cat 5-main.sql | mysql -uroot -p holberton
Enter password:
id  email   name    valid\_email
1   bob@dylan.com   Bob 0
2   sylvie@dylan.com    Sylvie  1
3   jeanne@dylan.com    Jeanne  1
--
--
id  email   name    valid\_email
1   bob@dylan.com   Bob 1
2   sylvie+new@dylan.com    Sylvie  0
3   jeanne@dylan.com    Jannis  1
--
--
id  email   name    valid\_email
1   bob@dylan.com   Bob 1
2   sylvie+new@dylan.com    Sylvie  0
3   jeanne@dylan.com    Jannis  1
bob@dylan:~$
```


### 7.

Write a SQL script that creates a stored procedure `AddBonus` that adds a new correction for a student.

**Requirements:**

*   Procedure `AddBonus` is taking 3 inputs (in this order):
    *   `user_id`, a `users.id` value (you can assume `user_id` is linked to an existing `users`)
    *   `project_name`, a new or already exists `projects` - if no `projects.name` found in the table, you should create it
    *   `score`, the score value for the correction

**Context:** _Write code in SQL is a nice level up!_
```
bob@dylan:~$ cat 6-init.sql
-- Initial
DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO\_INCREMENT,
    name varchar(255) not null,
    average\_score float default 0,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS projects (
    id int not null AUTO\_INCREMENT,
    name varchar(255) not null,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS corrections (
    user\_id int not null,
    project\_id int not null,
    score int default 0,
    KEY \`user\_id\` (\`user\_id\`),
    KEY \`project\_id\` (\`project\_id\`),
    CONSTRAINT fk\_user\_id FOREIGN KEY (\`user\_id\`) REFERENCES \`users\` (\`id\`) ON DELETE CASCADE,
    CONSTRAINT fk\_project\_id FOREIGN KEY (\`project\_id\`) REFERENCES \`projects\` (\`id\`) ON DELETE CASCADE
);

INSERT INTO users (name) VALUES ("Bob");
SET @user\_bob = LAST\_INSERT\_ID();

INSERT INTO users (name) VALUES ("Jeanne");
SET @user\_jeanne = LAST\_INSERT\_ID();

INSERT INTO projects (name) VALUES ("C is fun");
SET @project\_c = LAST\_INSERT\_ID();

INSERT INTO projects (name) VALUES ("Python is cool");
SET @project\_py = LAST\_INSERT\_ID();

INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_bob, @project\_c, 80);
INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_bob, @project\_py, 96);

INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_jeanne, @project\_c, 91);
INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_jeanne, @project\_py, 73);

bob@dylan:~$
bob@dylan:~$ cat 6-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 6-bonus.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 6-main.sql
Enter password:
-- Show and add bonus correction
SELECT \* FROM projects;
SELECT \* FROM corrections;

SELECT "--";

CALL AddBonus((SELECT id FROM users WHERE name = "Jeanne"), "Python is cool", 100);

CALL AddBonus((SELECT id FROM users WHERE name = "Jeanne"), "Bonus project", 100);
CALL AddBonus((SELECT id FROM users WHERE name = "Bob"), "Bonus project", 10);

CALL AddBonus((SELECT id FROM users WHERE name = "Jeanne"), "New bonus", 90);

SELECT "--";

SELECT \* FROM projects;
SELECT \* FROM corrections;

bob@dylan:~$
bob@dylan:~$ cat 6-main.sql | mysql -uroot -p holberton
Enter password:
id  name
1   C is fun
2   Python is cool
user\_id project\_id  score
1   1   80
1   2   96
2   1   91
2   2   73
--
--
--
--
id  name
1   C is fun
2   Python is cool
3   Bonus project
4   New bonus
user\_id project\_id  score
1   1   80
1   2   96
2   1   91
2   2   73
2   2   100
2   3   100
1   3   10
2   4   90
bob@dylan:~$
```


### 8.

Write a SQL script that creates a stored procedure `ComputeAverageScoreForUser` that computes and store the average score for a student. Note: An average score can be a decimal

**Requirements:**

*   Procedure `ComputeAverageScoreForUser` is taking 1 input:
    *   `user_id`, a `users.id` value (you can assume `user_id` is linked to an existing `users`)
```
bob@dylan:~$ cat 7-init.sql
-- Initial
DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO\_INCREMENT,
    name varchar(255) not null,
    average\_score float default 0,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS projects (
    id int not null AUTO\_INCREMENT,
    name varchar(255) not null,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS corrections (
    user\_id int not null,
    project\_id int not null,
    score int default 0,
    KEY \`user\_id\` (\`user\_id\`),
    KEY \`project\_id\` (\`project\_id\`),
    CONSTRAINT fk\_user\_id FOREIGN KEY (\`user\_id\`) REFERENCES \`users\` (\`id\`) ON DELETE CASCADE,
    CONSTRAINT fk\_project\_id FOREIGN KEY (\`project\_id\`) REFERENCES \`projects\` (\`id\`) ON DELETE CASCADE
);

INSERT INTO users (name) VALUES ("Bob");
SET @user\_bob = LAST\_INSERT\_ID();

INSERT INTO users (name) VALUES ("Jeanne");
SET @user\_jeanne = LAST\_INSERT\_ID();

INSERT INTO projects (name) VALUES ("C is fun");
SET @project\_c = LAST\_INSERT\_ID();

INSERT INTO projects (name) VALUES ("Python is cool");
SET @project\_py = LAST\_INSERT\_ID();

INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_bob, @project\_c, 80);
INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_bob, @project\_py, 96);

INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_jeanne, @project\_c, 91);
INSERT INTO corrections (user\_id, project\_id, score) VALUES (@user\_jeanne, @project\_py, 73);

bob@dylan:~$
bob@dylan:~$ cat 7-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 7-average\_score.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 7-main.sql
-- Show and compute average score
SELECT \* FROM users;
SELECT \* FROM corrections;

SELECT "--";
CALL ComputeAverageScoreForUser((SELECT id FROM users WHERE name = "Jeanne"));

SELECT "--";
SELECT \* FROM users;

bob@dylan:~$
bob@dylan:~$ cat 7-main.sql | mysql -uroot -p holberton
Enter password:
id  name    average\_score
1   Bob 0
2   Jeanne  0
user\_id project\_id  score
1   1   80
1   2   96
2   1   91
2   2   73
--
--
--
--
id  name    average\_score
1   Bob 0
2   Jeanne  82
bob@dylan:~$
```


### 9.

Write a SQL script that creates an index `idx_name_first` on the table `names` and the first letter of `name`.

**Requirements:**

*   Import this table dump: [names.sql.zip](https://intranet-projects-files.s3.amazonaws.com/holbertonschool-webstack/632/names.sql.zip "names.sql.zip")
*   Only the first letter of `name` must be indexed

**Context:** _Index is not the solution for any performance issue, but well used, it’s really powerful!_
```
bob@dylan:~$ cat names.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ mysql -uroot -p holberton
Enter password:
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%';
+-------------+
| COUNT(name) |
+-------------+
|      302936 |
+-------------+
1 row in set (2.19 sec)
mysql>
mysql> exit
bye
bob@dylan:~$
bob@dylan:~$ cat 8-index\_my\_names.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ mysql -uroot -p holberton
Enter password:
mysql> SHOW index FROM names;
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non\_unique | Key\_name       | Seq\_in\_index | Column\_name | Collation | Cardinality | Sub\_part | Packed | Null | Index\_type | Comment | Index\_comment |
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| names |          1 | idx\_name\_first |            1 | name        | A         |          25 |        1 | NULL   | YES  | BTREE      |         |               |
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
1 row in set (0.00 sec)
mysql>
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%';
+-------------+
| COUNT(name) |
+-------------+
|      302936 |
+-------------+
1 row in set (0.82 sec)
mysql>
mysql> exit
bye
bob@dylan:~$
```


### 10.

Write a SQL script that creates an index `idx_name_first_score` on the table `names` and the first letter of `name` and the `score`.

**Requirements:**

*   Import this table dump: [names.sql.zip](https://intranet-projects-files.s3.amazonaws.com/holbertonschool-webstack/632/names.sql.zip "names.sql.zip")
*   Only the first letter of `name` AND `score` must be indexed
```
bob@dylan:~$ cat names.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ mysql -uroot -p holberton
Enter password:
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%' AND score < 80;
+-------------+
| count(name) |
+-------------+
|       60717 |
+-------------+
1 row in set (2.40 sec)
mysql>
mysql> exit
bye
bob@dylan:~$
bob@dylan:~$ cat 9-index\_name\_score.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ mysql -uroot -p holberton
Enter password:
mysql> SHOW index FROM names;
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non\_unique | Key\_name             | Seq\_in\_index | Column\_name | Collation | Cardinality | Sub\_part | Packed | Null | Index\_type | Comment | Index\_comment |
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| names |          1 | idx\_name\_first\_score |            1 | name        | A         |          25 |        1 | NULL   | YES  | BTREE      |         |               |
| names |          1 | idx\_name\_first\_score |            2 | score       | A         |        3901 |     NULL | NULL   | YES  | BTREE      |         |               |
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
2 rows in set (0.00 sec)
mysql>
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%' AND score < 80;
+-------------+
| COUNT(name) |
+-------------+
|       60717 |
+-------------+
1 row in set (0.48 sec)
mysql>
mysql> exit
bye
bob@dylan:~$
```


### 11.

Write a SQL script that creates a function `SafeDiv` that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

**Requirements:**

*   You must create a function
*   The function `SafeDiv` takes 2 arguments:
    *   `a`, INT
    *   `b`, INT
*   And returns `a / b` or 0 if `b == 0`
```
bob@dylan:~$ cat 10-init.sql
-- Initial
DROP TABLE IF EXISTS numbers;

CREATE TABLE IF NOT EXISTS numbers (
    a int default 0,
    b int default 0
);

INSERT INTO numbers (a, b) VALUES (10, 2);
INSERT INTO numbers (a, b) VALUES (4, 5);
INSERT INTO numbers (a, b) VALUES (2, 3);
INSERT INTO numbers (a, b) VALUES (6, 3);
INSERT INTO numbers (a, b) VALUES (7, 0);
INSERT INTO numbers (a, b) VALUES (6, 8);

bob@dylan:~$ cat 10-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 10-div.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ echo "SELECT (a / b) FROM numbers;" | mysql -uroot -p holberton
Enter password:
(a / b)
5.0000
0.8000
0.6667
2.0000
NULL
0.7500
bob@dylan:~$
bob@dylan:~$ echo "SELECT SafeDiv(a, b) FROM numbers;" | mysql -uroot -p holberton
Enter password:
SafeDiv(a, b)
5
0.800000011920929
0.6666666865348816
2
0
0.75
bob@dylan:~$
```


### 12.

Write a SQL script that creates a view `need_meeting` that lists all students that have a score under 80 (strict) and no `last_meeting` or more than 1 month.

**Requirements:**

*   The view `need_meeting` should return all students name when:
    *   They score are under (strict) to 80
    *   **AND** no `last_meeting` date **OR** more than a month
```
bob@dylan:~$ cat 11-init.sql
-- Initial
DROP TABLE IF EXISTS students;

CREATE TABLE IF NOT EXISTS students (
    name VARCHAR(255) NOT NULL,
    score INT default 0,
    last\_meeting DATE NULL
);

INSERT INTO students (name, score) VALUES ("Bob", 80);
INSERT INTO students (name, score) VALUES ("Sylvia", 120);
INSERT INTO students (name, score) VALUES ("Jean", 60);
INSERT INTO students (name, score) VALUES ("Steeve", 50);
INSERT INTO students (name, score) VALUES ("Camilia", 80);
INSERT INTO students (name, score) VALUES ("Alexa", 130);

bob@dylan:~$ cat 11-init.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 11-need\_meeting.sql | mysql -uroot -p holberton
Enter password:
bob@dylan:~$
bob@dylan:~$ cat 11-main.sql
-- Test view
SELECT \* FROM need\_meeting;

SELECT "--";

UPDATE students SET score = 40 WHERE name = 'Bob';
SELECT \* FROM need\_meeting;

SELECT "--";

UPDATE students SET score = 80 WHERE name = 'Steeve';
SELECT \* FROM need\_meeting;

SELECT "--";

UPDATE students SET last\_meeting = CURDATE() WHERE name = 'Jean';
SELECT \* FROM need\_meeting;

SELECT "--";

UPDATE students SET last\_meeting = ADDDATE(CURDATE(), INTERVAL -2 MONTH) WHERE name = 'Jean';
SELECT \* FROM need\_meeting;

SELECT "--";

SHOW CREATE TABLE need\_meeting;

SELECT "--";

SHOW CREATE TABLE students;

bob@dylan:~$
bob@dylan:~$ cat 11-main.sql | mysql -uroot -p holberton
Enter password:
name
Jean
Steeve
--
--
name
Bob
Jean
Steeve
--
--
name
Bob
Jean
--
--
name
Bob
--
--
name
Bob
Jean
--
--
View    Create View character\_set\_client    collation\_connection
XXXXXX<yes, here it will display the View SQL statement :-) >XXXXXX
--
--
Table   Create Table
students    CREATE TABLE \`students\` (\\n  \`name\` varchar(255) NOT NULL,\\n  \`score\` int(11) DEFAULT '0',\\n  \`last\_meeting\` date DEFAULT NULL\\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
bob@dylan:~$
```
