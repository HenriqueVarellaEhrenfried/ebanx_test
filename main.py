from fastapi import HTTPException, FastAPI
from Data import Data

app = FastAPI()
data = Data()

@app.get("/balance", status_code=200)
async def get_balance(account_id=None):
    balance = data.view_balance(account_id)
    if balance != None:
        return balance
    else:
        # Fix: This code, although right, do not comply with the requirements
        raise HTTPException(status_code=404, detail=f'Account number {account_id} not found')
        return 0



# TO run: uvicorn main:app --reload