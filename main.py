import tkinter as tk
from tkinter import messagebox
import mysql.connector

# -------- DATABASE CONNECTION --------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",  # change this
    database="leave_management"
)
cursor = conn.cursor()

# -------- LOGIN FUNCTION --------
def login():
    email = email_entry.get()
    password = password_entry.get()

    query = "SELECT emp_id, name FROM employees WHERE email=%s AND password=%s"
    cursor.execute(query, (email, password))
    result = cursor.fetchone()

    if result:
        root.destroy()
        open_dashboard(result[0], result[1])
    else:
        messagebox.showerror("Error", "Invalid Credentials")


# -------- APPLY LEAVE --------
def apply_leave(emp_id):
    leave_type = type_entry.get()
    from_date = from_entry.get()
    to_date = to_entry.get()
    reason = reason_entry.get()

    query = """
    INSERT INTO leave_applications 
    (emp_id, leave_type, from_date, to_date, reason, status)
    VALUES (%s, %s, %s, %s, %s, 'Pending')
    """
    cursor.execute(query, (emp_id, leave_type, from_date, to_date, reason))
    conn.commit()

    messagebox.showinfo("Success", "Leave Applied!")


# -------- VIEW HISTORY --------
def view_history(emp_id):
    history_window = tk.Toplevel()
    history_window.title("Leave History")
    history_window.geometry("600x300")

    query = "SELECT leave_id, leave_type, from_date, to_date, reason, status FROM leave_applications WHERE emp_id=%s"
    cursor.execute(query, (emp_id,))
    data = cursor.fetchall()

    for i, row in enumerate(data):
        for j, val in enumerate(row):
            tk.Label(history_window, text=val, borderwidth=1, relief="solid", width=12).grid(row=i, column=j)


# -------- DASHBOARD --------
def open_dashboard(emp_id, name):
    global type_entry, from_entry, to_entry, reason_entry

    dash = tk.Tk()
    dash.title("Apply Leave")
    dash.geometry("400x400")
    dash.configure(bg="#1e2a38")

    tk.Label(dash, text="Apply Leave", fg="cyan", bg="#1e2a38", font=("Arial", 16)).pack(pady=10)

    tk.Label(dash, text="Leave Type", bg="#1e2a38", fg="white").pack()
    type_entry = tk.Entry(dash)
    type_entry.pack()

    tk.Label(dash, text="From Date (YYYY-MM-DD)", bg="#1e2a38", fg="white").pack()
    from_entry = tk.Entry(dash)
    from_entry.pack()

    tk.Label(dash, text="To Date (YYYY-MM-DD)", bg="#1e2a38", fg="white").pack()
    to_entry = tk.Entry(dash)
    to_entry.pack()

    tk.Label(dash, text="Reason", bg="#1e2a38", fg="white").pack()
    reason_entry = tk.Entry(dash)
    reason_entry.pack()

    tk.Button(dash, text="Apply Leave", bg="blue", fg="white",
              command=lambda: apply_leave(emp_id)).pack(pady=10)

    tk.Button(dash, text="View History", bg="blue", fg="white",
              command=lambda: view_history(emp_id)).pack()

    dash.mainloop()


# -------- LOGIN UI --------
root = tk.Tk()
root.title("Leave Management System")
root.geometry("400x300")
root.configure(bg="#1e2a38")

tk.Label(root, text="Leave Management System", fg="cyan", bg="#1e2a38",
         font=("Arial", 16)).pack(pady=20)

tk.Label(root, text="Email", bg="#1e2a38", fg="white").pack()
email_entry = tk.Entry(root, width=30)
email_entry.pack()

tk.Label(root, text="Password", bg="#1e2a38", fg="white").pack()
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack()

tk.Button(root, text="Login", bg="blue", fg="white", command=login).pack(pady=20)

root.mainloop()
