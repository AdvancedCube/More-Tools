#导入第三方库
import ttkbootstrap as ttk#ttkbootstrap
import os#os
import sys#sys
#定义函数
def startmmp():
    os.system(".\\Python\\python.exe .\\More_Message\\MMP.py")
def startmcp():
    os.system(".\\Python\\python.exe .\\More_Click\\MCP.py")
def exitprogram():
    sys.exit()
#主程序
mw=ttk.Window(themename='superhero')#mw窗口定义
mw.iconbitmap(".\\ICO\\MT-ICON.ico")#定义窗口图标
mw.wm_attributes("-topmost",1)#将窗口置于顶层
mw.title("More Tools")#mw标题
mw.geometry("800x600")#mw窗口尺寸
mainlabel=ttk.Label(mw,style="primary",text="欢迎来到More Tools",font=("Frutiger",24)).grid(column=0,row=0,padx=5,pady=5)
tiplabel=ttk.Label(mw,style="primary",text="我们有如下几款产品:").grid(column=0,row=1,padx=5,pady=5)
mmpbutton=ttk.Button(mw,style="success-outline",text="More Message:一款卓越的刷屏器",width=40,command=startmmp).grid(column=0,row=2,padx=5,pady=5)
tp1button=ttk.Button(mw,style="success-outline",text="敬请期待",width=40).grid(column=0,row=3,padx=5,pady=5)
tp2button=ttk.Button(mw,style="success-outline",text="敬请期待",width=40).grid(column=0,row=4,padx=5,pady=5)
tp3button=ttk.Button(mw,style="success-outline",text="敬请期待",width=40).grid(column=0,row=5,padx=5,pady=5)
tp4button=ttk.Button(mw,style="success-outline",text="敬请期待",width=40).grid(column=0,row=6,padx=5,pady=5)
tp5button=ttk.Button(mw,style="success-outline",text="敬请期待",width=40).grid(column=0,row=7,padx=5,pady=5)
tp6button=ttk.Button(mw,style="success-outline",text="敬请期待",width=40).grid(column=0,row=8,padx=5,pady=5)
tp7button=ttk.Button(mw,style="success-outline",text="敬请期待",width=40).grid(column=0,row=9,padx=5,pady=5)
tp8button=ttk.Button(mw,style="success-outline",text="敬请期待",width=40).grid(column=1,row=2,padx=5,pady=5)
tp9button=ttk.Button(mw,style="success-outline",text="敬请期待",width=40).grid(column=1,row=3,padx=5,pady=5)
tp10button=ttk.Button(mw,style="success-outline",text="敬请期待",width=40).grid(column=1,row=4,padx=5,pady=5)
tp11button=ttk.Button(mw,style="success-outline",text="敬请期待",width=40).grid(column=1,row=5,padx=5,pady=5)
tp12button=ttk.Button(mw,style="success-outline",text="敬请期待",width=40).grid(column=1,row=6,padx=5,pady=5)
tp13button=ttk.Button(mw,style="success-outline",text="敬请期待",width=40).grid(column=1,row=7,padx=5,pady=5)
tp14button=ttk.Button(mw,style="success-outline",text="敬请期待",width=40).grid(column=1,row=8,padx=5,pady=5)
tp15button=ttk.Button(mw,style="success-outline",text="敬请期待",width=40).grid(column=1,row=9,padx=5,pady=5)
exitbutton=ttk.Button(mw,style="danger-outline",text="退出",width=20,command=exitprogram).grid(column=1,row=14,padx=5,pady=5)
mw.mainloop()#保持mw窗口