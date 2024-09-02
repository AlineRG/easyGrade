import sqlite3
import pandas as pd

# Establish the connection once
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
    df = pd.DataFrame(result_data)
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

