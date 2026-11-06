from fastapi import FastAPI
from app.Presentation.Routers import UserRouter

app = FastAPI()

app.include_router(UserRouter.router)

@app.get("/")
def greeting():
    return { "message": "Welcome to the Task Management API!"}