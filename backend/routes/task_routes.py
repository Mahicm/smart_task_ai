from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.task_model import Task
from schemas.task_schema import TaskCreate, TaskUpdate, TaskResponse
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
@router.post("/", response_model=TaskResponse)
async def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(tittle=task.title, description=task.description, completed=task.completed)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

  
@router.get("/")
async def read_tasks(): 
    return {"message": "List of tasks"} 