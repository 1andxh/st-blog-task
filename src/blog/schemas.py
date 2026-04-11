from pydantic import BaseModel, ConfigDict
from datetime import datetime
import uuid


class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    pass


class PostUpdate(BaseModel):
    title: str | None = None
    content: str | None = None


class PostResponse(PostBase):
    id: uuid.UUID
    created_at: datetime
    modified: datetime

    model_config = ConfigDict(from_attributes=True)
