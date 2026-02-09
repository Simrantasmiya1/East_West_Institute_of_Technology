from tools.campus_info_tool import get_campus_info
from tools.departments_tool import get_departments
from tools.facilities_tool import get_facilities

def agent_response(user_query: str):
    query = user_query.lower()

    if "timing" in query or "office" in query:
        return get_campus_info()["office_timings"]

    elif "address" in query or "location" in query:
        return get_campus_info()["address"]

    elif "email" in query or "contact" in query:
        return get_campus_info()["contact_email"]

    elif "department" in query:
        departments = get_departments()
        return "Departments available:\n- " + "\n- ".join(departments)

    elif "facility" in query:
        facilities = get_facilities()
        return "Facilities available:\n- " + "\n- ".join(facilities)

    elif "college name" in query or "name" in query:
        return get_campus_info()["college_name"]

    else:
        return (
            "I can help with:\n"
            "- Office timings\n"
            "- College address\n"
            "- Contact email\n"
            "- Departments\n"
            "- Facilities"
        )
