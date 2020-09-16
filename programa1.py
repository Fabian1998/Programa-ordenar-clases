###Importar librerias###

try:
    from Tkinter import *
    from ttk import *
    from tkMessageBox import *
    print('Python 2')
    print('Su sistema usa Python 2, puede causar problemas en la ejecución')
except ImportError:
    from tkinter import *
    from tkinter.ttk import *
    from tkinter.messagebox import *
    print('Python 3')

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from firebase import firebase

###Ventana###

root= Tk()
root.title("Inicio")
#root.state('zoomed')

###Funciones###

def crearcertificado1():
    global framect1
    print("Hola1")
    try:
        framect1.destroy()
        framect2.destroy()
        framect3.destroy()
    except:
        print("pasa")
    
    ADGD0308=IntVar()
    ADGG0208=IntVar()
    ADGG0408=IntVar()
    ADGG0508=IntVar()
    COMV0211=IntVar()
    COMV0108=IntVar()
    COMT0411=IntVar()
    COMT0110=IntVar()
    framect1= ttk.Frame(adjudicaralumno)
    framect1.grid(row=3, column=0)
    Label(framect1, text="ADGD0308-Actividades de gestion administrativa").grid(row=0, column=0)
    Checkbutton(framect1, variable=ADGD0308, onvalue=True, offvalue=False).grid(row=0, column=1)

    Label(framect1, text="ADGG0208 Actividades administrativas en relacion con el cliente").grid(row=1, column=0)
    Checkbutton(framect1, variable=ADGG0208, onvalue=True, offvalue=False).grid(row=1, column=1)

    Label(framect1, text="ADGG0408-Operaciones auxiliares de servicios administrativos y generales").grid(row=2, column=0)
    Checkbutton(framect1, variable=ADGG0408, onvalue=True, offvalue=False).grid(row=2, column=1)

    Label(framect1, text="ADGG0508-Operaciones de grabacion y tratamiento de datos y documentacion").grid(row=3, column=0)
    Checkbutton(framect1, variable=ADGG0508, onvalue=True, offvalue=False).grid(row=3, column=1)

    Label(framect1, text="COMV0211-Actividades auxiliares de comercio").grid(row=4, column=0)
    Checkbutton(framect1, variable=COMV0211, onvalue=True, offvalue=False).grid(row=4, column=1)

    Label(framect1, text="COMV0108-Actividades de venta").grid(row=5, column=0)
    Checkbutton(framect1, variable=COMV0108, onvalue=True, offvalue=False).grid(row=5, column=1)

    Label(framect1, text="COMT0411-Gestion comercial de ventas").grid(row=6, column=0)
    Checkbutton(framect1, variable=COMT0411, onvalue=True, offvalue=False).grid(row=6, column=1)

    Label(framect1, text="COMT0110-Atencion al cliente, consumidor o usuario").grid(row=7, column=0)
    Checkbutton(framect1, variable=COMT0110, onvalue=True, offvalue=False).grid(row=7, column=1)

    Button(framect1, text="Selección de unidades", command=ventanacomercio).grid(row=8, column=0)



    print("Hola2")  


def crearcertificado2():
    global framect2
    print("Hola3")
    try:
        framect1.destroy()
        framect2.destroy()
        framect3.destroy()
    except:
        print("pasa")
    framect2= ttk.Frame(adjudicaralumno)
    framect2.grid(row=3, column=0)
    Label(framect2, text="Hola1").grid(row=1, column=2)
    print("hola4")

def crearcertificado3():
    global framect3
    try:
        framect1.destroy()
        framect2.destroy()
        framect3.destroy()
    except:
        print("pasa")
    framect3= ttk.Frame(adjudicaralumno)
    framect3.grid(row=3, column=0)
    Label(framect3, text="Hola").grid(row=0, column=0)

def ventanacomercio():
    global ventanacomercio
    ventanacomercio=Tk()
    MF0976_2=IntVar()
    Label(ventanacomercio, text="MF0976_2-Operaciones administrativas comerciales ").grid(row=0, column=0)
    Checkbutton(ventanacomercio, variable=MF0976_2, onvalue=True, offvalue=False, command=unidadesMF0976_2).grid(row=0, column=1)
    MF0979_2=IntVar()
    Label(ventanacomercio, text="MF0979_2: Gestión operativa de tesorería").grid(row=4, column=0)
    Checkbutton(ventanacomercio, variable=MF0979_2, onvalue=True, offvalue=False).grid(row=4, column=1)
    Button(ventanacomercio, text="Subir", command=subircomercio).grid(row=50, column=0)
    ventanacomercio.mainloop()

def unidadesMF0976_2():
    UF0349=IntVar()
    Label(ventanacomercio, text="UF0349: Atención al cliente en el proceso comercial").grid(row=1, column=2)
    Checkbutton(ventanacomercio, variable=UF0349, onvalue=True, offvalue=False).grid(row=1, column=3)

def subircomercio():
    print("HOla")




###Pestañas###

Notebook= ttk.Notebook(root)
Notebook.pack(fill='both', expand='yes')
adjudicaralumno = ttk.Frame(Notebook)
Notebook.add(adjudicaralumno, text="Añadir Alumno")
organizarclases = ttk.Frame(Notebook)
Notebook.add(organizarclases, text="Horario")

###Añadir nuevo alumno###

Label(adjudicaralumno, text="Nombre:").grid(row=0, column=0)
nombre = Entry(adjudicaralumno).grid(row=0, column=1)
Label(adjudicaralumno, text="Apellidos:").grid(row=0, column=2)
apellido = Entry(adjudicaralumno).grid(row=0, column=3)
Label(adjudicaralumno, text="Dni:").grid(row=0, column=4)
dni= StringVar()
dnientry = Entry(adjudicaralumno, textvariable=dni).grid(row=0, column=5)
Label(adjudicaralumno, text="Correo:").grid(row=1, column=0)
apellido = Entry(adjudicaralumno).grid(row=1, column=1)
Label(adjudicaralumno, text="Telefono:").grid(row=1, column=2)
apellido = Entry(adjudicaralumno).grid(row=1, column=3)


certificado1 = IntVar()
certificado2 = IntVar()
certificado3 = IntVar()
Radiobutton(adjudicaralumno, variable=certificado1, text="Comercio y administracion", command=crearcertificado1).grid(row=2, column=0)
Radiobutton(adjudicaralumno, variable=certificado2, text="Sala", command=crearcertificado2).grid(row=2, column=1)
Radiobutton(adjudicaralumno, variable=certificado3, text="Cocina, pasteleria y reposteria", command=crearcertificado3).grid(row=2, column=2)
###Organizacion de clases###






###Fin de programa###
root.mainloop()