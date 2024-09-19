import pytest
from database.query import *


# Test para obtener los datos de maestros por apellido
def test_get_maestros_data_by_apellido():
    df = get_maestros_data_by_apellido("Rodriguez")  # Obtener los datos del maestro
    if not df.empty:
        nombre = df["NOMBRE"].values[
            0
        ]  # Obtener nombre del primer maestro en el Data Frame
        assert isinstance(nombre, str)  # Verificar que el "nombre" sea string
        assert nombre == "Marta"
    else:
        print("No se encontraron datos.")


# Test para obtener datos de alumnos por ID de materia
def test_get_alumnos_data_by_materia_id():
    df = get_alumnos_data_by_materia_id(1)

    if not df.empty:
        alumno = df["ALUMNO"].values[0]
        assert isinstance(alumno, str)
        assert alumno == "Juan"
    else:
        print("No se encontraron datos.")


# Test para obtener datos de maestros por ID de materia
def test_get_maestros_by_materia_id():
    df = get_maestros_by_materia_id(1)

    if not df.empty:
        nombre = df["NOMBRE"].values[0]
        assert isinstance(nombre, str)
        assert nombre == "Marta"
    else:
        print("No se encontraron datos.")


# Test para obtener el promedio de calificaciones por ID de alumno
def test_get_average_calificacion_by_alumno_id():
    promedio = get_average_calificacion_by_alumno_id(1)
    print(promedio)

    if promedio is not None:
        assert isinstance(
            promedio, (int, float)
        )  # Revisar si promedio es un int o float
        assert promedio == 8.0
    else:
        print("No se encontraron datos o no se calculó el promedio.")


# Test para obtener materias por ID de maestro
def test_get_materias_by_maestro_id():
    df = get_materias_by_maestro_id(1)

    if not df.empty:
        materia = df["NOMBRE"].values[0]
        assert isinstance(materia, str)
        assert materia == "Matematicas"
    else:
        print("No se encontraron datos.")


# Test para contar alumnos por ID de maestro
def test_count_alumnos_by_maestro_id():
    df = count_alumnos_by_maestro_id(1)

    if not df.empty:
        count = df["Count"].values[0]
        assert isinstance(count, int)
        assert count == 2
    else:
        print("No se encontraron datos.")


# Test para obtener las tareas por ID de alumno
def test_get_tareas_by_alumno_id():
    df = get_tareas_by_alumno_id(1)

    if not df.empty:
        tareas = df["DESCRIPCION"].tolist()
        print("Tareas encontradas:")
        for tarea in tareas:
            print(f"- {tarea}")
    else:
        print("No se encontraron datos.")


# Test para obtener alumnos por materia, ordenados por apellido y nombre
def test_get_alumnos_by_materia_ordered_by_apellido_nombre():
    df = get_alumnos_by_materia_ordered_by_apellido_nombre()

    if not df.empty:
        apellidos = df["APELLIDO"].tolist()  # Obtener lista de apellidos
        nombres = df["NOMBRE"].tolist()  # Obtener lista de nombres

        print(
            f"Alumnos en la materia con ID {materia_id} ordenados por APELLIDO y NOMBRE:"
        )
        for apellido, nombre in zip(apellidos, nombres):  # Imprimir alumnos en tuplas
            print(f"{apellido}, {nombre}")

        assert isinstance(apellidos, list)  # Asegurar que apellidos sea una lista
        assert isinstance(nombres, list)
    else:
        print("No se encontraron datos.")
