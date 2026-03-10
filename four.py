from http.client import responses

from fastapi import FastAPI, APIRouter, HTTPException, Response, Depends
from authx import AuthX,AuthXConfig
from pydantic import BaseModel

router_four = APIRouter(prefix="/логин",tags=["Логин и пароль"])
app = FastAPI()
config = AuthXConfig()
config.JWT_SECRET_KEY = "SECRET_KEY"
config.JWT_ACCESS_COOKIE_NAME = "MY_TOKEN"
config.JWT_TOKEN_LOCATION = ['cookies',]

security = AuthX (config=config)

class Userlogin(BaseModel):
    username: str
    password: str
@router_four.post('/login')
def login(creds: Userlogin,resp:Response):
    if creds.username == 'test'  and creds.password == 'test':
        token = security.create_access_token(uid='12345678')
        resp.set_cookie(config.JWT_ACCESS_COOKIE_NAME,token)

        return {"message":"login success"}
    raise HTTPException(status_code=401,detail="incorrect username or password")

@router_four.get('/protected', dependencies=[Depends(security.access_token_required)])
def protected():
    return {'data': 'top secret'}