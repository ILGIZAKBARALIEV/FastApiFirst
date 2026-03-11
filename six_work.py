from fastapi import FastAPI,APIRouter,File,UploadFile

app = FastAPI()
six_work_router = APIRouter(
    prefix='/Working with Files in FastAPI — Uploading and Smart Downloading',tags=['Working with Files in FastAPI'] )

@six_work_router.post("/files")
async  def upload_file(uploaded_file: UploadFile):
    file1 = uploaded_file.file
    filename = uploaded_file.filename
    with (open(f'1_{filename}',"wb") as f):
        f.write(file1.read())

@six_work_router.post("/multi_files")
async def upload_files(uploaded_files: list[UploadFile]):
    for uploaded_file1 in uploaded_files:
        file = uploaded_file1.file
        filename = uploaded_files.filename
        with open(filename, "wb") as f:
            f.write(file.read())
    return {"ok": True}




