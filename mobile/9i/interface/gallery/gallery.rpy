init python:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    if persistent.replays is None:
        persistent.replays = []

    gallery = Gallery()
    gallery.transition = dissolve

    def get_replay_button_pos(i, side='left'):
        if side == 'left':
            xpos = 0.3
        else:
            xpos = 0.7

        if i == 0:
            ypos = 0.31
        if i == 1:
            ypos = 0.49
        if i == 2:
            ypos = 0.668
        if i == 3:
            ypos = 0.845
        return xpos, ypos

    from collections import OrderedDict
    gallery.buttons = OrderedDict(gallery.buttons) 
    del OrderedDict

    # 在这里添加CG
    gallery.button("1-1")
    gallery.unlock_image("rxl_cg-cg school smile")
    gallery.unlock_image("rxl_cg-cg school happy")
    gallery.unlock_image("rxl_cg-cg school surprise")
    gallery.unlock_image("rxl_cg-cg school angry")
    gallery.unlock_image("rxl_cg-cg school angry2")

    gallery.button("1-2")
    gallery.unlock_image("xz_cg-cg normal")
    gallery.unlock_image("xz_cg-cg shame")
    gallery.unlock_image("xz_cg-cg surprise")
    gallery.unlock_image("xz_cg-cg angry")
    gallery.unlock_image("xz_cg-cg happy")
    gallery.unlock_image("xz_cg-cg daze")

    gallery.button("1-3")
    gallery.unlock_image("beach-bg day beachball1")
    gallery.unlock_image("beach-bg day beachball2")
    gallery.unlock_image("beach-bg day beachball3")
    gallery.unlock_image("beach-bg huachi1")
    gallery.unlock_image("beach-bg huachi2")
    gallery.unlock_image("beach-bg huachi3")
    
    gallery.button("1-4")
    gallery.unlock_image("party-bg xiangzi")

    gallery.button("2-1")
    gallery.unlock_image("xz_cg-cg end one")
    gallery.unlock_image("xz_cg-cg end two")

    gallery.button("2-2")
    gallery.unlock_image("xz_cg-cg hsp normal")
    gallery.unlock_image("xz_cg-cg hsp happy")
    gallery.unlock_image("xz_cg-cg hsp daze")
    gallery.unlock_image("xz_cg-cg hsp sad")
    gallery.unlock_image("xz_cg-cg hsp surprise")
    gallery.unlock_image("xz_cg-cg hsp angry")

    gallery.button("2-3")
    gallery.unlock_image("xz_cg-cg gjt normal")
    gallery.unlock_image("xz_cg-cg gjt surprise")
    gallery.unlock_image("xz_cg-cg gjt daze")
    gallery.unlock_image("xz_cg-cg gjt surprise2")
    gallery.unlock_image("xz_cg-cg gjt cry1")
    gallery.unlock_image("xz_cg-cg gjt cry2")

    gallery.button("2-4")
    gallery.unlock_image("xz_memory-cg normal one")
    gallery.unlock_image("xz_memory-cg normal two")
    gallery.unlock_image("xz_memory-cg normal three")
    gallery.unlock_image("xz_memory-cg normal four")

    gallery.button("3-1")
    gallery.unlock_image("xz_cg-cg bed one")
    gallery.unlock_image("xz_cg-cg bed two")
    gallery.unlock_image("xz_cg-cg bed three")
    gallery.unlock_image("xz_cg-cg bed four")
    gallery.unlock_image("xz_cg-cg bed five")
    gallery.unlock_image("xz_cg-cg bed six")
    gallery.unlock_image("xz_cg-cg bed seven")

    gallery.button("3-2")
    gallery.unlock_image("xz_cg-cg yume end one")
    gallery.unlock_image("xz_cg-cg yume end two")

    gallery.button("3-3")
    gallery.unlock_image("lisite_cg-cg normal")
    gallery.unlock_image("lisite_cg-cg daze")
    gallery.unlock_image("lisite_cg-cg angry")
    gallery.unlock_image("lisite_cg-cg happy")
    gallery.unlock_image("lisite_cg-cg shy")
    gallery.unlock_image("lisite_cg-cg smile")
    gallery.unlock_image("lisite_cg-cg surprise")

    gallery.button("3-4")
    gallery.unlock_image("lisite_cg-cg sea1")
    gallery.unlock_image("lisite_cg-cg sea2")

    gallery.button("4-1")
    gallery.unlock_image("lisite_cg-cg cut1")
    gallery.unlock_image("lisite_cg-cg cut2")
    gallery.unlock_image("lisite_cg-cg cut3")
    gallery.unlock_image("lisite_cg-cg cut4")

    gallery.button("4-2")
    gallery.unlock_image("lisite_cg-cg head normal")
    gallery.unlock_image("lisite_cg-cg head shy")
    gallery.unlock_image("lisite_cg-cg head surprise")
    gallery.unlock_image("lisite_cg-cg head sad")

    gallery.button("4-3")
    gallery.unlock_image("lisite_cg-cg kiss")

    gallery.button("4-4")
    gallery.unlock_image("lisite_cg-cg final one")
    gallery.unlock_image("lisite_cg-cg final two")
    gallery.unlock_image("lisite_cg-cg final three")
    gallery.unlock_image("lisite_cg-cg final four")
    gallery.unlock_image("lisite_cg-cg final five")
    gallery.unlock_image("lisite_cg-cg final six")
    gallery.unlock_image("lisite_cg-cg final seven")
    gallery.unlock_image("lisite_cg-cg final eight")
    gallery.unlock_image("lisite_cg-cg final nine")

    gallery.button("5-1")
    gallery.unlock_image("lisite_cg-cg end one")
    gallery.unlock_image("lisite_cg-cg end two")

    gallery.button("5-2")
    gallery.unlock_image("aiyi_cg-cg one")
    gallery.unlock_image("aiyi_cg-cg two")
    gallery.unlock_image("aiyi_cg-cg three")
    gallery.unlock_image("aiyi_cg-cg four")
    gallery.unlock_image("aiyi_cg-cg five")

    gallery.button("5-3")
    gallery.unlock_image("ycxt_cg-cg two")
    gallery.unlock_image("ycxt_cg-cg three")
    gallery.unlock_image("ycxt_cg-cg four")
    
    gallery.button("5-4")
    gallery.unlock_image("ycxt_cg-cg nisang1")
    gallery.unlock_image("ycxt_cg-cg nisang2")
    gallery.unlock_image("ycxt_cg-cg nisang3")
    gallery.unlock_image("ycxt_cg-cg nisang4")
    gallery.unlock_image("ycxt_cg-cg nisang5")
    gallery.unlock_image("ycxt_cg-cg nisang6")

    gallery.button("6-1")
    gallery.unlock_image("party-bg xz_home one")
    gallery.unlock_image("party-bg xz_home two")

    gallery.button("6-2")
    gallery.unlock_image("shy_cg-cg one")
    gallery.unlock_image("shy_cg-cg two")
    gallery.unlock_image("shy_cg-cg three")
    gallery.unlock_image("shy_cg-cg four")
    gallery.unlock_image("shy_cg-cg five")

    gallery.button("6-3")
    gallery.unlock_image("alu_cg-cg one")
    gallery.unlock_image("alu_cg-cg two")
    gallery.unlock_image("alu_cg-cg three")
    gallery.unlock_image("alu_cg-cg four")
    gallery.unlock_image("alu_cg-cg five")
    gallery.unlock_image("alu_cg-cg six")
    gallery.unlock_image("alu_cg-cg seven")
    gallery.unlock_image("alu_cg-cg eight")
    gallery.unlock_image("alu_cg-cg nine")
    gallery.unlock_image("alu_cg-cg ten")
    gallery.unlock_image("alu_cg-cg eleven")

    gallery.button("6-4")
    gallery.unlock_image("myself_cg-cg one")
    gallery.unlock_image("myself_cg-cg two")
    gallery.unlock_image("myself_cg-cg three")
    gallery.unlock_image("myself_cg-cg four")
    gallery.unlock_image("myself_cg-cg five")

    gallery.button("7-1")
    gallery.unlock_image("tyt_cg-cg fight one")
    gallery.unlock_image("tyt_cg-cg fight two")
    gallery.unlock_image("tyt_cg-cg fight three")
    gallery.unlock_image("tyt_cg-cg fight four")
    gallery.unlock_image("tyt_cg-cg fight five")
    gallery.unlock_image("tyt_cg-cg fight six")
    gallery.unlock_image("tyt_cg-cg fight seven")
    gallery.unlock_image("tyt_cg-cg fight eight")
    gallery.unlock_image("tyt_cg-cg fight nine")

    gallery.button("7-2")
    gallery.unlock_image("tyt_cg-cg end one")
    gallery.unlock_image("tyt_cg-cg end two")
    gallery.unlock_image("tyt_cg-cg end three")

    gallery.button("7-3")
    gallery.unlock_image("kls_cg-cg normal")
    gallery.unlock_image("kls_cg-cg happy")
    gallery.unlock_image("kls_cg-cg sad")
    gallery.unlock_image("kls_cg-cg angry")

    gallery.button("7-4")
    gallery.unlock_image("lingyin_cg-cg one")
    gallery.unlock_image("lingyin_cg-cg two")
    gallery.unlock_image("lingyin_cg-cg three")

    gallery.button("8-1")
    gallery.unlock_image("lingyin_cg-cg fite one")
    gallery.unlock_image("lingyin_cg-cg fite two")
    gallery.unlock_image("lingyin_cg-cg fite three")
    gallery.unlock_image("lingyin_cg-cg fite four")
    gallery.unlock_image("lingyin_cg-cg fite five")

    gallery.button("8-2")
    gallery.unlock_image("lingyin_cg-cg final one")
    gallery.unlock_image("lingyin_cg-cg final two")
    gallery.unlock_image("lingyin_cg-cg final three")
    gallery.unlock_image("lingyin_cg-cg final four")
    gallery.unlock_image("lingyin_cg-cg final five")
    gallery.unlock_image("lingyin_cg-cg final six")

    gallery.button("8-3")
    gallery.unlock_image("lingyin_cg-cg kiss one")
    gallery.unlock_image("lingyin_cg-cg kiss two")
    gallery.unlock_image("lingyin_cg-cg kiss three")
    gallery.unlock_image("lingyin_cg-cg kiss four")

    gallery.button("8-4")
    gallery.unlock_image("yj_cg-cg normal3")
    gallery.unlock_image("yj_cg-cg daze1")
    gallery.unlock_image("yj_cg-cg daze2")
    gallery.unlock_image("yj_cg-cg sad2")
    gallery.unlock_image("yj_cg-cg sp2")

    gallery.button("9-1")
    gallery.unlock_image("yj_cg-cg rune1")
    gallery.unlock_image("yj_cg-cg rune2")
    gallery.unlock_image("yj_cg-cg rune3")
    gallery.unlock_image("yj_cg-cg rune4")
    gallery.unlock_image("yj_cg-cg rune5")
    gallery.unlock_image("yj_cg-cg rune6")

    gallery.button("9-2")
    gallery.unlock_image("yj_cg-cg bridge1")
    gallery.unlock_image("yj_cg-cg bridge2")
    gallery.unlock_image("yj_cg-cg bridge3")
    gallery.unlock_image("yj_cg-cg bridge4")
    gallery.unlock_image("yj_cg-cg bridge5")
    gallery.unlock_image("yj_cg-cg bridge6")
    gallery.unlock_image("yj_cg-cg bridge7")

    gallery.button("9-3")
    gallery.unlock_image("yj_cg-cg home1")
    gallery.unlock_image("yj_cg-cg home2")
    gallery.unlock_image("yj_cg-cg home3")
    gallery.unlock_image("yj_cg-cg home4")
    gallery.unlock_image("yj_cg-cg home5")

    gallery.button("9-4")
    gallery.unlock_image("yj_cg-cg rain one")
    gallery.unlock_image("yj_cg-cg rain two")
    gallery.unlock_image("yj_cg-cg rain three")
    gallery.unlock_image("yj_cg-cg rain four")

    gallery.button("10-1")
    gallery.unlock_image("yj_cg-cg rocket one")
    gallery.unlock_image("yj_cg-cg rocket two")
    gallery.unlock_image("yj_cg-cg rocket three")
    gallery.unlock_image("yj_cg-cg rocket four")
    gallery.unlock_image("yj_cg-cg rocket five")
    gallery.unlock_image("yj_cg-cg rocket six")
    gallery.unlock_image("yj_cg-cg rocket seven")
    gallery.unlock_image("yj_cg-cg rocket eight")
    gallery.unlock_image("yj_cg-cg rocket nine")
    gallery.unlock_image("yj_cg-cg rocket ten")
    gallery.unlock_image("yj_cg-cg rocket eleven")

    gallery.button("10-2")
    gallery.unlock_image("szl_cg-cg fight dzf1")
    gallery.unlock_image("szl_cg-cg fight dzf2")
    gallery.unlock_image("szl_cg-cg fight dzf3")
    gallery.unlock_image("szl_cg-cg fight dzf4")

    gallery.button("10-3")
    gallery.unlock_image("szl_cg-cg shop1")
    gallery.unlock_image("szl_cg-cg shop2")
    gallery.unlock_image("szl_cg-cg shop3")
    gallery.unlock_image("szl_cg-cg shop4")
    gallery.unlock_image("szl_cg-cg shop5")
    gallery.unlock_image("szl_cg-cg shop6")
    gallery.unlock_image("szl_cg-cg shop7")
    gallery.unlock_image("szl_cg-cg shop8")

    gallery.button("10-4")
    gallery.unlock_image("szl_cg-cg room1")
    gallery.unlock_image("szl_cg-cg room2")
    gallery.unlock_image("szl_cg-cg room3")
    gallery.unlock_image("szl_cg-cg room4")
    gallery.unlock_image("szl_cg-cg room5")
    gallery.unlock_image("szl_cg-cg room6")
    gallery.unlock_image("szl_cg-cg room7")
    gallery.unlock_image("szl_cg-cg room8")
    gallery.unlock_image("szl_cg-cg room9")
    gallery.unlock_image("szl_cg-cg room10")
    gallery.unlock_image("szl_cg-cg room11")
    gallery.unlock_image("szl_cg-cg room12")
    gallery.unlock_image("szl_cg-cg room13")
    gallery.unlock_image("szl_cg-cg room14")
    gallery.unlock_image("szl_cg-cg room15")
    gallery.unlock_image("szl_cg-cg room16")
    gallery.unlock_image("szl_cg-cg room17")
    gallery.unlock_image("szl_cg-cg room18")
    gallery.unlock_image("szl_cg-cg room19")
    gallery.unlock_image("szl_cg-cg room20")
    gallery.unlock_image("szl_cg-cg room21")
    gallery.unlock_image("szl_cg-cg room22")
    gallery.unlock_image("szl_cg-cg room23")
    gallery.unlock_image("szl_cg-cg room24")
    gallery.unlock_image("szl_cg-cg room25")

    gallery.button("11-1")
    gallery.unlock_image("szl_cg-cg fight dzf5")
    gallery.unlock_image("szl_cg-cg fight dzf6")
    gallery.unlock_image("szl_cg-cg fight dzf7")
    gallery.unlock_image("szl_cg-cg fight dzf8")
    gallery.unlock_image("szl_cg-cg fight dzf9")

    gallery.button("11-2")
    gallery.unlock_image("szl_cg-cg game1")
    gallery.unlock_image("szl_cg-cg game2")
    gallery.unlock_image("szl_cg-cg game3")
    gallery.unlock_image("szl_cg-cg game4")
    gallery.unlock_image("szl_cg-cg game5")
    gallery.unlock_image("szl_cg-cg game6")
    gallery.unlock_image("szl_cg-cg game7")
    gallery.unlock_image("szl_cg-cg game8")
    gallery.unlock_image("szl_cg-cg game9")
    gallery.unlock_image("szl_cg-cg game10")
    gallery.unlock_image("szl_cg-cg game11")

    gallery.button("11-3")
    gallery.unlock_image("liuli_cg-cg rocket one")
    gallery.unlock_image("liuli_cg-cg rocket two")
    gallery.unlock_image("liuli_cg-cg rocket three")
    gallery.unlock_image("liuli_cg-cg rocket four")

    gallery.button("11-4")
    gallery.unlock_image("liuli_cg-cg center normal")
    gallery.unlock_image("liuli_cg-cg center happy")
    gallery.unlock_image("liuli_cg-cg center shy")
    gallery.unlock_image("liuli_cg-cg center sp")
    gallery.unlock_image("liuli_cg-cg center sad")

    gallery.button("12-1")
    gallery.unlock_image("liuli_cg-cg city one")
    gallery.unlock_image("liuli_cg-cg city two")
    gallery.unlock_image("liuli_cg-cg city three")
    gallery.unlock_image("liuli_cg-cg city four")

    gallery.button("12-2")
    gallery.unlock_image("liuli_cg-cg tower one")
    gallery.unlock_image("liuli_cg-cg tower two")
    gallery.unlock_image("liuli_cg-cg tower three")

    gallery.button("12-3")
    gallery.unlock_image("liuli_cg-cg fight sad2")
    gallery.unlock_image("liuli_cg-cg fight daze2")
    gallery.unlock_image("liuli_cg-cg fight angry2")
    gallery.unlock_image("liuli_cg-cg fight angry3")

    gallery.button("12-4")
    gallery.unlock_image("liuli_cg-cg fight end1")
    gallery.unlock_image("liuli_cg-cg fight end2")
    gallery.unlock_image("liuli_cg-cg fight end3")
    gallery.unlock_image("liuli_cg-cg fight end4")
    gallery.unlock_image("liuli_cg-cg fight end5")

    gallery.button("13-1")
    gallery.unlock_image("liuli_cg-cg fight end6")
    gallery.unlock_image("liuli_cg-cg fight end7")
    gallery.unlock_image("liuli_cg-cg fight end8")
    gallery.unlock_image("liuli_cg-cg fight end6_2")

    gallery.button("13-2")
    gallery.unlock_image("liuli_cg-cg motian1")
    gallery.unlock_image("liuli_cg-cg motian2")
    gallery.unlock_image("liuli_cg-cg motian3")
    gallery.unlock_image("liuli_cg-cg motian4")

    gallery.button("13-3")
    gallery.unlock_image("liuli_cg-cg space1")
    gallery.unlock_image("liuli_cg-cg space2")
    gallery.unlock_image("liuli_cg-cg space3")
    gallery.unlock_image("liuli_cg-cg space4")
    gallery.unlock_image("liuli_cg-cg space22")
    gallery.unlock_image("liuli_cg-cg space23")
    gallery.unlock_image("liuli_cg-cg space24")
    gallery.unlock_image("liuli_cg-cg space25")
    gallery.unlock_image("liuli_cg-cg space26")

    gallery.button("13-4")
    gallery.unlock_image("liuli_cg-cg space31")
    gallery.unlock_image("liuli_cg-cg space32")
    gallery.unlock_image("liuli_cg-cg space33")
    gallery.unlock_image("liuli_cg-cg space34")

    gallery.button("14-1")
    gallery.unlock_image("lhx_cg-cg xizao1")
    gallery.unlock_image("lhx_cg-cg xizao2")
    gallery.unlock_image("lhx_cg-cg xizao3")
    gallery.unlock_image("lhx_cg-cg xizao4")
    gallery.unlock_image("lhx_cg-cg xizao5")

    gallery.button("14-2")
    gallery.unlock_image("lhx_cg-cg fight1")
    gallery.unlock_image("lhx_cg-cg fight2")
    gallery.unlock_image("lhx_cg-cg fight3")
    gallery.unlock_image("lhx_cg-cg fight4")

    gallery.button("14-3")
    gallery.unlock_image("lhx_cg-cg touch1")
    gallery.unlock_image("lhx_cg-cg touch2")
    gallery.unlock_image("lhx_cg-cg touch3")
    gallery.unlock_image("lhx_cg-cg touch4")
    gallery.unlock_image("lhx_cg-cg touch5")
    gallery.unlock_image("lhx_cg-cg touch6")

    gallery.button("14-4")
    gallery.unlock_image("lhx_cg-cg street1")
    gallery.unlock_image("lhx_cg-cg street2")
    gallery.unlock_image("lhx_cg-cg street3")

    gallery.button("15-1")
    gallery.unlock_image("lhx_cg-cg final one")
    gallery.unlock_image("lhx_cg-cg final two")
    gallery.unlock_image("lhx_cg-cg final three")
    gallery.unlock_image("lhx_cg-cg final four")
    gallery.unlock_image("lhx_cg-cg final five")
    gallery.unlock_image("lhx_cg-cg final six")
    gallery.unlock_image("lhx_cg-cg final seven")
    gallery.unlock_image("lhx_cg-cg final eight")
    gallery.unlock_image("lhx_cg-cg final nine")

    gallery.button("15-2")
    gallery.unlock_image("lhx_cg-cg final ten")
    gallery.unlock_image("lhx_cg-cg final eleven")
    gallery.unlock_image("lhx_cg-cg final twelve")

    gallery.button("15-3")
    gallery.unlock_image("lhx_cg-cg school one")
    gallery.unlock_image("lhx_cg-cg school two")
    gallery.unlock_image("lhx_cg-cg school three")
    gallery.unlock_image("lhx_cg-cg school four")
    
    gallery.button("15-4")
    gallery.unlock_image("lisite_cg-cg street normal")
    gallery.unlock_image("lisite_cg-cg street happy")
    gallery.unlock_image("lisite_cg-cg street angry")

    gallery.button("16-1")
    gallery.unlock_image("lisite_cg-cg meidou one")
    gallery.unlock_image("lisite_cg-cg meidou two")
    gallery.unlock_image("lisite_cg-cg meidou three")
    gallery.unlock_image("lisite_cg-cg meidou four")
    gallery.unlock_image("lisite_cg-cg meidou five")
    gallery.unlock_image("lisite_cg-cg meidou six")
    gallery.unlock_image("lisite_cg-cg meidou seven")
    gallery.unlock_image("lisite_cg-cg meidou eight")
    gallery.unlock_image("lisite_cg-cg meidou nine")
    gallery.unlock_image("lisite_cg-cg meidou ten")

    gallery.button("16-2")
    gallery.unlock_image("myself_cg-cg space one")
    gallery.unlock_image("myself_cg-cg space two")
    gallery.unlock_image("myself_cg-cg space three")

    gallery.button("16-3")
    gallery.unlock_image("lisite_cg-cg end xuejian1")
    gallery.unlock_image("lisite_cg-cg end xuejian2")
    gallery.unlock_image("lisite_cg-cg end xuejian3")
    gallery.unlock_image("lisite_cg-cg end xuejian4")
    gallery.unlock_image("lisite_cg-cg end xuejian5")
    gallery.unlock_image("lisite_cg-cg end xuejian6")

    gallery.button("16-4")
    gallery.unlock_image("street-bg klns party")

    gallery.button("17-1")
    gallery.unlock_image("xfe_cg-cg bridge normal")
    gallery.unlock_image("xfe_cg-cg bridge happy")
    gallery.unlock_image("xfe_cg-cg bridge daze")
    gallery.unlock_image("xfe_cg-cg bridge sad")
    gallery.unlock_image("xfe_cg-cg bridge angry")
    
    gallery.button("17-2")
    gallery.unlock_image("xfe_cg-cg memory0")
    gallery.unlock_image("xfe_cg-cg memory1")
    gallery.unlock_image("xfe_cg-cg memory2")
    gallery.unlock_image("xfe_cg-cg memory3")

    gallery.button("17-3")
    gallery.unlock_image("xfe_cg-cg memory4")
    gallery.unlock_image("xfe_cg-cg memory6")
    gallery.unlock_image("xfe_cg-cg memory7")
    gallery.unlock_image("xfe_cg-cg memory8")
    gallery.unlock_image("xfe_cg-cg memory10")

    gallery.button("17-4")
    gallery.unlock_image("xfe_cg-cg touch1")
    gallery.unlock_image("xfe_cg-cg touch2")
    gallery.unlock_image("xfe_cg-cg touch3")
    gallery.unlock_image("xfe_cg-cg touch4")
    gallery.unlock_image("xfe_cg-cg touch5")
    gallery.unlock_image("xfe_cg-cg touch6")
    gallery.unlock_image("xfe_cg-cg touch7")

    gallery.button("18-1")
    gallery.unlock_image("jsqd_cg-cg bed1")
    gallery.unlock_image("jsqd_cg-cg bed2")

    gallery.button("18-2")
    gallery.unlock_image("jsqd_cg-cg yume1")
    gallery.unlock_image("jsqd_cg-cg yume2")
    gallery.unlock_image("jsqd_cg-cg yume3")
    gallery.unlock_image("jsqd_cg-cg yume4")

    gallery.button("18-3")
    gallery.unlock_image("xfe_cg-cg memory one")
    gallery.unlock_image("xfe_cg-cg memory two")
    gallery.unlock_image("xfe_cg-cg memory three")
    gallery.unlock_image("xfe_cg-cg memory four")
    gallery.unlock_image("xfe_cg-cg memory five")
    gallery.unlock_image("xfe_cg-cg memory six")
    gallery.unlock_image("xfe_cg-cg memory seven")
    gallery.unlock_image("xfe_cg-cg memory eight")
    gallery.unlock_image("xfe_cg-cg memory nine")

    gallery.button("18-4")
    gallery.unlock_image("xfe_cg-cg tree one")
    gallery.unlock_image("xfe_cg-cg tree two")
    gallery.unlock_image("xfe_cg-cg tree three")
    gallery.unlock_image("xfe_cg-cg tree four")

    gallery.button("19-1")
    gallery.unlock_image("xfe_cg-cg end one")
    gallery.unlock_image("xfe_cg-cg end two")
    gallery.unlock_image("xfe_cg-cg end three")
    gallery.unlock_image("xfe_cg-cg end four")

    gallery.button("19-2")
    gallery.unlock_image("xfe_cg-cg end touch one")
    gallery.unlock_image("xfe_cg-cg end touch two")
    gallery.unlock_image("xfe_cg-cg end touch three")
    gallery.unlock_image("xfe_cg-cg end touch four")
    gallery.unlock_image("xfe_cg-cg end touch five")

    gallery.button("19-3")
    gallery.unlock_image("xfe_cg-cg end kiss one")
    gallery.unlock_image("xfe_cg-cg end kiss two")

    gallery.button("19-4")
    gallery.unlock_image("xfe_cg-cg leave one")
    gallery.unlock_image("xfe_cg-cg leave two")
    gallery.unlock_image("xfe_cg-cg leave three")
    gallery.unlock_image("xfe_cg-cg leave four")
    gallery.unlock_image("xfe_cg-cg leave five")
    gallery.unlock_image("xfe_cg-cg leave own")

    gallery.button("20-1")
    gallery.unlock_image("xfe_cg-cg final1")
    gallery.unlock_image("xfe_cg-cg final2")
    gallery.unlock_image("xfe_cg-cg final3")
    gallery.unlock_image("xfe_cg-cg final4")
    gallery.unlock_image("xfe_cg-cg final5")
    gallery.unlock_image("xfe_cg-cg final6")

    gallery.button("20-2")
    gallery.unlock_image("jsqd_cg-cg end three")
    gallery.unlock_image("jsqd_cg-cg end four")
    gallery.unlock_image("jsqd_cg-cg end five")

    gallery.button("20-3")
    gallery.unlock_image("xfe_cg-cg noodles one")
    gallery.unlock_image("xfe_cg-cg noodles two")
    gallery.unlock_image("xfe_cg-cg noodles three")
    gallery.unlock_image("xfe_cg-cg noodles four")
    gallery.unlock_image("xfe_cg-cg noodles five")

    gallery.button("20-4")
    gallery.unlock_image("jsqd_cg-cg end one")
    gallery.unlock_image("jsqd_cg-cg end two")

    gallery.button("21-1")
    gallery.unlock_image("xz_cg-cg yume xuejian one")
    gallery.unlock_image("xz_cg-cg yume xuejian two")
    gallery.unlock_image("xz_cg-cg yume xuejian three")
    gallery.unlock_image("xz_cg-cg yume xuejian four")


