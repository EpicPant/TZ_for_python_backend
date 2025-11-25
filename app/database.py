from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from app.models.base import Base

DATABASE_URL = "sqlite+aiosqlite:///./crm.db"

engine = create_async_engine(DATABASE_URL, echo=False)

# ✅ Правильно: async_sessionmaker
async_session = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


# Dependency для FastAPI
async def get_db():
    async with async_session() as session:
        yield session
