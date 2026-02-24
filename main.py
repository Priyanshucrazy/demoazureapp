from fastapi import FastAPI

app = FastAPI(title="FastAPI Web App")

@app.get("/")
def root():
    return {"message": "FastAPI Web App is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}