label movie1:
    $ suppress_overlay = True
    $ mouse_visible = False
    scene black
    show movie onlayer texture
    play movie "video/first_op.mnp4"
    $ renpy.music.play("video/first_op.mp3", synchro_start='movie')
    pause 115.0
    stop movie
    hide movie
    stop music fadeout 1.0
    $ renpy.end_replay()
    $ suppress_overlay = False
    $ mouse_visible = True
    return


label movie2:
    $ suppress_overlay = True
    $ mouse_visible = False
    scene black
    show movie onlayer texture
    play movie "video/second_op.mp4"
    $ renpy.music.play("video/second_op.mp3", synchro_start='movie')
    pause 136.0
    stop movie
    hide movie
    stop music fadeout 1.0
    $ renpy.end_replay()
    $ suppress_overlay = False
    $ mouse_visible = True
    return


# label movie3:
#     $ suppress_overlay = True
#     $ mouse_visible = False
#     scene black
#     show movie onlayer texture
#     play movie "video/third_op.webm" noloop
#     $ renpy.music.play("video/third_op.mp3", synchro_start='movie')
#     pause 134.0
#     stop movie
#     hide movie
#     stop music fadeout 1.0
#     $ renpy.end_replay()
#     $ suppress_overlay = False
#     $ mouse_visible = True
#     return


