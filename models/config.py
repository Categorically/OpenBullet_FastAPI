from pydantic import BaseModel
from typing import Optional,List

class configIn(BaseModel):
    name: str
    config_text: str
    replacement_variables: str
class configOut(BaseModel):
    name:str
    status: str
    variables: List[dict] = []
    capture_variables: List[dict] = []
