from application_executor import execute_application
from application_queue import application_queue
from cover_letter.generator import generate_cover_letter
from application_queue import add_to_queue, update_status, get_queue
from models import ApplicationStatus
from fastapi import APIRouter
from job_ranker import rank_jobs
from resume_parser.parser import parse_resume, clean_skills
from job_parser.parser import parse_job_description
from matcher import (
    calculate_weighted_match_score,
    calculate_final_match_score
)
from semantic_matcher import semantic_skill_similarity

router = APIRouter()

@router.post("/match")
def match_resume_to_job(payload: dict):
    resume_text = payload.get("resume_text", "")
    job_text = payload.get("job_text", "")

    parsed_resume = parse_resume(resume_text)
    resume_skills = clean_skills(parsed_resume["skills"])

    job_data = parse_job_description(job_text)

    exact = calculate_weighted_match_score(resume_skills, job_data)

    semantic_matches, semantic_missing = semantic_skill_similarity(
        resume_skills,
        exact["missing_required"]
    )

    final_score = calculate_final_match_score(
        exact["score"],
        semantic_matches,
        semantic_missing
    )

    return {
        "final_score": final_score,
        "exact_score": exact["score"],
        "matched_required": exact["matched_required"],
        "matched_optional": exact["matched_optional"],
        "semantic_matches": semantic_matches,
        "still_missing": semantic_missing
    }
    
    
    from job_ranker import rank_jobs

@router.post("/recommend-jobs")
def recommend_jobs(payload: dict):
    resume_text = payload.get("resume_text", "")
    jobs_payload = payload.get("jobs", {})
    top_n = payload.get("top_n", 5)

    parsed_resume = parse_resume(resume_text)
    resume_skills = clean_skills(parsed_resume["skills"])

    jobs = {}
    for job_id, job_text in jobs_payload.items():
        jobs[job_id] = parse_job_description(job_text)

    ranked_jobs = rank_jobs(resume_skills, jobs)

    return ranked_jobs[:top_n]

@router.post("/queue-job")
def queue_job(payload: dict):
    job_id = payload.get("job_id")
    job_data = payload.get("job_data")

    if not job_id or not job_data:
        return {"error": "job_id and job_data required"}

    return add_to_queue(job_id, job_data)


@router.post("/approve-job")
def approve_job(payload: dict):
    job_id = payload.get("job_id")
    return update_status(job_id, ApplicationStatus.APPROVED)


@router.post("/reject-job")
def reject_job(payload: dict):
    job_id = payload.get("job_id")
    return update_status(job_id, ApplicationStatus.REJECTED)


@router.get("/application-queue")
def view_queue():
    return get_queue()


@router.post("/generate-cover-letter")
def create_cover_letter(payload: dict):
    resume_data = payload.get("resume_data", {})
    job_data = payload.get("job_data", {})
    language = payload.get("language", "en")
    tone = payload.get("tone", "professional")

    return generate_cover_letter(
        resume_data=resume_data,
        job_data=job_data,
        language=language,
        tone=tone
    )
    
@router.post("/apply-job")
def apply_job(payload: dict):
    job_id = payload.get("job_id")

    if job_id not in application_queue:
        return {"error": "Job not found in queue"}

    application = application_queue[job_id]
    return execute_application(application)