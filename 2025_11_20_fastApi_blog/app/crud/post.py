from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.post import Post
from app.schemas.post import PostRead, PostCreate, PostUpdate
from typing import Optional, Any, Dict
from app.models.user import User as UserModel

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

async def get_posts_by_all(db: AsyncSession) -> list[PostRead] | None:
    result = await db.execute(select(Post))
    posts = result.scalars().all()

    return [PostRead.model_validate(post) for post in posts]


async def get_posts_by_user_id(db: AsyncSession, post_id:int) -> PostRead | None:
    result = await db.execute(select(Post).where(Post.id == post_id))
    result_post = result.scalars().first()

    return PostRead.model_validate(result_post)

async def insert_posts_by_user_id(db: AsyncSession, post: Post) -> Post:
    db.add(post)

    await db.commit()
    await db.refresh(post)

    return post


async def delete_posts_by_user_id(db: AsyncSession, *, post_id:int, current_user:UserModel) -> dict[str, str]:
    post = await db.get(Post, post_id)

    if not post:
        raise PostNotFound(post_id=post_id)

    if post.owner_id != current_user.id:
        raise PostOwnerNotMatched(post_id=post_id)

    await db.delete(post)
    await db.commit()

    return {"message": "삭제 완료"}

async def update_post_by_user_id(db: AsyncSession, *, post_id:int, current_user:UserModel, data:PostUpdate) -> Post:
    post = await db.get(Post, post_id)

    if not post:
        raise PostNotFound(post_id=post_id)

    if post.owner_id != current_user.id:
        raise PostOwnerNotMatched(post_id=post_id)

    post.title = data.title
    post.content = data.content

    await db.commit()
    await db.refresh(post)

    return post