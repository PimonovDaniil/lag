
import tkinter as tk
from PIL import Image
import ImageLabel


im37 = Image.open('./video/37.gif')
lagdelay = 2600
root = tk.Tk()
root.geometry('400x390')
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 - 400
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 300
root.wm_geometry("+%d+%d" % (x, y))
root.after(lagdelay, root.destroy)
root.attributes("-topmost", True)
lbl = ImageLabel.ImageLabel(root)
lbl.pack()
lbl.load(im37)
root.mainloop()