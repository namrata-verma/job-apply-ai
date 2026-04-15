from matcher import calculate_weighted_match_score, calculate_final_match_score
from semantic_matcher import semantic_skill_similarity

def rank_jobs(resume_skills, jobs):
    ranked_jobs = []

    for job_id, job_data in jobs.items():
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

        ranked_jobs.append({
            "job_id": job_id,
            "final_score": final_score,
            "exact_score": exact["score"],
            "matched_required": exact["matched_required"],
            "missing_required": semantic_missing
        })

    return sorted(
        ranked_jobs,
        key=lambda x: x["final_score"],
        reverse=True
    )