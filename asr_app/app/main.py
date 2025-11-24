from fastapi import FastAPI

from .routers import auth, history, loads, notifications

app = FastAPI(title="ASR Driver API", version="1.0.0")

app.include_router(auth.router)
app.include_router(loads.router)
app.include_router(history.router)
app.include_router(notifications.router)


@app.get("/")
def read_root():
    return {"status": "ok"}
