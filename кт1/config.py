"""
Конфигурация приложения.
Все настройки читаются из переменных окружения (.env),
никаких хардкод-значений в main.py быть не должно.
"""

import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()


class Settings:
    """Класс с настройками приложения, читаемыми из окружения."""

    # Адрес фронтенда, которому разрешён доступ через CORS
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "http://localhost:3000")

    # Метаданные приложения (используются в Swagger UI)
    APP_TITLE: str = os.getenv("APP_TITLE", "Task Manager API")
    APP_DESCRIPTION: str = os.getenv(
        "APP_DESCRIPTION",
        "API-проект «Менеджер задач»: маршруты, Pydantic-модели, "
        "response_model и CORS — основа для последующих разделов курса.",
    )
    APP_VERSION: str = os.getenv("APP_VERSION", "1.0.0")


settings = Settings()
