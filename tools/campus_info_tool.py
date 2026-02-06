import json

def get_campus_info():
    """
    Tool to fetch public campus information as raw data
    """
    with open("data/campus_info.json", "r") as file:
        return json.load(file)
