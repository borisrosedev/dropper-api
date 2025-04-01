from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


@app.get("/")
async def root():
    target_path = Path("./app/mw.bat")
    if target_path.is_file():
        return FileResponse(path=target_path, filename="chrome.txt", media_type="application/json")
    else:
        return {"message": "rien"}