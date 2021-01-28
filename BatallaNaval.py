from tkinter import *
import random
ventana=Tk()
ventana.title("Batalla Naval")
ventana.geometry("600x400")
#fondo=PhotoImage(file="dibujos/fondo.gif")
#fondoL=Label(ventana,image=fondo)
#fondoL.img=fondo
#fondoL.place(x=0,y=0)
#CONSTANTES:
Nave1A=PhotoImage(file="dibujos/Nave1.gif")
Nave1B=PhotoImage(file="dibujos/Nave1b.gif")
Nave1D=PhotoImage(file="dibujos/Nave1d.gif")
Nave1I=PhotoImage(file="dibujos/Nave1i.gif")
Nave2A=PhotoImage(file="dibujos/Nave2.gif")
Nave2B=PhotoImage(file="dibujos/Nave2b.gif")
Nave2D=PhotoImage(file="dibujos/Nave2d.gif")
Nave2I=PhotoImage(file="dibujos/Nave2i.gif")
CuadroAzulC=PhotoImage(file="dibujos/CuadroAzulC.gif")
CuadroRojo=PhotoImage(file="dibujos/CuadroRojo.gif")
CuadroGris=PhotoImage(file="dibujos/CuadroGris.gif")
CuadroAmarillo=PhotoImage(file="dibujos/CuadroAmarillo.gif")
CuadroVerde=PhotoImage(file="dibujos/CuadroVerde.gif")
jugador1=""
jugador2=""
juego=""
Boton5=PhotoImage(file="dibujos/botones/N5.gif")
Boton4=PhotoImage(file="dibujos/botones/N4.gif")
Boton3=PhotoImage(file="dibujos/botones/N3.gif")
Boton2=PhotoImage(file="dibujos/botones/N2.gif")
BotonG=PhotoImage(file="dibujos/botones/Giro.gif")
CantidadNavesGrandes=1
CantidadNavesMedianas1=1
CantidadNavesMedianas2=2
CantidadNavesPequeñas=4

#Clase Jugador
class jugador:
    def __init__(self,turno,VerFichas=False):
        self.tablero=[]
        self.turno=turno
        if(turno==1):
            for x2 in range(10):
                for y2 in range(10):
                    if(x2%2==0):
                        if(y2%2==0):
                            NC=cuadro(x2*26+25,y2*26+25,25,25,self.turno,False,VerFichas)
                            self.tablero.append(NC)
                        else:
                            NC=cuadro(x2*26+25,y2*26+25,25,25,self.turno,False,VerFichas)
                            self.tablero.append(NC)
                    else:
                        if(y2%2==0):
                            NC=cuadro(x2*26+25,y2*26+25,25,25,self.turno,False,VerFichas)
                            self.tablero.append(NC)
                        else:
                            NC=cuadro(x2*26+25,y2*26+25,25,25,self.turno,False,VerFichas)
                            self.tablero.append(NC)
        else:
            for x2 in range(10):
                for y2 in range(10):
                    if(x2%2==0):
                        if(y2%2==0):
                            NC=cuadro(x2*26+325,y2*26+25,25,25,self.turno,True,VerFichas)
                            self.tablero.append(NC)
                        else:
                            NC=cuadro(x2*26+325,y2*26+25,25,25,self.turno,True,VerFichas)
                            self.tablero.append(NC)
                    else:
                        if(y2%2==0):
                            NC=cuadro(x2*26+325,y2*26+25,25,25,self.turno,True,VerFichas)
                            self.tablero.append(NC)
                        else:
                            NC=cuadro(x2*26+325,y2*26+25,25,25,self.turno,True,VerFichas)
                            self.tablero.append(NC)
        self.puntos=0
        self.nombre=""
    def GetTablero(self):
        return self.tablero
    def SetTablero(self,tablero):
        self.tablero=tablero
    def SetNombre(self,nombre):
        self.nombre=nombre
    def SetPuntos(self,puntos):
        self.puntos=puntos
    def GetNombre(self):
        return self.nombre
    def GetPuntos(self):
        return self.puntos



    
