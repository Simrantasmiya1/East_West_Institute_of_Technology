import json

def get_campus_info():
    """
    Tool to fetch basic public campus information
    """
    with open("data/campus_info.json", "r") as file:
        data = json.load(file)

    return (
        f"🏫 College Name: {data['college_name']}\n"
        f"📍 Address: {data['address']}\n"
        f"🕘 Office Timings: {data['office_timings']}\n"
        f"📧 Contact Email: {data['contact_email']}"
    )