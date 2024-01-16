class Data():
    def __init__(self):
        
        # {
        #     "id1":"balance1",
        #     "id2":"balance2",
        #     "id3":"balance3"
        # }
        
        self.data = {}


    def reset(self):
        self.data = {}

    def view_balance(self, id):
        if self.data.keys() == id:
            balance = self.data["id"]
        else:
            balance = None
        return balance
    
    