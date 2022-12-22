#导入第三方库
import ttkbootstrap as ttk#ttkbootstrap
from tkinter import messagebox
import tkinter
import os#os
import sys#sys
import datetime
import subprocess
from tkinter import StringVar
#os.system("@echo off")
#主程序
mw=ttk.Window(themename='superhero')#mw窗口定义
mw.iconbitmap(".\\ICO\\MT-ICON.ico")#定义窗口图标
mw.title("More Tools")#mw标题
mw.geometry("800x600")#mw窗口尺寸
#定义变量
selectcomboboxvar=StringVar()
code=""
#定义函数
def startmmp():
    #os.system(".\\Python_Release\\MMP.exe")
    subprocess.Popen(".\\Python_Release\\MMP.exe")
def startccp():
    #os.system(".\\CPP_Release\\Caesar_Code_Part.exe")
    subprocess.Popen(".\\CPP_Release\\Caesar_Code_Part.exe")
def entersoft():
    global readsoft
    readsoft=selectcombobox.get()
    if(readsoft=="More Message"):
        startmmp()
    elif(readsoft=="Caesar Code"):
        startccp()
def exitprogram():
    os._exit(1)
def intowebsite():
    os.system("start https://sciencekiller.github.io")
def copyfile():
    global currentdic
    global code
    currentdic=os.getcwd()
    ufdic=currentdic+"\\Update.exe"
    todic=currentdic+"\\Runupdate.exe"
    code="copy \""+ufdic+"\" \""+todic+"\""
    print(code)
    os.system(code)
def updateprogram():
    if(os.path.exists(".\\Runupdate.exe")==False):
        copyfile()
    messagebox.showinfo("准备检查更新","程序即将重启，过程中可能有几个黑框，不要着急关掉，等再次出现主界面再关掉")
    os.system(".\\Runupdate.exe")
    os.system("exit")
#定义组件
mainlabel=ttk.Label(mw,style="primary",text="欢迎来到More Tools",font=("Frutiger",24)).grid(column=0,row=0,padx=5,pady=5)
selectcombobox=ttk.Combobox(mw,style="primary",textvariable=selectcomboboxvar,state="readonly",width=50,value=("More Message","Caesar Code"))
selectcombobox.current(0)
selectcombobox.grid(column=0,row=1,padx=5,pady=5)
enterbutton=ttk.Button(mw,style="primary",text="进入",command=entersoft,width=20).grid(column=1,row=2,padx=5,pady=5)
templabel0=ttk.Label(mw).grid(column=0,row=3,padx=5,pady=5)
templabel1=ttk.Label(mw).grid(column=0,row=4,padx=5,pady=5)
templabel2=ttk.Label(mw).grid(column=0,row=5,padx=5,pady=5)
exitbutton=ttk.Button(mw,style="primary",text="退出",command=exitprogram,width=20).grid(column=1,row=6,padx=5,pady=5)
wesitebutton=ttk.Button(mw,style="primary",text="进入官网",command=intowebsite,width=20).grid(column=1,row=7,padx=5,pady=5)
updatebutton=ttk.Button(mw,style="primary",text="检查更新",command=updateprogram,width=20).grid(column=1,row=8,padx=5,pady=5)
mw.mainloop()#保持mw窗口

