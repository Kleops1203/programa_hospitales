# Proyecto Programación básica
# Manipulación de información por medio de archivos
# Programa para manejo de información dentro dde hospitales
# Python 3.8
# Se detalla el uso de cada módulo, en este caso utilizamos tkinter para poder realizarlo de manera visual
# Audrey Samantha Bhor López - 22545 | Fernando Echeverria Leal - 22610 | Isabella Miralles Penagos - 22293 | Ruth De León Morataya - 22428

from tkinter import * # Importamos todas las herramientas de tkinter (constructor)
from tkinter import ttk,messagebox # ttk para que sea un agenda y messagebox para mensajes al usuario. 
import os # guardar datos.
from tkinter import filedialog # Sistema de archivos del computador. 
import pickle # vuelca los datos en bytes. 

###################### Inicio del contructor #################################################
v = Tk()
v.geometry("600x650")
v.title("Registros para hospitales")
sheet = ttk.Notebook(v,width=500,height=500)
sheet.place(x=10,y=5)
p1 = ttk.Frame(sheet)
p2 = ttk.Frame(sheet)
sheet.add(p1,text="1. Datos Personales")
l1 = Label(p1,text="Por favor ingrese todos los datos solicitados de los pacientes \n para poder llevar un mejor control")
l1.place(x=100,y=10)
norden=IntVar()
norden.set(0)
e1 = Label(p1,text="# de registro: ")
e1.place(x=80,y=60)
t1 = Entry(p1, state="readonly",textvariable=norden)

t1.place(x=250,y=60)
sheet.add(p2,text="2. Consulta General")

l2 = Label(p1,text="Nombres del paciente: ")
l2.place(x=80,y=80)
tx2 = Entry(p1)
tx2.place(x=250,y=80)

lb3 = Label(p1,text="Apellidos: ")
lb3.place(x=80,y=100)
tx3 = Entry(p1)
tx3.place(x=250,y=100)

lb4 = Label(p1,text="# de DPI: ")
lb4.place(x=80,y=120)
tx4 = Entry(p1)
tx4.place(x=250,y=120)

lb5 = Label(p1,text="Telefóno Móvil: ")
lb5.place(x=80,y=140)
tx5 = Entry(p1, width="20")
tx5.place(x=250,y=140)

lb6 = Label(p1,text="Resultado de prueba: ")
lb6.place(x=80,y=160)
tx6 = ttk.Combobox(p1, values=["Positivo", "Negativo"], width=17, state="readonly")
tx6.place(x=250,y=160)

lb7 = Label(p1,text="Fecha: ")
lb7.place(x=80,y=180)
tx7 = Entry(p1)
tx7.place(x=250,y=180)


lb8 = Label(p1,text="Síntomas:")
lb8.place(x=80,y=200)
tx8 = ttk.Combobox(p1, values=["Fiebre, tos seca, fatiga, odinofagia", "SO2<90%, Frecuancia respiraoria leve", "SDRA, Perdida de conocimiento "], width =30, state="readonly") # idea 1,2,3
tx8.place(x=250,y=200)

lb9 = Label(p1,text="Sede:")
lb9.place(x=80,y=220)
tx9 = Entry(p1)
tx9.place(x=250,y=220)

lb10 = Label(p1,text="Correo electrónico:")
lb10.place(x=80,y=240)
tx10 = Entry(p1)
tx10.place(x=250,y=240)

lb11 = Label(p1,text="Dirección:")
lb11.place(x=80,y=220)
tx11 = Entry(p1)
tx11.place(x=250,y=220)


t2=Text(p2,width="70",height="70")
t2.place(x=35,y=40)
###################### Fin del contructor #################################################

global rutaT # Ruta general del archivo en el programa 

def crear_abrir(): # Función de crear y abrir
    global rutaT 
    respuesta=messagebox.askquestion("pregunta","¿Deseas crear el archivo?")
    if(respuesta=="yes"):
        rutaT=filedialog.asksaveasfilename(filetypes=(("Texto","*.txt"),),title="Crear")
        rutaT=rutaT+".txt"
        if(not(os.path.isfile(rutaT))):
            archivo=open(rutaT,"wb")
            archivo.close()
    
    else:
        rutaT=filedialog.askopenfilename(filetypes=(("Texto","*.txt"),),title="Abrir")
        if (os.path.isfile(rutaT)):
            archivo=open(rutaT,"ab")
            archivo.close()
    bt1.config(state="normal")
    bt2.config(state="normal")
    bt3.config(state="normal")
    bt4.config(state="normal")
    #max=os.path.getsize(rutaT)
    #norden.set(int((max/180)+1))
