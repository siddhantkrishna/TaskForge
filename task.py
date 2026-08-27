from datetime import datetime

class Task:
    def __init__(self, task_id, title, priority="medium", completed=False, created_at=None):
        self.task_id = task_id
        self.title = title
        self.priority = priority
        self.completed = completed
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.task_id,
            "title": self.title,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at
        }
