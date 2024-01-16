from fastapi import HTTPException, Body, FastAPI, Response
from starlette.status import HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR
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
async def get_balance(account_id=None, response: Response = HTTP_200_OK):
    balance = data.view_balance(account_id)
    if balance != None:
        return balance
    else:
        response.status_code = HTTP_404_NOT_FOUND
        return 0

@app.post("/event", status_code=HTTP_201_CREATED)
async def reset_data(body = Body('{}'), response: Response = HTTP_200_OK):
    body_received = json.loads(body.decode()) # Transforms binary string into dictionary
    return_from_operation = None
    if "type" in body_received.keys():
        if tools.is_body_complete:
            if body_received["type"] == "deposit":            
                return_from_operation = data.deposit(body_received["destination"], body_received["amount"])
            elif body_received["type"] == "withdraw":
                return_from_operation =  data.withdraw(body_received["origin"], body_received["amount"])
            elif body_received["type"] == "transfer":
                return_from_operation = data.transfer(body_received["origin"],body_received["destination"],body_received["amount"])
            else:
                # Operation not implemented
                response.status_code = HTTP_500_INTERNAL_SERVER_ERROR
                return 0
        else:
            # Body incomplete
            response.status_code = HTTP_500_INTERNAL_SERVER_ERROR
            return 0
    else:
        # Type unknown
        response.status_code = HTTP_500_INTERNAL_SERVER_ERROR
        return 0

    if return_from_operation == 0:
        response.status_code = HTTP_404_NOT_FOUND
    return return_from_operation

# TO run: uvicorn main:app --reload