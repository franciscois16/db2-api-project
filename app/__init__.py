from litestar import Litestar
from app.controlers import AuthorController

from app.database import sqlalchemy_config


app = Litestar([AuthorController], debug=True, plugins=[sqlalchemy_config])
