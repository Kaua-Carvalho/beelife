from tkinter import *

import pygame.mixer
from pygame import mixer
from PIL import Image, ImageTk
import pyttsx3

mixer.init()

w=Tk()
w.geometry("360x640")

###################################
#          A U D I O S           #
##################################

########## G E R A L ###########
def Sim():
    pygame.mixer.music.load("audio/Sim.mp3")
    pygame.mixer.music.play(loops=0)
def Nao():
    pygame.mixer.music.load("audio/Não.mp3")
    pygame.mixer.music.play(loops=0)
def Janela():
    pygame.mixer.music.load("audio/Janela.mp3")
    pygame.mixer.music.play(loops=0)
def Luz():
    pygame.mixer.music.load("audio/Luz.mp3")
    pygame.mixer.music.play(loops=0)
def Tv():
    pygame.mixer.music.load("audio/Tv.mp3")
    pygame.mixer.music.play(loops=0)
def Controle():
    pygame.mixer.music.load("audio/Controle.mp3")
    pygame.mixer.music.play(loops=0)
###################################

########### S A L A ############
def Sofa():
    pygame.mixer.music.load("audio/Sofá.mp3")
    pygame.mixer.music.play(loops=0)
def Game():
    pygame.mixer.music.load("audio/Videogame.mp3")
    pygame.mixer.music.play(loops=0)
###################################

######### Q U A R T O ##########
def Cama():
    pygame.mixer.music.load("audio/Cama.mp3")
    pygame.mixer.music.play(loops=0)
def Roupa():
    pygame.mixer.music.load("audio/Roupa.mp3")
    pygame.mixer.music.play(loops=0)
###################################

######## C O Z I N H A #########
def Beber():
    pygame.mixer.music.load("audio/Beber.mp3")
    pygame.mixer.music.play(loops=0)
def Comer():
    pygame.mixer.music.load("audio/Comer.mp3")
    pygame.mixer.music.play(loops=0)
def Mesa():
    pygame.mixer.music.load("audio/Mesa.mp3")
    pygame.mixer.music.play(loops=0)
def Micro():
    pygame.mixer.music.load("audio/Micro-ondas.mp3")
    pygame.mixer.music.play(loops=0)
###################################

####### B A N H E I R O ########
def Banho():
    pygame.mixer.music.load("audio/Banho.mp3")
    pygame.mixer.music.play(loops=0)
def Dente():
    pygame.mixer.music.load("audio/Escovar dente.mp3")
    pygame.mixer.music.play(loops=0)
def Pente():
    pygame.mixer.music.load("audio/Pente.mp3")
    pygame.mixer.music.play(loops=0)
def Vaso():
    pygame.mixer.music.load("audio/Vaso.mp3")
    pygame.mixer.music.play(loops=0)
###################################

########## T E X T O ###########
def Ler():
    s=pyttsx3.init()
    data=entrada.get("1.0",END)
    s.say(data)
    s.runAndWait()
def Clear():
    entrada.delete("1.0",END)
##################################

##################################
#        D E F  S A I R         #
#################################
def v1():
    wsala.destroy()
def v2():
    wquarto.destroy()
def v3():
    wcozinha.destroy()
def v4():
    wbanheiro.destroy()
def v5():
    wsamu.destroy()
def v6():
    wtexto.destroy()
##################################


##################################
#        D E F  T E L A S       #
#################################

