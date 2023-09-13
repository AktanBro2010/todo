from database import Base, engine, SessionLocal
from fastapi import FastAPI, Depends, status, HTTPException
import schemas, models
from sqlalchemy.orm import Session


Base.metadata.create_all(engine)

app = FastAPI()


@app.get('/todo')
def root():
    return 'ToDoooooooo'


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@app.post('/task',response_model=schemas.ToDo, status_code=status.HTTP_201_CREATED)
def create_task(todo: schemas.CreateToDO, session: Session = Depends(get_session)):
    tododb = models.ToDo(task = todo.task)
    session.add(tododb)
    session.commit()
    return tododb


# '''uvicorn main:app --reload'''


@app.get('/task/{id}')
def read_todo(id: int, session: Session = Depends(get_session)):
    todo = session.query(models.ToDo).get(id)
    if not todo:
        raise HTTPException(status_code=404, detail=f'todo with id {id} not found')
    return todo


@app.get('/tasks')
def read_all_todos(session: Session = Depends(get_session)):
    todos = session.query(models.ToDo).all()
    return todos

@app.put('/task/{id}')
def update_todo(id: int, task: str, session: Session = Depends(get_session)):
    todo = session.query(models.ToDo).get(id)

    if todo:
        raise HTTPException(
            status_code=404,
            detail=f'todo item with id {id} not found'
        )
    todo.task = task
    session.commit()
    return todo


@app.delete('/task/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(id: int, task: str, session: Session = Depends(get_session)):
    todo = session.query(models.ToDo).get(id)

    if todo:
        raise HTTPException(
            status_code=404,
            detail=f'todo item with id {id} not found'
        )
    session.delete(todo)
    session.commit()
    return 'todo with id {id} deleted'