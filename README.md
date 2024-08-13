# EasyGrade
Este repositorio que contiene la informacion para una pagina web para maestros

# Table of Contents
1. [Description](#Description)
2. [Characteristics](#Characteristics)
3. [Previous_requirements](#Previous_requirements)
4. [Installation](#Installation)
5. [Usage](#Usage)
6. [Contributing](#Contributing)


# Description

EasyGrade is a platform designed to simplify academic management for teachers. It allows users to register student information, manage grades and evaluations, and provides an intuitive interface to facilitate daily use in educational environments. 

# Characteristics

## User Registration:
Allows teachers and students to register with a unique username and email.
## Grades and Evaluations:
Allows teachers to record and manage student grades and evaluations.

# Previous_requirements

- Python 3.6 or higher installed on the system.
- Flask framework installed and configured.
- Access to a compatible database (e.g., SQLite).
- Basic knowledge of HTML and CSS to customize the user interface, if necessary.

# Installation

Follow these steps to install and set up EasyGrade on your local system:
1. Clone the repository to your local system using the following command:
```bash
   git clone https://github.com/AlineRG/easyGrade
   cd easygrade
```
2. Create a virtual environment 
3. Install dependencies:
    pip install -r requirements.txt
4. Run the application
    flask --app myapp/app.py run
5. Access EasyGrade


# Usage
## Running the Application

1. Ensure that EasyGrade is installed and configured as per the [Installation](#installation) instructions.
2. Start the Flask application:

   ```bash
   flask --app myapp/app.py run

3. User Registration:
- To register as a teacher, navigate to the "Register" page and enter your details.
- To register as a student, navigate to the "Register" page and enter your details.

4. login 
- Navigate to the "Login" page and enter your username and password to access the application.

# Database 

1. Import modules 
import sqlite3
import os

2. Conexion and create the database file
conn = sqlite3.connect("instance/myDB.db")
print("Opened database successfully")

3. Create tables
Example
conn.execute(
    """CREATE TABLE MAESTROS
         (ID INTEGER PRIMARY KEY NOT NULL,
         NOMBRE VARCHAR NOT NULL,
         APELLIDO VARCHAR NOT NULL,
         TELEFONO VARCHAR,
         DIRECCION VARCHAR,
         CORREO_ELECTRONICO VARCHAR NOT NULL);"""
)
print("Table MAESTROS created successfully")

4. Run the file
When this file is executed, a database file named myDB.db is created in the instance directory. 



