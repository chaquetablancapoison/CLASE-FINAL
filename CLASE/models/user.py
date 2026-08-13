from dataclasses import dataclass


@dataclass
class User:
    fname: str
    lname: str
    age: int
    email: str
