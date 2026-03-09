from fastapi import FastAPI
app = FastAPI()
@app.get("/hello")
def hello():
    return {"message": "Hello World"}
@app.get("/print_hi")
def print_hi():





if __name__ == '__main__':
    print_hi('PyCharm')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
