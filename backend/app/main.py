

from app.model import create_admin_user
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routers import employees, users
from app.settings import ALLOW_ORIGINS



def create_tables():
    Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sprout Exam",
    docs_url="/docs",
)

@app.on_event("startup")
def on_startup():
    create_tables()
    create_admin_user()



app.add_middleware(
    CORSMiddleware,
    allow_origins=[ALLOW_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employees.router, prefix="/employees", tags=["employees"])
app.include_router(users.router, prefix="/users", tags=["users"])
