import re

# Skills that companies commonly expect
REQUIRED_SKILLS = [
    "python",
    "java",
    "c",
    "c++",
    "javascript",
    "react",
    "node",
    "express",
    "html",
    "css",
    "sql",
    "mysql",
    "mongodb",
    "flask",
    "django",
    "aws",
    "docker",
    "kubernetes",
    "git",
    "github",
    "firebase",
    "machine learning",
    "data science",
    "tensorflow",
    "opencv",
    "api",
    "rest"
]


def analyze_resume(text):

    text_lower = text.lower()

    # -----------------------------
    # Skill Detection
    # -----------------------------
    found_skills = []
    missing_skills = []

    for skill in REQUIRED_SKILLS:

        if skill in text_lower:
            found_skills.append(skill.title())
        else:
            missing_skills.append(skill.title())

    # -----------------------------
    # Education
    # -----------------------------
    education_keywords = [
        "b.tech",
        "btech",
        "m.tech",
        "mtech",
        "b.e",
        "be",
        "b.sc",
        "msc",
        "phd",
        "degree"
    ]

    education_found = False

    for edu in education_keywords:
        if edu in text_lower:
            education_found = True
            break

    # -----------------------------
    # Certifications
    # -----------------------------
    certification_keywords = [
        "aws",
        "nptel",
        "coursera",
        "udemy",
        "oracle",
        "google",
        "microsoft"
    ]

    certifications = []

    for cert in certification_keywords:
        if cert in text_lower:
            certifications.append(cert.title())

    # -----------------------------
    # Projects
    # -----------------------------
    project_keywords = [
        "project",
        "developed",
        "built",
        "implemented",
        "created"
    ]

    has_projects = False

    for word in project_keywords:
        if word in text_lower:
            has_projects = True
            break

    # -----------------------------
    # ATS Score
    # -----------------------------

    score = 0

    score += min(len(found_skills) * 3, 60)

    if education_found:
        score += 10

    if has_projects:
        score += 15

    if len(certifications) > 0:
        score += 15

    if score > 100:
        score = 100

    # -----------------------------
    # Suggestions
    # -----------------------------

    suggestions = []

    if len(found_skills) < 8:
        suggestions.append(
            "Add more technical skills related to your target job."
        )

    if not education_found:
        suggestions.append(
            "Mention your educational qualifications clearly."
        )

    if not has_projects:
        suggestions.append(
            "Include at least 2 projects with technologies used."
        )

    if len(certifications) == 0:
        suggestions.append(
            "Add certifications like AWS, NPTEL or Coursera."
        )

    if "github" not in text_lower:
        suggestions.append(
            "Include your GitHub profile."
        )

    if "linkedin" not in text_lower:
        suggestions.append(
            "Include your LinkedIn profile."
        )

    if score >= 85:
        suggestions.append(
            "Excellent Resume! Keep it updated regularly."
        )

    # -----------------------------
    # Return Analysis
    # -----------------------------

    return {

        "score": score,

        "skills": found_skills,

        "missing": missing_skills,

        "certifications": certifications,

        "education": education_found,

        "projects": has_projects,

        "suggestions": suggestions

    }