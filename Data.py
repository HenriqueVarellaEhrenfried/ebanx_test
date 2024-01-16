class Data():
    def __init__(self):
        # Model prototype:
        # {
        #     "id1":"balance1",
        #     "id2":"balance2",
        #     "id3":"balance3"
        # }
        
        self.data = {}


    def reset(self):
        self.data = {}

    def view_balance(self, id):
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
            self.data[id] += amount
            return {"origin": {"id": id, "balance": self.data[id]}}
        else:
            return 0

    def transfer(self, origin, destination, amount):
        amount = int(amount) # Make sure amount is a number
        if origin in self.data.keys():
            if destination in self.data.keys():
                # If both accounts exit, remove money from origin and add it t odestination
                self.data[origin] -= amount
                self.data[destination] += amount
                return {"origin": {"id": origin, "balance": self.data[origin]}, "destination": {"id": destination, "balance": self.data[destination]} }
            else:
                return 0
        else:
            return 0