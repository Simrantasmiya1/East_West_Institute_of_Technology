import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "departments.json")

def get_departments():
    with open(DATA_PATH, "r") as file:
        data = json.load(file)
    return data["departments"]