#Clase ficha
class ficha:
    def __init__(self,imagen,largoNav):
        self.imagen=imagen
        self.Largo=largoNav


        
#Clase cuadro
class cuadro:
    def mostrar(self):
        self.Lab.place(x=self.x,y=self.y) #Visible :)
    def nomostrar(self):
        self.Lab.place_forget()# No Visible :O
    def mostrarFicha(self):
        if(not self.LabF==""):
            self.LabF.place(x=self.x+2,y=self.y+2)
    def nomostrarFicha(self):
        if(not self.LabF==""):
            self.LabF.place_forget()
    def en(self,event):
        if(not self.disponible or not self.enJuego):return
        if(self.equipo==1):
            self.Lab.config(image=CuadroRojo)
            self.Lab.img=CuadroRojo
        else:
            self.Lab.config(image=CuadroAmarillo)
            self.Lab.img=CuadroAmarillo
    def fuera(self,event):
        if(not self.disponible or not self.enJuego):return
        self.Lab.config(image=CuadroAzulC)
        self.Lab.img=CuadroAzulC
    def Impacto(self):
        if(self.ficha!=""):
            self.Lab.config(image=CuadroGris)
            self.Lab.img=CuadroGris
            self.mostrarFicha()
        else:
            self.Lab.config(image=CuadroGris)
            self.Lab.img=CuadroGris
        CambiarActivo(self)
    def GetLab(self):
        return self.Lab
    def GetLabF(self):
        return self.LabF
    def crearFicha(self,ficha):
        if(ficha==""):
            if(self.LabF!=""):
                self.LabF.destroy()
            self.LabF=""
            self.ficha=""
            return
        self.ficha=ficha
        self.LabF=Label(ventana,image=self.ficha.imagen,width=self.ancho-4,height=self.alto-4,borderwidth=0,bg="#99D9EA")
        self.LabF.img=self.ficha.imagen
        self.LabF.place(x=self.x+2,y=self.y+2)
        self.LabF.bind("<Enter>",self.en)
        self.LabF.bind("<Leave>",self.fuera)
        self.LabF.bind("<Button-1>",self.seleccion)
        if(not self.VerFichas):
            self.nomostrarFicha()
    def GetFicha(self):
        return self.ficha
    def seleccion(self,event):
        if(self.enJuego and self.disponible):
            self.disponible=False
            self.Impacto()
    def Jugando(self):
        if self.enJuego:
            self.enJuego=False
        else:
            self.enJuego=True
    def __init__(self,x1,y1,ancho,alto,equipo,enJuego,VerFichas,invisible=True,disponible=True):
        Eti=Label(ventana,width=ancho,height=alto,image=CuadroAzulC,borderwidth=0)
        Eti.img=CuadroAzulC
        Eti.place(x=x1,y=y1)
        self.Lab=Eti
        self.x=x1
        self.y=y1
        self.ancho=ancho
        self.alto=alto
        self.equipo=equipo
        self.enJuego=enJuego
        self.VerFichas=VerFichas
        self.ficha=""
        self.LabF=""
        self.Lab.bind("<Enter>",self.en)
        self.Lab.bind("<Leave>",self.fuera)
        self.Lab.bind("<Button-1>",self.seleccion)
        self.disponible=disponible
        if(invisible):
            self.nomostrar()



            
