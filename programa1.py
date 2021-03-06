###Importar librerias###

try:
    from Tkinter import *
    from ttk import *
    from tkMessageBox import *
except ImportError:
    from tkinter import *
    from tkinter.ttk import *
    from tkinter.messagebox import *

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
from firebase_admin import storage

import datetime
from datetime import date

cred = credentials.Certificate('colocacion-de-alumnos-en-clase-9515a56cb8c4.json')
firebase_admin.initialize_app(cred)

db = firestore.client()



###Ventana###

root= Tk()
root.title("Inicio")
#root.state('zoomed')

###Funciones###

def crearcertificado1():
    global framect1
    try:
        framect1.destroy()
        framect2.destroy()
        framect3.destroy()
    except:
        pass
    global ADGD0308
    ADGD0308=IntVar()
    ADGG0208=IntVar()
    ADGG0408=IntVar()
    ADGG0508=IntVar()
    COMV0211=IntVar()
    COMV0108=IntVar()
    COMT0411=IntVar()
    COMT0110=IntVar()
    framect1= ttk.Frame(adjudicaralumno)
    framect1.grid(row=4, column=0)
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
    Button(framect1, text="unidades", command=subircomercio).grid(row=8, column=1)

def crearcertificado2():
    global framect2
    try:
        framect1.destroy()
        framect2.destroy()
        framect3.destroy()
    except:
        framect2= ttk.Frame(adjudicaralumno)
        framect2.grid(row=4, column=0)
        Label(framect2, text="Hola1").grid(row=1, column=2)

def crearcertificado3():
    global framect3
    try:
        framect1.destroy()
        framect2.destroy()
        framect3.destroy()
    except:
        print("")
    framect3= ttk.Frame(adjudicaralumno)
    framect3.grid(row=4, column=0)
    Label(framect3, text="Hola").grid(row=0, column=0)

def ventanacomercio():
    global ventanacomercio
    global MF0976_2
    global MF0979_2
    global UF0349
    global fechaUF0349
    global horarioUF0349
    UF0349=BooleanVar()
    MF0976_2=IntVar()
    MF0979_2=IntVar()
    fechaUF0349= StringVar()
    horarioUF0349= StringVar()
    ventanacomercio=Toplevel()
    ventanacomercio.title("Formación")
    if ADGD0308.get() == 1:
        Label(ventanacomercio, text="MF0976_2-Operaciones administrativas comerciales ").grid(row=0, column=0)
        Checkbutton(ventanacomercio, variable=MF0976_2, onvalue=True, offvalue=False).grid(row=0, column=1)
        Label(ventanacomercio, text="UF0349: Atención al cliente en el proceso comercial").grid(row=1, column=2)
        UF0349check=Checkbutton(ventanacomercio, variable=UF0349, onvalue=True, offvalue=False).grid(row=1, column=3)
        Label(ventanacomercio, text="Fechas").grid(row=1, column=4)
        Entry(ventanacomercio, textvariable=fechaUF0349).grid(row=1, column=5)
        Label(ventanacomercio, text="Horario").grid(row=1, column=6)
        Entry(ventanacomercio, textvariable=horarioUF0349).grid(row=1, column=7)
        Label(ventanacomercio, text="MF0979_2: Gestión operativa de tesorería").grid(row=4, column=0)
        Checkbutton(ventanacomercio, variable=MF0979_2, onvalue=True, offvalue=False).grid(row=4, column=1)
    else:
        pass
    Button(ventanacomercio, text="Subir", command=subircomercio).grid(row=50, column=0)

def subircomercio():
    totalesdias =  db.collection(u'fechas')
    diastotales = totalesdias.get()
    varfechafin= fechafin.get()
    varfechainicio= fechainicio.get()
    separarfechafin= varfechafin.split("/")
    diafin=int(separarfechafin[0])
    mesfin=int(separarfechafin[1])
    añofin=int(separarfechafin[2])

    separarfechainicio= varfechainicio.split("/")
    diainicio=int(separarfechainicio[0])
    mesinicio=int(separarfechainicio[1])
    añoinicio=int(separarfechainicio[2])

    inicio=date(añoinicio, mesinicio, diainicio)
    fin=date(añofin, mesfin,  diafin)
    listadias=[]

    #if dni.get() == "" or nombre.get() == "" or apellido.get() == "" or  correo.get() == "" or  telefono.get() == "" or fechainicio.get() == "" or fechafin.get() == "" or horario.get() == "":
#       showerror(title="Error", message="Faltan datos del alumno")
    #else:
    if Lunes.get() == 1:
        listadias.append("Monday")
    else:
        pass
    if Martes.get() == 1:
        listadias.append("Tuesday")
    else:
        pass
    if Miercoles.get() == 1:
        listadias.append("Wednesday")
    else:
        pass
    if Jueves.get() == 1:
        listadias.append("Thursday")
    else:
        pass
    if Viernes.get() == 1:
        listadias.append("Friday")
    else:
        pass
    for n in listadias:
        dias = str(fin - inicio)
        numdia = dias.split(" ")
        dias=int(numdia[0])

        while dias >= 0:
            buscador = inicio.strftime("%A")
            if buscador == n:
                for n in diastotales:
                    fechasarry = u'{}'.format(n.id,n.to_dict())
                    if fechasarry == inicio.strftime("%d" "%B" "%Y"):
                        print ("Esta")
                        print(inicio.strftime("%d" "%B" "%Y"))
                        doc_ref = db.collection(u'fechas').document(inicio.strftime("%d" "%B" "%Y"))
                        doc_ref.update({
                        dni.get(): firestore.ArrayUnion([horario.get()])
                        })

                    else:
                        print ("No esta")
                        print(inicio.strftime("%d" "%B" "%Y"))
                        doc_ref = db.collection(u'fechas').document(inicio.strftime("%d" "%B" "%Y"))
                        doc_ref.set({
                        dni.get(): horario.get()
                        })
            else:
                pass
            inicio = inicio + datetime.timedelta(days=1)
            dias = dias - 1
        inicio=date(añoinicio, mesinicio,  diainicio)

