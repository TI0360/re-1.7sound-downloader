# coding: utf-8
import configparser
import urllib.request
import PySimpleGUI as sg
import os
import getpass
import sys

file_version = "2"

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
config.read(f'C:\\Users\\{user}\\17-py-ti\\config.ini', encoding='utf-8')

sg.theme('BlueMono')


fv = config.get('main', 'FILE')
mv1 = config.get('main', 'VERSION1')
mv2 = config.get('main', 'VERSION2')
fn1 = config.get('download', 'FN1')
fn2 = config.get('download', 'FN2')


layout = [ [sg.Text("1.7sound-packダウンローダーへようこそ。安定最新版のファイルをダウンロードすることができます。")],
        [sg.Text(f"最新バージョン：   [{fv}]")],
        [sg.Text("バージョン選択："), sg.Combo((f'{mv1}', f'{mv2}'), default_value="選択してください...",size=(18, 1), key='select')],
        [sg.Text("ファイル名："), sg.InputText('', key='name'), sg.Text("[拡張子は含めないでください]")],
        [sg.Button('OK', key='enter'), sg.Button('終了', key='exit')]  ]

window = sg.Window('1.7sound-downloader', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        os.remove(f'C:\\Users\\{user}\\17-py-ti\\config.ini')
        break

    if event == 'exit':
        os.remove(f'C:\\Users\\{user}\\17-py-ti\\config.ini')
        break

    if event == 'enter':
        if values['select'] == f'{mv1}':
            url = f"https://github.com/TI0360/1.7sound-pack/releases/latest/download/{fn1}"
            if values['name'] in "":
                save_name = fn1
                data = urllib.request.urlopen(url).read()
                with open(f"C:\\Users\\{user}\\Desktop\\{save_name}", mode="wb") as f:
                    f.write(data)
                sg.popup("デスクトップへのダウンロードが完了しました。")
            else:
                data = urllib.request.urlopen(url).read()
                with open(f"C:\\Users\\{user}\\Desktop\\{values['name']}.zip", mode="wb") as f:
                    f.write(data)
                sg.popup("デスクトップへのダウンロードが完了しました。")

        if values['select'] == f'{mv2}':
            url = f"https://github.com/TI0360/1.7sound-pack/releases/latest/download/{fn2}"
            if values['name'] in "":
                save_name = fn2
                data = urllib.request.urlopen(url).read()
                with open(f"C:\\Users\\{user}\\Desktop\\{save_name}", mode="wb") as f:
                    f.write(data)
                sg.popup("デスクトップへのダウンロードが完了しました。")
            else:
                data = urllib.request.urlopen(url).read()
                with open(f"C:\\Users\\{user}\\Desktop\\{values['name']}.zip", mode="wb") as f:
                    f.write(data)
                sg.popup("デスクトップへのダウンロードが完了しました。")

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
