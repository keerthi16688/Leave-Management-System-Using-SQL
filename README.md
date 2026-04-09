# Leave-Management-System-Using-SQL
A Leave Management System developed using SQL to efficiently manage employee leave requests, approvals, and records.

# 🗂️ Leave Management System

## 📌 Description
The Leave Management System is a database-driven application designed to manage employee leave requests efficiently. It allows users to apply for leave, track leave history, and manage approvals using a structured SQL database.

---

## 🚀 Features
- 🔐 User Login System
- 📝 Apply for Leave
- 📊 View Leave History
- 📅 Leave Type & Date Management
- 🗃️ SQL Database Integration
- ✔️ Leave Status Tracking (Pending/Approved)

---

## 🛠️ Technologies Used
- SQL (MySQL)
- Database Management System
- Basic Frontend UI (Forms)

---

## 📷 Screenshots

### 🔑 Login Page
![Login](login.png)

### 📝 Apply Leave
![Apply Leave](apply_leave.png)

### 🗃️ Database (MySQL Workbench)
![Database](database.png)

### 📊 Leave History
![History](history.png)

---

## 🗄️ Database Structure

### Tables Used:
- **employees**
  - emp_id (Primary Key)
  - name
  - email
  - password
  - role

- **leave_applications**
  - leave_id (Primary Key)
  - emp_id (Foreign Key)
  - leave_type
  - from_date
  - to_date
  - reason
  - status

---

## ▶️ How to Run

1. Open MySQL Workbench
2. Create a new database
3. Run the SQL script provided in the project
4. Insert sample data (optional)
5. Run queries to test leave system

---

## 📈 Future Enhancements
- 🌐 Web-based interface
- 📧 Email notifications
- 📱 Mobile support
- 🔒 Advanced authentication system

---

## 👩‍💻 Author
**Keerthika S**

---

## ⭐ Project Purpose
This project is created for learning and demonstrating SQL-based database management skills for academic and placement purposes.
