import shutil
from unicodedata import name
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse


router = APIRouter(
    prefix="/file",
    tags=['file'] 
)


#Upload file in simple way as bytes
@router.post('/file')
def get_file(file: bytes=File(...)):
    content = file.decode('utf-8')
    lines = content.split('\n')
    return {'lines': lines}


#upload file using UploadFile for more advanced use cases
@router.post('/uploadfile')
def upload_file(uploaded_file: UploadFile=File(...)):
    path = f"files/{uploaded_file.filename}"
    with open(path, "wb") as f:
        shutil.copyfileobj(uploaded_file.file, f)
    return {'filename': uploaded_file.filename,
            'content_type': uploaded_file.content_type
    }

#To Download the file it will be viewed in the swagger ui Eg.Crab_Nebula.jpg
@router.get('/downloadfile/{name}',response_class=FileResponse)
def get_file(name: str):
    path = f"files/{name}"
    return path