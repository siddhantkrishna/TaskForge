class Task:
    def __init__(self, task_id, title, completed=False):
        self.task_id = task_id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {
            "id": self.task_id,
            "title": self.title,
            "completed": self.completed
        }