# label movie4:
#     $ suppress_overlay = True
#     $ mouse_visible = False
#     scene black
#     show movie onlayer texture
#     play movie "video/forth_op.mp4" noloop
#     $ renpy.music.play("video/forth_op.mp3", synchro_start='movie')
#     pause 106.0
#     stop movie
#     hide movie
#     stop music fadeout 1.0
#     $ renpy.end_replay()
#     $ suppress_overlay = False
#     $ mouse_visible = True
#     return


screen gallery():
    tag menu
    modal True
    zorder + 2

    on "show" action Function(renpy.show, "gallery_bg", behind=["menu"], layer="screens")
    on "replace" action Function(renpy.show, "gallery_bg", behind=["menu"], layer="screens")

    transform at gallery_menu_inter:
        imagebutton auto "9i/interface/gallery/book_%s.png":
            action NullAction()
            xcenter pscale(981.25) 
            ycenter pscale(850.75)
            ysize scale(390) 
            xsize scale(555)

        textbutton _("{#gallery}Event and Movie\nGallery") style "gallery_go_events_button":
            action Show("gallery_events")

        imagebutton auto "9i/interface/gallery/audio_%s.png":
            action NullAction()
            xcenter pscale(302.25) 
            ycenter pscale(520.75)
            ysize scale(713) 
            xsize scale(540)

        textbutton _("{#gallery}Music Gallery") style "gallery_go_music_button":
            action Show("musicroom")

        vbox style_prefix "gallery_menu":
            textbutton _("Return"):
                action [
                    Function(renpy.hide, "gallery_bg", layer="screens"),
                    MenuReturn()
                ]
                keysym "game_menu"

    label _("{#gallery}GALLERY") style "caption_label" at caption_inter


