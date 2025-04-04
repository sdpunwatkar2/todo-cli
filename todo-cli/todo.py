import json
import os

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
        return
    for i, task in enumerate(tasks):
        status = "✅" if task["done"] else "❌"
        print(f"{i+1}. [{status}] {task['title']}")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Complete Task\n4. Delete Task\n5. Exit")
        choice = input("Choose: ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            title = input("Enter task: ")
            tasks.append({"title": title, "done": False})
        elif choice == "3":
            show_tasks(tasks)
            idx = int(input("Complete task #: ")) - 1
            if 0 <= idx < len(tasks):
                tasks[idx]["done"] = True
        elif choice == "4":
            show_tasks(tasks)
            idx = int(input("Delete task #: ")) - 1
            if 0 <= idx < len(tasks):
                tasks.pop(idx)
        elif choice == "5":
            save_tasks(tasks)
            print("Bye! 👋")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