bt = Button(p1,text="Crear/Abrir Archivo",command=crear_abrir)
bt.place(x=110,y=250)
##################################################################################################
def ingresar(): # Función de ingresar
    if tx2.get() == "" and tx3.get() == "" and tx4.get() == "" and tx5.get() == "" and tx6.get() == "" and tx7.get() == "" and tx8.get() == "" and tx9.get() == "":
        messagebox.showerror("Error","Por favor ingrese todos los datos solicitados")
    else: 
        global rutaT
        f=open(rutaT,"ab")
        norden=int(t1.get())
        nombre=tx2.get()+"                              " #30
        apellido=tx3.get()+"                              "
        dpi=tx4.get()+"                              "
        tfijo=tx5.get()+"               "
        resultado=tx6.get()+"               "
        fecha=tx7.get()+"               "
        sintomas=tx8.get()+"               "
        sede=tx9.get()+"               "
        nombre=nombre[0:29]
        apellido=apellido[0:29]
        direc=direc[0:28]
        dpi=dpi[0:14]
        tfijo=tfijo[0:14]
        correo=correo[0:14]
        registro=[norden,nombre,apellido,dpi,tfijo, resultado, fecha, sintomas, sede]
        pickle.dump(registro,f)
        f.close()
        
        norden=norden+1
        t1.config(state="normal")
        t1.delete("0","end")
        t1.insert(INSERT,norden)
        t1.config(state="disabled")
        tx2.delete("0","end")
        tx3.delete("0","end")
        tx4.delete("0","end")
        tx5.delete("0","end")
        tx6.delete("0","end")
        tx7.delete("0","end")
        tx8.delete("0","end")
        tx9.delete("0","end")
bt1 = Button(p1,text="Ingresar",state="disabled",command=ingresar)
bt1.place(x=250,y=250)
##################################################################################################
def consultagen():# Función de consulta general de datos
    global rutaT
    br=open(rutaT,"rb")
    max=os.path.getsize(rutaT)
    pos=0
    acu=""
    t2.delete("1.0","end")
    while (pos<max):
        
        reg=pickle.load(br)
        acu=acu+"-".join((str(n).strip() for n in reg))+"\n"
        pos=br.tell()
        
    t2.insert(INSERT,acu)
    br.close()
bt2 = Button(p2,text="Consulta General",state="disabled",command=consultagen)
bt2.place(x=150,y=10)
##########################################################################################    
def buscardat(): # Función de buscar
    global rutaT
    br=open(rutaT,"rb")

    if busqueda.get() == "" or busqueda.get().isalpha() :
        messagebox.showerror("Error","Debe de ingresar el número de registro")
    else:
        
        br=open(rutaT,"rb")
        tx2.delete(0,END)
        tx3.delete(0,END)
        tx4.delete(0,END)
        tx5.delete(0,END)
        tx6.delete(0,END)
        tx7.delete(0,END)
        tx8.delete(0,END)
        tx9.delete(0,END)
        num=int(busqueda.get())
        t1.config(state="normal")
        t1.delete("0","end")
        t1.insert(INSERT,num)
        size=180
        max=os.path.getsize(rutaT)
        if ((max>((num-1)*size)) and (((num-1)*size)>=0)):
            br.seek((num-1)*size)
            reg=pickle.load(br)
            tx2.insert(INSERT,reg[1])
            tx3.insert(INSERT,reg[2])
            tx4.insert(INSERT,reg[3])
            tx5.insert(INSERT,reg[4])
            tx6.insert(INSERT,reg[5])
            tx7.insert(INSERT,reg[6])
            tx8.insert(INSERT,reg[7])
            tx9.insert(INSERT,reg[8])
        
        br.close()
        
bt3 = Button(p1,text="Busqueda",command=buscardat, state="disabled")
bt3.place(x=200,y=290)
###################################################################################################
def modificar(): # Función de modificar datos
    global rutaT
    br=open(rutaT,"rb")

    if busqueda.get() == "" or busqueda.get().isalpha() :
        messagebox.showerror("Error","Debe de ingresar el número de registro")
    else:
        
        br=open(rutaT,"rb")
        max=os.path.getsize(rutaT)
        pos=0
        arr=[]
        cadauno=[]
        t2.delete("1.0","end")
        while(pos<max):
            reg=pickle.load(br)
            arr.append(reg)
            pos=br.tell()
        br.close()
        br=open(rutaT,"wb")
        n1=int(busqueda.get())
        for cadauno in arr:
            if(n1==cadauno[0]):
                nombre=tx2.get()+"                              "
                apellido=tx3.get()+"                              "
                direc=tx4.get()+"                              "
                tmovil=tx5.get()+"               "
                tfijo=tx6.get()+"               "
                correo=tx7.get()+"               "
                año=tx8.get()+"               "
                zona=tx9.get()+"               "
                nombre=nombre[0:29]
                apellido=apellido[0:29]
                direc=direc[0:28]
                tmovil=tmovil[0:14]
                tfijo=tfijo[0:14]
                correo=correo[0:14]
                año=año[0:14]
                zona=zona[0:14]
                
                norden=n1
                registro=[norden,nombre,apellido,direc,tmovil,tfijo,correo,año,zona]
                pickle.dump(registro,br)
            else:
                pickle.dump(cadauno,br)
        br.close()
bt4= Button(p1,text="Modificar",command=modificar, state="disabled")
bt4.place(x=200,y=350)
####################################################################################################



busqueda=Entry(p1)
busqueda.place(x=170,y=320)



v.mainloop() # fin del constructor y programa 
