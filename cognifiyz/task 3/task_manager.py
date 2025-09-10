# Task Manager Console Application
# Author: Srimayee (CRUD Example)

class Task:
    """Represents a task with id, title, description, and status."""
    def __init__(self, task_id: int, title: str, description: str, status: str = "Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"ID: {self.task_id} | Title: {self.title} | Desc: {self.description} | Status: {self.status}"


class TaskManager:
    """Manages CRUD operations on tasks."""
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def create_task(self, title: str, description: str):
        task = Task(self.next_id, title, description)
        self.tasks.append(task)
        self.next_id += 1
        print("✅ Task created successfully!")

    def read_tasks(self):
        if not self.tasks:
            print("📭 No tasks available.")
        else:
            print("\n📋 Task List:")
            for task in self.tasks:
                print(task)

    def update_task(self, task_id: int, new_title: str, new_description: str, new_status: str):
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = new_title
                task.description = new_description
                task.status = new_status
                print("✅ Task updated successfully!")
                return
        print("❌ Task not found!")

    def delete_task(self, task_id: int):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print("🗑️ Task deleted successfully!")
                return
        print("❌ Task not found!")


def main():
    manager = TaskManager()

    while True:
        print("\n====== Task Manager ======")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            manager.create_task(title, description)

        elif choice == "2":
            manager.read_tasks()

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to update: "))
                new_title = input("Enter new title: ")
                new_description = input("Enter new description: ")
                new_status = input("Enter new status (Pending/Completed): ")
                manager.update_task(task_id, new_title, new_description, new_status)
            except ValueError:
                print("❌ Invalid ID!")

        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
                manager.delete_task(task_id)
            except ValueError:
                print("❌ Invalid ID!")

        elif choice == "5":
            print("👋 Exiting Task Manager. Goodbye!")
            break

        else:
            print("❌ Invalid choice! Please select 1-5.")


if __name__ == "__main__":
    main()
