from sqlalchemy import select, cast, Integer, func, and_, desc, asc, distinct, delete
from sqlalchemy.orm import aliased, selectinload, joinedload

from database import Base, session_, engine
from models import Clients, Employees, Products, Orders, Provider, Procurement, Many_to_Many


def create_table():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def insert_table():
    with session_() as session:
        client_1 = Clients(
            name_client="Русакова Василиса Евгеньевна", tel_client="+79119119111"
        )

        client_2 = Clients(
            name_client="Киренков Александр Алексеевич", tel_client="+79119119112"
        )

        client_3 = Clients(
            name_client="Владимиров Роман Петрович", tel_client="+79119119113"
        )

        client_4 = Clients(
            name_client="Родионов Михаил Александрович", tel_client="+79119119114"
        )

        client_5 = Clients(
            name_client="Баранов Тимур Михайлович", tel_client="+79119119115"
        )

        client_6 = Clients(
            name_client="Сурмина Валерия Валериевна", tel_client="+79119119116"
        )

        client_7 = Clients(
            name_client="Акимова Ольга Александровна", tel_client="+79119119117"
        )

        client_8 = Clients(
            name_client="Киреев Максим Леонидович", tel_client="+79119119118"
        )

        client_9 = Clients(
            name_client="Архипова Варвара Дмитриевна", tel_client="+79119119119"
        )

        client_10 = Clients(
            name_client="Караваева Анна Васильевна", tel_client="+79119119120"
        )
        session.add_all(
            [
                client_1,
                client_2,
                client_3,
                client_4,
                client_5,
                client_6,
                client_7,
                client_8,
                client_9,
                client_10,
            ]
        )

        employee_1 = Employees(
            surname_employee="Гирькин",
            last_employee="Василий",
            patr_employee="Васильевич",
            post_employee="Директор",
            privat_tel="+79119129121",
            birthdate="1968-01-12",
        )

        employee_2 = Employees(
            surname_employee="Штангин",
            last_employee="Никонор",
            patr_employee="Никонорович",
            post_employee="Заместитель директора",
            privat_tel="+79119129122",
            birthdate="1970-01-02",
        )

        employee_3 = Employees(
            surname_employee="Быстрова",
            last_employee="Евгения",
            patr_employee="Евгениевна",
            post_employee="Бухгалтер",
            privat_tel="+79119129123",
            birthdate="1988-04-12",
        )

        employee_4 = Employees(
            surname_employee="Каштанова",
            last_employee="Евдокия",
            patr_employee="Герасимовна",
            post_employee="Товаровед",
            privat_tel="+79119129124",
            birthdate="1983-01-31",
        )

        employee_5 = Employees(
            surname_employee="Трухачева",
            last_employee="Наталья",
            patr_employee="Васильевна",
            post_employee="Кассир",
            privat_tel="+79119129125",
            birthdate="1998-02-11",
        )

        employee_6 = Employees(
            surname_employee="Барсукова",
            last_employee="Гликерия",
            patr_employee="Борисовна",
            post_employee="Кассир",
            privat_tel="+79119129126",
            birthdate="1990-03-05",
        )

        employee_7 = Employees(
            surname_employee="Хомяков",
            last_employee="Спартак",
            patr_employee="Аристархович",
            post_employee="Грузчик",
            privat_tel="+79119129127",
            birthdate="1999-10-10",
        )

        session.add_all(
            [
                employee_1,
                employee_2,
                employee_3,
                employee_4,
                employee_5,
                employee_6,
                employee_7,
            ]
        )

        provider1 = Provider(
            name_provider="Зимнее утро",
            agent_provider="Утренний Владлен Владленович",
            contact_person="Рукавичкина",
            tel_prov="+79119009090",
            address_prov="Санкт-Петербург",
        )

        provider2 = Provider(
            name_provider="Зимние сумерки",
            agent_provider="Сумеречников Павел Павлович",
            contact_person="Косичкина",
            tel_prov="+79119009091",
            address_prov="Санкт-Петербург",
        )

        provider3 = Provider(
            name_provider="Зимний полдень",
            agent_provider="Полдничий Иван Иванович",
            contact_person="Кляксова",
            tel_prov="+79119009092",
            address_prov="Санкт-Петербург",
        )

        provider4 = Provider(
            name_provider="Зимняя слякоть",
            agent_provider="Слякотный Тимур Тимурович",
            contact_person="Пироженкова",
            tel_prov="+79119009093",
            address_prov="Москва",
        )

        provider5 = Provider(
            name_provider="Зимние забавы",
            agent_provider="Забавин Петр Петрович",
            contact_person="Пуговкина",
            tel_prov="+79119009094",
            address_prov="Москва",
        )

        provider6 = Provider(
            name_provider="Зимние каникулы",
            agent_provider="Отдыхай Игорь Игоревич",
            contact_person="Березкина",
            tel_prov="+79119009095",
            address_prov="Санкт-Петербург",
        )

        provider7 = Provider(
            name_provider="Зимние дороги",
            agent_provider="Незевай Сергей Сергеевич",
            contact_person="Шнурков",
            tel_prov="+79119009096",
            address_prov="Санкт-Петербург",
        )

        session.add_all(
            [
                provider1,
                provider2,
                provider3,
                provider4,
                provider5,
                provider6,
                provider7,
            ]
        )

        procurement1 = Procurement(date_procur="2023-12-20", provider_=provider7)

        procurement2 = Procurement(date_procur="2023-12-21", provider_=provider6)

        procurement3 = Procurement(date_procur="2023-12-22", provider_=provider5)

        procurement4 = Procurement(date_procur="2023-12-23", provider_=provider4)

        procurement5 = Procurement(date_procur="2023-12-24", provider_=provider3)

        procurement6 = Procurement(date_procur="2023-12-25", provider_=provider2)

        procurement7 = Procurement(date_procur="2023-12-26", provider_=provider1)

        session.add_all(
            [
                procurement1,
                procurement2,
                procurement3,
                procurement4,
                procurement5,
                procurement6,
                procurement7,
            ]
        )

        product1 = Products(
            name_product='Стиральный порошок "Не линяй"',
            specifications="Упаковка 10 кг",
            description="Порошок белого цвета, гиппоаллергенный",
            picture="https://opttorg-horeca.ru/assets/images/catalog/hoz-tovar/stiralnyj-poroshok-dosya-8-5kg.jpg",
            price_purchase=600,
            availability="в наличии",
            quantity=20,
            price_sale=700,
            procurements_=procurement1,
        )

        product2 = Products(
            name_product='Мыло "Не облезай"',
            specifications="200 гр.",
            description="Кусковое мыло белого цвета, без запаха",
            picture="https://opttorg-horeca.ru/assets/images/catalog/hoz-tovar/stiralnyj-poroshok-dosya-8-5kg.jpg",
            price_purchase=40,
            availability="в наличии",
            quantity=200,
            price_sale=48,
            procurements_=procurement2,
        )

        product3 = Products(
            name_product='Шампунь "Рискни не облысеть"',
            specifications="300 мл",
            description="Прозрачный, с запахом мха",
            picture="https://opttorg-horeca.ru/assets/images/catalog/hoz-tovar/stiralnyj-poroshok-dosya-8-5kg.jpg",
            price_purchase=400,
            availability="в наличии",
            quantity=15,
            price_sale=500,
            procurements_=procurement4,
        )

        product4 = Products(
            name_product='Средство для мытья посуды "Купи посудомойку"',
            specifications="400 мл",
            description="Прозрачного цвета, с запахом лимона",
            picture="https://opttorg-horeca.ru/assets/images/catalog/hoz-tovar/stiralnyj-poroshok-dosya-8-5kg.jpg",
            price_purchase=80,
            availability="в наличии",
            quantity=45,
            price_sale=90,
            procurements_=procurement5,
        )

        product5 = Products(
            name_product='Коврик для ванной "Не растянись"',
            specifications="1 х 1 м",
            description="Коврик нескользящий",
            picture="https://opttorg-horeca.ru/assets/images/catalog/hoz-tovar/stiralnyj-poroshok-dosya-8-5kg.jpg",
            price_purchase=350,
            availability="в наличии",
            quantity=10,
            price_sale=450,
            procurements_=procurement7,
        )

        product6 = Products(
            name_product='Кондиционер для белья "Без фанатизма"',
            specifications="500 мл",
            description="Средство белого цвета. Не вызывает аллергии",
            picture="https://opttorg-horeca.ru/assets/images/catalog/hoz-tovar/stiralnyj-poroshok-dosya-8-5kg.jpg",
            price_purchase=110,
            availability="в наличии",
            quantity=20,
            price_sale=150,
            procurements_=procurement6,
        )

        session.add_all([product1, product2, product3, product4, product5, product6])

        order1 = Orders(
            date_placement="2024-01-09",
            date_ex="2024-02-09",
            employee_=employee_4,
            products_=product1,
            clients_=client_10,
        )

        order2 = Orders(
            date_placement="2024-01-10",
            date_ex="2024-02-10",
            employee_=employee_4,
            products_=product6,
            clients_=client_9,
        )

        order3 = Orders(
            date_placement="2024-01-11",
            date_ex="2024-02-11",
            employee_=employee_4,
            products_=product5,
            clients_=client_8,
        )

        order4 = Orders(
            date_placement="2024-01-12",
            date_ex="2024-02-12",
            employee_=employee_2,
            products_=product4,
            clients_=client_7,
        )

        order5 = Orders(
            date_placement="2024-01-13",
            date_ex="2024-02-13",
            employee_=employee_4,
            products_=product3,
            clients_=client_6,
        )

        order6 = Orders(
            date_placement="2024-01-14",
            date_ex="2024-02-14",
            employee_=employee_2,
            products_=product2,
            clients_=client_5,
        )

        order7 = Orders(
            date_placement="2024-01-15",
            date_ex="2024-02-15",
            employee_=employee_2,
            products_=product6,
            clients_=client_4,
        )

        order8 = Orders(
            date_placement="2024-01-16",
            date_ex="2024-02-16",
            employee_=employee_4,
            products_=product6,
            clients_=client_1,
        )

        session.add_all(
            [order1, order2, order3, order4, order5, order6, order7, order8]
        )
        session.commit()


