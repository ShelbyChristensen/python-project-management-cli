import json
import os

def load_json(file_path):
    try:
        if not os.path.exists(file_path):
            return []
        with open(file_path, 'r') as file:
            content = file.read().strip()
            if not content:
                return []
            return json.loads(content)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
