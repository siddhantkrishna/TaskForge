import argparse
from storage import load_tasks, save_tasks
from task import Task

def create_parser():
    parser = argparse.ArgumentParser(description="TaskForge CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", type=str, help="Task title")

    return parser, subparsers

def add_task(title):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    new_task = Task(task_id, title)
    tasks.append(new_task.to_dict())
    save_tasks(tasks)
    print(f"Task added: [{task_id}] {title}")
