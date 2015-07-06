#!/usr/bin/env python
# -*- coding: utf-8 -*-
# noStdOut
# Pablo Pizarro, 2015
# Desactiva el stdout de python

class noStdOut:
    def __init__(self): pass
    def write(self, data): pass
    def read(self, data): pass
    def flush(self): pass
    def close(self): pass