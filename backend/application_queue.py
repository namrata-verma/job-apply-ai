from models import ApplicationStatus

# Temporary in-memory store (will become DB later)
application_queue = {}

def add_to_queue(job_id, job_data):
    application_queue[job_id] = {
        "job_id": job_id,
        "job_data": job_data,
        "status": ApplicationStatus.PENDING_APPROVAL
    }
    return application_queue[job_id]

def update_status(job_id, status):
    if job_id not in application_queue:
        return None

    application_queue[job_id]["status"] = status
    return application_queue[job_id]

def get_queue():
    return list(application_queue.values())