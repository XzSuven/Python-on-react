#Модели задачи (Task) для API-проекта «Менеджер задач».
#- Task     — модель для создания задачи (принимается от клиента).
#- TaskOut  — модель ответа (response_model), скрывающая служебное поле internal_note от клиента.
from pydantic import BaseModel, Field, field_validator

from models.category import Category


class Task(BaseModel):
    #Модель задачи, используемая при создании (POST) и хранении.

    title: str = Field(..., description="Название задачи", examples=["Сделать домашку"])
    description: str = Field(..., description="Описание задачи")
    is_completed: bool = Field(default=False, description="Признак выполнения задачи")
    category: Category = Field(..., description="Категория задачи")

    # Служебное поле — не должно попадать в ответ клиенту.
    # По умолчанию пустое; используется, например, для внутренних заметок.
    internal_note: str = Field(
        default="",
        description="Служебная заметка (только для внутреннего использования)",
    )

    @field_validator("title")
    @classmethod
    def title_must_be_long_enough(cls, value: str) -> str:
        #Кастомный валидатор
        if len(value.strip()) < 3:
            raise ValueError(
                "Название задачи должно содержать не менее 3 символов"
            )
        return value


class TaskOut(BaseModel):

    #Модель для ответа моему любимому(нет) клиенту.


    id: int = Field(..., description="Идентификатор задачи")
    title: str
    description: str
    is_completed: bool = False
    category: Category
