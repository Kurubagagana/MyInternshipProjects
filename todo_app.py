# Step 1: Create a Task class to represent individual tasks
class Task:
    def __init__(self, description, due_date=None, priority=None):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.description} (Due: {self.due_date}, Priority: {self.priority}) - {status}"

# Step 2: Create a ToDoList class to manage the list of tasks
class ToDoList:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        print("Tasks:")
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")

        print("\nCompleted Tasks:")
        for i, task in enumerate(self.completed_tasks):
            print(f"{i + 1}. {task}")

    def mark_as_completed(self, task_index):
        task = self.tasks.pop(task_index)
        task.completed = True
        self.completed_tasks.append(task)

    def update_task(self, task_index, new_description, new_due_date, new_priority):
        task = self.tasks[task_index]
        task.description = new_description
        task.due_date = new_due_date
        task.priority = new_priority

    def remove_task(self, task_index):
        del self.tasks[task_index]

# Step 3: Implement the user interface
def main():
    todo_list = ToDoList()

    while True:
        print("\n==== ToDo List App ====")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Update Task")
        print("5. Remove Task")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional): ")
            priority = input("Enter priority (optional): ")
            new_task = Task(description, due_date, priority)
            todo_list.add_task(new_task)
            print("Task added successfully!")

        elif choice == "2":
            todo_list.display_tasks()

        elif choice == "3":
            task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
            todo_list.mark_as_completed(task_index)
            print("Task marked as completed!")

        elif choice == "4":
            task_index = int(input("Enter the index of the task to update: ")) - 1
            new_description = input("Enter new task description: ")
            new_due_date = input("Enter new due date (optional): ")
            new_priority = input("Enter new priority (optional): ")
            todo_list.update_task(task_index, new_description, new_due_date, new_priority)
            print("Task updated successfully!")

        elif choice == "5":
            task_index = int(input("Enter the index of the task to remove: ")) - 1
            todo_list.remove_task(task_index)
            print("Task removed successfully!")

        elif choice == "0":
            print("Exiting the ToDo List App. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