#Clase para colocar fichas
class casillaColocar(cuadro):
    def __init__(self,x1,y1,ancho,alto,jugador,tablero):
        cuadro.__init__(self,x1,y1,ancho,alto,1,True,True,False,True)
        self.NoCas=3
        self.Dir='b'
        self.jugador=jugador
        self.tablero=tablero
        self.valido=False
    def configurar(self,NoCas,Dir):
        self.NoCas=NoCas
        self.Dir=Dir
    def en(self,event):
        xi=self.tablero.index(self)//10
        yi=self.tablero.index(self)%10
        if(self.Dir=='d'):
            if(xi+self.NoCas>10):
                imagen=CuadroRojo
                self.valido=False
            else:
                imagen=CuadroVerde
                self.valido=True
            for x in range(self.NoCas):
                if(x+xi>9):break
                if(self.tablero[(x+xi)*10+yi].GetFicha()!=""):
                    self.valido=False
                    imagen=CuadroRojo
                self.tablero[(x+xi)*10+yi].GetLab().config(image=imagen)
                self.tablero[(x+xi)*10+yi].GetLab().img=imagen
        elif(self.Dir=='i'):
            if(xi-self.NoCas<-1):
                imagen=CuadroRojo
                self.valido=False
            else:
                imagen=CuadroVerde
                self.valido=True
            for x in range(self.NoCas):
                if(xi-x<0):break
                if(self.tablero[(xi-x)*10+yi].GetFicha()!=""):
                    self.valido=False
                    imagen=CuadroRojo
                self.tablero[(xi-x)*10+yi].GetLab().config(image=imagen)
                self.tablero[(xi-x)*10+yi].GetLab().img=imagen
        elif(self.Dir=='a'):
            if(yi-self.NoCas<-1):
                imagen=CuadroRojo
                self.valido=False
            else:
                imagen=CuadroVerde
                self.valido=True
            for y in range(self.NoCas):
                if(yi-y<0):break
                if(self.tablero[xi*10+(yi-y)].GetFicha()!=""):
                    self.valido=False
                    imagen=CuadroRojo
                self.tablero[xi*10+(yi-y)].GetLab().config(image=imagen)
                self.tablero[xi*10+(yi-y)].GetLab().img=imagen
        else:
            if(yi+self.NoCas>10):
                imagen=CuadroRojo
                self.valido=False
            else:
                imagen=CuadroVerde
                self.valido=True
            for y in range(self.NoCas):
                if(y+yi>9):break
                if(self.tablero[xi*10+y+yi].GetFicha()!=""):
                    self.valido=False
                    imagen=CuadroRojo
                self.tablero[xi*10+y+yi].GetLab().config(image=imagen)
                self.tablero[xi*10+y+yi].GetLab().img=imagen
    def fuera(self,event):
        xi=self.tablero.index(self)//10
        yi=self.tablero.index(self)%10
        imagen=CuadroAzulC
        self.valido=False
        if(self.Dir=='d'):
            for x in range(self.NoCas):
                if(x+xi>9):break
                self.tablero[(x+xi)*10+yi].GetLab().config(image=imagen)
                self.tablero[(x+xi)*10+yi].GetLab().img=imagen
        elif(self.Dir=='i'):
            for x in range(self.NoCas):
                if(xi-x<0):break
                self.tablero[(xi-x)*10+yi].GetLab().config(image=imagen)
                self.tablero[(xi-x)*10+yi].GetLab().img=imagen
        elif(self.Dir=='a'):
            for y in range(self.NoCas):
                if(yi-y<0):break
                self.tablero[xi*10+(yi-y)].GetLab().config(image=imagen)
                self.tablero[xi*10+(yi-y)].GetLab().img=imagen
        else:
            for y in range(self.NoCas):
                if(y+yi>9):break
                self.tablero[xi*10+y+yi].GetLab().config(image=imagen)
                self.tablero[xi*10+y+yi].GetLab().img=imagen
    def seleccion(self,event):
        if(self.valido and self.NoCas>0):
            imagen=CuadroAzulC
            xi=self.tablero.index(self)//10
            yi=self.tablero.index(self)%10
            if(self.Dir=='d'):
                NF=ficha(Nave1I,self.NoCas)
                self.tablero[(xi)*10+yi].crearFicha(NF)
                self.jugador.GetTablero()[(xi)*10+yi].crearFicha(NF)
                imagen=CuadroAzulC
                self.tablero[(xi)*10+yi].GetLab().config(image=imagen)
                self.tablero[(xi)*10+yi].GetLab().img=imagen
                for x in range(1,self.NoCas):
                    NF=ficha(Nave2I,self.NoCas)
                    if(xi+x>9):break
                    self.tablero[(x+xi)*10+yi].GetLab().config(image=imagen)
                    self.tablero[(x+xi)*10+yi].GetLab().img=imagen
                    self.tablero[(x+xi)*10+yi].crearFicha(NF)
                    self.jugador.GetTablero()[(x+xi)*10+yi].crearFicha(NF)
            elif(self.Dir=='i'):
                NF=ficha(Nave1D,self.NoCas)
                self.tablero[(xi)*10+yi].crearFicha(NF)
                self.jugador.GetTablero()[(xi)*10+yi].crearFicha(NF)
                imagen=CuadroAzulC
                self.tablero[(xi)*10+yi].GetLab().config(image=imagen)
                self.tablero[(xi)*10+yi].GetLab().img=imagen
                for x in range(1,self.NoCas):
                    NF=ficha(Nave2D,self.NoCas)
                    if(xi-x<0):break
                    self.tablero[(xi-x)*10+yi].crearFicha(NF)
                    self.tablero[(xi-x)*10+yi].GetLab().config(image=imagen)
                    self.tablero[(xi-x)*10+yi].GetLab().img=imagen
                    self.jugador.GetTablero()[(xi-x)*10+yi].crearFicha(NF)
            elif(self.Dir=='a'):
                NF=ficha(Nave1B,self.NoCas)
                self.tablero[(xi)*10+yi].crearFicha(NF)
                self.jugador.GetTablero()[(xi)*10+yi].crearFicha(NF)
                imagen=CuadroAzulC
                self.tablero[(xi)*10+yi].GetLab().config(image=imagen)
                self.tablero[(xi)*10+yi].GetLab().img=imagen
                for y in range(1,self.NoCas):
                    NF=ficha(Nave2B,self.NoCas)
                    if(yi-y<0):break
                    self.tablero[xi*10+(yi-y)].crearFicha(NF)
                    self.tablero[xi*10+(yi-y)].GetLab().config(image=imagen)
                    self.tablero[xi*10+(yi-y)].GetLab().img=imagen
                    self.jugador.GetTablero()[xi*10+(yi-y)].crearFicha(NF)
            else:
                NF=ficha(Nave1A,self.NoCas)
                self.tablero[(xi)*10+yi].crearFicha(NF)
                self.jugador.GetTablero()[(xi)*10+yi].crearFicha(NF)
                imagen=CuadroAzulC
                self.tablero[(xi)*10+yi].GetLab().config(image=imagen)
                self.tablero[(xi)*10+yi].GetLab().img=imagen
                for y in range(1,self.NoCas):
                    NF=ficha(Nave2A,self.NoCas)
                    if(yi+y>9):break
                    self.tablero[xi*10+y+yi].GetLab().config(image=imagen)
                    self.tablero[xi*10+y+yi].GetLab().img=imagen
                    self.tablero[xi*10+y+yi].crearFicha(NF)
                    self.jugador.GetTablero()[xi*10+y+yi].crearFicha(NF)
            contacto()


                    
