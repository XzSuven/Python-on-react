from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings
from routers import tasks

import uvicorn

# Метаданные приложения читаются из config.py (никаких хардкод-значений здесь).
app = FastAPI(
    title=settings.APP_TITLE,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
)

# CORS: разрешённый origin берётся из .env через config.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем роутер задач
app.include_router(tasks.router)


@app.get("/", tags=["root"], summary="Проверка работоспособности API")
def root():
    return {"message": "Task Manager API работает. Документация на /docs"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)