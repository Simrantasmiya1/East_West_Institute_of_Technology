import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "campus_info.json")

def get_campus_info():
    with open(DATA_PATH, "r") as file:
        return json.load(file)
