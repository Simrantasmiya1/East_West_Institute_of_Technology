from tools.campus_info_tool import get_campus_info

def process_query(user_query):
    """
    Week-1 Agent Logic:
    Decides when to call which tool
    """
    query = user_query.lower()

    if "college" in query or "campus" in query:
        return get_campus_info()

    return (
        "🤖 I am still learning.\n\n"
        "From next week, I will answer questions about:\n"
        "- Departments\n"
        "- Facilities\n"
        "- Events\n"
        "- Rules and procedures"
    )