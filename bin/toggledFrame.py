#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Crea un toggle frame

# TOGGLEDFRAME
# Autor: PABLO PIZARRO @ ppizarro
# Fecha: AGOSTO 2014
# Licencia: GPLv2

# Importación de librerías
import ttk
import Tkinter as tk


class toggledFrame(tk.Frame):
    def __init__(self, parent, text='', **options):
        tk.Frame.__init__(self, parent, **options)
        self.show = tk.IntVar()
        self.show.set(0)
        self.titleFrame = ttk.Frame(self)
        self.titleFrame.pack(fill=tk.X, expand=1)
        ttk.Label(self.titleFrame, text=text).pack(side=tk.LEFT, fill=tk.X, expand=1)
        self.toggleButton = ttk.Checkbutton(self.titleFrame, width=2, text='+', command=self.toggle, variable=self.show,
                                            style='Toolbutton')
        self.toggleButton.pack(side=tk.LEFT)
        self.subFrame = tk.Frame(self, relief=tk.SUNKEN, borderwidth=1)

    def toggle(self):
        if bool(self.show.get()):
            self.subFrame.pack(fill=tk.X, expand=1)
            self.toggleButton.configure(text='-')
        else:
            self.subFrame.forget()
            self.toggleButton.configure(text='+')
