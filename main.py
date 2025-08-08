from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello World"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
