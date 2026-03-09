from pydantic import BaseModel

data = {
    "email": "okoo.goe@gmail.com",
    "bio": None,
    "age": 12,
}

class UserSchema(BaseModel):
    email: str
    bio: str | None
    age: int
    age: int

User = UserSchema(**data)


def func(data_:dict):
    data_ ["age"] = +1
