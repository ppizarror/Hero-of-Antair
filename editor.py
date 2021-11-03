# coding=utf-8
"""
MAP EDITOR
Editor de mapas.

Autor: PABLO PIZARRO @ ppizarror
Fecha: JULIO 2015, 2017, 2021
Licencia: GPLv2
"""

# Importación de librerías
from lib.medt import mapeditor

# Inicio del programa
if __name__ == "__main__":
    editor = mapeditor()
    editor.core.mainloop(0)
