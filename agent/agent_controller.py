from tools.campus_info_tool import get_campus_info

def process_query(user_query):
    data = get_campus_info()
    query = user_query.lower()

    # Office timings
    if "office" in query or "timing" in query:
        return f"🕘 Office Timings: {data['office_timings']}"

    # College name
    elif "college name" in query or "name of college" in query:
        return f"🏫 College Name: {data['college_name']}"

    # Address
    elif "address" in query or "location" in query:
        return f"📍 Address: {data['address']}"

    # Email / contact
    elif "email" in query or "contact" in query:
        return f"📧 Contact Email: {data['contact_email']}"

    # Unknown question
    else:
        return (
            "🤖 I can help with:\n"
            "- Office timings\n"
            "- College address\n"
            "- College contact email\n"
            "- College name\n\n"
            "More features coming next week 🚀"
        )
