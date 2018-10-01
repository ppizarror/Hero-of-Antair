# coding=utf-8
"""
TEXTURES EDITOR
Texturas usadas por el editor de mapas.

Autor: PABLO PIZARRO @ ppizarror
Fecha: 2013-2015, 2017
Licencia: GPLv2
"""

# Importación de librerias
from Tkinter import PhotoImage
import os
from textures import *

# Constantes
# Actores / Mobs
actores = [
    ["playerpos", 999],
    ["events", "events"],
    ["trash", "delete"],
    ["actor127_0", 1286],
    ["actor106_0", 1265],
    ["actor1_0", 301],
    ["actor72_0", 370],
    ["actor66_0", 364],
    ["actor67_0", 365],
    ["actor43_0", 341],
    ["actor39_0", 337],
    ["actor103_0", 1262],
    ["actor104_0", 1263],
    ["actor94_0", 392],
    ["actor98_0", 396],
    ["actor68_0", 366],
    ["actor113_0", 1272],
    ["actor48_0", 346],
    ["actor69_0", 367],
    ["actor123_0", 1282],
    ["actor124_0", 1283],
    ["actor114_0", 1273],
    ["actor80_0", 378],
    ["actor81_0", 379],
    ["actor90_0", 388],
    ["actor82_0", 380],
    ["actor83_0", 381],
    ["actor7_0", 305],
    ["actor46_0", 344],
    ["actor40_0", 338],
    ["actor8_0", 306],
    ["actor41_0", 339],
    ["actor42_0", 340],
    ["actor73_0", 371],
    ["actor128_0", 1287],
    ["actor11_0", 309],
    ["actor3_0", 303],
    ["actor12_0", 310],
    ["actor20_0", 318],
    ["actor75_0", 373],
    ["actor76_0", 374],
    ["actor77_0", 375],
    ["actor78_0", 376],
    ["actor64_0", 362],
    ["actor54_0", 352],
    ["actor50_0", 348],
    ["actor51_0", 349],
    ["actor13_0", 311],
    ["actor135_0", 1294],
    ["actor84_0", 382],
    ["actor19_0", 317],
    ["actor136_0", 1295],
    ["actor93_0", 391],
    ["actor4_0", 304],
    ["actor10_0", 308],
    ["actor30_0", 328],
    ["actor70_0", 368],
    ["actor24_0", 322],
    ["actor130_0", 1289],
    ["actor14_0", 312],
    ["actor97_0", 395],
    ["actor125_0", 1284],
    ["actor34_0", 332],
    ["actor60_0", 358],
    ["actor129_0", 1288],
    ["actor63_0", 361],
    ["actor105_0", 1264],
    ["actor38_0", 336],
    ["actor59_0", 357],
    ["actor62_0", 360],
    ["actor131_0", 1290],
    ["actor55_0", 353],
    ["actor53_0", 351],
    ["actor61_0", 359],
    ["actor15_0", 313],
    ["actor122_0", 1281],
    ["actor35_0", 333],
    ["actor16_0", 314],
    ["actor36_0", 334],
    ["actor92_0", 390],
    ["actor37_0", 335],
    ["actor17_0", 315],
    ["actor47_0", 345],
    ["actor87_0", 385],
    ["actor88_0", 386],
    ["actor74_0", 372],
    ["actor86_0", 384],
    ["actor56_0", 354],
    ["actor57_0", 355],
    ["actor45_0", 343],
    ["actor49_0", 347],
    ["actor52_0", 350],
    ["actor58_0", 356],
    ["actor65_0", 363],
    ["actor79_0", 377],
    ["actor85_0", 383],
    ["actor18_0", 316],
    ["actor91_0", 389],
    ["actor96_0", 394],
    ["actor101_0", 399],
    ["actor107_0", 1266],
    ["actor2_0", 302],
    ["actor108_0", 1267],
    ["actor109_0", 1268],
    ["actor110_0", 1269],
    ["actor112_0", 1271],
    ["actor9_0", 307],
    ["actor99_0", 397],
    ["actor115_0", 1274],
    ["actor116_0", 1275],
    ["actor117_0", 1276],
    ["actor118_0", 1277],
    ["actor119_0", 1278],
    ["actor120_0", 1279],
    ["actor121_0", 1280],
    ["actor102_0", 1261],
    ["actor133_0", 1292],
    ["actor134_0", 1293],
    ["actor32_0", 330],
    ["actor132_0", 1291],
]
# Edificación
# 0: objeto normal, 1: puerta, 2: edificio, 3: item / objeto usable, 4: evento
bbuilding = [
    ["building59_0", "7-1217", 2],
    ["building60_0", "7-1218", 2],
    ["building63_0", "7-1221", 2],
    ["building64_0", "7-1222", 2],
    ["building65_0", "7-1223", 2],
    ["building67_0", "7-1225", 2],
    ["building68_0", "7-1226", 2],
    ["building70_0", "7-1228", 2],
    ["building71_0", "7-1229", 2],
    ["building73_0", "7-1231", 2],
    ["building74_0", "7-1232", 2],
    ["building75_0", "7-1233", 2],
    ["building81_0", "7-1239", 2],
    ["building82_0", "7-1240", 2],
    ["building83_0", "7-1241", 2],
    ["building84_0", "7-1242", 2],
    ["building85_0", "7-1243", 2],
    ["building87_0", "7-1245", 2],
    ["building88_0", "7-1246", 2],
    ["building89_0", "7-1247", 2],
    ["building90_0", "7-1248", 2],
    ["building28_0", "7-1186", 2],
    ["building29_0", "7-1187", 2],
    ["building30_0", "7-1188", 2],
    ["building31_0", "7-1189", 2],
    ["building32_0", "7-1190", 2],
    ["building33_0", "7-1191", 2],
    ["building34_0", "7-1192", 2],
    ["building35_0", "7-1193", 2],
    ["building36_0", "7-1194", 2],
    ["building37_0", "7-1195", 2],
    ["building38_0", "7-1196", 2],
    ["building39_0", "7-1197", 2],
    ["building40_0", "7-1198", 2],
    ["building41_0", "7-1199", 2],
    ["building42_0", "7-1200", 2],
    ["building43_0", "7-1201", 2],
    ["building45_0", "7-1203", 2],
    ["building46_0", "7-1204", 2],
    ["building47_0", "7-1205", 2],
    ["building48_0", "7-1206", 2],
    ["building49_0", "7-1207", 2],
    ["building50_0", "7-1208", 2],
    ["building51_0", "7-1209", 2],
    ["building76_0", "7-1234", 2],
    ["building69_0", "7-1227", 2],
    ["building77_0", "7-1235", 2],
    ["building52_0", "7-1210", 2],
    ["building78_0", "7-1236", 2],
    ["building79_0", "7-1237", 2],
    ["building80_0", "7-1238", 2],
    ["building99_0", "7-1257", 2],
    ["building100_0", "7-1258", 2],
    ["building91_0", "7-1249", 2],
    ["building53_0", "7-1211", 2],
    ["building27_0", "7-1185", 2],
    ["building92_0", "7-1250", 2],
    ["building93_0", "7-1251", 2],
    ["building94_0", "7-1252", 2],
    ["building95_0", "7-1253", 2],
    ["building96_0", "7-1254", 2],
    ["building97_0", "7-1255", 2],
    ["building98_0", "7-1256", 2],
    ["building55_0", "7-1213", 2],
    ["building1_0", "7-433", 2],
    ["building2_0", "7-434", 2],
    ["building3_0", "7-435", 2],
    ["building4_0", "7-436", 2],
    ["building5_0", "7-437", 2],
    ["building6_0", "7-438", 2],
    ["building7_0", "7-439", 2],
    ["building8_0", "7-440", 2],
    ["building9_0", "7-441", 2],
    ["building10_0", "7-442", 2],
    ["building11_0", "7-443", 2],
    ["building12_0", "7-444", 2],
    ["building13_0", "7-445", 2],
    ["building14_0", "7-446", 2],
    ["building15_0", "7-447", 2],
    ["building16_0", "7-448", 2],
    ["building17_0", "7-449", 2],
    ["building18_0", "7-450", 2],
    ["building19_0", "7-451", 2],
    ["building20_0", "7-452", 2],
    ["building21_0", "7-453", 2],
    ["building22_0", "7-454", 2],
    ["building23_0", "7-455", 2],
    ["building24_0", "7-456", 2],
    ["building25_0", "7-457", 2],
    ["building26_0", "7-458", 2],
    ["trash5", "delete", -1]
]
building = [
    ["church_0", "7-401", 2],
    ["feudo_0", "7-402", 2],
    ["castle_0", "7-404", 2],
    ["castle2_0", "7-405", 2],
    ["castle3_0", "7-410", 2],
    ["house_0", "7-403", 2],
    ["volcan", "7-407", 2],
    ["trash2", "delete", -1]
]
# Construcción
# 0: objeto normal, 1: puerta, 2: edificio, 3: item / objeto usable, 4: evento
bconstruccion = [
    ["big_construction_wall1_0", "41-1071", 0],
    ["big_construction_wall55_0", "41-1300", 0],
    ["big_construction_wall56_0", "41-1301", 0],
    ["big_construction_wall2_0", "41-1072", 0],
    ["big_construction_wall53_0", "41-1298", 0],
    ["big_construction_wall54_0", "41-1299", 0],
    ["big_construction_wall3_0", "41-1073", 0],
    ["big_construction_wall57_0", "41-1302", 0],
    ["big_construction_wall58_0", "41-1303", 0],
    ["big_construction_wall4_0", "41-1074", 0],
    ["big_construction_wall5_0", "41-1075", 0],
    ["big_construction_wall6_0", "41-1076", 0],
    ["big_construction_wall7_0", "41-1077", 0],
    ["big_construction_wall59_0", "41-1304", 0],
    ["big_construction_wall60_0", "41-1305", 0],
    ["big_construction_wall8_0", "41-1078", 0],
    ["big_construction_wall61_0", "41-1306", 0],
    ["big_construction_wall9_0", "41-1079", 0],
    ["big_construction_wall50_0", "41-1260", 0],
    ["big_construction_wall49_0", "41-1259", 0],
    ["big_construction_wall10_0", "41-1080", 0],
    ["big_construction_wall11_0", "41-1081", 0],
    ["big_construction_wall12_0", "41-1082", 0],
    ["big_construction_wall13_0", "41-1083", 0],
    ["big_construction_wall14_0", "41-1084", 0],
    ["big_construction_wall62_0", "41-1307", 0],
    ["big_construction_wall63_0", "41-1308", 0],
    ["big_construction_wall15_0", "41-1085", 0],
    ["big_construction_wall16_0", "41-1086", 0],
    ["big_construction_wall17_0", "41-1087", 0],
    ["big_construction_wall18_0", "41-1088", 0],
    ["big_construction_wall19_0", "41-1089", 0],
    ["big_construction_wall20_0", "41-1090", 0],
    ["big_construction_wall21_0", "41-1091", 0],
    ["big_construction_wall22_0", "41-1092", 0],
    ["big_construction_wall23_0", "41-1093", 0],
    ["big_construction_wall24_0", "41-1094", 0],
    ["big_construction_wall25_0", "41-1095", 0],
    ["big_construction_wall26_0", "41-1096", 0],
    ["big_construction_wall27_0", "41-1097", 0],
    ["big_construction_wall28_0", "41-1098", 0],
    ["big_construction_wall29_0", "41-1099", 0],
    ["big_construction_wall30_0", "41-1100", 0],
    ["big_construction_wall31_0", "41-1101", 0],
    ["big_construction_wall32_0", "41-1102", 0],
    ["big_construction_wall33_0", "41-1103", 0],
    ["big_construction_wall34_0", "41-1104", 0],
    ["big_construction_wall51_0", "41-1296", 0],
    ["big_construction_wall52_0", "41-1297", 0],
    ["big_construction_wall35_0", "41-1105", 0],
    ["big_construction_wall36_0", "41-1106", 0],
    ["big_construction_wall37_0", "41-1107", 0],
    ["big_construction_wall38_0", "41-1108", 0],
    ["big_construction_wall39_0", "41-1109", 0],
    ["big_construction_wall40_0", "41-1110", 0],
    ["big_construction_wall41_0", "41-1111", 0],
    ["big_construction_wall42_0", "41-1112", 0],
    ["big_construction_wall43_0", "41-1113", 0],
    ["big_construction_wall44_0", "41-1114", 0],
    ["big_construction_wall45_0", "41-1115", 0],
    ["big_construction_wall46_0", "41-1116", 0],
    ["big_construction_wall47_0", "41-1117", 0],
    ["big_pilar1_0", "41-980", 0],
    ["big_pilar2_0", "41-981", 0],
    ["big_pilar3_0", "41-982", 0],
    ["big_pilar4_0", "41-983", 0],
    ["big_pilar5_0", "41-984", 0],
    ["big_pilar6_0", "41-985", 0],
    ["big_pilar7_0", "41-986", 0],
    ["big_pilar8_0", "41-987", 0],
    ["big_pilar9_0", "41-988", 0],
    ["big_pilar10_0", "41-989", 0],
    ["big_pilar11_0", "41-990", 0],
    ["big_pilar12_0", "41-991", 0],
    ["big_pilar13_0", "41-992", 0],
    ["big_pilar14_0", "41-993", 0],
    ["big_pilar15_0", "41-994", 0],
    ["big_escalera1_0", 1057, 7],
    ["big_escalera2_0", 1058, 7],
    ["big_escalera3_0", 1059, 7],
    ["big_escalera4_0", 1060, 7],
    ["big_escalera5_0", 1061, 7],
    ["big_escalera6_0", 1062, 7],
    ["big_escalera7_0", 1063, 7],
    ["big_escalera8_0", 1064, 7],
    ["big_escalera9_0", 1065, 7],
    ["big_escalera10_0", 1066, 7],
    ["big_escalera11_0", 1067, 7],
    ["big_escalera12_0", 1068, 7],
    ["big_escalera13_0", 1069, 7],
    ["big_escalera14_0", 1070, 7],
    ["big_puerta1_0", 1130, 1],
    ["big_puerta2_0", 1131, 1],
    ["big_puerta3_0", 1132, 1],
    ["big_puerta4_0", 1133, 1],
    ["big_puerta5_0", 1134, 1],
    ["big_puerta6_0", 1135, 1],
    ["big_puerta7_0", 1136, 1],
    ["big_puerta8_0", 1137, 1],
    ["big_puerta9_0", 1138, 1],
    ["big_puerta10_0", 1139, 1],
    ["big_puerta11_0", 1140, 1],
    ["big_puerta12_0", 1141, 1],
    ["trash5", "delete", -1]
]
construccion = [
    ["construction_wall1_0", "41-995", 0],
    ["construction_wall2_0", "41-996", 0],
    ["construction_wall3_0", "41-997", 0],
    ["construction_wall4_0", "41-998", 0],
    ["construction_wall5_0", "41-1042", 0],
    ["construction_wall6_0", "41-1000", 0],
    ["construction_wall7_0", "41-1001", 0],
    ["construction_wall8_0", "41-1002", 0],
    ["construction_wall9_0", "41-1003", 0],
    ["construction_wall10_0", "41-1004", 0],
    ["construction_wall11_0", "41-1005", 0],
    ["construction_wall12_0", "41-1006", 0],
    ["construction_wall13_0", "41-1007", 0],
    ["construction_wall14_0", "41-1008", 0],
    ["construction_wall15_0", "41-1009", 0],
    ["construction_wall16_0", "41-1010", 0],
    ["construction_wall17_0", "41-1011", 0],
    ["construction_wall18_0", "41-1012", 0],
    ["construction_wall19_0", "41-1013", 0],
    ["construction_wall20_0", "41-1014", 0],
    ["construction_wall21_0", "41-1015", 0],
    ["construction_wall22_0", "41-1016", 0],
    ["construction_wall23_0", "41-1017", 0],
    ["construction_wall24_0", "41-1018", 0],
    ["construction_wall25_0", "41-1019", 0],
    ["construction_wall26_0", "41-1020", 0],
    ["construction_wall27_0", "41-1021", 0],
    ["construction_wall28_0", "41-1022", 0],
    ["construction_wall29_0", "41-1023", 0],
    ["construction_wall30_0", "41-1024", 0],
    ["construction_wall31_0", "41-1025", 0],
    ["construction_wall32_0", "41-1026", 0],
    ["construction_wall33_0", "41-1027", 0],
    ["construction_wall34_0", "41-1028", 0],
    ["construction_wall35_0", "41-1029", 0],
    ["construction_wall36_0", "41-1030", 0],
    ["construction_wall37_0", "41-1031", 0],
    ["construction_wall38_0", "41-1032", 0],
    ["construction_wall39_0", "41-1033", 0],
    ["construction_wall40_0", "41-1034", 0],
    ["construction_wall41_0", "41-1035", 0],
    ["construction_wall42_0", "41-1036", 0],
    ["construction_wall43_0", "41-1037", 0],
    ["construction_wall44_0", "41-1038", 0],
    ["construction_wall45_0", "41-1039", 0],
    ["construction_wall46_0", "41-1040", 0],
    ["construction_wall47_0", "41-1041", 0],
    ["pilar1_0", "41-965", 0],
    ["pilar2_0", "41-966", 0],
    ["pilar3_0", "41-967", 0],
    ["pilar4_0", "41-968", 0],
    ["pilar5_0", "41-969", 0],
    ["pilar6_0", "41-970", 0],
    ["pilar7_0", "41-971", 0],
    ["pilar8_0", "41-972", 0],
    ["pilar9_0", "41-973", 0],
    ["pilar10_0", "41-974", 0],
    ["pilar11_0", "41-975", 0],
    ["pilar12_0", "41-976", 0],
    ["pilar13_0", "41-977", 0],
    ["pilar14_0", "41-978", 0],
    ["pilar15_0", "41-979", 0],
    ["escalera1_0", 1043, 7],
    ["escalera2_0", 1044, 7],
    ["escalera3_0", 1045, 7],
    ["escalera4_0", 1046, 7],
    ["escalera5_0", 1047, 7],
    ["escalera6_0", 1048, 7],
    ["escalera7_0", 1049, 7],
    ["escalera8_0", 1050, 7],
    ["escalera9_0", 1051, 7],
    ["escalera10_0", 1052, 7],
    ["escalera11_0", 1053, 7],
    ["escalera12_0", 1054, 7],
    ["escalera13_0", 1055, 7],
    ["escalera14_0", 1056, 7],
    ["puerta1_0", 1118, 1],
    ["puerta2_0", 1119, 1],
    ["puerta3_0", 1120, 1],
    ["puerta4_0", 1121, 1],
    ["puerta5_0", 1122, 1],
    ["puerta6_0", 1123, 1],
    ["puerta7_0", 1124, 1],
    ["puerta8_0", 1125, 1],
    ["puerta9_0", 1126, 1],
    ["puerta10_0", 1127, 1],
    ["puerta11_0", 1128, 1],
    ["puerta12_0", 1129, 1],
    ["door1_0", 210, 1],
    ["door2_0", 281, 1],
    ["trash2", "delete", -1]
]
# Ambiente
# 0: objeto normal, 1: puerta, 2: edificio, 3: item / objeto usable, 4: evento
benvironment = [
    ["big_tree14_0", "2-638", 0],
    ["big_tree1_0", "2-625", 0],
    ["big_tree2_0", "2-626", 0],
    ["big_tree7_0", "2-631", 0],
    ["big_tree3_0", "2-627", 0],
    ["big_tree4_0", "2-628", 0],
    ["big_tree5_0", "2-629", 0],
    ["big_tree6_0", "2-630", 0],
    ["big_tree8_0", "2-632", 0],
    ["big_tree9_0", "2-633", 0],
    ["big_tree10_0", "2-634", 0],
    ["big_tree11_0", "2-635", 0],
    ["big_tree12_0", "2-636", 0],
    ["big_tree15_0", "2-639", 0],
    ["big_tree16_0", "2-640", 0],
    ["big_tree17_0", "2-641", 0],
    ["big_tree18_0", "2-642", 0],
    ["big_tree19_0", "2-643", 0],
    ["big_tree20_0", "2-644", 0],
    ["big_tree21_0", "2-645", 0],
    ["big_tree22_0", "2-646", 0],
    ["big_tree23_0", "2-647", 0],
    ["big_tree24_0", "2-648", 0],
    ["big_tree26_0", "2-650", 0],
    ["big_tree27_0", "2-651", 0],
    ["big_tree28_0", "2-652", 0],
    ["big_tree29_0", "2-653", 0],
    ["big_tree30_0", "2-654", 0],
    ["big_tree31_0", "2-655", 0],
    ["big_tree32_0", "2-656", 0],
    ["big_tree33_0", "2-657", 0],
    ["big_tree34_0", "2-658", 0],
    ["big_tree35_0", "2-659", 0],
    ["big_tree36_0", "2-660", 0],
    ["big_tree37_0", "2-661", 0],
    ["big_tree38_0", "2-662", 0],
    ["big_tree39_0", "2-663", 0],
    ["big_tree40_0", "2-664", 0],
    ["big_tree41_0", "2-665", 0],
    ["big_tree42_0", "2-666", 0],
    ["big_tree43_0", "2-667", 0],
    ["big_tree44_0", "2-668", 0],
    ["big_tree13_0", "2-637", 0],
    ["big_stone1_0", "5-669", 0],
    ["big_stone2_0", "5-670", 0],
    ["big_stone3_0", "5-671", 0],
    ["big_stone4_0", "5-672", 0],
    ["big_stone5_0", "5-673", 0],
    ["big_stone6_0", "5-674", 0],
    ["big_stone7_0", "5-675", 0],
    ["big_stone8_0", "5-676", 0],
    ["big_stone9_0", "5-677", 0],
    ["big_stone10_0", "5-678", 0],
    ["big_stone11_0", "5-679", 0],
    ["big_hongo1_0", "36-712", 0],
    ["big_hongo2_0", "36-713", 0],
    ["big_hongo3_0", "36-714", 0],
    ["big_hongo4_0", "36-715", 0],
    ["big_hongo5_0", "36-716", 0],
    ["big_hongo6_0", "36-717", 0],
    ["big_hongo7_0", "36-718", 0],
    ["big_hongo8_0", "36-719", 0],
    ["big_hongo9_0", "36-720", 0],
    ["big_ambiance_other1_0", "12-820", 0],
    ["big_ambiance_other2_0", "12-821", 0],
    ["big_ambiance_other3_0", "12-822", 0],
    ["big_ambiance_other4_0", "12-823", 0],
    ["big_ambiance_other5_0", "12-824", 0],
    ["big_ambiance_other6_0", "12-825", 0],
    ["big_ambiance_other7_0", "12-826", 0],
    ["big_ambiance_other8_0", "12-827", 0],
    ["big_ambiance_other9_0", "12-828", 0],
    ["big_ambiance_other10_0", "12-829", 0],
    ["big_ambiance_other11_0", "12-830", 0],
    ["big_ambiance_other12_0", "12-831", 0],
    ["big_ambiance_other13_0", "12-832", 0],
    ["big_ambiance_other14_0", "12-833", 0],
    ["big_ambiance_other15_0", "12-834", 0],
    ["big_ambiance_other16_0", "12-835", 0],
    ["big_ambiance_other17_0", "12-836", 0],
    ["big_ambiance_other18_0", "12-837", 0],
    ["big_ambiance_other19_0", "12-838", 0],
    ["big_statue1_0", "37-680", 0],
    ["big_statue2_0", "37-681", 0],
    ["big_statue3_0", "37-682", 0],
    ["big_statue4_0", "37-683", 0],
    ["big_statue5_0", "37-684", 0],
    ["big_statue6_0", "37-685", 0],
    ["big_statue7_0", "37-686", 0],
    ["big_statue8_0", "37-687", 0],
    ["big_statue9_0", "37-688", 0],
    ["big_statue10_0", "37-689", 0],
    ["big_statue11_0", "37-690", 0],
    ["big_statue12_0", "37-691", 0],
    ["big_statue13_0", "37-692", 0],
    ["big_statue14_0", "37-693", 0],
    ["big_statue15_0", "37-694", 0],
    ["big_statue16_0", "37-695", 0],
    ["big_statue17_0", "37-696", 0],
    ["big_statue18_0", "37-697", 0],
    ["big_statue19_0", "37-698", 0],
    ["big_statue20_0", "37-699", 0],
    ["big_statue21_0", "37-700", 0],
    ["big_statue22_0", "37-701", 0],
    ["big_statue23_0", "37-702", 0],
    ["big_statue24_0", "37-703", 0],
    ["big_statue25_0", "37-704", 0],
    ["big_statue26_0", "37-705", 0],
    ["big_statue27_0", "37-706", 0],
    ["big_statue28_0", "37-707", 0],
    ["big_statue29_0", "37-708", 0],
    ["big_statue30_0", "37-709", 0],
    ["big_statue31_0", "37-710", 0],
    ["big_statue32_0", "37-711", 0],
    ["trash5", "delete", -1]
]
environment = [
    ["tree1_0", "2-200", 0],
    ["tree2_0", "2-201", 0],
    ["tree3_0", "2-202", 0],
    ["tree4_0", "2-203", 0],
    ["tree5_0", "2-260", 0],
    ["tree6_0", "2-261", 0],
    ["tree7_0", "2-285", 0],
    ["tree8_0", "2-212", 0],
    ["tree9_0", "2-213", 0],
    ["tree10_0", "2-214", 0],
    ["tree11_0", "2-215", 0],
    ["tree12_0", "2-216", 0],
    ["tree13_0", "2-217", 0],
    ["tree14_0", "2-218", 0],
    ["tree15_0", "2-219", 0],
    ["tree16_0", "2-220", 0],
    ["tree17_0", "2-221", 0],
    ["tree18_0", "2-222", 0],
    ["tree19_0", "2-223", 0],
    ["tree20_0", "2-224", 0],
    ["tree21_0", "2-225", 0],
    ["tree22_0", "2-226", 0],
    ["tree23_0", "2-227", 0],
    ["tree24_0", "2-228", 0],
    ["tree25_0", "2-229", 0],
    ["tree26_0", "2-230", 0],
    ["tree27_0", "2-231", 0],
    ["tree28_0", "2-232", 0],
    ["tree29_0", "2-233", 0],
    ["tree30_0", "2-234", 0],
    ["tree31_0", "2-235", 0],
    ["tree32_0", "2-236", 0],
    ["tree33_0", "2-237", 0],
    ["tree34_0", "2-238", 0],
    ["tree36_0", "2-240", 0],
    ["tree37_0", "2-241", 0],
    ["tree38_0", "2-242", 0],
    ["tree39_0", "2-243", 0],
    ["tree40_0", "2-244", 0],
    ["tree35_0", "2-239", 0],
    ["tree41_0", "2-245", 0],
    ["tree42_0", "2-246", 0],
    ["tree43_0", "2-247", 0],
    ["tree44_0", "2-248", 0],
    ["tree45_0", "2-249", 0],
    ["tree46_0", "2-250", 0],
    ["tree47_0", "2-251", 0],
    ["tree48_0", "2-252", 0],
    ["tree49_0", "2-253", 0],
    ["tree50_0", "2-254", 0],
    ["ambiance_grass1_0", "40-262", 0],
    ["ambiance_grass2_0", "40-263", 0],
    ["ambiance_grass3_0", "40-264", 0],
    ["ambiance_grass4_0", "40-265", 0],
    ["ambiance_grass5_0", "40-266", 0],
    ["ambiance_grass6_0", "40-267", 0],
    ["ambiance_grass7_0", "40-268", 0],
    ["ambiance_grass8_0", "40-269", 0],
    ["ambiance_grass9_0", "12-270", 0],
    ["bushes1_0", "34-271", 0],
    ["bushes2_0", "34-272", 0],
    ["bushes3_0", "34-273", 0],
    ["bushes4_0", "34-274", 0],
    ["bushes5_0", "34-275", 0],
    ["bushes6_0", "34-276", 0],
    ["bushes7_0", "34-277", 0],
    ["bushes8_0", "34-278", 0],
    ["bushes9_0", "34-279", 0],
    ["bushes10_0", "34-280", 0],
    ["flower1_0", "34-500", 0],
    ["flower2_0", "34-501", 0],
    ["flower3_0", "34-502", 0],
    ["flower4_0", "34-503", 0],
    ["flower5_0", "34-504", 0],
    ["flower6_0", "34-505", 0],
    ["flower7_0", "34-506", 0],
    ["flower8_0", "34-507", 0],
    ["flower9_0", "34-508", 0],
    ["flower10_0", "34-509", 0],
    ["flower11_0", "34-510", 0],
    ["flower12_0", "34-511", 0],
    ["flower13_0", "34-512", 0],
    ["flower14_0", "34-513", 0],
    ["flower15_0", "34-514", 0],
    ["flower16_0", "34-515", 0],
    ["flower17_0", "34-516", 0],
    ["flower18_0", "34-517", 0],
    ["flower19_0", "34-518", 0],
    ["flower20_0", "34-519", 0],
    ["flower21_0", "34-520", 0],
    ["flower22_0", "34-521", 0],
    ["flower23_0", "34-522", 0],
    ["flower24_0", "34-523", 0],
    ["flower25_0", "34-524", 0],
    ["flower26_0", "34-525", 0],
    ["flower27_0", "34-526", 0],
    ["flower28_0", "34-527", 0],
    ["flower29_0", "34-528", 0],
    ["flower30_0", "34-529", 0],
    ["flower31_0", "34-530", 0],
    ["flower32_0", "34-531", 0],
    ["flower33_0", "34-532", 0],
    ["flower34_0", "34-533", 0],
    ["flower35_0", "34-534", 0],
    ["flower36_0", "34-535", 0],
    ["flower37_0", "34-536", 0],
    ["plant1_0", "34-537", 0],
    ["plant2_0", "34-538", 0],
    ["plant3_0", "34-539", 0],
    ["plant4_0", "34-540", 0],
    ["plant5_0", "34-541", 0],
    ["plant6_0", "34-542", 0],
    ["plant7_0", "34-543", 0],
    ["plant8_0", "34-544", 0],
    ["plant9_0", "34-545", 0],
    ["plant10_0", "34-546", 0],
    ["plant11_0", "34-547", 0],
    ["plant12_0", "34-548", 0],
    ["plant13_0", "34-549", 0],
    ["plant14_0", "34-550", 0],
    ["plant15_0", "34-551", 0],
    ["plant16_0", "34-552", 0],
    ["plant17_0", "34-553", 0],
    ["plant18_0", "34-554", 0],
    ["plant19_0", "34-555", 0],
    ["plant20_0", "34-556", 0],
    ["plant21_0", "34-557", 0],
    ["plant22_0", "34-558", 0],
    ["plant23_0", "34-559", 0],
    ["cactus1_0", "35-593", 0],
    ["cactus2_0", "35-594", 0],
    ["cactus3_0", "35-595", 0],
    ["cactus4_0", "35-596", 0],
    ["cactus5_0", "35-597", 0],
    ["cactus6_0", "35-598", 0],
    ["cactus7_0", "35-599", 0],
    ["hongo1_0", "36-600", 0],
    ["hongo2_0", "36-601", 0],
    ["hongo3_0", "36-602", 0],
    ["hongo4_0", "36-603", 0],
    ["hongo5_0", "36-604", 0],
    ["hongo6_0", "36-605", 0],
    ["hongo7_0", "36-606", 0],
    ["hongo8_0", "36-607", 0],
    ["hongo9_0", "36-608", 0],
    ["hongo10_0", "36-609", 0],
    ["hongo11_0", "36-610", 0],
    ["hongo12_0", "36-611", 0],
    ["hongo13_0", "36-612", 0],
    ["hongo14_0", "36-613", 0],
    ["hongo15_0", "36-614", 0],
    ["hongo16_0", "36-615", 0],
    ["hongo17_0", "36-616", 0],
    ["hongo18_0", "36-617", 0],
    ["hongo19_0", "36-618", 0],
    ["hongo20_0", "36-619", 0],
    ["hongo21_0", "36-620", 0],
    ["tronco1_0", "2-204", 0],
    ["tronco2_0", "2-204", 0],
    ["rock1_0", "5-282", 0],
    ["rock2_0", "5-288", 0],
    ["stone1_0", "5-560", 0],
    ["stone2_0", "5-561", 0],
    ["stone3_0", "5-562", 0],
    ["stone4_0", "5-563", 0],
    ["stone5_0", "5-564", 0],
    ["stone6_0", "5-565", 0],
    ["stone7_0", "5-566", 0],
    ["stone8_0", "5-567", 0],
    ["stone9_0", "5-568", 0],
    ["stone10_0", "5-569", 0],
    ["stone11_0", "5-570", 0],
    ["stone12_0", "5-571", 0],
    ["stone13_0", "5-572", 0],
    ["stone14_0", "5-573", 0],
    ["stone15_0", "5-574", 0],
    ["stone16_0", "5-575", 0],
    ["stone17_0", "5-576", 0],
    ["stone18_0", "5-577", 0],
    ["stone19_0", "5-578", 0],
    ["stone20_0", "5-579", 0],
    ["stone21_0", "5-580", 0],
    ["stone22_0", "5-581", 0],
    ["stone23_0", "5-582", 0],
    ["stone24_0", "5-583", 0],
    ["stone25_0", "5-584", 0],
    ["stone26_0", "5-585", 0],
    ["stone27_0", "5-586", 0],
    ["stone28_0", "5-587", 0],
    ["stone29_0", "5-588", 0],
    ["stone30_0", "5-589", 0],
    ["stone31_0", "5-590", 0],
    ["stone32_0", "5-591", 0],
    ["stone33_0", "5-592", 0],
    ["shell1_0", "0-621", 0],
    ["shell2_0", "0-622", 0],
    ["shell3_0", "0-623", 0],
    ["shell4_0", "0-624", 0],
    ["lapida_0", "12-289", 0],
    ["statue1_0", "37-296", 0],
    ["statue2_0", "37-297", 0],
    ["statue3_0", "37-298", 0],
    ["statue4_0", "37-299", 0],
    ["sign1_0", "38-732", 38],
    ["sign2_0", "38-733", 38],
    ["sign3_0", "38-734", 38],
    ["sign4_0", "38-735", 38],
    ["sign5_0", "38-736", 38],
    ["sign6_0", "38-737", 38],
    ["sign7_0", "38-738", 38],
    ["sign8_0", "38-739", 38],
    ["sign9_0", "38-740", 38],
    ["sign10_0", "38-741", 38],
    ["sign11_0", "38-742", 38],
    ["sign12_0", "38-743", 38],
    ["sign13_0", "38-744", 38],
    ["sign14_0", "38-745", 38],
    ["sign15_0", "38-746", 38],
    ["sign16_0", "38-747", 38],
    ["sign17_0", "38-748", 38],
    ["sign18_0", "38-749", 38],
    ["sign19_0", "38-750", 38],
    ["flag1_0", "12-751", 0],
    ["flag2_0", "12-752", 0],
    ["flag3_0", "12-753", 0],
    ["flag4_0", "12-754", 0],
    ["flag5_0", "12-755", 0],
    ["flag6_0", "12-756", 0],
    ["flag7_0", "12-757", 0],
    ["flag8_0", "12-758", 0],
    ["flag9_0", "12-759", 0],
    ["ship_0", "27-295", 6],
    ["ambiance_other1_0", "12-760", 0],
    ["ambiance_other2_0", "12-761", 0],
    ["ambiance_other3_0", "12-762", 0],
    ["ambiance_other4_0", "12-763", 0],
    ["ambiance_other5_0", "12-764", 0],
    ["ambiance_other6_0", "12-765", 0],
    ["ambiance_other7_0", "12-766", 0],
    ["ambiance_other8_0", "12-767", 0],
    ["ambiance_other9_0", "12-768", 0],
    ["ambiance_other10_0", "12-769", 0],
    ["ambiance_other11_0", "12-770", 0],
    ["ambiance_other12_0", "12-771", 0],
    ["ambiance_other13_0", "12-772", 0],
    ["ambiance_other14_0", "12-773", 0],
    ["ambiance_other15_0", "12-774", 0],
    ["ambiance_other16_0", "12-775", 0],
    ["ambiance_other17_0", "12-776", 0],
    ["ambiance_other18_0", "12-777", 0],
    ["ambiance_other19_0", "12-778", 0],
    ["ambiance_other20_0", "12-779", 0],
    ["ambiance_other21_0", "12-780", 0],
    ["ambiance_other22_0", "12-781", 0],
    ["ambiance_other23_0", "12-782", 0],
    ["ambiance_other24_0", "12-783", 0],
    ["ambiance_other25_0", "12-784", 0],
    ["ambiance_other26_0", "12-785", 0],
    ["ambiance_other27_0", "12-786", 0],
    ["ambiance_other28_0", "12-787", 0],
    ["ambiance_other29_0", "12-788", 0],
    ["ambiance_other30_0", "12-789", 0],
    ["ambiance_other31_0", "12-790", 0],
    ["ambiance_other32_0", "12-791", 0],
    ["ambiance_other33_0", "12-792", 0],
    ["ambiance_other34_0", "12-793", 0],
    ["totem_0", "12-287", 0],
    ["ambiance_other35_0", "12-794", 0],
    ["ambiance_other36_0", "12-795", 0],
    ["ambiance_other37_0", "12-796", 0],
    ["ambiance_other38_0", "12-797", 0],
    ["ambiance_other39_0", "12-798", 0],
    ["ambiance_other40_0", "12-799", 0],
    ["ambiance_other41_0", "12-800", 0],
    ["ambiance_other42_0", "12-801", 0],
    ["ambiance_other43_0", "12-802", 0],
    ["ambiance_other44_0", "12-803", 0],
    ["ambiance_other45_0", "12-804", 0],
    ["ambiance_other46_0", "12-805", 0],
    ["ambiance_other47_0", "12-806", 0],
    ["ambiance_other48_0", "12-807", 0],
    ["ambiance_other49_0", "12-808", 0],
    ["ambiance_other50_0", "12-809", 0],
    ["ambiance_other51_0", "12-810", 0],
    ["ambiance_other52_0", "12-811", 0],
    ["ambiance_other53_0", "12-812", 0],
    ["ambiance_other54_0", "12-813", 0],
    ["ambiance_other55_0", "12-814", 0],
    ["ambiance_other56_0", "12-815", 0],
    ["ambiance_other57_0", "12-816", 0],
    ["ambiance_other58_0", "12-817", 0],
    ["ambiance_other59_0", "12-818", 0],
    ["ambiance_other60_0", "12-819", 0],
    ["ambient_effect1_0", "39-960", 0],
    ["ambient_effect3_0", "39-962", 0],
    ["ambient_effect4_0", "39-963", 0],
    ["ambient_effect5_0", "39-964", 0],
    ["ambient_effect2_0", "39-961", 2],
    ["antorcha", "14-408", 2],
    ["antorcha2", "14-411", 2],
    ["antorcha3", "14-412", 2],
    ["antorcha4", "14-413", 2],
    ["antorcha5", "14-414", 2],
    ["antorcha6", "14-415", 2],
    ["antorcha7", "14-416", 2],
    ["antorcha8", "14-417", 2],
    ["antorcha9", "14-418", 2],
    ["antorcha10", "14-419", 2],
    ["antorcha11", "14-420", 2],
    ["antorcha12", "14-421", 2],
    ["antorcha13", "14-422", 2],
    ["antorcha14", "14-423", 2],
    ["antorcha15", "14-424", 2],
    ["antorcha16", "14-425", 2],
    ["antorcha17", "14-426", 2],
    ["antorcha18", "14-427", 2],
    ["antorcha19", "14-428", 2],
    ["antorcha20", "14-429", 2],
    ["antorcha21", "14-430", 2],
    ["antorcha22", "14-431", 2],
    ["antorcha23", "14-432", 2],
    ["trash2", "delete", -1]
]
# Interior
# 0: objeto normal, 1: puerta, 2: edificio, 3: item / objeto usable, 4:
# evento, 5:cama [bed]
binterior = [
    ["big_interior1_0", "12-899", 0],
    ["big_interior2_0", "12-900", 0],
    ["big_interior3_0", "26-901", 0],
    ["big_interior4_0", "12-902", 0],
    ["big_interior5_0", "12-903", 0],
    ["big_interior6_0", "12-904", 0],
    ["big_interior7_0", "12-286", 0],
    ["big_carpet1_0", "44-721", 0],
    ["big_carpet2_0", "44-722", 0],
    ["big_carpet3_0", "44-723", 0],
    ["big_carpet4_0", "44-724", 0],
    ["big_carpet5_0", "44-725", 0],
    ["big_carpet6_0", "44-726", 0],
    ["big_carpet7_0", "44-727", 0],
    ["big_carpet8_0", "44-728", 0],
    ["big_carpet10_0", "44-730", 0],
    ["big_carpet11_0", "44-731", 0],
    ["big_furniture1_0", "12-1179", 0],
    ["big_furniture2_0", "12-1180", 0],
    ["big_furniture3_0", "12-1181", 0],
    ["big_furniture4_0", "12-1182", 0],
    ["big_furniture5_0", "12-1183", 0],
    ["big_furniture6_0", "12-1184", 0],
    ["big_barril1_0", "12-255", 0],
    ["trash5", "delete", -1]
]
interior = [
    ["interior1_0", "12-839", 0],
    ["interior2_0", "12-840", 0],
    ["interior3_0", "26-841", 0],
    ["bed_0", "26-290", 0],
    ["interior9_0", "26-847", 0],
    ["interior11_0", "26-849", 0],
    ["interior4_0", "26-842", 0],
    ["interior15_0", "26-853", 0],
    ["interior21_0", "26-859", 0],
    ["interior32_0", "26-870", 0],
    ["interior39_0", "26-877", 0],
    ["interior5_0", "12-843", 0],
    ["interior6_0", "12-844", 0],
    ["interior7_0", "12-845", 0],
    ["interior8_0", "12-846", 0],
    ["interior10_0", "12-848", 0],
    ["interior12_0", "12-850", 0],
    ["interior13_0", "12-851", 0],
    ["interior14_0", "12-852", 0],
    ["interior16_0", "12-854", 0],
    ["interior17_0", "12-855", 0],
    ["interior18_0", "12-856", 0],
    ["interior19_0", "12-857", 0],
    ["interior20_0", "12-858", 0],
    ["interior22_0", "12-860", 0],
    ["interior23_0", "12-861", 0],
    ["interior24_0", "12-862", 0],
    ["interior25_0", "12-863", 0],
    ["interior26_0", "12-864", 0],
    ["interior27_0", "12-865", 0],
    ["interior28_0", "12-866", 0],
    ["interior29_0", "12-867", 0],
    ["interior30_0", "12-868", 0],
    ["interior31_0", "12-869", 0],
    ["interior33_0", "12-871", 0],
    ["interior34_0", "12-872", 0],
    ["interior35_0", "12-873", 0],
    ["interior36_0", "12-874", 0],
    ["interior37_0", "12-875", 0],
    ["interior38_0", "12-876", 0],
    ["interior40_0", "12-878", 0],
    ["interior41_0", "12-879", 0],
    ["interior42_0", "12-880", 0],
    ["interior43_0", "12-881", 0],
    ["interior44_0", "12-882", 0],
    ["interior45_0", "12-883", 0],
    ["interior46_0", "12-884", 0],
    ["interior47_0", "12-885", 0],
    ["interior48_0", "12-886", 0],
    ["interior49_0", "12-887", 0],
    ["interior50_0", "12-888", 0],
    ["interior51_0", "12-889", 0],
    ["interior52_0", "12-890", 0],
    ["interior53_0", "12-891", 0],
    ["interior54_0", "12-892", 0],
    ["interior55_0", "12-893", 0],
    ["interior56_0", "12-894", 0],
    ["interior57_0", "12-895", 0],
    ["interior58_0", "12-896", 0],
    ["interior59_0", "12-897", 0],
    ["interior60_0", "12-898", 0],
    ["interior61_0", "12-925", 0],
    ["interior62_0", "12-926", 0],
    ["interior63_0", "12-927", 0],
    ["interior64_0", "12-928", 0],
    ["interior65_0", "12-929", 0],
    ["interior66_0", "12-930", 0],
    ["interior67_0", "12-931", 0],
    ["interior68_0", "12-932", 0],
    ["interior69_0", "12-933", 0],
    ["interior70_0", "12-934", 0],
    ["interior71_0", "12-935", 0],
    ["interior72_0", "12-936", 0],
    ["interior73_0", "12-937", 0],
    ["interior74_0", "12-938", 0],
    ["interior75_0", "12-939", 0],
    ["interior76_0", "12-940", 0],
    ["interior77_0", "12-941", 0],
    ["interior78_0", "12-942", 0],
    ["interior79_0", "12-943", 0],
    ["interior80_0", "12-944", 0],
    ["interior81_0", "12-945", 0],
    ["interior82_0", "12-946", 0],
    ["interior83_0", "12-947", 0],
    ["interior84_0", "12-948", 0],
    ["interior85_0", "12-949", 0],
    ["interior86_0", "12-950", 0],
    ["interior87_0", "12-951", 0],
    ["interior88_0", "12-952", 0],
    ["interior89_0", "12-953", 0],
    ["interior90_0", "12-954", 0],
    ["interior91_0", "12-955", 0],
    ["interior92_0", "12-956", 0],
    ["interior93_0", "12-957", 0],
    ["interior94_0", "12-958", 0],
    ["interior95_0", "12-959", 0],
    ["furniture1_0", "12-1142", 0],
    ["furniture2_0", "12-1143", 0],
    ["furniture3_0", "12-1144", 0],
    ["furniture4_0", "12-1145", 0],
    ["furniture5_0", "12-1146", 0],
    ["furniture6_0", "12-1147", 0],
    ["furniture7_0", "12-1148", 0],
    ["furniture8_0", "12-1149", 0],
    ["furniture9_0", "12-1150", 0],
    ["furniture10_0", "12-1151", 0],
    ["furniture11_0", "12-1152", 0],
    ["furniture12_0", "12-1153", 0],
    ["furniture13_0", "12-1154", 0],
    ["furniture14_0", "12-1155", 0],
    ["furniture15_0", "12-1156", 0],
    ["furniture16_0", "12-1157", 0],
    ["furniture17_0", "12-1158", 0],
    ["furniture18_0", "12-1159", 0],
    ["furniture19_0", "12-1160", 0],
    ["furniture20_0", "12-1161", 0],
    ["furniture21_0", "12-1162", 0],
    ["furniture22_0", "12-1163", 0],
    ["furniture23_0", "12-1164", 0],
    ["furniture24_0", "12-1165", 0],
    ["furniture25_0", "12-1166", 0],
    ["furniture26_0", "12-1167", 0],
    ["furniture27_0", "12-1168", 0],
    ["furniture28_0", "12-1169", 0],
    ["furniture29_0", "12-1170", 0],
    ["furniture30_0", "12-1171", 0],
    ["furniture31_0", "12-1172", 0],
    ["furniture32_0", "12-1173", 0],
    ["furniture33_0", "12-1174", 0],
    ["furniture34_0", "12-1175", 0],
    ["furniture35_0", "12-1176", 0],
    ["furniture36_0", "12-1177", 0],
    ["furniture37_0", "12-1178", 0],
    ["trophy1_0", "12-905", 0],
    ["trophy2_0", "12-906", 0],
    ["trophy3_0", "12-907", 0],
    ["trophy4_0", "12-908", 0],
    ["trophy5_0", "12-909", 0],
    ["trophy6_0", "12-910", 0],
    ["trophy7_0", "12-911", 0],
    ["trophy8_0", "12-912", 0],
    ["trophy9_0", "12-913", 0],
    ["trophy10_0", "12-914", 0],
    ["trophy11_0", "12-915", 0],
    ["trophy12_0", "12-916", 0],
    ["trophy13_0", "12-917", 0],
    ["trophy14_0", "12-918", 0],
    ["trophy15_0", "12-919", 0],
    ["trophy16_0", "12-920", 0],
    ["trophy17_0", "12-921", 0],
    ["trophy18_0", "12-922", 0],
    ["trophy19_0", "12-923", 0],
    ["trophy20_0", "12-924", 0],
    ["carpet1_0", "44-283", 0],
    ["carpet2_0", "44-284", 0],
    ["barril1_0", "12-257", 0],
    ["barril2_0", "12-258", 0],
    ["barril3_0", "12-259", 0],
    ["chair1_0", "12-291", 0],
    ["cofre_0", "3-292", 4],
    ["librero1_0", "16-293", 5],
    ["mesa_0", "12-294", 0],
    ["trash2", "delete", -1]
]
# Terreno
terrain = [
    ["dirt1_0", 101],
    ["dirt2_0", 102],
    ["dirt3_0", 103],
    ["dirt4_0", 116],
    ["dirt5_0", 130],
    ["dirt6_0", 170],
    ["dirt7_0", 117],
    ["dirt8_0", 118],
    ["dirt9_0", 119],
    ["dirt10_0", 123],
    ["sand1_0", 107],
    ["sand2_0", 108],
    ["sand3_0", 180],
    ["sand4_0", 181],
    ["sand5_0", 182],
    ["grava1_0", 114],
    ["grava2_0", 115],
    ["grava3_0", 133],
    ["grass1_0", 104],
    ["grass2_0", 105],
    ["grass3_0", 106],
    ["grass4_0", 164],
    ["grass5_0", 165],
    ["grass6_0", 166],
    ["grass7_0", 187],
    ["grass8_0", 197],
    ["grass9_0", 198],
    ["pavimento1_0", 113],
    ["pavimento5_0", 192],
    ["pavimento2_0", 160],
    ["pavimento4_0", 176],
    ["pavimento3_0", 175],
    ["pavimento6_0", 143],
    ["pavimento7_0", 144],
    ["pavimento8_0", 145],
    ["pavimento9_0", 146],
    ["pavimento10_0", 147],
    ["pavimento11_0", 148],
    ["ladrillo3_0", 163],
    ["pisomadera1_0", 112],
    ["pisomadera2_0", 193],
    ["pisomadera3_0", 167],
    ["pisomadera4_0", 168],
    ["pisomadera5_0", 169],
    ["pisomadera6_0", 149],
    ["floor1_0", 185],
    ["floor2_0", 196],
    ["floor3_0", 134],
    ["floor4_0", 135],
    ["floor5_0", 136],
    ["floor6_0", 137],
    ["floor7_0", 138],
    ["floor8_0", 139],
    ["floor9_0", 140],
    ["floor10_0", 141],
    ["floor11_0", 142],
    ["ladrillo4_0", 191],
    ["ladrillo1_0", 161],
    ["ladrillo2_0", 162],
    ["nether1_0", 120],
    ["nether3_0", 122],
    ["nether2_0", 121],
    ["nether4_0", 183],
    ["nether5_0", 184],
    ["ice1_0", 188],
    ["ice2_0", 189],
    ["ice3_0", 190],
    ["water1_0", 109],
    ["water2_0", 110],
    ["water3_0", 132],
    ["water4_0", 194],
    ["water5_0", 195],
    ["water6_0", 124],
    ["water7_0", 125],
    ["lava1", 150],
    ["lava2", 151],
    ["lava3", 152],
    ["pantano1_0", 111],
    ["pantano2_0", 131],
    ["black", 256]
]


