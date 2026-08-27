def format_status(completed):
    return "x" if completed else " "

def format_task_line(task_id, title, completed, priority="medium"):
    status = format_status(completed)
    return f"[{task_id}] [{status}] [{priority.upper()}] {title}"
