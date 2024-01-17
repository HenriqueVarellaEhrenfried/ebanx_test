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