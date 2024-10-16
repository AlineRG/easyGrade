import pandas as pd
import sqlite3


conn = sqlite3.connect("instance/easyGrade.db")

try:
    df_alumnos = pd.read_csv(
        "C:/Users/prin_/OneDrive/Documentos/easyGrade/database/csv_files/ALUMNOS.csv"
    )
    df_alumnos.to_sql("ALUMNOS", conn, if_exists="fail", index=False)
    print("Se han cargado los datos de ALUMNOS.csv correctamente")
except Exception as error:
    print("No se han cargado los datos de ALUMNOS.csv correctamente:", error)

try:
    df = pd.read_csv(
        "C:/Users/prin_/OneDrive/Documentos/easyGrade/database/csv_files/CALIFICACIONES_EJERCICIOS.csv"
    )
    df.to_sql("CALIFICACIONES_EJERCICIOS", conn, if_exists="fail", index=False)
    print("Se han cargado los datos de CALIFICACIONES_EJERCICIOS.csv correctamente")
except Exception as error:
    print(
        "No se han cargado los datos de CALIFICACIONES_EJERCICIOS.csv correctamente:",
        error,
    )

try:
    df = pd.read_csv(
        "C:/Users/prin_/OneDrive/Documentos/easyGrade/database/csv_files/CALIFICACIONES_EXAMENES.csv"
    )
    df.to_sql("CALIFICACIONES_EXAMENES", conn, if_exists="fail", index=False)
    print("Se han cargado los datos de CALIFICACIONES_EXAMENES.csv correctamente")
except Exception as error:
    print(
        "No se han cargado los datos de CALIFICACIONES_EXAMENES.csv correctamente:",
        error,
    )
