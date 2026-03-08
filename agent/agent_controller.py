from tools.campus_info_tool import get_campus_info
from tools.departments_tool import get_departments
from tools.facilities_tool import get_facilities
from tools.report_generator import generate_career_report


# =====================================================
# 🧠 CAREER SCORING ENGINE
# =====================================================

def career_scoring_engine(query, memory):
    query = query.lower()

    scores = {
        "Computer Science & Engineering": 0,
        "Artificial Intelligence & Machine Learning": 0,
        "Electronics & Communication": 0,
        "Mechanical Engineering": 0,
        "Civil Engineering": 0
    }

    interest = memory.get("interest")

    # Coding Interest
    if "coding" in query or interest == "coding":
        scores["Computer Science & Engineering"] += 40
        scores["Artificial Intelligence & Machine Learning"] += 35

    # AI Interest
    if "ai" in query or "machine learning" in query or interest == "ai":
        scores["Artificial Intelligence & Machine Learning"] += 45
        scores["Computer Science & Engineering"] += 25

    # Mechanical Interest
    if "machine" in query or "mechanical" in query or interest == "mechanical":
        scores["Mechanical Engineering"] += 45

    # Electronics
    if "electronics" in query:
        scores["Electronics & Communication"] += 40

    # Civil
    if "design" in query:
        scores["Civil Engineering"] += 35

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    best_branch = ranked[0][0]
    confidence = min(98, 70 + ranked[0][1])

    return best_branch, ranked, confidence


# =====================================================
# 📈 CAREER INTELLIGENCE ENGINE
# =====================================================

def career_intelligence_engine(branch):

    market_data = {
        "Computer Science & Engineering": {
            "growth": "Very High 📈",
            "salary": "₹8–25 LPA",
            "global_demand": "Excellent 🌍",
            "power_index": 9.8
        },
        "Artificial Intelligence & Machine Learning": {
            "growth": "Explosive 🚀",
            "salary": "₹10–30 LPA",
            "global_demand": "Very High 🌎",
            "power_index": 9.9
        },
        "Mechanical Engineering": {
            "growth": "Stable 📊",
            "salary": "₹5–12 LPA",
            "global_demand": "Moderate 🌐",
            "power_index": 8.2
        }
    }

    data = market_data.get(branch, {
        "growth": "Stable",
        "salary": "Industry Based",
        "global_demand": "Moderate",
        "power_index": 7.0
    })

    return (
        "📈 Market Intelligence Analysis:\n"
        f"• Industry Growth: {data['growth']}\n"
        f"• Average Salary Range: {data['salary']}\n"
        f"• Global Demand: {data['global_demand']}\n"
        f"• Career Power Index: {data['power_index']}/10"
    )


# =====================================================
# 🎯 SKILL GAP ANALYSIS
# =====================================================

def skill_gap_analysis(branch):

    skill_map = {
        "Computer Science & Engineering": [
            "Python",
            "Data Structures",
            "Algorithms",
            "Web Development",
            "Cloud Computing"
        ],
        "Artificial Intelligence & Machine Learning": [
            "Python",
            "Linear Algebra",
            "Machine Learning",
            "Deep Learning",
            "Data Analysis"
        ],
        "Mechanical Engineering": [
            "CAD Design",
            "Thermodynamics",
            "Robotics",
            "Manufacturing Systems"
        ]
    }

    skills = skill_map.get(branch, ["Core Technical Skills"])

    formatted_skills = "\n".join([f"• {skill}" for skill in skills])

    return (
        "🎯 Skill Gap Analysis:\n"
        "To succeed in this branch, focus on:\n"
        f"{formatted_skills}"
    )


# =====================================================
# 🛣 ROADMAP GENERATOR
# =====================================================

def generate_roadmap(branch):

    if "Computer Science" in branch:
        return {
            "Year 1": "Programming + Mathematics",
            "Year 2": "Data Structures + Algorithms",
            "Year 3": "Web Development + Internships",
            "Year 4": "AI / Cloud + Major Project"
        }

    if "Artificial Intelligence" in branch:
        return {
            "Year 1": "Python + Math Foundations",
            "Year 2": "Machine Learning Basics",
            "Year 3": "Deep Learning + Projects",
            "Year 4": "AI Specialization + Research"
        }

    if "Mechanical" in branch:
        return {
            "Year 1": "Engineering Mechanics",
            "Year 2": "Thermodynamics",
            "Year 3": "Robotics / CAD",
            "Year 4": "Industrial Internship"
        }

    return {
        "Year 1": "Foundation",
        "Year 2": "Core",
        "Year 3": "Specialization",
        "Year 4": "Industry Experience"
    }


