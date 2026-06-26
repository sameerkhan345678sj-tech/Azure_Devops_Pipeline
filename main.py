from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Azure Devops + Docker + Kubernetes"}

@app.get("/health")
def health():
    return {"status": "ok"}