from models import ApplicationStatus

def execute_application(application):
    """
    Simulates job application execution.
    Real automation will be added later.
    """

    if application["status"] != ApplicationStatus.APPROVED:
        return {
            "error": "Job must be approved before applying"
        }

    # Simulate application process
    application["status"] = ApplicationStatus.APPLIED

    return {
        "job_id": application["job_id"],
        "status": application["status"],
        "message": "Application submitted successfully (simulated)"
    }