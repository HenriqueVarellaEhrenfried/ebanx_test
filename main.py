from fastapi import HTTPException, Body, FastAPI
from Data import Data
from Tools import Tools
import json

app = FastAPI()
data = Data()
tools = Tools()

@app.post("/reset", status_code=200)
async def reset_data():
    data.reset()
    return 'OK'

@app.get("/balance", status_code=200)
async def get_balance(account_id=None):
    balance = data.view_balance(account_id)
    if balance != None:
        return balance
    else:
        # Fix: This code, although right, do not comply with the requirements
        raise HTTPException(status_code=404, detail=f'Account number {account_id} not found')
        return 0

@app.post("/event", status_code=201)
async def reset_data(body = Body('{}')):
    body_received = json.loads(body.decode())
    if "type" in body_received.keys():
        if body_received["type"] == "deposit":
            if tools.is_body_complete:
                data.deposit(body_received["destination"], body_received["amount"])
            else:
                status_code = 500
            return 1
        elif body_received["type"] == "withdraw":
            return 2
        elif body_received["type"] == "transfer":
            return 3
        else:
            return 4


    return 'OK'

# TO run: uvicorn main:app --reload