init:
    transform gallery_menu_inter:
        on show:
            alpha 0
            linear 0.5 alpha 1
        on replace:
            alpha 0
            0.5
            linear 0.5 alpha 1
        on replaced:
            linear 0.5 alpha 0
        on hide:
            linear 0.5 alpha 0

    image gallery_bg:
        "9i/interface/gallery/bg.png"
        imagescale(1080)
        on show:
            alpha 0
            linear 0.5 alpha 1
        on hide:
            linear 0.5 alpha 0

    image gallery_bg blur:
        imagescale(1080)
        on show:
            "9i/interface/gallery/bg blur.png"
            alpha 0
            linear 0.5 alpha 1
        on replace:
            "9i/interface/gallery/bg.png"
            alpha 1
            "9i/interface/gallery/bg blur.png" with dissolve
            0.5
        on hide:
            linear 0.5 alpha 0
        on replaced:
            "9i/interface/gallery/bg blur.png"
            "9i/interface/gallery/bg.png" with dissolve
            0.5
            alpha 0

    style gallery_button_text is text:
        xcenter 0.5 text_align 0.5 ycenter 0.5
        font "9i/fonts/FOT-SkipStd-B.otf"
        line_spacing scale(6) line_leading scale(6) size scale(38)
        color "#69717c"
        outlines [
            (scale(6.0), "#00000003"),
            (scale(5.0), "#00000007"),
            (scale(4.0), "#0000000b"),
            (scale(3.0), "#0000000f"),
            (scale(2.0), "#00000013"),
            (scale(1.0), "#00000017")
        ]
        hover_color "#fff"
        hover_outlines [
            (scale(6.0), "#ffd43d0f"),
            (scale(5.0), "#ffd43d17"),
            (scale(4.0), "#ffd43d1f"),
            (scale(3.0), "#ffd43d2f"),
            (scale(2.0), "#ffd43d3f"),
            (scale(1.0), "#ffd43d5f")
        ]

    style gallery_go_music_button is default:
        xcenter pscale(302.25) ycenter pscale(520.75)
        ysize scale(713) xsize scale(540)
        hover_background imagescale(1080)(child="9i/interface/gallery/audio_hover.png")
        activate_sound "9i/interface/click1.ogg"
        hover_sound "9i/interface/click2.ogg"

    style gallery_go_music_button_text is gallery_button_text:
        xcenter pscale(258.625) ycenter pscale(511.625)

    style gallery_go_events_button is default:
        xcenter pscale(981.25) ycenter pscale(850.75)
        ysize scale(390) xsize scale(555)
        hover_background imagescale(1080)(child="9i/interface/gallery/book_hover.png")
        activate_sound "9i/interface/click1.ogg"
        hover_sound "9i/interface/click2.ogg"

    style gallery_go_events_button_text is gallery_button_text:
        xcenter pscale(267.95) ycenter pscale(179.475)

    style gallery_bar is default:
        ysize scale(18)
        left_bar Solid("#fff")
        right_bar BasicFrame("#0000", "#fff")

    style gallery_menu_vbox is vbox:
        xalign 1.0 ypos pscale(1041) yanchor 1.0
        spacing scale(9)

    style gallery_menu_button is default:
        xsize scale(387) yminimum scale(91) xpadding scale(54)
        background Frame(
            imagescale(1080)(child="9i/interface/gallery/button.png"),
            top=scale(8))
        activate_sound "9i/interface/click1.ogg"
        hover_sound "9i/interface/click2.ogg"
        
    style gallery_menu_button_text is text:
        xalign 1.0 text_align 1.0 ycenter 0.5
        font "9i/fonts/FOT-ChiaroStd-B.otf"
        line_spacing scale(6) line_leading scale(6) size scale(35)
        color "#fff"
        outlines [
            (scale(9.0), "#00000003"),
            (scale(8.0), "#00000007"),
            (scale(7.0), "#0000000b"),
            (scale(6.0), "#0000000f"),
            (scale(5.0), "#00000013"),
            (scale(4.0), "#00000017"),
            (scale(3.0), "#0000001f"),
            (scale(2.0), "#00000027"),
            (scale(1.0), "#0000002f")
        ]
        hover_outlines [
            (scale(9.0), "#8baeff03"),
            (scale(8.0), "#8baeff07"),
            (scale(7.0), "#8baeff0b"),
            (scale(6.0), "#8baeff0f"),
            (scale(5.0), "#8baeff1f"),
            (scale(4.0), "#8baeff2f"),
            (scale(3.0), "#8baeff3f"),
            (scale(2.0), "#8baeff57"),
            (scale(1.0), "#8baeff7f")
        ]


