from fastapi import FastAPI, APIRouter
from api.routers import tasks

app = FastAPI()

root_router = APIRouter()


@root_router.get("/")
async def read_root():
    return {"message": "Welcome to the Task API. Go to /tasks/ to view tasks."}


app.include_router(root_router)
app.include_router(tasks.router)


@app.on_event("startup")
async def startup_event():
    print("Server is starting. API documentation is available at http://127.0.0.1:8000/docs")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
