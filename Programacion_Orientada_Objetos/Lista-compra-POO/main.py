import functions
import Conection
from functions import txt_to_pdf
from functions import envio_archivo, escribir_archivo
import io
import os

def MenuPrincipal():
    conectar = Conection.DAO()

    while True:
        print('***** MENÚ PRINCIPAL *****')
        print('1.- Añadir producto\n'
              '2.- Listar productos\n'
              '3.- Modificar producto\n'
              '4.- Eliminar producto\n'
              '5.- Crear documento de la lista\n'
              '6.- Enviar documento por email\n'
              '7.- Salir\n')

        opcion = int(input('Selecciona una opción: '))

        if opcion > 0 and opcion < 8:

            if opcion == 1:
                datos_lista = functions.agrega()
                try:
                    conectar.agregar(datos_lista)
                except:
                    print('** Error al agregar el producto **\n')

            elif opcion == 2:
                try:
                    lista_compra = conectar.listarProductos()
                    if len(lista_compra) > 0:
                        functions.listar(lista_compra)
                    else:
                        print('** La lista está vacía **\n')
                except:
                    print('** No se ha podido ejecutar la consulta\n **')

            elif opcion == 3:
                try:
                    producto = conectar.listarProductos()
                    if len(producto) > 0:
                        codigoProducto = functions.modificar(producto)
                        if codigoProducto:
                            conectar.modificarProducto(codigoProducto)
                        else:
                            print('** No se encuentran productos con el código proporcionado **\n')
                    else:
                        print('** No existen productos **\n')
                except:
                    print('** Error except Main **\n')

            elif opcion == 4:
                try:
                    productos = conectar.listarProductos()
                    if len(productos) > 0:
                        dato_eliminar = functions.eliminar(productos)
                        print(f'Dato a eliminar -->  {dato_eliminar}')
                        if not(dato_eliminar == ""):
                            conectar.eliminarProducto(dato_eliminar)
                        else:
                            print('** Código del curso no encontrado o vacío **\n')
                    else:
                        print('** No hay coinciden registros para eliminar **\n')
                except:
                      print('** Error except Main **\n')
                      
            elif opcion == 5:
                try:
                    productos = conectar.listarProductos()
                    if len(productos) > 0:
                        escribir_archivo(productos)  # Paso lista a documento .txt
                        ruta = r'C:\Users\jgome\OneDrive\Escritorio\Lista_compra POO\Archivos'
                        
                        txt_file = os.path.join(ruta, 'Lista de la compra.txt') #Variable necesaria para transformación a pdf
                        pdf_file = os.path.join(ruta, 'Lista de la compra.pdf') #Variable necesaria para transformación a pdf
                        txt_to_pdf(txt_file, pdf_file) #Transformo arhivo a pdf
                    else:
                        print('** Error. La lista de la comprar está vacía. Seleccione la opción 1 para añadir productos **\n')
                except:
                    print('** Error al pasar la lista a un documento **\n')
                   
            
            elif opcion == 6:
                try:
                    envio = envio_archivo()
                    envio
                except:
                    print('** Error al enviar archivo. ERROR --> No se encuentra el archivo\n')
                    
            else:
                print('** Programa cerrado **')
                break

        else:
            print('** Opción no válida. Seleccione una opción entre 1 y 7 **')

MenuPrincipal()