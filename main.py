from fastapi import FastAPI
from src.database.Data import Data
from src.helpers.Tools import Tools
from src.Router import Router


# Initialize app
app = FastAPI()

# Initialize data
data = Data()

# Initialize helpers
tools = Tools()

# Initialize routes
routes = Router(app, data, tools)
