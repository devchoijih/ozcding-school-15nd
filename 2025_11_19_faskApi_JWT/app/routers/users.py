from app.models.users import UserModel
from app.schemas.users import UserLoginRequest, UserLoginResponse
from fastapi import APIRouter, Response, HTTPException, Request
from fastapi import Depends

from app.services.auth import AuthService

user_router = APIRouter(prefix="/users")

@user_router.post("/login", status_code=204)
async def login(get_current_user: UserLoginRequest, auth_service: AuthService = Depends()) -> Response:
    return auth_service.login(get_current_user.username, get_current_user.password)

@user_router.post("/signup", status_code=201)
async def signup(get_current_user: UserLoginRequest):
    try:
        user = UserModel.create(get_current_user.username, get_current_user.password)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"username": user.username}

@user_router.get("/me")
async def get_me(
    request: Request,
    auth_service: AuthService = Depends(),
):
    request = auth_service.get_current_user(request)
    user = request.state.user

    return {"username": user.username}

