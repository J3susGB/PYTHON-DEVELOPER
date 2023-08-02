# En este arhivo incluiré las  funciones para el menú:

# 1: Lo primero es importar las funciones para el menú:
from conexion import DAO #Con esta se importa la clase DAO
import conexion
import funciones

# 2: Creo una función que se llama Menú principal:
def MenuPrincipal():
    conectar = DAO()
    while True:
        print('***** MENÚ PRINCIPAL *****')
        print('1.- Listar Clientes\n'
              '2.- Registrar cliente\n'
              '3.- Actualizar cliente\n'
              '4.- Borrar cliente\n'
              '5.- Salir\n')
        
        opcion = int(input('Selecciona una opción: '))
        
        if opcion > 0 and opcion < 6:
            if opcion == 1:
                try:
                    clientes = conectar.ListarClientes()
                    if len(clientes) > 0:
                        funciones.listar(clientes)
                    else:
                        print('No existen registros')
                except:
                    print('No se ha podido ejecutar la consulta')
                        
            elif opcion == 2:
                datos_curso = funciones.DatosClientes()
                print(f'Estos son los datos a registrar: {datos_curso}')
                try:
                    conectar.registarClientes(datos_curso)
                except:
                    print('No se ha podio agregar el cliente')
                
            elif opcion == 3:
                try:
                    clientes = conectar.ListarClientes()
                    if len(clientes) > 0:
                        codigoCliente = funciones.DatosClientesActualizar(clientes)
                        print(f'Código cliente: {codigoCliente}')
                        if codigoCliente:
                            conectar.actualizarClientes(codigoCliente)
                        else:
                            print('** Código de cliente no encontrado **')
                    else:
                        print('No hay clientes')
                except:
                    print('Error Except Master')
            
            elif opcion == 4:
                try:
                    clientes=conectar.ListarClientes()  #muestra clientes
                    if len(clientes) > 0:
                        dato_eliminar=funciones.registroEliminar(clientes)
                        print(f"Dato a Eliminar --> {dato_eliminar}")
                        if not(dato_eliminar == ""):  #Si no es Vacio 
                            conectar.EliminarCurso(dato_eliminar)
                        else:
                            print('** Código del curso no encontrado o vacío **')
                    else:
                        print('No hay coinciden registros para eliminar')
                except:
                    print('Error Except Master')
            
            elif opcion == 5:
                print('Programa cerrado')
                break
                
        else:
            print('Opción incorrecta. Introduce una opción entre el 1 y el 5')
                
# Llamo a la función MenuPrincipal para ir probando:
MenuPrincipal()