import datetime

import sqlalchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, MetaData, Numeric
from typing import Optional, Annotated
from database import Base

from sqlalchemy import Column, Integer, String, DateTime, Text
# date = sqlalchemy.Column(sqlalchemy.date)

intpk = Annotated[int, mapped_column(primary_key=True)]

class Client(Base):
    __tablename__ = 'Клиенты'

    Код: Mapped[intpk]
    ФИО: Mapped[str] = mapped_column(String(180), nullable=False, unique=False)
    Адрес: Mapped[str] = mapped_column(String(220), nullable=True)
    Телефон: Mapped[str] = mapped_column(String(20), nullable=False)

    Заказы = relationship('Orders', backref='Клиент1')


class Employees(Base):
    __tablename__ = 'Сотрудники'

    КодСотрудника: Mapped[intpk]
    Фамилия: Mapped[str] = mapped_column(String(50), nullable=False)
    Имя: Mapped[str] = mapped_column(String(50), nullable=False)
    Отчество: Mapped[str] = mapped_column(String(70), nullable=True)
    Должность: Mapped[str] = mapped_column(String(120), nullable=False)
    Адрес: Mapped[str] = mapped_column(String(120), nullable=True)
    ДомашнийТелефон: Mapped[str] = mapped_column(String(20), nullable=False)
    ДатаРождения: Mapped[datetime.date]

    Заказы = relationship('Orders', backref='Сотрудник1')


class Products(Base):
    __tablename__ = 'Товары'

    КодТовара = Column(Integer(), primary_key=True)
    КодПоставки = Column(Integer(), ForeignKey('Поставка.КодПоставки'))
    НаименованиеТовара = Column(String(100), nullable=False)
    ТехническиеХарактеристики = Column(Text)
    Описание = Column(Text, nullable=False)
    Изображение = Column(Text)
    СтоимостьЗакупки = Column(Numeric, nullable=False)
    Наличие = Column(String(20))
    Количество = Column(Integer, nullable=False)
    СтоимостьПродажи = Column(Numeric, nullable=False)

    Заказы = relationship('Orders', backref='Товар1')
    Поставка_ = relationship('Procurement')


class Orders(Base):
    __tablename__ = 'Заказы'

    КодЗаказа: Mapped[intpk]
    КодСотрудника: Mapped[int] = mapped_column(ForeignKey('Сотрудники.КодСотрудника'))
    КодТовара: Mapped[int] =  mapped_column(ForeignKey('Товары.КодТовара'))
    ДатаРазмещения: Mapped[datetime.date]
    ДатаИсполнения: Mapped[datetime.date]
    КодКлиента: Mapped[int] =  mapped_column(ForeignKey('Клиенты.Код'))

    Товары_=relationship('Products')
    Сотрудник_=relationship('Employees')
    Клиент_=relationship('Client')


class Provider(Base):
    __tablename__ = 'Поставщик'

    КодПоставщика: Mapped[intpk]
    НазваниеПоставщика: Mapped[str] = mapped_column(String(180), nullable=False)
    ПредставительПоставщика: Mapped[str] = mapped_column(String(200), nullable=False)
    Обращаться: Mapped[str]
    КонтактныйТелефон: Mapped[str] = mapped_column(String(20), nullable=False)
    Адрес: Mapped[str] = mapped_column(String(200))

    Поставка = relationship('Procurement', backref='Поставщик1')

class Procurement(Base):
    __tablename__ = 'Поставка'

    КодПоставки: Mapped[intpk]
    КодПоставщика: Mapped[int] = mapped_column(ForeignKey('Поставщик.КодПоставщика'))
    ДатаПоставки: Mapped[datetime.date]

    Товары = relationship('Products', backref='Поставка1')
    Поставщик_ = relationship('Provider')




















