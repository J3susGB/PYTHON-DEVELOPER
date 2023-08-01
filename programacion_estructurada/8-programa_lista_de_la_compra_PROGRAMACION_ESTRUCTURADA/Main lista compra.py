# El programa trata sobre una lista de la compra, donde se le pedirá al usuario que añada productos, los elimine, consulte 
# los productos de la lista y consulte el número de productos que lleva incluidos en la lista.
# Una vez creada la lista de la compra, el programa la copiará en un archivo txt y luego trasnformará dicho archivo a pdf.
# Por último, el archivo pdf será enviado por correo electrónico al usuario.

# Importo librerías:
import io
import os

# Importo todas las funciones:
from Funciones_lista_compra import agregar, eliminar, consultar, numero, lista_previa, escribir_archivo, txt_to_pdf, envio_archivo
        
#Comienzo la ejecución del programa:
e = []
texto =' '

while True:
    print('\n1.- Añadir producto\n'
          '2.- Eliminar producto\n'
          '3.- Consultar producto\n'
          '4.- Consultar número total de productos añadidos a la lista\n'
          '5.- Previsualización de la lista\n'
          '6.- Salir\n')
    opcion = int(input('Elija la opción que desee: '))
    
    if opcion > 0 and opcion < 7:
        if opcion == 1:
            e = agregar(e)
        elif opcion == 2:
            e = eliminar(e)
        elif opcion == 3:
            consultar(e)
        elif opcion == 4:
            numero(e)
        elif opcion == 5:
            lista_previa(e)
        elif opcion == 6:
            print('Programa finalizado')
            break
    else: 
        print('Opción elegida no váida. Por favor, elija una opción entre 1 y 6')

print('****** LISTA DE LA COMPRA *****')
for i in e:
    print(f'- {i}', end="\n")
    

# Escribo la lista en un archivo.txt:
escribir_archivo(e)

# Transformo el archivo de texto a PDF
ruta = ruta = r'C:\Users\jgome\OneDrive\Escritorio\Curso Python (Udemy)\Ejercicios\Programa lista_compra\Archivos'
txt_file = os.path.join(ruta, 'Lista de la compra' + '.txt')
pdf_file = os.path.join(ruta, 'Lista de la compra' + '.pdf')
txt_to_pdf(txt_file, pdf_file)

# Envío documento pdf por correo electrónico:
envio_archivo()