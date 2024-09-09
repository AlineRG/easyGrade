import pytest
from database.query import *


def test_get_maestros_data_by_apellido():
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


def get_average_calificacion_by_alumno_id():
    df = get_average_calificacion_by_alumno_id(1)
    calificacion = df["CALIFICACION"].values[0]

    assert isinstance(calificacion, int)
    assert calificacion == 8


def get_materias_by_maestro_id():
    df = get_materias_by_maestro_id(1)
    materia = df["MATERIA"].values[0]

    assert isinstance(materia, str)
    assert materia == "Matematicas"


def count_alumnos_by_maestro_id():
    df = count_alumnos_by_maestro_id(1)
    alumnos = df["ALUMNOS"].values[0]

    assert isinstance(alumnos, int)
    assert alumnos == "2"


def get_tareas_by_alumno_id():
    df = get_tareas_by_alumno_id(1)
    tareas = df["TAREAS"].values[0]

    assert isinstance(tareas, str)
    assert tareas == "Tarea 1, Tarea 2"


def get_alumnos_ordered_by_apellido_nombre():
    df = get_alumnos_ordered_by_apellido_nombre()
    alumno = df["ALUMNO"].values[0]

    assert isinstance(alumno, str)
    assert alumno == "Ramirez"
