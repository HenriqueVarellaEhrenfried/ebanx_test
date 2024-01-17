import json
from fastapi import  Body, Response
from fastapi.responses import PlainTextResponse
from starlette.status import HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR

class Router():
    def __init__(self, app, data, tools):
        # The response_class PlainTextResponse is used to remove quotes from the string.
        @app.post("/reset", status_code=HTTP_200_OK, response_class=PlainTextResponse)
        async def reset_data():
            data.reset()
            return 'OK'

        @app.get("/balance", status_code=HTTP_200_OK)
        async def get_balance(account_id=None, response: Response = HTTP_200_OK):
            balance = data.view_balance(account_id)
            # None is important here because if the account does not exist the status code should change
            if balance != None: 
                return balance
            else:
                response.status_code = HTTP_404_NOT_FOUND
                return 0

        @app.post("/event", status_code=HTTP_201_CREATED)
        async def perform_event(body = Body('{}'), response: Response = HTTP_200_OK):

            if isinstance(body, dict): # If we have a dictionary, just attribute it
                body_received = body
            else:
                body_received = json.loads(body.decode()) # Else transforms string into dictionary

            return_from_operation = None
            if "type" in body_received.keys():

                # Check of all fields in the body exist and perform the operation accordingly
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
                # If there is an error in the operation, set the status code to 404
                response.status_code = HTTP_404_NOT_FOUND

            return return_from_operation