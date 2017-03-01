# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
COLOR
Colores en consola.

Autor: PABLO PIZARRO @ ppizarror
Fecha: JULIO 2015, 2017
Licencia: GPLv2
"""

# Importación de librerías
import os

# noinspection PyClassHasNoInit
class color(object):
    """Clase que permite manejar colores en la terminal"""

    # Si el sistema operativo no es windows entonces los colores se activan
    if os.name != "nt":
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'
    else:
        PURPLE = ''
        CYAN = ''
        DARKCYAN = ''
        BLUE = ''
        GREEN = ''
        YELLOW = ''
        RED = ''
        BOLD = ''
        UNDERLINE = ''
        END = ''
