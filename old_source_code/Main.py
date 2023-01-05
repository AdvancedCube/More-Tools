#导入第三方库
import ttkbootstrap as ttk#ttkbootstrap
from tkinter import messagebox
import tkinter
import os#os
import sys#sys
import datetime
import subprocess
import zipfile
import requests
from tkinter import StringVar
import json
#os.system("@echo off")
#加载配置
with open(".\\config.json") as cfg:
    loadcfg=json.load(cfg)
#检查JDK
def checkjdk():
    if(os.path.exists(loadcfg["jdkpath"])==False):
        ask=messagebox.askquestion("未找到JDK","此部分需要JDK来运行,但是未找到JDK,您可以下载,或者在config.json的jdkpath部分指定java.exe的绝对路径,是否在线下载？")
        if(ask=="yes"):
            messagebox.showinfo("准备就绪!","将在按下确定后下载，下载过程可能会花费几分钟，取决于网速，请耐心等待")
            downloadjdk=requests.get("https://mirrors.huaweicloud.com/openjdk/19.0.1/openjdk-19.0.1_windows-x64_bin.zip")
            with open("./jdk.zip","wb") as jdk_file:
                jdk_file.write(downloadjdk.content)
                jdk_file.flush() 
            ext=zipfile.ZipFile("./jdk.zip")
            ext.extractall("./")
            ext.close()
            os.remove("./jdk.zip")
            messagebox.showinfo("完成!","下载完成,请重新进入")
        else:
            return
    else:
        return
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
def startmcp():
    checkjdk()
    if(os.path.exists(loadcfg["jdkpath"])):
        code="\""+loadcfg["jdkpath"]+"\" -jar .\\mcp.jar"
        os.system(code)
def entersoft():
    global readsoft
    readsoft=selectcombobox.get()
    if(readsoft=="More Message"):
        startmmp()
    elif(readsoft=="Caesar Code"):
        startccp()
    elif(readsoft=="Morse Code"):
        startmcp()
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
selectcombobox=ttk.Combobox(mw,style="primary",textvariable=selectcomboboxvar,state="readonly",width=50,value=("More Message","Caesar Code","Morse Code"))
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

