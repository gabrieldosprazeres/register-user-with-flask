class EmailAlreadyExistsError(Exception):

    def __init__(self, email: str) -> None:
        self.message = {"errors": []}
        self.message["errors"].append(
            {
                "message": "Email already exists",
                "email": email
            }
        )

        super().__init__(self.message)

class PatternEmailError(Exception):

    def __init__(self, email: str) -> None:
        self.message = {"errors": []}
        self.message["errors"].append(
            {
                "field_sent": {
                    "email": email,
                    "message": "Invalid email format, expected format: xxxxx@xxxx.xxx or xxxxx@xxxx.xxx.xx"
                }
            }
        )

        super().__init__(self.message)