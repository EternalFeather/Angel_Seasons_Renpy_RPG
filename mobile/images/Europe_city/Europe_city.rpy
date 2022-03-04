define set Europe_city:
    path 'images/Europe_city'
    python:
        layer_move('b1', 2200)
        layer_move('b2', 2200)
        layer_move('m1', 1849)
        layer_move('m2', 1849)
        layer_move('f1', 1280)
        layer_move('f2', 1280)
    piece bg onlayer b1:
        subpixel True
        xcenter 0.5
        ycenter 0.5
        zoom scale(1.18)
    piece mobm01 optional at mobpos(x=770, y=1218, zoom=1.18) onlayer b1
    piece mobm02 optional at mobpos(x=1226, y=1256, zoom=1.18) onlayer b1
    piece mobm03 optional at mobpos(x=1544, y=1336, zoom=1.18) onlayer b1
    piece mobm04 optional at mobpos(x=1660, y=1202, zoom=1.18) onlayer b1
    piece mobm05 optional at mobpos(x=1802, y=1264, zoom=1.18) onlayer b1
    piece mobm06 optional at mobpos(x=1912, y=1234, zoom=1.18) onlayer b1
    piece mobm07 optional at mobpos(x=3156, y=1266, zoom=1.18) onlayer b1
    piece mobm08 optional at mobpos(x=3551, y=1224, zoom=1.18) onlayer b1
    piece mobm09 optional at mobpos(x=3138, y=1266, zoom=1.18) onlayer b1
    piece mobm10 optional at mobpos(x=3090, y=1166, zoom=1.18) onlayer b1
    piece mobm11 optional at mobpos(x=2828, y=1146, zoom=1.18) onlayer b1
    piece mobd1 optional at mobpos(x=708, y=1228, zoom=1.18) onlayer b1
    piece mobd2 optional at mobpos(x=908, y=1350, zoom=1.18) onlayer b1
    piece mobd3 optional at mobpos(x=1252, y=1338, zoom=1.18) onlayer b1
    piece mobd4 optional at mobpos(x=3050, y=1292, zoom=1.18) onlayer b1
    piece mobd5 optional at mobpos(x=3498, y=1272, zoom=1.18) onlayer b1
    piece mobd6 optional at mobpos(x=3328, y=1286, zoom=1.18) onlayer b1
    piece mobd7 optional at mobpos(x=3062, y=1168, zoom=1.18) onlayer b1
    piece mobd8 optional at mobpos(x=1580, y=1248, zoom=1.18) onlayer b1
    piece mobe1 optional at mobpos(x=708, y=1228, zoom=1.18) onlayer b1
    piece mobe2 optional at mobpos(x=908, y=1350, zoom=1.18) onlayer b1
    piece mobe3 optional at mobpos(x=1252, y=1338, zoom=1.18) onlayer b1
    piece mobe4 optional at mobpos(x=3050, y=1292, zoom=1.18) onlayer b1
    piece mobe5 optional at mobpos(x=3498, y=1272, zoom=1.18) onlayer b1
    piece mobe6 optional at mobpos(x=3328, y=1286, zoom=1.18) onlayer b1
    piece mobe7 optional at mobpos(x=3062, y=1168, zoom=1.18) onlayer b1
    piece mobe8 optional at mobpos(x=1580, y=1248, zoom=1.18) onlayer b1
    piece mobn1 optional at mobpos(x=3282, y=1270, zoom=1.18) onlayer b1
    piece mobn2 optional at mobpos(x=2998, y=1138, zoom=1.18) onlayer b1
    piece mobn3 optional at mobpos(x=1408, y=1238, zoom=1.18) onlayer b1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
