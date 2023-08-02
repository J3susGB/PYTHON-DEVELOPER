# Complemento al archivo master

# Funcion listar:
def listar(clientes):
    print('\nClientes: ')
    contador = 0
    
    for c in clientes:
        contador += 1
        print(f'{contador}.- Código: {c[0]} · Nombre: {c[1]} {c[2]} {c[3]} · Créditos: {c[4]}.')
    print('--------------------------------------------------------------\n')

# Función para registrar:
def DatosClientes():
    codigo = int(input('Introduce el código del cliente: '))
    nombre = input('Introduce el nombre del cliente: ')
    apellido1 = input('Introduce el primer apellido del cliente: ')
    apellido2 = input('Introduce el segundo apellido del cliente: ')
    creditos = int(input('Introduce los créditos del cliente: '))

    clientes = (codigo, nombre, apellido1, apellido2, creditos)
    return clientes

# Función para actualizar datos de clientes:
def DatosClientesActualizar(clientes):
    listar(clientes) # Llamamos a la función listar para ver los clientes
    existe = False
    codigoActualizar = int(input('Introduce el código del cliente que quieres modificar: '))
     
    for c in clientes:
        print(c[0])
        if c[0] == codigoActualizar:
            print(f'Dato encontrado: {codigoActualizar}')
            existe = True
            break
        
    if existe == True:
        nombre = input('Introduce el nombre del cliente: ')
        apellido1 = input('Introduce el primer apellido del cliente: ')
        apellido2 = input('Introduce el segundo apellido del cliente: ')
        creditos = int(input('Introduce los créditos del cliente: '))
        clientesE = ( nombre, apellido1, apellido2, creditos, codigoActualizar)
        
    else:
        clientesE = None
        
    return clientesE

# Función para eliminar clientes:
def registroEliminar(clientes):
    listar(clientes)
    existe = False
    codigoEliminar = int(input('Introduce el código del cliente que quieres eliminar:'))
    
    for c in clientes:
        print(c[0])
        if c[0] == codigoEliminar:
            print('Dato encontrado a eliminar')
            existe = True
            break
        
    if not existe:
        codigoEliminar = ""
        
    return codigoEliminar