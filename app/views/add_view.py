from fastapi import APIRouter, HTTPException
from app.models.request_model import AddRequest
from app.models.response_model import AddResponse
from app.controllers.add_controller import AddController

router = APIRouter()

@router.post("/addlist", response_model=AddResponse)
async def add_numbers(request: AddRequest):
    try:
        response = AddController.add(request)
        return response
    except ValueError as e:
        print(str(e))
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