def select_table():
    with session_() as session:
        id_provider = 1
        # # Получаем ОДНОГО поставщика
        provider1 = session.get(Provider, id_provider)
        # Получаем всех поставщиков
        query = select(Provider)  # SELECT * FROM Provider
        result = session.execute(query)
        providers = result.all()

        print(f"{providers=}")


def update_table(
    client_id: int = 1, new_adress: str = "Санкт-Петербург, ул. Елизарова, д.15"
):
    with session_() as session:
        client_1 = session.get(Clients, client_id)
        client_1.address_client = new_adress
        # Сбросить все изменения
        # session.expire_all()
        # Обновить данные (Забирает последнее обновление из базы данных)
        # session.refresh(client_1)
        session.commit()


def update_table_1():
    with session_() as session:
        client_2 = session.get(Clients, 2)
        client_2.address_client = "г. Санкт-Петербург, ул. Крупской, д. 2"

        client_3 = session.get(Clients, 3)
        client_3.address_client = "г. Санкт-Петербург, проспект Обуховской Обороны, 82"

        client_4 = session.get(Clients, 4)
        client_4.address_client = "г. Санкт-Петербург, ул. Седова, д. 13"

        clients_new = session.query(Clients).filter(Clients.address_client == None)
        clients_new.update({Clients.address_client: "Санкт-Петербург"})

        session.commit()


