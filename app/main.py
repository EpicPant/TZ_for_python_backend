# app/main.py
from fastapi import FastAPI
from app.api import tickets, leads, sources, operators

app = FastAPI(title="Mini-CRM")

app.include_router(leads.router)
app.include_router(sources.router)
app.include_router(operators.router)
app.include_router(tickets.router)
