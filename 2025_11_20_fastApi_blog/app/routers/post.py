from typing import Annotated

from fastapi import APIRouter, status, Path, Query
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_current_user, get_db
from app.schemas.comment import CommentCreate, CommentUpdate
from app.schemas.post import PostRead, PostCreate, PostUpdate
from app.models.post import Post
from app.models.user import User as UserModel
from app.crud.post import (get_posts_by_all, get_posts_by_user_id, insert_posts_by_user_id, delete_posts_by_user_id, update_post_by_user_id)
from app.crud.comment import (create_comment_by_post_id_crud, get_comments_by_post_id_crud,
                              update_comments_by_post_id_crud, SortType)


router = APIRouter(prefix="/posts", tags=["posts"])

# 게시글 전체 목록 조회 (페이지네이션 지원)
@router.get("", response_model=list[PostRead])
async def get_posts(
        db:AsyncSession = Depends(get_db)
      , page: int = Query(default=1, ge=1)
      , limit: int = Query(default=20, ge=1, le=100)
):

    return await get_posts_by_all(db, page, limit)

# 게시글 단건 조회 (post_id 기준)
@router.get("/{post_id}")
async def get_post_by_post_id(
        post_id : Annotated['int', Path(ge=1)]
      , db:AsyncSession = Depends(get_db)):

    return await get_posts_by_user_id(db, post_id)

# 게시글 생성 (로그인 유저 기준)
@router.post(""
             ,status_code=status.HTTP_201_CREATED
             )
async def create_post(
      data: PostCreate
    , db:AsyncSession = Depends(get_db)
    , current_user: UserModel = Depends(get_current_user)
):

    post = Post(**data.model_dump(), owner_id=current_user.id)

    return await insert_posts_by_user_id(db, post)

# 게시글 삭제 (작성자 본인만 가능)
@router.delete("/{post_id}")
async def delete_post(
        post_id: Annotated[int, Path(title="게시글 ID", ge=1)]
      , db:AsyncSession = Depends(get_db)
      , current_user: UserModel = Depends(get_current_user)
):

    return await delete_posts_by_user_id(db, post_id=post_id, current_user=current_user)

# 게시글 수정 (작성자 본인만 가능)
@router.put("/{post_id}")
async def update_post_by_post_id(
        post_id: Annotated[int, Path(title="게시글 ID", ge=1)]
      , data: PostUpdate
      , db:AsyncSession = Depends(get_db)
      , current_user: UserModel = Depends(get_current_user)
):
    return await update_post_by_user_id(db, post_id=post_id, current_user=current_user, data=data)


# 특정 게시글에 댓글 작성
@router.post("/{post_id}/comments")
async def post_comment_by_post_id(
        post_id : Annotated[int, Path(title="게시글 ID", ge=1)]
      , data: CommentCreate
      , db:AsyncSession = Depends(get_db)
      , current_user: UserModel = Depends(get_current_user)
):
    return await create_comment_by_post_id_crud(db, post_id=post_id, data=data, current_user=current_user)


# 특정 게시글의 댓글 목록 조회
# - 정렬: asc / desc
# - 페이지네이션: page, limit
@router.get("/{post_id}/comments")
async def get_comments_by_post_id(
        post_id : Annotated[int, Path(title="게시글 ID", ge=1)]
      , sort: SortType = Query(default=SortType.desc)
      , page: int = Query(default=1, ge=1)
      , limit: int = Query(default=20, ge=1, le=100)
      , db:AsyncSession = Depends(get_db)
):
    return await get_comments_by_post_id_crud(db, post_id=post_id, sort=sort, page=page, limit=limit)


# 특정 게시글의 특정 댓글 수정
@router.put("/{post_id}/comments/{comment_id}")
async def update_comments_by_post_id_and_comment_id(
        post_id : Annotated[int, Path(title="게시글 ID", ge=1)]
        , comment_id : Annotated[int, Path(title="댓글 ID", ge=1)]
        , data: CommentUpdate
        , db:AsyncSession = Depends(get_db)
        , current_user: UserModel = Depends(get_current_user)
):
    return await update_comments_by_post_id_crud(db, data=data, comment_id=comment_id, current_user=current_user)

# 특정 게시글의 특정 댓글 삭제
@router.delete("/{post_id}/comments/{comment_id}")
async def delete_comments_by_post_id_and_comment_id(
        post_id : Annotated[int, Path(title="게시글 ID", ge=1)]
        , comment_id : Annotated[int, Path(title="댓글 ID", ge=1)]
):
    return {"test": "ok"}