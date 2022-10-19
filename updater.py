import urllib.request
import PySimpleGUI as sg
import requests
import json
import os
import subprocess
import getpass
import sys

user = getpass.getuser()
sg.theme('BlueMono')

os.makedirs(f"C:\\Users\\{user}\\17-py-ti\\", exist_ok=True)

try:
    subprocess.run(f"C:\\Users\\{user}\\17-py-ti\\1.7sound-pack-downloader.exe version")
    dict = f"C:\\Users\\{user}\\17-py-ti\\version.txt"
    with open(dict) as f:
        nover = int(f.read())
except:
    url='https://github.com/TI0360/re-1.7sound-downloader/releases/latest/download/1.7sound-pack-downloader.exe'
    save_name='1.7sound-pack-downloader.exe'
    data = urllib.request.urlopen(url).read()
    with open(f"C:\\Users\\{user}\\17-py-ti\\{save_name}", mode="wb") as f:
        f.write(data)
    layout = [ [sg.Text("アプリがダウンロードされました。起動しなおしてください。")],
        [sg.Button('OK', key='enter')]  ]

    window = sg.Window('TIAppUpdater', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == 'enter':
            break

    window.close()
    
base_url = "https://api.github.com/repos/TI0360/re-1.7sound-downloader/releases"
session = requests.Session()
req = session.get(base_url)
req.close()
res = json.loads(req.text)
never = res[0]["tag_name"]
ver = never.split('-')[1]

try:
    if int(ver) > nover:
        url='https://github.com/TI0360/re-1.7sound-downloader/releases/latest/download/1.7sound-pack-downloader.exe'
        save_name='1.7sound-pack-downloader.exe'
        data = urllib.request.urlopen(url).read()
        with open(f"C:\\Users\\{user}\\17-py-ti\\{save_name}", mode="wb") as f:
            f.write(data)
    else:
        subprocess.run(f"C:\\Users\\{user}\\17-py-ti\\1.7sound-pack-downloader.exe go")
        sys.exit()

except:
    sys.exit()


layout = [ [sg.Text("アプリのアップデートが完了しました。再度起動しなおしてください。")],
        [sg.Button('OK', key='enter')]  ]

window = sg.Window('TIAppUpdater', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'enter':
        break

window.close()


'''
Copyright © 2001-2021 Python Software Foundation; All Rights Reserved

© Copyright 2021 PySimpleGUI

https://github.com/TI0360/re-1.7sound-downloader

[LGPL3]
https://github.com/TI0360/re-1.7sound-downloader/blob/main/LICENCE

Discord
Minakami#9858

'''
