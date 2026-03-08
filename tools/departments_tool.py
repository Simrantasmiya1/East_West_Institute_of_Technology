import json
import os

DATA_PATH = os.path.join("data", "departments.json")


def get_departments():
    with open(DATA_PATH, "r") as file:
        data = json.load(file)

    return data["departments"]
