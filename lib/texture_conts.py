#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Constantes usadas por las texturas

# TEXTURE CONTS
# Autor: PABLO PIZARRO @ ppizarro
# Fecha: 2013-2015
# Licencia: GPLv2

# Importación de librerias
import os

# Constantes del programa
_libdir = "lib"
ACTUAL_FOLDER = str(
    os.path.abspath(os.path.dirname(__file__))).replace("\\", "/").replace(_libdir, "") + "/"
# prefijos de armas arrojadizas de flechas
ARROW_WEAPONS_PREFIX = ["arco", "ballesta"]
AVAIABLE_ACTOR_TEXTURES = ["actor1", "actor2", "actor3", "actor4", "actor7", "actor8", "actor9", "actor10", "actor11",
                           "actor12", "actor13", "actor14", "actor15", "actor16", "actor17", "actor18", "actor19",
                           "actor20",
                           "actor21", "actor22", "actor23", "actor24", "actor25", "actor26", "actor27", "actor28",
                           "actor29",
                           "actor30", "actor31", "actor32", "actor33", "actor34", "actor35", "actor36", "actor37",
                           "actor38",
                           "actor39", "actor40", "actor41", "actor42", "actor43", "actor44", "actor45", "actor46",
                           "actor47",
                           "actor48", "actor49", "actor50", "actor51", "actor52", "actor53", "actor54", "actor55",
                           "actor56",
                           "actor57", "actor58", "actor59", "actor60", "actor61", "actor62", "actor63", "actor64",
                           "actor65",
                           "actor66", "actor67", "actor68", "actor69", "actor70", "actor71", "actor72", "actor73",
                           "actor74",
                           "actor75", "actor76", "actor77", "actor78", "actor79", "actor80", "actor81", "actor82",
                           "actor83",
                           "actor84", "actor85", "actor86", "actor87", "actor88", "actor89", "actor90", "actor91",
                           "actor92",
                           "actor93", "actor94", "actor95", "actor96", "actor97", "actor98", "actor99", "actor100",
                           "actor101",
                           "actor102", "actor103", "actor104", "actor105", "actor106", "actor107", "actor108",
                           "actor109", "actor110",
                           "actor111", "actor112", "actor113", "actor114", "actor115", "actor116", "actor117",
                           "actor118", "actor119",
                           "actor120", "actor121", "actor122", "actor123", "actor124", "actor125", "actor126",
                           "actor127", "actor128",
                           "actor129", "actor130", "actor131", "actor132", "actor133", "actor134", "actor135",
                           "actor136"]
BUILD_LINKS_KEY = ["castle_0", "castle2_0", "castle3_0", "cabana_0", "house_0",
                   "feudo_0", "building1_0", "building2_0", "building3_0", "building4_0",
                   "building5_0", "building6_0", "building7_0", "building8_0", "building9_0",
                   "building10_0", "building11_0", "building12_0", "building15_0", "building16_0",
                   "building17_0", "building18_0", "building20_0", "building21_0", "building22_0",
                   "building23_0", "building24_0", "building25_0", "building26_0", "building28_0",
                   "building29_0", "building30_0", "building31_0", "building32_0", "building33_0",
                   "building34_0", "building35_0", "building36_0", "building37_0", "building38_0",
                   "building39_0", "building40_0", "building41_0", "building42_0", "building43_0",
                   "building44_0", "building45_0", "building46_0", "building47_0", "building48_0",
                   "building49_0", "building50_0", "building51_0", "building54_0", "building55_0",
                   "building56_0", "building57_0", "building58_0", "building59_0", "building61_0",
                   "building62_0", "building63_0", "building64_0", "building65_0", "building66_0",
                   "building67_0", "building68_0", "building70_0", "building71_0", "building72_0",
                   "building73_0", "building74_0", "building75_0", "building81_0", "building82_0",
                   "building83_0", "building84_0", "building85_0", "building86_0", "building87_0",
                   "building88_0", "building89_0", "building90_0", "building92_0", "building93_0",
                   "building94_0", "building95_0", "building96_0", "building97_0", "building98_0",
                   "building101_0", "building102_0", "building103_0"]
BUILD_LINKS_NOKEY = ["volcan", "building13_0", "building14_0", "building19_0", "building27_0",
                     "building52_0", "building53_0", "building60_0", "building69_0", "building76_0",
                     "building77_0", "building78_0", "building79_0", "building80_0", "building91_0",
                     "building99_0", "building100_0"]
