import datetime

import sqlalchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, MetaData, Numeric
from typing import Optional, Annotated
from database import Base

from sqlalchemy import Column, Integer, String, DateTime, Text
# date = sqlalchemy.Column(sqlalchemy.date)

intpk = Annotated[int, mapped_column(primary_key=True)]

class Clients(Base):
    __tablename__ = 'clients'

    id_client: Mapped[intpk]
    name_client: Mapped[str] = mapped_column(String(180), nullable=False, unique=False)
    address_client: Mapped[str] = mapped_column(String(220), nullable=True)
    tel_client: Mapped[str] = mapped_column(String(20), nullable=False)


class Employees(Base):
    __tablename__ = 'employees'

    id_employee: Mapped[intpk]
    surname_employee: Mapped[str] = mapped_column(String(50), nullable=False)
    last_employee: Mapped[str] = mapped_column(String(50), nullable=False)
    patr_employee: Mapped[str] = mapped_column(String(70), nullable=True)
    post_employee: Mapped[str] = mapped_column(String(120), nullable=False)
    address_employee: Mapped[str] = mapped_column(String(120), nullable=True)
    privat_tel: Mapped[str] = mapped_column(String(20), nullable=False)
    birthdate: Mapped[datetime.date]


class Products(Base):
    __tablename__ = 'products'

    id_product = Column(Integer(), primary_key=True)
    id_procur = Column(Integer(), ForeignKey('procurement.id_procurement'))
    name_product = Column(String(100), nullable=False)
    specifications = Column(Text)
    description = Column(Text, nullable=False)
    picture = Column(Text)
    price_purchase = Column(Numeric, nullable=False)
    availability = Column(String(20))
    quantity = Column(Integer, nullable=False)
    price_sale = Column(Numeric, nullable=False)

    procurements_ = relationship('Procurement')


class Orders(Base):
    __tablename__ = 'orders'

    id_order: Mapped[intpk]
    id_empl: Mapped[int] = mapped_column(ForeignKey('employees.id_employee'))
    id_prod: Mapped[int] =  mapped_column(ForeignKey('products.id_product'))
    date_placement: Mapped[datetime.date]
    date_ex: Mapped[datetime.date]
    id_cl: Mapped[int] =  mapped_column(ForeignKey('clients.id_client'))

    products_=relationship('Products')
    employee_=relationship('Employees')
    clients_=relationship('Clients')


class Provider(Base):
    __tablename__ = 'provider'

    id_provider: Mapped[intpk]
    name_provider: Mapped[str] = mapped_column(String(180), nullable=False)
    agent_provider: Mapped[str] = mapped_column(String(200), nullable=False)
    contact_person: Mapped[str]
    tel_prov: Mapped[str] = mapped_column(String(20), nullable=False)
    address_prov: Mapped[str] = mapped_column(String(200))


class Procurement(Base):
    __tablename__ = 'procurement'

    id_procurement: Mapped[intpk]
    id_prov: Mapped[int] = mapped_column(ForeignKey('provider.id_provider'))
    date_procur: Mapped[datetime.date]

    provider_ = relationship('Provider')




















