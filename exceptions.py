class TaskNotFoundError(Exception):
    """Raised when a task with a given ID is not found."""
    pass

class InvalidTaskError(Exception):
    """Raised when task data is invalid."""
    pass
