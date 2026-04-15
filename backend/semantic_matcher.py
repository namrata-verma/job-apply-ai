from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model once (IMPORTANT)
model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_skill_similarity(resume_skills, job_skills, threshold=0.6):
    matched = []
    missing = []

    resume_embeddings = model.encode(resume_skills)
    job_embeddings = model.encode(job_skills)

    for i, job_skill in enumerate(job_skills):
        similarities = cosine_similarity(
            [job_embeddings[i]], resume_embeddings
        )[0]

        best_score = max(similarities)

        if best_score >= threshold:
            matched.append((job_skill, round(float(best_score), 2)))
        else:
            missing.append(job_skill)

    return matched, missing