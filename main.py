##!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Archivo principal del juego

# MAIN
# Autor: PABLO PIZARRO @ ppizarro
# Fecha: JULIO 2015
# Licencia: GPLv2

# Importación de librerías
from lib.hoa import *

# Inicio del programa
if __name__ == '__main__':
    loadLang(True)  # se carga el idioma por defecto
    game = hoa(sys.argv)  # se instancia el objeto
    game.root.mainloop(0)  # se ejecuta la interfaz gráfica