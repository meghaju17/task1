class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def __str__(self):
        status = 'Completed' if self.completed else 'Pending'
        return f"{self.title}: {self.description} [{status}]"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        print(f"Task '{title}' added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")

    def update_task(self, index, title=None, description=None, completed=None):
        if index < 0 or index >= len(self.tasks):
            print("Invalid task number.")
            return
        task = self.tasks[index]
        if title:
            task.title = title
        if description:
            task.description = description
        if completed is not None:
            task.completed = completed
        print(f"Task '{task.title}' updated successfully.")

    def delete_task(self, index):
        if index < 0 or index >= len(self.tasks):
            print("Invalid task number.")
            return
        task = self.tasks.pop(index)
        print(f"Task '{task.title}' deleted successfully.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)

        elif choice == '2':
            todo_list.view_tasks()

        elif choice == '3':
            todo_list.view_tasks()
            try:
                index = int(input("Enter task number to update: ")) - 1
                title = input("Enter new title (leave blank to keep current): ")
                description = input("Enter new description (leave blank to keep current): ")
                completed = input("Is the task completed? (yes/no): ").lower()
                if completed == 'yes':
                    completed = True
                elif completed == 'no':
                    completed = False
                else:
                    completed = None
                todo_list.update_task(index, title or None, description or None, completed)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '4':
            todo_list.view_tasks()
            try:
                index = int(input("Enter task number to delete: ")) - 1
                todo_list.delete_task(index)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

