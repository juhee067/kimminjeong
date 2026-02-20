# To-Do List Feature with Console Interface

class TodoList:
    def __init__(self):
        self.todos = []

    def add_todo(self, task):
        self.todos.append({'task': task, 'completed': False})

    def complete_todo(self, index):
        if 0 <= index < len(self.todos):
            self.todos[index]['completed'] = True

    def remove_todo(self, index):
        if 0 <= index < len(self.todos):
            self.todos.pop(index)

    def list_todos(self):
        return self.todos

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Remove Task")
        print("4. Show Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_todo(task)
            print("Task added.")
        elif choice == "2":
            index = int(input("Enter the task number to complete: ")) - 1
            todo_list.complete_todo(index)
            print("Task marked as completed.")
        elif choice == "3":
            index = int(input("Enter the task number to remove: ")) - 1
            todo_list.remove_todo(index)
            print("Task removed.")
        elif choice == "4":
            print("\nCurrent Tasks:")
            for i, todo in enumerate(todo_list.list_todos(), start=1):
                status = "[Done]" if todo['completed'] else "[Pending]"
                print(f"{i}. {todo['task']} {status}")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()