#Importando librerías para conexión MySQL:
import mysql.connector
from mysql.connector.errors import Error

class DAO():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = '*******',
                port = '****',
                user = '*****',
                password = '********',
                db = 'lista_compra'
            )
            print ('\n** Contectado a la base de datos correctamente **\n')
        except Error as ex:
            print(f'\n** Error al conectar con la base de datos. Código--> {ex} **\n')
            

    #Método mágico para listar los prodcutos de la base de datos:
    def __str__(self):
        datos = self.consulta_productos()
        if datos is None:
            return 'No hay productos en la lista'
        aux =''
        for row in datos:
            aux = aux + str(row) + '\n'
        return aux
    
    #Método para consultar productos en la base de datos:
    def consulta_productos(self):
        cursor = self.conexion.cursor()
        cursor.execute('SELECT * FROM lista ORDER BY supermercado, seccion ASC')
        datos = cursor.fetchall()
        cursor.close()
        return datos
    
    #Método para insertar/añadir producto a la base de datos:
    def insertar_producto (self, supermercado, seccion, codigo, producto, cantidad):
        cursor = self.conexion.cursor()
        sql = 'INSERT INTO lista (supermercado, seccion, codigo, producto, cantidad) VALUES (%s, %s, %s, %s, %s)'
        values = (supermercado, seccion, codigo, producto, cantidad)
        cursor.execute(sql, values)
        n = cursor.rowcount #Con esta línea asigno a 'n' el número de filas afectadas por la insercción, que será 1
        self.conexion.commit()
        cursor.close()
        return n #Devolverá 1
    
    #Método para eliminar productos de la base de datos:
    def eliminar_producto(self, codigo):
        cursor = self.conexion.cursor()
        sql = (f'DELETE FROM lista WHERE codigo = {codigo}')
        cursor.execute(sql)
        n = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return n
    
    #Método para modificar productos de la base de datos:
    def modificar_producto(self, supermercado, seccion, producto, cantidad, codigo):
        cursor = self.conexion.cursor()
        sql = 'UPDATE lista SET supermercado=%s, seccion=%s, producto=%s, cantidad=%s WHERE codigo=%s'
        values = (supermercado, seccion, producto, cantidad, codigo)
        cursor.execute(sql, values)
        n = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return n            