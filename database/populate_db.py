import pandas as pd
import sqlite3


conn = sqlite3.connect("instance/easyGrade.db")

# try:
#     df_alumnos = pd.read_csv(
#         "C:/Users/prin_/OneDrive/Documentos/easyGrade/database/csv_files/ALUMNOS.csv"
#     )
#     df_alumnos.to_sql("ALUMNOS", conn, if_exists="append", index=False)
#     print("Se han cargado los datos de ALUMNOS.csv correctamente")
# except Exception as error:
#     print("No se han cargado los datos de ALUMNOS.csv correctamente:", error)

# try:
#     df = pd.read_csv(
#         "C:/Users/prin_/OneDrive/Documentos/easyGrade/database/csv_files/CALIFICACIONES_EJERCICIOS.csv"
#     )
#     df.to_sql("CALIFICACIONES_EJERCICIOS", conn, if_exists="append", index=False)
#     print("Se han cargado los datos de CALIFICACIONES_EJERCICIOS.csv correctamente")
# except Exception as error:
#     print(
#         "No se han cargado los datos de CALIFICACIONES_EJERCICIOS.csv correctamente:",
#         error,
#     )

# try:
#     df = pd.read_csv(
#         "C:/Users/prin_/OneDrive/Documentos/easyGrade/database/csv_files/CALIFICACIONES_EXAMENES.csv"
#     )
#     df.to_sql("CALIFICACIONES_EXAMENES", conn, if_exists="append", index=False)
#     print("Se han cargado los datos de CALIFICACIONES_EXAMENES.csv correctamente")
# except Exception as error:
#     print(
#         "No se han cargado los datos de CALIFICACIONES_EXAMENES.csv correctamente:",
#         error,
#     )


# try:
#     df = pd.read_csv(
#         "C:/Users/prin_/OneDrive/Documentos/easyGrade/database/csv_files/CALIFICACIONES_MATERIA.csv"
#     )
#     df.to_sql("CALIFICACIONES_MATERIA", conn, if_exists="append", index=False)
#     print("Se han cargado los datos de CALIFICACIONES_MATERIA.csv correctamente")
# except Exception as error:
#     print(
#         "No se han cargado los datos de CALIFICACIONES_MATERIA.csv correctamente:",
#         error,
#     )


# try:
#     df = pd.read_csv(
#         "C:/Users/prin_/OneDrive/Documentos/easyGrade/database/csv_files/CALIFICACIONES_TAREAS.csv"
#     )
#     df.to_sql("CALIFICACIONES_TAREAS", conn, if_exists="append", index=False)
#     print("Se han cargado los datos de CALIFICACIONES_TAREAS.csv correctamente")
# except Exception as error:
#     print(
#         "No se han cargado los datos de CALIFICACIONES_TAREAS.csv correctamente:",
#         error,
#     )

# try:
#     df = pd.read_csv(
#         "C:/Users/prin_/OneDrive/Documentos/easyGrade/database/csv_files/CONTACTO.csv"
#     )
#     df.to_sql("CONTACTO", conn, if_exists="append", index=False)
#     print("Se han cargado los datos de CONTACTO.csv correctamente")
# except Exception as error:
#     print(
#         "No se han cargado los datos de CONTACTO.csv correctamente:",
#         error,
#     )


# try:
#     df = pd.read_csv(
#         "C:/Users/prin_/OneDrive/Documentos/easyGrade/database/csv_files/MAESTROS.csv"
#     )
#     df.to_sql("MAESTROS", conn, if_exists="append", index=False)
#     print("Se han cargado los datos de MAESTROS.csv correctamente")
# except Exception as error:
#     print(
#         "No se han cargado los datos de MAESTROS.csv correctamente:",
#         error,
#     )

# try:
#     df = pd.read_csv(
#         "C:/Users/prin_/OneDrive/Documentos/easyGrade/database/csv_files/MATERIAS.csv"
#     )
#     df.to_sql("MATERIAS", conn, if_exists="append", index=False)
#     print("Se han cargado los datos de MATERIAS.csv correctamente")
# except Exception as error:
#     print(
#         "No se han cargado los datos de MATERIAS.csv correctamente:",
#         error,
#     )

# try:
#     df = pd.read_csv(
#         "C:/Users/prin_/OneDrive/Documentos/easyGrade/database/csv_files/REGISTRO_MATERIAS_ALUMNOS.csv"
#     )
#     df.to_sql("REGISTRO_MATERIAS_ALUMNOS", conn, if_exists="append", index=False)
#     print("Se han cargado los datos de REGISTRO_MATERIAS_ALUMNOS.csv correctamente")
# except Exception as error:
#     print(
#         "No se han cargado los datos de REGISTRO_MATERIAS_ALUMNOS.csv correctamente:",
#         error,
#     )

# try:
#     df = pd.read_csv(
#         "C:/Users/prin_/OneDrive/Documentos/easyGrade/database/csv_files/REGISTRO_MATERIAS_MAESTROS.csv"
#     )
#     df.to_sql("REGISTRO_MATERIAS_MAESTROS", conn, if_exists="append", index=False)
#     print("Se han cargado los datos de REGISTRO_MATERIAS_MAESTROS.csv correctamente")
# except Exception as error:
#     print(
#         "No se han cargado los datos de REGISTRO_MATERIAS_MAESTROS.csv correctamente:",
#         error,
#     )

try:
    df = pd.read_csv(
        "C:/Users/prin_/OneDrive/Documentos/easyGrade/database/csv_files/TAREAS.csv"
    )
    df.to_sql("TAREAS", conn, if_exists="fail", index=False)
    print("Se han cargado los datos de TAREAS.csv correctamente")
except Exception as error:
    print(
        "No se han cargado los datos de TAREAS.csv correctamente:",
        error,
    )
