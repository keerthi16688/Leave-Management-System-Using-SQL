import tkinter as tk
from tkinter import messagebox
from db_connection import connect_db
from datetime import datetime

# ---------------- LOGIN ---------------- #

def login():
    email = email_entry.get()
    password = password_entry.get()

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT emp_id, role FROM employees WHERE email=%s AND password=%s",
                   (email, password))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("Success", "Login Successful")
        root.destroy()
        if user[1] == "admin":
            admin_panel()
        else:
            employee_panel(user[0])
    else:
        messagebox.showerror("Error", "Invalid Login")

    conn.close()

# ---------------- ADMIN PANEL ---------------- #

def admin_panel():
    admin = tk.Tk()
    admin.title("Admin Panel")

    def view_leaves():
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM leave_applications")
        data = cursor.fetchall()
        messagebox.showinfo("All Leaves", str(data))
        conn.close()

    def approve_leave():
        leave_id = leave_id_entry.get()
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE leave_applications SET status='Approved' WHERE leave_id=%s",
                       (leave_id,))
        conn.commit()
        messagebox.showinfo("Success", "Leave Approved")
        conn.close()

    tk.Button(admin, text="View Leaves", command=view_leaves).pack()
    tk.Label(admin, text="Leave ID").pack()
    leave_id_entry = tk.Entry(admin)
    leave_id_entry.pack()
    tk.Button(admin, text="Approve Leave", command=approve_leave).pack()

    admin.mainloop()

# ---------------- EMPLOYEE PANEL ---------------- #

def employee_panel(emp_id):
    emp = tk.Tk()
    emp.title("Employee Panel")

    def apply_leave():
        leave_type = type_entry.get()
        from_date = from_entry.get()
        to_date = to_entry.get()
        reason = reason_entry.get()

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO leave_applications 
                          (emp_id, leave_type, from_date, to_date, reason) 
                          VALUES (%s,%s,%s,%s,%s)""",
                       (emp_id, leave_type, from_date, to_date, reason))
        conn.commit()

        messagebox.showinfo("Success", "Leave Applied")
        conn.close()

    def view_history():
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM leave_applications WHERE emp_id=%s",
                       (emp_id,))
        data = cursor.fetchall()
        messagebox.showinfo("Leave History", str(data))
        conn.close()

    tk.Label(emp, text="Leave Type").pack()
    type_entry = tk.Entry(emp)
    type_entry.pack()

    tk.Label(emp, text="From Date (YYYY-MM-DD)").pack()
    from_entry = tk.Entry(emp)
    from_entry.pack()

    tk.Label(emp, text="To Date (YYYY-MM-DD)").pack()
    to_entry = tk.Entry(emp)
    to_entry.pack()

    tk.Label(emp, text="Reason").pack()
    reason_entry = tk.Entry(emp)
    reason_entry.pack()

    tk.Button(emp, text="Apply Leave", command=apply_leave).pack()
    tk.Button(emp, text="View History", command=view_history).pack()

    emp.mainloop()

# ---------------- MAIN LOGIN WINDOW ---------------- #

root = tk.Tk()
root.title("Leave Management System")

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Login", command=login).pack()

root.mainloop()
