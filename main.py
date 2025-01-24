from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/hello")
def say_hello():
    return {"message": "Hello, from the hello route!"}

@app.get("/test1")
def test1():
    return {"message": "This is test1!"}

@app.get("/test2")
def test2():
    return {"message": "This is test2!"}