screen gallery_events(page=1, mode='events', animation=None):
    tag menu    
    modal True
    zorder + 2

    python:
        from __future__ import division

        from math import ceil

        if mode != "movies":
            page_buttons = gallery.buttons.keys()[8 * (page - 1):8 * page]
            page_total = int(ceil(len(gallery.button_list) / 8))
        else:
            # 在这里添加Movie
            total_pages = [
                ("movie1", "9i/interface/gallery/thumbs/movie-first.png", "video/first_op.mp4"),
                ("movie2", "9i/interface/gallery/thumbs/movie-second.png", "video/second_op.mp4")
            ]
            page_buttons = total_pages[2 * (page - 1):2 * page]
            page_total = int(ceil(len(total_pages) / 2))

        del ceil

    if animation == "left":
        on "replace" action [
            Function(
                renpy.show, "gallery_book flip_left", behind=["menu"], layer="screens"),
            Play(channel="audio", file="9i/interface/68224__xtyl33__paper-double.ogg")
        ]
    elif animation == "right":
        on "replace" action [
            Function(
                renpy.show, "gallery_book flip_right", behind=["menu"], layer="screens"),
            Play(channel="audio", file="9i/interface/68224__xtyl33__paper-double.ogg")
        ]
    else:
        on "replace" action [
            Function(renpy.show, "gallery_bg blur", behind=["menu"], layer="screens"),
            Function(renpy.show, "gallery_book", at_list=[gallery_book_inter], zorder=+1, layer="screens"),
            Play(channel="audio", file="9i/interface/paper_slide.ogg")
        ]

    frame style_prefix "gallery_events" at gallery_book_contents_inter(page):
        if mode != "movies":
            vbox style "gallery_events_left_vbox":
                for idx, item in enumerate(page_buttons[:4], start=1):
                    add gallery.make_button(
                        name=item,
                        unlocked=imagescale(1080)(
                            child=Image(
                                "9i/interface/gallery/images/{}.png".format(item),
                                xcenter=0.5,
                                ycenter=0.5)),
                        locked="gallery_event_thumb locked",
                        hover_border="gallery_event_thumb hover",
                        style="gallery_events_button")
            vbox style "gallery_events_right_vbox":
                for idx, item in enumerate(page_buttons[4:8], start=5):
                    add gallery.make_button(
                        name=item,
                        unlocked=imagescale(1080)(
                            child=Image(
                                "9i/interface/gallery/images/{}.png".format(item),
                                xcenter=0.5,
                                ycenter=0.5)),
                        locked="gallery_event_thumb locked",
                        hover_border="gallery_event_thumb hover",
                        style="gallery_events_button")
            frame style_prefix "gallery_page":
                if page > 1:
                    button style "gallery_page_left_button":
                        action Show("gallery_events", page=page - 1, animation="left")
                text "[page] / [page_total]"
                if page < page_total:
                    button style "gallery_page_right_button":
                        action Show("gallery_events", page=page + 1, animation="right")
            for i in range(4):
                $ label = "label"
                if page % 2 == 0:
                    $ tmp_page = 2 * page
                    $ label += str(tmp_page) + "_" + str(i+1)
                    $ side = 'right'
                else:
                    $ tmp_page = 2 * page - 1
                    $ label += str(tmp_page) + "_" + str(i+1)
                    $ side = 'left'

                if label in persistent.replays:
                    $ xpos, ypos = get_replay_button_pos(i, side)
                    if len(page_buttons) == 1:
                        $ ypos = 0.58
                    imagebutton auto "9i/interface/gallery/replay%s.png" action [MyReplay(label, tmp_page), Play(channel="audio", file="9i/interface/68224__xtyl33__paper-double.ogg")] xanchor 0.5 yanchor 0.5 pos (xpos, ypos)
        else:
            vbox style "gallery_events_movie_left_vbox" style_prefix "gallery_events_movie":
                for idx, (obj, thumb_path, movie_path) in enumerate(page_buttons[:1], start=1):
                    button:
                        background imagescale(1080)(child=thumb_path)
                        insensitive_background imagescale(1080)(child="9i/interface/gallery/thumbs/movie locked.png")
                        action Function(renpy.call_replay, obj)
                        sensitive renpy.seen_audio(movie_path)
            if len(page_buttons) > 1:
                vbox style "gallery_events_movie_right_vbox" style_prefix "gallery_events_movie":
                    for idx, (obj, thumb_path, movie_path) in enumerate(page_buttons[1:2], start=2):
                        button:
                            background imagescale(1080)(child=thumb_path)
                            insensitive_background imagescale(1080)(child="9i/interface/gallery/thumbs/movie locked.png")
                            action Function(renpy.call_replay, obj)
                            sensitive renpy.seen_audio(movie_path)
            frame style_prefix "gallery_page":
                if page > 1:
                    button style "gallery_page_left_button":
                        action Show("gallery_events", page=page - 1, mode="movies", animation="left")
                text "[page] / [page_total]"
                if page < page_total:
                    button style "gallery_page_right_button":
                        action Show("gallery_events", page=page + 1, mode="movies", animation="right") 

        vbox style_prefix "gallery_menu":
            if mode != "movies":
                textbutton _("{#gallery}Movies"):
                    action [
                        Show("gallery_events", page=1, mode="movies", animation="left"),
                        Play(channel="audio", file="9i/interface/68224__xtyl33__paper-double.ogg")
                    ]
            else:
                textbutton _("{#gallery}Event CG"):
                    action [
                        Show("gallery_events", page=1, animation="right"),
                        Play(channel="audio", file="9i/interface/68224__xtyl33__paper-double.ogg")
                    ]
            textbutton _("Return"):
                action [
                    Show("gallery"),
                    Function(renpy.hide, "gallery_book", layer="screens"),
                    Play(channel="audio", file="9i/interface/paper_slide_reverse.ogg")
                ]
                keysym "game_menu"

    if mode != "movies":
        label _("{#gallery}EVENT CG") style "caption_label" at caption_inter
    else:
        label _("{#gallery}MOVIES") style "caption_label" at caption_inter


