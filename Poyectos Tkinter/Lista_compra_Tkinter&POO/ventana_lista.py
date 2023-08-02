# Importando librerías y documentos necesarios:
from os import stat
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from typing import Any
from typing_extensions import Literal
from conexion_lista import DAO
import os

#Creo una clase del tipo Frame:
class Ventana(Frame):
    dao = DAO() #Instancio la clase DAO del documento conexion.py
    txt_file = r'C:\Users\jgome\OneDrive\Escritorio\Curso Python (Udemy)\Ejercicios\Versiones lista_compra\Lista_compra_Tkinter&POO\archivos\Lista de la compra.txt'
    pdf_file = r'C:\Users\jgome\OneDrive\Escritorio\Curso Python (Udemy)\Ejercicios\Versiones lista_compra\Lista_compra_Tkinter&POO\archivos\Lista de la compra.pdf'
    
    def __init__(self, master = None):
        super().__init__(master, width=1000, height=400)
        self.master = master
        self.pack()
        self.crear_widget() #Creando los controles
        self.cargarDatos() #Llamo a cargarDatos para que me presente todos los registros
        self.habilitarTexto('disabled') #LLamo a la función HabilitarText y le pongo el parámetro disabled de momento, para que estén desabilitados
        self.HabilitarBotonesEventos('normal')
        self.HabilitarBotonesGuardarCancelar('disabled')
        self.bandera = 'Guardar'
        self.codigo_seleccionado = None # Inicializo la variable para almacenar el código seleccionado al actualizar producto.
    
    #2.- # TODAS LAS FUNCIONES, EVENTOS, ETC:
    #Función para cargar los datos en el grid automáticamente cuando se abra el programa:
    def cargarDatos(self):
        datos = self.dao.consulta_productos()
        for row in datos:
            self.grid.insert("", END, text=row[0], values=(row[1], row[2], row[3], row[4]))
    
    #Función para limpiar el Grid (cuando introduzca nuevo dato, aparecerá sin tener que abrir y cerrar el programa):
    def limpiarGrid(self):
        for item in self.grid.get_children(): #Con get.children obtengo todos los datos del grid
            self.grid.delete(item)
            
    #Función para habilitar/desabilitar texto (estados: 'normal' y 'disabled')
    def habilitarTexto(self, estado):
        self.txtSupermercado.configure(state=estado)
        self.txtSeccion.configure(state=estado)
        self.txtCodigo.configure(state=estado)
        self.txtProducto.configure(state=estado)
        self.txtCantidad.configure(state=estado) 
        
    # Función para habilitar/desabilitar los botones de eventos:
    def HabilitarBotonesEventos(self, estado):
        self.alta.configure(state=estado)
        self.actualizar.configure(state=estado)
        self.eliminar.configure(state=estado)
        self.enviar.configure(state=estado)
        
    # Función para habilitar/desabilitar los botones de Guardar y cancelar:
    def HabilitarBotonesGuardarCancelar(self, estado):
        self.guardar.configure(state=estado)
        self.cancelar.configure(state=estado)
        
    # Función para limpiar texto:
    def LimpiarText(self):
        self.txtSupermercado.delete(0,END)
        self.txtSeccion.delete(0,END)
        self.txtCodigo.delete(0,END)
        self.txtProducto.delete(0,END)
        self.txtCantidad.delete(0,END)
        self.txtSupermercado.focus() #Cuando llame a la función limpiarText, lo limpirará y manda el cursor a supermercado 
        
    #FUNCIONES PARA ARCHIVO .txt
    # Función para escribir la lista de la compra en el archivo .txt:
    def escribir_archivo(self, productos):
        import io
        import os
        
        nombre_archivo = 'Lista de la compra.txt'
        ruta = r'C:\Users\jgome\OneDrive\Escritorio\Curso Python (Udemy)\Ejercicios\Versiones lista_compra\Lista_compra_Tkinter&POO\archivos'
        ruta_completa = os.path.join(ruta, nombre_archivo)
        
        with open(ruta_completa, 'w') as f:
            f.write(f'           ******** LISTA DE LA COMPRA ********\n')
            for p in productos:
                f.write(f'{p[0]} ({p[1]}) | {p[3]} | Cantidad: {p[4]}\n')
        
        f.close()   
        
    # Función para transformar archivo en pdf:
    def txt_to_pdf(self):
        from reportlab.pdfgen import canvas

        c = canvas.Canvas(self.pdf_file)
        with open(self.txt_file, 'r') as f:
            lines = f.readlines()
            y = 750
            for line in lines:
                c.drawString(100, y, line.strip())
                y -= 20
        c.save()
    
    # FUNCIÓN PARA ENVIAR EL ARCHIVO POR EMAIL:
    # Decorador para indicar que la función enviar_archivo es un método estático
    @staticmethod
    def enviar_archivo():
        #librerías:
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.base import MIMEBase
        from email import encoders
        from email.mime.text import MIMEText

        
        # Datos del remitente y destinatario
        remitente = "***************@gmail.com"
        contraseña = "**************"
        destinatario = "***************@gmail.com"
        #destinatarios = ["***************@gmail.com", "***************@gmail.com"] # Varios destinatarios
        #cc = ["***************@gmail.com"] # Añadir a alguien en copia
        #bcc = ["***************@gmail.com"] # Añadir a alguien en copia oculta

        # Crear objeto del mensaje
        mensaje = MIMEMultipart()
        mensaje["From"] = remitente
        mensaje["To"] = destinatario 
        #mensaje["To"] = ", ".join(destinatarios) # Varios destinatarios
        #mensaje["CC"] = ", ".join(cc) # Cuando se envía con alguien en copia
        #mensaje["BCC"] = ", ".join(bcc) # Cuando se envía con alguien en copia oculta
        mensaje["Subject"] = "LISTA DE LA COMPRA" # Este es el asunto del email
        
        # Agregar descripción en el cuerpo del mensaje
        descripcion = "¡Hola!\n\nTe envío la lista de la compra.\n\nUn saludo"
        parte_descripcion = MIMEText(descripcion)
        mensaje.attach(parte_descripcion)
        
        # Adjuntar el archivo PDF al mensaje
        ruta = r'C:\Users\jgome\OneDrive\Escritorio\Curso Python (Udemy)\Ejercicios\Versiones lista_compra\Lista_compra_Tkinter&POO\archivos'
        archivo_adjunto = os.path.join(ruta, 'Lista de la compra.pdf')
        
        with open(archivo_adjunto, "rb") as adjunto:
            parte = MIMEBase("application", "octet-stream")
            parte.set_payload(adjunto.read())
            encoders.encode_base64(parte)
            parte.add_header("Content-Disposition", f"attachment; filename= {archivo_adjunto}")
            mensaje.attach(parte)

        # Enviar el correo electrónico utilizando un servidor SMTP
        servidor_smtp = smtplib.SMTP("smtp.gmail.com", 587)
        servidor_smtp.starttls()
        servidor_smtp.login(remitente, contraseña)
        servidor_smtp.send_message(mensaje)
        servidor_smtp.quit()
        
    # Función para guardar la acción  del botón  alta:
    def fNuevo(self):
        self.HabilitarBotonesEventos('disabled')
        self.habilitarTexto('normal')
        self.HabilitarBotonesGuardarCancelar('normal')
        self.LimpiarText()
    
    # Función para guardar la acción  del botón  actualizar:
    def fActualizar(self):
        select = self.grid.focus() #Saca los datos de toda la línea seleccionada
        #print(f"Selected item: {select}") #código para comprobar error
        row = self.grid.item(select) #Focaliza en los datos necesarios
        #print(f"Row data: {row}") #código para comprobar error
        supermercado = self.grid.item(select, 'text')
        valores = self.grid.item(select, 'values') #Selecciona el valor de la clave código
        #print(f"Values: {valores}") #código para comprobar error
        try:
            if not valores:
                messagebox.showwarning('Modificar', 'Debes seleccionar un elemento')
            else:
                self.bandera = 'Actualizar'
                self.habilitarTexto('normal')
                self.HabilitarBotonesGuardarCancelar('normal')
                self.LimpiarText()
                self.txtSupermercado.insert(0, supermercado) # -> Supermercado
                self.txtSeccion.insert(0, valores[0]) # Posición 1 en valores -> Sección
                self.txtCodigo.insert(0, valores[1]) # Posición 2 en valores -> Código
                self.txtProducto.insert(0, valores[2]) # Posición 3 en valores -> Producto
                self.txtCantidad.insert(0, valores[3]) # Posición 4 en valores -> Cantidad
                self.codigo_seleccionado = valores[1] # Almaceno el valor de la columna código para la actualización
        except:
            messagebox.showwarning('Actualizar', 'Error al actualizar')
     
    # Función para guardar la acción  del botón  eliminar:
    def fEliminar(self):
        select = self.grid.focus() #Saca los datos de toda la línea seleccionada
        row = self.grid.item(select) #Focaliza en los datos necesarios
        valores = self.grid.item(select, 'values') #Selecciona el valor de la clave código
        codigo = int(valores[1])
        try:
            if not valores:
                messagebox.showwarning('Eliminar', 'Debes seleccionar un elemento')
            else:
                r =messagebox.askquestion('Eliminar', '¿Estás seguro que deseas eliminar el producto seleccionado?')
                if r == 'yes':
                    n = self.dao.eliminar_producto(codigo)
                    if n == 1:
                        messagebox.showinfo('Eliminar', 'Producto eliminado correctamente')
                        self.limpiarGrid()
                        self.cargarDatos()
                    else:
                        messagebox.showinfo('Eliminar', 'No se pudo eliminar')
                else:
                    pass
        except:
            messagebox.showwarning('Eliminar', 'Error al eliminar')
    
     # Función para guardar la acción  del botón  enviar:
    def fEnviar(self):
        try:
            self.escribir_archivo(self.dao.consulta_productos())
            self.txt_to_pdf()
            self.enviar_archivo()  # Llamar al método estático enviar_archivo() sin self
            self.limpiarGrid() #Para limpiar el grid
            self.cargarDatos() #Para que vuelva a cargar los datos automáticamente
            self.LimpiarText() #Para borrar los datos de la caja de texto
            self.HabilitarBotonesEventos('normal') #Habilita botones de eventos
            self.HabilitarBotonesGuardarCancelar('disabled') #Desabilita botones guardar y cancelar
            self.habilitarTexto('disabled') #Desabilita las cajas de texto
            messagebox.showinfo('Enviar', 'Archivo creado y enviado por email correctamente')
        except:
            messagebox.showwarning('Se produjo un error al crear y enviar el arhivo por email')
        
    # Función para guardar la acción  del botón  Guardar:
    def fGuardar(self):
        if self.bandera == 'Guardar':
            sup = self.txtSupermercado.get()
            sec = self.txtSeccion.get()
            cod = self.txtCodigo.get()
            pro = self.txtProducto.get()
            can = self.txtCantidad.get()
            try:
                self.dao.insertar_producto(sup,sec,cod,pro,can)
                messagebox.showinfo('Guardar', 'Producto añadido correctamente a la lista')
            except:
                messagebox.showwarning('Guardar', 'No se pudo agregar el producto a la lista')
        elif self.bandera == 'Actualizar':
            supM = self.txtSupermercado.get()
            secM = self.txtSeccion.get()
            codM = self.txtCodigo.get()
            proM = self.txtProducto.get()
            canM = self.txtCantidad.get()
            try:
                self.dao.modificar_producto(supM, secM, proM, canM, codM)
                messagebox.showinfo('Actualizar', 'Producto actualizado correctamente')
                self.bandera = 'Guardar'
            except:
                messagebox.showwarning('Actualizar', 'No se pudo actualizar el producto')
                self.bandera = 'Actualizar'
                
        self.limpiarGrid() #Para limpiar el grid
        self.cargarDatos() #Para que vuelva a cargar los datos automáticamente
        self.LimpiarText() #Para borrar los datos de la caja de texto
        self.HabilitarBotonesEventos('normal') #Habilita botones de eventos
        self.HabilitarBotonesGuardarCancelar('disabled') #Desabilita botones guardar y cancelar
        self.habilitarTexto('disabled') #Desabilita las cajas de texto
    
    # Función para guardar la acción  del botón  Cancelar:
    def fCancelar(self):
        self.limpiarGrid() #Para limpiar el grid
        self.cargarDatos() #Para que vuelva a cargar los datos automáticamente
        self.LimpiarText() #Para borrar los datos de la caja de texto
        self.HabilitarBotonesEventos('normal') #Habilita botones de eventos
        self.HabilitarBotonesGuardarCancelar('disabled') #Desabilita botones guardar y cancelar
        self.habilitarTexto('disabled') #Desabilita las cajas de texto
    
    #1.- Creo el método crear_widget(), que empezará a crear la interface dentro de la Ventana:
    def crear_widget(self):
        #CREO FRAME1, DONDE ESTARÁN LOS BOTONES PRINCIPALES
        frame1 = Frame(self, bg ="#21618C") #Creo objeto de la clase frame
        frame1.place(x=0, y=0, width=150, height=399) #pongo 399 porque el heigth total de la ventana es 400
        
        #BOTONES DE EVENTOS EN FRAME1:
        # Creo botón alta cliente:
        self.alta = Button(frame1, text = "Alta producto", command = self.fNuevo, bg = '#E67E22', fg = 'white')
        self.alta.place(x=13, y=50, width=125, height=40) #Lugar en el que estará el botón y tamaño
        
        # Creo botón modificar cliente:
        self.actualizar = Button(frame1, text = "Modificar prodcuto", command = self.fActualizar, bg = '#E67E22', fg = 'white')
        self.actualizar.place(x=13, y=135, width=125, height=40) #Lugar en el que estará el botón y tamaño
        
        # Creo botón eliminar cliente:
        self.eliminar = Button(frame1, text = "Eliminar prodcuto", command = self.fEliminar, bg = '#E67E22', fg = 'white')
        self.eliminar.place(x=13, y=225, width=125, height=40) #Lugar en el que estará el botón y tamaño
        
        # Creo botón enviar lista por email:
        self.enviar = Button(frame1, text = "Enviar", command = self.fEnviar, bg = '#E67E22', fg = 'white')
        self.enviar.place(x=85, y=368, width=60, height=25) #Lugar en el que estará el botón y tamaño
        
        # CREO FRAME2, A CONTINUACIÓN DE FRAME1, QUE SERÁ LA SECCIÓN DONDE SE INTRODUCIRÁN LOS DATOS:
        frame2 = Frame(self, bg = "#A9CCE3")
        frame2.place(x = 150, y = 0, width = 230, height = 399)
        
        # Creo la etiqueta supermercado:
        label1 = Label(frame2, text = 'Supermercado')
        label1.place(x = 30, y = 30)
        self.txtSupermercado = Entry(frame2) #Usando Entry convertimos en una caja de texto
        self.txtSupermercado.place(x=30, y=61, width=150, height=20)
        
        # Creo la etiqueta para el sección:
        label2 = Label(frame2, text = 'Sección: ')
        label2.place(x = 30, y = 93)
        self.txtSeccion = Entry(frame2) #Con el comando Entry, le decimos que va a ser una caja de texto
        self.txtSeccion.place(x=30, y=124, width=150, height=20)
        
        # Creo la etiqueta para el código:
        label3 = Label(frame2, text = 'Código: ')
        label3.place(x = 30, y = 158)
        self.txtCodigo = Entry(frame2) #Con el comando Entry, le decimos que va a ser una caja de texto
        self.txtCodigo.place(x=30, y=189, width=150, height=20)
        
        # Creo la etiqueta para el Producto:
        label4 = Label(frame2, text = 'Producto: ')
        label4.place(x = 30, y = 223)
        self.txtProducto = Entry(frame2) #Con el comando Entry, le decimos que va a ser una caja de texto
        self.txtProducto.place(x=30, y=254, width=150, height=20)
        
        # Creo la etiqueta para el cantidad:
        label5 = Label(frame2, text = 'Cantidad: ')
        label5.place(x = 30, y = 287)
        self.txtCantidad = Entry(frame2) #Con el comando Entry, le decimos que va a ser una caja de texto
        self.txtCantidad.place(x=30, y=319, width=150, height=20)
        
        # Creo botón de guardar:
        self.guardar = Button(frame2, text = 'Guardar', command = self.fGuardar, bg = '#797D7F', fg = 'white' )
        self.guardar.place(x=75, y=357, width=70, height=33)
        
        # Creo botón de cancelar:
        self.cancelar = Button(frame2, text = 'Cancelar', command = self.fCancelar, bg = '#C0392B', fg = 'white' )
        self.cancelar.place(x=151, y=357, width=70, height=33)
        
        #CREO EL FRAME3, A CONTINUACIÓN DEL FRAME2, QUE CONTENDRÁ EL GRID CON TODOS LOS DATOS EXTRAIDOS DE LA BASE DE DATOS:
        frame3 = Frame(self, bg = '#CCD1D1')
        frame3.place(x=380, y=15, width=620, height=390)
        
        self.grid = ttk.Treeview(self, columns=('col1', 'col2', 'col3', 'col4'))        
       
        #Creo el Grid:
        self.grid.column('#0', width=75, anchor=CENTER)
        self.grid.column('col1', width=90, anchor=CENTER)
        self.grid.column('col2', width=90, anchor=CENTER)
        self.grid.column('col3', width=90, anchor=CENTER)
        self.grid.column('col4', width=90, anchor=CENTER)
        
        #Cambio el título a las columnas:
        self.grid.heading('#0', text='Supermercado', anchor=CENTER) #Cambio el título de cada columna
        self.grid.heading('col1', text='Sección', anchor=CENTER)
        self.grid.heading('col2', text='Códido', anchor=CENTER)
        self.grid.heading('col3', text='Producto', anchor=CENTER)
        self.grid.heading('col4', text='Cantidad', anchor=CENTER)
        
        #Coloco el grid:
        self.grid.place(x=380, y=0, width=590, height=399)
        
        # Coloco opción para que NO pueda seleccionar varias líneas del grid:
        self.grid['selectmode']='browse'
            