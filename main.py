# from tkinter import *
# import time
# import threading
# from tkinter import *
# from tkvideo import tkvideo
# from bvPlayer import bvPlayer
#
#
# def thread_function(name):
#     root = Tk()
#     my_label = Label(root)
#     my_label.pack()
#     root.after(10000, root.destroy)
#     root.attributes("-topmost", True)
#     player = tkvideo("C:\\Users\\pimon\\PycharmProjects\\lag\\video\\1.mp4", my_label, size=(1280, 720))
#     player.play()
#     root.mainloop()
#
#
# x = threading.Thread(target=thread_function, args=(1,))
# x.start()
# time.sleep(0.1)
# # x = threading.Thread(target=thread_function, args=(1,))
# # x.start()



import time
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle
import threading
import ImageLabel
import subprocess
import pyglet
import sys

def thread_functionSong(name):
    #exec(open("audio.py").read())
    subprocess.call("audio.exe")

print("lol")
im = Image.open('./video/2.gif')
im1 = Image.open('./video/1.gif')
im3 = Image.open('./video/3.gif')
im4 = Image.open('./video/4.gif')
im5 = Image.open('./video/5.gif')
def thread_function2(name):
    root = tk.Tk()
    root.geometry('370x390')
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 - 500
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 100
    root.wm_geometry("+%d+%d" % (x, y))
    # root.after(700, root.destroy)
    root.attributes("-topmost", True)
    lbl = ImageLabel.ImageLabel(root)
    lbl.pack()
    lbl.load(im)
    root.mainloop()

root = tk.Tk()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 - 200
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 200
root.wm_geometry("+%d+%d" % (x, y))
root.after(24000, root.destroy)
root.attributes("-topmost", True)
lbl = ImageLabel.ImageLabel(root)
lbl.pack()
lbl.load(im1)
x2 = threading.Thread(target=thread_functionSong, args=(1,))
root.after(0, x2.start)
root.mainloop()

lagdelay = 300
for i in range(2):
    root = tk.Tk()
    root.geometry('370x390')
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 - 500
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 100
    root.wm_geometry("+%d+%d" % (x, y))
    root.after(lagdelay, root.destroy)
    root.attributes("-topmost", True)
    lbl = ImageLabel.ImageLabel(root)
    lbl.pack()
    lbl.load(im)
    root.mainloop()

    root = tk.Tk()
    root.geometry('370x390')
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 - 200
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 100
    root.wm_geometry("+%d+%d" % (x, y))
    root.after(lagdelay, root.destroy)
    root.attributes("-topmost", True)
    lbl = ImageLabel.ImageLabel(root)
    lbl.pack()
    lbl.load(im)
    root.mainloop()

    root = tk.Tk()
    root.geometry('370x390')
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 + 100
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 100
    root.wm_geometry("+%d+%d" % (x, y))
    root.after(lagdelay, root.destroy)
    root.attributes("-topmost", True)
    lbl = ImageLabel.ImageLabel(root)
    lbl.pack()
    lbl.load(im)
    root.mainloop()

    root = tk.Tk()
    root.geometry('370x390')
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 + 400
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 100
    root.wm_geometry("+%d+%d" % (x, y))
    root.after(lagdelay, root.destroy)
    root.attributes("-topmost", True)
    lbl = ImageLabel.ImageLabel(root)
    lbl.pack()
    lbl.load(im)
    root.mainloop()


lagdelay3 = 750
root = tk.Tk()
root.geometry('340x390')
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 - 500
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 100
root.wm_geometry("+%d+%d" % (x, y))
root.after(lagdelay3, root.destroy)
root.attributes("-topmost", True)
lbl = ImageLabel.ImageLabel(root)
lbl.pack()
lbl.load(im3)
root.mainloop()

root = tk.Tk()
root.geometry('340x390')
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 - 200
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 100
root.wm_geometry("+%d+%d" % (x, y))
root.after(lagdelay3, root.destroy)
root.attributes("-topmost", True)
lbl = ImageLabel.ImageLabel(root)
lbl.pack()
lbl.load(im3)
root.mainloop()

root = tk.Tk()
root.geometry('340x390')
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 + 100
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 100
root.wm_geometry("+%d+%d" % (x, y))
root.after(lagdelay3, root.destroy)
root.attributes("-topmost", True)
lbl = ImageLabel.ImageLabel(root)
lbl.pack()
lbl.load(im3)
root.mainloop()

root = tk.Tk()
root.geometry('340x390')
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 + 400
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 100
root.wm_geometry("+%d+%d" % (x, y))
root.after(lagdelay3, root.destroy)
root.attributes("-topmost", True)
lbl = ImageLabel.ImageLabel(root)
lbl.pack()
lbl.load(im3)
root.mainloop()


