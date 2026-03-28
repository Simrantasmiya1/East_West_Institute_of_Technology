# =====================================================
# 🤖 ADVANCED AI AGENT PIPELINE
# =====================================================

def detect_intent(query):
    query = query.lower()

    if "career" in query or "branch" in query:
        return "career"

    elif "skills" in query:
        return "skills"

    elif "interview" in query:
        return "interview"

    else:
        return "general"


# =====================================================
# 🧠 MEMORY ENGINE
# =====================================================

def memory_engine(memory, query):
    if "coding" in query:
        memory["interest"] = "coding"

    elif "ai" in query:
        memory["interest"] = "ai"

    elif "mechanical" in query:
        memory["interest"] = "mechanical"

    return memory


# =====================================================
# 🎯 RESPONSE BUILDER
# =====================================================

def build_response(parts):
    return "\n\n".join(parts)