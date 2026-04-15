from cover_letter.prompts import ENGLISH_PROMPT, GERMAN_PROMPT
from llm.client import generate_text

def generate_cover_letter(
    resume_data,
    job_data,
    language="en",
    tone="professional"
):
    skills = ", ".join(resume_data.get("skills", []))
    experience = " ".join(resume_data.get("experience", []))

    prompt_base = ENGLISH_PROMPT if language == "en" else GERMAN_PROMPT

    prompt = prompt_base + f"\n\nTone preference: {tone}"

    filled_prompt = prompt.format(
        skills=skills,
        experience=experience,
        job_title=job_data.get("title", ""),
        company=job_data.get("company", ""),
        job_requirements=", ".join(job_data.get("requirements", []))
    )

    letter_text = generate_text(filled_prompt)

    return {
        "language": language,
        "tone": tone,
        "status": "draft_generated",
        "cover_letter": letter_text
    }