#Роутер задач: /tasks

#Содержит минимум 3 маршрута:
#- GET  /tasks/            — список задач
#- POST /tasks/             — создание задачи
#- GET  /tasks/{task_id}    — получение задачи по ID (response_model=TaskOut)

from fastapi import APIRouter, HTTPException, status

from models.task import Task, TaskOut

router = APIRouter(prefix="/tasks", tags=["tasks"])

# Делаем вид будто есть бд
tasks_db: dict[int, Task] = {}
next_id: int = 1


@router.get("/", response_model=list[TaskOut], summary="Получить список всех задач")
def get_tasks() -> list[TaskOut]:
    #Верну список задач
    return [
        TaskOut(id=task_id, **task.model_dump(exclude={"internal_note"}))
        for task_id, task in tasks_db.items()
    ]


@router.post(
    "/",
    response_model=TaskOut,
    status_code=status.HTTP_201_CREATED,
    summary="Создать новую задачу",
)
def create_task(task: Task) -> TaskOut:
    """Создаёт новую задачу и возвращает её без служебных полей."""
    global next_id
    task_id = next_id
    tasks_db[task_id] = task
    next_id += 1
    return TaskOut(id=task_id, **task.model_dump(exclude={"internal_note"}))


@router.get(
    "/{task_id}",
    response_model=TaskOut,
    summary="Получить задачу по ID",
)
def get_task(task_id: int) -> TaskOut:
    """Возвращает задачу по её идентификатору. Скрывает internal_note благодаря response_model."""
    task = tasks_db.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return TaskOut(id=task_id, **task.model_dump(exclude={"internal_note"}))
