# This file is part of the ebanx_test distribution (https://github.com/HenriqueVarellaEhrenfried/ebanx_test).
# Copyright (c) 2024 Henrique Varella Ehrenfried.

# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, version 3.

# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
# General Public License for more details.

# You should have received a copy of the GNU General Public License 
# along with this program. If not, see <http://www.gnu.org/licenses/>.


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
