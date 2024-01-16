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
        if id in self.data.keys():
            self.data[id] += amount
        else:
            self.data[id] = amount
        
        return self.data[id]

    def withdraw(self, id, amount):
        # If the account exists, withdraw the "amount" to the balance, 
        # else do nothing"
        if id in self.data.keys():
            self.data[id] += amount
            return self.data[id]
        else:
            return None

    