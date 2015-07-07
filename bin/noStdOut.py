#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Desactiva el canal de salida de python

# NOSTDOUT
# Autor: PABLO PIZARRO @ ppizarro
# Fecha: ENERO 2014
# Licencia: GPLv2

class noStdOut:
    def __init__(self): pass

    def write(self, data): pass

    def read(self, data): pass

    def flush(self): pass

    def close(self): pass
