class InvalidKeyUserError(Exception):

    def __init__(self, **kwargs) -> None:
        self.message = {"errors": []}
        available_keys = {"name", "last_name", "email", "password"}
        invalid_keys = [key for key in kwargs.keys() if key not in available_keys]
        
        if invalid_keys:
            self.message["errors"].append({
                "message": "Invalid keys provided.",
                "invalid_keys": invalid_keys,
                "available_keys": list(available_keys)
            })
        else:
            self.message["errors"].append({"Unexpected error occurred."})
        
        super().__init__(self.message)

class InvalidTypeUserError(Exception):

    types = {
        str: "string",
        int: "integer",
        float: "float",
        list: "list",
        dict: "dictionary",
        bool: "boolean"
    }
    
    def __init__(self, **kwargs) -> None:
        self.message = {"errors": []}
        
        for field_name, value in kwargs.items():
            if type(value) != str:
                self.message["errors"].append({
                    "field": field_name,
                    "expected": "string",
                    "received": self.types.get(type(value), "unknown")
                })
        
        super().__init__(self.message)
