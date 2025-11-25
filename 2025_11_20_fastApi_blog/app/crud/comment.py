from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, asc, desc
from fastapi import HTTPException, status

from app.models.comment import Comment
from app.models.post import Post
from app.models.user import User as UserModel
from app.schemas.comment import CommentCreate, CommentUpdate
from app.enums.sort import SortType

async def create_comment_by_post_id_crud(
        db:AsyncSession,
        *,
        post_id:int,
        data:CommentCreate,
        current_user:UserModel
) -> Comment:
    comment = Comment(**data.model_dump(), owner_id= current_user.id, post_id=post_id)
    db.add(comment)

    await db.commit()
    await db.refresh(comment)

    return comment

async def get_comments_by_post_id_crud(
        db:AsyncSession,
        *,
        post_id:int,
        sort:SortType = SortType.desc,
        page:int = 1,
        limit:int = 20
) -> list[dict]:
    if page < 1:
        page = 1

    MAX_LIMIT = 100
    limit = min(limit, MAX_LIMIT)

    order_clause = {
        SortType.asc: asc(Comment.created_at),
        SortType.desc: desc(Comment.created_at)
    }[sort]

    results = await db.execute(
        select(
            Comment.id,
            Comment.content,
            Comment.created_at,
            Post.id.label("post_id"),
            Post.title.label("post_title"),
            Post.content.label("post_content"),
        )
        .join(Post, Post.id == Comment.post_id)
        .where(Post.id == post_id)
        .order_by(order_clause)
        .limit(limit)
        .offset((page - 1) * limit)
    )

    rows = results.mappings().all()

    return [dict(row) for row in rows]

async def update_comments_by_post_id_crud(
        db:AsyncSession,
        *,
        data:CommentUpdate,
        comment_id:int,
        current_user:UserModel
) -> Comment:
    comment = await db.get(Comment, comment_id)

    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")

    if comment.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="permission denied")

    comment.content = data.content

    await db.commit()
    await db.refresh(comment)

    return comment