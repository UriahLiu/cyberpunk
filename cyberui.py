'''

@File name: cyberui.py
@Effect: Create a tk-ui to make a image cyberpunk
@Author: CSU Uriah Liu
@Last change date : 2020.10.12

'''
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import cv2
from cyber import cyberpunk


root = Tk()
root.geometry('1000x700')
root.title('Cyberpunk')

global img1 #label图片
global img #原图的cyberpunk
global label_img

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
    #将图片按比例缩小
    f1 = 1.0*800/img.shape[0]
    f2 = 1.0*800/img.shape[1]
    factor = min([f1,f2])
    width = int(img.shape[1]*factor)
    height = int(img.shape[0]*factor)
    return (width,height)


def open_img():
    #打开图像并显示
    global img1
    global img
    global label_img
    OpenFile = tk.Tk()
    OpenFile.withdraw()
    file_path = askopenfilename(title = '选择图片位置', filetypes = [('jpg类型','*.jpg'),('jpeg类型','*.jpeg'),('png类型','*.png')])
    img = cv2.imread(file_path)
    img = cyberpunk(img)
    img_rgb = img[...,::-1] #反转bgr通道
    img_resized = cv2.resize(img_rgb,resize_scale(img_rgb),interpolation= cv2.INTER_AREA)
    im = Image.fromarray(img_resized)
    img1 = ImageTk.PhotoImage(im)
    label_img = tk.Label(root,image = img1)
    label_img.pack()

def save_img():
    #保存图像
    global img
    global label_img
    SaveFile = tk.Tk()
    SaveFile.withdraw()
    file_savepath = asksaveasfilename(title = '保存赛伯朋克风格图片',filetypes = [('jpg类型','*.jpg'),('jpeg类型','*.jpeg'),('png类型','*.png')])
    cv2.imwrite(str(file_savepath),img)
    label_img.destroy()
    img = 0


b2 = tk.Button(root,text = '保存图像',command = save_img)
b2.place(relx = 0.6, rely = 0.95,anchor = CENTER)
b1 = tk.Button(root,text = '打开图像',command = open_img)

b1.place(relx = 0.4, rely = 0.95,anchor = CENTER)

root.mainloop()

'''
                           _ooOoo_
                          o8888888o
                          88" . "88
                          (| -_- |)
                          O\  =  /O
                       ____/`---'\____
                     .'  \\|     |//  `.
                    /  \\|||  :  |||//  \
                   /  _||||| -:- |||||-  \
                   |   | \\\  -  /// |   |
                   | \_|  ''\---/''  |   |
                   \  .-\__  `-`  ___/-. /
                 ___`. .'  /--.--\  `. . __
              ."" '<  `.___\_<|>_/___.'  >'"".
             | | :  `- \`.;`\ _ /`;.`/ - ` : | |
             \  \ `-.   \_ __\ /__ _/   .-` /  /
        ======`-.____`-.___\_____/___.-`____.-'======
                           `=---='
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                 佛祖保佑       永无BUG
'''