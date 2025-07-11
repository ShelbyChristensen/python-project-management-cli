class Task:
    def __init__(self, title, assigned_to):
        self.title = title
        self.assigned_to = assigned_to
        self.status = "Pending"

    def complete(self):
        self.status = "Completed"

    def __str__(self):
        return f"{self.title} - {self.status} (Assigned to: {self.assigned_to})"
