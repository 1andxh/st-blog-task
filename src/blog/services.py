from sqlalchemy.orm import Session
from .models import Post
import uuid
from src.database import get_db
from .exceptions import PostNotFoundError
from sqlalchemy import select
from .schemas import PostCreate, PostUpdate


def _get_post_or_404(post_id: uuid.UUID, session: Session) -> Post:
    statement = select(Post).where(Post.id == post_id)
    result = session.execute(statement)
    post = result.scalar_one_or_none()

    if post is None:
        raise PostNotFoundError

    return post


def get_post(post_id: uuid.UUID, session: Session) -> Post:
    return _get_post_or_404(post_id, session)


def get_posts(session: Session) -> list[Post]:
    posts = session.execute(select(Post).order_by(Post.created_at))
    return list(posts.scalars().all())


def create_post(session: Session, payload: PostCreate) -> Post:
    new_post = Post(title=payload.title, content=payload.content)
    session.add(new_post)
    session.commit()
    session.refresh(new_post)
    return new_post


def update_post(post_id: uuid.UUID, session: Session, payload: PostUpdate) -> Post:
    post = _get_post_or_404(post_id, session)
    update = payload.model_dump(exclude_unset=True)
    for k, v in update.items():
        setattr(post, k, v)

    session.commit()
    session.refresh(post)
    return post


def delete_post(post_id: uuid.UUID, session: Session) -> None:
    post = _get_post_or_404(post_id, session)
    session.delete(post)
    session.commit()
    return
