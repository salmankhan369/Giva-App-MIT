from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Giva-App-MIT")

@app.get("/")
def home():
    return {"message": "Welcome to Giva-App Production v2.0", "status": "Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
