#导入第三方库
import sys
from tkinter import StringVar
from tkinter.ttk import Style
import ttkbootstrap as ttk
import pyautogui
from tkinter import *
from ttkbootstrap.constants import *
from tkinter import StringVar
from tkinter import messagebox
import time
#用户验证函数
def check_number(x) -> bool:
    return x.isdigit()
#变量定义
readnum=0
readcli=False
readlat=0
i=0
#主程序
mcp=ttk.Window(themename='vapor')#定义mcp窗口
mcp.iconbitmap("./ICO/MCP-ICON.ico")#定义mcp窗口图标
mcp.wm_attributes("-topmost",1)#将窗口置于顶层
mcp.title("More Click Part")#mcp标题
mcp.geometry("700x300")#mcp窗口尺寸
number_check=mcp.register(check_number)#窗口内用户输入验证
clicomboboxvar=StringVar()#定义clicombobox的变量
numberentryvar=StringVar(value="10")#定义numberentry的变量
lateentryvar=StringVar(value="1")#定义lateentry的变量
#函数定义
def exitprogram():
    sys.exit()
def startcli():
    global i
    global readnum
    global readcli
    global readlat
    readnum=int(numberentryvar.get())
    if(clicomboboxvar.get()=="左键"):
        readcli=True
    else:
        readcli=False
    readlat=int(lateentryvar.get())
    for i in range(readnum):
        if(readcli==True):
            pyautogui.click()
        else:
            pyautogui.rightClick()
        time.sleep(readlat)
    return
#定义窗口组件
clilabel=ttk.Label(mcp,text="按键?",style="primary",font=("楷体",14)).grid(column=0,row=0,padx=5,pady=5)#按键标签
clicombobox=ttk.Combobox(mcp,style="primary",textvariable=clicomboboxvar,state="readonly",value=("左键","右键"))#定义按键下拉菜单
clicombobox.current(0)#按键下拉菜单默认值
clicombobox.grid(column=1,row=0,padx=5,pady=5)#按键下拉菜单位置
numberlabel=ttk.Label(mcp,text="点击次数:",style="primary",font=("楷体",14)).grid(column=0,row=1,padx=5,pady=5)#次数标签
numberentry=ttk.Entry(mcp,width=40,text="401",style="primary",validate="focus",textvariable=numberentryvar,validatecommand=(number_check,'%P')).grid(column=1,row=1,padx=5,pady=5)#次数输入框
latelabel=ttk.Label(mcp,text="间隔:",style="primary",font=("楷体",14)).grid(column=0,row=2,padx=5,pady=5)#延时标签
lateentry=ttk.Entry(mcp,style="primary",validate="focus",textvariable=lateentryvar,validatecommand=(number_check,'%P')).grid(column=1,row=2)#延时文本框
startbutton=ttk.Button(mcp,style="success-outline",text="开始",command=startcli).grid(column=0,row=3,padx=5,pady=5)#开始按钮
exitbutton=ttk.Button(mcp,style="danger-outline",text="退出",command=exitprogram).grid(column=2,row=3,padx=5,pady=5)#结束按钮
mcp.mainloop()#保持窗口