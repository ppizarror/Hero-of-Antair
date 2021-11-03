# coding=utf-8
"""
CURSORS
Programa que muestra los cursores disponibles en T-Kinter.

Autor: PABLO PIZARRO @ ppizarror
Fecha: SEPT 2013, 2017
Licencia: GPLv2
"""

# Importacion de librerias
from Tkinter import *
from functools import partial

# Cargo los cursores disponibles
cur = []
archivo = open(".config/cur.txt")
for i in archivo:
    cur.append(str(i).strip().replace("\\n", ""))
cur.sort()

# Deficion de variables
pos = [0]
PROGRAM_SIZE = 300, 300


# Definicion de funciones


def loadCur(cursors, pos, app, pag="sig", curlabel=None, e=None):
    """
    Establece los cursores
    :param cursors: Cursor
    :param pos: Posición
    :param app: Aplicación
    :param pag: Evento de UI
    :param curlabel: Título del cursor
    :param e: Evento
    :return: void
    """
    if pag == "sig":
        pos[0] += 1
    elif pag == "self":
        pass
    else:
        pos[0] -= 1
    pos[0] = max(0, min(pos[0], len(cursors) - 1))
    app.config(cursor=cursors[pos[0]])
    app.title(cursors[pos[0]])
    if not curlabel is None:
        curlabel.config(text="Cursor actual: " + cursors[pos[0]])


def copyToClipboard(cursors, pos, app, e=None):
    """
    Copia al clipboard
    :param cursors: Cursor
    :param pos: Posición
    :param app: App
    :param e: Event
    :return: void
    """
    app.clipboard_append(cursors[pos[0]])


root = Tk()
root.minsize(width=PROGRAM_SIZE[0], height=PROGRAM_SIZE[1])
root.resizable(width=False, height=False)
root.geometry('%dx%d+%d+%d' % (PROGRAM_SIZE[0], PROGRAM_SIZE[1], (root.winfo_screenwidth() - PROGRAM_SIZE[0]) / 2,
                               (root.winfo_screenheight() - PROGRAM_SIZE[1] - 50) / 2))
root.title("Cursores")
frame = Frame(root)
frame.pack(anchor=CENTER, fill=BOTH, expand=TRUE)
Label(frame, text="Mueva los cursores con las teclas Izquierda/Derecha").pack(anchor=CENTER)
Label(frame, text="Para copiar el cursor pulse Ctrl-C").pack(anchor=CENTER)
Label(frame, text="Autor: Pablo Pizarro © 2014").pack(anchor=CENTER)
cursorLabel = Label(frame)
cursorLabel.pack(side=BOTTOM)
cmd = partial(loadCur, cur, pos, root, "ant", cursorLabel)
root.bind("<Left>", cmd)
cmd = partial(loadCur, cur, pos, root, "sig", cursorLabel)
root.bind("<Right>", cmd)
copy = partial(copyToClipboard, cur, pos, root)
root.bind("<Control-c>", copy)
root.bind("<Control-C>", copy)

loadCur(cur, pos, root, "self", cursorLabel)
root.iconbitmap(".config/app.ico")  # Icono del programa
root.mainloop(0)
