import string
from builtins import list, int, dict


class Todo:
    def __init__(self):
        self.completed = None

    def _init_(self, code_id: int, title: string, description: string):
        self.code_id = code_id
        self.title = title
        self.description = description
        self.completed = False
        self.tags: list[string] = []

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag: string):
        if tag not in self.tags:
            self.tags.append(tag)

    def _str_(self):
        return f"{self.code_id} - {self.title}"


class TodoBook:
    def __init__(self):
        self.todos: dict[int, Todo] = {}

    def add_todo(self, title: string, description: string) -> int:
        code_id = len(self.todos) + 1
        new_todo = Todo()
        new_todo._init_(code_id, title, description)
        self.todos[code_id] = new_todo
        return code_id

    def pending_todos(self) -> list[Todo]:
        return [todo for todo in self.todos.values() if not todo.completed]

    def completed_todos(self) -> list[Todo]:
        return [todo for todo in self.todos.values() if todo.completed]

    def tags_todo_count(self) -> dict[string, int]:
        tags_count: dict[string, int] = {}
        for todo in self.todos.values():
            for tag in todo.tags:
                if tag in tags_count:
                    tags_count[tag] += 1
                else:
                    tags_count[tag] = 1
        return tags_count
