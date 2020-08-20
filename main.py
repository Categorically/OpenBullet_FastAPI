
from OpenBullet2Python.TestConfig import TestConfig
from OpenBullet2Python.Models.BotData import BotData
from OpenBullet2Python.Models.CVar import CVar
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from base64 import b64decode

app = FastAPI()


@app.post("/")
async def root():
    return {"message": "Hello World"}
    
@app.post("/test/")
async def test_config(config_text:str):
    data = BotData()
    try:
        print(config_text)
        config_text = b64decode(config_text).decode('utf-8')
        print(config_text)
    except:
        return JSONResponse(status_code=400,content={"message": "Error decoding b64"})    
    try:
        TestConfig(config_text,data)
    except:
        return JSONResponse(status_code=400,content={"message": "Error while testing the config"})
    Variables = []
    for v in data.Variables.All:
        if v.Hidden == False:
            variable = {"Name":v.Name,"Value":v.ToString()}
            Variables.append(variable)
    return JSONResponse(status_code=200,content={"message": "Tested","Satus":str(data.Status.value), "Variables":Variables})
