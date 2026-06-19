from tkinter import*
from tkinter import ttk
import os

import pygame
#----------------------------------------------------------------------
def tocar_som(entrada):
  nota = pygame.mixer.Sound(entrada)
  nota.play()

pygame.mixer.init()

base_dir = os.path.dirname(os.path.abspath(__file__))
notas = os.path.join(base_dir, "Notas")

#§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§

root = Tk()
root.geometry('600x400')
#
#janela = ttk.Notebook(root)
#seletor1 = Frame(janela)
#seletor2 = Frame(janela)
#janela.add(seletor1, text= 'Início')
#janela.add(seletor2, text= 'Seleção de músicas')
#janela.pack()

#Label(janela, text="Aperte no botão da música que quer escutar", font=("Arial",12)).pack()

img = PhotoImage(file='pyano.png')

tecla1=PhotoImage(file='tecla2.png')
tecla2=PhotoImage(file='tecla3.png')
tecla3=PhotoImage(file='tecla1.png')
preta = PhotoImage(file='t_preta.png')

root.iconphoto(True, img)

root.config(background="#484886")

frame=Frame(root, relief=FLAT)

Do = Button(frame, image=tecla1,
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=lambda :tocar_som(os.path.join(notas, "Do.wav"))).pack(side=LEFT)
#------------------------------------------
Re = Button(frame, image=tecla2,
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=lambda :tocar_som(os.path.join(notas, "Re.wav"))).pack(side=LEFT)
#------------------------------------------
Mi = Button(frame, image=tecla3,
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=lambda :tocar_som(os.path.join(notas, "Mi.wav"))).pack(side=LEFT)
#------------------------------------------
Fa = Button(frame, image=tecla1,
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=lambda :tocar_som(os.path.join(notas, "Fa.wav"))).pack(side=LEFT)
#------------------------------------------
Sol = Button(frame, image=tecla2,
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=lambda :tocar_som(os.path.join(notas, "Sol.wav"))).pack(side=LEFT)
#------------------------------------------
La = Button(frame, image=tecla3,
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=lambda :tocar_som(os.path.join(notas, "La.wav"))).pack(side=LEFT)
#------------------------------------------
Si = Button(frame, image=tecla1,
             width=30, height=130, 
             activebackground='#000000', activeforeground='#000000',
             command=lambda :tocar_som(os.path.join(notas, "Si.mp3"))).pack(side=LEFT)
#------------------------------------------
Do_ = Button(frame, image=tecla3,
             width=30, height=130,
             activebackground='#000000', activeforeground="#000000",
             command=lambda :tocar_som(os.path.join(notas, "Do#.wav"))).pack(side=LEFT)
#------------------------------------------

frame.grid(padx=100, pady=100)

root.mainloop()