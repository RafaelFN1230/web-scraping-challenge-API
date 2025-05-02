from dataclasses import dataclass

@dataclass
class UserDTO:
    email: str
    password: str