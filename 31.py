
import tkinter as tk
from PIL import Image
import ImageLabel


im30 = Image.open('./video/30.gif')
lagdelay = 6000
root = tk.Tk()
root.geometry('170x390')
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 + 300
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 -100
root.wm_geometry("+%d+%d" % (x, y))
root.after(lagdelay, root.destroy)
root.attributes("-topmost", True)
lbl = ImageLabel.ImageLabel(root)
lbl.pack()
lbl.load(im30)
root.mainloop()