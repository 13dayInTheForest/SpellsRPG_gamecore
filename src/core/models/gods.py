from sqlalchemy import Table, Column, String, Integer, Boolean
from src.db.database import metadata


gods = Table(
    'gods',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('description', String),
    Column('contract_terms', String),

    Column('nerf_hp', Integer),
    Column('nerf_age', Integer),
    Column('nerf_max_age', Integer),
    Column('min_atk', Integer),
    Column('max_atk', Integer),

    Column('magic_lvl', Integer, default=5),
    Column('physical_lvl', Integer, default=5),
    Column('agility_lvl', Integer, default=5),
    Column('carma_lvl', Integer, default=5),
)