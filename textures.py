# @PydevCodeAnalysisIgnore
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Textures - Texturas y funciones analizadoras para Hero of Antair
# Pablo Pizarro, 2014-2015

# Importación de librerias
from lib import *
from texture_analysis import *
from texture_items import *
from texture_world import *


class hoaTextures:  # Clase principal de las texturas

    # Función constructora, unica del juego donde se cargan las texturas
    def __init__(self, lang=["Cargando textura '%.gif' ...", "ok"]):
        self.lang = lang
        self.images = {

            # links de escape--
            None: None, \
            "None": None, \
            "_0": None, \
            "_1": None, \
            "_16": None, \
            "_32": None, \

            # Gui #interfaz de usuario
            "actualizacion": DATA_ICONS + "actualizacion.ico", \
            "alert_icon": DATA_ICONS + "alert.ico", \
            "arrow_left": PhotoImage(file=DATA_IMAGES_GUI + "arrow_left.gif"), \
            "arrow_right": PhotoImage(file=DATA_IMAGES_GUI + "arrow_right.gif"), \
            "background": PhotoImage(file=DATA_IMAGES_GUI + "background.gif"), \
            "configuration_icon": DATA_ICONS + "configuration.ico", \
            "console_icon": DATA_ICONS + "console.ico", \
            "door_in": DATA_ICONS + "door_in.ico", \
            "error_icon": DATA_ICONS + "error_icon.ico", \
            "group": DATA_ICONS + "group.ico", \
            "icon": DATA_ICONS + "hoa.ico", \
            "iconmuerte": DATA_ICONS + "iconmuerte.ico", \
            "new_user_icon": DATA_ICONS + "new_user.ico", \
            "no_lw": PhotoImage(file=DATA_IMAGES_ITEMS + "no_lw.gif"), \
            "no_rw": PhotoImage(file=DATA_IMAGES_ITEMS + "no_rw.gif"), \
            "no_casco": PhotoImage(file=DATA_IMAGES_ITEMS + "no_casco.gif"), \
            "no_botas": PhotoImage(file=DATA_IMAGES_ITEMS + "no_botas.gif"), \
            "no_pantalon": PhotoImage(file=DATA_IMAGES_ITEMS + "no_pantalon.gif"), \
            "no_chaleco": PhotoImage(file=DATA_IMAGES_ITEMS + "no_chaleco.gif"), \
            "quest_list": DATA_ICONS + "quest_list.ico", \
            "loading0": PhotoImage(file=DATA_IMAGES_GUI + "loading0.gif"), \
            "loading1": PhotoImage(file=DATA_IMAGES_GUI + "loading1.gif"), \
            "loading2": PhotoImage(file=DATA_IMAGES_GUI + "loading2.gif"), \
            "loading3": PhotoImage(file=DATA_IMAGES_GUI + "loading3.gif"), \
            "loading4": PhotoImage(file=DATA_IMAGES_GUI + "loading4.gif"), \
            "loading5": PhotoImage(file=DATA_IMAGES_GUI + "loading5.gif"), \
            "save_icon": DATA_ICONS + "save.ico", \
            "server_disconnect": DATA_ICONS + "server_disconnect.ico", \
            "server_add": DATA_ICONS + "server_add.ico", \
            "server_error": DATA_ICONS + "server_error.ico", \
            "server_icon": DATA_ICONS + "server_connect.ico", \
            "sound_icon": DATA_ICONS + "sound_add.ico", \
            "statics": DATA_ICONS + "statics.ico", \
            "text_icon": DATA_ICONS + "text_icon.ico", \
            "user_icon": DATA_ICONS + "user.ico", \
            "vacio_16": PhotoImage(data="R0lGODlhEAAQAIAAAP///wAAACH5BAEAAAEALAAAAAAQABAAAAIOjI+py+0Po5y02ouzPgUAOw=="), \
            "vacio_32": PhotoImage(file=DATA_IMAGES_ITEMS + "vacio_32.gif"), \

            # Efectos
            "ambient_effect1_0": PhotoImage(file=DATA_IMAGES_EFFECTS + "ambient_effect1_0.gif"), \
            "ambient_effect1_1": PhotoImage(file=DATA_IMAGES_EFFECTS + "ambient_effect1_1.gif"), \
            "ambient_effect2_0": PhotoImage(file=DATA_IMAGES_EFFECTS + "ambient_effect2_0.gif"), \
            "ambient_effect2_1": PhotoImage(file=DATA_IMAGES_EFFECTS + "ambient_effect2_1.gif"), \
            "ambient_effect3_0": PhotoImage(file=DATA_IMAGES_EFFECTS + "ambient_effect3_0.gif"), \
            "ambient_effect3_1": PhotoImage(file=DATA_IMAGES_EFFECTS + "ambient_effect3_1.gif"), \
            "ambient_effect4_0": PhotoImage(file=DATA_IMAGES_EFFECTS + "ambient_effect4_0.gif"), \
            "ambient_effect4_1": PhotoImage(file=DATA_IMAGES_EFFECTS + "ambient_effect4_1.gif"), \
            "ambient_effect5_0": PhotoImage(file=DATA_IMAGES_EFFECTS + "ambient_effect5_0.gif"), \
            "ambient_effect5_1": PhotoImage(file=DATA_IMAGES_EFFECTS + "ambient_effect5_1.gif"), \
            "life1": PhotoImage(file=DATA_IMAGES_EFFECTS + "life1.gif"), \
            "life2": PhotoImage(file=DATA_IMAGES_EFFECTS + "life2.gif"), \
            "life3": PhotoImage(file=DATA_IMAGES_EFFECTS + "life3.gif"), \
            "life4": PhotoImage(file=DATA_IMAGES_EFFECTS + "life4.gif"), \
            "life5": PhotoImage(file=DATA_IMAGES_EFFECTS + "life5.gif"), \
            "life6": PhotoImage(file=DATA_IMAGES_EFFECTS + "life6.gif"), \
            "life7": PhotoImage(file=DATA_IMAGES_EFFECTS + "life7.gif"), \
            "life8": PhotoImage(file=DATA_IMAGES_EFFECTS + "life8.gif"), \
            "life9": PhotoImage(file=DATA_IMAGES_EFFECTS + "life9.gif"), \
            "life10": PhotoImage(file=DATA_IMAGES_EFFECTS + "life10.gif"), \
            "sangre1_0": PhotoImage(file=DATA_IMAGES_EFFECTS + "sangre1_0.gif"), \
            "sangre1_1": PhotoImage(file=DATA_IMAGES_EFFECTS + "sangre1_1.gif"), \
            "sangre2_0": PhotoImage(file=DATA_IMAGES_EFFECTS + "sangre2_0.gif"), \
            "sangre2_1": PhotoImage(file=DATA_IMAGES_EFFECTS + "sangre2_1.gif"), \
            "sangre3_0": PhotoImage(file=DATA_IMAGES_EFFECTS + "sangre3_0.gif"), \
            "sangre3_1": PhotoImage(file=DATA_IMAGES_EFFECTS + "sangre3_1.gif"), \
            "sangre4_0": PhotoImage(file=DATA_IMAGES_EFFECTS + "sangre4_0.gif"), \
            "sangre4_1": PhotoImage(file=DATA_IMAGES_EFFECTS + "sangre4_1.gif"), \
            "sangre5_0": PhotoImage(file=DATA_IMAGES_EFFECTS + "sangre5_0.gif"), \
            "sangre5_1": PhotoImage(file=DATA_IMAGES_EFFECTS + "sangre5_1.gif"), \

            # Terreno
            "black": Image.open(DATA_IMAGES_TERRAIN + "black.gif"), \
            "dirt1_0": Image.open(DATA_IMAGES_TERRAIN + "dirt1_0.gif"), \
            "dirt1_1": Image.open(DATA_IMAGES_TERRAIN + "dirt1_1.gif"), \
            "dirt2_0": Image.open(DATA_IMAGES_TERRAIN + "dirt2_0.gif"), \
            "dirt2_1": Image.open(DATA_IMAGES_TERRAIN + "dirt2_1.gif"), \
            "dirt3_0": Image.open(DATA_IMAGES_TERRAIN + "dirt3_0.gif"), \
            "dirt3_1": Image.open(DATA_IMAGES_TERRAIN + "dirt3_1.gif"), \
            "dirt4_0": Image.open(DATA_IMAGES_TERRAIN + "dirt4_0.gif"), \
            "dirt4_1": Image.open(DATA_IMAGES_TERRAIN + "dirt4_1.gif"), \
            "dirt5_0": Image.open(DATA_IMAGES_TERRAIN + "dirt5_0.gif"), \
            "dirt5_1": Image.open(DATA_IMAGES_TERRAIN + "dirt5_1.gif"), \
            "dirt6_0": Image.open(DATA_IMAGES_TERRAIN + "dirt6_0.gif"), \
            "dirt6_1": Image.open(DATA_IMAGES_TERRAIN + "dirt6_1.gif"), \
            "dirt7_0": Image.open(DATA_IMAGES_TERRAIN + "dirt7_0.gif"), \
            "dirt7_1": Image.open(DATA_IMAGES_TERRAIN + "dirt7_1.gif"), \
            "dirt8_0": Image.open(DATA_IMAGES_TERRAIN + "dirt8_0.gif"), \
            "dirt8_1": Image.open(DATA_IMAGES_TERRAIN + "dirt8_1.gif"), \
            "dirt9_0": Image.open(DATA_IMAGES_TERRAIN + "dirt9_0.gif"), \
            "dirt9_1": Image.open(DATA_IMAGES_TERRAIN + "dirt9_1.gif"), \
            "dirt10_0": Image.open(DATA_IMAGES_TERRAIN + "dirt10_0.gif"), \
            "dirt10_1": Image.open(DATA_IMAGES_TERRAIN + "dirt10_1.gif"), \
            "floor1_0": Image.open(DATA_IMAGES_TERRAIN + "floor1_0.gif"), \
            "floor1_1": Image.open(DATA_IMAGES_TERRAIN + "floor1_1.gif"), \
            "floor2_0": Image.open(DATA_IMAGES_TERRAIN + "floor2_0.gif"), \
            "floor2_1": Image.open(DATA_IMAGES_TERRAIN + "floor2_1.gif"), \
            "floor3_0": Image.open(DATA_IMAGES_TERRAIN + "floor3_0.gif"), \
            "floor3_1": Image.open(DATA_IMAGES_TERRAIN + "floor3_1.gif"), \
            "floor4_0": Image.open(DATA_IMAGES_TERRAIN + "floor4_0.gif"), \
            "floor4_1": Image.open(DATA_IMAGES_TERRAIN + "floor4_1.gif"), \
            "floor5_0": Image.open(DATA_IMAGES_TERRAIN + "floor5_0.gif"), \
            "floor5_1": Image.open(DATA_IMAGES_TERRAIN + "floor5_1.gif"), \
            "floor6_0": Image.open(DATA_IMAGES_TERRAIN + "floor6_0.gif"), \
            "floor6_1": Image.open(DATA_IMAGES_TERRAIN + "floor6_1.gif"), \
            "floor7_0": Image.open(DATA_IMAGES_TERRAIN + "floor7_0.gif"), \
            "floor7_1": Image.open(DATA_IMAGES_TERRAIN + "floor7_1.gif"), \
            "floor8_0": Image.open(DATA_IMAGES_TERRAIN + "floor8_0.gif"), \
            "floor8_1": Image.open(DATA_IMAGES_TERRAIN + "floor8_1.gif"), \
            "floor9_0": Image.open(DATA_IMAGES_TERRAIN + "floor9_0.gif"), \
            "floor9_1": Image.open(DATA_IMAGES_TERRAIN + "floor9_1.gif"), \
            "floor10_0": Image.open(DATA_IMAGES_TERRAIN + "floor10_0.gif"), \
            "floor10_1": Image.open(DATA_IMAGES_TERRAIN + "floor10_1.gif"), \
            "floor11_0": Image.open(DATA_IMAGES_TERRAIN + "floor11_0.gif"), \
            "floor11_1": Image.open(DATA_IMAGES_TERRAIN + "floor11_1.gif"), \
            "grava1_0": Image.open(DATA_IMAGES_TERRAIN + "grava1_0.gif"), \
            "grava1_1": Image.open(DATA_IMAGES_TERRAIN + "grava1_1.gif"), \
            "grava2_0": Image.open(DATA_IMAGES_TERRAIN + "grava2_0.gif"), \
            "grava2_1": Image.open(DATA_IMAGES_TERRAIN + "grava2_1.gif"), \
            "grava3_0": Image.open(DATA_IMAGES_TERRAIN + "grava3_0.gif"), \
            "grava3_1": Image.open(DATA_IMAGES_TERRAIN + "grava3_1.gif"), \
            "grass1_0": Image.open(DATA_IMAGES_TERRAIN + "grass1_0.gif"), \
            "grass1_1": Image.open(DATA_IMAGES_TERRAIN + "grass1_1.gif"), \
            "grass2_0": Image.open(DATA_IMAGES_TERRAIN + "grass2_0.gif"), \
            "grass2_1": Image.open(DATA_IMAGES_TERRAIN + "grass2_1.gif"), \
            "grass3_0": Image.open(DATA_IMAGES_TERRAIN + "grass3_0.gif"), \
            "grass3_1": Image.open(DATA_IMAGES_TERRAIN + "grass3_1.gif"), \
            "grass4_0": Image.open(DATA_IMAGES_TERRAIN + "grass4_0.gif"), \
            "grass4_1": Image.open(DATA_IMAGES_TERRAIN + "grass4_1.gif"), \
            "grass5_0": Image.open(DATA_IMAGES_TERRAIN + "grass5_0.gif"), \
            "grass5_1": Image.open(DATA_IMAGES_TERRAIN + "grass5_1.gif"), \
            "grass6_0": Image.open(DATA_IMAGES_TERRAIN + "grass6_0.gif"), \
            "grass6_1": Image.open(DATA_IMAGES_TERRAIN + "grass6_1.gif"), \
            "grass7_0": Image.open(DATA_IMAGES_TERRAIN + "grass7_0.gif"), \
            "grass7_1": Image.open(DATA_IMAGES_TERRAIN + "grass7_1.gif"), \
            "grass8_0": Image.open(DATA_IMAGES_TERRAIN + "grass8_0.gif"), \
            "grass8_1": Image.open(DATA_IMAGES_TERRAIN + "grass8_1.gif"), \
            "grass9_0": Image.open(DATA_IMAGES_TERRAIN + "grass9_0.gif"), \
            "grass9_1": Image.open(DATA_IMAGES_TERRAIN + "grass9_1.gif"), \
            "ice1_0": Image.open(DATA_IMAGES_TERRAIN + "ice1_0.gif"), \
            "ice1_1": Image.open(DATA_IMAGES_TERRAIN + "ice1_1.gif"), \
            "ice2_0": Image.open(DATA_IMAGES_TERRAIN + "ice2_0.gif"), \
            "ice2_1": Image.open(DATA_IMAGES_TERRAIN + "ice2_1.gif"), \
            "ice3_0": Image.open(DATA_IMAGES_TERRAIN + "ice3_0.gif"), \
            "ice3_1": Image.open(DATA_IMAGES_TERRAIN + "ice3_1.gif"), \
            "nether1_0": Image.open(DATA_IMAGES_TERRAIN + "nether1_0.gif"), \
            "nether1_1": Image.open(DATA_IMAGES_TERRAIN + "nether1_1.gif"), \
            "nether2_0": Image.open(DATA_IMAGES_TERRAIN + "nether2_0.gif"), \
            "nether2_1": Image.open(DATA_IMAGES_TERRAIN + "nether2_1.gif"), \
            "nether3_0": Image.open(DATA_IMAGES_TERRAIN + "nether3_0.gif"), \
            "nether3_1": Image.open(DATA_IMAGES_TERRAIN + "nether3_1.gif"), \
            "nether4_0": Image.open(DATA_IMAGES_TERRAIN + "nether4_0.gif"), \
            "nether4_1": Image.open(DATA_IMAGES_TERRAIN + "nether4_1.gif"), \
            "nether5_0": Image.open(DATA_IMAGES_TERRAIN + "nether5_0.gif"), \
            "nether5_1": Image.open(DATA_IMAGES_TERRAIN + "nether5_1.gif"), \
            "ladrillo1_0": Image.open(DATA_IMAGES_TERRAIN + "ladrillo1_0.gif"), \
            "ladrillo1_1": Image.open(DATA_IMAGES_TERRAIN + "ladrillo1_1.gif"), \
            "ladrillo2_0": Image.open(DATA_IMAGES_TERRAIN + "ladrillo2_0.gif"), \
            "ladrillo2_1": Image.open(DATA_IMAGES_TERRAIN + "ladrillo2_1.gif"), \
            "ladrillo3_0": Image.open(DATA_IMAGES_TERRAIN + "ladrillo3_0.gif"), \
            "ladrillo3_1": Image.open(DATA_IMAGES_TERRAIN + "ladrillo3_1.gif"), \
            "ladrillo4_0": Image.open(DATA_IMAGES_TERRAIN + "ladrillo4_0.gif"), \
            "ladrillo4_1": Image.open(DATA_IMAGES_TERRAIN + "ladrillo4_1.gif"), \
            "lava1": Image.open(DATA_IMAGES_TERRAIN + "lava1.gif"), \
            "lava2": Image.open(DATA_IMAGES_TERRAIN + "lava2.gif"), \
            "lava3": Image.open(DATA_IMAGES_TERRAIN + "lava3.gif"), \
            "pantano1_0": Image.open(DATA_IMAGES_TERRAIN + "pantano1_0.gif"), \
            "pantano1_1": Image.open(DATA_IMAGES_TERRAIN + "pantano1_1.gif"), \
            "pantano2_0": Image.open(DATA_IMAGES_TERRAIN + "pantano2_0.gif"), \
            "pantano2_1": Image.open(DATA_IMAGES_TERRAIN + "pantano2_1.gif"), \
            "pavimento1_0": Image.open(DATA_IMAGES_TERRAIN + "pavimento1_0.gif"), \
            "pavimento1_1": Image.open(DATA_IMAGES_TERRAIN + "pavimento1_1.gif"), \
            "pavimento2_0": Image.open(DATA_IMAGES_TERRAIN + "pavimento2_0.gif"), \
            "pavimento2_1": Image.open(DATA_IMAGES_TERRAIN + "pavimento2_1.gif"), \
            "pavimento3_0": Image.open(DATA_IMAGES_TERRAIN + "pavimento3_0.gif"), \
            "pavimento3_1": Image.open(DATA_IMAGES_TERRAIN + "pavimento3_1.gif"), \
            "pavimento4_0": Image.open(DATA_IMAGES_TERRAIN + "pavimento4_0.gif"), \
            "pavimento4_1": Image.open(DATA_IMAGES_TERRAIN + "pavimento4_1.gif"), \
            "pavimento5_0": Image.open(DATA_IMAGES_TERRAIN + "pavimento5_0.gif"), \
            "pavimento5_1": Image.open(DATA_IMAGES_TERRAIN + "pavimento5_1.gif"), \
            "pavimento6_0": Image.open(DATA_IMAGES_TERRAIN + "pavimento6_0.gif"), \
            "pavimento6_1": Image.open(DATA_IMAGES_TERRAIN + "pavimento6_1.gif"), \
            "pavimento7_0": Image.open(DATA_IMAGES_TERRAIN + "pavimento7_0.gif"), \
            "pavimento7_1": Image.open(DATA_IMAGES_TERRAIN + "pavimento7_1.gif"), \
            "pavimento8_0": Image.open(DATA_IMAGES_TERRAIN + "pavimento8_0.gif"), \
            "pavimento8_1": Image.open(DATA_IMAGES_TERRAIN + "pavimento8_1.gif"), \
            "pavimento9_0": Image.open(DATA_IMAGES_TERRAIN + "pavimento9_0.gif"), \
            "pavimento9_1": Image.open(DATA_IMAGES_TERRAIN + "pavimento9_1.gif"), \
            "pavimento10_0": Image.open(DATA_IMAGES_TERRAIN + "pavimento10_0.gif"), \
            "pavimento10_1": Image.open(DATA_IMAGES_TERRAIN + "pavimento10_1.gif"), \
            "pavimento11_0": Image.open(DATA_IMAGES_TERRAIN + "pavimento11_0.gif"), \
            "pavimento11_1": Image.open(DATA_IMAGES_TERRAIN + "pavimento11_1.gif"), \
            "pisomadera1_0": Image.open(DATA_IMAGES_TERRAIN + "pisoMadera1_0.gif"), \
            "pisomadera1_1": Image.open(DATA_IMAGES_TERRAIN + "pisoMadera1_1.gif"), \
            "pisomadera2_0": Image.open(DATA_IMAGES_TERRAIN + "pisoMadera2_0.gif"), \
            "pisomadera2_1": Image.open(DATA_IMAGES_TERRAIN + "pisoMadera2_1.gif"), \
            "pisomadera3_0": Image.open(DATA_IMAGES_TERRAIN + "pisoMadera3_0.gif"), \
            "pisomadera3_1": Image.open(DATA_IMAGES_TERRAIN + "pisoMadera3_1.gif"), \
            "pisomadera4_0": Image.open(DATA_IMAGES_TERRAIN + "pisoMadera4_0.gif"), \
            "pisomadera4_1": Image.open(DATA_IMAGES_TERRAIN + "pisoMadera4_1.gif"), \
            "pisomadera5_0": Image.open(DATA_IMAGES_TERRAIN + "pisoMadera5_0.gif"), \
            "pisomadera5_1": Image.open(DATA_IMAGES_TERRAIN + "pisoMadera5_1.gif"), \
            "pisomadera6_0": Image.open(DATA_IMAGES_TERRAIN + "pisoMadera6_0.gif"), \
            "pisomadera6_1": Image.open(DATA_IMAGES_TERRAIN + "pisoMadera6_1.gif"), \
            "sand1_0": Image.open(DATA_IMAGES_TERRAIN + "sand1_0.gif"), \
            "sand1_1": Image.open(DATA_IMAGES_TERRAIN + "sand1_1.gif"), \
            "sand2_0": Image.open(DATA_IMAGES_TERRAIN + "sand2_0.gif"), \
            "sand2_1": Image.open(DATA_IMAGES_TERRAIN + "sand2_1.gif"), \
            "sand3_0": Image.open(DATA_IMAGES_TERRAIN + "sand3_0.gif"), \
            "sand3_1": Image.open(DATA_IMAGES_TERRAIN + "sand3_1.gif"), \
            "sand4_0": Image.open(DATA_IMAGES_TERRAIN + "sand4_0.gif"), \
            "sand4_1": Image.open(DATA_IMAGES_TERRAIN + "sand4_1.gif"), \
            "sand5_0": Image.open(DATA_IMAGES_TERRAIN + "sand5_0.gif"), \
            "sand5_1": Image.open(DATA_IMAGES_TERRAIN + "sand5_1.gif"), \
            "water1_0": Image.open(DATA_IMAGES_TERRAIN + "water1_0.gif"), \
            "water1_1": Image.open(DATA_IMAGES_TERRAIN + "water1_1.gif"), \
            "water2_0": Image.open(DATA_IMAGES_TERRAIN + "water2_0.gif"), \
            "water2_1": Image.open(DATA_IMAGES_TERRAIN + "water2_1.gif"), \
            "water3_0": Image.open(DATA_IMAGES_TERRAIN + "water3_0.gif"), \
            "water3_1": Image.open(DATA_IMAGES_TERRAIN + "water3_1.gif"), \
            "water4_0": Image.open(DATA_IMAGES_TERRAIN + "water4_0.gif"), \
            "water4_1": Image.open(DATA_IMAGES_TERRAIN + "water4_1.gif"), \
            "water5_0": Image.open(DATA_IMAGES_TERRAIN + "water5_0.gif"), \
            "water5_1": Image.open(DATA_IMAGES_TERRAIN + "water5_1.gif"), \
            "water6_0": Image.open(DATA_IMAGES_TERRAIN + "water6_0.gif"), \
            "water6_1": Image.open(DATA_IMAGES_TERRAIN + "water6_1.gif"), \
            "water7_0": Image.open(DATA_IMAGES_TERRAIN + "water7_0.gif"), \
            "water7_1": Image.open(DATA_IMAGES_TERRAIN + "water7_1.gif")}

    # Función que llama a las imágenes, si existe se retorna el objeto
    # PhotoImage, si no existe se crea y se agrega
    def image(self, image):
        try:
            return self.images[image]
        except:
            print str(self.lang[0]).replace("%", image),
            try:
                # Se cargan las imágenes desde el mundo
                self.images[image] = PhotoImage(file=IMAGES[image])
            except:
                self.images[image] = PhotoImage(
                    file=IMAGES_ITEMS[image])  # O desde los items
            print self.lang[1]
            return self.images[image]

    def getLinkImage(self, image):  # Función que obtiene el linkd e una imagen
        try:
            return IMAGES[image]
        except:
            print self.lang[1]
        return "None"


