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