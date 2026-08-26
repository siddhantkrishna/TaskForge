import argparse
from storage import load_tasks, save_tasks, mark_done
from task import Task

def create_parser():
    parser = argparse.ArgumentParser(description="TaskForge CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", type=str, help="Task title")

    subparsers.add_parser("list", help="List all tasks")

    done_parser = subparsers.add_parser("done", help="Mark a task as completed")
    done_parser.add_argument("id", type=int, help="Task ID")

    return parser

def add_task(title):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    new_task = Task(task_id, title)
    tasks.append(new_task.to_dict())
    save_tasks(tasks)
    print(f"Task added: [{task_id}] {title}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for t in tasks:
        status = "?" if t["completed"] else " "
        print(f"[{t['id']}] [{status}] {t['title']}")

def complete_task(task_id):
    if mark_done(task_id):
        print(f"Task [{task_id}] marked as completed.")
    else:
        print(f"Task [{task_id}] not found.")