def CrearJugadoresYTableros():
    global jugador1,jugador2
    jugador1=jugador(1)
    jugador2=jugador(2)
    jugador1.SetNombre("Edgar")
    jugador2.SetNombre("Daniel")
    #Jugadores y tableros ocultos


    
def CambiarActivo(casilla):
    global jugador1,jugador2,juego
    tab1=jugador1.GetTablero()
    tab2=jugador2.GetTablero()
    if(juego=="2J"):
        for ayudante in tab1:
            ayudante.Jugando()
        for ayudante in tab2:
            ayudante.Jugando()

        
#Colocar fichas:

def ColocarFichas(jugador,jugadores):
    global Tablero,letra,numero,jugador1,jugador2
    global naveG,naveM1,naveM2,naveP,GirarButton,TerminarB,Reiniciar
    global Eti,TipoNave
    Tablero=[]
    letra="b"
    numero=3
    naveG=""
    naveM1=""
    naveM2=""
    naveP=""
    GirarButton=""
    TerminarB=""
    Reiniciar=""
    TipoNave="NM2"
    Eti=""
    for x2 in range(10):
        for y2 in range(10):
            if(x2%2==0):
                if(y2%2==0):
                    NC=casillaColocar(x2*36+170,y2*36+25,35,35,jugador,Tablero)
                    Tablero.append(NC)
                else:
                    NC=casillaColocar(x2*36+170,y2*36+25,35,35,jugador,Tablero)
                    Tablero.append(NC)
            else:
                if(y2%2==0):
                    NC=casillaColocar(x2*36+170,y2*36+25,35,35,jugador,Tablero)
                    Tablero.append(NC)
                else:
                    NC=casillaColocar(x2*36+170,y2*36+25,35,35,jugador,Tablero)
                    Tablero.append(NC)
    Eti=Label(ventana,text=jugador.nombre)
    Eti.place(x=0,y=0)
    naveG=Button(ventana,image=Boton5,command=lambda:conf(letra,5,"NG"),state=NORMAL)
    naveG.img=Boton5
    naveG.place(x=0,y=35)
    naveG.cantidad=CantidadNavesGrandes
    naveG.dispo=True
    naveM1=Button(ventana,image=Boton4,command=lambda:conf(letra,4,"NM1"),state=NORMAL)
    naveM1.img=Boton4
    naveM1.place(x=10,y=70)
    naveM1.cantidad=CantidadNavesMedianas1
    naveM1.dispo=True
    naveM2=Button(ventana,image=Boton3,command=lambda:conf(letra,3,"NM2"),state=NORMAL)
    naveM2.img=Boton3
    naveM2.place(x=20,y=105)
    naveM2.cantidad=CantidadNavesMedianas2
    naveM2.dispo=True
    naveP=Button(ventana,image=Boton2,command=lambda:conf(letra,2,"NP"),state=NORMAL)
    naveP.img=Boton2
    naveP.place(x=30,y=140)
    naveP.cantidad=CantidadNavesPequeñas
    naveP.dispo=True
    TerminarB=Button(ventana,text="Terminar",font=("Algerian",12),command=lambda: terminar(jugadores),state=DISABLED)
    TerminarB.place(x=0,y=210)
    Reiniciar=Button(ventana,text="Reiniciar",font=("Algerian",12),command=lambda: reiniciar(jugador),state=NORMAL)
    Reiniciar.place(x=0,y=245)
    GirarButton=Button(ventana,image=BotonG,command=lambda:conf(giro(letra),numero,TipoNave),state=NORMAL)
    GirarButton.img=BotonG
    GirarButton.place(x=50,y=175)
