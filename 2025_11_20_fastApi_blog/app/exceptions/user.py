from typing import Optional, Any, Dict

class UserAlreadyExists(Exception):
    """중복 사용자 예외: 기본 409"""
    status_code: int = 409
    code: str = "user_already_exists"

    def __init__(
        self,
        message: str = "user already exists",
        *,
        field: Optional[str] = None,
        value: Optional[str] = None,
    ) -> None:
        super().__init__(message)
        self.field = field
        self.value = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            "error": self.code,
            "message": str(self),
            "field": self.field,
            "value": self.value,
        }


class UserNotFound(Exception):
    """사용자 미존재 예외: 기본 404"""
    status_code: int = 404
    code: str = "user_not_found"

    def __init__(
        self,
        message: str = "user not found",
        *,
        user_id: Optional[int] = None,
        username: Optional[str] = None,
        email: Optional[str] = None,
    ) -> None:
        super().__init__(message)
        self.user_id = user_id
        self.username = username
        self.email = email

    def to_dict(self) -> Dict[str, Any]:
        return {
            "error": self.code,
            "message": str(self),
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
        }