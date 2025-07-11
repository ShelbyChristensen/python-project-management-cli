import argparse
from models.user import User
from models.project import Project
from models.task import Task
from utils import file_io

USERS_FILE = "data/users.json"
PROJECTS_FILE = "data/projects.json"
TASKS_FILE = "data/tasks.json"

def add_user(args):
    users = file_io.load_json(USERS_FILE)
    user = {"name": args.name, "email": args.email}
    users.append(user)
    file_io.save_json(USERS_FILE, users)
    print(f"✅ User {args.name} added.")

def add_project(args):
    projects = file_io.load_json(PROJECTS_FILE)
    project = {"title": args.title, "description": args.description, "due_date": args.due_date, "user": args.user}
    projects.append(project)
    file_io.save_json(PROJECTS_FILE, projects)
    print(f"✅ Project {args.title} added for user {args.user}.")

def add_task(args):
    tasks = file_io.load_json(TASKS_FILE)
    task = {"title": args.title, "assigned_to": args.assigned_to, "project": args.project, "status": "Pending"}
    tasks.append(task)
    file_io.save_json(TASKS_FILE, tasks)
    print(f"✅ Task {args.title} added to project {args.project}.")

def complete_task(args):
    tasks = file_io.load_json(TASKS_FILE)
    for task in tasks:
        if task["title"] == args.title and task["project"] == args.project:
            task["status"] = "Completed"
            print(f"✅ Task {args.title} marked as complete.")
            break
    else:
        print("❌ Task not found.")
    file_io.save_json(TASKS_FILE, tasks)

def main():
    parser = argparse.ArgumentParser(description="Project Management CLI Tool")
    subparsers = parser.add_subparsers()

    user_parser = subparsers.add_parser("add-user", help="Add a new user")
    user_parser.add_argument("--name", required=True)
    user_parser.add_argument("--email", required=True)
    user_parser.set_defaults(func=add_user)

    project_parser = subparsers.add_parser("add-project", help="Add a new project")
    project_parser.add_argument("--user", required=True)
    project_parser.add_argument("--title", required=True)
    project_parser.add_argument("--description", required=True)
    project_parser.add_argument("--due_date", required=True)
    project_parser.set_defaults(func=add_project)

    task_parser = subparsers.add_parser("add-task", help="Add a new task")
    task_parser.add_argument("--project", required=True)
    task_parser.add_argument("--title", required=True)
    task_parser.add_argument("--assigned_to", required=True)
    task_parser.set_defaults(func=add_task)

    complete_parser = subparsers.add_parser("complete-task", help="Complete a task")
    complete_parser.add_argument("--project", required=True)
    complete_parser.add_argument("--title", required=True)
    complete_parser.set_defaults(func=complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
