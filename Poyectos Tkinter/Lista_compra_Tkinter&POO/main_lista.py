# Importando herramientas para trabajar con Tkinter:
from tkinter import *
from tkinter import ttk
from ventana_lista import *

def main():
    root = Tk() # Creando objeto del tipo Tk
    root.wm_title("LISTA DE LA COMPRA")
    app = Ventana(root)
    app.mainloop()
    
if __name__ == '__main__':
    main()