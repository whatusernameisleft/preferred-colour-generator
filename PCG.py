# Preferred Colour= HSV(h,s,v)
# D={(h,s,v)|h∈R,0°≤h≤360°;s∈R,0.25≤s≤0.65;v=1}

import PySimpleGUI as sg
import random
import colorsys
from tkinter import Tk

def generate():
    hue = random.randint(0, 360)
    sat = random.randint(25, 65)
    val = 100

    rgb = colorsys.hsv_to_rgb(hue / 360, sat / 100, val / 100)
    rgb255 = [round(x) for x in [v * 255 for v in rgb]]

    return ("#%02x%02x%02x" % (rgb255[0], rgb255[1], rgb255[2]), [hue, sat, val], [rgb255[0], rgb255[1], rgb255[2]])

hex, hsv, rgb = generate()

sg.theme("LightGrey")

layout = [
    [sg.Button("Generate")],
    [sg.Text(f"Hex: {hex}", key="hex"), sg.Button("Copy", key="hexCopy")],
    [sg.Text(f"H: {hsv[0]}°\tS: {hsv[1]}%\tV: {hsv[2]}%", key="hsv"), sg.Button("Copy", key="hsvCopy")],
    [sg.Text(f"R: {rgb[0]}\tG: {rgb[1]}\tB: {rgb[2]}", key="rgb"), sg.Button("Copy", key="rgbCopy")]
]

window = sg.Window("Preferred Colour Generator", layout, size=(400, 400), background_color=hex)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == "Generate":
        hex, hsv, rgb = generate()
        window.TKroot.configure(background=hex)
        window["hex"].update(f"Hex: {hex}")
        window["hsv"].update(f"H: {hsv[0]}°\tS: {hsv[1]}%\tV: {hsv[2]}%")
        window["rgb"].update(f"R: {rgb[0]}\tG: {rgb[1]}\tB: {rgb[2]}")
    elif event == "hexCopy":
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(hex)
        r.update()
        r.destroy()
    elif event == "hsvCopy":
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(f"hsv({hsv[0]}, {hsv[1]}%, {hsv[2]}%)")
        r.update()
        r.destroy()
    elif event == "rgbCopy":
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(f"rgb({rgb[0]}, {rgb[1]}, {rgb[2]})")
        r.update()
        r.destroy()


window.close()