# =====================================================
# 🤖 MAIN AGENT RESPONSE
# =====================================================

def agent_response(query, memory):
    query = query.lower()

    # 🔹 INTEREST DETECTION
    if "coding" in query:
        memory["interest"] = "coding"

    elif "ai" in query or "machine learning" in query:
        memory["interest"] = "ai"

    elif "machine" in query or "mechanical" in query:
        memory["interest"] = "mechanical"

    # 🔹 CAREER ANALYSIS
    if "branch" in query or "career" in query or "future" in query:

        best_branch, ranked, confidence = career_scoring_engine(query, memory)

        # Store scores for dashboard
        memory["branch_scores"] = {
            branch: min(100, score + 60)
            for branch, score in ranked if score > 0
        }

        roadmap = generate_roadmap(best_branch)
        intelligence = career_intelligence_engine(best_branch)
        skill_analysis = skill_gap_analysis(best_branch)

        # Dynamic Career Roles
        if "Computer Science" in best_branch:
            careers = [
                "Software Engineer",
                "Full Stack Developer",
                "Cloud Engineer",
                "Cybersecurity Analyst"
            ]

        elif "Artificial Intelligence" in best_branch:
            careers = [
                "Machine Learning Engineer",
                "AI Research Scientist",
                "Data Scientist",
                "Robotics Engineer"
            ]

        elif "Mechanical" in best_branch:
            careers = [
                "Automotive Engineer",
                "Robotics Engineer",
                "Manufacturing Engineer",
                "Aerospace Engineer"
            ]

        else:
            careers = [
                "Technical Consultant",
                "Project Engineer"
            ]

        # Generate PDF
        generate_career_report({
            "best_branch": best_branch,
            "ranking": memory["branch_scores"],
            "careers": careers,
            "roadmap": roadmap,
            "confidence": confidence
        })

        formatted_scores = "\n".join(
            [f"• {branch} → {score}%" for branch, score in memory["branch_scores"].items()]
        )

        formatted_roadmap = "\n".join(
            [f"{year}: {content}" for year, content in roadmap.items()]
        )

        formatted_careers = "\n".join(
            [f"• {career}" for career in careers]
        )

        return (
            "🧠 AI Career Intelligence Report\n\n"
            f"🏆 Best Fit Branch: {best_branch}\n\n"
            "📊 Suitability Ranking:\n"
            f"{formatted_scores}\n\n"
            f"{intelligence}\n\n"
            f"{skill_analysis}\n\n"
            "🚀 Future Career Roles:\n"
            f"{formatted_careers}\n\n"
            "🛣 4-Year Success Roadmap:\n"
            f"{formatted_roadmap}\n\n"
            f"📊 Confidence Score: {confidence}%"
        )

    # 🔹 FACILITIES
    elif "facilities" in query:
        facilities = get_facilities()
        formatted = "\n".join([f"• {fac}" for fac in facilities])
        return f"🏢 Campus Facilities:\n{formatted}\n\n📊 Confidence Score: 100%"

    # 🔹 DEPARTMENTS
    elif "departments" in query:
        departments = get_departments()
        formatted = "\n".join([f"• {dept}" for dept in departments])
        return f"🎓 Available Departments:\n{formatted}\n\n📊 Confidence Score: 100%"

    # 🔹 COLLEGE INFO
    elif "college name" in query:
        campus = get_campus_info()
        return f"🏫 College Name: {campus['college_name']}\n\n📊 Confidence Score: 100%"

    # 🔹 FALLBACK
    return (
        "🤖 I can help with:\n"
        "• Branch recommendations\n"
        "• Career prediction\n"
        "• Market intelligence analysis\n"
        "• Skill gap analysis\n"
        "• 4-Year roadmap planning\n"
        "• Facilities\n"
        "• Departments\n"
        "• College information\n\n"
        "📊 Confidence Score: 65%"
    )
