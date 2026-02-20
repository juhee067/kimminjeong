# To-Do List Feature

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

if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.add_todo("Write code")
    todo_list.add_todo("Test feature")
    print("Current To-Dos:", todo_list.list_todos())
    todo_list.complete_todo(0)
    print("Updated To-Dos:", todo_list.list_todos())