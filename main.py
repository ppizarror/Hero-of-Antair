# coding=utf-8
"""
MAIN
Archivo principal del juego.

Autor: PABLO PIZARRO @ ppizarror
Fecha: JULIO 2015, 2017, 2021
Licencia: GPLv2
"""

# Importación de librerías
from lib.hoa import *

# Inicio del programa
if __name__ == '__main__':
    loadLang(True)  # se carga el idioma por defecto
    game = hoa(sys.argv)  # se instancia el objeto
    game.root.mainloop(0)  # se ejecuta la interfaz gráfica
