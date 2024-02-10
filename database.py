from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine
from config_for_st_5 import conf_url

# создание движка
engine = create_engine(conf_url, echo=True)


# Создание сессии
# Session = sessionmaker(bind=engine)
session_ = sessionmaker(bind=engine)

# Объявление базового класса
class Base(DeclarativeBase):
    pass


