from fastapi import FastAPI, Request, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, adjust as needed
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods, adjust as needed
    allow_headers=["*"],  # Allows all headers, adjust as needed
)

with open("q-vercel-python.json", "r") as file:
    data = json.load(file)



@app.get("/")
def index():
    return {
        "message": "Welcome to the FastAPI application!"
        }

@app.get("/api")
def get_marks(request: Request):

    output = []
    names = request.query_params.getlist("name")

    name_to_marks = {entry["name"]: entry["marks"] for entry in data}

    output = [name_to_marks.get(name, None) for name in names]

    return output