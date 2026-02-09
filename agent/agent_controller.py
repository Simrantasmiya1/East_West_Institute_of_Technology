from tools.campus_info_tool import get_campus_info
from tools.departments_tool import get_departments
from tools.facilities_tool import get_facilities


def agent_response(user_query: str) -> str:
    query = user_query.lower()

    # Intent: Office Timings
    if "office" in query or "timing" in query or "hours" in query:
        info = get_campus_info()
        return f"🕘 Office Timings:\n{info['office_timings']}"

    # Intent: College Name
    if "college name" in query or "name of college" in query:
        info = get_campus_info()
        return f"🏫 College Name:\n{info['college_name']}"

    # Intent: Address
    if "address" in query or "location" in query:
        info = get_campus_info()
        return f"📍 College Address:\n{info['address']}"

    # Intent: Departments
    if "department" in query:
        departments = get_departments()
        dept_list = "\n".join(f"• {d}" for d in departments)
        return f"🎓 Available Departments:\n{dept_list}"

    # Intent: Facilities
    if "facility" in query or "facilities" in query:
        facilities = get_facilities()
        fac_list = "\n".join(f"• {f}" for f in facilities)
        return f"🏢 Campus Facilities:\n{fac_list}"

    # Fallback
    return (
        "🤖 I can help you with:\n"
        "• Office timings\n"
        "• College address\n"
        "• College name\n"
        "• Departments\n"
        "• Facilities\n\n"
        "Please ask a relevant campus-related question 😊"
    )
