from typing import Annotated
from fastapi import FastAPI, Path
from pydantic import EmailStr, BaseModel

import uvicorn

from items_views import router as items_router

app = FastAPI()
app.include_router(items_router)


class CreateUser(BaseModel):
    email: EmailStr

@app.get("/")
def hello_index():
    return {"message": "Hello World"}

@app.get("/hello/")
def hello(name: str = "World"):
    name = name.strip().title()
    return {"message": f"Hello {name}"}


@app.post("/users/")
def create_user(user: CreateUser):
    return {
        "message": "User created successfully",
        "email": user.email,
    }


@app.post("/calc/add/")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b
    }

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)