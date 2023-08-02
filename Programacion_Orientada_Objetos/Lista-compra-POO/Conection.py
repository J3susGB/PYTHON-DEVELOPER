# Importando librerías necesarias:
import mysql.connector
from mysql.connector import Error

# Creo una nueva clase que se llamará DAO:

class DAO():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = '*******',
                port = '****,',
                user = '*****',
                password = '*******',
                db = 'lista_compra'
            )
            print('\n*** Conectado a la base de datos correctamente ***\n')
            
        except Error as ex:
            print(f'\n** Error al conectar con la base de datos. Except: {ex} **\n')
            
    # Creo una función para agregar producto a la lista:
    def agregar (self, productos):
        if self.conexion.is_connected():
            try:
                producto = self.conexion.cursor()
                sql="INSERT INTO lista (supermercado, seccion, codigo, producto , cantidad) VALUES (%s,%s,%s,%s,%s)"
                producto.execute(sql, productos)
                self.conexion.commit() #Ejecuta el código
                print('** Procudto añadido correctamente correctamente **') 
            except Error as ex:
                print(f'** Error al añadir producto- Código de error {ex} **')
                
    # Creo función para previsualizar la  lista:
    def listarProductos(self):
        if self.conexion.is_connected:
            try:
                producto = self.conexion.cursor()
                producto.execute("SELECT * FROM lista ORDER BY supermercado, seccion ASC")
                resultados = producto.fetchall()
                return resultados
            except Error as ex:
                print(f'** No se pudo hacer la consulta. Except --> {ex}')
                
    # Creo función para modificar producto de la  lista:
    def modificarProducto(self,datos):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE lista SET supermercado = %s, seccion = %s, producto = %s, cantidad = %s WHERE codigo = %s"
                cursor.execute(sql,datos)
                self.conexion.commit()
                print('** Registro actualizado correctamente **\n')
            except Error as ex:
                print(f'No se pudo actualizar el regstro. Código de error: {ex}\n')
    
    # Creo función para eliminar productos:
    def eliminarProducto(self, producto_eliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM lista WHERE codigo = %s"
                cursor.execute(sql, (producto_eliminar,))
                self.conexion.commit()
                print('** Registro eliminado correctamente **\n')
            except Error as ex:
                print(f'No se pudo eliminar. Except Conexion {ex}')      