BUILD_TORCHES = ["antorcha", "antorcha2", "antorcha3", "antorcha4", "antorcha5",
                 "antorcha6", "antorcha7", "antorcha8", "antorcha9", "antorcha10",
                 "antorcha11", "antorcha12", "antorcha13", "antorcha14", "antorcha15",
                 "antorcha16", "antorcha17", "antorcha18", "antorcha19", "antorcha20",
                 "antorcha21", "antorcha22", "antorcha23", "ambient_effect2_0"]
BUILD_TORCHES_ID = ["407", "408", "411", "412", "413", "414", "415", "416", "417", "418", "419",
                    "420", "421", "422", "423", "424", "425", "426", "427", "428", "429", "430",
                    "431", "432", "961"]
DATA_FOLDER = ACTUAL_FOLDER + "data/"
DATA_ICONS = DATA_FOLDER + "icons/"
DATA_ICONS_ITEMS = DATA_ICONS + "items/"
DATA_ICONS_POWERS = DATA_ICONS + "powers/"
DATA_IMAGES = DATA_FOLDER + "images/"
DATA_IMAGES_ACTORS = DATA_IMAGES + "actor/"
DATA_IMAGES_AMBIANCE = DATA_IMAGES + "ambiance/"
DATA_IMAGES_AMBIANCE_BIG = DATA_IMAGES_AMBIANCE + "big/"
DATA_IMAGES_BUILDING = DATA_IMAGES + "buildings/"
DATA_IMAGES_BUILDING_BIG = DATA_IMAGES_BUILDING + "big/"
DATA_IMAGES_CONSTRUCTION = DATA_IMAGES + "construction/"
DATA_IMAGES_CONSTRUCTION_BIG = DATA_IMAGES_CONSTRUCTION + "big/"
DATA_IMAGES_EDITOR = DATA_IMAGES + "editor/"
DATA_IMAGES_EFFECTS = DATA_IMAGES + "effects/"
DATA_IMAGES_GUI = DATA_IMAGES + "gui/"
DATA_IMAGES_INTERIOR = DATA_IMAGES + "interior/"
DATA_IMAGES_INTERIOR_BIG = DATA_IMAGES_INTERIOR + "big/"
DATA_IMAGES_ITEMS = DATA_IMAGES + "items/"
DATA_IMAGES_POWERS = DATA_IMAGES + "powers/"
DATA_IMAGES_TERRAIN = DATA_IMAGES + "terrain/"
DATA_IMAGES_VEHICLES = DATA_IMAGES + "vehicles/"
EFFECT_BLOOD_DAY = ["sangre1_0", "sangre2_0", "sangre3_0",
                    "sangre4_0", "sangre5_0"]  # texturas de sangre de dia
EFFECT_BLOOD_NIGHT = ["sangre1_1", "sangre2_1", "sangre3_1",
                      "sangre4_1", "sangre5_1"]  # exturas de sangre de noche
EJE_X = "x"
EJE_Y = "y"
EVENT_IMAGE_EDITOR = ["text", "minushp", "minusmana", "plushp", "pass", "nopass", "plusmana", "playerpos",
                      "object", "teleport", "sound", "mute", "longtext", "autosave", "suddendeath",
                      "nopassalert"]
PIXEL_MOVE = 0.5  # pixeles movidos por fracción de segundo
LOWER_TEXTURES_FIRSy = ["building"]  # Texturas basales primarias
LOWER_TEXTURES = ["ambiance_grass", "sangre", "cabana", "castle", "church", "feudo",
                  "house", "volcan", "big_carpet", "carpet", "interior20", "interior48", "ambiance_other_27",
                  "ambiance_other_59", "flower35", "plant1", "plant2", "plant5", "plant10", "plant22",
                  "shell", "plant1", "tronco2"]
TEXTURE_EMPTY = "R0lGODlhAQABAJEAAAAAAP///////wAAACH5BAEAAAIALAAAAAABAAEAAAICVAEAOw=="
TEXTURE_LAVA = [150, 151, 152]  # texturas de lava
TEXTURE_OBSTACLES = ["ambiance_other27", "ambiance_other32", "ambiance_other44", "ambiance_other59", "ambiance_other60",
                     "hongo7", "hongo4", "hongo6", "hongo11", "hongo19", "rock1", "rock2", "tronco1"]
