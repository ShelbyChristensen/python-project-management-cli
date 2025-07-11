import subprocess

def test_add_user():
    result = subprocess.run(
        ["python3", "main.py", "add-user", "--name", "Alice", "--email", "alice@example.com"],
        capture_output=True,
        text=True
    )
    assert "✅ User Alice added." in result.stdout

def test_add_project():
    result = subprocess.run(
        [
            "python3", "main.py", "add-project",
            "--user", "Alice", "--title", "CLI Tool", "--description", "Test CLI", "--due_date", "2025-08-01"
        ],
        capture_output=True,
        text=True
    )
    assert "✅ Project CLI Tool added for user Alice." in result.stdout

def test_add_task_and_complete():
    subprocess.run(
        [
            "python3", "main.py", "add-task",
            "--project", "CLI Tool", "--title", "Write CLI", "--assigned_to", "Alice"
        ],
        capture_output=True,
        text=True
    )
    result = subprocess.run(
        [
            "python3", "main.py", "complete-task",
            "--project", "CLI Tool", "--title", "Write CLI"
        ],
        capture_output=True,
        text=True
    )
    assert "✅ Task Write CLI marked as complete." in result.stdout