lagdelay = 400 #Прыжки
for i in range(2):
    root = tk.Tk()
    root.geometry('370x390')
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 - 500
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 100
    root.wm_geometry("+%d+%d" % (x, y))
    root.after(lagdelay, root.destroy)
    root.attributes("-topmost", True)
    lbl = ImageLabel.ImageLabel(root)
    lbl.pack()
    lbl.load(im4)
    root.mainloop()

    root = tk.Tk()
    root.geometry('370x390')
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 - 200
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 100
    root.wm_geometry("+%d+%d" % (x, y))
    root.after(lagdelay, root.destroy)
    root.attributes("-topmost", True)
    lbl = ImageLabel.ImageLabel(root)
    lbl.pack()
    lbl.load(im4)
    root.mainloop()

    root = tk.Tk()
    root.geometry('370x390')
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 + 100
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 100
    root.wm_geometry("+%d+%d" % (x, y))
    root.after(lagdelay, root.destroy)
    root.attributes("-topmost", True)
    lbl = ImageLabel.ImageLabel(root)
    lbl.pack()
    lbl.load(im4)
    root.mainloop()

    root = tk.Tk()
    root.geometry('370x390')
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 + 400
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 100
    root.wm_geometry("+%d+%d" % (x, y))
    root.after(lagdelay, root.destroy)
    root.attributes("-topmost", True)
    lbl = ImageLabel.ImageLabel(root)
    lbl.pack()
    lbl.load(im4)
    root.mainloop()

# x2 = threading.Thread(target=thread_function2, args=(1,))
# x2.start()
time.sleep(0.5)
root = tk.Tk()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 +400
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 +50
root.wm_geometry("+%d+%d" % (x, y))
root.geometry('370x390')
root.after(2500, root.destroy)
root.attributes("-topmost", True)
lbl = ImageLabel.ImageLabel(root)
lbl.pack()
lbl.load(im5)
root.mainloop()

lagdelay = 250 #Рука
for i in range(2):
    root = tk.Tk()
    root.geometry('370x390')
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 - 500
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 100
    root.wm_geometry("+%d+%d" % (x, y))
    root.after(lagdelay, root.destroy)
    root.attributes("-topmost", True)
    lbl = ImageLabel.ImageLabel(root)
    lbl.pack()
    lbl.load(im)
    root.mainloop()

    root = tk.Tk()
    root.geometry('370x390')
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 - 200
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 100
    root.wm_geometry("+%d+%d" % (x, y))
    root.after(lagdelay, root.destroy)
    root.attributes("-topmost", True)
    lbl = ImageLabel.ImageLabel(root)
    lbl.pack()
    lbl.load(im)
    root.mainloop()

    root = tk.Tk()
    root.geometry('370x390')
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 + 100
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 100
    root.wm_geometry("+%d+%d" % (x, y))
    root.after(lagdelay, root.destroy)
    root.attributes("-topmost", True)
    lbl = ImageLabel.ImageLabel(root)
    lbl.pack()
    lbl.load(im)
    root.mainloop()

    root = tk.Tk()
    root.geometry('370x390')
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 + 400
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 100
    root.wm_geometry("+%d+%d" % (x, y))
    root.after(lagdelay, root.destroy)
    root.attributes("-topmost", True)
    lbl = ImageLabel.ImageLabel(root)
    lbl.pack()
    lbl.load(im)
    root.mainloop()

lagdelay = 350 #Прыжки
for i in range(2):
    root = tk.Tk()
    root.geometry('370x390')
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 - 500
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 100
    root.wm_geometry("+%d+%d" % (x, y))
    root.after(lagdelay, root.destroy)
    root.attributes("-topmost", True)
    lbl = ImageLabel.ImageLabel(root)
    lbl.pack()
    lbl.load(im4)
    root.mainloop()

    root = tk.Tk()
    root.geometry('370x390')
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 - 200
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 100
    root.wm_geometry("+%d+%d" % (x, y))
    root.after(lagdelay, root.destroy)
    root.attributes("-topmost", True)
    lbl = ImageLabel.ImageLabel(root)
    lbl.pack()
    lbl.load(im4)
    root.mainloop()

    root = tk.Tk()
    root.geometry('370x390')
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 + 100
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 100
    root.wm_geometry("+%d+%d" % (x, y))
    root.after(lagdelay, root.destroy)
    root.attributes("-topmost", True)
    lbl = ImageLabel.ImageLabel(root)
    lbl.pack()
    lbl.load(im4)
    root.mainloop()

    root = tk.Tk()
    root.geometry('370x390')
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 + 400
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 100
    root.wm_geometry("+%d+%d" % (x, y))
    root.after(lagdelay, root.destroy)
    root.attributes("-topmost", True)
    lbl = ImageLabel.ImageLabel(root)
    lbl.pack()
    lbl.load(im4)
    root.mainloop()

#subprocess.call('./2/2.exe')
sys.exit()
