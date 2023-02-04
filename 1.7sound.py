# coding: utf-8
import configparser
import urllib.request
import customtkinter
import os
import getpass
import sys
import PySimpleGUI as sg

file_version = "4"

user = getpass.getuser()

args = sys.argv

def write_version():
    with open(f"C:\\Users\\{user}\\17-py-ti\\version.txt", mode = "w") as f:
        f.write(file_version)

if args[1] == "version":
    write_version()
    sys.exit()
if args[1] == "go":
    pass
else:
    pass

os.makedirs(f"C:\\Users\\{user}\\17-py-ti\\", exist_ok=True)
with open(f"C:\\Users\\{user}\\17-py-ti\\version.txt", mode = "w") as f:
    f.write(file_version)

confurl='https://github.com/TI0360/1.7sound-definition/releases/latest/download/config.ini'
confsave_name='config.ini'
data = urllib.request.urlopen(confurl).read()
with open(f"C:\\Users\\{user}\\17-py-ti\\{confsave_name}", mode="wb") as f:
    f.write(data)

config = configparser.ConfigParser()
try:
    config.read(f'C:\\Users\\{user}\\17-py-ti\\config.ini', encoding='utf-8')
except:
    layout = [ [sg.Text("コンフィグファイルを読み込めませんでした。起動しなおしてください。")],
        [sg.Button('OK', key='enter')]  ]

    window = sg.Window('Startup Error!', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            sys.exit()

        if event == 'enter':
            sys.exit()

fv = config.get('main', 'FILE')
mv1 = config.get('main', 'VERSION1')
mv2 = config.get('main', 'VERSION2')
mv3 = config.get('main', 'VERSION3')
fn1 = config.get('download', 'FN1')
fn2 = config.get('download', 'FN2')
fn3 = config.get('download', 'FN3')


customtkinter.set_appearance_mode("System")
app = customtkinter.CTk()
app.geometry("520x200")
app.title("1.7sound-downloader")

def enter_f():
    dversion = combobox.get()
    if dversion == f'{mv1}':
        url = f"https://github.com/TI0360/1.7sound-pack/releases/latest/download/{fn1}"
        save_name = fn1
        data = urllib.request.urlopen(url).read()
        with open(f"{save_name}", mode="wb") as f:
            f.write(data)
        window = customtkinter.CTkToplevel()
        window.title("Success")
        window.geometry("400x100")
        label = customtkinter.CTkLabel(window, text="ファイルのダウンロードが完了しました。")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)

    if dversion == f'{mv2}':
        url = f"https://github.com/TI0360/1.7sound-pack/releases/latest/download/{fn2}"
        save_name = fn2
        data = urllib.request.urlopen(url).read()
        with open(f"{save_name}", mode="wb") as f:
            f.write(data)
        window = customtkinter.CTkToplevel()
        window.title("Success")
        window.geometry("400x100")
        label = customtkinter.CTkLabel(window, text="ファイルのダウンロードが完了しました。")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)

    if dversion == f'{mv3}':
        url = f"https://github.com/TI0360/1.7sound-pack/releases/download/1.9.2-1.20ready/{fn3}"
        save_name = fn3
        data = urllib.request.urlopen(url).read()
        with open(f"{save_name}", mode="wb") as f:
            f.write(data)
        window = customtkinter.CTkToplevel()
        window.title("Success")
        window.geometry("400x100")
        label = customtkinter.CTkLabel(window, text="ファイルのダウンロードが完了しました。")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)

    else:
        window = customtkinter.CTkToplevel()
        window.title("Error")
        window.geometry("400x100")
        label = customtkinter.CTkLabel(window, text="バージョンを選択してください！")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)
    


def exit_f():
    os.remove(f'C:\\Users\\{user}\\17-py-ti\\config.ini')
    sys.exit()
    


label2 = customtkinter.CTkLabel(master=app, text=f"最新ファイルバージョン\n[ {fv} ]")
label_ep = customtkinter.CTkLabel(master=app, text="")
label3 = customtkinter.CTkLabel(master=app, text="MCバージョン選択")
combobox = customtkinter.CTkOptionMenu(master=app,
                                     values=[f'{mv1}', f'{mv2}', f'{mv3}'])
combobox.set("選択してください...")
button1 = customtkinter.CTkButton(master=app, text="実行", command=enter_f)
button2 = customtkinter.CTkButton(master=app, text="終了", command=exit_f)

label2.pack(side=customtkinter.LEFT, expand=True)
label_ep.pack()
label3.pack()
combobox.pack()
button1.pack(side=customtkinter.LEFT, expand=True)
button2.pack(side=customtkinter.RIGHT, expand=True)

app.mainloop()

'''
Copyright © 2001-2021 Python Software Foundation; All Rights Reserved

© Copyright 2021 PySimpleGUI

https://github.com/TI0360/re-1.7sound-downloader

[LGPL3]
https://github.com/TI0360/re-1.7sound-downloader/blob/main/LICENCE

Discord
Minakami#9858

'''