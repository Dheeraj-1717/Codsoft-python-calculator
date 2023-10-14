import os

# Initialize an empty list to store tasks
tasks = []

# Function to display the list of tasks
def display_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to add a new task
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks()
    print(f"Task '{task}' added to the to-do list.")

# Function to update a task
def update_task():
    display_tasks()
    try:
        index = int(input("Enter the number of the task to update: ")) - 1
        if 0 <= index < len(tasks):
            new_task = input("Enter the updated task: ")
            tasks[index] = new_task
            save_tasks()
            print(f"Task updated to '{new_task}'.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Function to delete a task
def delete_task():
    display_tasks()
    try:
        index = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= index < len(tasks):
            deleted_task = tasks.pop(index)
            save_tasks()
            print(f"Task '{deleted_task}' deleted from the to-do list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Function to save tasks to a file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to load tasks from a file
def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            global tasks
            tasks = [line.strip() for line in file]

# Main function
def main():
    load_tasks()
    print("Welcome to the To-Do List Application!")

    while True:
        print("\nMenu:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
