
import tkinter as tk
from PIL import Image
import ImageLabel


im20 = Image.open('./video/20.gif')
lagdelay = 1000
root = tk.Tk()
root.geometry('180x390')
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 - 300
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 200
root.wm_geometry("+%d+%d" % (x, y))
root.after(lagdelay, root.destroy)
root.attributes("-topmost", True)
lbl = ImageLabel.ImageLabel(root)
lbl.pack()
lbl.load(im20)
root.mainloop()