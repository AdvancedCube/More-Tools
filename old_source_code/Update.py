import json
import requests
import tkinter.messagebox
import os
with open(".\\version.json") as ver:
    loadver=json.load(ver)
nowver=loadver["version"]
response = requests.get("https://api.github.com/repos/sciencekiller/More-Tools/releases/latest",verify=False)
latestver=response.json()["tag_name"]
nowver="v"+nowver
if(nowver<latestver):
    update=tkinter.messagebox.askquestion("更新可用","最新版本："+latestver+"可用，当前版本："+nowver+"，是否更新?")
    if(update=="no"):
        exit()
    else:
        os.system(".\git\cmd\git.exe fetch --all")
        os.system(".\git\cmd\git.exe reset --hard origin/main")
        os.system(".\git\cmd\git.exe pull")
else:
    tkinter.messagebox.showinfo("恭喜","你使用了最新版的More_Tools!")