init:
    transform gallery_book_inter:
        on show:
            subpixel True yoffset scale(1620)
            ease 0.5 yoffset scale(0)
        on hide:
            subpixel True
            0.5
            ease 0.5 yoffset scale(1620)

    transform gallery_book_contents_inter(page):
        on show:
            alpha 0
            0.5
            linear 0.5 alpha 1
        on update:
            alpha 0
            0.5
            linear 0.5 alpha 1
        on replace:
            alpha 0
            0.5
            linear 0.5 alpha 1
        on start:
            alpha 0
            0.5
            linear 0.5 alpha 1
        on hide:
            linear 0.5 alpha 0
        on replaced:
            linear 0.5 alpha 0

    image gallery_book:
        "9i/interface/gallery/book/book.png"
        xcenter pscale(961.5) yalign 1.0
        imagescale(1080)

    image gallery_book flip_left:
        block:
            contains:
                "gallery_book"
                xoffset pscale(-1.5)
            contains:
                "9i/interface/gallery/book/01.png"
                subpixel True xpos pscale(963.75) xanchor 1.0 ypos pscale(1045.5) yanchor 1.0 xoffset pscale(-3)
                imagescale(1080)
                0.1
                "9i/interface/gallery/book/02.png"
                xpos pscale(964.5) ypos pscale(1045.5)
                0.1
                "9i/interface/gallery/book/03.png"
                xpos pscale(964.5) ypos pscale(1045.5)
                0.1
                "9i/interface/gallery/book/04.png"
                xpos pscale(956.25) xanchor 0.0 ypos pscale(1045.5)
                0.1
                "9i/interface/gallery/book/05.png"
                xpos pscale(957) ypos pscale(1045.5)
                0.1
                "9i/interface/gallery/book/06.png"
                xpos pscale(959.25) ypos pscale(1045.5)
                0.1
            0.6
        "gallery_book"

    image gallery_book flip_right:
        block:
            contains:
                "gallery_book"
                xoffset pscale(-1.5)
            contains:
                "9i/interface/gallery/book/06.png"
                subpixel True xpos pscale(959.25) xanchor 0.0 ypos pscale(1045.5) yanchor 1.0 xoffset pscale(-3)
                imagescale(1080)
                0.1
                "9i/interface/gallery/book/05.png"
                xpos pscale(957) ypos pscale(1045.5)
                0.1
                "9i/interface/gallery/book/04.png"
                xpos pscale(956.25) ypos pscale(1045.5)
                0.1
                "9i/interface/gallery/book/03.png"
                xpos pscale(964.5) xanchor 1.0 ypos pscale(1045.5)
                0.1
                "9i/interface/gallery/book/02.png"
                xpos pscale(964.5) ypos pscale(1045.5)
                0.1
                "9i/interface/gallery/book/01.png"
                xpos pscale(963.75) ypos pscale(1045.5)
                0.1
            0.6
        "gallery_book"

    image gallery_event_thumb locked = imagescale(1080)(
        child=Image(
            "9i/interface/gallery/images/event locked.png",
            xcenter=0.5,
            ycenter=0.5))

    image gallery_event_thumb hover = imagescale(1080)(
        child=Image(
            "9i/interface/gallery/images/event hover.png",
            xcenter=0.5,
            ycenter=0.5))

    style gallery_events_frame is default:
        xcenter 0.5 ycenter 0.5
        ysize scale(1040) xsize scale(1513)

    style gallery_events_left_vbox is vbox:
        xcenter pscale(448.5) ycenter pscale(513)
        spacing scale(39)

    style gallery_events_right_vbox is gallery_events_left_vbox:
        xcenter pscale(1069.5)
        
    style gallery_events_button is default:
        xcenter 0.5 ycenter 0.5
        ysize scale(150) xsize scale(525)

    style gallery_events_movie_left_vbox is gallery_events_left_vbox:
        xcenter pscale(445.5)

    style gallery_events_movie_right_vbox is gallery_events_right_vbox:
        xcenter pscale(1065)

    style gallery_events_movie_button is gallery_events_button:
        xcenter 0.5 ycenter 0.5
        ysize scale(303) xsize scale(488)
        hover_foreground imagescale(1080)(
            child=Image(
                "9i/interface/gallery/thumbs/movie hover.png",
                xcenter=0.5,
                ycenter=0.5))

    style gallery_page_frame is default:
        xcenter pscale(1150.5) ycenter pscale(90)
        xsize scale(474) ysize scale(80)
        background imagescale(1080)(child="9i/interface/gallery/event page base.png")

    style gallery_page_text is text:
        xcenter pscale(255) ycenter 0.5
        font "9i/fonts/FOT-ChiaroStd-B.otf"
        size scale(36)
        color "#ffe4ae"
        outlines [
            (scale(6.0), "#c2980607"),
            (scale(4.5), "#c298060b"),
            (scale(3.0), "#c2980613"),
            (scale(1.5), "#c298061f")
        ]

    style gallery_page_left_button is default:
        xcenter pscale(115.5) ycenter 0.5
        child imagescale(1080)(child="9i/interface/gallery/page left.png")

    style gallery_page_right_button is gallery_page_left_button:
        xpos pscale(389.25) ycenter 0.5
        child imagescale(1080)(child="9i/interface/gallery/page right.png")


















