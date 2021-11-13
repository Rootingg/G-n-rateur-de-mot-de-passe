import string
from random import randint, choice
from tkinter import *

def generate_password():
	password_min = 10
	password_max = 25
	all_chars = string.ascii_letters + string.punctuation + string.digits
	password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
	password_entry.delete(0, END)
	password_entry.insert(0, password)
	

# création d'une fênetre
window = Tk()
window.title("Rooting Générateur de mot de passe")
window.geometry("720x480")
window.config(background='#6b989c')

# creer la frame principale
frame = Frame(window, bg='#6b989c')

# creation d'image
width = 300
height = 300
image = PhotoImage(file="password.png").zoom(20).subsample(32)
canvas = Canvas(frame, width=width, height=height, bg='#6b989c', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

# creer une sous boite
right_frame = Frame(frame, bg='#6b989c')

# creer un titre
label_title = Label(right_frame, text="Mot de passe", font=("Helvetica", 20), bg='#6b989c', fg='white')
label_title.pack()

# creer un champs/entrée
password_entry = Entry(right_frame, font=("Helvetica", 20), bg='#6b989c', fg='white')
password_entry.pack()

# creer un bouton
generate_password_button = Button(right_frame, text="Générer", font=("Helvetica", 20), bg='#6b989c', fg='white', command=generate_password)
generate_password_button.pack(fill=X)

# on place la sous boite à droite de la principal
right_frame.grid(row=0, column=1, sticky=W)


# affiche la frame
frame.pack(expand=YES)

# affiche la fênetre
window.mainloop()



