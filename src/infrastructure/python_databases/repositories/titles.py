from .base import BaseRepo
from src.domain.titles.repository import ITitleRepo


class TitlesRepo(BaseRepo, ITitleRepo):
    pass
