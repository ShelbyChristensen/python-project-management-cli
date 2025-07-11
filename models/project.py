from datetime import datetime

class Project:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def __str__(self):
        return f"{self.title} (Due: {self.due_date.date()})"
