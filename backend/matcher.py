def calculate_weighted_match_score(resume_skills, job_skills):
    required = set(job_skills["required"])
    optional = set(job_skills["optional"])
    resume = set(resume_skills)

    matched_required = resume & required
    matched_optional = resume & optional

    # Weights
    required_weight = 0.7
    optional_weight = 0.3

    required_score = (
        len(matched_required) / len(required) if required else 0
    )

    optional_score = (
        len(matched_optional) / len(optional) if optional else 0
    )

    final_score = int(
        (required_score * required_weight + optional_score * optional_weight) * 100
    )

    return {
        "score": final_score,
        "matched_required": list(matched_required),
        "matched_optional": list(matched_optional),
        "missing_required": list(required - resume)
    }
    
def calculate_final_match_score(
    exact_score,
    semantic_matches,
    missing_required
):
    """
    exact_score: int (0–100)
    semantic_matches: list of (skill, similarity)
    missing_required: list of skills
    """

    # Average semantic confidence
    if semantic_matches:
        semantic_score = sum(score for _, score in semantic_matches) / len(semantic_matches)
    else:
        semantic_score = 0

    # Penalize missing required skills
    penalty = len(missing_required) * 10  # strong penalty per missing skill

    # Final blended score
    final_score = int(
        (exact_score * 0.7) +
        (semantic_score * 100 * 0.3) -
        penalty
    )

    # Clamp between 0 and 100
    final_score = max(0, min(100, final_score))

    return final_score