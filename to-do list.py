#_______________________________________________________________________________
#Name: Atharva Lokhande
#Purpose: Task
#Task: 1
#Author: atharva
#created: 20-07-23
#_______________________________________________________________________________

import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_task():
    global root  # Make root global
    try:
        index = listbox_tasks.curselection()[0]
        selected_task = listbox_tasks.get(index)
        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Task")

        entry_edit_task = tk.Entry(edit_window, width=40)
        entry_edit_task.insert(0, selected_task)
        entry_edit_task.pack(pady=10)

        def save_changes():
            new_task = entry_edit_task.get()
            if new_task:
                listbox_tasks.delete(index)
                listbox_tasks.insert(index, new_task)
                edit_window.destroy()
            else:
                messagebox.showwarning("Warning", "Please enter a task.")

        button_save_changes = tk.Button(edit_window, text="Save Changes", command=save_changes, bg="blue", fg="white")
        button_save_changes.pack(pady=5)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

def clear_tasks():
    listbox_tasks.delete(0, tk.END)

def main():
    global entry_task, listbox_tasks, root  # Make entry_task, listbox_tasks, and root global
    root = tk.Tk()
    root.title("To-Do List")
    root.geometry("400x400")

    label_title = tk.Label(root, text="To-Do List", font=("Helvetica", 20))
    label_title.pack(pady=10)

    frame_tasks = tk.Frame(root)
    frame_tasks.pack()

    listbox_tasks = tk.Listbox(frame_tasks, width=50, height=10, selectbackground="lightblue", selectforeground="black")
    listbox_tasks.pack(side=tk.LEFT)

    scrollbar_tasks = tk.Scrollbar(frame_tasks)
    scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

    listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
    scrollbar_tasks.config(command=listbox_tasks.yview)

    entry_task = tk.Entry(root, width=40)
    entry_task.pack(pady=10)

    button_add_task = tk.Button(root, text="Add Task", command=add_task, bg="green", fg="white")
    button_add_task.pack(side=tk.LEFT, padx=5)

    button_update_task = tk.Button(root, text="Update Task", command=update_task, bg="blue", fg="white")
    button_update_task.pack(side=tk.LEFT, padx=5)

    button_delete_task = tk.Button(root, text="Delete Task", command=delete_task, bg="red", fg="white")
    button_delete_task.pack(side=tk.LEFT, padx=5)

    button_clear_tasks = tk.Button(root, text="Clear All", command=clear_tasks, bg="orange", fg="white")
    button_clear_tasks.pack(side=tk.LEFT, padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()
