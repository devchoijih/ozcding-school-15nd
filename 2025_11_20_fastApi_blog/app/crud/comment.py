from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, status

from app.models.comment import Comment
from app.models.user import User as UserModel
from app.schemas.comment import CommentCreate


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
        post_id:int
) -> list[Comment]:
    comments = await db.execute(select(Comment)
                                .where(Comment.post_id == post_id)
                                .order_by(Comment.created_at.desc())
                                )

    comments = comments.scalars().all()

    return list(comments)

async def update_comments_by_post_id_crud(
        db:AsyncSession,
        *,
        data:CommentCreate,
        post_id:int,
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