def select_from_products(like_productname: str = "бел"):
    """Средняя стоимость закупки товара"""
    with session_() as session:
        query = (
            select(
                Products.name_product,
                cast(func.avg(Products.price_purchase), Integer).label("avg_price"),
            )
            .select_from(Products)
            .filter(
                and_(
                    Products.quantity > 3,
                    Products.description.contains(like_productname),
                )
            )
            .group_by(Products.name_product)
            .having(cast(func.avg(Products.price_purchase), Integer) > 100)
        )
        print(query.compile(compile_kwargs={"literal_binds": True}))
        res = session.execute(query)
        result = res.all()
        print(result[0].avg_price)


def select_from_products_1():
    with session_() as session:
        # query_1 = session.query(Products).filter(Products.price_sale == 700).order_by(Products.price_sale)
        # # res_1 = session.execute(query_1)
        # result_1 = res_1.all()
        # print(query_1.all())
        query = (
            select(Products.name_product, Products.price_purchase, Products.price_sale)
            .select_from(Products)
            .filter(Products.price_sale > 100)
            .order_by(Products.price_sale)
        )
        result = session.execute(query)
        print(result.all())


def select_with_join():
    """Объединение таблиц"""
    with session_() as session:
        query = (
            select(Products.name_product, Products.description, Procurement.date_procur)
            .select_from(Products)
            .join(Procurement)
        )

        result = session.execute(query)
        # заголовки столбцов
        # titles = Products.__table__.columns.keys()
        print("Название", " " * 42, "Описание", " " * 42, "Дата поставки")

        for res in result:
            name = "{:<50}||".format(res.name_product)
            date_ = res.date_procur
            desc = "{:<50}||".format(res.description)

            print(name, desc, date_)


