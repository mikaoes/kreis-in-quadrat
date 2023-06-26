from tkinter import *
import numpy as np
# Fensterconfiguration
Fenster=Tk()
Fenster.geometry("400x430")
Fenster.title("Kreis")
# Fenster.configure(bg='blue')
# Fenster["bg"]="blue"
# Canvas
canvas=Canvas(width=400,height=400)
canvas.configure(bg="blue")
canvas.create_oval(1,1,400,400, fill="red")
#Places
canvas.pack()


inside, outside = 0, 0

for i in range(4000):
    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        inside += 1
    else:
        outside += 1
    canvas.create_oval(200+x*200, 200+y*200, 200+x*200, 200+200*y, fill="white")
a=(f"Innen: {inside} Außen: {outside} Errechnetes π: {inside/(inside+outside)*4}")
Anzeige=Label(text=a)
Anzeige.pack()
Fenster.mainloop()