########### S A L A ############
def sala():
    global wsala
    wsala=Toplevel()
    wsala.geometry("360x640")
    pygame.mixer.music.load("audio/Sala.mp3")
    pygame.mixer.music.play(loops=0)

    i2x = (Image.open("Imagens/TELASALA.png"))
    i2y = i2x.resize((360, 640), Image.LANCZOS)
    i2 = ImageTk.PhotoImage(i2y)
    i2label = Label(wsala, image=i2)
    i2label.place(x=0, y=0)

    b1=Button(wsala,bg='#FFDE59',text='Voltar',command=v1)
    b1.place(x=20,y=40)

    fotosalax = (Image.open("Imagens/assistir-tv.png"))
    fotosalay = fotosalax.resize((110, 110), Image.LANCZOS)
    fotosala = ImageTk.PhotoImage(fotosalay)
    botaosala = Button(wsala, image=fotosala, width=110, height=110, command=Tv, borderwidth=5, background='#FFDE59',activebackground="#DBBF4C")
    botaosala.grid(row=0, column=0, sticky="w", pady=(100, 20), padx=30)

    fotoquartox = (Image.open("Imagens/controlador-de-tv.png"))
    fotoquartoy = fotoquartox.resize((110, 110), Image.LANCZOS)
    fotoquarto = ImageTk.PhotoImage(fotoquartoy)
    botaoquarto = Button(wsala, image=fotoquarto, width=110, height=110, command=Controle, borderwidth=5,background='#FFDE59', activebackground="#DBBF4C")
    botaoquarto.grid(row=0, column=1, sticky="e", pady=(100, 20), padx=30)

    fotocozinhax = (Image.open("Imagens/controle-de-video-game.png"))
    fotocozinhay = fotocozinhax.resize((110, 110), Image.LANCZOS)
    fotocozinha = ImageTk.PhotoImage(fotocozinhay)
    botaocozinha = Button(wsala, image=fotocozinha, width=110, height=110, command=Game, borderwidth=5,background='#FFDE59', activebackground="#DBBF4C")
    botaocozinha.grid(row=1, column=0, sticky="w", pady=20, padx=30)

    fotobanheirox = (Image.open("Imagens/sofa.png"))
    fotobanheiroy = fotobanheirox.resize((110, 110), Image.LANCZOS)
    fotobanheiro = ImageTk.PhotoImage(fotobanheiroy)
    botaobanheiro = Button(wsala, image=fotobanheiro, width=110, height=110, command=Sofa, borderwidth=5,background='#FFDE59', activebackground="#DBBF4C")
    botaobanheiro.grid(row=1, column=1, sticky="e", pady=20, padx=30)

    fotoemergenciax = (Image.open("Imagens/janelas.png"))
    fotoemergenciay = fotoemergenciax.resize((110, 110), Image.LANCZOS)
    fotoemergencia = ImageTk.PhotoImage(fotoemergenciay)
    botaoemergencia = Button(wsala, image=fotoemergencia, width=110, height=110, command=Janela, borderwidth=5,background='#FFDE59', activebackground="#DBBF4C")
    botaoemergencia.grid(row=2, column=0, sticky="w", pady=20, padx=30)

    fototextox = (Image.open("Imagens/lampada.png"))
    fototextoy = fototextox.resize((110, 110), Image.LANCZOS)
    fototexto = ImageTk.PhotoImage(fototextoy)
    botaotexto = Button(wsala, image=fototexto, width=110, height=110, command=Luz, borderwidth=5, background='#FFDE59',activebackground="#DBBF4C")
    botaotexto.grid(row=2, column=1, sticky="e", pady=20, padx=30)

    botaocheck = Button(wsala, text="Sim", bg='#FFDE59', command=Sim, width=15, height=2, activebackground="#DBBF4C")
    botaocheck.grid(row=3, column=0, sticky="w", pady=20, padx=30)
    botaocross = Button(wsala, text="Não", bg='#FFDE59', command=Nao, width=15, height=2, activebackground="#DBBF4C")
    botaocross.grid(row=3, column=1, sticky="e", pady=20, padx=30)


    wsala.mainloop()
#######################################################################################################################

