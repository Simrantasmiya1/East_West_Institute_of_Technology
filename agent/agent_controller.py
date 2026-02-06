from tools.campus_info_tool import get_campus_info
import json

def handle_query(user_query: str):
    query = user_query.lower()

    with open("data/campus_info.json", "r") as f:
        data = json.load(f)

    if "office" in query or "timing" in query:
        return f"🕘 Office Timings: {data['office_timings']}"

    if "college name" in query or "name" in query:
        return f"🏫 College Name: {data['college_name']}"

    if "address" in query:
        return f"📍 Address: {data['address']}"

    if "email" in query or "contact" in query:
        return f"📧 Contact Email: {data['contact_email']}"

    return (
        "🤖 I can help with:\n"
        "- Office timings\n"
        "- College name\n"
        "- Address\n"
        "- Contact email\n\n"
        "More features coming soon 🚀"
    )
