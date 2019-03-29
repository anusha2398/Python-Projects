#table

CREATE TABLE books (id INTEGER PRIMARY KEY, name TEXT, rating INTEGER);

INSERT into books VALUES (1, "One Indian Girl", 4);
INSERT into books VALUES (2, "Becoming", 5);
INSERT into books VALUES (3, "Angel's Flight", 5);

SELECT * FROM books;






#selecting

CREATE TABLE movies (id INTEGER PRIMARY KEY, name TEXT, release_year INTEGER);
INSERT INTO movies VALUES (1, "Avatar", 2009);
INSERT INTO movies VALUES (2, "Titanic", 1997);
INSERT INTO movies VALUES (3, "Star Wars: Episode IV - A New Hope", 1977);
INSERT INTO movies VALUES (4, "Shrek 2", 2004);
INSERT INTO movies VALUES (5, "The Lion King", 1994);
INSERT INTO movies VALUES (6, "Disney's Up", 2009);

SELECT * FROM movies;
SELECT * FROM movies WHERE release_year > 2000 ORDER BY release_year


#aggregate
CREATE TABLE todo_list (id INTEGER PRIMARY KEY, item TEXT, minutes INTEGER);
INSERT INTO todo_list VALUES (1, "Wash the dishes", 15);
INSERT INTO todo_list VALUES (2, "vacuuming", 20);
INSERT INTO todo_list VALUES (3, "Learn some stuff on KA", 30);
INSERT INTO todo_list VALUES (4, "Outing", 60);

SELECT SUM(minutes) FROM todo_list 



#project
#project
CREATE TABLE clothing (id INTEGER PRIMARY KEY, name TEXT, price INTEGER, quantity INTEGER, availability TEXT);
INSERT INTO clothing VALUES (1, "Shirts", 200, 1, "yes");
INSERT INTO clothing VALUES (2, "T-shirts", 150, 3, "no");
INSERT INTO clothing VALUES (3, "Trousers", 500, 2, "yes");
INSERT INTO clothing VALUES (4, "Shirts", 200, 1, "yes");
INSERT INTO clothing VALUES (5, "Jeans", 800, 2, "no");
SELECT * FROM clothing;


SELECT SUM(price) FROM clothing;
SELECT * FROM clothing GROUP BY price;