######### Q U A R T O ##########
def quarto():
    global wquarto
    wquarto=Toplevel()
    wquarto.geometry("360x640")
    pygame.mixer.music.load("audio/Quarto.mp3")
    pygame.mixer.music.play(loops=0)

    i3x = (Image.open("Imagens/TELAQUARTO.png"))
    i3y = i3x.resize((360, 640), Image.LANCZOS)
    i3 = ImageTk.PhotoImage(i3y)
    i3label = Label(wquarto, image=i3)
    i3label.place(x=0, y=0)

    b1 = Button(wquarto, bg='#FFDE59', text='Voltar', command=v2)
    b1.place(x=20, y=40)

    fotosalax = (Image.open("Imagens/assistir-tv.png"))
    fotosalay = fotosalax.resize((110, 110), Image.LANCZOS)
    fotosala = ImageTk.PhotoImage(fotosalay)
    botaosala = Button(wquarto, image=fotosala, width=110, height=110, command=Tv, borderwidth=5, background='#FFDE59',activebackground="#DBBF4C")
    botaosala.grid(row=0, column=0, sticky="w", pady=(100, 20), padx=30)

    fotoquartox = (Image.open("Imagens/controlador-de-tv.png"))
    fotoquartoy = fotoquartox.resize((110, 110), Image.LANCZOS)
    fotoquarto = ImageTk.PhotoImage(fotoquartoy)
    botaoquarto = Button(wquarto, image=fotoquarto, width=110, height=110, command=Controle, borderwidth=5,background='#FFDE59', activebackground="#DBBF4C")
    botaoquarto.grid(row=0, column=1, sticky="e", pady=(100, 20), padx=30)

    fotocozinhax = (Image.open("Imagens/cama-de-casal.png"))
    fotocozinhay = fotocozinhax.resize((110, 110), Image.LANCZOS)
    fotocozinha = ImageTk.PhotoImage(fotocozinhay)
    botaocozinha = Button(wquarto, image=fotocozinha, width=110, height=110, command=Cama, borderwidth=5,background='#FFDE59', activebackground="#DBBF4C")
    botaocozinha.grid(row=1, column=0, sticky="w", pady=20, padx=30)

    fotobanheirox = (Image.open("Imagens/guarda-roupa.png"))
    fotobanheiroy = fotobanheirox.resize((110, 110), Image.LANCZOS)
    fotobanheiro = ImageTk.PhotoImage(fotobanheiroy)
    botaobanheiro = Button(wquarto, image=fotobanheiro, width=110, height=110, command=Roupa, borderwidth=5,background='#FFDE59', activebackground="#DBBF4C")
    botaobanheiro.grid(row=1, column=1, sticky="e", pady=20, padx=30)

    fotoemergenciax = (Image.open("Imagens/janelas.png"))
    fotoemergenciay = fotoemergenciax.resize((110, 110), Image.LANCZOS)
    fotoemergencia = ImageTk.PhotoImage(fotoemergenciay)
    botaoemergencia = Button(wquarto, image=fotoemergencia, width=110, height=110, command=Janela, borderwidth=5,background='#FFDE59', activebackground="#DBBF4C")
    botaoemergencia.grid(row=2, column=0, sticky="w", pady=20, padx=30)

    fototextox = (Image.open("Imagens/lampada.png"))
    fototextoy = fototextox.resize((110, 110), Image.LANCZOS)
    fototexto = ImageTk.PhotoImage(fototextoy)
    botaotexto = Button(wquarto, image=fototexto, width=110, height=110, command=Luz, borderwidth=5,background='#FFDE59', activebackground="#DBBF4C")
    botaotexto.grid(row=2, column=1, sticky="e", pady=20, padx=30)

    botaocheck = Button(wquarto, text="Sim", bg='#FFDE59', command=Sim, width=15, height=2, activebackground="#DBBF4C")
    botaocheck.grid(row=3, column=0, sticky="w", pady=20, padx=30)
    botaocross = Button(wquarto, text="Não", bg='#FFDE59', command=Nao, width=15, height=2, activebackground="#DBBF4C")
    botaocross.grid(row=3, column=1, sticky="e", pady=20, padx=30)

    wquarto.mainloop()
#######################################################################################################################

