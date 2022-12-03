#导入库
from sre_parse import State
from ttkbootstrap.constants import *#美化包
import ttkbootstrap as ttk#美化库
import pyperclip#剪切板控制库
from tkinter import *#图形库
import time#时间库
import random#随机库
from tkinter import StringVar#StringVar库
from tkinter import messagebox#MessageBox弹窗库
import pyautogui#键盘模拟库
import datetime#时间库
import sys#系统库sys
import os#系统库os
import keyboard#键盘库
#变量定义
clipboard = False
Readmessage=""
sendtimes=0
wait=0
plan=0
soft=""
saveclipboard=""
emergency=False
askyesno=""
asknext=False
i=0
j=0
wavecheck=0
wavelist=[0,2,4,6,8,10,8,6,4,2,0]
#用户验证函数
def check_number(x) -> bool:
    return x.isdigit()
#窗口
mmp=ttk.Window(themename='darkly')#mmp窗口定义
mmp.iconbitmap("./ICO/MMP-ICON.ico")#设置图标
mmp.wm_attributes("-topmost",1)#将窗口置于顶层
mmp.title("More Message Part")#mmp标题
mmp.geometry("800x600")#mmp窗口尺寸
number_check=mmp.register(check_number)#窗口内用户输入验证
changecombovar=StringVar()#定义changecombobox的变量
plancombovar=StringVar()#定义plancombobox的变量
softcombovar=StringVar()#定义softcombobox的变量
wordentryvar=StringVar(value="Welcome to the More Message Service")#定义textentry的变量
numberentryvar=StringVar(value="401")#定义numberentry的变量
waitentryvar=StringVar(value="6")#定义lateentry的变量

#退出函数
def exit_button():
    sys.exit()
#开始函数
def start_button():
    #引入变量
    global wordentryvar
    global numberentryvar
    global waitentryvar
    global saveclipboard
    global Readmessage
    global sendtimes
    global wait
    global i
    global j
    global askyesno
    global wavecheck
    global asknext
    global emergency
    global plan
    global soft
    global wavelist
    #初始化变量
    wavecheck=0
    emergency=False
    #读入变量
    #读入文本
    if(changecombobox.get()=='文本框'):#当模式为文本框时
        Readmessage=wordentryvar.get()#读取文本框
        saveclipboard=pyperclip.paste()#保存剪切板
        pyperclip.copy(Readmessage)#复制文本
    else:#否则为剪切板模式
        pass#跳过，因为后面主体部分采用pyperclip将内容复制到剪切板，所以此处无需读取
    #读入次数
    sendtimes=int(numberentryvar.get())#从numberentry读入
    #读入等待时间
    wait=int(waitentryvar.get())#从lateentry读入
    #读入计划
    if(plancombobox.get()=="直列式"):#当为直列式时
        plan=0#plan为0
    elif(plancombobox.get()=="波浪式"):#当为波浪式时
        plan=1#plan为1
    else:
        plan=2#plan为2
    #读入软件
    if(softcombobox.get() == "微信" or softcombobox.get() == "钉钉" or softcombobox.get() == "文本文档" or softcombobox.get() == "其他按enter键发送的软件"):#按enter键发送的软件
        soft=0 #soft为0
    else:#否则为按ctrl+enter发送
        soft=1 #soft为1
    #主体部分
    askyesno="请于按下是后"+str(wait)+"秒后将光标选中文本框"#提示框内容
    asknext=messagebox.askyesno("请确认",askyesno)#提示框
    if(asknext==False):#如果为否就取消
        return
    mmp.state("icon")#最小化窗口
    time.sleep(wait)
    for i in range(sendtimes):
        if keyboard.is_pressed("esc"):
            emergency=True
            break
        if(plan==1):
            for j in range(wavelist[wavecheck]):#循环wavelist中的次数
                pyautogui.press("space")#按下空格
            wavecheck+=1
            if(wavecheck>10): 
                wavecheck=0
        if(plan==2):
            wavecheck=random.randint(0,10)#产生随机数
            for j in range(wavecheck):#循环随机次
                pyautogui.press("space")#按下空格
        pyautogui.hotkey("ctrl","v")#粘贴内容
        if(soft==0):
            pyautogui.press("enter")#按下回车
        else:
            pyautogui.press("ctrl","enter")#按下ctrl+enter
    mmp.state("normal")#恢复窗口
    if(emergency==False):
        messagebox.showinfo("提示","发送结束")
    else:
        messagebox.showinfo("提示","用户中断发送")
