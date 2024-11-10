import pytest
from src.models.sqlite.settings.connection import SqliteConnectionHandle
from src.models.sqlite.repository.products_repository import ProductsRepository

conn_handle = SqliteConnectionHandle()
conn = conn_handle.connect()


@pytest.mark.skip(reason="interaction with the database")
def test_insert_product():
    repo = ProductsRepository(conn)

    name = "something"
    price = 12.34
    quantity = 8

    repo.insert_product(name, price, quantity)


@pytest.mark.skip(reason="interaction with the database")
def test_find_product():
    repo = ProductsRepository(conn)

    name = "something"
    response = repo.find_product_by_name(name)
    print(response)
    print(type(response))
