from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.blog.schemas import PostResponse, PostCreate, PostUpdate
from .services import create_post, get_post, get_posts, update_post, delete_post
import uuid

router = APIRouter()


@router.post("/", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
async def create_blogpost(payload: PostCreate, session: Session = Depends(get_db)):
    return create_post(session, payload)


@router.get("/", response_model=list[PostResponse])
async def list_blogposts(session: Session = Depends(get_db)):
    return get_posts(session)


@router.get("/{post_id}", response_model=PostResponse)
async def read_blogpost(post_id: uuid.UUID, session: Session = Depends(get_db)):
    return get_post(post_id, session)


@router.patch("/{post_id}", response_model=PostResponse)
async def update_blogpost(
    post_id: uuid.UUID, payload: PostUpdate, session: Session = Depends(get_db)
):
    return update_post(post_id, session, payload)


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blogpost(post_id: uuid.UUID, session: Session = Depends(get_db)):
    return delete_post(post_id, session)
