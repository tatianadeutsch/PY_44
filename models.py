import datetime

import sqlalchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, MetaData, Numeric, UniqueConstraint
from typing import Optional, Annotated
from database import Base

from sqlalchemy import Column, Integer, String, DateTime, Text

intpk = Annotated[int, mapped_column(primary_key=True)]


class Clients(Base):
    __tablename__ = "clients"

    id_client: Mapped[intpk]
    name_client: Mapped[str] = mapped_column(String(180), nullable=False, unique=False)
    address_client: Mapped[str] = mapped_column(String(220), nullable=True)
    tel_client: Mapped[str] = mapped_column(String(20), nullable=False)

    orders__cl: Mapped[list["Orders"]] = relationship(back_populates="clients_")


class Employees(Base):
    __tablename__ = "employees"

    id_employee: Mapped[intpk]
    surname_employee: Mapped[str] = mapped_column(String(50), nullable=False)
    last_employee: Mapped[str] = mapped_column(String(50), nullable=False)
    patr_employee: Mapped[str] = mapped_column(String(70), nullable=True)
    post_employee: Mapped[str] = mapped_column(String(120), nullable=False)
    address_employee: Mapped[str] = mapped_column(String(120), nullable=True)
    privat_tel: Mapped[str] = mapped_column(String(20), nullable=False)
    birthdate: Mapped[datetime.date]

    orders__emp: Mapped["Orders"] = relationship(back_populates="employee_")


class Products(Base):
    __tablename__ = "products"

    id_product = Column(Integer(), primary_key=True)
    id_procur = Column(
        Integer(), ForeignKey("procurement.id_procurement", ondelete="set null")
    )
    name_product = Column(String(100), nullable=False)
    specifications = Column(Text)
    description = Column(Text, nullable=False)
    picture = Column(Text)
    price_purchase = Column(Numeric, nullable=False)
    availability = Column(String(20))
    quantity = Column(Integer, nullable=False)
    price_sale = Column(Numeric, nullable=False)

    procurements_: Mapped[list["Procurement"]] = relationship(
        back_populates="product__"
    )
    orders__: Mapped["Orders"] = relationship(back_populates="products_")


class Orders(Base):
    __tablename__ = "orders"

    id_order: Mapped[intpk]
    id_empl: Mapped[int] = mapped_column(
        ForeignKey("employees.id_employee", ondelete="set null")
    )
    id_prod: Mapped[int] = mapped_column(
        ForeignKey("products.id_product", ondelete="set null")
    )
    date_placement: Mapped[datetime.date]
    date_ex: Mapped[datetime.date]
    id_cl: Mapped[int] = mapped_column(
        ForeignKey("clients.id_client", ondelete="set null")
    )

    products_: Mapped[list["Products"]] = relationship(back_populates="orders__")
    employee_: Mapped["Employees"] = relationship(back_populates="orders__emp")
    clients_: Mapped["Clients"] = relationship(back_populates="orders__cl")


class Provider(Base):
    __tablename__ = "provider"

    id_provider: Mapped[intpk]
    name_provider: Mapped[str] = mapped_column(String(180), nullable=False)
    agent_provider: Mapped[str] = mapped_column(String(200), nullable=False)
    contact_person: Mapped[str]
    tel_prov: Mapped[str] = mapped_column(String(20), nullable=False)
    address_prov: Mapped[str] = mapped_column(String(200))

    procurements__prov: Mapped[list["Procurement"]] = relationship(
        back_populates="provider_"
    )

    procurements_: Mapped[list["Procurement"]] = relationship(
        secondary="many_to_many", back_populates="providers_"
    )


class Procurement(Base):
    __tablename__ = "procurement"

    id_procurement: Mapped[intpk]
    id_prov: Mapped[int] = mapped_column(
        ForeignKey("provider.id_provider", ondelete="cascade")
    )
    date_procur: Mapped[datetime.date]

    provider_: Mapped["Provider"] = relationship(back_populates="procurements__prov")
    product__: Mapped["Products"] = relationship(back_populates="procurements_")

    providers_: Mapped[list["Provider"]] = relationship(
        secondary="many_to_many", back_populates="procurements_"
    )

class Many_to_Many(Base):
    __tablename__ = "many_to_many"
    __table_args__ = (UniqueConstraint("proc_id", "prov_id", name="idx_proc_prov"),)

    id: Mapped[intpk]
    proc_id: Mapped[int] = mapped_column(ForeignKey("procurement.id_procurement"))
    prov_id: Mapped[int] = mapped_column(ForeignKey("provider.id_provider"))


# from sqlalchemy import Table, Column, Integer, String
#
# table_m_to_m = Table(
#     "many_to_many",
#     Base.metadata,
#     Column("id", Integer, primary_key=True),
#     Column("proc_id", ForeignKey("procurement.id_procurement"), nullable=False),
#     Column("prov_id", ForeignKey("provider.id_provider"), nullable=False),
#     UniqueConstraint("proc_id", "prov_id", name="idx_proc_prov"),
# )