# texturas de agua
TEXTURE_WATER = [109, 110, 111, 124, 125, 131, 132, 194, 195]

# MAPEO DE ELEMENTOS LOGICOS POR ID
ITEM_TYPE_CROSS = [452, 1219, 1222, 1225]
#    -#-
#    #x#
#    -#-

# ITEM_TYPE_CROSS
ITEM_TYPE_FULL = [437, 447, 451, 455, 1234]
# ITEM_TYPE_FULL
#    -#-
#    #x#
#    ###

# ITEM_TYPE_CROSS
ITEM_TYPE_FULL_A = [1210, 1223, 1237, 1238, 1242, 1246]
# ITEM_TYPE_FULL
#    ###
#    #x#
#    ###

ITEM_TYPE_FULL_V = [434, 436, 438, 440, 446, 450, 1226]
# ITEM_TYPE_FULL
#    -#-
#    #x#
#    -##

ITEM_TYPE_MEDIUM = [
    435, 448, 454, 456, 1228, 1229, 1231, 1232, 1233, 1235, 1236, 1241]
# ITEM_TYPE_MEDIUM
#    ---
#    #x#
#    ###

ITEM_TYPE_MEDIUM_A = [1227, 1248]
# ITEM_TYPE_MEDIUM_A
#    ###
#    #x#
#    ---

ITEM_TYPE_MEDIUM_L = [443, 457]
# ITEM_TYPE_MEDIUM_L
#    ---
#    -x#
#    ###

ITEM_TYPE_MEDIUM_R = [433, 444, 453, 1243, 1247]
# ITEM_TYPE_MEDIUM_R
#    ---
#    #x#
#    ##-

ITEM_TYPE_MEDIUM_S = [445, 449, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192, 1193, 1194, 1195,
                      1196, 1197, 1198, 1199, 1200, 1201, 1202, 1203, 1204, 1205, 1206, 1207, 1208,
                      1209, 1220, 1240]
# ITEM_TYPE_MEDIUM_S
#    ---
#    #x#
#    -##

ITEM_TYPE_MEDIUM_T = [1217]
# ITEM_TYPE_MEDIUM_T
#    -##
#    #x#
#    ---

ITEM_TYPE_MEDIUM_U = [1218]
# ITEM_TYPE_MEDIUM_T
#    ###
#    #x#
#    ##-

ITEM_TYPE_MEDIUM_V = [439, 441, 442, 1221, 1239, 1244, 1245]
# ITEM_TYPE_MEDIUM_V
#    -#-
#    #x#
#    ##-

ITEM_TYPE_SMALL = [676, 823, 824, 825, 826, 827, 828, 831, 832,
                   833, 834, 835, 836, 837, 691, 692, 696, 708, 899, 900, 904, 255]
# ITEM_TYPE_SMALL
#    ##-
#    #x-
#    ---

ITEM_TYPE_SMALL_L = [1115]
# ITEM_TYPE_SMALL
#    -#-
#    #x-
#    ---

ITEM_TYPE_SMALL_LINE_DOW = [
    1212, 1213, 1214, 1215, 1216, 1250, 1252, 1253, 1254, 1255, 1256]
# ITEM_TYPE_SMALL_LINE_DOWN
#    ---
#    -x-
#    -#-

ITEM_TYPE_SMALL_LINE_DOWN = [676, 822, 830, 1179, 1130, 1131, 637]
# ITEM_TYPE_SMALL_LINE_DOWN
#    ---
#    #x-
#    ---

ITEM_TYPE_SMALL_LINE_RIGHT = [838]
# ITEM_TYPE_SMALL_LINE_RIGHT
#    -#-
#    -x-
#    ---

ITEM_TYPE_SMALL_LINE_DIAG = [
    1059, 1060, 1061, 1062, 1063, 1064, 1065, 1067, 1068, 1069, 1070]
# ITEM_TYPE_SMALL_LINE_DIAG
#    #--
#    -x-
#    ---

ITEM_TYPE_SMALL_T = [456, 1251]
# ITEM_TYPE_SMALL_T
#    ---
#    -x-
#    ###

ITEM_TYPE_SMALL_Z = [458, 1211, 1249, 1257, 1258]
# ITEM_TYPE_SMALL_T
#    ---
#    #x-
#    -##
