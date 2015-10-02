#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Ventanas emergentes de HOA

# POP
# Autor: PABLO PIZARRO @ ppizarro
# Fecha: 2013-2015
# Licencia: GPLv2

# Importación de librerias
from lib import *

# Constantes del programa
if isWindows():
    DEFAULT_FONT_TITLE = "Arial", 10
else:
    DEFAULT_FONT_TITLE = "Arial", 15
COMMENT_COLOR = "#666666"
LANGS = {"AR": "العربي",
         "DE": "Deutsch",
         "EN": "English",
         "ES": "Español",
         "FR": "Français",
         "HI": "हिंदी",
         "IT": "Italiano",
         "JA": "日本",
         "PR-PT": "Português",
         "RU": "Русский",
         "TH": "ภาษาไทย",
         "ZH-CN": "中国的"}


def desParseType(a):
    """
    Función interna que retorna un dato dependiendo del tipo que sea
    :param a: String
    :return: String formateado
    """
    if a.replace(".", "").isdigit():  # Si la variable a es un digito
        if "." in a:
            a = "flt_" + str(float(a))  # Si el numero es un flotante
        else:
            a = "int_" + str(int(a))
    # Si la variable a a es un booleano
    elif a.upper() == "TRUE" or a.upper() == "FALSE":
        if a.upper == "TRUE":
            a = "boo_True"
        else:
            a = "boo_False"
    else:
        a = "str_" + str(a)  # caso general es un texto
    return a


def sortby(tree, col, descending):
    """
    Función que ordena las columnas segun orden
    :param tree: Tree
    :param col: Columna
    :param descending: Boolean
    :return: void
    """
    data = [(tree.set(child, col), child)
            for child in tree.get_children('')]  # obtiene los datos para ordenar
    data.sort(reverse=descending)  # se reonrdenan y modifican
    for indx, item in enumerate(data):
        tree.move(item[1], '', indx)
    tree.heading(col, command=lambda col=col: sortby(
        tree, col, int(not descending)))


