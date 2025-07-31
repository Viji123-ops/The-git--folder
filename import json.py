import json
import os

TASKS_FILE = 'tasks.json'

# Load tasks from file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)

# Show all tasks
def show_tasks(tasks):
    if not tasks:
        print("✅ No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✅" if task['completed'] else "❌"
        print(f"{i}. {task['title']} [{status}]")

# Add new task
def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({'title': title, 'completed': False})
    print("Task added successfully!")

# Mark task as completed
def complete_task(tasks):
    show_tasks(tasks)
    index = int(input("Enter task number to mark complete: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task(tasks):
    show_tasks(tasks)
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("Task deleted!")
    else:
        print("Invalid task number.")

# Main menu
def main():
    tasks = load_tasks()
    while True:
        print("\n🗒️  TO-DO LIST MENU")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Goodbye 👋")
            break
        else:
            print("Invalid option. Try again!")

if __name__ == "__main__":
    main()
