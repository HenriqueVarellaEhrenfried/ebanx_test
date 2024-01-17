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

class Data():
    def __init__(self):
        # Model prototype:
        # {
        #     "id1":"balance1",
        #     "id2":"balance2",
        #     "id3":"balance3"
        # }
        # Where id1, id2, ..., idn is the account id and
        # balance1, balance2, ..., balancen is the account balance        
        self.data = {}

    def reset(self):
        self.data = {}

    def view_balance(self, id):
        # Before showing the the balance, we must know it the account exists
        if id in self.data.keys():
            balance = self.data[id]
        else:
            balance = None
        return balance
    
    def deposit(self, id, amount):
        # If the account exists, add the "amount" to the balance, 
        # else create an account and initialize the value as "amount"
        amount = int(amount) # Make sure amount is a number
        if id in self.data.keys():
            self.data[id] += amount
        else:
            self.data[id] = amount

        return {"destination": {"id":id, "balance": self.data[id]}}

    def withdraw(self, id, amount):
        # If the account exists, withdraw the "amount" to the balance, 
        # else do nothing"
        amount = int(amount) # Make sure amount is a number
        if id in self.data.keys():
            self.data[id] -= amount
            return {"origin": {"id": id, "balance": self.data[id]}}
        else:
            return 0

    def transfer(self, origin, destination, amount):
        # If the origin account exists, make a transfer:
        # 1) if the destination exists, just increase its balance and reduce the balance from the origin
        # 2) if the destination does not exist, create it and its balance is the received amount. Also reduce the balance from the origin
        # If the origin account does not exist, return 0

        amount = int(amount) # Make sure amount is a number
        if origin in self.data.keys():
            if destination in self.data.keys():
                # If both accounts exist, remove money from origin and add it to destination
                self.data[origin] -= amount
                self.data[destination] += amount
                return {"origin": {"id": origin, "balance": self.data[origin]}, "destination": {"id": destination, "balance": self.data[destination]} }
            else:
                 # If destination account does not exist, create it and make the transfer
                self.data[origin] -= amount
                self.data[destination] = amount
                return {"origin": {"id": origin, "balance": self.data[origin]}, "destination": {"id": destination, "balance": self.data[destination]} }
        else:
            # If origin does not exist, abort
            return 0