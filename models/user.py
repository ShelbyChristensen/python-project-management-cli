class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def __str__(self):
        return f"{self.name} ({self.email})"
