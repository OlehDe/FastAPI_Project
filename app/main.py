from fastapi import FastAPI
from contextlib import asynccontextmanager

# Імпортуємо базу даних і базову модель відповідно до твоєї структури
from app.core.setting.db import Database
from app.core.models.base import BaseModel

DATABASE_URL = "sqlite+aiosqlite:///./test.db"
db = Database(url=DATABASE_URL)


@asynccontextmanager
async def lifespan(_fastapi_app: FastAPI):
    await db.connect()
    async with db.engine.begin() as connection:
        await connection.run_sync(BaseModel.metadata.create_all)
    yield
    await db.disconnect()


app = FastAPI(lifespan=lifespan)


@app.get(path="/health", tags=["System"])
async def health():
    ok = await db.ping()
    return {"status": "ok" if ok else "error"}
