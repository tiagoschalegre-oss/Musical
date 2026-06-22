from tkinter import*
from tkinter import ttk
import os

import pygame
#----------------------------------------------------------------------
def tocar_som(entrada):
  nota = pygame.mixer.Sound(entrada)
  nota.play()

def seletor(event):
  janela = Toplevel()
  janela.config(background='#484886')
  janela.geometry('700x500')

  retorno=Button(janela, image=voltar, width=30, height=30,
                 bg='#484886',
                 activebackground="#484886", activeforeground="#484886",
                 relief='flat',
                 command=lambda: janela.destroy())
  retorno.pack(anchor='nw')

  Label(janela, text="Aperte no botão da música que quer escutar", image=img, compound='top',
        font=("Arial",12, 'bold'),
        fg="#ffffff", bg='#484886').pack(anchor='center')

  frame2=Frame(janela, relief=FLAT)

  b1=Button(frame2, text= 'musga q tiago vai por (1)', command=NONE).pack(side='bottom')
  b2=Button(frame2, text= 'musga q tiago vai por (2)', command=NONE).pack(side='bottom')
  b3=Button(frame2, text= 'musga q tiago vai por (3)', command=NONE).pack(side='bottom')
  b4=Button(frame2, text= 'musga q tiago vai por (4)', command=NONE).pack(side='bottom')

  frame2.pack(padx=100, pady=100)

pygame.mixer.init()

base_dir = os.path.dirname(os.path.abspath(__file__))
notas = os.path.join(base_dir, "Notas")

#§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§

root = Tk()
root.geometry('700x500')

img = PhotoImage(file='pyano.png')
voltar = PhotoImage(file='voltar.png')
lista=PhotoImage(file='lista.png')

salvar=Label(root, image=lista, width=50, height=50, bg='#484886')
salvar.pack(anchor='nw')
salvar.bind("<Button-1>", seletor)

tecla1=PhotoImage(file='tecla2.png')
tecla2=PhotoImage(file='tecla3.png')
tecla3=PhotoImage(file='tecla1.png')
preta = PhotoImage(file='t_preta.png')

root.iconphoto(True, img)

root.config(background="#484886")

frame=Frame(root, relief=FLAT)

Pyano=Label(root, image=img,
            text ='PYANO',
            font=('Lato', 50),
            background="#484886",
            compound='right',
            border=4, padx= 4, pady= 4,
            relief='flat')
Pyano.pack(anchor='center')
#Pyano.bind("<Button-1>", seletor)

#------------------------------------------
Do = Button(frame, image=tecla1,
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "C.wav"))).pack(side=LEFT)
#------------------------------------------
Re = Button(frame, image=tecla2,
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "D.wav"))).pack(side=LEFT)
#------------------------------------------
Mi = Button(frame, image=tecla3,
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "E.wav"))).pack(side=LEFT)
#------------------------------------------
Fa = Button(frame, image=tecla1,
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "F.wav"))).pack(side=LEFT)
#------------------------------------------
Sol = Button(frame, image=tecla2,
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "G.wav"))).pack(side=LEFT)
#------------------------------------------
La = Button(frame, image=tecla3,
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "A.wav"))).pack(side=LEFT)
#------------------------------------------
Si = Button(frame, image=tecla1,
             width=30, height=130, 
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "B.wav"))).pack(side=LEFT)
#------------------------------------------
Do1 = Button(frame, image=tecla3,
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "C1.wav"))).pack(side=LEFT)
#------------------------------------------
Do_s = Button(frame, image=tecla3,
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "C_s.wav"))).pack(side=LEFT)
#------------------------------------------
RE_s= Button(frame, image=tecla3,
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "D_s.wav"))).pack(side=LEFT)
#------------------------------------------
Fa_s = Button(frame, image=tecla3,
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "F_s.wav"))).pack(side=LEFT)
#------------------------------------------
Sol_s = Button(frame, image=tecla3,
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "G_s.wav"))).pack(side=LEFT)
#------------------------------------------
La_s = Button(frame, image=tecla3,
             width=30, height=130,
             bg='#484886' ,activebackground="#484886", activeforeground="#484886",
             relief='flat',
             command=lambda :tocar_som(os.path.join(notas, "Bb.wav"))).pack(side=LEFT)
#------------------------------------------

frame.pack(padx=100, pady=100)

root.mainloop()
