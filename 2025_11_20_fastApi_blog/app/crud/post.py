from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.models.post import Post
from app.schemas.post import PostRead, PostCreate, PostUpdate
from app.models.user import User as UserModel
from app.exceptions.post import PostNotFound, PostOwnerNotMatched

async def get_posts_by_all(
        db: AsyncSession
      , page: int = 1
      , limit: int = 20
) -> list[PostRead]:

    if page < 1:
        page = 1

    MAX_LIMIT = 100
    limit = min(limit, MAX_LIMIT)

    offset = (page - 1) * limit

    query = (select(Post)
             .options(selectinload(Post.comments))
             .order_by(Post.created_at.desc())
             .limit(limit)
             .offset(offset))

    result = await db.execute(query)
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