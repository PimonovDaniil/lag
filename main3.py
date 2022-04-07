import time
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle
import threading
import ImageLabel
import subprocess
import pyglet
import os

def thread_functionSong(name):
    #exec(open("audio.py").read())
    subprocess.call("audio3.exe")

print("start")
im = Image.open('./video/2.gif')
im1 = Image.open('./video/1.gif')
im3 = Image.open('./video/3.gif')
im4 = Image.open('./video/4.gif')
im5 = Image.open('./video/5.gif')
im6 = Image.open('./video/6.gif')
im7 = Image.open('./video/7.gif')
im8 = Image.open('./video/8.gif')
im9 = Image.open('./video/9.gif')
im10 = Image.open('./video/10.gif')
im11 = Image.open('./video/11.gif')
im12 = Image.open('./video/12.gif')
im13 = Image.open('./video/13.gif')
im14 = Image.open('./video/14.gif')
im15 = Image.open('./video/15.gif')
im24 = Image.open('./video/24.gif')
im25 = Image.open('./video/25.gif')
im26 = Image.open('./video/26.gif')
im30 = Image.open('./video/30.gif')
im31 = Image.open('./video/31.gif')
im36 = Image.open('./video/36.gif')
im39 = Image.open('./video/39.gif')
im40 = Image.open('./video/40.gif')
im41 = Image.open('./video/41.gif')
im42 = Image.open('./video/42.gif')
im43 = Image.open('./video/43.gif')
im44 = Image.open('./video/44.gif')
im45 = Image.open('./video/45.gif')

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

def thread_functionSong(name):
    subprocess.Popen(['python', 'audio4.py'])
def thread_function6(name):
    subprocess.Popen(['python', '6.py'])
def thread_function7(name):
    subprocess.Popen(['python', '7.py'])
def thread_function8(name):
    subprocess.Popen(['python', '8.py'])
def thread_function9(name):
    subprocess.Popen(['python', '9.py'])
def thread_function16(name):
    subprocess.Popen(['python', '16.py'])
def thread_function17(name):
    subprocess.Popen(['python', '17.py'])
def thread_function18(name):
    subprocess.Popen(['python', '18.py'])
def thread_function19(name):
    subprocess.Popen(['python', '19.py'])
def thread_function20(name):
    subprocess.Popen(['python', '20.py'])
def thread_function21(name):
    subprocess.Popen(['python', '21.py'])
def thread_function22(name):
    subprocess.Popen(['python', '22.py'])
def thread_function23(name):
    subprocess.Popen(['python', '23.py'])
def thread_function27(name):
    subprocess.Popen(['python', '27.py'])
def thread_function28(name):
    subprocess.Popen(['python', '28.py'])
def thread_function29(name):
    subprocess.Popen(['python', '29.py'])
def thread_function30(name):
    subprocess.Popen(['python', '30.py'])
def thread_function31(name):
    subprocess.Popen(['python', '31.py'])
def thread_function32(name):
    subprocess.Popen(['python', '32.py'])
def thread_function33(name):
    subprocess.Popen(['python', '33.py'])
def thread_function34(name):
    subprocess.Popen(['python', '34.py'])
def thread_function35(name):
    subprocess.Popen(['python', '35.py'])
def thread_function37(name):
    subprocess.Popen(['python', '37.py'])
def thread_function38(name):
    subprocess.Popen(['python', '38.py'])

# time.sleep(500)


x2 = threading.Thread(target=thread_functionSong, args=(1,))
x2.start()

lagdelay = 0.1
x6 = threading.Thread(target=thread_function6, args=(1,))
x6.start()
time.sleep(lagdelay)
x7 = threading.Thread(target=thread_function7, args=(1,))
x7.start()
time.sleep(lagdelay)
x8 = threading.Thread(target=thread_function8, args=(1,))
x8.start()
time.sleep(lagdelay)
subprocess.Popen(['python', '9.py'])
time.sleep(3)




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

lagdelay = 300 #Прыжки
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

root = tk.Tk()
root.geometry('340x390')
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 - 100
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 100
root.wm_geometry("+%d+%d" % (x, y))
root.after(1700, root.destroy)
root.attributes("-topmost", True)
lbl = ImageLabel.ImageLabel(root)
lbl.pack()
lbl.load(im44)
root.mainloop()

root = tk.Tk()
root.geometry('340x390')
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 - 100
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 100
root.wm_geometry("+%d+%d" % (x, y))
root.after(1500, root.destroy)
root.attributes("-topmost", True)
lbl = ImageLabel.ImageLabel(root)
lbl.pack()
lbl.load(im45)
root.mainloop()

lagdelay = 0.05
x6 = threading.Thread(target=thread_function6, args=(1,))
x6.start()
time.sleep(lagdelay)
x7 = threading.Thread(target=thread_function7, args=(1,))
x7.start()
time.sleep(lagdelay)
x8 = threading.Thread(target=thread_function8, args=(1,))
x8.start()
time.sleep(lagdelay)
subprocess.Popen(['python', '9.py'])
time.sleep(3)



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