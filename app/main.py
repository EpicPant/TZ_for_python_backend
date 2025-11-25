# app/main.py
from fastapi import FastAPI
from app.api import tickets, leads, sources, operators

app = FastAPI(title="Mini-CRM")

# ❌ Убираем автоматическое создание таблиц
# @app.on_event("startup")
# async def startup():
#     await create_tables()

app.include_router(leads.router)
app.include_router(sources.router)
app.include_router(operators.router)
app.include_router(tickets.router)
