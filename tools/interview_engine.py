# =====================================================
# 🎤 AI INTERVIEW SIMULATOR ENGINE
# =====================================================

def generate_interview_questions(branch):

    if "Computer Science" in branch:
        return [
            "Explain how a HashMap works internally.",
            "What is the difference between REST and GraphQL?",
            "How does multithreading work in Python?",
            "Explain time complexity of quicksort."
        ]

    if "Artificial Intelligence" in branch:
        return [
            "What is overfitting in Machine Learning?",
            "Explain difference between supervised and unsupervised learning.",
            "What is backpropagation?",
            "How does a neural network learn?"
        ]

    if "Mechanical" in branch:
        return [
            "Explain thermodynamics laws.",
            "What is the difference between CNC and conventional machining?",
            "Define stress-strain relationship.",
            "What is robotics automation?"
        ]

    return [
        "Tell me about yourself.",
        "What are your strengths?",
        "Why should we hire you?"
    ]


def evaluate_answer(answer):

    score = 0

    if len(answer) > 20:
        score += 30

    if any(keyword in answer.lower() for keyword in ["example", "because", "therefore"]):
        score += 30

    if len(answer.split()) > 30:
        score += 40

    final_score = min(100, score)

    if final_score > 80:
        feedback = "Excellent structured answer. Very confident response!"
    elif final_score > 60:
        feedback = "Good answer, but you can add more technical depth."
    else:
        feedback = "Try explaining concepts clearly with examples."

    return final_score, feedback
