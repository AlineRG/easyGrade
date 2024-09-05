import pytest
from database.query import get_maestros_data_by_apellido


def test_query():
    df = get_maestros_data_by_apellido("Rodriguez")
    nombre = df["NOMBRE"].values[0]

    assert isinstance(nombre, str)
    assert nombre == "Marta"


def get_alumnos_data_by_materia_id():
    df = get_alumnos_data_by_materia_id(1)
    alumno = df["ALUMNO"].values[0]

    assert isinstance(alumno, str)
    assert alumno == "Juan"


def get_maestros_by_materia_id():
    df = get_maestros_by_materia_id(1)
    maestro = df["MAESTRO"].values[0]

    assert isinstance(maestro, str)
    assert maestro == "Marta"

