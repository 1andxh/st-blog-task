from fastapi import status


class PostNotFoundError(Exception):
    def __init__(
        self,
        message: str = "Post not found",
        status_code: int = status.HTTP_404_NOT_FOUND,
    ):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)
