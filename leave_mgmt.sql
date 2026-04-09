-- 1️⃣ Create Database
CREATE DATABASE IF NOT EXISTS leave_management;
USE leave_management;

-- 2️⃣ Create Employees Table
CREATE TABLE IF NOT EXISTS employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    role VARCHAR(20) NOT NULL,
    casual_leave INT DEFAULT 12,
    sick_leave INT DEFAULT 10,
    earned_leave INT DEFAULT 15
);

-- 3️⃣ Create Leave Applications Table
CREATE TABLE IF NOT EXISTS leave_applications (
    leave_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_id INT NOT NULL,
    leave_type VARCHAR(50) NOT NULL,
    from_date DATE NOT NULL,
    to_date DATE NOT NULL,
    reason TEXT NOT NULL,
    status VARCHAR(20) DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id) ON DELETE CASCADE
);

-- 4️⃣ Insert Sample Employees (15 + Admin)
INSERT INTO employees (name,email,password,role) VALUES
('Admin','admin@gmail.com','admin123','admin'),
('Arun','arun@gmail.com','1234','employee'),
('Bala','bala@gmail.com','1234','employee'),
('Charan','charan@gmail.com','1234','employee'),
('David','david@gmail.com','1234','employee'),
('Ezhil','ezhil@gmail.com','1234','employee'),
('Farhan','farhan@gmail.com','1234','employee'),
('Gokul','gokul@gmail.com','1234','employee'),
('Hari','hari@gmail.com','1234','employee'),
('Irfan','irfan@gmail.com','1234','employee'),
('Jeeva','jeeva@gmail.com','1234','employee'),
('Karthik','karthik@gmail.com','1234','employee'),
('Lokesh','lokesh@gmail.com','1234','employee'),
('Manoj','manoj@gmail.com','1234','employee'),
('Naveen','naveen@gmail.com','1234','employee');

-- 5️⃣ Optional: Sample Leave Applications
INSERT INTO leave_applications (emp_id, leave_type, from_date, to_date, reason)
VALUES
(2, 'Casual', '2026-04-10', '2026-04-12', 'Family function'),
(3, 'Sick', '2026-04-15', '2026-04-16', 'Fever and cold'),
(4, 'Earned', '2026-04-20', '2026-04-22', 'Vacation trip');

-- ✅ 6️⃣ Example: SELECT to check data
SELECT * FROM employees;
SELECT * FROM leave_applications;
