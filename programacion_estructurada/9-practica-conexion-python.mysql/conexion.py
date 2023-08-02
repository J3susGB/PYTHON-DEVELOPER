# En este archivo irá todo lo relacionado con base de datos MySQL

import mysql.connector
from mysql.connector import Error

# 3: Conectando con MySQL (usando POO):

# Creo una clase llamada DAO, que contentrá como constructor la conexión a la base de datos, todo dentro de un try - except, 
# por si da algún error, que lo capture y no se paralice la ejecución:
class DAO():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = '*******',
                password = '*******',
                db = '********'
            )
            print('\n*** Conexión realizada correctamente ***\n')
            
        except Error as ex:
            print(f'\n *** No ha sido posible establecer la conexión con la base de datos. Error {ex} ***\n')
    
    # Creo función dentro de la clase para listar los clientes:
    def ListarClientes(self):
        if self.conexion.is_connected(): # Para condicionar a estar conectado a la db
            try:
                cliente = self.conexion.cursor() # cursor conecta y asigna el valor a la variable cliente
                cliente.execute("SELECT * FROM clientes ORDER BY codigo ASC")
                resultados = cliente.fetchall() #fetchall guarda los datos en una lista, tupla...
                return resultados
            except Error as ex:
                print(f'** No se pudo hacer la consulta. Except --> {ex}')
    
    # Creo función dentro de la clase para registrar cliente:
    def registarClientes(self, curso):
        if self.conexion.is_connected():
            try:
                cliente = self.conexion.cursor()
                sql="INSERT INTO clientes (codigo,nombre,apellido1,apellido2,creditos) VALUES (%s,%s,%s,%s,%s)"
                cliente.execute(sql, curso)
                self.conexion.commit() #Ejecuta el código
                print('** Registro guardado correctamente **')
            except Error as ex:
                print(f'** No se pudo hacer el registro. Except --> {ex}')
    
    # Creo función dentro de la clase para modificar datos del cliente:
    def actualizarClientes(self, clientes):
        if self.conexion.is_connected(): # Para condicionar a estar conectado a la db
            try:
                cliente = self.conexion.cursor() # cursor conecta y asigna el valor a la variable cliente
                sql = "UPDATE clientes SET nombre = %s, apellido1 = %s, apellido2 = %s, creditos = %s WHERE codigo = %s"
                cliente.execute(sql, clientes)
                self.conexion.commit() #Ejecuta el código
                print('** Registro actualizado correctamente **')
            except Error as ex:
                print(f'** No se pudo actualizar el registro. Except --> {ex}')        
    
    # Creo una función para eliminar clientes:
    def EliminarCurso(self, curso_eliminar):
        if self.conexion.is_connected():
            try:
                cliente = self.conexion.cursor()
                print(f'llego a conexión {curso_eliminar}')
                sql = f"DELETE FROM clientes WHERE codigo = {curso_eliminar}"
                cliente.execute(sql)
                self.conexion.commit()
                print('Registro eliminado correctamente')
            except Error as ex:
                print(f'No se pudo eliminar. Except Conexion {ex}')