class mapEditorTextures(object):
    """Clase principal de texturas del editor de mapas"""

    def __init__(self):
        """
        Función constructora, en ella se cargan todas las imágenes
        :return: void
        """
        # Se genera el objeto hoaTextures
        self._hoatextures = hoaTextures()
        # Se cargan los paquetes
        self.packages = self._hoatextures.packages
        # Cargo las imagenes básicas
        self.images = self._hoatextures.images
        # Cargo las imágenes del mundo
        for link in IMAGES.keys():
            self.loadIMAGE(link)
        # Texturas especiales para map editor
        self.images["a_mov"] = PhotoImage(file=DATA_IMAGES_EDITOR + "a_mov.gif")
        self.images["alert_icon"] = DATA_ICONS + "alert.ico"
        self.images["amove"] = PhotoImage(file=DATA_IMAGES_EDITOR + "amove.gif")
        self.images["autosave"] = PhotoImage(file=DATA_IMAGES_EDITOR + "autosave.gif")
        self.images["autosave_ico"] = DATA_ICONS + "autosave.ico"
        self.images["b_mov"] = PhotoImage(file=DATA_IMAGES_EDITOR + "b_mov.gif")
        self.images["black"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "black.gif")
        self.images["bmove"] = PhotoImage(file=DATA_IMAGES_EDITOR + "bmove.gif")
        self.images["building_add"] = DATA_ICONS + "building_add.ico"
        self.images["c_mov"] = PhotoImage(file=DATA_IMAGES_EDITOR + "c_mov.gif")
        self.images["d_mov"] = PhotoImage(file=DATA_IMAGES_EDITOR + "d_mov.gif")
        self.images["dirt10_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "dirt10_0.gif")
        self.images["dirt10_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "dirt10_1.gif")
        self.images["dirt1_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "dirt1_0.gif")
        self.images["dirt1_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "dirt1_1.gif")
        self.images["dirt2_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "dirt2_0.gif")
        self.images["dirt2_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "dirt2_1.gif")
        self.images["dirt3_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "dirt3_0.gif")
        self.images["dirt3_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "dirt3_1.gif")
        self.images["dirt4_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "dirt4_0.gif")
        self.images["dirt4_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "dirt4_1.gif")
        self.images["dirt5_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "dirt5_0.gif")
        self.images["dirt5_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "dirt5_1.gif")
        self.images["dirt6_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "dirt6_0.gif")
        self.images["dirt6_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "dirt6_1.gif")
        self.images["dirt7_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "dirt7_0.gif")
        self.images["dirt7_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "dirt7_1.gif")
        self.images["dirt8_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "dirt8_0.gif")
        self.images["dirt8_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "dirt8_1.gif")
        self.images["dirt9_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "dirt9_0.gif")
        self.images["dirt9_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "dirt9_1.gif")
        self.images["door"] = DATA_IMAGES_EDITOR + "door_icon.ico"
        self.images["e_mov"] = PhotoImage(file=DATA_IMAGES_EDITOR + "e_mov.gif")
        self.images["error_icon"] = DATA_ICONS + "error_icon.ico"
        self.images["event_ico"] = DATA_ICONS + "event.ico"
        self.images["events"] = PhotoImage(file=DATA_IMAGES_EDITOR + "events.gif")
        self.images["f_mov"] = PhotoImage(file=DATA_IMAGES_EDITOR + "f_mov.gif")
        self.images["floor10_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "floor10_0.gif")
        self.images["floor10_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "floor10_1.gif")
        self.images["floor11_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "floor11_0.gif")
        self.images["floor11_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "floor11_1.gif")
        self.images["floor1_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "floor1_0.gif")
        self.images["floor1_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "floor1_1.gif")
        self.images["floor2_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "floor2_0.gif")
        self.images["floor2_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "floor2_1.gif")
        self.images["floor3_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "floor3_0.gif")
        self.images["floor3_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "floor3_1.gif")
        self.images["floor4_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "floor4_0.gif")
        self.images["floor4_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "floor4_1.gif")
        self.images["floor5_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "floor5_0.gif")
        self.images["floor5_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "floor5_1.gif")
        self.images["floor6_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "floor6_0.gif")
        self.images["floor6_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "floor6_1.gif")
        self.images["floor7_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "floor7_0.gif")
        self.images["floor7_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "floor7_1.gif")
        self.images["floor8_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "floor8_0.gif")
        self.images["floor8_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "floor8_1.gif")
        self.images["floor9_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "floor9_0.gif")
        self.images["floor9_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "floor9_1.gif")
        self.images["g_mov"] = PhotoImage(file=DATA_IMAGES_EDITOR + "g_mov.gif")
        self.images["grass1_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "grass1_0.gif")
        self.images["grass1_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "grass1_1.gif")
        self.images["grass2_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "grass2_0.gif")
        self.images["grass2_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "grass2_1.gif")
        self.images["grass3_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "grass3_0.gif")
        self.images["grass3_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "grass3_1.gif")
        self.images["grass4_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "grass4_0.gif")
        self.images["grass4_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "grass4_1.gif")
        self.images["grass5_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "grass5_0.gif")
        self.images["grass5_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "grass5_1.gif")
        self.images["grass6_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "grass6_0.gif")
        self.images["grass6_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "grass6_1.gif")
        self.images["grass7_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "grass7_0.gif")
        self.images["grass7_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "grass7_1.gif")
        self.images["grass8_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "grass8_0.gif")
        self.images["grass8_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "grass8_1.gif")
        self.images["grass9_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "grass9_0.gif")
        self.images["grass9_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "grass9_1.gif")
        self.images["grava1_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "grava1_0.gif")
        self.images["grava1_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "grava1_1.gif")
        self.images["grava2_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "grava2_0.gif")
        self.images["grava2_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "grava2_1.gif")
        self.images["grava3_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "grava3_0.gif")
        self.images["grava3_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "grava3_1.gif")
        self.images["group"] = DATA_ICONS + "group.ico"
        self.images["ice1_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "ice1_0.gif")
        self.images["ice1_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "ice1_1.gif")
        self.images["ice2_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "ice2_0.gif")
        self.images["ice2_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "ice2_1.gif")
        self.images["ice3_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "ice3_0.gif")
        self.images["ice3_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "ice3_1.gif")
        self.images["ladrillo1_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "ladrillo1_0.gif")
        self.images["ladrillo1_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "ladrillo1_1.gif")
        self.images["ladrillo2_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "ladrillo2_0.gif")
        self.images["ladrillo2_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "ladrillo2_1.gif")
        self.images["ladrillo3_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "ladrillo3_0.gif")
        self.images["ladrillo3_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "ladrillo3_1.gif")
        self.images["ladrillo4_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "ladrillo4_0.gif")
        self.images["ladrillo4_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "ladrillo4_1.gif")
        self.images["lava1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "lava1.gif")
        self.images["lava2"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "lava2.gif")
        self.images["lava3"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "lava3.gif")
        self.images["lightbulb_add"] = DATA_ICONS + "lightbulb_add.ico"
        self.images["lightning"] = DATA_ICONS + "lightning.ico"
        self.images["longtext"] = PhotoImage(file=DATA_IMAGES_EDITOR + "longtext.gif")
        self.images["longtext_ico"] = DATA_ICONS + "longtext.ico"
        self.images["mapeditoricon"] = DATA_ICONS + "mapeditor.ico"
        self.images["mapinfo"] = DATA_ICONS + "mapinfo.ico"
        self.images["minushp"] = PhotoImage(file=DATA_IMAGES_EDITOR + "minushp.gif")
        self.images["minushp_ico"] = DATA_ICONS + "minushp.ico"
        self.images["minusmana"] = PhotoImage(file=DATA_IMAGES_EDITOR + "minusman.gif")
        self.images["minusmana_ico"] = DATA_ICONS + "minusmana.ico"
        self.images["move"] = PhotoImage(file=DATA_IMAGES_EDITOR + "move.gif")
        self.images["move_ico"] = DATA_ICONS + "move.ico"
        self.images["mute"] = PhotoImage(file=DATA_IMAGES_EDITOR + "mute.gif")
        self.images["mute_ico"] = DATA_ICONS + "mute.ico"
        self.images["nether1_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "nether1_0.gif")
        self.images["nether1_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "nether1_1.gif")
        self.images["nether2_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "nether2_0.gif")
        self.images["nether2_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "nether2_1.gif")
        self.images["nether3_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "nether3_0.gif")
        self.images["nether3_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "nether3_1.gif")
        self.images["nether4_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "nether4_0.gif")
        self.images["nether4_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "nether4_1.gif")
        self.images["nether5_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "nether5_0.gif")
        self.images["nether5_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "nether5_1.gif")
        self.images["new_object"] = DATA_ICONS + "new_object.ico"
        self.images["noneterrain"] = PhotoImage(file=DATA_IMAGES_EDITOR + "noneterrain.gif")
        self.images["nopass"] = PhotoImage(file=DATA_IMAGES_EDITOR + "nopass.gif")
        self.images["nopass_ico"] = DATA_ICONS + "nopass.ico"
        self.images["nopassalert"] = PhotoImage(file=DATA_IMAGES_EDITOR + "nopassalert.gif")
        self.images["nopassalert_ico"] = DATA_ICONS + "nopassalert.ico"
        self.images["object"] = PhotoImage(file=DATA_IMAGES_EDITOR + "object.gif")
        self.images["object_ico"] = DATA_ICONS + "object.ico"
        self.images["pantano1_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pantano1_0.gif")
        self.images["pantano1_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pantano1_1.gif")
        self.images["pantano2_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pantano2_0.gif")
        self.images["pantano2_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pantano2_1.gif")
        self.images["pass"] = PhotoImage(file=DATA_IMAGES_EDITOR + "pass.gif")
        self.images["pass_ico"] = DATA_ICONS + "pass.ico"
        self.images["pavimento10_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pavimento10_0.gif")
        self.images["pavimento10_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pavimento10_1.gif")
        self.images["pavimento11_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pavimento11_0.gif")
        self.images["pavimento11_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pavimento11_1.gif")
        self.images["pavimento1_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pavimento1_0.gif")
        self.images["pavimento1_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pavimento1_1.gif")
        self.images["pavimento2_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pavimento2_0.gif")
        self.images["pavimento2_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pavimento2_1.gif")
        self.images["pavimento3_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pavimento3_0.gif")
        self.images["pavimento3_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pavimento3_1.gif")
        self.images["pavimento4_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pavimento4_0.gif")
        self.images["pavimento4_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pavimento4_1.gif")
        self.images["pavimento5_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pavimento5_0.gif")
        self.images["pavimento5_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pavimento5_1.gif")
        self.images["pavimento6_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pavimento6_0.gif")
        self.images["pavimento6_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pavimento6_1.gif")
        self.images["pavimento7_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pavimento7_0.gif")
        self.images["pavimento7_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pavimento7_1.gif")
        self.images["pavimento8_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pavimento8_0.gif")
        self.images["pavimento8_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pavimento8_1.gif")
        self.images["pavimento9_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pavimento9_0.gif")
        self.images["pavimento9_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pavimento9_1.gif")
        self.images["pisomadera1_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pisoMadera1_0.gif")
        self.images["pisomadera1_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pisoMadera1_1.gif")
        self.images["pisomadera2_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pisoMadera2_0.gif")
        self.images["pisomadera2_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pisoMadera2_1.gif")
        self.images["pisomadera3_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pisoMadera3_0.gif")
        self.images["pisomadera3_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pisoMadera3_1.gif")
        self.images["pisomadera4_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pisoMadera4_0.gif")
        self.images["pisomadera4_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pisoMadera4_1.gif")
        self.images["pisomadera5_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pisoMadera5_0.gif")
        self.images["pisomadera5_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pisoMadera5_1.gif")
        self.images["pisomadera6_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pisoMadera6_0.gif")
        self.images["pisomadera6_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "pisoMadera6_1.gif")
        self.images["playerpos"] = PhotoImage(file=DATA_IMAGES_EDITOR + "playerpos.gif")
        self.images["plushp"] = PhotoImage(file=DATA_IMAGES_EDITOR + "plushp.gif")
        self.images["plushp_ico"] = DATA_ICONS + "plushp.ico"
        self.images["plusmana"] = PhotoImage(file=DATA_IMAGES_EDITOR + "plusmana.gif")
        self.images["plusmana_ico"] = DATA_ICONS + "plusmana.ico"
        self.images["quest"] = PhotoImage(file=DATA_IMAGES_EDITOR + "quest.gif")
        self.images["quest_ico"] = DATA_ICONS + "quest.ico"
        self.images["sand1_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "sand1_0.gif")
        self.images["sand1_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "sand1_1.gif")
        self.images["sand2_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "sand2_0.gif")
        self.images["sand2_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "sand2_1.gif")
        self.images["sand3_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "sand3_0.gif")
        self.images["sand3_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "sand3_1.gif")
        self.images["sand4_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "sand4_0.gif")
        self.images["sand4_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "sand4_1.gif")
        self.images["sand5_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "sand5_0.gif")
        self.images["sand5_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "sand5_1.gif")
        self.images["save_icon"] = DATA_ICONS + "save.ico"
        self.images["sign_ico"] = DATA_IMAGES_EDITOR + "sign_ico.ico"
        self.images["sound"] = PhotoImage(file=DATA_IMAGES_EDITOR + "sound.gif")
        self.images["sound_ico"] = DATA_ICONS + "sound.ico"
        self.images["stair_icon"] = DATA_IMAGES_EDITOR + "stair_icon.ico"
        self.images["suddendeath"] = PhotoImage(file=DATA_IMAGES_EDITOR + "suddendeath.gif")
        self.images["suddendeath_ico"] = DATA_ICONS + "suddendeath.ico"
        self.images["teleport"] = PhotoImage(file=DATA_IMAGES_EDITOR + "teleport.gif")
        self.images["teleport_ico"] = DATA_ICONS + "teleport.ico"
        self.images["text"] = PhotoImage(file=DATA_IMAGES_EDITOR + "text.gif")
        self.images["text_ico"] = DATA_ICONS + "text.ico"
        self.images["text_icon"] = DATA_ICONS + "text_icon.ico"
        self.images["text_icon"] = DATA_ICONS + "text_icon.ico"
        self.images["textfield_add"] = DATA_ICONS + "textfield_add.ico"
        self.images["trash"] = PhotoImage(file=DATA_IMAGES_EDITOR + "trash.gif")
        self.images["trash2"] = PhotoImage(file=DATA_IMAGES_EDITOR + "trash2.gif")
        self.images["trash5"] = PhotoImage(file=DATA_IMAGES_EDITOR + "trash5.gif")
        self.images["trash6"] = PhotoImage(file=DATA_IMAGES_EDITOR + "trash6.gif")
        self.images["water1_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "water1_0.gif")
        self.images["water1_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "water1_1.gif")
        self.images["water2_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "water2_0.gif")
        self.images["water2_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "water2_1.gif")
        self.images["water3_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "water3_0.gif")
        self.images["water3_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "water3_1.gif")
        self.images["water4_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "water4_0.gif")
        self.images["water4_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "water4_1.gif")
        self.images["water5_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "water5_0.gif")
        self.images["water5_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "water5_1.gif")
        self.images["water6_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "water6_0.gif")
        self.images["water6_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "water6_1.gif")
        self.images["water7_0"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "water7_0.gif")
        self.images["water7_1"] = PhotoImage(file=DATA_IMAGES_TERRAIN + "water7_1.gif")

    def inZip(self, pack):
        """
        Comprueba si la imagen a cargar esta en un zip o en un directorio
        :return: Boolean
        """
        if pack in self.packages.keys():
            return True
        return False

    @staticmethod
    def getPackage(image):
        """
        Transforma la ubicación de la imagen a un paquete
        :return: String
        """
        image = image.replace(DATA_IMAGES, "").split("/")
        image.pop()
        return "-".join(image)

    def loadIMAGE(self, image):
        """
        Función que carga una imagen de un zip si corresponde
        caso contrario retorna un string
        :param image: String del imagen a cargar
        """
        pack = self.getPackage(IMAGES[image])
        if self.inZip(pack):
            if ".gif" in IMAGES[image]:
                try:
                    self.images[image] = PhotoImage(data=self.packages[pack].read(image + ".gif"))
                except:
                    print 'Error al cargar la imagen {1}/{0}'.format(image, pack)
                    exit()
            else:
                print "TODO: NO GIF"
        else:
            self.images[image] = PhotoImage(file=IMAGES[image])

    def loadIMAGE_ITEM(self, image):
        """
        Función que carga una imagen de un item de un zip si corresponde
        caso contrario retorna un string
        :param image: String del imagen a cargar
        """
        pack = self.getPackage(IMAGES_ITEMS[image])
        self.images[image] = PhotoImage(
            data=self.packages[pack].read(image + ".gif"))


def getTileLogicNeighbor(data, j, k, logic_matrix):
    """
    Función que obtiene los nombres lógicos
    :param data: Data
    :param j: Pos X
    :param k: Pos Y
    :param logic_matrix: Matriz lógica
    :return: State list
    """
    if data != "0-0":
        if "copy" not in data:
            del_normal = [data, j, k]
            data = data.split("-")
            del_copy = data[
                           0] + "-copy(" + data[1] + "%" + str(j) + "%" + str(
                k) + ")"
            if len(data) > 2:
                del_copy += "-" + data[2]
        else:
            del_copy = data
            data = data.split("-")
            texture = data[1].replace("copy(", "").replace(")", "").split("%")
            id_texture = texture[0]
            del_normal = [
                data[0] + "-" + id_texture, int(texture[1]), int(texture[2])]
            if len(data) > 2:
                del_normal[0] = del_normal[0] + "-" + data[2]
        return del_copy, del_normal
    else:
        return "null", "null"


def delTileLogicNeighbor(data, j, k, logic_matrix, texture_matrix):
    """
    Función que elimina elementos lógicos en formato copy(id%x&y)
    :param data: Data
    :param j: Pos X
    :param k: Pos Y
    :param logic_matrix: Matriz lógica
    :param texture_matrix: Matriz de texturas
    :return: State list
    :return: void
    """
    (del_copy, del_normal) = getTileLogicNeighbor(data, j, k, logic_matrix)
    if del_copy != "null":
        for y in range(len(logic_matrix)):
            for x in range(len(logic_matrix[0])):
                if logic_matrix[y][x] == del_copy:
                    logic = logic_matrix[y][x].split("-")
                    # Si no es agua
                    if logic[0] != "4":
                        logic_matrix[y][x] = "0-0"
                    else:
                        logic_matrix[y][x] = "4-0"
                    texture_matrix[y][x] = "None"
        if logic_matrix[del_normal[1]][del_normal[2]] == del_normal[0]:
            texture_matrix[del_normal[1]][del_normal[2]] = "None"
            logic_matrix[del_normal[1]][del_normal[2]] = "0-0"


# noinspection PyShadowingBuiltins
def logicTileCorrection(data, j, k, logic_matrix, texture_matrix):
    """
    Función que inserta elementos lógicos de un tile si este cumple con el id pedido
    :param data: Data
    :param j: Pos X
    :param k: Pos Y
    :param logic_matrix: Matriz lógica
    :param texture_matrix: Matriz de texturas
    :return: void
    """
    data = data.split("-")
    id = int(data[1])
    logic = data[0] + "-copy(" + str(id) + "%" + str(j) + "%" + str(k) + ")"
    if len(data) > 2:
        logic += "-" + data[2]

    # Reviso por id
    if id in ITEM_TYPE_CROSS:
        # Superior
        try:
            logic_matrix[j - 1][k] = logic
            texture_matrix[j - 1][k] = "None"
        except:
            pass
        # Medio
        try:
            logic_matrix[j][k - 1] = logic
            texture_matrix[j][k - 1] = "None"
        except:
            pass
        try:
            logic_matrix[j][k + 1] = logic
            texture_matrix[j][k + 1] = "None"
        except:
            pass
        # Abajo
        try:
            logic_matrix[j + 1][k] = logic
            texture_matrix[j + 1][k] = "None"
        except:
            pass
    elif id in ITEM_TYPE_FULL:
        # Superior
        try:
            logic_matrix[j - 1][k] = logic
            texture_matrix[j - 1][k] = "None"
        except:
            pass
        # Medio
        try:
            logic_matrix[j][k - 1] = logic
            texture_matrix[j][k - 1] = "None"
        except:
            pass
        try:
            logic_matrix[j][k + 1] = logic
            texture_matrix[j][k + 1] = "None"
        except:
            pass
        # Abajo
        try:
            logic_matrix[j + 1][k - 1] = logic
            texture_matrix[j + 1][k - 1] = "None"
        except:
            pass
        try:
            logic_matrix[j + 1][k] = logic
            texture_matrix[j + 1][k] = "None"
        except:
            pass
        try:
            logic_matrix[j + 1][k + 1] = logic
            texture_matrix[j + 1][k + 1] = "None"
        except:
            pass
    elif id in ITEM_TYPE_FULL_A:
        # Superior
        try:
            logic_matrix[j - 1][k - 1] = logic
            texture_matrix[j - 1][k - 1] = "None"
        except:
            pass
        try:
            logic_matrix[j - 1][k] = logic
            texture_matrix[j - 1][k] = "None"
        except:
            pass
        try:
            logic_matrix[j - 1][k + 1] = logic
            texture_matrix[j - 1][k + 1] = "None"
        except:
            pass
        # Medio
        try:
            logic_matrix[j][k - 1] = logic
            texture_matrix[j][k - 1] = "None"
        except:
            pass
        try:
            logic_matrix[j][k + 1] = logic
            texture_matrix[j][k + 1] = "None"
        except:
            pass
        # Abajo
        try:
            logic_matrix[j + 1][k - 1] = logic
            texture_matrix[j + 1][k - 1] = "None"
        except:
            pass
        try:
            logic_matrix[j + 1][k] = logic
            texture_matrix[j + 1][k] = "None"
        except:
            pass
        try:
            logic_matrix[j + 1][k + 1] = logic
            texture_matrix[j + 1][k + 1] = "None"
        except:
            pass
    elif id in ITEM_TYPE_FULL_V:
        # Superior
        try:
            logic_matrix[j - 1][k] = logic
            texture_matrix[j - 1][k] = "None"
        except:
            pass
        # Medio
        try:
            logic_matrix[j][k - 1] = logic
            texture_matrix[j][k - 1] = "None"
        except:
            pass
        try:
            logic_matrix[j][k + 1] = logic
            texture_matrix[j][k + 1] = "None"
        except:
            pass
        # Abajo
        try:
            logic_matrix[j + 1][k] = logic
            texture_matrix[j + 1][k] = "None"
        except:
            pass
        try:
            logic_matrix[j + 1][k + 1] = logic
            texture_matrix[j + 1][k + 1] = "None"
        except:
            pass
    elif id in ITEM_TYPE_MEDIUM:
        # Medio
        try:
            logic_matrix[j][k - 1] = logic
            texture_matrix[j][k - 1] = "None"
        except:
            pass
        try:
            logic_matrix[j][k + 1] = logic
            texture_matrix[j][k + 1] = "None"
        except:
            pass
        # Abajo
        try:
            logic_matrix[j + 1][k - 1] = logic
            texture_matrix[j + 1][k - 1] = "None"
        except:
            pass
        try:
            logic_matrix[j + 1][k] = logic
            texture_matrix[j + 1][k] = "None"
        except:
            pass
        try:
            logic_matrix[j + 1][k + 1] = logic
            texture_matrix[j + 1][k + 1] = "None"
        except:
            pass
    elif id in ITEM_TYPE_MEDIUM_A:
        # Superior
        try:
            logic_matrix[j - 1][k - 1] = logic
            texture_matrix[j - 1][k - 1] = "None"
        except:
            pass
        try:
            logic_matrix[j - 1][k] = logic
            texture_matrix[j - 1][k] = "None"
        except:
            pass
        try:
            logic_matrix[j - 1][k + 1] = logic
            texture_matrix[j - 1][k + 1] = "None"
        except:
            pass
        # Medio
        try:
            logic_matrix[j][k - 1] = logic
            texture_matrix[j][k - 1] = "None"
        except:
            pass
        try:
            logic_matrix[j][k + 1] = logic
            texture_matrix[j][k + 1] = "None"
        except:
            pass
    elif id in ITEM_TYPE_MEDIUM_L:
        # Medio
        try:
            logic_matrix[j][k + 1] = logic
            texture_matrix[j][k + 1] = "None"
        except:
            pass
        # Abajo
        try:
            logic_matrix[j + 1][k - 1] = logic
            texture_matrix[j + 1][k - 1] = "None"
        except:
            pass
        try:
            logic_matrix[j + 1][k] = logic
            texture_matrix[j + 1][k] = "None"
        except:
            pass
        try:
            logic_matrix[j + 1][k + 1] = logic
            texture_matrix[j + 1][k + 1] = "None"
        except:
            pass
    elif id in ITEM_TYPE_MEDIUM_R:
        # Medio
        try:
            logic_matrix[j][k + 1] = logic
            texture_matrix[j][k + 1] = "None"
        except:
            pass
        # Abajo
        try:
            logic_matrix[j + 1][k - 1] = logic
            texture_matrix[j + 1][k - 1] = "None"
        except:
            pass
        try:
            logic_matrix[j + 1][k] = logic
            texture_matrix[j + 1][k] = "None"
        except:
            pass
    elif id in ITEM_TYPE_MEDIUM_S:
        # Medio
        try:
            logic_matrix[j][k - 1] = logic
            texture_matrix[j][k - 1] = "None"
        except:
            pass
        try:
            logic_matrix[j][k + 1] = logic
            texture_matrix[j][k + 1] = "None"
        except:
            pass
        # Abajo
        try:
            logic_matrix[j + 1][k] = logic
            texture_matrix[j + 1][k] = "None"
        except:
            pass
        try:
            logic_matrix[j + 1][k + 1] = logic
            texture_matrix[j + 1][k + 1] = "None"
        except:
            pass
    elif id in ITEM_TYPE_MEDIUM_T:
        # Superior
        try:
            logic_matrix[j - 1][k] = logic
            texture_matrix[j - 1][k] = "None"
        except:
            pass
        try:
            logic_matrix[j - 1][k + 1] = logic
            texture_matrix[j - 1][k + 1] = "None"
        except:
            pass
        # Medio
        try:
            logic_matrix[j][k - 1] = logic
            texture_matrix[j][k - 1] = "None"
        except:
            pass
        try:
            logic_matrix[j][k + 1] = logic
            texture_matrix[j][k + 1] = "None"
        except:
            pass
    elif id in ITEM_TYPE_MEDIUM_U:
        # Superior
        try:
            logic_matrix[j - 1][k - 1] = logic
            texture_matrix[j - 1][k - 1] = "None"
        except:
            pass
        try:
            logic_matrix[j - 1][k] = logic
            texture_matrix[j - 1][k] = "None"
        except:
            pass
        try:
            logic_matrix[j - 1][k + 1] = logic
            texture_matrix[j - 1][k + 1] = "None"
        except:
            pass
        # Medio
        try:
            logic_matrix[j][k - 1] = logic
            texture_matrix[j][k - 1] = "None"
        except:
            pass
        try:
            logic_matrix[j][k + 1] = logic
            texture_matrix[j][k + 1] = "None"
        except:
            pass
        # Abajo
        try:
            logic_matrix[j + 1][k - 1] = logic
            texture_matrix[j + 1][k - 1] = "None"
        except:
            pass
        try:
            logic_matrix[j + 1][k] = logic
            texture_matrix[j + 1][k] = "None"
        except:
            pass
    elif id in ITEM_TYPE_MEDIUM_V:
        # Superior
        try:
            logic_matrix[j - 1][k] = logic
            texture_matrix[j - 1][k] = "None"
        except:
            pass
        # Medio
        try:
            logic_matrix[j][k - 1] = logic
            texture_matrix[j][k - 1] = "None"
        except:
            pass
        try:
            logic_matrix[j][k + 1] = logic
            texture_matrix[j][k + 1] = "None"
        except:
            pass
        # Abajo
        try:
            logic_matrix[j + 1][k - 1] = logic
            texture_matrix[j + 1][k - 1] = "None"
        except:
            pass
        try:
            logic_matrix[j + 1][k] = logic
            texture_matrix[j + 1][k] = "None"
        except:
            pass
    elif id in ITEM_TYPE_SMALL:
        # Superior
        try:
            logic_matrix[j - 1][k - 1] = logic
            texture_matrix[j - 1][k - 1] = "None"
        except:
            pass
        try:
            logic_matrix[j - 1][k] = logic
            texture_matrix[j - 1][k] = "None"
        except:
            pass
        # Medio
        try:
            logic_matrix[j][k - 1] = logic
            texture_matrix[j][k - 1] = "None"
        except:
            pass
    elif id in ITEM_TYPE_SMALL_L:
        # Superior
        try:
            logic_matrix[j - 1][k] = logic
            texture_matrix[j - 1][k] = "None"
        except:
            pass
        # Medio
        try:
            logic_matrix[j][k - 1] = logic
            texture_matrix[j][k - 1] = "None"
        except:
            pass
    elif id in ITEM_TYPE_SMALL_LINE_DIAG:
        # Superior
        try:
            logic_matrix[j - 1][k - 1] = logic
            texture_matrix[j - 1][k - 1] = "None"
        except:
            pass
    elif id in ITEM_TYPE_SMALL_LINE_DOW:
        # Abajo
        try:
            logic_matrix[j + 1][k] = logic
            texture_matrix[j + 1][k] = "None"
        except:
            pass
    elif id in ITEM_TYPE_SMALL_LINE_DOWN:
        # Medio
        try:
            logic_matrix[j][k - 1] = logic
            texture_matrix[j][k - 1] = "None"
        except:
            pass
    elif id in ITEM_TYPE_SMALL_LINE_RIGHT:
        # Superior
        try:
            logic_matrix[j - 1][k] = logic
            texture_matrix[j - 1][k] = "None"
        except:
            pass
    elif id in ITEM_TYPE_SMALL_T:
        # Abajo
        try:
            logic_matrix[j + 1][k - 1] = logic
            texture_matrix[j + 1][k - 1] = "None"
        except:
            pass
        try:
            logic_matrix[j + 1][k] = logic
            texture_matrix[j + 1][k] = "None"
        except:
            pass
        try:
            logic_matrix[j + 1][k + 1] = logic
            texture_matrix[j + 1][k + 1] = "None"
        except:
            pass
    elif id in ITEM_TYPE_SMALL_Z:
        # Medio
        try:
            logic_matrix[j][k - 1] = logic
            texture_matrix[j][k - 1] = "None"
        except:
            pass
        # Abajo
        try:
            logic_matrix[j + 1][k] = logic
            texture_matrix[j + 1][k] = "None"
        except:
            pass
        try:
            logic_matrix[j + 1][k + 1] = logic
            texture_matrix[j + 1][k + 1] = "None"
        except:
            pass
