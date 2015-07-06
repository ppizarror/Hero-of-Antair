# -*- coding: utf-8 -*-
# @PydevCodeAnalysisIgnore
# !/usr/bin/env python
# Textures - Constantes y sonidos para Hero of Antair
# Pablo Pizarro, 2014-2015

# Importación de librerías
import os

# Constantes del programa
ACTUAL_FOLDER = str(
    os.path.abspath(os.path.dirname(__file__))).replace("\\", "/") + "/"
AUDIO_VOLUME = 80
DATA_FOLDER = ACTUAL_FOLDER + "data/"
DATA_SOUND = DATA_FOLDER + "sound/"
SOUND_ALERT = DATA_SOUND + "alerts/"
SOUND_AMBIENCE = DATA_SOUND + "ambience/"
SOUND_DOOR = DATA_SOUND + "door/"
SOUND_EFFECT = DATA_SOUND + "effect/"
SOUND_FIGHT = DATA_SOUND + "fight/"
SOUND_FORMAT = ".wav"  # para archivos chicos
SOUND_FORMAT_EXTRA = ".mp3"  # para archivos grandes
SOUND_MOB = DATA_SOUND + "mobs/"
SOUND_WALK = DATA_SOUND + "walk/"
SOUND_WEAPONS = DATA_SOUND + "weapons/"
SONIDO = [
    # INTRO
    [DATA_SOUND + "intro1" + SOUND_FORMAT, \
     DATA_SOUND + "intro2" + SOUND_FORMAT], \
 \
    # ABRIR PUERTA (SIN LLAVE)
    [SOUND_DOOR + "door_open_1" + SOUND_FORMAT, \
     SOUND_DOOR + "door_open_2" + SOUND_FORMAT, \
     SOUND_DOOR + "door_open_3" + SOUND_FORMAT, \
     SOUND_DOOR + "door_open_4" + SOUND_FORMAT, \
     SOUND_DOOR + "door_open_5" + SOUND_FORMAT], \
 \
    # PUERTA BLOQUEADA
    [SOUND_DOOR + "door_closed_1" + SOUND_FORMAT, \
     SOUND_DOOR + "door_closed_2" + SOUND_FORMAT, \
     SOUND_DOOR + "door_closed_3" + SOUND_FORMAT, \
     SOUND_DOOR + "door_closed_4" + SOUND_FORMAT, \
     SOUND_DOOR + "door_closed_5" + SOUND_FORMAT, \
     SOUND_DOOR + "door_closed_6" + SOUND_FORMAT], \
 \
    # VIENTO ARTICO
    [SOUND_EFFECT + "articwind" + SOUND_FORMAT, \
     SOUND_EFFECT + "articwind2" + SOUND_FORMAT, \
     SOUND_EFFECT + "articwind3" + SOUND_FORMAT, \
     SOUND_EFFECT + "articwind4" + SOUND_FORMAT], \
 \
    # PAJAROS
    [SOUND_EFFECT + "birds_1" + SOUND_FORMAT, \
     SOUND_EFFECT + "birds_2" + SOUND_FORMAT, \
     SOUND_EFFECT + "birds_3" + SOUND_FORMAT], \
 \
    # COIN
    [SOUND_EFFECT + "coin_1" + SOUND_FORMAT, \
     SOUND_EFFECT + "coin_2" + SOUND_FORMAT], \
 \
    # FUEGO
    [SOUND_EFFECT + "fire" + SOUND_FORMAT, \
     SOUND_EFFECT + "fire1" + SOUND_FORMAT, \
     SOUND_EFFECT + "fire2" + SOUND_FORMAT, \
     SOUND_EFFECT + "fire3" + SOUND_FORMAT, \
     SOUND_EFFECT + "fire4" + SOUND_FORMAT, \
     SOUND_EFFECT + "fire5" + SOUND_FORMAT], \
 \
    # LLUVIA
    [SOUND_EFFECT + "rain_1" + SOUND_FORMAT, \
     SOUND_EFFECT + "rain_2" + SOUND_FORMAT, \
     SOUND_EFFECT + "rain_3" + SOUND_FORMAT], \
 \
    # TORMENTA
    [SOUND_EFFECT + "storm_1" + SOUND_FORMAT, \
     SOUND_EFFECT + "storm_2" + SOUND_FORMAT, \
     SOUND_EFFECT + "storm_3" + SOUND_FORMAT, \
     SOUND_EFFECT + "storm_4" + SOUND_FORMAT], \
 \
    # TELETRANSPORTACION
    [SOUND_EFFECT + "teletransportacion_1" + SOUND_FORMAT, \
     SOUND_EFFECT + "teletransportacion_2" + SOUND_FORMAT], \
 \
    # VIENTO
    [SOUND_EFFECT + "wind_1" + SOUND_FORMAT, \
     SOUND_EFFECT + "wind_2" + SOUND_FORMAT, \
     SOUND_EFFECT + "wind_3" + SOUND_FORMAT], \
 \
    # GARRA
    [SOUND_FIGHT + "claw_miss_1" + SOUND_FORMAT, \
     SOUND_FIGHT + "claw_miss_2" + SOUND_FORMAT], \
 \
    # PERRO
    [SOUND_FIGHT + "dog_1" + SOUND_FORMAT, \
     SOUND_FIGHT + "dog_2" + SOUND_FORMAT], \
 \
    # IMPACTO
    [SOUND_FIGHT + "impacto_1" + SOUND_FORMAT, \
     SOUND_FIGHT + "impacto_2" + SOUND_FORMAT, \
     SOUND_FIGHT + "impacto_3" + SOUND_FORMAT, \
     SOUND_FIGHT + "law_bounce" + SOUND_FORMAT], \
 \
    # IMPACTO DE CUCHILLO EN CUERPO
    [SOUND_FIGHT + "knife_hit1" + SOUND_FORMAT, \
     SOUND_FIGHT + "knife_hit2" + SOUND_FORMAT, \
     SOUND_FIGHT + "knife_hit3" + SOUND_FORMAT, \
     SOUND_FIGHT + "knife_hit4" + SOUND_FORMAT, \
     SOUND_FIGHT + "knife_hit5" + SOUND_FORMAT, \
     SOUND_FIGHT + "knife_hit6" + SOUND_FORMAT, \
     SOUND_FIGHT + "knife_hit7" + SOUND_FORMAT, \
     SOUND_FIGHT + "knife_hit8" + SOUND_FORMAT, \
     SOUND_FIGHT + "knife_hit9" + SOUND_FORMAT, \
     SOUND_FIGHT + "knife_hit10" + SOUND_FORMAT, \
     SOUND_FIGHT + "knife_hit11" + SOUND_FORMAT, \
     SOUND_FIGHT + "knife_hit12" + SOUND_FORMAT, \
     SOUND_FIGHT + "knife_hit13" + SOUND_FORMAT, \
     SOUND_FIGHT + "knife_hitwall1" + SOUND_FORMAT], \
 \
    # CUCHILLAZO
    [SOUND_FIGHT + "knife_slash1" + SOUND_FORMAT, \
     SOUND_FIGHT + "knife_slash2" + SOUND_FORMAT, \
     SOUND_FIGHT + "knife_slash3" + SOUND_FORMAT, \
     SOUND_FIGHT + "knife_slash4" + SOUND_FORMAT, \
     SOUND_FIGHT + "knife_slash5" + SOUND_FORMAT, \
     SOUND_WEAPONS + "sword_1" + SOUND_FORMAT, \
     SOUND_WEAPONS + "sword_2" + SOUND_FORMAT, \
     SOUND_WEAPONS + "sword_3" + SOUND_FORMAT, \
     SOUND_WEAPONS + "sword_4" + SOUND_FORMAT], \
 \
    # MAGIA
    [SOUND_FIGHT + "mage_1" + SOUND_FORMAT, \
     SOUND_FIGHT + "mage_2" + SOUND_FORMAT, \
     SOUND_FIGHT + "mage_3" + SOUND_FORMAT], \
 \
    # COMBO
    [SOUND_FIGHT + "punch_1" + SOUND_FORMAT, \
     SOUND_FIGHT + "punch_2" + SOUND_FORMAT], \
 \
    # APLAUSOS
    [DATA_SOUND + "applause" + SOUND_FORMAT_EXTRA], \
 \
    # CREDITOS
    [DATA_SOUND + "credits" + SOUND_FORMAT_EXTRA], \
 \
    # DROP
    [SOUND_EFFECT + "drop_1" + SOUND_FORMAT, \
     SOUND_EFFECT + "drop_2" + SOUND_FORMAT], \
 \
    # POTION
    [SOUND_EFFECT + "potion_1" + SOUND_FORMAT, \
     SOUND_EFFECT + "potion_2" + SOUND_FORMAT, \
     SOUND_EFFECT + "potion_3" + SOUND_FORMAT], \
 \
    # ENEMY OP
    [SOUND_FIGHT + "enemy_op_3" + SOUND_FORMAT, \
     SOUND_FIGHT + "enemy_op_3" + SOUND_FORMAT, \
     SOUND_FIGHT + "enemy_op_3" + SOUND_FORMAT], \
 \
    # CLOTHES
    [SOUND_EFFECT + "clothes1" + SOUND_FORMAT, \
     SOUND_EFFECT + "clothes2" + SOUND_FORMAT], \
 \
    # FLECHAS
    [SOUND_WEAPONS + "arrow_1" + SOUND_FORMAT, \
     SOUND_WEAPONS + "arrow_2" + SOUND_FORMAT, \
     SOUND_WEAPONS + "arrow_3" + SOUND_FORMAT, \
     SOUND_WEAPONS + "arrow_4" + SOUND_FORMAT, \
     SOUND_WEAPONS + "arrow_5" + SOUND_FORMAT, \
     SOUND_WEAPONS + "arrow_6" + SOUND_FORMAT, \
     SOUND_WEAPONS + "arrow_7" + SOUND_FORMAT, \
     SOUND_WEAPONS + "arrow_8" + SOUND_FORMAT, \
     SOUND_WEAPONS + "arrow_9" + SOUND_FORMAT, \
     SOUND_WEAPONS + "arrow_10" + SOUND_FORMAT, \
     SOUND_WEAPONS + "arrow_11" + SOUND_FORMAT, \
     SOUND_WEAPONS + "arrow_12" + SOUND_FORMAT, \
     SOUND_WEAPONS + "arrow_13" + SOUND_FORMAT], \
 \
    # COMER MANZANA
    [SOUND_EFFECT + "apple_eat_1" + SOUND_FORMAT], \
 \
    # OPEN SODA
    [SOUND_EFFECT + "open_soda_1" + SOUND_FORMAT], \
 \
    # TEXT
    [SOUND_EFFECT + "text_1" + SOUND_FORMAT, \
     SOUND_EFFECT + "text_2" + SOUND_FORMAT, \
     SOUND_EFFECT + "text_3" + SOUND_FORMAT, \
     SOUND_EFFECT + "text_4" + SOUND_FORMAT, \
     SOUND_EFFECT + "text_5" + SOUND_FORMAT], \
 \
    # ALERT
    [SOUND_ALERT + "alert1" + SOUND_FORMAT_EXTRA], \
 \
    # GAME OVER
    [SOUND_ALERT + "game_over" + SOUND_FORMAT], \
 \
    # NEW LEVEL
    [SOUND_ALERT + "new_level" + SOUND_FORMAT], \
 \
    # NOTIFICACION
    [SOUND_ALERT + "notificacion" + SOUND_FORMAT, \
     SOUND_ALERT + "notificacion_2" + SOUND_FORMAT], \
 \
    # MONSTER
    [SOUND_FIGHT + "monster1" + SOUND_FORMAT_EXTRA], \
 \
    # AXE
    [SOUND_WEAPONS + "axe_1" + SOUND_FORMAT], \
 \
    # AFILAR ESPADA
    [SOUND_WEAPONS + "sonido_espada_1" + SOUND_FORMAT, \
     SOUND_WEAPONS + "sonido_espada_2" + SOUND_FORMAT, \
     SOUND_WEAPONS + "sonido_espada_3" + SOUND_FORMAT], \
 \
    # BOTAR ESPADA
    [SOUND_WEAPONS + "drop_weapon_1" + SOUND_FORMAT, \
     SOUND_WEAPONS + "drop_weapon_2" + SOUND_FORMAT, \
     SOUND_WEAPONS + "drop_weapon_3" + SOUND_FORMAT], \
 \
    # ABIR PUERTA CON LLAVE
    [SOUND_DOOR + "door_key_1" + SOUND_FORMAT, \
     SOUND_DOOR + "door_key_2" + SOUND_FORMAT], \
 \
    # TROMPETAS
    [SOUND_ALERT + "trumpet_1" + SOUND_FORMAT, \
     SOUND_ALERT + "trumpet_2" + SOUND_FORMAT], \
 \
    # LADDER
    [SOUND_DOOR + "ladder_1" + SOUND_FORMAT, \
     SOUND_DOOR + "ladder_2" + SOUND_FORMAT], \
 \
    # PASS
    [SOUND_EFFECT + "pass" + SOUND_FORMAT], \
 \
    # MAGIA
    [SOUND_FIGHT + "magia_1" + SOUND_FORMAT, \
     SOUND_FIGHT + "magia_2" + SOUND_FORMAT, \
     SOUND_FIGHT + "magia_3" + SOUND_FORMAT, \
     SOUND_FIGHT + "magia_4" + SOUND_FORMAT, \
     SOUND_FIGHT + "magia_5" + SOUND_FORMAT, \
     SOUND_FIGHT + "magia_6" + SOUND_FORMAT, \
     SOUND_FIGHT + "magia_7" + SOUND_FORMAT]
]
