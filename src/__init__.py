from fastapi import FastAPI
from src.blog.routes import router

app = FastAPI(title="Blog API")


app.include_router(router)
