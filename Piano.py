from tkinter import*
import pygame
#----------------------------------------------------------------------
def tocar_som(entrada):
  nota = pygame.mixer.Sound(entrada)
  nota.play()

pygame.mixer.init()

#§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§

root = Tk()
root.geometry('600x400')

img = PhotoImage(file='piano.png')
preta = PhotoImage(file='t_preta.png')
root.iconphoto(True, img)

root.config(background="#484886")

Do = Button(root, image=preta,
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=lambda n=str("Do.wav"):tocar_som(n)).pack(side=LEFT)
#------------------------------------------
Re = Button(root, image=preta,
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=lambda n=str("Re.wav"):tocar_som(n)).pack(side=LEFT)
#------------------------------------------
Mi = Button(root, image=preta,
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=lambda n=str("Mi.wav"):tocar_som(n)).pack(side=LEFT)
#------------------------------------------
Fa = Button(root, image=preta,
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=lambda n=str("Fa.wav"):tocar_som(n)).pack(side=LEFT)
#------------------------------------------
Sol = Button(root, image=preta,
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=lambda n=str("Sol.wav"):tocar_som(n)).pack(side=LEFT)
#------------------------------------------
La = Button(root, image=preta,
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=lambda n=str("La.wav"):tocar_som(n)).pack(side=LEFT)
#------------------------------------------
Si = Button(root, image=preta,
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=lambda n=str("Si.mp3"):tocar_som(n)).pack(side=LEFT)
#------------------------------------------
Do_ = Button(root, image=preta,
             width=30, height=130,
             activebackground='#000000', activeforeground='#000000',
             command=lambda n=str("Do#.wav"):tocar_som(n)).pack(side='left')
#------------------------------------------

teclas= Frame(root)

teclas.pack()

root.mainloop()
