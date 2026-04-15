ENGLISH_PROMPT = """
You are an expert career assistant.

Write a professional, concise cover letter for the following job.

Candidate skills:
{skills}

Candidate experience:
{experience}

Job title:
{job_title}

Company:
{company}

Job requirements:
{job_requirements}

Tone: confident, professional, human.
Length: 3–4 short paragraphs.
Do not exaggerate. Do not invent experience.
"""

GERMAN_PROMPT = """
Du bist ein professioneller Karriereberater.

Schreibe ein formelles Anschreiben für folgende Stelle.

Fähigkeiten des Bewerbers:
{skills}

Berufserfahrung:
{experience}

Stellenbezeichnung:
{job_title}

Unternehmen:
{company}

Anforderungen der Stelle:
{job_requirements}

Ton: professionell, höflich, sachlich.
Länge: 3–4 kurze Absätze.
Keine Übertreibungen, keine erfundenen Erfahrungen.
"""