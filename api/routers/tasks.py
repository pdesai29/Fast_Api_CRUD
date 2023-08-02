from fastapi import APIRouter, HTTPException
from typing import List, Optional
from api.models import Task
from api.crud import (
    get_all_tasks,
    get_task_by_id,
    create_task,
    update_task,
    delete_task,
)

router = APIRouter()


@router.get("/tasks/", response_model=List[Task])
async def read_all_tasks():
    """Get all tasks"""
    return get_all_tasks()


@router.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: int):
    """Get a specific task by ID"""
    task = get_task_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.post("/tasks/", response_model=Task, status_code=201)
async def create_new_task(task: Task):
    """Create a new task"""
    return create_task(task)


@router.put("/tasks/{task_id}", response_model=Task)
async def update_existing_task(task_id: int, task: Task):
    """Update an existing task by ID"""
    updated_task = update_task(task_id, task)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task


@router.delete("/tasks/{task_id}", response_model=Task)
async def delete_existing_task(task_id: int):
    """Delete an existing task by ID"""
    deleted_task = delete_task(task_id)
    if deleted_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return deleted_task
