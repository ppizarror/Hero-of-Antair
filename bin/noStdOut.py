# coding=utf-8
"""
NOSTDOUT
Desactiva el canal de salida de python.

Autor: PABLO PIZARRO @ ppizarror
Fecha: ENERO 2014, 2017
Licencia: GPLv2
"""


class noStdOut(object):
    def __init__(self): pass

    def write(self, data): pass

    def read(self, data): pass

    def flush(self): pass

    def close(self): pass
