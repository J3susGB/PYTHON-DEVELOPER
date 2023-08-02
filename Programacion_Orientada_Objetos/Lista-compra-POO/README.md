# **`CONEXIÓN PYTHON - MYSQL`** 

### *Jesús Gómez - Python Data Analist | Python Developer⚡*
[![Contact Me](https://img.shields.io/badge/Email-informational?style=for-the-badge&logo=Mail.Ru&logoColor=fff&color=c6362c)](mailto:jgomezbeltran88@gmail.com)
[![LinkedId](https://img.shields.io/badge/LinkedIn-informational?style=for-the-badge&logo=linkedin&logoColor=fff&color=0274b3)](https://www.linkedin.com/in/jesusgb-dev/)
[![Linktree](https://img.shields.io/badge/-Linktree-323330?style=for-the-badge&logo=linktree&logoColor=1de9b6)](https://linktr.ee/jesusgb?utm_source=linktree_admin_share )

### **`Información del proyecto:`**

#### Se trata de un ejercicio en el que pongo en práctica lo aprendido en cuanto a la conexión de Python con Mysql, y la Programación Orientada a Objetos. Trabajo con Php MyAdmin, y ahí se crea inicialmente la estructura de la base de datos, y una vez hecho esto, utilizando el programa creado, se va rellenando.

#### El programa permite añadir productos, listar todos los productos, modificarlos, eliminarlos, crear un documento .txt  con la lista de la compra, transformar este documento en pdf, y finalmente, enviar el pdf por correo electrónico.
### Todo ello realizado con POO e interactuando con el usuario por consola.

#### El proyecto está estructurado en tres documentos:

### **`LISTA DE LA COMPRA:`**

  - *main.py* --> Documento principal

      - Se importan los dos documentos restantes
      - Contiene el menú principal del programa, el cual consta de las siguientes opciones:

                1.- Añadir producto
                2.- Listar productos
                3.- Modificar producto
                4.- Eliminar producto
                5.- Crear documento de la lista
                6.- Enviar documento por email
                7.- Salir
    
      
  - *Conection.py* --> Conexión con la base de datos

      - Se implementa la conexión con la base de datos y se crean todas las funciones que permiten interactuar directamente con la base de datos.

  - *functions.py* --> Funciones

      - Resto  de funciones necesarias conectadas directamente con las funciones que llevan las instrucciones sql para modificar la base de datos.
      - Funciones para crear archivo txt con la lista, transformarlo a pdf y enviarlo por correo electrónico

#### Hecho con el único objetivo de practicar.