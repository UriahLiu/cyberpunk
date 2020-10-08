import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfilename
import time
import cv2
from cyber import cyberpunk
import io

root = Tk()
root.geometry('1000x700')
root.title('图片处理')
global img1
'''
class PathyThing:
    def __init__(self):
        self.browsebutton2 = Button(root, text="Last Week's Report", command=self.getFilepast)
        self.browsebutton2.grid(row=0, column=1)
        # etc.

    def getFilepast(self):
        # open dialog box to select file
        self.pathpast = askopenfilename(initialdir="/", title="Select file")

    # etc.
'''
'''
pathy = PathyThing()
def openfile():
    fname_origin = askopenfilename(title = "打开一张图片")
    return fname_origin
def openimg():
    global fname
    fname = openfile()
 

b1 = tk.Button(root, text = '选择文件',command = openimg)
b1.pack(side = BOTTOM)
'''
def resize_scale(img):
    f1 = 1.0*800/img.shape[0]
    f2 = 1.0*800/img.shape[1]
    factor = min([f1,f2])
    width = int(img.shape[1]*factor)
    height = int(img.shape[0]*factor)
    return (width,height)


def open_img():
    #打开图像并显示
    global img1
    OpenFile = tk.Tk()
    OpenFile.withdraw()
    file_path = askopenfilename()
    img = cv2.imread(file_path)
    img = cyberpunk(img)
    img = img [...,::-1]
    img_resized = cv2.resize(img,resize_scale(img),interpolation= cv2.INTER_AREA)
    im = Image.fromarray(img_resized)
    img1 = ImageTk.PhotoImage(im)
    label_img = tk.Label(root,image = img1)
    label_img.pack()

b1 = tk.Button(root,text = '打开图像',command = open_img)
b1.pack(side = BOTTOM)


root.mainloop()