class pop:
    """
    Ventanas emergentes
    """

    def __init__(self, properties):
        """
        Función constructora
        :param properties: Propiedades de la ventana
        :return: void
        """
        self.lang = properties[0]
        if "list" in str(type(self.lang)):
            title = self.lang[0]
        else:
            title = properties[0]
        icon = properties[1]
        typeObject = properties[2]
        size = properties[4], properties[3]
        if title == "Error" or title == "Licencia":
            self.w = Toplevel()
        else:
            self.w = Tk()
        self.w.protocol("WM_DELETE_WINDOW", self.kill)
        self.values = []
        if size[0] != 0 and size[1] != 0:
            self.w.minsize(width=size[0], height=size[1])
            self.w.geometry('%dx%d+%d+%d' % (size[0], size[1], (self.w.winfo_screenwidth(
            ) - size[0]) / 2, (self.w.winfo_screenheight() - size[1]) / 2))
        self.w.resizable(width=False, height=False)
        self.w.focus_force()
        self.w.title(title)
        try:
            self.w.iconbitmap(icon)
        except:
            self.w.iconbitmap("data/icons/hoa.ico")
        self.sent = False
        if typeObject == "about":  # Acerca de
            Label(self.w, text=self.lang[
                1] + properties[5], font=DEFAULT_FONT_TITLE, border=5).pack()
            Label(self.w, text=self.lang[
                2] + properties[6], font=DEFAULT_FONT_TITLE, border=5).pack()
            Label(self.w, text=self.lang[
                3] + str(properties[7]), font=DEFAULT_FONT_TITLE, border=5).pack()
            Button(
                self.w, text=self.lang[4], command=self.w.destroy, relief=GROOVE).pack()
            self.w.bind("<Return>", self.destruir)
            self.w.bind("<Escape>", self.destruir)
        elif typeObject == "actualizacion":  # Actualización del programa
            Label(self.w, text=self.lang[
                4], font=DEFAULT_FONT_TITLE, border=10).pack()
            Label(self.w, text=self.lang[1].format(
                properties[5]), font=DEFAULT_FONT_TITLE, border=1).pack()
            Label(self.w, text=self.lang[2].format(
                properties[6]), font=DEFAULT_FONT_TITLE, border=1).pack()
            F = Frame(self.w)
            F.pack(pady=6)
            Button(F, text=self.lang[5], command=lambda: self.response(
                "si", "act"), width=8, relief=GROOVE).pack(side=LEFT)  # si
            Label(F, text=" ").pack(side=LEFT)
            Button(F, text=self.lang[6], command=lambda: self.response(
                "no", "act"), width=8, relief=GROOVE).pack(side=LEFT)  # no
            Label(F, text=" ").pack()
            self.buscaractualizacion = IntVar(self.w)
            self.buscaractualizacion.set(0)
            c = Checkbutton(self.w, text=self.lang[
                3], variable=self.buscaractualizacion, onvalue=1, offvalue=0)
            c.pack()
            self.w.bind("<Escape>", self.destruir)
        elif typeObject == "command":  # Ventana de comandos
            self.commandsfile = properties[5] + "prevcommands.log"
            self.commands = loadFromArchive(
                self.commandsfile, self.lang[2], False)
            self.lastcommand = -1

            def _caps(event):
                """
                Convierte el texto a mayusculas
                :param event: Evento
                :return: void
                """
                self.eventTextSv.set(self.eventTextSv.get().upper())

            def _prevcommand(event):
                """
                Carga el comando anterior
                :param event: Event
                :return: void
                """
                if len(self.commands) != 0:
                    self.lastcommand = min(
                        self.lastcommand + 1, len(self.commands) - 1)
                    self.eventTextSv.set(
                        self.commands[self.lastcommand].upper())

            def _upcommand(event):
                """
                Carga el comando siguiente
                :param event: Event
                :return: void
                """
                if len(self.commands) != 0:
                    self.lastcommand = max(-1, self.lastcommand - 1)
                    if self.lastcommand == -1:
                        self.eventTextSv.set("")
                    else:
                        self.eventTextSv.set(
                            self.commands[self.lastcommand].upper())

            f = Frame(self.w, border=10)
            f.pack()
            Label(f, text=self.lang[1], anchor=E, width=8).pack(side=LEFT)
            self.eventTextSv = StringVar(f)
            if isWindows():
                self.eventText = Entry(
                    f, relief=GROOVE, width=35, bg="#F0F0F0", textvariable=self.eventTextSv)
            else:
                self.eventText = Entry(
                    f, relief=GROOVE, width=35, bg="#F0F0F0", textvariable=self.eventTextSv, highlightthickness=0)
            self.eventText.pack()
            self.eventText.focus_force()
            # self.eventText.bind("<KeyRelease>", _caps)
            self.eventText.bind("<Up>", _prevcommand)
            self.eventText.bind("<Down>", _upcommand)
            self.w.bind("<Escape>", self.destruir)
            self.w.bind("<Return>", self.enviarComando)
            self.w.bind("<F2>", self.destruir)
        elif typeObject == "config_hoa":  # Ventana de configuraciones

            def _buscarNombreColor(color, mode):
                """
                Función que busca el nombre del color entregado por el argumento
                :param color: Color
                :param mode: Modo de color
                :return:
                """
                for i in self.colors:
                    if i[1] == color.upper():
                        return i[0]
                if mode == "bg":
                    return self.lang[21]
                else:
                    return self.lang[12]

            Label(self.w, text=self.lang[
                1] + " - Hero of Antair", font=DEFAULT_FONT_TITLE, border=10).pack()
            self.configon = self.lang[6].upper().strip()
            f = Frame(self.w, border=3)
            f.pack(fill=X)
            # Se cargan todos los idiomas disponibles
            langlist = loadFromArchive(
                properties[7] + "/config/langs.txt", self.lang[26], False)
            if len(langlist) != 0:
                # Reemplazo el final de cada lang en langlist por ""
                for k in range(len(langlist)):
                    try:
                        if langlist[k] != "":
                            langlist[k] = langlist[k].replace(properties[8], "") + " - " + \
                                LANGS[langlist[k].replace(properties[8], "")]
                        else:
                            langlist.pop(k)
                    except:
                        pass
            else:
                tkMessageBox.showerror(self.lang[28], self.lang[29])
            if isWindows():
                _sizelabel = 12
            else:
                _sizelabel = 15
            self.conflang = StringVar(self.w)
            # valor por defecto
            self.conflang.set(properties[5] + " - " + LANGS[properties[5]])
            Label(f, text=self.lang[2], anchor=E, width=18).pack(side=LEFT)
            # menu de opciones para el idioma
            w = apply(OptionMenu, (f, self.conflang) + tuple(langlist))
            w["width"] = _sizelabel
            w["relief"] = GROOVE
            w["anchor"] = W
            w.pack(side=LEFT)
            # Sonido
            f = Frame(self.w, border=3)
            f.pack(fill=X)
            self.confsound = StringVar(self.w)
            if properties[6] == 1:
                # se define el sonido que llega por el comando
                s = self.lang[6]
            else:
                s = self.lang[7]
            self.confsound.set(s)  # valor por defecto
            Label(f, text=self.lang[3], anchor=E, width=18).pack(side=LEFT)
            # menu de opciones para sonido
            w = apply(
                OptionMenu, (f, self.confsound) + tuple([self.lang[6], self.lang[7]]))
            w["width"] = _sizelabel
            w["relief"] = GROOVE
            w["anchor"] = W
            w.pack(side=LEFT)
            # Guardar al salir
            f = Frame(self.w, border=3)
            f.pack(fill=X)
            self.confsaveonexit = StringVar(self.w)
            if properties[9] == 1:
                # se define el sonido que llega por el comando
                s = self.lang[6]
            else:
                s = self.lang[7]
            self.confsaveonexit.set(s)  # valor por defecto
            Label(f, text=self.lang[5], anchor=E, width=18).pack(side=LEFT)
            # menu de opciones para sonido
            w = apply(
                OptionMenu, (f, self.confsaveonexit) + tuple([self.lang[6], self.lang[7]]))
            w["width"] = _sizelabel
            w["relief"] = GROOVE
            w["anchor"] = W
            w.pack(side=LEFT)
            # Definición de colores
            self.colors = [[self.lang[10], "#FFFF00"],
                           [self.lang[11], "#0000FF"],
                           [self.lang[12], "#FFFFFF"],
                           [self.lang[13], "#996633"],
                           [self.lang[14], "#8B4513"],
                           [self.lang[15], "#99FFFF"],
                           [self.lang[16], "#00FFFF"],
                           [self.lang[17], "#CCCCCC"],
                           [self.lang[18], "#999999"],
                           [self.lang[19], "#800080"],
                           [self.lang[20], "#FF9900"],
                           [self.lang[21], "#000000"],
                           [self.lang[22], "#FF0000"],
                           [self.lang[23], "#FF00FF"],
                           [self.lang[24], "#009900"],
                           [self.lang[25], "#006600"]]

            # Color fondo consola
            f = Frame(self.w, border=3)
            f.pack(fill=X)
            self.colorfondo = StringVar(self.w)
            # valor por defecto
            self.colorfondo.set(
                _buscarNombreColor(properties[10].strip().upper(), "bg"))
            Label(f, text=self.lang[8], anchor=E, width=18).pack(side=LEFT)
            w = apply(OptionMenu, (f, self.colorfondo) + tuple(
                [self.lang[10], self.lang[11], self.lang[12], self.lang[13], self.lang[14], self.lang[15],
                 self.lang[16], self.lang[17], self.lang[
                     18], self.lang[19], self.lang[20], self.lang[21],
                 self.lang[22], self.lang[23], self.lang[24], self.lang[25]]))
            w["width"] = _sizelabel
            w["relief"] = GROOVE
            w["anchor"] = W
            w.pack(side=LEFT)
            # Color texto consola
            f = Frame(self.w, border=3)
            f.pack(fill=X)
            self.colortexto = StringVar(self.w)
            # valor por defecto
            self.colortexto.set(
                _buscarNombreColor(properties[11].strip().upper(), "fg"))
            Label(f, text=self.lang[9], anchor=E, width=18).pack(side=LEFT)
            w = apply(OptionMenu, (f, self.colortexto) + tuple(
                [self.lang[10], self.lang[11], self.lang[12], self.lang[13], self.lang[14], self.lang[15],
                 self.lang[16], self.lang[17], self.lang[
                     18], self.lang[19], self.lang[20], self.lang[21],
                 self.lang[22], self.lang[23], self.lang[24], self.lang[25]]))
            w["width"] = _sizelabel
            w["relief"] = GROOVE
            w["anchor"] = W
            w.pack(side=LEFT)
            self.w.bind("<Escape>", self.destruir)
            Button(self.w, text=self.lang[
                4], command=self.sendconfig, relief=GROOVE, width=7).pack(pady=5)
        elif typeObject == "deseaDesconectarse":  # Desea guardar
            if properties[5] and isWindows():
                winsound.MessageBeep(-1)
            self.w.focus_force()
            # desea guardar
            Label(self.w, text=self.lang[
                1], font=DEFAULT_FONT_TITLE, border=10).pack()
            F = Frame(self.w)
            F.pack()
            Button(F, text=self.lang[2], command=lambda: self.response(
                "si"), width=14, relief=GROOVE).pack(side=LEFT)  # si
            Label(F, text=" ").pack(side=LEFT)
            Button(F, text=self.lang[3], command=lambda: self.response(
                "cancel"), width=8, relief=GROOVE).pack(side=LEFT)  # no
        elif typeObject == "deseaGuardar":  # Desea guardar
            if properties[5] and isWindows():
                winsound.MessageBeep(1)
            self.w.focus_force()
            # desea guardar
            Label(self.w, text=self.lang[
                1], font=DEFAULT_FONT_TITLE, border=10).pack()
            F = Frame(self.w)
            F.pack()
            Button(F, text=self.lang[2], command=lambda: self.response(
                "si"), width=5, relief=GROOVE).pack(side=LEFT)  # si
            Label(F, text=" ").pack(side=LEFT)
            Button(F, text=self.lang[3], command=lambda: self.response(
                "no"), width=5, relief=GROOVE).pack(side=LEFT)  # no
            Label(F, text=" ").pack(side=LEFT)
            Button(F, text=self.lang[4], command=lambda: self.response(
                "cancel"), width=8, relief=GROOVE).pack()  # cancelar
        elif typeObject == "escogerArmamento":  # escoger armamento
            tipo = properties[5]
            # titulo
            Label(self.w, text=self.lang[
                1], font=DEFAULT_FONT_TITLE, border=10).pack()
            armamento = properties[6][0]
            armamento.sort()
            fp = properties[6][1]
            sp = properties[6][2]
            if "bullet" in tipo:
                f = Frame(self.w, border=3)
                f.pack(fill=X)
                for k in range(len(armamento)):
                    armamento[k] = str(armamento[k][0]).strip().capitalize().ljust(45) + " / " + \
                        self.lang[7] + " " + str(armamento[k][1]) + " - " + self.lang[8] + " " + str(
                        armamento[k][2]) + " - " + "ID " + str(armamento[k][3])
                self.escogerArmamento_bullet = StringVar(self.w)
                self.escogerArmamento_bullet.set(
                    self.lang[5])  # texto por defecto
                Label(f, text=self.lang[2], anchor=E, width=12).pack(side=LEFT)
                # menu de opciones para el idioma
                w = apply(
                    OptionMenu, (f, self.escogerArmamento_bullet) + tuple(armamento))
                w["width"] = 25
                w["relief"] = GROOVE
                w["anchor"] = W
                w.pack(side=LEFT, fill=X)
            Label(self.w, text=" ").pack(fill=X)
            Button(self.w, text=self.lang[6], command=lambda: self.sendArmamento(
                self.lang[5]), relief=GROOVE).pack()  # boton de continuar
            self.w.bind("<Return>", lambda: self.sendArmamento(self.lang[5]))
            self.w.bind("<Escape>", self.destruir)
        elif typeObject == "error" or typeObject == "aviso":  # Alerta
            if typeObject == "error" and isWindows():
                winsound.MessageBeep(16)  # Sonido de error
            Label(self.w, text=properties[
                5], wraplength=250, anchor=N, border=10).pack()
            Button(
                self.w, text=self.lang[1], command=self.w.destroy, relief=GROOVE).pack()
            self.w.bind("<Return>", self.destruir)
            self.w.bind("<Escape>", self.destruir)
        # Informacion de un objeto
        elif typeObject == "itemInfo" or typeObject == "itemInfoArmor":
            Label(self.w, text=properties[
                5], font=DEFAULT_FONT_TITLE, border=10).pack()
            tipo = properties[6]
            info = properties[7]
            F = Frame(self.w)
            F.pack()
            f = Frame(F, border=3, height=5)
            f.pack(side=LEFT)
            # Se agrega la informacion dependiendo del tipo de objeto
            if tipo == "arma" or tipo == "armadura" or tipo == "bullet" or tipo == "pocion":
                Label(f, text=self.lang[
                    1] + str(properties[8]) + " HP", width=13, anchor=NW).pack(side=TOP)
                Label(
                    f, text=self.lang[2] + str(properties[9]), width=13, anchor=NW).pack(side=TOP)
            elif tipo == "armawb":
                # si el arma tiene balas
                if properties[11] != 0:
                    Label(f, text=self.lang[
                        1] + str(properties[8] + properties[11]) + " HP", width=13, anchor=NW).pack(
                        side=TOP)
                else:
                    Label(f, text=self.lang[
                        1] + str(properties[8]) + " HP", width=13, anchor=NW).pack(side=TOP)
                Label(
                    f, text=self.lang[2] + str(properties[9]), width=13, anchor=NW).pack(side=TOP)
                if properties[10] != 0:
                    Label(
                        f, text=self.lang[5] + str(properties[10]), width=13, anchor=NW).pack(side=TOP)
                else:
                    Label(f, text=self.lang[6], width=13, anchor=NW).pack(
                        side=TOP)  # si el arma tiene balas
            elif tipo == "coin":
                Label(
                    f, text=self.lang[1] + str(properties[8]), width=13, anchor=NW).pack(side=TOP)
            elif tipo == "libro":
                pass
            elif tipo == "objeto":
                Label(
                    f, text=self.lang[1] + str(properties[8]), width=13, anchor=NW).pack(side=TOP)
                Label(
                    f, text=self.lang[2] + str(properties[9]), width=13, anchor=NW).pack(side=TOP)
            elif tipo == "mana":
                Label(f, text=self.lang[
                    1] + str(properties[8]) + " PTS", width=13, anchor=NW).pack(side=TOP)
                Label(
                    f, text=self.lang[2] + str(properties[9]), width=13, anchor=NW).pack(side=TOP)
            f2 = Frame(F, border=5)
            f2.pack()
            Label(f2, text=info, width=27, height=5, anchor=CENTER,
                  relief=GROOVE, wraplength=150).pack()
            bt = Frame(self.w, border=5)
            bt.pack()
            if typeObject != "itemInfoArmor":
                Button(bt, text="<-", command=lambda:
                       self.actionitem("super_left"), relief=GROOVE).pack(side=LEFT)
                Label(bt, text=" ").pack(side=LEFT)
                Button(bt, text="<", command=lambda: self.actionitem(
                    "left"), relief=GROOVE).pack(side=LEFT)
                Label(bt, text=" ").pack(side=LEFT)
            Button(bt, text=self.lang[3], command=self.w.destroy, relief=GROOVE).pack(
                side=LEFT)
            Label(bt, text=" ").pack(side=LEFT)
            Button(bt, text=self.lang[4], command=lambda: self.actionitem(
                "drop"), relief=GROOVE).pack(side=LEFT)
            if typeObject != "itemInfoArmor":
                Label(bt, text=" ").pack(side=LEFT)
                Button(bt, text=">", command=lambda: self.actionitem(
                    "right"), relief=GROOVE).pack(side=LEFT)
                Label(bt, text=" ").pack(side=LEFT)
                Button(bt, text="->", command=lambda:
                       self.actionitem("super_right"), relief=GROOVE).pack(side=LEFT)
            self.w.bind("<Return>", self.destruir)
            self.w.bind("<Escape>", self.destruir)
        elif typeObject == "new_game":  # Nuevo juego
            Label(self.w, text=self.lang[1], border=10).pack()  # titulo
            f = Frame(self.w, border=3)
            f.pack()
            Label(f, text=self.lang[2], anchor=E, width=9).pack(
                side=LEFT)  # nombre
            self.name = Entry(f, relief=GROOVE, width=24)
            self.name.pack(side=LEFT, padx=5)
            Label(f, text="  ").pack(side=LEFT)
            # solo 23 caracteres
            Label(f, text=self.lang[3], width=21,
                  anchor=W, fg=COMMENT_COLOR).pack()
            self.name.focus_force()
            f = Frame(self.w, border=3)
            f.pack()
            Label(f, text=self.lang[4], width=9, anchor=E).pack(
                side=LEFT)  # pais
            self.pais = Entry(f, relief=GROOVE, width=24)
            self.pais.pack(side=LEFT, padx=5)
            Label(f, text="  ").pack(side=LEFT)
            Label(f, text="", width=21).pack()
            f = Frame(self.w, border=3)
            f.pack()
            Label(f, text=self.lang[5], width=9, anchor=E).pack(
                side=LEFT)  # edad
            self.edad = Entry(f, relief=GROOVE, width=24)
            self.edad.pack(side=LEFT, padx=5)
            Label(f, text="  ").pack(side=LEFT)
            Label(f, text="", width=21).pack()
            f = Frame(self.w, border=3)
            f.pack(fill=X, padx=3, pady=0)
            # dificultad
            Label(f, text=self.lang[6] + " ",
                  anchor=E, width=9).pack(side=LEFT)
            dif_opc = self.lang[7].strip().replace("[", "").replace("]", "").split(
                "/")  # opciones facil/medio/dificil
            self.dificultad = StringVar(f)
            self.dificultad.set(dif_opc[1])  # valor por defecto
            w = apply(OptionMenu, (f, self.dificultad) + tuple(dif_opc))
            w["width"] = 18
            w["relief"] = GROOVE
            w.pack(side=LEFT)
            f = Frame(self.w, border=2)
            f.pack(fill=X, padx=4, pady=0)
            # tipo
            Label(f, text=self.lang[8] + " ",
                  anchor=E, width=9).pack(side=LEFT)
            tipo_opc = self.lang[9].strip().replace(
                "[", "").replace("]", "").split("/")  # tipos de jugador
            self.tipodejugador = StringVar(f)
            self.tipodejugador.set(tipo_opc[0])  # valor por defecto
            w = apply(OptionMenu, (f, self.tipodejugador) + tuple(tipo_opc))
            w["width"] = 18
            w["relief"] = GROOVE
            w.pack(side=LEFT)
            Label(self.w, text="", height=1).pack()
            Button(
                self.w, text=self.lang[10], relief=GROOVE, command=self.new_game).pack()
            self.w.bind("<Escape>", self.destruir)
        elif typeObject == "powerInfo":  # Información de un poder
            Label(self.w, text=properties[
                5], font=DEFAULT_FONT_TITLE, border=10).pack()
            F = Frame(self.w)
            F.pack()
            f = Frame(F, border=3, height=5)
            f.pack(side=LEFT)
            Label(
                f, text=self.lang[1] + str(properties[7]), width=13, anchor=NW).pack(side=TOP)
            if properties[8] != "0:00":
                Label(f, text=self.lang[
                    2] + str(properties[8]) + " " + self.lang[3], width=13, anchor=NW).pack(side=TOP)
            else:
                Label(f, text=self.lang[5], width=13, anchor=NW).pack(side=TOP)
            f2 = Frame(F, border=5)
            f2.pack()
            Label(f2, text=properties[
                6], width=27, height=5, anchor=CENTER, relief=GROOVE, wraplength=150).pack()
            bt = Frame(self.w, border=5)
            bt.pack()
            Button(bt, text=self.lang[4], command=self.w.destroy, relief=GROOVE).pack(
                side=LEFT)
        elif typeObject == "save_game_name":  # Guardar una partida
            Label(self.w, text=self.lang[1], border=10).pack()
            f = Frame(self.w, border=3)
            f.pack()
            Label(f, text=self.lang[2], anchor=W).pack(side=LEFT)
            self.namePartida = Entry(f, relief=GROOVE)
            self.namePartida.pack()
            self.namePartida.focus_force()
            Label(self.w, text="", height=1).pack()
            Button(
                self.w, text=self.lang[3], relief=GROOVE, command=self.savegame).pack()
        elif typeObject == "server_connect":  # Conectarse a un servidor
            self.serverfile = properties[5] + "prevservers.log"
            self.servers = loadFromArchive(
                self.serverfile, self.lang[2], False)
            self.lastserver = -1

            def _prevcommand(event):
                """
                Carga el servidor anterior
                :param event: Event
                :return: void
                """
                if len(self.servers) != 0:
                    self.lastserver = min(
                        self.lastserver + 1, len(self.servers) - 1)
                    server = self.servers[self.lastserver].split(":")
                    self.eventServer.set(server[0])
                    self.eventPort.set(server[1])

            def _upcommand(event):
                """
                Carga el servidor siguiente
                :param event: Event
                :return: void
                """
                if len(self.servers) != 0:
                    self.lastserver = max(-1, self.lastserver - 1)
                    if self.lastserver == -1:
                        self.eventPort.set("")
                        self.eventServer.set("")
                    else:
                        server = self.servers[self.lastserver].split(":")
                        self.eventServer.set(server[0])
                        self.eventPort.set(server[1])

            f = Frame(self.w, border=5)
            f.pack(fill=X)
            Label(f, text=self.lang[1], width=11, anchor=E).pack(side=LEFT)
            self.eventServer = StringVar(f)
            self.serverName = Entry(
                f, relief=GROOVE, width=29, textvariable=self.eventServer)
            self.serverName.pack(side=LEFT, padx=5)
            self.serverName.focus_force()
            f1 = Frame(self.w, border=5)
            f1.pack(fill=X)
            Label(f1, text=self.lang[2], width=11, anchor=E).pack(side=LEFT)
            self.eventPort = StringVar(f1)
            self.serverPort = Entry(
                f1, relief=GROOVE, width=29, textvariable=self.eventPort)
            self.serverPort.pack(side=LEFT, padx=5)
            bt = Frame(self.w, border=5)
            bt.pack()
            Button(bt, text=self.lang[3], command=self.serverConnect, relief=GROOVE).pack(
                side=LEFT)
            self.w.bind("<Return>", self.serverConnect)
            self.w.bind("<Escape>", self.destruir)
            self.serverName.bind("<Up>", _prevcommand)
            self.serverName.bind("<Down>", _upcommand)
        elif typeObject == "server_create":  # Crear una sala

            def _dsc(e=None):
                """
                Desconecta del servidor
                :param e: Event
                :return: void
                """
                self.serverLobby("disconnect")

            f = Frame(self.w, border=10)
            f.pack()
            Label(f, text=self.lang[1], anchor=E, width=8).pack(side=LEFT)
            self.eventTextSv = StringVar(f)
            self.eventText = Entry(
                f, relief=GROOVE, width=35, textvariable=self.eventTextSv)
            self.eventText.pack()
            self.eventText.focus_force()
            # self.eventText.bind("<KeyRelease>", _caps)
            self.w.bind("<Escape>", _dsc)
            self.w.bind("<Return>", self.enviarTextoSala)
            self.w.protocol("WM_DELETE_WINDOW", _dsc)
        elif typeObject == "server_joinlobby":  # Unirse a una sala

            def _dsc(e=None):
                """
                Desconecta del servidor
                :param e: Event
                :return: void
                """
                self.serverLobby("disconnect")

            self.serverdata = properties[5]
            lobbys = []
            for i in self.serverdata.keys():
                lobb = self.serverdata[i]
                if lobb[0].strip() != "null":
                    lobbys.append("'" + lobb[0].strip() + "'    " + self.lang[7] + " " + lobb[1].strip() + " / " +
                                  self.lang[8] + " " + lobb[2].replace(".lvl", "").strip() + " | " + i)
            if len(lobbys) > 0:
                avaiable = True
            else:
                avaiable = False
            # titulo
            Label(self.w, text=self.lang[
                1], font=DEFAULT_FONT_TITLE, border=10).pack()
            f = Frame(self.w, border=3)
            f.pack(fill=X)
            Label(f, text=self.lang[6], anchor=E, width=15).pack(side=LEFT)
            if avaiable:
                self.lobby = StringVar(self.w)
                self.lobby.set(self.lang[5])  # texto por defecto
                # menu de opciones para el idioma
                w = apply(OptionMenu, (f, self.lobby) + tuple(lobbys))
                w["width"] = 25
                w["relief"] = GROOVE
                w["anchor"] = W
                w.pack(side=LEFT, fill=X)
            else:
                Label(
                    f, text=" " + self.lang[11], anchor=W, width=25).pack(side=LEFT)
            f2 = Frame(self.w, border=3)
            f2.pack()
            if avaiable:
                Button(f2, text=self.lang[2], relief=GROOVE, command=lambda: self.serverLobby(
                    "connect")).pack(side=LEFT, padx=2)
                Button(f2, text=self.lang[3], relief=GROOVE, command=lambda: self.serverLobby(
                    "create")).pack(side=LEFT, padx=2)
                Button(f2, text=self.lang[4], relief=GROOVE, command=lambda: self.serverLobby(
                    "disconnect")).pack(padx=2)
            else:
                Button(f2, text=self.lang[3], relief=GROOVE, command=lambda: self.serverLobby(
                    "create")).pack(side=LEFT, padx=2, pady=7)
                Button(f2, text=self.lang[4], relief=GROOVE, command=lambda: self.serverLobby(
                    "disconnect")).pack(padx=2, pady=7)
            self.w.bind("<Escape>", _dsc)
            self.w.protocol("WM_DELETE_WINDOW", _dsc)
        # Mostrar la información del jugador
        elif typeObject == "show_info_player":
            Label(self.w, text=properties[
                5], border=10, font=DEFAULT_FONT_TITLE).pack()
            F = Frame(self.w)
            F.pack()
            f = Frame(F, border=3, height=5)
            f.pack(side=LEFT)
            menu1 = Frame(f)
            menu1.pack(pady=1, fill=X, anchor=NW)
            menu2 = Frame(menu1)
            menu2.pack(fill=X, anchor=NW)
            if isWindows():
                _sizelabel = 5
            else:
                _sizelabel = 6
            Label(menu2, text=self.lang[
                4], width=_sizelabel, anchor=E, fg=COMMENT_COLOR).pack(side=LEFT)  # vida
            infoVidaCanv = Canvas(
                menu2, width=100, height=16, bg="#B30000")  # barra de vida
            infoVidaCanv.pack(side=LEFT)
            infoVida = Label(menu2, width=6, anchor=E)
            infoVida.pack()
            menu3 = Frame(menu1)
            menu3.pack(fill=X)
            Label(menu3, text=self.lang[
                5], width=_sizelabel, anchor=E, fg=COMMENT_COLOR).pack(side=LEFT)  # mana
            infoManaCanv = Canvas(
                menu3, width=100, height=16, bg="#97991E")  # barra de mana
            infoManaCanv.pack(side=LEFT)
            infoMana = Label(menu3, width=6, anchor=E)
            infoMana.pack()
            menu4 = Frame(menu1)
            menu4.pack(fill=X)
            Label(menu4, text=self.lang[6], width=_sizelabel, anchor=E, fg=COMMENT_COLOR).pack(
                side=LEFT)  # experiencia
            # barra de experiencia
            infoExpCanv = Canvas(menu4, width=100, height=16)
            infoExpCanv.pack(side=LEFT)
            infoExp = Label(menu4, width=6, anchor=E)
            infoExp.pack()
            # Actualizo las barras de información
            life = properties[9]
            maxl = properties[10]
            barras = min(100, int((life * 100) / max(1, maxl)))
            infoVidaCanv.delete(ALL)
            infoVidaCanv.create_rectangle(
                0, 0, barras + 2, 18, fill="#008000", outline="#008000")
            infoVida.config(text=str(life).zfill(3) + "/" + str(maxl).zfill(3))
            mana = properties[11]
            maxm = properties[12]
            barras = int((mana * 100) / max(1, maxm))
            infoManaCanv.delete(ALL)
            infoManaCanv.create_rectangle(
                0, 0, barras + 2, 18, fill="#6F7116", outline="#6F7116")
            infoMana.config(text=str(mana).zfill(3) + "/" + str(maxm).zfill(3))
            barras = min(100, int(
                (properties[13] - properties[14]) * 100 / max(1, properties[15] - properties[14])))
            infoExpCanv.delete(ALL)
            infoExpCanv.create_rectangle(
                0, 0, barras + 2, 18, fill="#000080", outline="#000080")
            if 0 <= properties[13] < 10000000:
                msg = str(properties[13])
            elif 10000000 <= properties[13] < 100000000:
                msg = str(properties[13])[0:4] + "m"
            elif 100000000 <= properties[13] < 1000000000:
                msg = str(properties[13])[0:5] + "M"
            else:
                msg = "∞"
            infoExp.config(text=msg)
            menu8 = Frame(f)  # Nivel
            menu8.pack(fill=X)
            Label(menu8, text=self.lang[9], width=5, anchor=E, fg=COMMENT_COLOR).pack(
                side=LEFT)
            if str(properties[18]).strip() != "12":
                Label(menu8, text=str(properties[18]).strip(
                ) + self.lang[10].format(str(properties[15] - properties[13])), width=20, anchor=W).pack()
            else:
                Label(
                    menu8, text=str(properties[18]).strip(), width=20, anchor=W).pack()
            menu5 = Frame(f)  # Tipo
            menu5.pack(fill=X)
            Label(menu5, text=self.lang[1], width=5, anchor=E, fg=COMMENT_COLOR).pack(
                side=LEFT)
            Label(
                menu5, text=str(properties[6]).strip(), width=20, anchor=W).pack()
            menu7 = Frame(f)  # País
            menu7.pack(fill=X)
            Label(menu7, text=self.lang[8], width=5, anchor=E, fg=COMMENT_COLOR).pack(
                side=LEFT)
            Label(
                menu7, text=str(properties[17]).strip(), width=20, anchor=W).pack()
            menu6 = Frame(f)  # Edad
            menu6.pack(fill=X)
            Label(menu6, text=self.lang[2], width=5, anchor=E, fg=COMMENT_COLOR).pack(
                side=LEFT)
            Label(
                menu6, text=str(properties[7]).strip(), width=20, anchor=W).pack()
            f2 = Frame(F, border=3)
            f2.pack()
            imageplayer = Canvas(f2, width=32, height=32)  # barra de mana
            imageplayer.pack()
            # Se escribe la imagen del jugador
            try:
                imageplayer.create_image(0, 0, image=properties[16])
            except:
                imageplayer.pack_forget()
            f2 = LabelFrame(f2, relief=GROOVE, text=self.lang[7])
            f2.pack(padx=5)
            Label(f2, text=properties[8], width=26, wraplength=150, border=0).pack(
                anchor=NW, pady=5)
            bt = Frame(self.w, border=5)
            bt.pack()
            Button(bt, text=self.lang[3], command=self.w.destroy, relief=GROOVE).pack(
                side=LEFT)
            self.w.bind("<Return>", self.destruir)
            self.w.bind("<Escape>", self.destruir)
        elif typeObject == "statics":  # Estadísticas
            Label(self.w, text=self.lang[0], border=8).pack()  # título
            f = Frame(self.w, border=3)
            f.pack(fill=X, padx=5)
            static = properties[5]
            # armaduras botadas id:208
            Label(
                f, text=self.lang[15] + str(static[13]), anchor=W).pack(fill=X)
            # armas botadas id:199
            Label(f, text=self.lang[6] + str(static[4]), anchor=W).pack(fill=X)
            # enemigos id:195
            Label(f, text=self.lang[2] + str(static[0]), anchor=W).pack(fill=X)
            # escapes id:203
            Label(
                f, text=self.lang[10] + str(static[8]), anchor=W).pack(fill=X)
            # items botados id:200
            Label(f, text=self.lang[7] + str(static[5]), anchor=W).pack(fill=X)
            # mapas id:197
            Label(f, text=self.lang[4] + str(static[2]), anchor=W).pack(fill=X)
            # movimientos id:205
            Label(
                f, text=self.lang[12] + str(static[10]), anchor=W).pack(fill=X)
            # npc interactuados id:444
            Label(
                f, text=self.lang[17] + str(static[15]), anchor=W).pack(fill=X)
            # libros leidos id:204
            Label(
                f, text=self.lang[11] + str(static[9]), anchor=W).pack(fill=X)
            # objetos id:196
            Label(f, text=self.lang[3] + str(static[1]), anchor=W).pack(fill=X)
            # oro ganado id:201
            Label(f, text=self.lang[8] + str(static[7]), anchor=W).pack(fill=X)
            # oro gastado id:202
            Label(f, text=self.lang[9] + str(static[6]), anchor=W).pack(fill=X)
            # pociones id:206
            Label(
                f, text=self.lang[13] + str(static[11]), anchor=W).pack(fill=X)
            # poderes usados id:445
            Label(
                f, text=self.lang[18] + str(static[16]), anchor=W).pack(fill=X)
            # puertas abiertas id:211
            Label(
                f, text=self.lang[16] + str(static[14]), anchor=W).pack(fill=X)
            # quest hechas id:591
            Label(
                f, text=self.lang[20] + str(static[18]), anchor=W).pack(fill=X)
            # seguidores id:722
            Label(
                f, text=self.lang[21] + str(static[19]), anchor=W).pack(fill=X)
            # señales leidas id:446
            Label(
                f, text=self.lang[19] + str(static[17]), anchor=W).pack(fill=X)
            # trucos id:198
            Label(f, text=self.lang[5] + str(static[3]), anchor=W).pack(fill=X)
            # veces guardadas id:207
            Label(
                f, text=self.lang[14] + str(static[12]), anchor=W).pack(fill=X)
            f.pack()
            Label(self.w, text="")
            Button(
                self.w, text=self.lang[1], command=self.w.destroy, relief=GROOVE).pack()
            self.w.bind("<Return>", self.destruir)
            self.w.bind("<Escape>", self.destruir)
        elif typeObject == "ver_followers":  # Ver a los seguidores
            Label(self.w, text=self.lang[1], border=8).pack()  # título
            dif = properties[5]  # dificultad actual
            atk = properties[6]  # ataque del jugador actual
            dff = properties[7]  # defensa del jugador actual
            mhp = properties[8]  # máxima vida actual del jugador
            c_l = properties[9]  # cantidad de followers livianos
            c_m = properties[10]  # cantidad de followers medios
            c_p = properties[11]  # cantidad de followers pesados
            if c_l + c_m + c_p > 0:  # Si tiene seguidores
                f1 = Frame(self.w, border=3)  # tipo liviano
                f1.pack(fill=X, padx=5)
                if c_l > 0:  # Si tiene seguidores livianos
                    Label(f1, text=self.lang[2], anchor=E, fg=COMMENT_COLOR, width=10).pack(
                        side=LEFT)  # tipo de follower
                    Label(f1, text=c_l, anchor=CENTER, width=3).pack(side=LEFT)
                    Label(f1, text=self.lang[3], anchor=E, fg=COMMENT_COLOR).pack(
                        side=LEFT)  # vida media
                    Label(f1, text=int(0.1 * dif * mhp),
                          anchor=CENTER, width=3).pack(side=LEFT)
                    Label(f1, text=self.lang[4], anchor=E, fg=COMMENT_COLOR).pack(
                        side=LEFT)  # ataque medio
                    Label(f1, text=int(0.5 * dif * atk),
                          anchor=CENTER, width=3).pack(side=LEFT)
                    Label(f1, text=self.lang[5], anchor=E, fg=COMMENT_COLOR).pack(
                        side=LEFT)  # defensa media
                    Label(
                        f1, text=int(0.1 * dif * dff), anchor=CENTER, width=3).pack()
                else:
                    # si no tiene seguidores livianos
                    Label(f1, text=self.lang[6], fg=COMMENT_COLOR).pack()
                f2 = Frame(self.w, border=3)  # tipo medio
                f2.pack(fill=X, padx=5)
                if c_m > 0:  # Si tiene seguidores medios
                    Label(f2, text=self.lang[8], anchor=E, fg=COMMENT_COLOR, width=10).pack(
                        side=LEFT)  # tipo de follower
                    Label(f2, text=c_m, anchor=CENTER, width=3).pack(side=LEFT)
                    Label(f2, text=self.lang[3], anchor=E, fg=COMMENT_COLOR).pack(
                        side=LEFT)  # vida media
                    Label(f2, text=int(0.13 * dif * mhp),
                          anchor=CENTER, width=3).pack(side=LEFT)
                    Label(f2, text=self.lang[4], anchor=E, fg=COMMENT_COLOR).pack(
                        side=LEFT)  # ataque medio
                    Label(f2, text=int(0.4 * dif * atk),
                          anchor=CENTER, width=3).pack(side=LEFT)
                    Label(f2, text=self.lang[5], anchor=E, fg=COMMENT_COLOR).pack(
                        side=LEFT)  # defensa media
                    Label(
                        f2, text=int(0.3 * dif * dff), anchor=CENTER, width=3).pack()
                else:
                    # si no tiene seguidores medios
                    Label(f2, text=self.lang[9], fg=COMMENT_COLOR).pack()
                f3 = Frame(self.w, border=3)  # tipo pesado
                f3.pack(fill=X, padx=5)
                if c_p > 0:  # Si tiene seguidores pesados
                    Label(f3, text=self.lang[10], anchor=E, fg=COMMENT_COLOR, width=10).pack(
                        side=LEFT)  # tipo de follower
                    Label(f3, text=c_p, anchor=CENTER, width=3).pack(side=LEFT)
                    Label(f3, text=self.lang[3], anchor=E, fg=COMMENT_COLOR).pack(
                        side=LEFT)  # vida media
                    Label(f3, text=int(0.15 * dif * mhp),
                          anchor=CENTER, width=3).pack(side=LEFT)
                    Label(f3, text=self.lang[4], anchor=E, fg=COMMENT_COLOR).pack(
                        side=LEFT)  # ataque medio
                    Label(f3, text=int(0.3 * dif * atk),
                          anchor=CENTER, width=3).pack(side=LEFT)
                    Label(f3, text=self.lang[5], anchor=E, fg=COMMENT_COLOR).pack(
                        side=LEFT)  # defensa media
                    Label(
                        f3, text=int(0.5 * dif * dff), anchor=CENTER, width=3).pack()
                else:
                    # si no tiene seguidores medios
                    Label(f3, text=self.lang[11], fg=COMMENT_COLOR).pack()
            else:
                Label(self.w, text=self.lang[7], border=10, fg=COMMENT_COLOR).pack(
                    fill=BOTH, anchor=CENTER)  # mensaje de que no tiene seguidores
            self.w.bind("<Return>", self.destruir)
            self.w.bind("<Escape>", self.destruir)
        elif typeObject == "ver_quest":  # Ver las quest
            import ttk

            Label(self.w, text=self.lang[1], border=10).pack()
            data = properties[5]
            newdata = []
            for i in range(properties[6]):
                data_quest = str(data[i]).split(properties[7])
                if len(data_quest) == 3:
                    newdata.append([data_quest[1], data_quest[2]])
            if len(newdata) != 0:
                self.lista = VerticalScrolledFrame(self.w)
                self.lista.pack(fill=BOTH)
                f = Frame(self.lista.interior)
                Label(f, text=self.lang[2], width=20).pack(side=LEFT)
                Label(f, text="", width=3, anchor=W).pack(side=LEFT)
                Label(f, text=self.lang[3]).pack(fill=X)
                f.pack(fill=X, padx=4, pady=4)
                for line in newdata:  # Se agrega la información
                    f = Frame(self.lista.interior)
                    Label(f, text=line[0], width=20, anchor=W).pack(side=LEFT)
                    Label(f, text="", width=3, anchor=W).pack(side=LEFT)
                    Label(f, text=line[1], anchor=W).pack(fill=X)
                    f.pack(fill=X)
            else:
                # Mensaje que avisa que no tiene quest
                Label(
                    self.w, text=self.lang[4], border=10, fg=COMMENT_COLOR).pack()
            self.w.bind("<Return>", self.destruir)
            self.w.bind("<Escape>", self.destruir)
        # Licencia o gnu
        elif typeObject in ["licence", "changelog", "ayuda", "longtext", "license"]:
            print "Recurso [{0}] ...".format(properties[5].replace("//", "/")),
            try:
                name = properties[6]
            except:
                name = ""
            archivo = open(properties[5], "r")
            Yscroll = Scrollbar(self.w, orient=VERTICAL, highlightthickness=0)
            Yscroll.pack(side=RIGHT, fill=Y)
            if len(properties) > 6:
                if properties[6]:
                    Xscroll = Scrollbar(self.w, orient=HORIZONTAL)
                    Xscroll.pack(side=BOTTOM, fill=X)
                    texto = Text(
                        self.w, wrap=NONE, yscrollcommand=Yscroll.set, xscrollcommand=Xscroll.set, highlightthickness=0)
                else:
                    texto = Text(
                        self.w, wrap=NONE, yscrollcommand=Yscroll.set, xscrollcommand=None, highlightthickness=0)
            else:
                texto = Text(
                    self.w, wrap=NONE, yscrollcommand=Yscroll.set, xscrollcommand=None, highlightthickness=0)
            texto.focus_force()
            for i in archivo:
                texto.insert(INSERT, i)
            texto.pack(fill=BOTH)
            texto.configure(state="disabled", highlightthickness=0)
            if len(properties) > 6:
                if properties[6]:
                    # noinspection PyUnboundLocalVariable
                    Xscroll.config(command=texto.xview)
            Yscroll.config(command=texto.yview)
            archivo.close()
            print "ok"
            self.w.bind("<Return>", self.destruir)
            self.w.bind("<Escape>", self.destruir)

    def actionitem(self, action):
        """
        Función que envia un booleano que indica que el objeto ha de botarse
        :param action: Evento de la ui
        :return: void
        """
        delMatrix(self.values)
        self.values.append(action)
        self.sent = True
        self.destruir()

    def destruir(self, e=None):
        """
        Función para destruir la ventana via evento
        :param e: Evento
        :return: void
        """
        self.w.destroy()

    def enviarComando(self, e=None):
        """
        Función que envía un comando y lo guarda
        :param e: Event
        :return: void
        """
        delMatrix(self.values)
        a = str(self.eventText.get())
        if len(a) > 0:
            try:
                index = self.commands.index(a)
                self.commands.pop(index)
            except:
                pass
            self.commands.insert(0, a)
            if a == "clear":
                self.commands = []
            archivo = open(self.commandsfile, "w")
            c = 0
            for i in self.commands:
                c += 1
                archivo.write(str(i) + "\n")
                if c == 20:
                    break
            archivo.close()
            del self.commands
            self.values.append(a)
            self.sent = True
            self.destruir()

    def enviarTexto(self, e=None):
        """
        Función que envia un texto
        :param e: Event
        :return: void
        """
        delMatrix(self.values)
        a = str(self.eventText.get())
        if len(a) > 0:
            self.values.append(a)
            self.sent = True
            self.destruir()

    def enviarTextoSala(self, e=None):
        """
        Función que envia un texto
        :param e: Event
        :return: void
        """
        delMatrix(self.values)
        a = str(self.eventText.get()).strip()
        if len(a) > 0:
            from server import RESTRICTED_LOBBYNAMES

            if a not in RESTRICTED_LOBBYNAMES:
                self.values.append(a)
                self.sent = True
                self.destruir()
            else:
                tkMessageBox.showerror(self.lang[3], self.lang[2])
                self.eventText.focus_force()
                return

    def kill(self):
        """
        Función que destruye la ventana
        :return: void
        """
        self.sent = False
        self.w.destroy()

    def new_game(self):
        """
        Función que envia los datos para crear un nuevo juego
        :return: void
        """
        delMatrix(self.values)
        a = self.name.get().strip()
        b = self.pais.get().strip()
        c = self.edad.get().strip()
        d = self.dificultad.get().strip().lower().replace("á", "a").replace(
            "é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
        e = self.tipodejugador.get().strip().lower()
        # Comprueba si los datos son correctos
        if 23 >= len(a) > 0 != len(b) and str(c).isdigit():
            self.sent = True
            self.values.append(a.title())
            self.values.append(b.title())
            self.values.append(int(c))
            self.values.append(d)
            self.values.append(e)
            self.destruir()
        else:
            if not 0 < len(a) <= 32:
                if len(a) == 0:
                    tkMessageBox.showerror(self.lang[11], self.lang[12])
                    self.name.focus_force()
                    return
                elif len(a) > 32:
                    tkMessageBox.showerror(self.lang[11], self.lang[13])
                    self.name.focus_force()
                    return
            if len(b) == 0:
                tkMessageBox.showerror(self.lang[11], self.lang[14])
                self.pais.focus_force()
                return
            if len(c) == 0:
                tkMessageBox.showerror(self.lang[11], self.lang[15])
                self.edad.focus_force()
                return
            elif not str(c).isdigit():
                tkMessageBox.showerror(self.lang[11], self.lang[16])
                self.edad.focus_force()
                return

    def response(self, res, typ="normal"):
        """
        Función que envia una respuesta
        :param res: Respuesta
        :param typ: Tipo
        :return: void
        """
        delMatrix(self.values)
        self.values.append(res)
        if typ == "act":
            self.values.append(self.buscaractualizacion.get())
        self.sent = True
        self.destruir()

    def savegame(self):
        """
        Función que envia el nombre de la partida guardada
        :return: void
        """
        delMatrix(self.values)
        name = self.namePartida.get().strip().lower()
        noneTypes = "!\"#$%&/()=?¿'¡¿´+*~[]{}^`-_.:;,°|¬@"
        if len(name) > 0:
            able = True  # compruebo que los caracteres ingresados sean válidos
            for i in noneTypes:
                if i in name:
                    able = False
                    break
            if able:
                self.values.append(name)
                self.sent = True
                self.destruir()
            else:
                tkMessageBox.showerror(self.lang[4], self.lang[6] + noneTypes)
                self.namePartida.focus_force()
                return
        else:
            if len(name) == 0:
                tkMessageBox.showerror(self.lang[4], self.lang[5])
                self.namePartida.focus_force()
                return

    def sendconfig(self, e=None):
        """
        Función que envia la informacion de la configuración
        :param e: Event
        :return: void
        """

        def _buscarColorNombre(nombre):
            """
            Función que busca el nombre del color entregado por el argumento
            :param nombre: Nombre del color
            :return: String
            """
            for i in self.colors:
                if i[0] == nombre:
                    return i[1]
            return "%NOCOLOR%"

        delMatrix(self.values)
        a = self.confsound.get().upper()  # sonido
        b = self.conflang.get().upper().split(" - ")  # idioma
        c = self.confsaveonexit.get().upper()  # guardar al salir
        d = _buscarColorNombre(self.colorfondo.get())
        e = _buscarColorNombre(self.colortexto.get())
        b = b[0]
        if len(b) > 0 and d != "%NOCOLOR%" and e != "%NOCOLOR%":
            if d != e:  # Si los colores son distintos entre sí
                if a == self.configon:
                    a = True
                else:
                    a = False
                if c == self.configon:
                    c = True
                else:
                    c = False
                self.values.append(b)
                self.values.append(a)
                self.values.append(c)
                self.values.append(d)
                self.values.append(e)
                self.sent = True
                self.destruir()

    def sendArmamento(self, t=None):
        """
        Función que envia el armamento
        :param t: String
        :return: void
        """
        delMatrix(self.values)
        bullet = self.escogerArmamento_bullet.get().split("ID")
        if bullet[0] != t:
            idBullet = bullet[1].strip()
            if idBullet.isdigit():
                self.values.append(int(idBullet))
        else:
            self.values.append(-1)
        self.sent = True
        self.destruir()

    def serverConnect(self, e=None):
        """
        Función que envía los datos de la conexión
        :param e: Event
        :return: void
        """
        a = self.serverName.get().strip()
        b = self.serverPort.get().strip()
        if len(a) > 0 and str(b).isdigit():
            try:
                index = self.servers.index(a + ":" + b)
                self.servers.pop(index)
            except:
                pass
            self.servers.insert(0, a + ":" + b)
            archivo = open(self.serverfile, "w")
            c = 0
            for i in self.servers:
                c += 1
                archivo.write(str(i) + "\n")
                if c == 20:
                    break
            archivo.close()
            del self.servers
            self.values.append(a)
            self.values.append(int(b))
            self.sent = True
            self.destruir()
        else:
            if len(a) == 0:
                tkMessageBox.showerror(self.lang[7], self.lang[6])
                self.serverName.focus_force()
                return
            if not str(b).isdigit():
                tkMessageBox.showerror(self.lang[5], self.lang[4])
                self.serverPort.focus_force()
                return

    def serverLobby(self, e=None):
        """
        Función que envía los datos del lobby
        :param e: Event
        :return: void
        """
        if e == "disconnect":
            self.values.append("disconnect")
            self.sent = True
            self.destruir()
        elif e == "connect":
            a = self.lobby.get()
            if a != self.lang[5]:  # Si no es el texto por defecto
                try:
                    a = a.split("|")
                    lobbyid = a[1].strip()
                    self.values.append("connect")
                    self.values.append(lobbyid)
                    self.sent = True
                    self.destruir()
                except:
                    tkMessageBox.showerror(self.lang[9], self.lang[10])
        elif e == "create":
            self.values.append("create")
            self.sent = True
            self.destruir()
