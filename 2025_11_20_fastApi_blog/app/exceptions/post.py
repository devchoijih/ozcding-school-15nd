from typing import Optional, Any, Dict

class PostNotFound(Exception):
    """사용자 미존재 예외: 기본 404"""
    status_code: int = 404
    code: str = "post_not_found"

    def __init__(
        self,
        message: str = "post not found",
        *,
        post_id: Optional[int] = None
    ) -> None:
        super().__init__(message)
        self.post_id = post_id

    def to_dict(self) -> Dict[str, Any]:
        return {
            "error": self.code,
            "message": str(self),
            "post_id": self.post_id,
        }

class PostOwnerNotMatched(Exception):
    status_code: int = 500
    code: str = "post_owner_not_matched"

    def __init__(
        self,
        message: str = "post_owner_not_matched",
        *,
        post_id: Optional[int] = None,
        owner_id: Optional[int] = None
    ) -> None:
        super().__init__(message)
        self.post_id = post_id
        self.owner_id = owner_id

    def to_dict(self) -> Dict[str, Any]:
        return {
            "error": self.code,
            "message": str(self),
            "post_id": self.post_id,
            "owner_id": self.owner_id,
        }