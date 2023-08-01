# 1.-  FUNCIONES PRINCIPALES:
# Función añadir producto:
def agregar(e):
    try:
        p = input('Producto a añadir: ').capitalize()
        if p not in e:
            e = e + [p]
            print(f'{p} añadido correctamente a la lista\n')
        else:
            print(f'El producto {p} ya está en la lista\n')
        return e      
    except:
        print('Hubo un problema al añadir el producto. Inténtalo de nuevo')
        
# Función eliminar producto:
def eliminar(e):
    try:
        p = input('Producto a eliminar: ').capitalize()
        if p in e:
            e.remove(p)
            print(f'{p} eliminado correctamente de la lista\n')
        else:
            print(f'El producto {p} no está en la lista\n')
        return e
            
    except:
        print('Hubo un problema al eliminar el producto. Inténtalo de nuevo')
        
# Función consultar producto:
def consultar(e):
    try:
        p = input('Producto a consultar: ').capitalize()
        if p in e:
            print(f'{p} está en la lista\n')
        else:
            print(f'El producto {p} no está en la lista\n')
            
    except:
        print('Hubo un problema con la consulta. Inténtalo de nuevo')
        
# Función consultar número productos:
def numero(e):
    
    try:
        productos = len(e)
        
        if productos < 0:
            print('El programa tiene un problema. Vuelve a intentarlo\n')
        elif productos == 0:
            print('La lista de la compra está vacía\n')
        elif productos == 1:
            print(f'Hay {productos} producto en la lista\n')
        elif productos > 1: 
            print(f'Hay {productos} productos en la lista\n')
            
    except:
        print('Hubo un problema con la consulta. Inténtalo de nuevo')
        
# Función previsualización de la lista:
def lista_previa(e):
    print('\nPrevisualización de la lista:')
    for i in e:
        print(f'- {i}', end="\n")
    
# 2.- FUNCIONES PARA ARCHIVO .txt
import io
import os

# Función para escribir la lista de la compra en el archivo .txt:
def escribir_archivo(e):
    
    nombre_archivo = 'Lista de la compra.txt'
    ruta = r'C:\Users\jgome\OneDrive\Escritorio\Curso Python (Udemy)\Ejercicios\Programa lista_compra\Archivos'
    ruta_completa = os.path.join(ruta, nombre_archivo)
    
    with open(ruta_completa, 'w') as f:
        f.write('******** LISTA DE LA COMPRA ********\n')
        for producto in e:
            f.write(f'  - {producto}\n')
    
    print('\n***** Archivo creado y lista de la compra escrita con éxito *****')
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

    print('***** Archivo transformado a pdf con éxito *****')
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
    remitente = "jgomezbeltran88@gmail.com"
    contraseña = "otkskjmzodpbtagq"
    destinatario = "sesionlourdes@gmail.com"
    #destinatarios = ["sesionlourdes@gmail.com", "akenaton86@hotmail.com"] # Varios destinatarios
    #cc = ["jgomezbeltran88@gmail.com"] # Añadir a alguien en copia
    #bcc = ["akenaton86@hotmail.com"] # Añadir a alguien en copia oculta

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
    ruta = ruta = r'C:\Users\jgome\OneDrive\Escritorio\Curso Python (Udemy)\Ejercicios\Programa lista_compra\Archivos'
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
    
    print ('***** Archivo enviado por email con éxito *****')
    
