from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
from datetime import date

app = FastAPI()

class Movie(BaseModel):
    table: str
    Autor: str
    Descripcion: str
    FechadeEstreno: str
# Revisar en su cmd ipconfig si es windows e ifconfig linux o mac mirar su ipv4 ya sea de su adaptador wifi o ethernet dependiendo del caso.
# En caso de no ser igual al host reemplzarlo por el de su máquina
db_params = {
    'host': '172.27.0.1',
    'user': 'root',
    'password': 'root',
    'database': 'my_collections',
}

conn = mysql.connector.connect(**db_params)

# Solicitud get para ver todos los items de la tabla
@app.get('/movie')
def get_movie():

    temporal_list = []

    with conn.cursor() as cursor:
        
        try:
            get_data_query = '''
            SELECT * FROM my_movies
            '''
            cursor.execute(get_data_query)

            rows = cursor.fetchall()
            for row in rows:
                print(row)
                temporal_list.append(row)
        except:
            print("Error con la consulta GET")

    return {"message": temporal_list}


# Solicitud get para ver un item segun su id, que se ingresa como query
@app.get('/movie/{ID}')
def get_movie(ID:int):

    temporal_list = []

    with conn.cursor() as cursor:
        
        try:
            get_data_query = f'''
            SELECT * FROM my_movies WHERE ID = {ID}
            '''
            cursor.execute(get_data_query)

            rows = cursor.fetchall()
            for row in rows:
                print(row)
                temporal_list.append(row)
        except:
            print("Error con la consulta GET")

    return {"message": temporal_list}


# Solicitud post para ingresar una pelicula a la base de datos
@app.post('/movie')
def create_task(datos:Movie):
    with conn.cursor() as cursor:
        
        try:
            post_data_query = f'''
            INSERT INTO {datos.table} (Autor, Descripcion, FechadeEstreno) VALUES (%s, %s, %s);
            '''
            data_to_insert = (datos.Autor, datos.Descripcion, datos.FechadeEstreno)
            cursor.execute(post_data_query,data_to_insert)
            conn.commit()
        except:
            print("Error con el POST")

    return {"message": "BIen"}

# Actualizar las peliculas dando la id y los atributos y valores que se quieran actualizar, se puede mandar uno o dos si se quiere o todos los que se quieran actualizar
@app.put('/movie')
def put_movie(datos: dict):
    with conn.cursor() as cursor:
        try:
            # Construir la consulta UPDATE y la tupla de datos
            query = f"UPDATE {datos['table']} SET"
            data = []

            # Obtener el ID de la movie a actualizar
            tarea_id = datos.get('ID')

            for attr, value in datos.items():
                if attr not in ['ID', 'table']:
                    # Agregar el nombre de la columna y el nuevo valor a la consulta y los datos
                    query += f" {attr} = %s,"
                    data.append(value)

            # Eliminar la última coma y agregar la condición WHERE para el ID
            query = query.rstrip(',') + f" WHERE ID = %s;"
            data.append(tarea_id)

            # Ejecutar la consulta
            cursor.execute(query, data)
            conn.commit()
        except Exception as e:
            print(f"Error en la consulta: {e}")

    return {"message": "OK"}

#Solicitud delete para borrar algun item segun su id
@app.delete('/movie/{ID}')
def delete_movie(ID:int):
    with conn.cursor() as cursor:
        try:
            query = f'DELETE FROM my_movies WHERE ID = {ID};'
            cursor.execute(query)
            conn.commit()
        except:
            print("Error al borrar")

    return {"message": "Borrado"}

