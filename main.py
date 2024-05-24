from fastapi import FastAPI
import uvicorn
from app.views import add_view

app = FastAPI()

app.include_router(add_view.router)

if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8000)

