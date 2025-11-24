from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import auth, loads, history, notifications

app = FastAPI(title="ASR Driver API", version="1.0.0")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(loads.router)
app.include_router(history.router)
app.include_router(notifications.router)


@app.get("/")
def read_root():
    return {"message": "ASR Driver API is running"}

