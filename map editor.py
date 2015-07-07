##!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Editor de mapas

# MAP EDITOR
# Autor: PABLO PIZARRO @ ppizarro
# Fecha: JULIO 2015
# Licencia: GPLv2

# Importación de librerías
from lib.medt import mapeditor

# Inicio del programa
if __name__ == "__main__":
    editor = mapeditor()
    editor.core.mainloop(0)
