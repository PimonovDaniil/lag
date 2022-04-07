# Lagtrain
# https://github.com/PimonovDaniil/lag
# created by Pimonov Daniil

import time
import tkinter as tk
from PIL import Image
import threading
import ImageLabel
import subprocess

def thread_functionSong(name):
    subprocess.call("audio.exe")

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

def thread_function6(name):
    subprocess.Popen(['python', '6.py'])
def thread_function7(name):
    subprocess.Popen(['python', '7.py'])
def thread_function8(name):
    subprocess.Popen(['python', '8.py'])
def thread_function9(name):
    subprocess.Popen(['python', '9.py'])


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

lagdelay = 0.15
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
time.sleep(4)
lagdelay = 350 #Прыжки
for i in range(1):
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

root = tk.Tk() #стрелочка
root.geometry('340x390')
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 - 50
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 100
root.wm_geometry("+%d+%d" % (x, y))
root.after(6000, root.destroy)
root.attributes("-topmost", True)
lbl = ImageLabel.ImageLabel(root)
lbl.pack()
lbl.load(im10)
root.mainloop()

root = tk.Tk() #знак стоп
root.geometry('340x390')
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 - 50
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 100
root.wm_geometry("+%d+%d" % (x, y))
root.after(6000, root.destroy)
root.attributes("-topmost", True)
lbl = ImageLabel.ImageLabel(root)
lbl.pack()
lbl.load(im11)
root.mainloop()

root = tk.Tk() #волосы
root.geometry('340x390')
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 +400
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 +50
root.wm_geometry("+%d+%d" % (x, y))
root.after(7000, root.destroy)
root.attributes("-topmost", True)
lbl = ImageLabel.ImageLabel(root)
lbl.pack()
lbl.load(im12)
root.mainloop()

root = tk.Tk() #ноги
root.geometry('340x390')
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 -400
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 300
root.wm_geometry("+%d+%d" % (x, y))
root.after(6500, root.destroy)
root.attributes("-topmost", True)
lbl = ImageLabel.ImageLabel(root)
lbl.pack()
lbl.load(im13)
root.mainloop()

root = tk.Tk() #рука низ
root.geometry('340x390')
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 + 400
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 50
root.wm_geometry("+%d+%d" % (x, y))
root.after(3000, root.destroy)
root.attributes("-topmost", True)
lbl = ImageLabel.ImageLabel(root)
lbl.pack()
lbl.load(im14)
root.mainloop()

lagdelay = 350
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

lagdelay = 0.15
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
time.sleep(4)


lagdelay3 = 650
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


lagdelay = 370 #Прыжки
for i in range(1):
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
for i in range(1):
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
    lbl.load(im15)
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

#TODO main 2
subprocess.Popen(['python', 'main2.py'])
