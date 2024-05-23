from pydantic import BaseModel
from typing import List

class AddRequest(BaseModel):
    batchid: str
    payload: List[List[int]]

