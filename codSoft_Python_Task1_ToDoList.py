''' Author- Jagu Manish || Python Programming Internship at CodSoft

------------------ TASK 1 - TO-DO LIST -----------------------
A To-Do List application is a useful project that helps users manage
and organize their tasks efficiently. This project aims to create a
command-line or GUI-based application using Python, allowing
users to create, update, and track their to-do lists.

IDE used: Pycharm
Tip: Use VS Code for better performance / UI.
'''

#importing modules
import os

#class for list contents description updation
class Task:
    def __init__(self, description):
        self.description = description
        self.has_completed = False

    def marked_as_completed(self):
        self.has_completed = True

    def update_description(self, updated_description):
        self.description = updated_description

#class for To-Do list
class ToDoList:
    def __init__(self):
        self.tasks = []

    def view_tasks(self):
        if not self.tasks:
            print("Your To-Do List is empty!")
        else:
            for index, task in enumerate(self.tasks, start=1):
                if task.has_completed:
                    status = "Completed"
                else:
                    status = "pending"
                print(f"{index}. {task.description} - {status}")

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Task {description} is added successfully!")

    def update_task(self, task_index, updated_description = None, marked_as_completed = False):
        if 0 <= task_index < len(self.tasks):
            if updated_description:
                self.tasks[task_index].update_description(updated_description)
                print(f"Task {task_index + 1} description is updated successfully!")
            if marked_as_completed:
                self.tasks[task_index].marked_as_completed()
                print(f"Task {task_index + 1} is marked as completed successfully!")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f" Task {removed_task.description} is deleted successfully!")
        else:
            print("Invalid task index.")

def application():
    todo_list = ToDoList()

    while True:
        print("┌────────────────────────────────┐")
        print("│     TO-DO LIST APPLICATION     │")
        print("├────────────────────────────────┤")
        print("│       1. View Tasks            │")
        print("│       2. Add a Task            │")
        print("│       3. Update a Task         │")
        print("│       4. Delete a Task         │")
        print("│       5. Clear the screen      │")
        print("│       6. Exit                  │")
        print("└────────────────────────────────┘")

        choice =int(input("Enter your choice: "))

        if choice == 1:
            todo_list.view_tasks()
        elif choice == 2:
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == 3:
            print("\nYour Tasks:")
            todo_list.view_tasks()
            print("\n")
            task_index = int(input("Enter task index to proceed the updation process: ")) - 1
            updated_description = input("Enter new description (or leave blank to keep current): ")
            marked_as_completed = input("Do you want to mark it as completed? (y/n): ").lower() == 'y'
            todo_list.update_task(task_index, updated_description if updated_description else None, marked_as_completed)
        elif choice == 4:
            print("\nYour Tasks:")
            todo_list.view_tasks()
            print("\n")
            task_index = int(input("Enter task index to delete: ")) - 1
            todo_list.delete_task(task_index)

        elif choice == 5:
            os.system('cls')

        elif choice == 6:
            break
            os.system('cls')
        else:
            print("Invalid choice. Please try again.")
application()