#窗口控件定义
textlabel=ttk.Label(mmp,text="请输入文本:",bootstyle="primary",font=("楷体",14)).grid(column=0,row=0,padx=40,pady=5)#文字输入提示符
textentry=ttk.Entry(mmp,width=40,bootstyle="primary",textvariable=wordentryvar).grid(column=1,row=0,pady=5)#文字输入文本框
numberlabel=ttk.Label(mmp,text="请输入次数:",bootstyle="primary",font=("楷体",14)).grid(column=0,row=1,pady=5)#数字输入提示符
numberentry=ttk.Entry(mmp,width=40,bootstyle="primary",validate="focus",textvariable=numberentryvar,validatecommand=(number_check,'%P')).grid(column=1,row=1,pady=5)#数字输入文本框+验证用户输入
changelabel=ttk.Label(mmp,text="文本模式？",bootstyle="primary",font=("楷体",14)).grid(column=0,row=2,pady=5)#更改文本模式标签
changecombobox=ttk.Combobox(mmp,textvariable=changecombovar,bootstyle="primary",state="readonly",value=("文本框","剪切板"))#更改文本模式下拉菜单定义
changecombobox.current(0)#更改文本模式下拉菜单默认值
changecombobox.grid(column=1,row=2,pady=5)#更改文本模式下拉菜单位置
planlabel=ttk.Label(mmp,text="发送模式？",bootstyle="primary",font=("楷体",14)).grid(column=0,row=3,pady=5)#发送模式标签
plancombobox=ttk.Combobox(mmp,textvariable=plancombovar,bootstyle="primary",state="readonly",value=("直列式","波浪式","随机式"))#发送方式下拉菜单定义
plancombobox.current(0)#发送方式下拉菜单默认值
plancombobox.grid(column=1,row=3,padx=10,pady=5)#发送方式下拉菜单位置
softlabel=ttk.Label(mmp,text="你的软件是？",bootstyle="primary",font=("楷体",14)).grid(column=0,row=4,padx=40,pady=5)#软件询问标签
softcombobox=ttk.Combobox(mmp,textvariable=softcombovar,bootstyle="primary",state="readonly",value=("微信","钉钉","QQ","文本文档","其他按enter键发送的软件"))#软件询问下拉菜单定义
softcombobox.current(0)#软件询问下拉菜单默认值
softcombobox.grid(column=1,row=4,padx=40,pady=5)#软件询问下拉下拉菜单位置
latelabel=ttk.Label(mmp,text="等待时间:",bootstyle="primary",font=("楷体",14)).grid(column=0,row=5,padx=40,pady=5)#延时询问标签
lateentry=ttk.Entry(mmp,width=40,bootstyle="primary",textvariable=waitentryvar,validate="focus",validatecommand=(number_check,"%P")).grid(column=1,row=5,pady=5)#延时询问文本框+验证用户输入
startbutton=ttk.Button(mmp,bootstyle="success-outline",width=14,text="开始",command=start_button).grid(column=0,row=6,padx=40,pady=100)#开始按钮
exitbutton=ttk.Button(mmp,bootstyle="danger-outline",width=14,text="退出",command=exit_button).grid(sticky="e",column=3,row=6,padx=40,pady=100)#退出按钮
mmp.mainloop()#维持窗口