from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine
from config_for_st_5 import conf_url

# создание движка
engine = create_engine(conf_url, echo=True)


# Создание сессии
session_ = sessionmaker(bind=engine)


# Объявление базового класса
class Base(DeclarativeBase):
    pass

    # repr_cols_num = 5
    # repr_cols = tuple()
    #
    # def __repr__(self):
    #     cols = []
    #     for idx, col in enumerate(self.__table__.columns.keys()):
    #         if col in self.repr_cols or idx < self.repr_cols_num:
    #             cols.append(f'{col}={getattr(self, col)}')
    #
    #     return f'<{self.__class__.__name__} {", ".join(cols)}>'
