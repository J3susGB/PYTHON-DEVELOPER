# **`Lista de la compra con Tkinter&POO`** 

### *Jesús Gómez - Python Data Analist | Python Developer⚡*
[![Contact Me](https://img.shields.io/badge/Email-informational?style=for-the-badge&logo=Mail.Ru&logoColor=fff&color=c6362c)](mailto:jgomezbeltran88@gmail.com)
[![LinkedId](https://img.shields.io/badge/LinkedIn-informational?style=for-the-badge&logo=linkedin&logoColor=fff&color=0274b3)](https://www.linkedin.com/in/jesusgb-dev/)
[![Linktree](https://img.shields.io/badge/-Linktree-323330?style=for-the-badge&logo=linktree&logoColor=1de9b6)](https://linktr.ee/jesusgb?utm_source=linktree_admin_share )

### **`Información del proyecto:`**

#### Se trata de un ejercicio en el que pongo en práctica lo aprendido en cuanto a la conexión de Python con Mysql y la Programación Orientada a Objetos, implementandolo todo con Tkinter, lo que me ha permitido crear un simple programa de escritorio de uso local. Trabajo con Php MyAdmin, y ahí se crea inicialmente la estructura de la base de datos, y una vez hecho esto, utilizando el programa creado, se va rellenando.

#### La base de datos está formada por las siguientes columnas:

        Supermercado    Seccion     Codigo      Producto        Cantidad

#### El programa permite añadir productos, listar todos los productos, modificarlos, eliminarlos y enviar la lista de la compra en un documento pdf por correo electrónico.

### Al ejecutar el programa, se abre una ventana dividida en tres secciones:

        - Sección de eventos: Aquí aparecen los botones principales que permiten añadir, modificar y eliminar productos de la lista, y también un botón de enviar, que al pulsarlo, transforma los datos  de la lista en un documento txt, este documentos txt lo transforma a pdf, y finalmente, lo envía por correo electrónico.
        - Sección de datos: En esta sección, aparecen unas cajas de texto en las que vamos poniendo los datos del producto que se quiere añadir o modificar. También aparecen los botones Guardar y Cancelar, que guarda los cambios o se cancela, respectivamente.
        - Sección Grid: En esta sección, se visualizan todos los productos que se han ido añadiendo, y se va actualizando sobre la marcha conforme se añaden, modifican o eliminan productos

#### El proyecto está estructurado en tres documentos:

### **`LISTA DE LA COMPRA:`**

  - *main_lista.py* --> Documento principal

      - A través de este documento, se realiza la ejecución del programa.
      
  - *conexion_lista.py* --> Conexión con la base de datos

      - Se implementa la conexión con la base de datos y se crean todas las funciones que permiten interactuar directamente con la base de datos.

  - *ventana.py* --> Grueso del programa

      - Se implementa con trabajo de back-end, para el correcto funcionamiento del programa, y con trabajo de front-end, ya que se crean toda la inferfaz gráfica, botones, colores, etc.

#### Hecho con el único objetivo de practicar.