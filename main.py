
from OpenBullet2Python.TestConfig import TestConfig
from OpenBullet2Python.Models.BotData import BotData
from OpenBullet2Python.Models.CVar import CVar
from fastapi import FastAPI,HTTPException,Request
from base64 import b64decode
from models.config import configIn,configOut
from fastapi.responses import JSONResponse
app = FastAPI()



class config_exception(Exception):
    def __init__(self,message:str):
        self.message = message
@app.exception_handler(config_exception)
async def unicorn_exception_handler(request: Request, exc: config_exception):
    return JSONResponse(
        status_code=400,
        content={"message": exc.message},
    )
@app.post("/")
async def root():
    return {"message": "Hello World"}

@app.post("/api/import/",response_model=configOut)
async def test_config(config: configIn):
    
    # Decode the base64
    try:
        config.text = b64decode(config.text).decode('utf-8')
    except:
        raise config_exception(message="Error decoding b64")

    # Data contains the list of variable and the bot status
    data = BotData()

    # Add variables to to the list for repalcement
    for variable in config.replacement_variables:
        data.Variables.Set(CVar(variable.name,variable.value,variable.IsCapture,variable.hidden))


    try:
        TestConfig(config.text,data)
    except:
        raise config_exception(message="Error while testing the config")

    # OpenBullet CVars to pydantic CVars, Values return as a string e.g. Lists, Dicts
    variables = [{"name":v.Name,"value":v.ToString(),"IsCapture":v.IsCapture,"hidden":v.Hidden} for v in data.Variables.All if v.Hidden == False and v.IsCapture == False]
    capture_variables = [{"name":v.Name,"value":v.ToString(),"IsCapture":v.IsCapture,"hidden":v.Hidden} for v in data.Variables.All if v.Hidden == False and v.IsCapture == True]

    return {"name":config.name,"status":str(data.Status.value),"variables":variables,"capture_variables":capture_variables}