# -*- coding: simple task -*-

# -*- coding: UTF-8 -*-

tasks = []

def add_task(description):
    tasks.append({"description": description, "completed": False})

def show_tasks():
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task['description']} - Completed: {task['completed']}")

def update_task(index, description=None, completed=None):
    if description:
        tasks[index]["description"] = description
    if completed is not None:
        tasks[index]["completed"] = completed

def remove_task(index):
    tasks.pop(index)

while True:
    action = input("What would you like to do? (add/show/update/remove/exit) ")
    if action == "add":
        description = input("Enter the task description: ")
        add_task(description)
    elif action == "show":
        show_tasks()
    elif action == "update":
        index = int(input("Enter the task index: "))
        description = input("Enter the new task description (or leave empty to keep the current one): ")
        completed = None
        if description:
            completed = input("Is the task completed (yes/no)? ") == "yes"
        update_task(index, description, completed)
    elif action == "remove":
        index = int(input("Enter the task index: "))
        remove_task(index)
    elif action == "exit":
        break
    else:
        print("Invalid action.")
