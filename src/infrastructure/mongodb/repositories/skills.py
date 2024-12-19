from .base import BaseRepo
from src.domain.skills.repository import ISkillsRepo


class SkillsRepo(BaseRepo, ISkillsRepo):
    pass


"""
{
    "id": str,
    "name": str,
    "dev_name": str,
    "description": str,
    "active": bool
}
"""