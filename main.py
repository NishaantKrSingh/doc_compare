from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, HTMLResponse
import shutil
from pathlib import Path

from modules.pdfConvert import convert
from modules.pdfComp import compare

app = FastAPI()

# Paths for HTML file and upload directory
html_path = Path("static/index.html")
upload_directory = Path("uploads")
upload_directory.mkdir(exist_ok=True)  # Create the directory if it doesn't exist

# Endpoint to serve the HTML file
@app.get("/", response_class=HTMLResponse)
async def main():
    return FileResponse(html_path)

# Endpoint to handle uploading two files
@app.post("/uploadfiles/")
async def upload_files(file1: UploadFile = File(...), file2: UploadFile = File(...)):
    # Save file1
    file1_path = upload_directory / file1.filename
    with file1_path.open("wb") as buffer:
        shutil.copyfileobj(file1.file, buffer)

    # Save file2
    file2_path = upload_directory / file2.filename
    with file2_path.open("wb") as buffer:
        shutil.copyfileobj(file2.file, buffer)

    data = convert(file1_path, file2_path)
    percentage_diff = compare(data1= data[0], data2=data[1])

    return {
        "message": "Files uploaded successfully!",
        "file1_name": file1.filename,
        "file2_name": file2.filename,
        "data" : data,
        "difference" : f"{percentage_diff:.2f}%" 
    }
