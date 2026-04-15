def parse_job_description(text):
    job_skills = {
        "required": [],
        "optional": []
    }

    current_section = None

    for line in text.split("\n"):
        line = line.strip()

        if not line:
            continue

        if "REQUIRED SKILLS" in line.upper():
            current_section = "required"
            continue

        if "OPTIONAL SKILLS" in line.upper():
            current_section = "optional"
            continue

        if current_section in job_skills:
            job_skills[current_section].append(line.lower())

    return job_skills