#        carpeta = db.collection(u'info')
#        nombre1 = carpeta.get()
#        for n in nombre1:
#            dniarray=u'{}'.format(n.id,n.to_dict())
#            if dniarray == dni.get():
#                doc_ref = db.collection(u'info').document(dni.get())
#                doc_ref.update({
#                u'Nombre': nombre.get(),
#                u'Apellido': apellido.get(),
#                u'Correo': correo.get(),
#                u'Telefono': telefono.get()
#                })
#                showinfo(title="Info", message="Usuario actualizado con exito")
#                return
#            else:
#                doc_ref = db.collection(u'info').document(dni.get())
#                doc_ref.set({
#                u'Nombre': nombre.get(),
#                u'Apellido': apellido.get(),
#                u'Correo': correo.get(),
#                u'Telefono': telefono.get()
#                })
#                showinfo(title="Info", message="Usuario subido con exito")
#                return


###Pestañas###

Notebook= ttk.Notebook(root)
Notebook.pack(fill='both', expand='yes')
adjudicaralumno = ttk.Frame(Notebook)
Notebook.add(adjudicaralumno, text="Añadir Alumno")
#organizarclases = ttk.Frame(Notebook)
#Notebook.add(organizarclases, text="Horario")

###Añadir nuevo alumno###

dni= StringVar()
nombre= StringVar()
apellido= StringVar()
correo= StringVar()
telefono= StringVar()
fechainicio = StringVar()
fechafin = StringVar()
Lunes= IntVar()
Martes=IntVar()
Miercoles= IntVar()
Jueves= IntVar()
Viernes= IntVar()
comercio= IntVar()
sala= IntVar()
cocina= IntVar()
horario = StringVar()
Label(adjudicaralumno, text="Nombre:").grid(row=0, column=0)
Entry(adjudicaralumno, textvariable=nombre).grid(row=0, column=1)
Label(adjudicaralumno, text="Apellidos:").grid(row=0, column=2)
Entry(adjudicaralumno, textvariable=apellido).grid(row=0, column=3)
Label(adjudicaralumno, text="Dni:").grid(row=0, column=4)
Entry(adjudicaralumno, textvariable=dni).grid(row=0, column=5)
Label(adjudicaralumno, text="Telefono:").grid(row=0, column=6)
Entry(adjudicaralumno, textvariable=telefono).grid(row=0, column=7)
Label(adjudicaralumno, text="Correo:").grid(row=1, column=0)
Entry(adjudicaralumno, textvariable=correo).grid(row=1, column=1)
Label(adjudicaralumno, text="Fecha inicio:").grid(row=1, column=2)
Entry(adjudicaralumno, textvariable=fechainicio).grid(row=1, column=3)
Label(adjudicaralumno, text="Fecha fin:").grid(row=1, column=4)
Entry(adjudicaralumno, textvariable=fechafin).grid(row=1, column=5)
Label(adjudicaralumno, text="Horario:").grid(row=1, column=6)
Entry(adjudicaralumno, textvariable=horario).grid(row=1, column=7)
Label(adjudicaralumno, text="Lunes:").grid(row=2, column=0)
Checkbutton(adjudicaralumno, variable=Lunes, onvalue=1, offvalue=0).grid(row=2, column=1, sticky="w")
Label(adjudicaralumno, text="Martes:").grid(row=2, column=2)
Checkbutton(adjudicaralumno, variable=Martes, onvalue=1, offvalue=0).grid(row=2, column=3, sticky="w")
Label(adjudicaralumno, text="Miercoles:").grid(row=2, column=4)
Checkbutton(adjudicaralumno, variable=Miercoles, onvalue=1, offvalue=0).grid(row=2, column=5, sticky="w")
Label(adjudicaralumno, text="Jueves:").grid(row=2, column=6)
Checkbutton(adjudicaralumno, variable=Jueves, onvalue=1, offvalue=0).grid(row=2, column=7, sticky="w")
Label(adjudicaralumno, text="Viernes:").grid(row=2, column=8)
Checkbutton(adjudicaralumno, variable=Viernes, onvalue=1, offvalue=0).grid(row=2, column=9, sticky="w")

Checkbutton(adjudicaralumno, text="Comercio y administracion", variable=comercio, onvalue=1, offvalue=0).grid(row=3, column=0)
Checkbutton(adjudicaralumno, text="Sala", variable=sala, onvalue=1, offvalue=0).grid(row=3, column=1)
Checkbutton(adjudicaralumno, text="Cocina, pasteleria y reposteria", variable=cocina, onvalue=1, offvalue=0).grid(row=3, column=2)
Button(adjudicaralumno, text="Subir", command=subircomercio).grid(row=50, column=0)
#certificado1 = IntVar()
#certificado2 = IntVar()
#certificado3 = IntVar()
#Radiobutton(adjudicaralumno, variable=certificado1, text="Comercio y administracion", command=crearcertificado1).grid(row=3, column=0)
#Radiobutton(adjudicaralumno, variable=certificado2, text="Sala", command=crearcertificado2).grid(row=3, column=1)
#Radiobutton(adjudicaralumno, variable=certificado3, text="Cocina, pasteleria y reposteria", command=crearcertificado3).grid(row=3, column=2)

###Organizacion de clases###






###Fin de programa###
root.mainloop()