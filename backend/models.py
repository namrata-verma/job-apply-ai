from enum import Enum

class ApplicationStatus(str, Enum):
    PENDING_APPROVAL = "pending_approval"
    APPROVED = "approved"
    REJECTED = "rejected"
    APPLIED = "applied"
