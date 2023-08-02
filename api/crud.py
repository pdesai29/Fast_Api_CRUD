from typing import Dict, List, Optional
from api.models import Task

database = {
    1: Task(id=1, title="Task 1", description="Description for Task 1", completed=False),
    2: Task(id=2, title="Task 2", description="Description for Task 2", completed=True),
}


def get_all_tasks() -> List[Task]:
    return list(database.values())


def get_task_by_id(task_id: int) -> Optional[Task]:
    return database.get(task_id)


def create_task(task: Task) -> Task:
    task_id = max(database.keys()) + 1
    task.id = task_id
    database[task_id] = task
    return task


def update_task(task_id: int, task: Task) -> Optional[Task]:
    if task_id not in database:
        return None
    database[task_id] = task
    return task


def delete_task(task_id: int) -> Optional[Task]:
    return database.pop(task_id, None)