######## C O Z I N H A  #########
def cozinha():
    global wcozinha
    wcozinha=Toplevel()
    wcozinha.geometry("360x640")
    pygame.mixer.music.load("audio/Cozinha.mp3")
    pygame.mixer.music.play(loops=0)

    i3x = (Image.open("Imagens/TELACOZINHA.png"))
    i3y = i3x.resize((360, 640), Image.LANCZOS)
    i3 = ImageTk.PhotoImage(i3y)
    i3label = Label(wcozinha, image=i3)
    i3label.place(x=0, y=0)

    b1 = Button(wcozinha, bg='#FFDE59', text='Voltar', command=v3)
    b1.place(x=20, y=40)

    fotosalax = (Image.open("Imagens/copo-de-agua.png"))
    fotosalay = fotosalax.resize((110, 110), Image.LANCZOS)
    fotosala = ImageTk.PhotoImage(fotosalay)
    botaosala = Button(wcozinha, image=fotosala, width=110, height=110, command=Beber, borderwidth=5, background='#FFDE59',activebackground="#DBBF4C")
    botaosala.grid(row=0, column=0, sticky="w", pady=(100, 20), padx=30)

    fotoquartox = (Image.open("Imagens/prato.png"))
    fotoquartoy = fotoquartox.resize((110, 110), Image.LANCZOS)
    fotoquarto = ImageTk.PhotoImage(fotoquartoy)
    botaoquarto = Button(wcozinha, image=fotoquarto, width=110, height=110, command=Comer, borderwidth=5,background='#FFDE59', activebackground="#DBBF4C")
    botaoquarto.grid(row=0, column=1, sticky="e", pady=(100, 20), padx=30)

    fotocozinhax = (Image.open("Imagens/mesa.png"))
    fotocozinhay = fotocozinhax.resize((110, 110), Image.LANCZOS)
    fotocozinha = ImageTk.PhotoImage(fotocozinhay)
    botaocozinha = Button(wcozinha, image=fotocozinha, width=110, height=110, command=Mesa, borderwidth=5,background='#FFDE59', activebackground="#DBBF4C")
    botaocozinha.grid(row=1, column=0, sticky="w", pady=20, padx=30)

    fotobanheirox = (Image.open("Imagens/microwave.png"))
    fotobanheiroy = fotobanheirox.resize((110, 110), Image.LANCZOS)
    fotobanheiro = ImageTk.PhotoImage(fotobanheiroy)
    botaobanheiro = Button(wcozinha, image=fotobanheiro, width=110, height=110, command=Micro, borderwidth=5,background='#FFDE59', activebackground="#DBBF4C")
    botaobanheiro.grid(row=1, column=1, sticky="e", pady=20, padx=30)

    fotoemergenciax = (Image.open("Imagens/janelas.png"))
    fotoemergenciay = fotoemergenciax.resize((110, 110), Image.LANCZOS)
    fotoemergencia = ImageTk.PhotoImage(fotoemergenciay)
    botaoemergencia = Button(wcozinha, image=fotoemergencia, width=110, height=110, command=Janela, borderwidth=5,background='#FFDE59', activebackground="#DBBF4C")
    botaoemergencia.grid(row=2, column=0, sticky="w", pady=20, padx=30)

    fototextox = (Image.open("Imagens/lampada.png"))
    fototextoy = fototextox.resize((110, 110), Image.LANCZOS)
    fototexto = ImageTk.PhotoImage(fototextoy)
    botaotexto = Button(wcozinha, image=fototexto, width=110, height=110, command=Luz, borderwidth=5,background='#FFDE59', activebackground="#DBBF4C")
    botaotexto.grid(row=2, column=1, sticky="e", pady=20, padx=30)

    botaocheck = Button(wcozinha, text="Sim", bg='#FFDE59', command=Sim, width=15, height=2, activebackground="#DBBF4C")
    botaocheck.grid(row=3, column=0, sticky="w", pady=20, padx=30)
    botaocross = Button(wcozinha, text="Não", bg='#FFDE59', command=Nao, width=15, height=2, activebackground="#DBBF4C")
    botaocross.grid(row=3, column=1, sticky="e", pady=20, padx=30)

    wcozinha.mainloop()
#######################################################################################################################