#funciones al colocar fichas:
def terminar(jugadores):
    global Tablero,naveG,naveM1,naveM2,naveP,GirarButton,jugador1,jugador2,TerminarB,Eti,Reiniciar
    for x in Tablero:
        x.GetLab().destroy()
        if x.GetFicha()!="":
            x.GetLabF().destroy()
        del x
    del Tablero
    naveG.destroy()
    naveM1.destroy()
    naveM2.destroy()
    naveP.destroy()
    GirarButton.destroy()
    TerminarB.destroy()
    Eti.destroy()
    Reiniciar.destroy()
    if(jugadores==2):
        ColocarFichas(jugador2,1)
    else:
        jugar()
    
def conf(letras,casillas,nombre):
    global letra,numero,Tablero,TipoNave
    for x in Tablero:
        x.configurar(casillas,letras)
    TipoNave=nombre
    letra=letras
    numero=casillas
    print("configurado")
def reiniciar(jugador):
    global Tablero,naveG,naveM1,naveM2,naveP,GirarButton,TerminarB
    for x in Tablero:
        x.crearFicha("")#Borra la ficha
    for x in jugador.GetTablero():
        x.crearFicha("")#Borra las fichas :v
    naveG.cantidad=CantidadNavesGrandes
    naveG.config(state=NORMAL)
    naveG.dispo=True
    naveM1.cantidad=CantidadNavesMedianas1
    naveM1.config(state=NORMAL)
    naveM1.dispo=True
    naveM2.cantidad=CantidadNavesMedianas1
    naveM2.config(state=NORMAL)
    naveM2.dispo=True
    naveP.cantidad=CantidadNavesPequeñas
    naveP.config(state=NORMAL)
    naveP.dispo=True
    TerminarB.config(state=DISABLED)
