from classes import Client, Employees, Products, Orders, Provider, Procurement
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from config_for_st_5 import conf_url
import create_table

# файл конфигурации
url = conf_url

# создание движка
engine = create_engine(url)
# создание подключения
connection = engine.connect()

Base = declarative_base()
# # классы
# clients = Client
# employees = Employees
# products = Products
# orders = Orders
# procurement = Procurement
# provider = Provider

# Создание таблиц
Base.metadata.create_all(engine)
# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# переименование файла с таблицами
c_tab = create_table


# заполнение таблиц
session.add_all([c_tab.client_1, c_tab.client_2, c_tab.client_3, c_tab.client_4,
                 c_tab.client_5, c_tab.client_6, c_tab.client_7, c_tab.client_8,
                 c_tab.client_9, c_tab.client_10])
session.add_all([c_tab.employee_1, c_tab.employee_2, c_tab.employee_3,
                 c_tab.employee_4, c_tab.employee_5, c_tab.employee_6,
                 c_tab.employee_7])
session.add_all([c_tab.product1, c_tab.product2, c_tab.product3, c_tab.product4,
                 c_tab.product5, c_tab.product6, c_tab.order1, c_tab.order2,
                 c_tab.order3, c_tab.order4, c_tab.order5, c_tab.order6, c_tab.order7,
                 c_tab.order8])
session.add_all([c_tab.provider1, c_tab.provider2, c_tab.provider3, c_tab.provider4,
                 c_tab.provider5, c_tab.provider6, c_tab.provider7, c_tab.procurement1,
                 c_tab.procurement2, c_tab.procurement3, c_tab.procurement4,
                 c_tab.procurement5, c_tab.procurement6, c_tab.procurement7])
session.commit()

# обновление таблиц (значения с foreignkey)
upd1 = session.query(Procurement).get(4)
upd2 = session.query(Procurement).get(5)
upd3 = session.query(Procurement).get(6)
upd4 = session.query(Procurement).get(7)
upd5 = session.query(Procurement).get(1)
upd6 = session.query(Procurement).get(2)
upd7 = session.query(Procurement).get(3)
upd1.КодПоставщика = 4
upd2.КодПоставщика = 3
upd3.КодПоставщика = 2
upd4.КодПоставщика = 7
upd5.КодПоставщика = 6
upd6.КодПоставщика = 5
upd7.КодПоставщика = 1

session.add_all([upd1, upd2, upd3, upd4, upd5, upd6, upd7])
session.commit()

employee_query = session.query(Employees)
clean_py_query = employee_query.filter(Employees.КодСотрудника == 7)
clean_py_query.update({Employees.Адрес: 'Санкт-Петербург, пр. Пятилеток, д. 15'})

session.add(employee_query)
session.commit()

find_query1 = session.query(Orders).filter(Orders.КодЗаказа == 1)
find_query2 = session.query(Orders).filter(Orders.КодЗаказа == 2)
find_query3 = session.query(Orders).filter(Orders.КодЗаказа == 3)
find_query4 = session.query(Orders).filter(Orders.КодЗаказа == 4)
find_query5 = session.query(Orders).filter(Orders.КодЗаказа == 5)
find_query6 = session.query(Orders).filter(Orders.КодЗаказа == 6)
find_query7 = session.query(Orders).filter(Orders.КодЗаказа == 7)
find_query8 = session.query(Orders).filter(Orders.КодЗаказа == 8)

find_query1.update({Orders.КодСотрудника: 4})
find_query3.update({Orders.КодСотрудника: 4})
find_query5.update({Orders.КодСотрудника: 4})
find_query8.update({Orders.КодСотрудника: 4})
find_query2.update({Orders.КодСотрудника: 2})
find_query4.update({Orders.КодСотрудника: 2})
find_query6.update({Orders.КодСотрудника: 2})
find_query7.update({Orders.КодСотрудника: 2})

session.add_all(find_query1)
session.add_all(find_query2)
session.add_all(find_query3)
session.add_all(find_query4)
session.add_all(find_query5)
session.add_all(find_query6)
session.add_all(find_query7)
session.add_all(find_query8)
session.commit()

