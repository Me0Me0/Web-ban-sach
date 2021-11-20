from configs.db import getDB
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
app = FastAPI()

# get DB
db = getDB()

# static files
app.mount("/public", StaticFiles(directory="public"))

@app.get("/")
def main():
	return {"data": db}
