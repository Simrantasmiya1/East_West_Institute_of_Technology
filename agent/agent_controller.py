from tools.campus_info_tool import get_campus_info
from tools.departments_tool import get_departments
from tools.facilities_tool import get_facilities

def agent_response(user_query: str) -> str:
    query = user_query.lower()
    info = get_campus_info()

    # Office timings
    if any(word in query for word in ["office", "timing", "hours"]):
        return f"🕘 The college office timings are {info['office_timings']}."

    # Address / location
    if any(word in query for word in ["address", "location", "where"]):
        return f"📍 The college is located at:\n{info['address']}."

    # Contact / email
    if any(word in query for word in ["email", "contact", "mail"]):
        return f"📧 You can contact the college at:\n{info['contact_email']}."

    # Departments
    if any(word in query for word in ["department", "branch", "course"]):
        departments = get_departments()
        return (
            "🏫 The college offers the following departments:\n"
            + "\n".join(f"• {dept}" for dept in departments)
        )

    # Facilities
    if any(word in query for word in ["facility", "facilities", "amenities"]):
        facilities = get_facilities()
        return (
            "🏢 The campus provides these facilities:\n"
            + "\n".join(f"• {facility}" for facility in facilities)
        )

    # Polite fallback
    return (
        "🤖 I’m here to help with campus-related information.\n\n"
        "You can ask me about:\n"
        "• Office timings\n"
        "• College address\n"
        "• Departments or courses\n"
        "• Campus facilities\n"
        "• Contact email\n\n"
        "Please try asking one of these 😊"
    )
