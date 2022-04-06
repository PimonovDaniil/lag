

import time
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle
import threading
import ImageLabel


im = Image.open('./video/2.gif')
im3 = Image.open('./video/3.gif')
def thread_function2(name):
    root = tk.Tk()
    root.geometry('370x390')
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 - 300
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 100
    root.wm_geometry("+%d+%d" % (x, y))
    root.after(700, root.destroy)
    root.attributes("-topmost", True)
    lbl = ImageLabel.ImageLabel(root)
    lbl.pack()
    lbl.load(im)
    root.mainloop()



x2 = threading.Thread(target=thread_function2, args=(1,))
x2.start()
time.sleep(1)
