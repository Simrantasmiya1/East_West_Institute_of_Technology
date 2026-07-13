def agent_response(query, memory):
    # ==============================
    # 🔥 NORMALIZE QUERY
    # ==============================
    query = query.lower().strip()

    # ==============================
    # 🔥 INITIALIZE MEMORY
    # ==============================
    if "branch_scores" not in memory:
        memory["branch_scores"] = {}

    if "interest" not in memory:
        memory["interest"] = None

    # ==============================
    # 🎯 1. INTEREST DETECTION (UPDATED)
    # ==============================

    if any(word in query for word in [
        "coding", "programming", "software", "developer",
        "ai", "artificial intelligence"
    ]):

        # 🔥 AI-specific handling
        if "ai" in query or "artificial intelligence" in query:
            best_branch = "Artificial Intelligence & Data Science"
            memory["interest"] = "ai"

            memory["branch_scores"] = {
                "Artificial Intelligence": 90,
                "Computer Science": 85,
                "Information Technology": 75
            }

        else:
            best_branch = "Computer Science"
            memory["interest"] = "coding"

            memory["branch_scores"] = {
                "Computer Science": 90,
                "Information Technology": 80,
                "Electronics": 60
            }

        return f"""
🎯 Recommended Branch: {best_branch}

💼 Career Roles:
- Software Engineer
- Data Scientist
- AI Engineer

📊 Skill Gap:
- Python
- Machine Learning
- DSA

🛤️ Roadmap:
- Year 1: Programming Basics
- Year 2: DSA + Projects
- Year 3: Internships + AI/ML
- Year 4: Specialization + Placement Prep

📈 Confidence Score: 90%
"""

    # ==============================
    # 🎯 2. FOLLOW-UP HANDLING
    # ==============================

    if "branch" in query or "best branch" in query:
        if memory.get("interest") == "coding":
            return "👉 Based on your interest in coding, the best branch is Computer Science."
        elif memory.get("interest") == "ai":
            return "👉 Based on your interest in AI, the best branch is Artificial Intelligence & Data Science."

    # ==============================
    # 🎯 3. CAREER QUERY
    # ==============================

    if "career" in query:
        return """
💼 Career Options:
- Software Engineer
- Data Scientist
- AI Engineer
- Web Developer
"""

    # ==============================
    # 🎯 4. FACILITIES QUERY
    # ==============================

    if "facilities" in query:
        return """
🏫 Campus Facilities:
- Modern Labs
- Library
- Wi-Fi Campus
- Innovation Centers
"""

    # ==============================
    # 🎯 5. DEPARTMENTS QUERY
    # ==============================

    if "department" in query:
        return """
🏫 Departments Available:
- Computer Science
- Information Technology
- Electronics
- Mechanical
- Civil
"""

    # ==============================
    # ⚠️ DEFAULT RESPONSE
    # ==============================

    return """
🤖 I can help with:

• Branch recommendations  
• Career guidance  
• Skill analysis  
• Roadmap planning  

👉 Try asking:
- "I like coding"
- "I like AI"
- "Best branch for AI"
- "Career options"
"""