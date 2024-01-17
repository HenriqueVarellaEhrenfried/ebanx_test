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

class Tools():
    """This class is a toolbox, designed to hold helper functions"""
    def __init__(self):
        pass

    def is_body_complete(self, type, body):
        """Verify for each type of operation if the body has all mandatory fields"""
        if type == "deposit":
            if "destination" in body.keys():
                if "amount" in body.keys():
                    return True
                else:
                   return False
            else:
                return False

        elif type == "withdraw":
            if "origin" in body.keys():
                if "amount" in body.keys():
                    return True
                else:
                   return False
            else:
                return False

        elif type == "transfer":
            if "origin" in body.keys():
                if "amount" in body.keys(): 
                    if "destination" in body.keys():
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False