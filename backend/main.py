from fastapi import FastAPI
from routes import task_routes
from models import task_models 
from  database import engine, Base

Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(task_routes.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Task API"} 