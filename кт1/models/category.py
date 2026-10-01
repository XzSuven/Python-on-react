"""
Вложенная модель Category, используется внутри модели Task.
"""

from pydantic import BaseModel, Field


class Category(BaseModel):
    """Категория задачи."""

    name: str = Field(..., description="Название категории", examples=["Работа"])
    color: str = Field(..., description="Цвет категории (например, HEX)", examples=["#FF5733"])
