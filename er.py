from tkinter import*
import pygame

#----------------------------------------------------------------------

def tocar_som():
  nota =  pygame.mixer.Sound("Do (octave).wav")
  nota.play()

pygame.mixer.init()
#----------------------------------------------------------------------

root = Tk()
root.geometry('600x600')

img= PhotoImage(file='piano.png')
preta= PhotoImage(file='t_preta.png')
root.iconphoto(True, img)
root.config(background='#02021A')

label=Label(root, bg='#02021A',
              image= img,
              compound='bottom')

button=Button(root, image=preta,
             bg='#000000',
             width=30,
             height=130,
             activebackground='#000000',
             activeforeground='#000000',
             command=tocar_som)

button.pack()

root.mainloop()