def select_with_allias():
    with session_() as session:
        pr = aliased(Products)
        pc = aliased(Procurement)
        prov = aliased(Provider)
        query = (
            select(
                pr.name_product,
                pc.id_procurement,
                prov.name_provider,
            )
            .select_from(Products)
            # full=True isouter=True
            .join(pc)
            .join(prov)
            .order_by(desc(prov.name_provider))
            .limit(5)
        )

        results = session.execute(query)
        # print(results.scalar())
        print(results.all())


def diff_date():
    with session_() as session:
        query = (
            select(
                Products.name_product,
                Orders.date_placement,
                Orders.date_ex,
                (Orders.date_ex - Orders.date_placement).label("diff_date"),
            )
            .select_from(Orders)
            .join(Products)
            .order_by(Products.name_product)
        )

        result = session.execute(query)
        # print(result.all())
        print(
            "Название",
            " " * 42,
            "Дата разм.",
            " " * 3,
            "Дата исп.",
            " " * 3,
            "Макс. кол-во дней на исполнение",
        )

        for res in result:
            name = "{:<50}||".format(res.name_product)
            date_placement = res.date_placement
            date_ex = res.date_ex
            dif_date = res.diff_date

            print(name, date_placement, "||", date_ex, "||", dif_date)


def select_with_agr():
    with session_() as session:
        query = (
            select(
                Products.name_product,
                Products.price_purchase,
                Products.price_sale,
                func.sum(Products.price_sale - Products.price_purchase).label(
                    "price_profit"
                ),
            )
            .select_from(Products)
            .where(Products.price_purchase > 50)
            .group_by(
                Products.name_product, Products.price_purchase, Products.price_sale
            )
            .order_by(asc(Products.price_sale))
        )

        result = session.execute(query)
        print(
            "Название товара",
            " " * 34,
            "Стоимость закупки",
            "Стоимость продажи",
            "Прибыль",
        )

        for res in result:
            name = "{:<50}||".format(res.name_product)
            price_pursh = "{:<15}||".format(res.price_purchase)
            price_sal = "{:<15}||".format(res.price_sale)
            prise_prof = res.price_profit

            print(name, price_pursh, price_sal, prise_prof)


def select_with_distinct():
    with session_() as session:
        query = (
            select(
                distinct(Employees.surname_employee), Orders.id_order, Orders.id_empl
            )
            .select_from(Employees)
            .join(Orders)
            .filter(Orders.id_prod != 6)
            .limit(2)
        )

        result = session.execute(query)
        print(result.all())


def delete_for_provider():
    with session_() as session:
        query = (
            session.query(Provider).filter(Provider.address_prov == "Москва").delete()
        )

        session.commit()


def select_with_relationship():
    with session_() as session:
        query = select(Orders).options(selectinload(Orders.employee_))
        # query = (select(Orders, Employees.id_employee).join(Employees, isouter=True))
        engine.echo = False

        result = session.execute(query)
        # res = result.all()
        # print(result.all())
        res = result.scalars()

        # заголовки
        columns = Orders.__table__.columns.keys()
        columns[0], columns[1], columns[2], columns[3], columns[4], columns[5] = (
            "Код заказчика",
            "Код сотрудника",
            "Код поставки",
            "Дата размещения",
            "Дата отправки",
            "Код клиента",
        )

        print(f" {' -- '.join(columns)} -- Отв. сотрудник")

        for r in res:
            id_order = "{:<15}||".format(r.id_order)
            id_empl = "{:<15}||".format(r.id_empl)
            id_prod = "{:<15}||".format(r.id_prod)
            id_cl = "{:<10}".format(r.id_cl)

            print(
                id_order,
                id_empl,
                id_prod,
                r.date_placement,
                " " * 4,
                "||",
                r.date_ex,
                " " * 2,
                "||",
                id_cl,
                r.employee_.surname_employee,
            )


def select_with_joinedload():
    with session_() as session:
        query = (
            select(Orders).options(joinedload(Orders.employee_))
            # .selectinload(Employees.surname_employee))
            .order_by(Orders.id_order)
        )

        result = session.execute(query)
        res = result.scalars()

        for r in res:
            print(r.id_order, r.employee_.surname_employee)



