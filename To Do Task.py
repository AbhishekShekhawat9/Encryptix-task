to_do_list = []

def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter a new task: ")
    to_do_list.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully.")

def view_tasks():
    if not to_do_list:
        print("No tasks found.")
    else:
        for idx, task in enumerate(to_do_list, start=1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{idx}. {task['task']} - {status}")

def update_task():
    view_tasks()
    try:
        task_no = int(input("Enter the task number to update: "))
        if 1 <= task_no <= len(to_do_list):
            new_task = input("Enter the new task description: ")
            to_do_list[task_no - 1]["task"] = new_task
            print(f"Task {task_no} updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter the task number to delete: "))
        if 1 <= task_no <= len(to_do_list):
            removed_task = to_do_list.pop(task_no - 1)
            print(f"Task '{removed_task['task']}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