####### B A N H E I R O ########
def banheiro():
    global wbanheiro
    wbanheiro=Toplevel()
    wbanheiro.geometry("360x640")
    pygame.mixer.music.load("audio/Banheiro.mp3")
    pygame.mixer.music.play(loops=0)

    i3x = (Image.open("Imagens/TELABANHEIRO.png"))
    i3y = i3x.resize((360, 640), Image.LANCZOS)
    i3 = ImageTk.PhotoImage(i3y)
    i3label = Label(wbanheiro, image=i3)
    i3label.place(x=0, y=0)

    b1 = Button(wbanheiro, bg='#FFDE59', text='Voltar', command=v4)
    b1.place(x=20, y=40)

    fotosalax = (Image.open("Imagens/banho.png"))
    fotosalay = fotosalax.resize((110, 110), Image.LANCZOS)
    fotosala = ImageTk.PhotoImage(fotosalay)
    botaosala = Button(wbanheiro, image=fotosala, width=110, height=110, command=Banho, borderwidth=5, background='#FFDE59',activebackground="#DBBF4C")
    botaosala.grid(row=0, column=0, sticky="w", pady=(100, 20), padx=30)

    fotoquartox = (Image.open("Imagens/escova-de-dente.png"))
    fotoquartoy = fotoquartox.resize((110, 110), Image.LANCZOS)
    fotoquarto = ImageTk.PhotoImage(fotoquartoy)
    botaoquarto = Button(wbanheiro, image=fotoquarto, width=110, height=110, command=Dente, borderwidth=5,background='#FFDE59', activebackground="#DBBF4C")
    botaoquarto.grid(row=0, column=1, sticky="e", pady=(100, 20), padx=30)

    fotocozinhax = (Image.open("Imagens/pente-de-cabelo.png"))
    fotocozinhay = fotocozinhax.resize((110, 110), Image.LANCZOS)
    fotocozinha = ImageTk.PhotoImage(fotocozinhay)
    botaocozinha = Button(wbanheiro, image=fotocozinha, width=110, height=110, command=Pente, borderwidth=5,background='#FFDE59', activebackground="#DBBF4C")
    botaocozinha.grid(row=1, column=0, sticky="w", pady=20, padx=30)

    fotobanheirox = (Image.open("Imagens/vaso-sanitario.png"))
    fotobanheiroy = fotobanheirox.resize((110, 110), Image.LANCZOS)
    fotobanheiro = ImageTk.PhotoImage(fotobanheiroy)
    botaobanheiro = Button(wbanheiro, image=fotobanheiro, width=110, height=110, command=Vaso, borderwidth=5,background='#FFDE59', activebackground="#DBBF4C")
    botaobanheiro.grid(row=1, column=1, sticky="e", pady=20, padx=30)

    fotoemergenciax = (Image.open("Imagens/janelas.png"))
    fotoemergenciay = fotoemergenciax.resize((110, 110), Image.LANCZOS)
    fotoemergencia = ImageTk.PhotoImage(fotoemergenciay)
    botaoemergencia = Button(wbanheiro, image=fotoemergencia, width=110, height=110, command=Janela, borderwidth=5,background='#FFDE59', activebackground="#DBBF4C")
    botaoemergencia.grid(row=2, column=0, sticky="w", pady=20, padx=30)

    fototextox = (Image.open("Imagens/lampada.png"))
    fototextoy = fototextox.resize((110, 110), Image.LANCZOS)
    fototexto = ImageTk.PhotoImage(fototextoy)
    botaotexto = Button(wbanheiro, image=fototexto, width=110, height=110, command=Luz, borderwidth=5,background='#FFDE59', activebackground="#DBBF4C")
    botaotexto.grid(row=2, column=1, sticky="e", pady=20, padx=30)

    botaocheck = Button(wbanheiro, text="Sim", bg='#FFDE59', command=Sim, width=15, height=2, activebackground="#DBBF4C")
    botaocheck.grid(row=3, column=0, sticky="w", pady=20, padx=30)
    botaocross = Button(wbanheiro, text="Não", bg='#FFDE59', command=Nao, width=15, height=2, activebackground="#DBBF4C")
    botaocross.grid(row=3, column=1, sticky="e", pady=20, padx=30)

    wbanheiro.mainloop()
#######################################################################################################################

##### E M E R G E N C I A ######
def emergencia():
    global wsamu
    wsamu = Toplevel()
    wsamu.geometry("360x640")
    pygame.mixer.music.load("audio/Emergência.mp3")
    pygame.mixer.music.play(loops=3)

    i3x = (Image.open("Imagens/TELASAMU.png"))
    i3y = i3x.resize((360, 640), Image.LANCZOS)
    i3 = ImageTk.PhotoImage(i3y)
    i3label = Label(wsamu, image=i3)
    i3label.place(x=0, y=0)

    b1 = Button(wsamu, bg='black',fg='white', text='Cancelar', command=v5,width=15)
    b1.place(x=125, y=590)

    wsamu.mainloop()
#######################################################################################################################

########## T E X T O ###########
def texto():
    global entrada
    global wtexto
    wtexto = Toplevel()
    wtexto.geometry("360x640")
    pygame.mixer.music.load("audio/Texto.mp3")
    pygame.mixer.music.play(loops=0)

    i3x = (Image.open("Imagens/Bem-Vindo ao Assistente Auditivo.png"))
    i3y = i3x.resize((360, 640), Image.LANCZOS)
    i3 = ImageTk.PhotoImage(i3y)
    i3label = Label(wtexto, image=i3)
    i3label.place(x=0, y=0)
    fotocheckx=(Image.open("Imagens/alto-falante-de-audio.png"))
    fotochecky=fotocheckx.resize((50,50), Image.LANCZOS)
    fotocheck=ImageTk.PhotoImage(fotochecky)
    fotoxx=(Image.open("Imagens/x.png"))
    fotoxy=fotoxx.resize((50,50), Image.LANCZOS)
    fotox=ImageTk.PhotoImage(fotoxy)
    b1 = Button(wtexto, bg='#FFDE59', text='Voltar', command=v6)
    b1.place(x=20, y=40)
    entrada=Text(wtexto,width=35,height=4,font='15')
    entrada.grid(pady=(160,10),padx=20,columnspan=2)
    bo1=Button(wtexto,image=fotocheck,width=50,height=50,command=Ler,bg='#FFDE59')
    bo1.grid(row=1,column=0,padx=20)
    bo2=Button(wtexto,image=fotox,width=50,height=50,command=Clear,bg='#FFDE59')
    bo2.grid(row=1,column=1,padx=20)

    botaocheck = Button(wtexto, text="Sim", bg='#FFDE59', command=Sim, width=15, height=2,activebackground="#DBBF4C")
    botaocheck.grid(row=3, column=0, sticky="w", pady=280, padx=30)
    botaocross = Button(wtexto, text="Não", bg='#FFDE59', command=Nao, width=15, height=2,activebackground="#DBBF4C")
    botaocross.grid(row=3, column=1, sticky="e", pady=280, padx=30)

    wtexto.mainloop()
