from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel, Field
from typing import Optional


class ToDoBase(BaseModel):
    task: str = Field(description="the description of the task")


class ToDo(ToDoBase):
    is_completed: bool = Field(description="has the task been completed ?")
    id: int | None = Field(default=None,
                           description="the unique ID of the task")


class ToDoReturn(ToDoBase):
    pass


app = FastAPI(title="simple API")

todos = []


@app.get("/", status_code=status.HTTP_200_OK, tags=["sanity check"])
async def root():
    return {"message": "hello world"}


@app.post("/todos",
          status_code=status.HTTP_201_CREATED,
          tags=["to do version 2"],
          response_model=ToDoReturn)
async def create_todos(todo: ToDo):
    todo.id = len(todos) + 1
    todos.append(todo)
    return todo


@app.get("/todos",
         status_code=status.HTTP_200_OK,
         tags=["to do version 2"])
async def list_todos(completed: Optional[bool] = None):
    if completed is None:
        print(f"completed was none = {completed}")
        print(todos)
        return todos
    else:
        res = [todo for todo in todos if todo.is_completed == completed]
        print(f"after removing the todo for completed = {completed}")
        print(res)
    return res


@app.get("/todos/{id}",
         status_code=status.HTTP_200_OK,
         tags=["to do version 2"])
async def list_todos(id: int):
    for todo in todos:
        if todo.id == id:
            return todo
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"item {id} no found")


@app.put("/todos/{id}",
         status_code=status.HTTP_200_OK,
         tags=["to do version 2"])
async def update_todos(id: int, new_todo: ToDo):
    for index, todo in enumerate(todos):
        if todo.id == id:
            todos[index] = new_todo
            todos[index].id = id
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"item {id} no found")


@app.delete("/todos/{id}",
            status_code=status.HTTP_200_OK,
            tags=["to do version 2"])
async def update_todos(id: int):
    for index, todo in enumerate(todos):
        if todo.id == id:
            del todos[index]
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"item {id} no found")
