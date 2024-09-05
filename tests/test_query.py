import pytest
from database.query import get_maestros_data_by_apellido


def test_query():
    df = get_maestros_data_by_apellido("Rodriguez")
    nombre = df["NOMBRE"].value[0]

    assert isinstance(nombre, str)
    assert nombre == "Marta"
