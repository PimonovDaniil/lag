
import tkinter as tk
from PIL import Image
import ImageLabel


im29 = Image.open('./video/29.gif')
lagdelay = 12000
root = tk.Tk()
root.geometry('180x300')
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 + 150
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 +100
root.wm_geometry("+%d+%d" % (x, y))
root.after(lagdelay, root.destroy)
root.attributes("-topmost", True)
lbl = ImageLabel.ImageLabel(root)
lbl.pack()
lbl.load(im29)
root.mainloop()