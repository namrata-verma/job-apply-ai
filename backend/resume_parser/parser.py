def parse_resume(text):
    sections = {
        "skills": [],
        "experience": [],
        "education": []
    }

    current_section = None

    for line in text.split("\n"):
        line = line.strip()

        if not line:
            continue

        if "SKILLS" in line.upper():
            current_section = "skills"
            continue
        elif "EXPERIENCE" in line.upper():
            current_section = "experience"
            continue
        elif "EDUCATION" in line.upper():
            current_section = "education"
            continue

        if current_section:
            sections[current_section].append(line)

    return sections


def clean_skills(skills_lines):
    skills = []

    for line in skills_lines:
        # Split by comma
        items = line.split(",")

        for item in items:
            cleaned = item.strip().lower()
            if cleaned:
                skills.append(cleaned)

    # Remove duplicates
    return list(set(skills))