#######################################################################################################################

##################################
#  T E L A  P R I N C I P A L   #
#################################

i1x=(Image.open("Imagens/i1.png"))
i1y=i1x.resize((360,640),Image.LANCZOS)
i1=ImageTk.PhotoImage(i1y)
i1label=Label(w,image=i1)
i1label.place(x=0,y=0)

fotosalax=(Image.open("Imagens/sala-de-estar.png"))
fotosalay=fotosalax.resize((110,110),Image.LANCZOS)
fotosala=ImageTk.PhotoImage(fotosalay)
botaosala=Button(w,image=fotosala,width=110,height=110,command=sala,borderwidth=5,background='#FFDE59',activebackground="#DBBF4C")
botaosala.grid(row=0,column=0,sticky="w",pady=(100,20),padx=30)

fotoquartox=(Image.open("Imagens/quarto.png"))
fotoquartoy=fotoquartox.resize((110,110),Image.LANCZOS)
fotoquarto=ImageTk.PhotoImage(fotoquartoy)
botaoquarto=Button(w,image=fotoquarto,width=110,height=110,command=quarto,borderwidth=5,background='#FFDE59',activebackground="#DBBF4C")
botaoquarto.grid(row=0,column=1,sticky="e",pady=(100,20),padx=30)

fotocozinhax=(Image.open("Imagens/cozinha.png"))
fotocozinhay=fotocozinhax.resize((110,110),Image.LANCZOS)
fotocozinha=ImageTk.PhotoImage(fotocozinhay)
botaocozinha=Button(w,image=fotocozinha,width=110,height=110,command=cozinha,borderwidth=5,background='#FFDE59',activebackground="#DBBF4C")
botaocozinha.grid(row=1,column=0,sticky="w",pady=20,padx=30)

fotobanheirox=(Image.open("Imagens/banheiro-publico.png"))
fotobanheiroy=fotobanheirox.resize((110,110),Image.LANCZOS)
fotobanheiro=ImageTk.PhotoImage(fotobanheiroy)
botaobanheiro=Button(w,image=fotobanheiro,width=110,height=110,command=banheiro,borderwidth=5,background='#FFDE59',activebackground="#DBBF4C")
botaobanheiro.grid(row=1,column=1,sticky="e",pady=20,padx=30)

fotoemergenciax=(Image.open("Imagens/servico-medico.png"))
fotoemergenciay=fotoemergenciax.resize((110,110),Image.LANCZOS)
fotoemergencia=ImageTk.PhotoImage(fotoemergenciay)
botaoemergencia=Button(w,image=fotoemergencia,width=110,height=110,command=emergencia,borderwidth=5,background='#FFDE59',activebackground="#DBBF4C")
botaoemergencia.grid(row=2,column=0,sticky="w",pady=20,padx=30)

fototextox=(Image.open("Imagens/caixa-de-texto.png"))
fototextoy=fototextox.resize((110,110),Image.LANCZOS)
fototexto=ImageTk.PhotoImage(fototextoy)
botaotexto=Button(w,image=fototexto,width=110,height=110,command=texto,borderwidth=5,background='#FFDE59',activebackground="#DBBF4C")
botaotexto.grid(row=2,column=1,sticky="e",pady=20,padx=30)

botaocheck=Button(w,text="Sim",bg='#FFDE59',command=Sim,width=15,height=2,activebackground="#DBBF4C")
botaocheck.grid(row=3,column=0,sticky="w",pady=20,padx=30)
botaocross=Button(w,text="Não",bg='#FFDE59',command=Nao,width=15,height=2,activebackground="#DBBF4C")
botaocross.grid(row=3,column=1,sticky="e",pady=20,padx=30)


w.mainloop()
#######################################################################################################################