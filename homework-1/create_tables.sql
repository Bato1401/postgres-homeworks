-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employee_id serial PRIMARY KEY NOT NULL,
    first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
    title varchar(300) NOT NULL,
	birth_date date NOT NULL,
    notes text
);

CREATE TABLE customers
(
    customer_id char(100) PRIMARY KEY NOT NULL,
	company_name varchar(150) NOT NULL,
    contact_name varchar(300) NOT NULL
);


CREATE TABLE orders
(
    order_id int PRIMARY KEY NOT NULL,
	customer_id char(100) REFERENCES customers(customer_id) NOT NULL,
    employee_id int REFERENCES employees(employee_id) NOT NULL,
	order_date date NOT NULL,
	ship_city char(100) NOT NULL
);