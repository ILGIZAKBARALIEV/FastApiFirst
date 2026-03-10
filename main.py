from  fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from seccand import router as seccand_router
from three import router_three as third_router_three

app = FastAPI()
app.include_router(seccand_router)
app.include_router(third_router_three)
@app.get("/",summary='Главная страница', tags=['Оснавная страница '])
def root():
    return {"message": "Привет мир"}
books = [
    {
        "id":1,
        "title":"My first book",
        "author":"Ilgiz",
    },
    {
        "id":2,
        "title":"My second book",
        "author":"Ilgiz",
    }
]
@app.get("/Книги",
         tags=["Книги"],
         summary='Получить все книги')
def read_root():
    return books

@app.get("/книга_/{id}",
         tags=["Книги"],
         summary="Получить конкретную  книжку")
def read_book(boook_id: int):
    for book in books:
        if book["id"] == boook_id:
            return book
        raise HTTPException(status_code=404, detail="Book not found")


class New_Book(BaseModel):
    id: int
    title: str
    author: str
@app.post("/Китептерди_Жазу")
def create_book(new_book: New_Book):
    books.append({
        "id": len(books)+1,
        "title": new_book.title,
        "author": new_book.author,
    })
    return {'success': True, "massage":"китеп кошулду!"}




if __name__ == "__main__":
    uvicorn.run('main:app',reload=True)