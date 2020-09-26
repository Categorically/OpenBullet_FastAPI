from pydantic import BaseModel,Field
from typing import Optional,List,Dict


class CVar(BaseModel):
    name : str = Field(description="The name of the variable", min_length=1)
    value : str = Field(description="The value of the variable", min_length=1)
    IsCapture : bool = Field(False,description="If the variable is capture")
    hidden : bool = Field(False, description="Hidden variables will not be outputted")

class configIn(BaseModel):
    name: str = Field(description="Name of the config",min_length=1)
    text: str = Field(description="Base64 encoded config text",min_length=1)
    replacement_variables: List[CVar] = Field([], description="Create new variables to be used for replacements")

class configOut(BaseModel):
    name:str
    status: str
    variables: List[CVar]
    capture_variables: List[CVar]
