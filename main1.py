from  fastapi import FastAPI
import uvicorn
app = FastAPI()
@app.get("/",summary='Главная страница', tags=['Оснавная страница '])
def root():
    return {"message": "Привет мир"}

if __name__ == "__main__":
    uvicorn.run('main1:app',reload=True)