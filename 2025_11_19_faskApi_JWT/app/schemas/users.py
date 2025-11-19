from pydantic import BaseModel


class UserLoginRequest(BaseModel):
    username: str
    password: str

class UserLoginResponse(BaseModel):
    user: str
    password: str