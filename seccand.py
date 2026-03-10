from fastapi import APIRouter
from pydantic import BaseModel, Field,EmailStr,ConfigDict
import uvicorn

router = APIRouter(prefix="/users", tags=["users"])

data_wo_age = {
    "email": "okoo.goe@gmail.com",
    "bio": None,
}

data = {
    "email": "abc@mail.ru",
    "bio": "Мен татумун жанмын",
    "age": 1,
}


class UserLive(BaseModel):
    email: EmailStr
    bio: str |None = Field(max_length=1000)

class UserAgeSchema(BaseModel):
    age: int =  Field(ge=0, le=130)

    model_config = ConfigDict(extra="forbid")

users = []
@router.post("/users")
def add_user(user: UserLive):
    users.append(user)
    return {"ok":True , "massage":"Юздер кошулду "}

@router.get("/users")
def get_users()->list[UserLive]:
    return users