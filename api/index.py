from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def index():
    return {
        "message": "Welcome to the FastAPI application!"
        }