# Función que arrastra una imagen desde su posición inicial hasta (c,d)
def arrastrarImagen(image, canvas, c, d):
    try:
        (a, b) = canvas.coords(image)  # obtengo la pos anterior
        a = int(a)
        b = int(b)
        while True:
            if a < c:
                a += PIXEL_MOVE
                x = PIXEL_MOVE
            elif a > c:
                a -= PIXEL_MOVE
                x = -PIXEL_MOVE
            else:
                x = 0
            if b < d:
                b += PIXEL_MOVE
                y = PIXEL_MOVE
            elif b > d:
                b -= PIXEL_MOVE
                y = -PIXEL_MOVE
            else:
                y = 0
            canvas.move(image, x, y)  # muevo a la imagen
            canvas.update()
            if x == 0 and y == 0:
                break
    except:
        pass


# Función que arrastra una imagen desde su posición inicial hasta (c,d)
def arrastrarImagenPx(image, canvas, c, d, pixels):
    try:
        (a, b) = canvas.coords(image)  # obtengo la pos anterior
        a = int(a)
        b = int(b)
        while True:
            if a < c:
                a += pixels
                x = pixels
            elif a > c:
                a -= pixels
                x = -pixels
            else:
                x = 0
            if b < d:
                b += pixels
                y = pixels
            elif b > d:
                b -= pixels
                y = -pixels
            else:
                y = 0
            canvas.move(image, x, y)  # muevo a la imagen
            canvas.update()
            if x == 0 and y == 0:
                break
    except:
        pass


def dibujarImagen(image, canvas, x, y):  # Dibuja una imagen en el canvas
    canvas.move(image, x, y)  # muevo a la imagen
    canvas.update()


def moveWay(image_tag, canvas, way):  # Traza una ruta de movimientos
    for pos in way:  # Recorre las posiciones
        arrastrarImagen(image_tag, canvas, pos[0], pos[1])
        time.sleep(0.05)


# Obtiene el despazamiento de las imágenes cuando no son de tamaño 32x32
def textureMover(image, tipo):
    if image.width() == 32:
        if tipo == EJE_X:
            return 0
        elif tipo == EJE_Y:
            return 0
        else:
            raise Exception("Tipo no valido")
    elif image.width() == 64:
        if tipo == EJE_X:
            return -16
        elif tipo == EJE_Y:
            return -16
        else:
            raise Exception("Tipo no valido")
    elif image.width() == 128:
        if tipo == EJE_X:
            return 0
        elif tipo == EJE_Y:
            return -18
        else:
            raise Exception("Tipo no valido")