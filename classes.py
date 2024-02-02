from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine, Numeric, ForeignKey

Base = declarative_base()

class Client(Base):
    __tablename__ = 'Клиенты'

    Код = Column(Integer(), primary_key=True)
    ФИО = Column(String(120), nullable=False, unique=False)
    Адрес = Column(String(200))
    Телефон = Column(String(20), nullable=False)
    Заказы = relationship('Orders', backref='Клиент1')


class Employees(Base):
    __tablename__ = 'Сотрудники'

    КодСотрудника = Column(Integer(), primary_key=True)
    Фамилия = Column(String(50), nullable=False)
    Имя = Column(String(50), nullable=False)
    Отчество = Column(String(70))
    Должность = Column(String(120), nullable=False)
    Адрес = Column(Text)
    ДомашнийТелефон = Column(String(20), nullable=False)
    ДатаРождения = Column(DateTime(), nullable=False)
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


class Orders(Base):
    __tablename__ = 'Заказы'

    КодЗаказа = Column(Integer(), primary_key=True)
    КодСотрудника = Column(Integer(), ForeignKey('Сотрудники.КодСотрудника'))
    КодТовара = Column(Integer(), ForeignKey('Товары.КодТовара'))
    ДатаРазмещения = Column(DateTime())
    ДатаИсполнения = Column(DateTime())
    КодКлиента = Column(Integer(), ForeignKey('Клиенты.Код'))


class Provider(Base):
    __tablename__ = 'Поставщик'

    КодПоставщика = Column(Integer(), primary_key=True)
    НазваниеПоставщика = Column(String(180), nullable=False)
    ПредставительПоставщика = Column(String(200), nullable=False)
    Обращаться = Column(Text)
    КонтактныйТелефон = Column(String(20), nullable=False)
    Адрес = Column(String(200))
    Поставка = relationship('Procurement', backref='Поставщик1')


class Procurement(Base):
    __tablename__ = 'Поставка'

    КодПоставки = Column(Integer(), primary_key=True)
    КодПоставщика = Column(Integer(), ForeignKey('Поставщик.КодПоставщика'))
    ДатаПоставки = Column(DateTime())
    Товары = relationship('Products', backref='Поставка1')

