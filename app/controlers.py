from litestar import Controller, get, post
from litestar.di import Provide
from app.dtos import AuthorReadDTO, AuthorWriteDTO
from app.models import Author

from app.repositories import AuthorRepository, provide_authors_repo


class AuthorController(Controller):
    path = "/authors"
    return_dto = AuthorReadDTO
    dependencies = {"authors_repo": Provide(provide_authors_repo)}

    @get()
    async def list_authors(self, authors_repo: AuthorRepository) -> list[Author]:
        return authors_repo.list()

    @post(dto=AuthorWriteDTO)
    async def create_author(self, data: Author, authors_repo: AuthorRepository) -> Author:
        return authors_repo.add(data)