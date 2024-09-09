import sqlite3
import pandas as pd

conn = sqlite3.connect("instance/easyGrade.db")


def get_maestros_data_by_apellido(apellido: str) -> pd.DataFrame:
    """
    This function queries the database and retrieves all the data from the table
    MAESTROS where APELLIDO == apellido.

    Args:
    * apellido : str. The apellido to query

    Returns:
    * df: pd.DataFrame. A table with all the data from the MAESTROS table
    where APELLIDO is equal to the variable apellido
    """
    query = f"SELECT * FROM MAESTROS WHERE APELLIDO = '{apellido}'"
    result = conn.execute(query)

    result_data = result.fetchall()
    columns = [description[0] for description in result.description]  # Get column names
    df = pd.DataFrame(result_data, columns=columns)
    return df


def get_alumnos_data_by_materia_id(materia_id: int) -> pd.DataFrame:
    """
    This function queries the database and retrieves all the data from the table
    ALUMNOS where MATERIA_ID == materia_id.

    Args:
    * materia_id : int. The MATERIA_ID to query

    Returns:
    * df: pd.DataFrame. A table with all the data from the ALUMNOS table
    where MATERIA_ID is equal to the variable materia_id
    """
    query = f"SELECT * FROM ALUMNOS WHERE MATERIA_ID = {materia_id}"
    result = conn.execute(query)

    result_data = result.fetchall()
    df = pd.DataFrame(result_data)
    return df


def get_maestros_by_materia_id(materia_id: int) -> pd.DataFrame:
    """
    This function queries the database and retrieves the NOMBRE and APELLIDO
    from the MAESTROS table for a specific MATERIA_ID.

    Args:
    * materia_id : int. The MATERIA_ID to query

    Returns:
    * df: pd.DataFrame. A table with NOMBRE and APELLIDO of MAESTROS
    who teach the specified MATERIA_ID
    """
    query = f"""
    SELECT MAESTROS.NOMBRE, MAESTROS.APELLIDO 
    FROM MAESTROS 
    JOIN MATERIAS ON MAESTROS.MATERIA_ID = MATERIAS.ID
    WHERE MATERIAS.ID = {materia_id};
    """
    result = conn.execute(query)

    result_data = result.fetchall()
    df = pd.DataFrame(result_data, columns=["NOMBRE", "APELLIDO"])
    return df


def get_average_calificacion_by_alumno_id(alumno_id: int) -> float:
    """
    This function queries the database to calculate the average CALIFICACION
    from the EXAMENES table for a specific ALUMNO_ID.

    Args:
    * alumno_id : int. The ALUMNO_ID to query

    Returns:
    * promedio: float. The average CALIFICACION for the given ALUMNO_ID
    """
    query = f"""
    SELECT AVG(CALIFICACION) AS Promedio 
    FROM EXAMENES 
    WHERE ALUMNO_ID = {alumno_id};
    """
    result = conn.execute(query)

    result_data = result.fetchall()
    df = pd.DataFrame(result_data, columns=["Promedio"])
    return df


def get_materias_by_maestro_id(maestro_id: int) -> pd.DataFrame:
    """
    This function queries the database and retrieves the NOMBRE of all
    subjects from the MATERIAS table where MAESTRO_ID == maestro_id.

    Args:
    * maestro_id : int. The MAESTRO_ID to query

    Returns:
    * df: pd.DataFrame. A table with the NOMBRE of subjects taught by the given MAESTRO_ID
    """
    query = f"""
    SELECT NOMBRE 
    FROM MATERIAS 
    WHERE MAESTRO_ID = {maestro_id};
    """
    result = conn.execute(query)

    result_data = result.fetchall()
    df = pd.DataFrame(result_data, columns=["NOMBRE"])
    return df


def count_alumnos_by_maestro_id(maestro_id: int) -> pd.DataFrame:
    """
    This function queries the database to count the number of ALUMNOS
    enrolled in subjects taught by a specific MAESTRO_ID.

    Args:
    * maestro_id : int. The MAESTRO_ID to query

    Returns:
    * df: pd.DataFrame. A table with the count of ALUMNOS for the given MAESTRO_ID
    """
    query = f"""
    SELECT COUNT(ALUMNOS.ALUMNO_ID) AS Count 
    FROM ALUMNOS 
    JOIN MATERIAS ON ALUMNOS.MATERIA_ID = MATERIAS.ID 
    WHERE MATERIAS.MAESTRO_ID = {maestro_id};
    """
    result = conn.execute(query)

    result_data = result.fetchall()
    columns = [description[0] for description in result.description]
    df = pd.DataFrame(result_data, columns=columns)
    return df


def get_tareas_by_alumno_id(alumno_id: int) -> pd.DataFrame:
    """
    This function queries the database and retrieves all the data from the TAREAS
    table where ALUMNO_ID == alumno_id.

    Args:
    * alumno_id : int. The ALUMNO_ID to query

    Returns:
    * df: pd.DataFrame. A table with all the data from the TAREAS table
    where ALUMNO_ID is equal to the variable alumno_id
    """
    query = f"""
    SELECT * 
    FROM TAREAS 
    WHERE ALUMNO_ID = {alumno_id};
    """
    result = conn.execute(query)

    result_data = result.fetchall()
    columns = [description[0] for description in result.description]
    df = pd.DataFrame(result_data, columns=columns)
    return df


def get_alumnos_by_materia_ordered_by_apellido_nombre(materia_id: int) -> pd.DataFrame:
    """
    This function queries the database to retrieve all data from the ALUMNOS
    table for a specific MATERIA_ID and orders the results by APELLIDO and then NOMBRE.

    Args:
    * materia_id : int. The MATERIA_ID to query

    Returns:
    * df: pd.DataFrame. A table with all the data from the ALUMNOS table
    ordered by APELLIDO and NOMBRE.
    """
    query = """
    SELECT * 
    FROM ALUMNOS 
    ORDER BY APELLIDO, NOMBRE;
    """
    result = conn.execute(query)

    result_data = result.fetchall()
    columns = [description[0] for description in result.description]
    df = pd.DataFrame(result_data, columns=columns)
    return df


# Close the connection after all operations
conn.close()
