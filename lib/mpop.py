#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Maneja ventanas utilitarias del editor de mapas

# MPOP
# Autor: PABLO PIZARRO @ ppizarro
# Fecha: 2014-2015
# Licencia: GPLv2

# Importación de librerias
from lib import *

# Constantes del programa
if isWindows():
    DEFAULT_FONT_TITLE = "Arial", 10
else:
    DEFAULT_FONT_TITLE = "Arial", 15
COMMENT_COLOR = "#666666"


class pop:  # Ventanas emergentes

    def __init__(self, properties):  # Función constructora
        lang = properties[0]
        if "list" in str(type(lang)):
            title = lang[0]
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
        self.sent = False
        if typeObject == "about":  # Acerca de
            Label(self.w, text=lang[1] + properties[5],
                  font=DEFAULT_FONT_TITLE, border=5).pack()
            Label(self.w, text=lang[2] + properties[6],
                  font=DEFAULT_FONT_TITLE, border=5).pack()
            Label(self.w, text=lang[
                3] + str(properties[7]), font=DEFAULT_FONT_TITLE, border=5).pack()
            Button(
                self.w, text=lang[4], command=self.w.destroy, relief=GROOVE).pack()
            self.w.bind("<Return>", self.destruir)
        elif typeObject == "deseaGuardar":  # Desea guardar
            if properties[5] and isWindows():
                winsound.MessageBeep(-1)
            self.w.focus_force()
            Label(self.w, text="¿Desea Guardar?",
                  font=DEFAULT_FONT_TITLE, border=10).pack()
            F = Frame(self.w)
            F.pack()
            Button(F, text="Si", command=lambda: self.response(
                "si"), width=5, relief=GROOVE).pack(side=LEFT)
            Label(F, text=" ").pack(side=LEFT)
            Button(F, text="No", command=lambda: self.response(
                "no"), width=5, relief=GROOVE).pack(side=LEFT)
            Label(F, text=" ").pack(side=LEFT)
            Button(F, text="Cancelar", command=lambda: self.response(
                "cancel"), width=8, relief=GROOVE).pack()
        elif typeObject == "error" or typeObject == "aviso":  # Alerta
            if typeObject == "error" and isWindows():
                winsound.MessageBeep(16)  # Sonido de error
            Label(self.w, text=properties[
                5], wraplength=250, anchor=N, border=10).pack()
            Label(self.w, text="")
            Button(
                self.w, text="Cerrar", command=self.w.destroy, relief=GROOVE).pack()
            self.w.bind("<Return>", self.destruir)
            self.w.bind("<Escape>", self.destruir)
        elif typeObject == "infoTile_info":  # Información del tile
            f = Frame(self.w, border=3)
            f.pack(fill=X, padx=5, pady=1)
            Label(f, text="Posición (x,y)", anchor=W, width=10, fg=COMMENT_COLOR).pack(
                side=LEFT)
            Label(f, text="(" + str(properties[5][1]) + "," + str(
                properties[5][0]) + ")", anchor=W, width=5).pack(side=LEFT)
            separator = Frame(self.w, height=2, bd=1, relief=GROOVE)
            separator.pack(fill=X, padx=0, pady=2)
            f = Frame(self.w, border=3)
            f.pack(fill=X, padx=5, pady=0)
            Label(f, text="Iluminación", anchor=NW, width=10, fg=COMMENT_COLOR).pack(
                side=LEFT, anchor=N)
            if str(properties[8]) == "1":
                i = "No"
            else:
                i = "Si"
            Label(f, text=i, anchor=NW, wraplength=250, justify=LEFT).pack(
                side=LEFT)
            f = Frame(self.w, border=3)
            f.pack(fill=X, padx=5, pady=0)
            Label(f, text="Terreno", anchor=NW, width=10, fg=COMMENT_COLOR).pack(
                side=LEFT, anchor=N)
            Label(f, text=properties[7], anchor=NW, wraplength=250, justify=LEFT).pack(
                side=LEFT)
            separator = Frame(self.w, height=2, bd=1, relief=GROOVE)
            separator.pack(fill=X, padx=0, pady=2)
            f = Frame(self.w, border=3)
            f.pack(fill=X, padx=5, pady=0)
            Label(f, text="Lógico", anchor=NW, width=10, fg=COMMENT_COLOR).pack(
                side=LEFT, anchor=N)
            Label(f, text=properties[
                6], anchor=NW, wraplength=237, justify=LEFT, height=2).pack(side=LEFT)
            Button(
                self.w, text="Cerrar", command=self.w.destroy, relief=GROOVE).pack()
            self.w.bind("<Return>", self.destruir)
            self.w.bind("<Escape>", self.destruir)
        elif typeObject == "new_event":  # Nuevo evento
            btWidth = 14
            Label(self.w, text="Seleccione un evento", border=10).pack()
            f1 = Frame(self.w, border=1)
            f1.pack()
            f11 = Frame(f1)
            f11.pack(side=LEFT)
            Button(f11, text="Move", relief=GROOVE, command=lambda: self.new_event(
                "move"), width=btWidth).pack()
            Label(f1, text=" ").pack(side=LEFT)
            f12 = Frame(f1)
            f12.pack()
            Button(f12, text="Disminuir HP", relief=GROOVE, command=lambda: self.new_event(
                "minushp"), width=btWidth).pack()
            f2 = Frame(self.w, border=1)
            f2.pack()
            f21 = Frame(f2)
            f21.pack(side=LEFT)
            Button(f21, text="Disminuir Mana", relief=GROOVE, command=lambda: self.new_event(
                "minusmana"), width=btWidth).pack()
            Label(f2, text=" ").pack(side=LEFT)
            f22 = Frame(f2)
            f22.pack()
            Button(f22, text="No pasar", relief=GROOVE, command=lambda: self.new_event(
                "nopass"), width=btWidth).pack()
            f3 = Frame(self.w, border=1)
            f3.pack()
            f31 = Frame(f3)
            f31.pack(side=LEFT)
            Button(f31, text="Objeto", relief=GROOVE, command=lambda: self.new_event(
                "object"), width=btWidth).pack()
            Label(f3, text=" ").pack(side=LEFT)
            f32 = Frame(f3)
            f32.pack()
            Button(f32, text="Pasar", relief=GROOVE, command=lambda: self.new_event(
                "pass"), width=btWidth).pack()
            f4 = Frame(self.w, border=1)
            f4.pack()
            f41 = Frame(f4)
            f41.pack(side=LEFT)
            Button(f41, text="Aumentar HP", relief=GROOVE, command=lambda: self.new_event(
                "plushp"), width=btWidth).pack()
            Label(f4, text=" ").pack(side=LEFT)
            f42 = Frame(f4)
            f42.pack()
            Button(f42, text="Aumentar Mana", relief=GROOVE, command=lambda: self.new_event(
                "plusmana"), width=btWidth).pack()
            f5 = Frame(self.w, border=1)
            f5.pack()
            f51 = Frame(f5)
            f51.pack(side=LEFT)
            Button(f51, text="Teletransportar", relief=GROOVE, command=lambda: self.new_event(
                "teleport"), width=btWidth).pack()
            Label(f5, text=" ").pack(side=LEFT)
            f52 = Frame(f5)
            f52.pack()
            Button(f52, text="Longtext", relief=GROOVE, command=lambda: self.new_event(
                "longtext"), width=btWidth).pack()
            f6 = Frame(self.w, border=1)
            f6.pack()
            f61 = Frame(f6)
            f61.pack(side=LEFT)
            Button(f61, text="Sound", relief=GROOVE, command=lambda: self.new_event(
                "sound"), width=btWidth).pack()
            Label(f6, text=" ").pack(side=LEFT)
            f62 = Frame(f6)
            f62.pack()
            Button(f62, text="Mute", relief=GROOVE, command=lambda: self.new_event(
                "mute"), width=btWidth).pack()
            f7 = Frame(self.w, border=1)
            f7.pack()
            f71 = Frame(f7)
            f71.pack(side=LEFT)
            Button(f71, text="Autosave", relief=GROOVE, command=lambda: self.new_event(
                "autosave"), width=btWidth).pack()
            Label(f7, text=" ").pack(side=LEFT)
            f72 = Frame(f7)
            f72.pack()
            Button(f72, text="Muerte Subita", relief=GROOVE, command=lambda: self.new_event(
                "suddendeath"), width=btWidth).pack()
            f8 = Frame(self.w, border=1)
            f8.pack()
            f81 = Frame(f8)
            f81.pack(side=LEFT)
            Button(f81, text="No pass Alert", relief=GROOVE, command=lambda: self.new_event(
                "nopassalert"), width=btWidth).pack()
            Label(f8, text=" ").pack(side=LEFT)
            f82 = Frame(f8)
            f82.pack()
            Button(f82, text="Text", relief=GROOVE, command=lambda: self.new_event(
                "text"), width=btWidth).pack()
            Label(self.w, text=" ").pack()
            Button(self.w, text="Cancelar",
                   command=self.w.destroy, relief=GROOVE).pack()
            self.w.bind("<Return>", self.destruir)
            self.w.bind("<Escape>", self.destruir)
        elif typeObject == "new_key_building":  # Nuevo edificio con llave
            Label(self.w,
                  text="Rellene ambos campos para crear un edificio restrictivo, rellene solo 'Archivo de mapa' pa" +
                       "ra crear un link a su archivo o deje ambos campos en blanco para crear solo un edificio decorativo.",
                  border=10, wraplength=280).pack()
            f = Frame(self.w, border=3)
            f.pack()
            Label(f, text="Archivo del mapa ", anchor=E, width=15).pack(
                side=LEFT)
            self.buildMap = Entry(f, relief=GROOVE, width=25)
            self.buildMap.pack()
            self.buildMap.focus_force()
            f = Frame(self.w, border=3)
            f.pack()
            Label(f, text="Nombre de la llave ", anchor=E, width=15).pack(
                side=LEFT)
            self.buildKey = Entry(f, relief=GROOVE, width=25)
            self.buildKey.pack()
            Label(self.w, text="", height=1).pack()
            Button(self.w, text="Crear", relief=GROOVE,
                   command=self.sendResBuild).pack()
            self.w.bind("<Escape>", self.destruir)
        elif typeObject == "new_nokey_building":  # Nuevo edificio sin llave
            Label(self.w, text="Rellene 'Archivo de mapa' para crear un link a su archivo o deje el campo en " +
                               "blanco para crear un edificio decorativo.", border=10, wraplength=280,
                  fg=COMMENT_COLOR).pack()
            f = Frame(self.w, border=3)
            f.pack()
            Label(f, text="Archivo del mapa ", anchor=E, width=15).pack(
                side=LEFT)
            self.buildMap = Entry(f, relief=GROOVE, width=25)
            self.buildMap.pack()
            self.buildMap.focus_force()
            Label(self.w, text="", height=1).pack()
            Button(self.w, text="Crear", relief=GROOVE,
                   command=self.sendNoResBuild).pack()
            self.w.bind("<Escape>", self.destruir)
        # Ingresar los datos para una puerta
        elif typeObject == "new_door" or typeObject == "edit_door":
            Label(self.w, text="Ingrese los siguientes datos para crear una puerta.",
                  border=10, fg=COMMENT_COLOR).pack()
            f = Frame(self.w, border=3)
            f.pack()
            Label(f, text="Archivo del mapa ", anchor=E, width=15).pack(
                side=LEFT)
            self.doorMap = Entry(f, relief=GROOVE, width=25)
            self.doorMap.pack()
            self.doorMap.focus_force()
            f = Frame(self.w, border=3)
            f.pack()
            Label(f, text="Nombre de la llave ", anchor=E, width=15).pack(
                side=LEFT)
            self.doorKey = Entry(f, relief=GROOVE, width=25)
            self.doorKey.pack()
            Label(self.w, text="", height=1).pack()
            if typeObject == "new_door":
                Button(self.w, text="Crear", relief=GROOVE,
                       command=self.sendDoor).pack()
            else:
                Button(self.w, text="Editar", relief=GROOVE,
                       command=self.sendDoor).pack()
            self.w.bind("<Escape>", self.destruir)
            if typeObject == "edit_door":  # Inserto datos
                try:
                    if properties[5] != "%SELF%":
                        self.doorMap.insert(0, properties[5])
                except:
                    pass
                try:
                    if properties[6] != "%NULL%":
                        self.doorKey.insert(0, properties[6])
                except:
                    pass
        elif typeObject == "new_sound_background":  # Sonido de fondo
            folder = properties[5]
            try:
                tkSnack.initializeSnack(self.w)
            except:
                pass
            try:
                self.sound = tkSnack.Sound()
                _sound = True
            except:
                _sound = False
            if _sound:
                self.sound.config(fileformat="mp3")
            Label(
                self.w, text="Escoga un sonido de fondo para el actual mapa", border=10).pack()
            f = Frame(self.w, border=3)
            f.pack()
            Label(f, text="Archivo", anchor=E, width=6).pack(side=LEFT)
            # se cargan todas las texturas
            sounds = loadFromArchive(folder + "_ambience_sounds.txt")
            self.sound_background = StringVar(f)
            self.sound_background.set(
                "Escoja una sonido".rjust(30))  # valor por defecto
            w1 = apply(OptionMenu, (f, self.sound_background) + tuple(sounds))
            w1["width"] = 30
            w1["relief"] = GROOVE
            w1["anchor"] = W
            w1.pack(side=LEFT, padx=5)

            def _play(e=None):
                filename = self.sound_background.get().strip()
                if filename != "Escoja una sonido":
                    try:
                        self.sound.read(folder + filename)
                        self.sound.play()
                    except:
                        pass

            def _pause(e=None):
                self.sound.pause()

            def _stop(e=None):
                self.sound.stop()

            if _sound:
                Button(f, bitmap='snackPlay', command=_play, relief=GROOVE).pack(
                    side=LEFT, padx=1, pady=1)
                Button(f, bitmap='snackPause', command=_pause, relief=GROOVE).pack(
                    side=LEFT, padx=1, pady=1)
                Button(f, bitmap='snackStop', command=_stop, relief=GROOVE).pack(
                    side=LEFT, padx=1, pady=1)
            Button(self.w, text="Insertar", relief=GROOVE,
                   command=self.enviarBgSound).pack(pady=10)
            self.w.bind("<Escape>", self.destruir)
        elif typeObject == "new_sound_mob":  # Sonido del mob
            folder = properties[5]
            try:
                tkSnack.initializeSnack(self.w)
                _sound = True
            except:
                _sound = False
            if _sound:
                self.sound = tkSnack.Sound()
                self.sound.config(fileformat="mp3")
            Label(
                self.w, text="Escoja un sonido para el actual mob", border=10).pack()
            f = Frame(self.w, border=3)
            f.pack()
            Label(f, text="Archivo", anchor=E, width=6).pack(side=LEFT)
            # se cargan todas las texturas
            sounds = loadFromArchive(folder + "_mobs_sounds.txt")
            self.sound_background = StringVar(f)
            self.sound_background.set(
                "Escoja una sonido".rjust(30))  # valor por defecto
            w1 = apply(OptionMenu, (f, self.sound_background) + tuple(sounds))
            w1["width"] = 30
            w1["relief"] = GROOVE
            w1["anchor"] = W
            w1.pack(side=LEFT, padx=5)

            def _play(e=None):
                filename = self.sound_background.get().strip()
                if filename != "Escoja una sonido":
                    try:
                        self.sound.read(folder + filename)
                        self.sound.play()
                    except:
                        pass

            def _pause(e=None):
                self.sound.pause()

            def _stop(e=None):
                self.sound.stop()

            if _sound:
                Button(f, bitmap='snackPlay', command=_play, relief=GROOVE).pack(
                    side=LEFT, padx=1, pady=1)
                Button(f, bitmap='snackPause', command=_pause, relief=GROOVE).pack(
                    side=LEFT, padx=1, pady=1)
                Button(f, bitmap='snackStop', command=_stop, relief=GROOVE).pack(
                    side=LEFT, padx=1, pady=1)
            Button(self.w, text="Insertar", relief=GROOVE,
                   command=self.enviarBgSound).pack(pady=10)
            self.w.bind("<Escape>", self.destruir)
        # Ingresar los datos para una escalera
        elif typeObject == "new_stair" or typeObject == "edit_stair":
            Label(self.w, text="Ingrese los siguientes datos para crear una escalera",
                  border=10, fg=COMMENT_COLOR).pack()
            f = Frame(self.w, border=3)
            f.pack()
            Label(f, text="Archivo del mapa ", anchor=E, width=15).pack(
                side=LEFT)
            self.stairMap = Entry(f, relief=GROOVE, width=25)
            self.stairMap.pack()
            self.stairMap.focus_force()
            f = Frame(self.w, border=3)
            f.pack()
            if typeObject == "new_stair":
                Button(self.w, text="Crear", relief=GROOVE,
                       command=self.sendStair).pack()
            else:
                Button(self.w, text="Editar", relief=GROOVE,
                       command=self.sendStair).pack()
            self.w.bind("<Escape>", self.destruir)
            if typeObject == "edit_stair":
                try:
                    self.stairMap.insert(0, properties[5])
                except:
                    pass
        elif typeObject == "new_map":  # Creación de un nuevo mapa
            Label(self.w, text="Ingrese los siguientes datos",
                  border=10, fg=COMMENT_COLOR).pack()
            f = Frame(self.w, border=3)
            f.pack()
            Label(f, text="Nombre ", anchor=E, width=15).pack(side=LEFT)
            self.namemap = Entry(f, relief=GROOVE, width=25)
            self.namemap.pack()
            self.namemap.focus_force()
            f = Frame(self.w, border=3)
            f.pack()
            Label(f, text="Descripción ", width=15, anchor=E).pack(side=LEFT)
            self.descripcionmap = Entry(f, width=25)
            self.descripcionmap.pack()
            f = Frame(self.w, border=3)
            f.pack()
            Label(f, text="Hora (día/noche) ",
                  width=15, anchor=E).pack(side=LEFT)
            self.horamap = Entry(f, width=25)
            self.horamap.pack()
            f = Frame(self.w, border=3)
            f.pack()
            Label(f, text="Terreno (default) ", width=15, anchor=E).pack(
                side=LEFT)
            self.terrainmap = Entry(f, width=25)
            self.terrainmap.pack()
            f = Frame(self.w, border=3)
            f.pack()
            Label(f, text="Nombre del autor ", width=15, anchor=E).pack(
                side=LEFT)
            self.autormap = Entry(f, width=25)
            self.autormap.pack()
            f = Frame(self.w, border=3)
            f.pack()
            Label(f, text="Largo (max 19) ", width=15, anchor=E).pack(
                side=LEFT)
            self.largomap = Entry(f, width=3)
            self.largomap.pack()
            f = Frame(self.w, border=3)
            f.pack()
            Label(f, text="Ancho (max 18) ", width=15, anchor=E).pack(
                side=LEFT)
            self.anchomap = Entry(f, width=3)
            self.anchomap.pack()
            Label(self.w, text="", height=1).pack()
            Button(self.w, text="Crear nuevo mapa",
                   relief=GROOVE, command=self.new_map).pack()
            self.w.bind("<Escape>", self.destruir)
        # Crear un nuevo mob
        elif typeObject == "new_mob" or typeObject == "edit_mob":
            def _setmusic():
                q = pop(['Escoger sonido de fondo',
                         str(os.getcwd()).replace("\\", "/") + "/" +
                         "data/" + "icons/" + "sound_add.ico",
                         'new_sound_mob', 120, 380, "data/sound/mobs/"])
                q.w.mainloop(2)
                if q.sent:
                    self.soundmob.delete(0, END)
                    self.soundmob.insert(
                        0, str(q.values[0]).replace(".wav", ""))
                del q

            try:
                tkSnack.initializeSnack(self.w)
                _sound = True
            except:
                _sound = False
            if typeObject == "new_mob":
                def _newNpc():
                    self.values.append("create-new-npc")
                    self.sent = True
                    self.destruir()

                f = Frame(self.w, border=8)
                f.pack(fill=X)
                Button(
                    f, text="Cambiar a NPC", relief=GROOVE, command=_newNpc).pack()
            Label(
                self.w, text="Ingrese las propiedades del mob", border=5).pack()
            f = Frame(self.w, border=3)
            f.pack(fill=X)
            Label(f, text="Nombre", anchor=E, width=11).pack(side=LEFT)
            self.namemob = Entry(f, relief=GROOVE, width=30)
            self.namemob.pack(side=LEFT, padx=9)
            self.namemob.focus_force()
            f = Frame(self.w, border=3)
            f.pack(fill=X)
            Label(f, text="Vida   ", anchor=E, width=12).pack(side=LEFT)
            self.vidamob = Entry(f, relief=GROOVE, width=6)
            self.vidamob.pack(side=LEFT, padx=2)
            Label(f, text="Regeneración ", anchor=E, width=13).pack(side=LEFT)
            self.regeneracionmob = Entry(f, relief=GROOVE, width=6)
            self.regeneracionmob.pack(side=LEFT, padx=3)
            f = Frame(self.w, border=3)
            f.pack(fill=X)
            Label(f, text="Ataque   ", anchor=E, width=12).pack(side=LEFT)
            self.ataquemob = Entry(f, relief=GROOVE, width=6)
            self.ataquemob.pack(side=LEFT, padx=2)
            Label(f, text="Defensa ", anchor=E, width=13).pack(side=LEFT)
            self.defensamob = Entry(f, relief=GROOVE, width=6)
            self.defensamob.pack(side=LEFT, padx=3)
            f = Frame(self.w, border=3)
            f.pack(fill=X)
            Label(f, text="Target   ", anchor=E, width=12).pack(side=LEFT)
            self.targetmob = Entry(f, relief=GROOVE, width=6)
            self.targetmob.pack(side=LEFT, padx=2)
            Label(f, text="Velocidad ", anchor=E, width=13).pack(side=LEFT)
            self.velocidadmob = Entry(f, relief=GROOVE, width=6)
            self.velocidadmob.pack(side=LEFT, padx=3)
            f = Frame(self.w, border=3)
            f.pack(fill=X)
            Label(f, text="Movimiento  ", anchor=E, width=12).pack(side=LEFT)
            self.movimientomob = Entry(f, relief=GROOVE, width=6)
            self.movimientomob.pack(side=LEFT, padx=2)
            Label(f, text="Experiencia ", anchor=E, width=13).pack(side=LEFT)
            self.experienciamob = Entry(f, relief=GROOVE, width=6)
            self.experienciamob.pack(side=LEFT, padx=3)
            f = Frame(self.w, border=3)
            f.pack(fill=X)
            Label(f, text="Máxima distancia desde el Origen", anchor=E, width=32).pack(
                side=LEFT, padx=2)
            self.maxdistmob = Entry(f, relief=GROOVE, width=6)
            self.maxdistmob.pack(side=LEFT)
            f = Frame(self.w, border=3)
            f.pack(fill=X)
            Label(f, text="Reseña", anchor=E, width=11).pack(side=LEFT)
            self.infomob = Entry(f, relief=GROOVE, width=30)
            self.infomob.pack(side=LEFT, padx=9)
            f = Frame(self.w, border=3)
            f.pack(fill=X)
            Label(f, text="Objeto  ", anchor=E, width=12).pack(side=LEFT)
            self.objetomob = Entry(f, relief=GROOVE, width=23)
            self.objetomob.pack(side=LEFT, padx=2)
            Button(f, text=" + ", relief=GROOVE, command=self.addObject).pack()
            f = Frame(self.w)
            f.pack(fill=X, padx=3, pady=1)
            Label(f, text="Sonido  ", anchor=E, width=12).pack(side=LEFT)
            self.soundmob = Entry(f, relief=GROOVE, width=23)
            self.soundmob.pack(side=LEFT, padx=2)
            if _sound:
                Button(
                    f, bitmap='snackPlay', relief=GROOVE, command=_setmusic).pack()
            f = Frame(self.w)
            f.pack(fill=X, padx=3, pady=3)
            Label(f, text="Persigue  ", anchor=E, width=12).pack(side=LEFT)
            if isWindows():
                tuplewidth = 4
            else:
                tuplewidth = 9
            self.persiguemob = StringVar(f)
            self.persiguemob.set("No")  # valor por defecto
            w = apply(OptionMenu, (f, self.persiguemob) + tuple(["Si", "No"]))
            w["width"] = tuplewidth
            w["relief"] = GROOVE
            w.pack(side=LEFT)
            Label(f, text="Escapa", anchor=E, width=6).pack(side=LEFT)
            self.escapamob = StringVar(f)
            self.escapamob.set("No")  # valor por defecto
            w1 = apply(OptionMenu, (f, self.escapamob) + tuple(["Si", "No"]))
            w1["width"] = tuplewidth
            w1["relief"] = GROOVE
            w1.pack(side=LEFT, padx=2)
            f = Frame(self.w)
            f.pack(fill=X, padx=3, pady=1)
            Label(f, text="Combate  ", anchor=E, width=12).pack(side=LEFT)
            self.tipocombmob = StringVar(f)
            self.tipocombmob.set("Normal")  # valor por defecto
            w2 = apply(
                OptionMenu, (f, self.tipocombmob) + tuple(["Lineal", "Normal", "Grupal"]))
            w2["width"] = tuplewidth
            w2["relief"] = GROOVE
            w2.pack(side=LEFT)
            Label(f, text="Ataque", anchor=E, width=6).pack(side=LEFT)
            self.tipoatkmob = StringVar(f)
            self.tipoatkmob.set("Normal")  # valor por defecto
            w3 = apply(
                OptionMenu, (f, self.tipoatkmob) + tuple(["Normal", "Largo"]))
            w3["width"] = tuplewidth
            w3["relief"] = GROOVE
            w3.pack(side=LEFT, padx=2)
            Label(self.w, text="", height=1).pack()
            if typeObject == "new_mob":
                Button(self.w, text="Crear mob", relief=GROOVE,
                       command=self.new_mob).pack()
            else:
                Button(self.w, text="Editar mob", relief=GROOVE,
                       command=self.new_mob).pack()
            self.w.bind("<Escape>", self.destruir)
            # Se inserta la información si se edita
            if typeObject == "edit_mob":
                try:
                    self.namemob.insert(0, properties[5])
                except:
                    pass
                try:
                    self.vidamob.insert(0, int(properties[6]))
                except:
                    pass
                try:
                    self.regeneracionmob.insert(0, int(properties[7]))
                except:
                    pass
                try:
                    self.ataquemob.insert(0, int(properties[8]))
                except:
                    pass
                try:
                    self.defensamob.insert(0, int(properties[9]))
                except:
                    pass
                try:
                    self.targetmob.insert(0, int(properties[10]))
                except:
                    pass
                try:
                    self.velocidadmob.insert(0, int(properties[11]))
                except:
                    pass
                try:
                    self.movimientomob.insert(0, int(properties[12]))
                except:
                    pass
                try:
                    self.experienciamob.insert(0, int(properties[13]))
                except:
                    pass
                try:
                    self.maxdistmob.insert(0, int(properties[14]))
                except:
                    self.maxdistmob.insert(0, 0)
                try:
                    self.infomob.insert(0, properties[15])
                except:
                    pass
                try:
                    if properties[16] != "%NULL%":
                        self.objetomob.insert(0, properties[16])
                except:
                    pass
                try:
                    if properties[17] == "True":
                        self.escapamob.set("Si")
                    else:
                        self.escapamob.set("No")
                except:
                    pass
                try:
                    if properties[18] == "True":
                        self.persiguemob.set("Si")
                    else:
                        self.persiguemob.set("No")
                except:
                    pass
                try:
                    if properties[19] == "GRUPAL":
                        self.tipocombmob.set("Grupal")
                    elif properties[19] == "LINEAL":
                        self.tipocombmob.set("Lineal")
                    else:
                        self.tipocombmob.set("Normal")
                except:
                    pass
                try:
                    if properties[20] == "LARGO":
                        self.tipoatkmob.set("Largo")
                    else:
                        self.tipoatkmob.set("Normal")
                except:
                    pass
                try:
                    if properties[21] == "%NOSOUND%":
                        self.soundmob.insert(0, "")
                    else:
                        self.soundmob.insert(0, str(properties[21]).strip())
                except:
                    pass
        # Crear un nuevo mob
        elif typeObject == "new_npc" or typeObject == "edit_npc":
            Label(
                self.w, text="Ingrese las propiedades del npc", border=5).pack()
            f = Frame(self.w, border=3)
            f.pack(fill=X)
            Label(f, text="Nombre ", anchor=E, width=11).pack(side=LEFT)
            self.namenpc = Entry(f, relief=GROOVE, width=30)
            self.namenpc.pack(padx=0)
            self.namenpc.focus_force()
            f = Frame(self.w, border=3)
            f.pack(fill=X)
            Label(f, text="Descripción", anchor=E, width=11).pack(side=LEFT)
            self.descnpc = Entry(f, relief=GROOVE, width=30)
            self.descnpc.pack()
            f = Frame(self.w, border=3)
            f.pack(fill=X)
            Label(f, text="String", anchor=E, width=11).pack(side=LEFT)
            self.stringnpc = Entry(f, relief=GROOVE, width=30)
            self.stringnpc.pack()
            f = Frame(self.w, border=3)
            f.pack(fill=X)
            Label(f, text="Oro   ", anchor=E, width=12).pack(side=LEFT)
            self.oronpc = Entry(f, relief=GROOVE, width=6)
            self.oronpc.pack(side=LEFT, padx=1)
            Label(f, text="Distancia ", anchor=E, width=14).pack(side=LEFT)
            self.distnpc = Entry(f, relief=GROOVE, width=6)
            self.distnpc.pack(side=LEFT)
            f = Frame(self.w, border=3)
            f.pack(fill=X)
            Label(f, text="Objeto  ", anchor=E, width=12).pack(side=LEFT)
            self.objetonpc = Entry(f, relief=GROOVE, width=23)
            self.objetonpc.pack(side=LEFT)
            Label(f, text=" ").pack(side=LEFT)
            Button(f, text=" + ", relief=GROOVE,
                   command=self.addObjectnpc).pack()
            f = Frame(self.w, border=3)
            f.pack(fill=X)
            Label(f, text="Request ", anchor=E, width=11).pack(side=LEFT)
            self.requestnpc = Entry(f, relief=GROOVE, width=30)
            self.requestnpc.pack(padx=0)
            f = Frame(self.w, border=3)
            f.pack(fill=X)
            Label(f, text="Quest req. ", anchor=E, width=11).pack(side=LEFT)
            self.needquestnpc = Entry(f, relief=GROOVE, width=30)
            self.needquestnpc.pack(padx=0)
            f = Frame(self.w)
            f.pack(fill=X, padx=3, pady=1)
            Label(f, text="Mueve  ", anchor=E, width=12).pack(side=LEFT)
            if isWindows():
                tuplewidth = 3
            else:
                tuplewidth = 7
            self.movenpc = StringVar(f)
            self.movenpc.set("No")  # valor por defecto
            w = apply(OptionMenu, (f, self.movenpc) + tuple(["Si", "No"]))
            w["width"] = tuplewidth
            w["relief"] = GROOVE
            w.pack(side=LEFT)
            Label(f, text="Fade", anchor=E, width=7).pack(side=LEFT)
            self.fadenpc = StringVar(f)
            self.fadenpc.set("No")  # valor por defecto
            w1 = apply(OptionMenu, (f, self.fadenpc) + tuple(["Si", "No"]))
            w1["width"] = tuplewidth
            w1["relief"] = GROOVE
            w1.pack()
            Label(self.w, text="", height=1).pack()
            if typeObject == "new_npc":
                Button(self.w, text="Crear npc", relief=GROOVE,
                       command=self.new_npc).pack()
            else:
                Button(self.w, text="Editar npc", relief=GROOVE,
                       command=self.new_npc).pack()
            self.w.bind("<Escape>", self.destruir)
            if typeObject == "edit_npc":  # Inserto datos de edición
                try:
                    self.namenpc.insert(0, properties[5])
                except:
                    pass
                try:
                    self.descnpc.insert(0, properties[6])
                except:
                    pass
                try:
                    self.stringnpc.insert(0, properties[7])
                except:
                    pass
                try:
                    self.oronpc.insert(0, int(properties[8]))
                except:
                    pass
                try:
                    self.distnpc.insert(0, int(properties[9]))
                except:
                    pass
                try:
                    if properties[10] != "%NULL%":
                        self.objetonpc.insert(0, properties[10])
                except:
                    pass
                try:
                    if properties[11] != "%NULL%":
                        self.requestnpc.insert(0, properties[11])
                except:
                    pass
                try:
                    if properties[12] == "True":
                        self.movenpc.set("Si")
                    else:
                        self.movenpc.set("No")
                except:
                    pass
                try:
                    if properties[13] == "True":
                        self.fadenpc.set("Si")
                    else:
                        self.fadenpc.set("No")
                except:
                    pass
                try:
                    if properties[14] != "None":
                        self.needquestnpc.insert(0, properties[14])
                except:
                    pass
        elif typeObject == "new_object":  # Crear un nuevo objeto
            Label(
                self.w, text="Ingrese las propiedades del objeto", border=10).pack()
            f = Frame(self.w, border=3)
            f.pack(fill=X)
            Label(f, text="Nombre ", anchor=E, width=12).pack(side=LEFT)
            self.nameobj = Entry(f, relief=GROOVE, width=30)
            self.nameobj.pack()
            self.nameobj.focus_force()
            f = Frame(self.w, border=3)
            f.pack(fill=X)
            Label(f, text="Descripción ", anchor=E, width=12).pack(side=LEFT)
            self.descripcionobj = Entry(f, relief=GROOVE, width=30)
            self.descripcionobj.pack()
            f = Frame(self.w, border=3)
            f.pack(fill=X, pady=0)
            Label(f, text="Tipo", anchor=E, width=12).pack(side=LEFT)
            self.tipoobj = StringVar(f)
            self.tipoobj.set("< -- >".rjust(26))  # valor por defecto
            # se cargan todos los tipos de objetos
            object_type = loadFromArchive(
                "data/doc/documentation/object_type.txt")
            object_type.sort()
            w2 = apply(OptionMenu, (f, self.tipoobj) + tuple(object_type))
            w2["width"] = 26
            w2["relief"] = GROOVE
            w2["anchor"] = W
            w2.pack(side=LEFT, padx=17)
            fe = Frame(self.w)
            fe.pack(fill=X, pady=2)
            # se cargan todas las texturas
            self.textures = loadFromArchive("data/images/items/_textures.txt")
            Label(fe, text="Textura", anchor=E, width=12).pack(side=LEFT)
            self.texturaobj = StringVar(fe)
            self.texturaobj.set("< -- >".rjust(26))  # valor por defecto
            w1 = apply(
                OptionMenu, (fe, self.texturaobj) + tuple(self.textures))
            w1["width"] = 26
            w1["relief"] = GROOVE
            w1["anchor"] = W
            w1.pack(side=LEFT, padx=20)
            f = Frame(self.w, border=3)
            f.pack(fill=X, pady=0)
            Label(f, text="ID ", anchor=E, width=12).pack(side=LEFT)
            self.idobj = Entry(f, relief=GROOVE, width=6)
            self.idobj.pack(side=LEFT)
            Label(f, text="Stackable ", anchor=E, width=12).pack(
                side=LEFT, padx=1)
            self.stackableobj = StringVar(f)
            self.stackableobj.set("False")  # valor por defecto
            w3 = apply(
                OptionMenu, (f, self.stackableobj) + tuple(["True", "False"]))
            if isWindows():
                w3["width"] = 4
            else:
                w3["width"] = 4
            w3["relief"] = GROOVE
            w3["anchor"] = W
            w3.pack(side=LEFT, padx=6)
            f = Frame(self.w, border=3)
            f.pack(fill=X)
            Label(f, text="Duración ", anchor=E, width=12).pack(side=LEFT)
            self.vidaobj = Entry(f, relief=GROOVE, width=6)
            self.vidaobj.pack(side=LEFT)
            Label(f, text="      Propiedades", anchor=W, width=13).pack(
                side=LEFT, padx=1)
            self.propiedadesobj = Entry(f, relief=GROOVE, width=10)
            self.propiedadesobj.pack(side=LEFT)
            Label(self.w, text="", height=1).pack()
            Button(self.w, text="Crear objeto",
                   relief=GROOVE, command=self.new_obj).pack()
            self.w.bind("<Escape>", self.destruir)
            lastTipo = ["<all>"]

            def _setLast(e=None):
                lastTipo[0] = "change"

            # Obtengo la textura y cambio el icono de la ventana
            def _sortByType(tipo, menu, e=None):
                if self.texturaobj.get().strip() != "< -- >":
                    try:
                        self.w.iconbitmap(
                            "data/icons/items/" + self.texturaobj.get() + "_16.ico")
                    except:
                        self.w.iconbitmap(icon)
                else:
                    try:
                        self.w.iconbitmap(icon)
                    except:
                        self.w.iconbitmap("data/icons/mapeditor.ico")
                if lastTipo[0] != tipo:  # Si el tipo cambio
                    if tipo != "<all>" and tipo.strip() != "< -- >":
                        # Oculto la lista anterior
                        menu.pack_forget()
                        self.texturaobj
                        del menu
                        valid_textures = []
                        # Busco los elementos correctos e inserto propiedad
                        self.propiedadesobj.config(state=NORMAL)
                        self.propiedadesobj.delete(0, END)
                        if tipo == "armor/botas":
                            valid = ["botas_"]
                            self.propiedadesobj.insert(0, "0,def")
                        elif tipo == "armor/casco":
                            valid = ["casco_"]
                            self.propiedadesobj.insert(0, "0,def")
                        elif tipo == "armor/chaleco":
                            valid = ["chaleco_"]
                            self.propiedadesobj.insert(0, "0,def")
                        elif tipo == "armor/pantalones":
                            valid = ["pantalon_"]
                            self.propiedadesobj.insert(0, "0,def")
                        elif tipo == "bullet":
                            valid = ["flecha_"]
                            self.propiedadesobj.insert(0, "daño,0")
                        elif tipo == "coin":
                            valid = ["iron_", "gold_"]
                            self.propiedadesobj.insert(0, "0,0")
                            self.propiedadesobj.config(state=DISABLED)
                        elif tipo == "mana/normal" or tipo == "potion/normal":
                            valid = ["pocion_", "liquido_", "mana_"]
                            self.propiedadesobj.insert(0, "hp,0")
                        elif tipo == "object/carry":
                            valid = ["chest_", "saco_", "mochila_"]
                            self.propiedadesobj.insert(0, "tipo,uso")
                        elif tipo == "object/holy":
                            valid = ["biblia"]
                            self.propiedadesobj.insert(0, "tipo,uso")
                        elif tipo == "object/key":
                            valid = ["key_"]
                            self.propiedadesobj.insert(
                                0, "Llave,Abrir puertas")
                            self.propiedadesobj.config(state=DISABLED)
                        elif tipo == "potion/apple":
                            valid = ["manzana_"]
                            self.propiedadesobj.insert(0, "hp,0")
                        elif tipo == "potion/food":
                            valid = ["food_"]
                            self.propiedadesobj.insert(0, "hp,0")
                        elif tipo == "read":
                            valid = [
                                "libro_", "book_", "spellbook_", "spellbook", "papel_"]
                            self.propiedadesobj.insert(0, "file,0")
                        elif tipo == "weapon/left":
                            valid = ["arco_", "ballesta_", "escudo_", "lanza_"]
                            self.propiedadesobj.insert(0, "daño,0")
                        elif tipo == "weapon/right":
                            valid = ["mazo_", "hacha_", "espada_"]
                            self.propiedadesobj.insert(0, "daño,0")
                        for i in self.textures:
                            if isIn(i, valid):
                                valid_textures.append(i)
                        menu = apply(
                            OptionMenu, (fe, self.texturaobj) + tuple(valid_textures))
                        menu["width"] = 26
                        menu["relief"] = GROOVE
                        menu["anchor"] = W
                        menu.pack(side=LEFT, padx=20)
                        lastTipo[0] = tipo
                        # valor por defecto
                        self.texturaobj.set(valid_textures[0])
                    else:
                        # valor por defecto
                        self.texturaobj.set("< -- >".rjust(26))
                try:
                    self.w.after(
                        250, partial(_sortByType, self.tipoobj.get(), menu))
                except:
                    pass

            _sortByType("<all>", w1)
            fe.bind("<Button-1>", _setLast)
        # Ingresar un dígito positivo
        elif typeObject == "new_absdigit" or typeObject == "edit_absdigit":
            f = Frame(self.w, border=10)
            f.pack()
            Label(f, text=properties[5] + " ",
                  anchor=E, width=8).pack(side=LEFT)
            self.absDigit = Entry(f, relief=GROOVE, width=35)
            self.absDigit.pack()
            self.absDigit.focus_force()
            if typeObject == "new_absdigit":
                Button(self.w, text="Crear", relief=GROOVE,
                       command=self.enviarAbsDigit).pack()
            else:
                Button(self.w, text="Editar", relief=GROOVE,
                       command=self.enviarAbsDigit).pack()
            self.w.bind("<Escape>", self.destruir)
            if typeObject == "edit_absdigit":
                try:
                    self.absDigit.insert(0, properties[6])
                except:
                    pass
        elif typeObject == "new_move":  # Ingresar un movimiento
            Label(self.w, text="Ingrese dos puntos para mover al jugador, A (inicio) a B (final)",
                  border=10, wraplength=280).pack()
            f = Frame(self.w, border=10)
            f.pack()
            Label(f, text="Punto A (x,y)", anchor=E, width=10).pack(side=LEFT)
            self.eventMoveAx = Entry(f, relief=GROOVE, width=6)
            self.eventMoveAx.pack(side=LEFT)
            Label(f, text=" ").pack(side=LEFT)
            self.eventMoveAy = Entry(f, relief=GROOVE, width=6)
            self.eventMoveAy.pack()
            self.eventMoveAx.focus_force()
            f1 = Frame(self.w, border=5)
            f1.pack()
            Label(f1, text="Punto B (x,y)", anchor=E, width=10).pack(side=LEFT)
            self.eventMoveBx = Entry(f1, relief=GROOVE, width=6)
            self.eventMoveBx.pack(side=LEFT)
            Label(f1, text=" ").pack(side=LEFT)
            self.eventMoveBy = Entry(f1, relief=GROOVE, width=6)
            self.eventMoveBy.pack()
            Label(self.w, text="", height=1).pack()
            Button(self.w, text="Crear", relief=GROOVE,
                   command=self.enviarMove).pack()
            self.w.bind("<Escape>", self.destruir)
        # Ingresar un texto
        elif typeObject == "new_text" or typeObject == "edit_text":
            f = Frame(self.w, border=10)
            f.pack()
            Label(f, text="Texto ", anchor=E, width=8).pack(side=LEFT)
            self.eventText = Entry(f, relief=GROOVE, width=35)
            self.eventText.pack()
            self.eventText.focus_force()
            if typeObject == "new_text":
                Button(self.w, text="Crear", relief=GROOVE,
                       command=self.enviarTexto).pack()
            else:
                Button(self.w, text="Editar", relief=GROOVE,
                       command=self.enviarTexto).pack()
            self.w.bind("<Escape>", self.destruir)
            if typeObject == "edit_text":
                try:
                    self.eventText.insert(0, properties[5])
                except:
                    pass
        # Ingresar un longtext
        elif typeObject == "new_longtext" or typeObject == "edit_longtext":
            f = Frame(self.w, border=10)
            f.pack()
            Label(f, text="Archivo ", anchor=E, width=8).pack(side=LEFT)
            self.eventLongText = Entry(f, relief=GROOVE, width=35)
            self.eventLongText.pack()
            self.eventLongText.focus_force()
            if typeObject == "new_longtext":
                Button(self.w, text="Insertar", relief=GROOVE,
                       command=self.enviarLongText).pack()
            else:
                Button(self.w, text="Editar", relief=GROOVE,
                       command=self.enviarLongText).pack()
            self.w.bind("<Escape>", self.destruir)
            if typeObject == "edit_longtext":
                try:
                    self.eventLongText.insert(0, properties[5])
                except:
                    pass
        # Ingresar un texto largo
        elif typeObject == "new_maplink" or typeObject == "edit_maplink":
            f = Frame(self.w, border=10)
            f.pack()
            Label(f, text="Mapa ", anchor=E, width=8).pack(side=LEFT)
            self.eventMap = Entry(f, relief=GROOVE, width=35)
            self.eventMap.pack()
            self.eventMap.focus_force()
            if typeObject == "new_maplink":
                Button(self.w, text="Crear", relief=GROOVE,
                       command=self.enviarMapLink).pack()
            else:
                Button(self.w, text="Editar", relief=GROOVE,
                       command=self.enviarMapLink).pack()
            self.w.bind("<Escape>", self.destruir)
            if typeObject == "edit_maplink":
                try:
                    self.eventMap.insert(0, properties[5])
                except:
                    pass
        # Ingresar un sonido
        elif typeObject == "new_sound" or typeObject == "edit_sound":
            f = Frame(self.w, border=10)
            f.pack()
            Label(f, text="Sonido ", anchor=E, width=8).pack(side=LEFT)
            self.eventSound = Entry(f, relief=GROOVE, width=35)
            self.eventSound.pack()
            self.eventSound.focus_force()
            if typeObject == "new_sound":
                Button(self.w, text="Insertar", relief=GROOVE,
                       command=self.enviarSound).pack()
            else:
                Button(self.w, text="Insertar", relief=GROOVE,
                       command=self.enviarSound).pack()
            self.w.bind("<Escape>", self.destruir)
            if typeObject == "edit_sound":
                try:
                    self.eventSound.insert(0, properties[5])
                except:
                    pass
        # Nueva antorcha con luminosidad por definir
        elif typeObject == "new_torch":
            Label(
                self.w, text="Ingrese la luminosidad de la antorcha", border=10).pack()
            f = Frame(self.w, border=3)
            f.pack()
            Label(f, text="Luminosidad ", anchor=E, width=10).pack(side=LEFT)
            self.lightTorch = Entry(f, relief=GROOVE, width=25)
            self.lightTorch.pack()
            self.lightTorch.focus_force()
            Label(self.w, text="", height=1).pack()
            Button(self.w, text="Insertar", relief=GROOVE,
                   command=self.sendTorch).pack()
        elif typeObject == "save_map_name":  # Guardar un mapa
            Label(
                self.w, text="Ingrese el nombre de su mapa", border=10).pack()
            f = Frame(self.w, border=3)
            f.pack()
            Label(f, text="Nombre del mapa: ", anchor=W).pack(side=LEFT)
            self.namePartida = Entry(f, relief=GROOVE)
            self.namePartida.pack()
            self.namePartida.focus_force()
            Label(self.w, text="", height=1).pack()
            Button(self.w, text="Guardar", relief=GROOVE,
                   command=self.savegame).pack()
        # Licencia o gnu
        elif typeObject in ["licence", "changelog", "ayuda", "longtext", "license"]:
            archivo = open(properties[5], "r")
            Yscroll = Scrollbar(self.w)
            Yscroll.pack(side=RIGHT, fill=Y)
            texto = Text(self.w, wrap=NONE,
                         yscrollcommand=Yscroll.set, xscrollcommand=None)
            texto.focus_force()
            for i in archivo:
                texto.insert(INSERT, i)
            texto.pack()
            texto.configure(state="disabled")
            Yscroll.config(command=texto.yview)
            archivo.close()
            self.w.bind("<Return>", self.destruir)
            self.w.bind("<Escape>", self.destruir)
        # Icono de la ventana
        try:
            self.w.iconbitmap(icon)
        except:
            self.w.iconbitmap("data/icons/mapeditor.ico")

    # Función que llama a una ventana para agregar un objeto
    def addObject(self, e=None):
        if isWindows():
            q = pop(
                ['Nuevo objeto', "data/icons/new_object.ico", 'new_object', 280, 320])
        else:
            q = pop(
                ['Nuevo objeto', "data/icons/new_object.ico", 'new_object', 300, 360])
        q.w.mainloop(2)
        if q.sent:
            self.objetomob.delete(0, END)
            self.objetomob.insert(0, q.values[0])
        del q

    # Función que llama a una ventana para agregar un objeto
    def addObjectnpc(self, e=None):
        if isWindows():
            q = pop(
                ['Nuevo objeto', "data/icons/new_object.ico", 'new_object', 280, 320])
        else:
            q = pop(
                ['Nuevo objeto', "data/icons/new_object.ico", 'new_object', 300, 360])
        q.w.mainloop(2)
        if q.sent:
            self.objetonpc.delete(0, END)
            self.objetonpc.insert(0, q.values[0])
        del q

    def destruir(self, e=None):  # Función para destruir la ventana via evento
        self.w.destroy()

    def enviarAbsDigit(self):  # Función que envía un numero positivo
        delMatrix(self.values)
        num = str(self.absDigit.get())
        if len(num) > 0 and (num.isdigit() or num.replace("%", "").isdigit()):
            self.values.append(num)
            self.sent = True
            self.destruir()

    def enviarBgSound(self):  # Función que envía el string del sonido
        a = self.sound_background.get().strip()
        if len(a) > 0 and a != "Escoja una sonido":
            self.sound.stop()
            self.values.append(a)
            self.sent = True
            self.destruir()

    def enviarMapLink(self):  # Función que envía el link de un mapa
        delMatrix(self.values)
        mapa = str(self.eventMap.get())
        if len(mapa) > 0 and ".lvl" in mapa:
            self.values.append(mapa)
            self.sent = True
            self.destruir()

    def enviarMove(self):  # Función que envía dos coordenadas de movimiento
        delMatrix(self.values)
        ax = str(self.eventMoveAx.get())
        ay = str(self.eventMoveAy.get())
        bx = str(self.eventMoveBx.get())
        by = str(self.eventMoveBy.get())
        # Si todos los campos no estan vacios
        if len(ax) > 0 and len(ay) > 0 and len(bx) > 0 and len(by) > 0:
            # Si todas las coordenadas son digitos
            if ax.isdigit() and ay.isdigit() and bx.isdigit() and by.isdigit():
                self.values.append(ax + "," + ay + "," + bx + "," + by)
                self.sent = True
                self.destruir()

    def enviarTexto(self, e=None):  # Función que envía un texto
        delMatrix(self.values)
        a = str(self.eventText.get())
        if len(a) > 0:
            self.values.append(a)
            self.sent = True
            self.destruir()

    def enviarLongText(self):  # Función que inserta un longtext
        delMatrix(self.values)
        a = str(self.eventLongText.get())
        if len(a) > 0 and (".txt" in a or ".TXT" in a):
            self.values.append(a)
            self.sent = True
            self.destruir()

    def enviarSound(self):  # Función que envía un sonido wav
        delMatrix(self.values)
        a = str(self.eventSound.get())
        if len(a) > 0 and (".wav" in a or ".WAV" in a):
            self.values.append(a)
            self.sent = True
            self.destruir()

    def kill(self):  # Función que destruye la ventana
        self.sent = False
        self.w.update()
        try:
            self.w.destroy()
        except:
            self.w.destroy()

    def new_event(self, ev):  # Función que envía un evento
        delMatrix(self.values)
        self.values.append(ev)
        self.sent = True
        self.destruir()

    def new_map(self):  # Función para enviar un nuevo mapa
        delMatrix(self.values)
        a = self.namemap.get().strip()
        b = self.descripcionmap.get().strip()
        c = self.horamap.get().strip().lower().replace("á", "a").replace(
            "é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
        d = self.terrainmap.get().strip()
        e = self.largomap.get().strip()
        f = self.anchomap.get().strip()
        g = self.autormap.get().strip()
        # Si los datos no estan vacios y el largo y ancho son números
        if len(a) > 0 and len(b) > 0 and len(c) > 0:
            # Se comprueba el largo y el ancho, si no fueron ingresados o son
            # erróneos se dejan como el máximo
            if e != "":
                if str(e).isdigit():
                    e = int(e)
                else:
                    e = 19
            else:
                e = 19
            if f != "":
                if str(f).isdigit():
                    f = int(f)
                else:
                    f = 18
            else:
                f = 18
            # Si el largo y ancho del mapa son correctos
            if 0 < e <= 19 and 0 < f <= 18:
                # Si la hora corresponde
                if (c == "dia" or "day") or (c == "noche" or c == "night"):
                    # Si el terreno corresponde
                    if str(d).isdigit() or len(d) == 0:
                        if len(d) != 0:  # Si el terreno es valido
                            if 100 < int(d) < 200:
                                d = int(d)
                            else:
                                d = 199  # tile sin rellenar (no valido)
                        else:
                            d = 199
                        if c == "dia" or c == "day":
                            c = 0  # si la hora escogida fue el dia
                        else:
                            c = 1
                        if len(g) == 0:
                            g = "Anonimo/Unknown"  # si no se ingreso un autor
                        self.values.append(a)
                        self.values.append(b)
                        self.values.append(c)
                        self.values.append(d)
                        self.values.append(e)
                        self.values.append(f)
                        self.values.append(g)
                        self.sent = True
                        self.destruir()

    def new_obj(self):  # Función que crea un nuevo objeto
        delMatrix(self.values)
        a = str(self.nameobj.get())
        b = str(self.descripcionobj.get())
        c = str(self.texturaobj.get())
        d = str(self.tipoobj.get())
        e = str(self.idobj.get())
        f = str(self.stackableobj.get())
        g = str(self.vidaobj.get())
        h = str(self.propiedadesobj.get())
        # Si todos los campos son no vacios (excepto la descripción
        if len(a) > 0 and len(c) > 0 and len(d) > 0 and len(e) > 0 and len(f) > 0 and len(g) > 0:
            if c.strip() != "< -- >" and d.strip() != "< -- >":
                # Si el id es un número, la vida es un numero y el stackable es
                # un booleano y las propiedades estan separadas por una coma
                if e.isdigit() and g.isdigit() and (f.upper() == "TRUE" or f.upper() == "FALSE"):
                    if len(b) == 0:
                        b = "No hay una descripcion disponible"
                    else:
                        b = replaceStrict(b)
                    if "," in h:  # Si las propiedades son validas
                        h = h.split(",")
                        h1 = h[0]
                        h2 = h[1]
                        if len(h1) == 0:
                            h1 = "0"
                        if len(h2) == 0:
                            h2 = "0"
                        h1 = desParseType(h1)
                        h2 = desParseType(h2)
                    else:
                        h1 = "int_0"
                        h2 = "int_0"
                    sep = "/_/"
                    obj = replaceStrict(
                        a) + sep + b + sep + c + sep + d + sep + e + sep + f + sep + g + sep + h1 + sep + h2
                    self.values.append(obj)
                    self.sent = True
                    self.destruir()

    def new_mob(self):  # Función que crea un nuevo mob
        delMatrix(self.values)
        a = str(self.ataquemob.get())
        b = str(self.vidamob.get())
        c = str(self.targetmob.get())
        d = str(self.velocidadmob.get())
        e = str(self.namemob.get())
        f = str(self.infomob.get())
        g = str(self.regeneracionmob.get())
        h = str(self.movimientomob.get())
        i = str(self.defensamob.get())
        j = str(self.experienciamob.get())
        k = str(self.objetomob.get())
        l = str(self.escapamob.get())
        m = str(self.persiguemob.get())
        n = str(self.maxdistmob.get())
        o = str(self.tipocombmob.get()).strip().upper()
        p = str(self.tipoatkmob.get()).strip().upper()
        q = str(self.soundmob.get()).strip()
        if l == "Si":
            l = "True"
        else:
            l = "False"
        if m == "Si":
            m = "True"
        else:
            m = "False"
        if q == "":
            q = "%NOSOUND%"
        # Se comprueban los campos numéricos
        if a.isdigit() and b.isdigit() and c.isdigit() and d.isdigit() and g.isdigit() and i.isdigit() and j.isdigit() and h.isdigit() and n.isdigit():
            # Ningún campo puede estar vacío
            if len(e) > 0 and len(f) > 0 and int(b) > 0 and int(c) >= 0 and int(d) >= 0 and int(g) >= 0 and int(
                    h) >= 0 and int(i) >= 0 and int(j) >= 0 and int(n) >= 0:
                self.sent = True
                self.values.append(a)
                self.values.append(b)
                self.values.append("IMAGE")
                self.values.append(c)
                self.values.append(d)
                self.values.append(e)
                self.values.append(f)
                self.values.append(g)
                self.values.append(h)
                self.values.append(i)
                self.values.append(j)
                self.values.append(k)
                self.values.append(l)
                self.values.append(m)
                self.values.append(n)
                self.values.append(o)
                self.values.append(p)
                self.values.append(q)
                self.destruir()

    def new_npc(self):  # Función que envía los datos del nuevo npc
        delMatrix(self.values)
        a = str(self.namenpc.get())
        b = str(self.descnpc.get())
        c = str(self.stringnpc.get())
        d = str(self.objetonpc.get())
        e = str(self.requestnpc.get())
        f = str(self.oronpc.get())
        g = str(self.movenpc.get())
        h = str(self.distnpc.get())
        i = str(self.fadenpc.get())
        j = str(self.needquestnpc.get())
        if i == "Si":
            i = "True"
        else:
            i = "False"
        if g == "Si":
            g = "True"
        else:
            g = "False"
        if len(a) > 0 and len(c) > 0 and len(i) > 0 and len(g) > 0:
            if (len(h) > 0 and h.isdigit()) or len(h) == 0:
                if (len(f) > 0 and h.isdigit()) or len(f) == 0:
                    if len(f) == 0:
                        f = "0"
                    if len(h) == 0:
                        h = "0"
                    if len(d) == 0:
                        d = "%NULL%"
                    if len(e) == 0:
                        e = "%NULL%"
                    if len(j) == 0:
                        j = "None"
                    self.values.append(a)
                    self.values.append("IMAGE")
                    self.values.append(b)
                    self.values.append(c)
                    self.values.append(d)
                    self.values.append(e)
                    self.values.append(f)
                    self.values.append(g)
                    self.values.append(h)
                    self.values.append(i)
                    self.values.append(j)
                    self.sent = True
                    self.destruir()

    def response(self, res):  # Función que envia una respuesta
        delMatrix(self.values)
        self.values.append(res)
        self.sent = True
        self.destruir()

    def savegame(self):  # Función que envia el nombre de la partida guardada
        delMatrix(self.values)
        name = self.namePartida.get().strip()
        noneTypes = "%&@#!?)(/"
        if len(name) > 0:
            able = True  # Compruebo que los caracteres ingresados sean validos
            for i in noneTypes:
                if i in name:
                    able = False
                    break
            if able:
                self.values.append(name)
                self.sent = True
                self.destruir()

    # Función que envia los datos para la creacion de una puerta
    def sendDoor(self):
        delMatrix(self.values)
        a = str(self.doorMap.get())
        b = str(self.doorKey.get())
        if len(a) >= 0:  # Si los datos no estan vacios
            if len(a) == 0:
                a = "%SELF%"  # Puerta que desaparece
            if len(b) == 0:
                b = "%NULL%"  # Si la puerta no necesita una llave
            if ".lvl" not in a and a != "%SELF%":
                a += ".lvl"  # Se le agrega la extension al nombre del mapa
            self.values.append(a)
            self.values.append(b)
            self.sent = True
            self.destruir()

    # Función que envia los datos para la creacion de un edificio no restictivo
    def sendNoResBuild(self):
        delMatrix(self.values)
        a = str(self.buildMap.get())
        if (".lvl" not in a) and len(a) > 0:
            a += ".lvl"  # Se le agreva el .lvl al nombre del mapa
        if a == "":
            a = "%NULL%"  # Se reemplaza por null
        self.values.append(a)
        self.sent = True
        self.destruir()

    # Función que envia los datos para la creacion de un edificio
    def sendResBuild(self):
        delMatrix(self.values)
        a = str(self.buildMap.get())
        b = str(self.buildKey.get())
        # Si ambos campos estan vacios o ambos campos no estan vacios o hay un
        # mapa que no necesita llaves
        if (a == "" and b == "") or (len(a) > 0 and len(b) > 0) or (len(a) > 0 and len(b) == 0):
            if (".lvl" not in a) and len(a) > 0:
                # Se le agrega .lvl al nombre del mapa en caso que exista
                a += ".lvl"
            if a == "":
                a = "%NULL%"
            if b == "":
                b = "%NULL%"
            self.values.append(a)
            self.values.append(b)
            self.sent = True
            self.destruir()

    def sendStair(self):  # Función que envia una escalera
        delMatrix(self.values)
        a = str(self.stairMap.get())
        if len(a) > 0:  # Si el adto no esta vacio
            if ".lvl" not in a:
                a += ".lvl"  # Se le agrega la extension al nombre del mapa
            self.values.append(a)
            self.values.append("%NULL%")
            self.sent = True
            self.destruir()

    def sendTorch(self):  # Función que envia la luminosidad de la antorcha
        delMatrix(self.values)
        a = str(self.lightTorch.get())
        if a.isdigit():  # Si el campo es numerico
            a = int(a)
            if a > 17:
                # Si la luminosidad es mayor al largo del mapa, se restringe al
                # maximo
                a = 17
            self.values.append(a)
            self.sent = True
            self.destruir()
