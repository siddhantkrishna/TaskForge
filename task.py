class Task:
    def __init__(self, task_id, title, priority="medium", completed=False):
        self.task_id = task_id
        self.title = title
        self.priority = priority
        self.completed = completed

    def to_dict(self):
        return {
            "id": self.task_id,
            "title": self.title,
            "priority": self.priority,
            "completed": self.completed
        }
