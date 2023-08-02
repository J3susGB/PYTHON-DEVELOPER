# 1.- FUNCIONES PARA EL MENÚ PRINCIPAL:
#Función para añadir producto:
def agrega():
    supermercado = input('Introduce el Supermercado: ').capitalize()
    seccion = input('Introduce la sección: ').capitalize()
    codigo = int(input('Introduce el código del producto: '))
    producto = input('Introduce el producto: ').capitalize()
    cantidad = int(input('Introduce la cantidad: '))
    
    lista = (supermercado, seccion, codigo, producto, cantidad)
    
    return lista

#Función para listar productos:
def listar(producto):
    print('\n\t\t\t   ****** LISTA DE LA COMPRA ******\n')
    contador = 0
    
    for p in producto:
        contador += 1
        print(f'{contador}.- {p[0]} --> Sección: {p[1]} | Producto: {p[3]} (Código: {p[2]}) | Cantidad: {p[4]}')
    print('--------------------------------------------------------------------------------------------\n')
    
#Función para modificar productos:
def modificar(producto):
    listar(producto)
    existe = False
    codigoActualizar = int(input('Introduce el código del producto que quieres actualizar: '))

    for p in producto:
        print(p[2])
        if p[2] == codigoActualizar:
            existe = True
            break

    if existe:
        supermercado = input('Introduce el Supermercado: ').capitalize()
        seccion = input('Introduce la sección: ').capitalize()
        nuevo_producto = input('Introduce el producto: ').capitalize()  # Cambio de nombre de variable
        cantidad = int(input('Introduce la cantidad: '))

        listaM = (supermercado, seccion, nuevo_producto, cantidad, codigoActualizar)  # Cambio de nombre de variable
    else:
        listaM = ()

    return listaM

#Función para eliminar productos:
def eliminar(productos):
    listar(productos)
    existe = False
    codigoEliminar = int(input('Introduce el código del producto que desea eliminar: '))
    
    for p in productos:
        if p[2] == codigoEliminar:
            print('Dato a eliminar encontrado')
            existe = True
            break
    if not existe:
        codigoEliminar = ""
        
    return codigoEliminar

# 2.- FUNCIONES PARA ARCHIVO .txt
import io
import os

# Función para escribir la lista de la compra en el archivo .txt:
def escribir_archivo(productos):
    
    nombre_archivo = 'Lista de la compra.txt'
    ruta = r'C:\Users\jgome\OneDrive\Escritorio\Lista_compra POO\Archivos'
    ruta_completa = os.path.join(ruta, nombre_archivo)
    
    with open(ruta_completa, 'w') as f:
        f.write(f'           ******** LISTA DE LA COMPRA ********\n')
        for p in productos:
            f.write(f'{p[0]} ({p[1]}) | {p[3]} | Cantidad: {p[4]}\n')
    
    print('\n** Archivo creado y lista de la compra escrita con éxito **')
    f.close()
    
# 3.- FUNCIÓN PARA TRANSFORMAR TXT A PDF:
def txt_to_pdf(txt_file, pdf_file):
    from reportlab.pdfgen import canvas
    
    c = canvas.Canvas(pdf_file)

    with open(txt_file, 'r') as f:
        lines = f.readlines()
        y = 750
        for line in lines:
            c.drawString(100, y, line.strip())
            y -= 20

    print('** Archivo transformado a pdf con éxito **\n')
    c.save()

# 4.- FUNCIÓN PARA ENVIAR EL ARCHIVO POR EMAIL:
def envio_archivo():
    #librerías:
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders
    from email.mime.text import MIMEText

    
    # Datos del remitente y destinatario
    remitente = "**************@gmail.com"
    contraseña = "*************"
    destinatario = "**************@gmail.com"
    #destinatarios = ["**************@gmail.com", "**************@gmail.com"] # Varios destinatarios
    #cc = ["**************@gmail.com"] # Añadir a alguien en copia
    #bcc = ["**************@gmail.com"] # Añadir a alguien en copia oculta

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
    ruta = r'C:\Users\jgome\OneDrive\Escritorio\Lista_compra POO\Archivos'
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
    
    print ('** Archivo enviado por email con éxito **\n')