""" To-Do List Manager """

import json
import os

FILENAME = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file, or start with an empty list if none exist."""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    """Save the current list of tasks to the JSON file."""
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks):
    task_name = input("Enter the task: ").strip()
    if task_name:
        tasks.append({"task": task_name, "done": False})
        save_tasks(tasks)
        print(f"Added: {task_name}")
    else:
        print("Task cannot be empty.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks yet. Add one!")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "x" if task["done"] else " "
        print(f"{i}. [{status}] {task['task']}")


def complete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        choice = int(input("Enter the task number to mark as done: "))
        tasks[choice - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as done!")
    except (ValueError, IndexError):
        print("Invalid task number.")


def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        choice = int(input("Enter the task number to delete: "))
        removed = tasks.pop(choice - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed['task']}")
    except (ValueError, IndexError):
        print("Invalid task number.")


def print_menu():
    print("""
==== To-Do List Manager ====
1. View tasks
2. Add task
3. Mark task as done
4. Delete task
5. Exit
""")


def main():
    tasks = load_tasks()

    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
