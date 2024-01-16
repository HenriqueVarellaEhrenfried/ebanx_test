class Tools():
    def __init__(self):
        pass

    def is_body_complete(self, type, body):
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