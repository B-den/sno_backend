import uvicorn
import aiofiles
from fastapi import FastAPI, Body, Query, UploadFile, File
from sqlalchemy import create_engine
from db.session import engine
from db.session import SessionLocal
from db.base import Base
from db.models.person import Person
from db.models.password import Password
from db.funcs import *
from audio.process import process


app = FastAPI()

@app.post('/auth')
async def auth(data=Body(), type: str = Query(default="old")):
    email = data["email"]
    password = data["password"]
    if type == "old":
        veri = await get_user(email)
        if veri == None:return "Invalid email"
        if veri.code == password:return True
        return False
    if type == "new":
        return await new_user(data)

async def save_file(in_file: UploadFile, out_file_path: str):
    async with aiofiles.open(out_file_path, 'wb') as out_file:
        while content := await in_file.read(1024):  # async read chunk
            await out_file.write(content)  # async write chunk

@app.post('/upload_file')
async def process_file(file: UploadFile):
    path = 'sample.' + file.filename.split('.')[-1]
    await save_file(file, path)
    await file.close()
    return await process(path)

#drop_tables()
#create_tables()
#d = Person(name="d", nickname='c', email='d@c', is_active=False)
#c = Password(code='dfhje', person_id=1)
#session.add_all([c])
#session.commit()

#if __name__ == "__main__":
#   uvicorn.run(app)        # or cmd: uvicorn main:app --reload