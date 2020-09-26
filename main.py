
from OpenBullet2Python.TestConfig import TestConfig
from OpenBullet2Python.Models.BotData import BotData
from OpenBullet2Python.Models.CVar import CVar
from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from base64 import b64decode
from models.config import configIn,configOut
app = FastAPI()


@app.post("/")
async def root():
    return {"message": "Hello World"}
    
@app.post("/api/import/",response_model=configOut)
async def test_config(config: configIn):
    # Decode the base64
    try:
        config.config_text = b64decode(config.config_text).decode('utf-8')
    except:
        raise HTTPException(status_code=400,detail={"message": "Error decoding b64"})

    # Data contains the list of variable and the bot status
    data = BotData()

    try:
        TestConfig(config.config_text,data)
    except:
        raise HTTPException(status_code=400,detail={"message": "Error while testing the config"})

    variables = [{"Name":v.Name,"Value":v.ToString()} for v in data.Variables.All if v.Hidden == False and v.IsCapture == False]
    capture_variables = [{"Name":v.Name,"Value":v.ToString()} for v in data.Variables.All if v.Hidden == False and v.IsCapture == True]
    return {"name":config.name,"status":str(data.Status.value),"variables":variables,"capture_variables":capture_variables}