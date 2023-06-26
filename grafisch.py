import numpy as np
import tkinter as tk

root = tk.Tk()
root.title('Grafisch')

c = tk.Canvas(root, width=400, height=400)
c.pack()

c.create_rectangle(0, 0, 400, 400, fill='blue')
c.create_oval(0, 0, 400, 400, fill='red')

l1 = tk.Label(root, text='0') # inside
l1.pack(side=tk.LEFT)
l2 = tk.Label(root, text='0') # outside
l2.pack(side=tk.LEFT)
l3 = tk.Label(root, text='0') # pi approximation
l3.pack(side=tk.LEFT)


for i in range(4000):
    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        l1['text'] = str(int(l1['text']) + 1)
    else:
        l2['text'] = str(int(l2['text']) + 1)

    c.create_oval(200 + x*200, 200 + y*200, 200 + x*200, 200 + y*200, fill='white')
    l3['text'] = str(4*int(l1['text'])/(i+1))


root.mainloop()