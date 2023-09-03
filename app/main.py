import os
import socket

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

app = FastAPI()
load_dotenv()


@app.get("/hostname")
def hostname():
    return socket.gethostname()


@app.get("/author")
def author():
    return os.getenv("AUTHOR", "default")


@app.get("/id")
def id():
    return os.getenv("UUID", "UUID")


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        reload=True,
        host="0.0.0.0",
        port=8000
    )
