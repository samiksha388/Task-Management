import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring
from datetime import datetime

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        due_date = askstring("Due Date", "Enter due date (YYYY-MM-DD) or leave blank:")
        priority = askstring("Priority", "Enter priority (High/Medium/Low) or leave blank:")
        category = askstring("Category", "Enter category or leave blank:")
        task_details = {
            "task": task,
            "completed": False,
            "due_date": due_date if due_date else "No due date",
            "priority": priority if priority else "No priority",
            "category": category if category else "No category"
        }
        tasks.append(task_details)
        update_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        update_tasks()
    else:
        messagebox.showwarning("Warning", "No task selected!")

def complete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks[selected_task_index[0]]["completed"] = True
        update_tasks()
    else:
        messagebox.showwarning("Warning", "No task selected!")

def search_tasks():
    keyword = search_entry.get()
    if keyword:
        search_results = [task for task in tasks if keyword.lower() in task["task"].lower()]
        task_listbox.delete(0, tk.END)
        for task in search_results:
            status = "Completed" if task["completed"] else "Pending"
            task_listbox.insert(tk.END, f'{task["task"]} [{status}] - Due: {task["due_date"]} - Priority: {task["priority"]} - Category: {task["category"]}')
    else:
        messagebox.showwarning("Warning", "Search keyword cannot be empty!")

def update_tasks():
    task_listbox.delete(0, tk.END)
    sorted_tasks = sorted(tasks, key=lambda x: x["priority"], reverse=True)
    for task in sorted_tasks:
        status = "Completed" if task["completed"] else "Pending"
        task_listbox.insert(tk.END, f'{task["task"]} [{status}] - Due: {task["due_date"]} - Priority: {task["priority"]} - Category: {task["category"]}')

def clear_all_tasks():
    tasks.clear()
    update_tasks()

def change_due_date():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        new_due_date = askstring("New Due Date", "Enter new due date (YYYY-MM-DD):")
        if new_due_date:
            tasks[selected_task_index[0]]["due_date"] = new_due_date
            update_tasks()
        else:
            messagebox.showwarning("Warning", "Due date cannot be empty!")
    else:
        messagebox.showwarning("Warning", "No task selected!")

# Create the main window
root = tk.Tk()
root.title("Task Manager")
root.geometry("600x700")  # Set window size
root.configure(bg="#2e2e2e")  # Set background color to dark

# Define custom fonts
font_style = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")

# Create and place the widgets
task_label = tk.Label(root, text="Enter a task:", font=font_style, fg="white", bg="#2e2e2e")
task_label.pack(pady=5)

task_entry = tk.Entry(root, width=50, font=font_style, bg="#3e3e3e", fg="white")
task_entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task, font=button_font, bg="#4caf50", fg="white")
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, font=button_font, bg="#f44336", fg="white")
delete_button.pack(pady=5)

complete_button = tk.Button(root, text="Complete Task", command=complete_task, font=button_font, bg="#2196f3", fg="white")
complete_button.pack(pady=5)

change_due_date_button = tk.Button(root, text="Change Due Date", command=change_due_date, font=button_font, bg="#ffeb3b", fg="black")
change_due_date_button.pack(pady=5)

search_label = tk.Label(root, text="Search tasks:", font=font_style, fg="white", bg="#2e2e2e")
search_label.pack(pady=5)

search_entry = tk.Entry(root, width=50, font=font_style, bg="#3e3e3e", fg="white")
search_entry.pack(pady=5)

search_button = tk.Button(root, text="Search", command=search_tasks, font=button_font, bg="#ff9800", fg="white")
search_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", command=clear_all_tasks, font=button_font, bg="#9e9e9e", fg="white")
clear_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=50, height=10, font=font_style, bg="#3e3e3e", fg="white")
task_listbox.pack(pady=10)

# Start the main loop
root.mainloop()