from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.db import db, Database
from app.core.models import BaseModel

DATABASE_URL = "sqlite+aiosqlite:///./test.db"
db = Database(url=DATABASE_URL)


@asynccontextmanager
async def lifespan(_app: FastAPI):
    await db.connect()
    async with db.engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)
    yield
    await db.disconnect()


app = FastAPI(lifespan=lifespan)


@app.get("/health", tags=["System"])
async def health():
    ok = await db.ping()
    return {"status": "ok" if ok else "error"}