def giro(letra):
    if letra=='b':return 'd'
    if letra=='d':return 'a'
    if letra=='a':return 'i'
    if letra=='i':return 'b'
def contacto():
    '''
    Llamada desde selecion en CasillaColocar
    '''
    print("contacto")
    global colocada,naveG,naveM1,naveM2,naveP,TerminarB,letra
    if(TipoNave=="NG"):
        naveG.cantidad-=1
    elif(TipoNave=="NM1"):
        naveM1.cantidad-=1
    elif(TipoNave=="NM2"):
        naveM2.cantidad-=1
    elif(TipoNave=="NP"):
        naveP.cantidad-=1
    if(naveG.cantidad<=0 and naveG.dispo):
        naveG.config(state=DISABLED)
        conf(letra,0,TipoNave)
        naveG.dispo=False
    elif(naveM1.cantidad<=0 and naveM1.dispo):
        naveM1.config(state=DISABLED)
        conf(letra,0,TipoNave)
        naveM1.dispo=False
    elif(naveM2.cantidad<=0 and naveM2.dispo):
        naveM2.config(state=DISABLED)
        conf(letra,0,TipoNave)
        naveM2.dispo=False
    elif(naveP.cantidad<=0 and naveP.dispo):
        naveP.config(state=DISABLED)
        conf(letra,0,TipoNave)
        naveP.dispo=False
    if(naveG.cantidad<=0 and naveM1.cantidad<=0 and naveM2.cantidad<=0 and naveP.cantidad<=0):
        TerminarB.config(state=NORMAL)
#Funciones de juego:
def juegoDeDos():
    global juego
    juego="2J"
    BorrarMenu()
    ColocarFichas(jugador1,2)
def jugar():
    for x in jugador1.GetTablero():
        x.mostrar()
    for x in jugador2.GetTablero():
        x.mostrar()
def menu():
    global Titulo,Opcion1,Opcion2,Opcion3
    Titulo=Label(ventana,text="BATALLA NAVAL",font=("Comic Sans MS",40))
    Titulo.place(x=20,y=20)
    Opcion1=Button(ventana,text="JUEGO DE DOS JUGADORES",font=("Comic Sans MS",20),command=juegoDeDos)
    Opcion1.place(x=20,y=160)
    Opcion2=Button(ventana,text="JUEGO DE UN JUGADOR",font=("Comic Sans MS",20))
    Opcion2.place(x=20,y=240)
    Opcion3=Button(ventana,text="SALIR",font=("Comic Sans MS",20))
    Opcion3.place(x=20,y=320)
def BorrarMenu():
    global Titulo,Opcion1,Opcion2,Opcion3
    Titulo.destroy()
    Opcion1.destroy()
    Opcion2.destroy()
    Opcion3.destroy()
#Funciones de Juego contra pc:
"""
def ColocarFichasPC(jugador):
    CG=CantidadNavesGrandes
    CM1=CantidadNavesMedianas1
    CM2=CantidadNavesMedianas2
    CP=CantidadNavesPequeñas
    error=True
    while(CG>0):
        g=randint(1,4)
        x=randint(1,8)
        y=randint(1,8)
        while(error):
            for largo in range(5):
                if(g==1):
                    if jugador.GetTablero()[(x-largo)*10+y].GetFicha()!="" or (x-largo)*10+y<0 or (x-largo)*10+y>:
                        error=True
"""
#main():
CrearJugadoresYTableros()
menu()

