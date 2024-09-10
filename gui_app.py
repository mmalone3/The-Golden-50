import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to get a database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn

# Function to add an activity to the database
def add_activity(name, start_time, end_time, duration):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO activities (name, start_time, end_time, duration) VALUES (?, ?, ?, ?)",
                   (name, start_time, end_time, duration))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Activity added successfully")

# Function to display activities for a specific date
def display_activities_for_date(date):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM activities WHERE start_time LIKE ?", (date + '%',))
    activities = cursor.fetchall()
    conn.close()

    display_text = ""
    for activity in activities:
        display_text += f"ID: {activity[0]}, Name: {activity[1]}, Start Time: {activity[2]}, End Time: {activity[3]}, Duration: {activity[4]}\n"
    
    if display_text:
        messagebox.showinfo("Activities", display_text)
    else:
        messagebox.showinfo("Activities", "No activities found for this date")

# Create the main window
root = tk.Tk()
root.title("Activity Tracker")

# Create and place the widgets
tk.Label(root, text="Name").grid(row=0, column=0)
tk.Label(root, text="Start Time").grid(row=1, column=0)
tk.Label(root, text="End Time").grid(row=2, column=0)
tk.Label(root, text="Duration").grid(row=3, column=0)
tk.Label(root, text="Date (YYYY-MM-DD)").grid(row=4, column=0)

name_entry = tk.Entry(root)
start_time_entry = tk.Entry(root)
end_time_entry = tk.Entry(root)
duration_entry = tk.Entry(root)
date_entry = tk.Entry(root)

name_entry.grid(row=0, column=1)
start_time_entry.grid(row=1, column=1)
end_time_entry.grid(row=2, column=1)
duration_entry.grid(row=3, column=1)
date_entry.grid(row=4, column=1)

tk.Button(root, text="Add Activity", command=lambda: add_activity(
    name_entry.get(), start_time_entry.get(), end_time_entry.get(), duration_entry.get())).grid(row=5, column=0, columnspan=2)

tk.Button(root, text="Display Activities for Date", command=lambda: display_activities_for_date(date_entry.get())).grid(row=6, column=0, columnspan=2)

# Run the main loop
root.mainloop()