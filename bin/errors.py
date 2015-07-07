##!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Maneja las configuraciones del núcleo de HOA

# CONFIG
# Autor: PABLO PIZARRO @ ppizarro
# Fecha: JULIO 2015
# Licencia: GPLv2

# Importación de librerías
from color import color
from config import *

# Constantes
BR_ERRORxERROR_SET_FORM = 8
BR_ERRORxERROR_SET_SUBMIT = 9
BR_ERRORxNO_ACCESS_WEB = 1
BR_ERRORxNO_FORM = 3
BR_ERRORxNO_FORMID = 2
BR_ERRORxNO_OPENED = 0
BR_ERRORxNO_SELECTED_FORM = 5
BR_ERRORxNO_VALIDID = 4
BR_ERRORxNO_VALID_SUBMIT_EMPTY = 6
BR_ERRORxNO_VALID_SUBMIT_NOT_EQUAL = 7
ERROR_TAG_CANTRETRIEVEHTML = 16
ERROR_TAG_INITNOTCORRECTENDING = 14
ERROR_TAG_INITNOTFINDED = 13
ERROR_TAG_LASTNOTFINDED = 15
ST_ERROR = "[ERR]"
ST_INFO = "[INF]"
ST_WARNING_ID = "[ERR][{0}]"
ST_WARNING = "[WRN]"
WRAP_ERROR_MSG = 70


def st_error(msg, callExit=False):
    """Muestra un mensaje de error en pantalla"""
    print color.RED + ST_ERROR + color.END + " {0}".format(msg)
    if callExit:
        exit()


def st_info(msg, callExit=False):
    """Muestra un mensaje de información en pantalla"""
    print color.DARKCYAN + ST_INFO + color.END + " {0}".format(msg)
    if callExit:
        exit()


def st_warning(msg, callExit=False):
    """Muestra un mensaje de precaución en pantalla"""
    print color.BLUE + ST_WARNING + color.END + " {0}".format(msg)
    if callExit:
        exit()


def parseLangError(msg):
    """
    Formatea un código de error
    :param msg:
    :return:
    """

    def insertEach(string, each, every):
        """
        Inserta el string -each- cada -every- caracteres en el string -string-
        :param string: String a formatear
        :param each: String a insertar
        :param every: Cantidad de carácteres
        :return: string formateado
        """
        return each.join(string[i:i + every] for i in xrange(0, len(string), every))

    data = msg.split("::")
    code = data[0].strip().split("[")[1]
    code = code.replace("]", "")
    msg = data[1].strip()
    msg = insertEach(msg, "-\n\t    ", WRAP_ERROR_MSG)
    ct = 0
    ci = 0

    msg = color.RED + ST_WARNING_ID.format(code) + color.END + " " + msg
    return msg
