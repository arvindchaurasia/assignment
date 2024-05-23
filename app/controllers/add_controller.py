from app.models.request_model import AddRequest
from app.models.response_model import AddResponse
from app.services.add_service import addition
from datetime import datetime

class AddController:
    @staticmethod
    def add(request: AddRequest) -> AddResponse:
        started_at = datetime.utcnow()
        response_list = addition(request.payload)
        completed_at = datetime.utcnow()

        return AddResponse(
            batchid=request.batchid,
            response=response_list,
            status="complete",
            started_at=started_at,
            completed_at=completed_at
        )

    