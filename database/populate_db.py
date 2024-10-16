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
