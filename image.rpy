
define slowdissolve = Dissolve(1.0)
define slowedissolve = Dissolve(2.0)
define slowerdissolve = Dissolve(3.0)
define ultraslowdissolve = Dissolve(6.0)

define trans01 = ImageDissolve("trans/rule_3.png", 1.0)
define trans02 = ImageDissolve("trans/rule_1.png", 1.0)
define trans03 = ImageDissolve("trans/rule_16.png", 1.0)
define trans04 = ImageDissolve("trans/rule_11.png", 1.0)
define trans05 = ImageDissolve("trans/rule_13.png", 1.0)
define trans06 = ImageDissolve("trans/rule_6.png", 1.0)

image third16 grayscale = im.Grayscale("images/third16.png")
image third20 grayscale = im.Grayscale("images/third20.png")
image third22 grayscale = im.Grayscale("images/third22.png")
image third30 grayscale = im.Grayscale("images/third30.png")

define narrator = Character(None, kind=nvl, window_xpos=250, window_ypos=60, ctc="ctc")
define pcenter = Character(None, kind=nvl, window_xpos=400, window_ypos=320, ctc="ctc")
define pcenter3 = Character(None, kind=nvl, window_xpos=320, window_ypos=320, ctc="ctc")
define pcenter5 = Character(None, kind=nvl, window_xpos=250, window_ypos=230, ctc="ctc")
define pcenter51 = Character(None, kind=nvl, window_xpos=250, window_ypos=280, ctc="ctc")
define pcenter0 = Character(None, kind=nvl, window_xpos=300, window_ypos=150, ctc="ctc")


define d = Character(_(' '), color="#ffffff", ctc="ctc_animation", ctc_position="fixed")
define q = Character(_('？？？'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define xz = Character(_('青木翔子'), who_outlines=[(2,"#fffbeb")], color="#c7bb70", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define xz_h01 = Character(_('青木翔子'), who_outlines=[(2,"#fffbeb")], color="#c7bb70", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/xiangzi_happy01.png", xalign=0.06, yalign=1.0))
define m = Character(_('神野凉'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define xz_s01 = Character(_('青木翔子'), who_outlines=[(2,"#fffbeb")], color="#c7bb70", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/xiangzi_surprise01.png", xalign=0.06, yalign=1.0))
define xz_a01 = Character(_('青木翔子'), who_outlines=[(2,"#fffbeb")], color="#c7bb70", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/xiangzi_anger01.png", xalign=0.06, yalign=1.0))
define t = Character(_('天使'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define xz_h02 = Character(_('青木翔子'), who_outlines=[(2,"#fffbeb")], color="#c7bb70", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/xiangzi_happy02.png", xalign=0.06, yalign=1.0))
define xz_n01 = Character(_('青木翔子'), who_outlines=[(2,"#fffbeb")], color="#c7bb70", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/xiangzi_normal01.png", xalign=0.06, yalign=1.0))
define l = Character(_('日向怜'), who_outlines=[(2,"#833a43")], color="#d95f64", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define l_a01 = Character(_('日向怜'), who_outlines=[(2,"#833a43")], color="#d95f64", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/rxl_anger01.png", xalign=0.11, yalign=1.0))
define l_s01 = Character(_('日向怜'), who_outlines=[(2,"#833a43")], color="#d95f64", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/rxl_sad01.png", xalign=0.11, yalign=1.0))
define xz_h03 = Character(_('青木翔子'), who_outlines=[(2,"#fffbeb")], color="#c7bb70", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/xiangzi_happy03.png", xalign=0.06, yalign=1.0))
define z = Character(_('一诚总司'), who_outlines=[(2,"#495d44")], color="#a79968", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define o = Character(_('翔子母亲'), who_outlines=[(2,"#3b4430")], color="#6d743a", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define f = Character(_('翔子父亲'), who_outlines=[(2,"#46342a")], color="#956d5a", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define xz_h04 = Character(_('青木翔子'), who_outlines=[(2,"#fffbeb")], color="#c7bb70", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/xiangzi_happy04.png", xalign=0.06, yalign=1.0))
define xz_ns01 = Character(_('青木翔子'), who_outlines=[(2,"#fffbeb")], color="#c7bb70", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/xiangzi_nanshou01.png", xalign=0.06, yalign=1.0))
define n = Character(_('迷之少女'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define j = Character(_('流氓甲'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define p = Character(_('地痞老大'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define s = Character(_('莉斯特·F·艾斯特雷亚'), who_outlines=[(2,"#c3c5e5")], color="#fcfff4", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define s_n01 = Character(_('莉斯特·F·艾斯特雷亚'), who_outlines=[(2,"#c3c5e5")], color="#fcfff4", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/my_normal01.png", xalign=0.03, yalign=1.0))
define xz_w01 = Character(_('青木翔子'), who_outlines=[(2,"#fffbeb")], color="#c7bb70", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/xiangzi_warry01.png", xalign=0.06, yalign=1.0))
define xz_w02 = Character(_('青木翔子'), who_outlines=[(2,"#fffbeb")], color="#c7bb70", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/xiangzi_warry02.png", xalign=0.06, yalign=1.0))
define xz_h05 = Character(_('青木翔子'), who_outlines=[(2,"#fffbeb")], color="#c7bb70", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/xiangzi_happy05.png", xalign=0.06, yalign=1.0))
define l_h01 = Character(_('日向怜'), who_outlines=[(2,"#833a43")], color="#d95f64", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/rxl_happy01.png", xalign=0.11, yalign=1.0))
define s_w01 = Character(_('莉斯特·F·艾斯特雷亚'), who_outlines=[(2,"#c3c5e5")], color="#fcfff4", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/my_warry01.png", xalign=0.03, yalign=1.0))
define c = Character(_('老师'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define h = Character(_('众人'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define s_su01 = Character(_('莉斯特·F·艾斯特雷亚'), who_outlines=[(2,"#c3c5e5")], color="#fcfff4", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/my_surprise01.png", xalign=0.03, yalign=1.0))
define s_h01 = Character(_('莉斯特·F·艾斯特雷亚'), who_outlines=[(2,"#c3c5e5")], color="#fcfff4", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/my_happy01.png", xalign=0.03, yalign=1.0))
define s_a01 = Character(_('莉斯特·F·艾斯特雷亚'), who_outlines=[(2,"#c3c5e5")], color="#fcfff4", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/my_anger01.png", xalign=0.03, yalign=1.0))
define xz_n02 = Character(_('青木翔子'), who_outlines=[(2,"#fffbeb")], color="#c7bb70", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/xiangzi_normal02.png", xalign=0.06, yalign=1.0))
define s_n02 = Character(_('莉斯特·F·艾斯特雷亚'), who_outlines=[(2,"#c3c5e5")], color="#fcfff4", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/my_normal02.png", xalign=0.03, yalign=1.0))
define l_w01 = Character(_('日向怜'), who_outlines=[(2,"#833a43")], color="#d95f64", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/rxl_warry01.png", xalign=0.11, yalign=1.0))
define s_a02 = Character(_('莉斯特·F·艾斯特雷亚'), who_outlines=[(2,"#c3c5e5")], color="#fcfff4", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/my_anger02.png", xalign=0.03, yalign=1.0))
define s_w02 = Character(_('莉斯特·F·艾斯特雷亚'), who_outlines=[(2,"#c3c5e5")], color="#fcfff4", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/my_warry02.png", xalign=0.03, yalign=1.0))
define s_s01 = Character(_('莉斯特·F·艾斯特雷亚'), who_outlines=[(2,"#c3c5e5")], color="#fcfff4", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/my_sad01.png", xalign=0.03, yalign=1.0))
define s_g01 = Character(_('莉斯特·F·艾斯特雷亚'), who_outlines=[(2,"#c3c5e5")], color="#fcfff4", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/my_ganga01.png", xalign=0.03, yalign=1.0))
define z_h01 = Character(_('一诚总司'), who_outlines=[(2,"#495d44")], color="#a79968", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/yc_happy01.png", xalign=0.09, yalign=1.0))
define l_h02 = Character(_('日向怜'), who_outlines=[(2,"#833a43")], color="#d95f64", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/rxl_happy02.png", xalign=0.11, yalign=1.0))
define xz_h06 = Character(_('青木翔子'), who_outlines=[(2,"#fffbeb")], color="#c7bb70", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/xiangzi_happy06.png", xalign=0.06, yalign=1.0))
define z_n01 = Character(_('一诚总司'), who_outlines=[(2,"#495d44")], color="#a79968", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/yc_normal01.png", xalign=0.09, yalign=1.0))
define xz_a02 = Character(_('青木翔子'), who_outlines=[(2,"#fffbeb")], color="#c7bb70", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/xiangzi_anger02.png", xalign=0.06, yalign=1.0))
define l_w02 = Character(_('日向怜'), who_outlines=[(2,"#833a43")], color="#d95f64", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/rxl_warry02.png", xalign=0.11, yalign=1.0))
define xz_sa01 = Character(_('青木翔子'), who_outlines=[(2,"#fffbeb")], color="#c7bb70", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/xiangzi_sad01.png", xalign=0.08, yalign=1.0))
define z_h02 = Character(_('一诚总司'), who_outlines=[(2,"#495d44")], color="#a79968", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/yc_happy02.png", xalign=0.09, yalign=1.0))
define l_h03 = Character(_('日向怜'), who_outlines=[(2,"#833a43")], color="#d95f64", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/rxl_happy03.png", xalign=0.11, yalign=1.0))
define xz_c01 = Character(_('青木翔子'), who_outlines=[(2,"#fffbeb")], color="#c7bb70", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/xiangzi_cry01.png", xalign=0.08, yalign=1.0))
define s_s02 = Character(_('莉斯特·F·艾斯特雷亚'), who_outlines=[(2,"#c3c5e5")], color="#fcfff4", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/my_sad02.png", xalign=0.03, yalign=1.0))
define xz_w03 = Character(_('青木翔子'), who_outlines=[(2,"#fffbeb")], color="#c7bb70", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/xiangzi_warry03.png", xalign=0.06, yalign=1.0))
define x = Character(_('希菲尔·M·克里斯蒂恩'), who_outlines=[(2,"#da97c3")], color="#f9faf8", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define a = Character(_('日向爱衣'), who_outlines=[(2,"#843217")], color="#cf5c4d", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define qb = Character(_('泽村千波'), who_outlines=[(2,"#88cc90")], color="#e8ffbb", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define xt = Character(_('一诚小桃'), who_outlines=[(2,"#405c73")], color="#7b99b0", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define xt_sm01 = Character(_('一诚小桃'), who_outlines=[(2,"#405c73")], color="#7b99b0", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/xt_smile01.png", xalign=0.06, yalign=1.0))
define xt_sl01 = Character(_('一诚小桃'), who_outlines=[(2,"#405c73")], color="#7b99b0", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/xt_shuijiao01.png", xalign=0.06, yalign=1.0))
define ls = Character(_('千川老师'),  color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define ay_sm01 = Character(_('日向爱衣'), who_outlines=[(2,"#843217")], color="#cf5c4d", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/ay_smile01.png", xalign=0.06, yalign=1.0))
define yj = Character(_('植澄友加'), who_outlines=[(2,"#e05b76")], color="#ffb9ab", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define lhx = Character(_('立花希'), who_outlines=[(2,"#b9c3c2")], color="#edf4f5", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define lnn = Character(_('小桃的奶奶'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define ll = Character(_('花山院琉璃'), who_outlines=[(2,"#e4c03c")], color="#ffecad", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define szl = Character(_('水之濑凛'), who_outlines=[(2,"#7c52a2")], color="#c6a3da", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define ll_su01 = Character(_('花山院琉璃'), who_outlines=[(2,"#e4c03c")], color="#ffecad", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/ll_surprise01.png", xalign=0.0, yalign=1.0))
define tyt = Character(_('藤原瞳'), who_outlines=[(2,"#591635")], color="#8a2352", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define ly = Character(_('青木铃音'), who_outlines=[(2,"#c6ab83")], color="#fffaec", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define tyt_a01 = Character(_('藤原瞳'), who_outlines=[(2,"#591635")], color="#8a2352", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/tyt_anger01.png", xalign=0.08, yalign=1.0))
define tyt_su01 = Character(_('藤原瞳'), who_outlines=[(2,"#591635")], color="#8a2352", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/tyt_surprise01.png", xalign=0.08, yalign=1.0))
define xz_sa02 = Character(_('青木翔子'), who_outlines=[(2,"#fffbeb")], color="#c7bb70", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/xiangzi_sad02.png", xalign=0.06, yalign=1.0))
define wyh = Character(_('南星万夜花'), who_outlines=[(2,"#746069")], color="#96817d", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define shy = Character(_('圣护院'), who_outlines=[(2,"#7f3f66")], color="#d19a9e", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define szl_n01 = Character(_('水之濑凛'), who_outlines=[(2,"#7c52a2")], color="#c6a3da", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/szl_normal01.png", xalign=0.04, yalign=1.0))
define wyh_su01 = Character(_('南星万夜花'), who_outlines=[(2,"#746069")], color="#96817d", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/wyh_surprise01.png", xalign=0.03, yalign=1.0))
define wyh_h01 = Character(_('南星万夜花'), who_outlines=[(2,"#746069")], color="#96817d", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/wyh_happy01.png", xalign=0.03, yalign=1.0))
define tyt_s01 = Character(_('藤原瞳'), who_outlines=[(2,"#591635")], color="#8a2352", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/tyt_sad02.png", xalign=0.08, yalign=1.0))
define hz = Character(_('学生会会长'), who_outlines=[(2,"#685500")], color="#bca24c", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define al = Character(_('阿露毕蕾欧'), who_outlines=[(2,"#ff5fd0")], color="#ff8cfe", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define x_sa01 = Character(_('希菲尔·M·克里斯蒂恩'), who_outlines=[(2,"#da97c3")], color="#f9faf8", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/xfe_sad02b.png", xalign=0.03, yalign=1.0))
define yj_sa01 = Character(_('植澄友加'), who_outlines=[(2,"#e05b76")], color="#ffb9ab", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/yj_sad01.png", xalign=0.03, yalign=1.0))
define by = Character(_('白羽'), who_outlines=[(2,"#30362c")], color="#687460", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define xing = Character(_('姬神千冬'), who_outlines=[(2,"#ef6679")], color="#b04f6a", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define xing_sa03 = Character(_('姬神千冬'), who_outlines=[(2,"#ef6679")], color="#b04f6a", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/xing_sad03.png", xalign=0.01, yalign=1.0))
define xing_sm01 = Character(_('姬神千冬'), who_outlines=[(2,"#ef6679")], color="#b04f6a", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/xing_smile01.png", xalign=0.01, yalign=1.0))
define tyt_sa02 = Character(_('藤原瞳'), who_outlines=[(2,"#591635")], color="#8a2352", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/tyt_sad02.png", xalign=0.08, yalign=1.0))
define k = Character(_('克丽丝·X·米尔克利玛'), who_outlines=[(2,"#545554")], color="#e5d24a", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define dh = Character(_('神野大和'), who_outlines=[(2,"#b14234")], color="#652118", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define yj_sm01 = Character(_('植澄友加'), who_outlines=[(2,"#e05b76")], color="#ffb9ab", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/yj_smile03.png", xalign=0.00, yalign=1.0))
define yey_su01 = Character(_('幼儿园老师'), color="#ffb9ab", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/yey_surprise01.png", xalign=0.06, yalign=1.0))
define lhx_wu01 = Character(_('立花希'), who_outlines=[(2,"#b9c3c2")], color="#edf4f5", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/lhx_wunai01.png", xalign=0.06, yalign=1.0))
define yj_wu03 = Character(_('植澄友加'), who_outlines=[(2,"#e05b76")], color="#ffb9ab", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/yj_wunai03.png", xalign=0.03, yalign=1.0))
define yj_wu01 = Character(_('植澄友加'), who_outlines=[(2,"#e05b76")], color="#ffb9ab", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/yj_wunai01.png", xalign=0.01, yalign=1.0))
define lhx_su01 = Character(_('立花希'), who_outlines=[(2,"#b9c3c2")], color="#edf4f5", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/lhx_surprise01.png", xalign=0.06, yalign=1.0))
define lhx_no01 = Character(_('立花希'), who_outlines=[(2,"#b9c3c2")], color="#edf4f5", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/lhx_normal03.png", xalign=0.06, yalign=1.0))
define yj_sm01 = Character(_('植澄友加'), who_outlines=[(2,"#e05b76")], color="#ffb9ab", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/yj_smile06.png", xalign=0.00, yalign=1.0))
define yj_su01 = Character(_('植澄友加'), who_outlines=[(2,"#e05b76")], color="#ffb9ab", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/yj_surprise06.png", xalign=0.00, yalign=1.0))
define lhx_k01 = Character(_('立花希'), who_outlines=[(2,"#b9c3c2")], color="#edf4f5", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/lhx_kun01.png", xalign=0.06, yalign=1.0))
define tyt_h01 = Character(_('藤原瞳'), who_outlines=[(2,"#591635")], color="#8a2352", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/tyt_happy01.png", xalign=0.08, yalign=1.0))
define x_no01 = Character(_('希菲尔·M·克里斯蒂恩'), who_outlines=[(2,"#da97c3")], color="#f9faf8", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/xfe_normal01b.png", xalign=0.03, yalign=1.0))
define sn = Character(_('诗乃'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define xz_n03 = Character(_('青木翔子'), who_outlines=[(2,"#fffbeb")], color="#c7bb70", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/xiangzi_normal03.png", xalign=0.2, yalign=1.0))
define szl_wn01 = Character(_('水之濑凛'), who_outlines=[(2,"#7c52a2")], color="#c6a3da", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/szl_wunai01.png", xalign=0.04, yalign=1.0))

define ltl_qh01 = Character(_('？？？'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/ltl_happy01.png", xalign=0.08, yalign=1.0))
define ltl_qs01 = Character(_('？？？'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/ltl_sad01.png", xalign=0.08, yalign=1.0))
define ltl_qn01 = Character(_('？？？'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/ltl_normal01.png", xalign=0.08, yalign=1.0))
define ltl_qs02 = Character(_('？？？'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/ltl_sad02.png", xalign=0.08, yalign=1.0))
define ltl_su01 = Character(_('？？？'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/ltl_su01.png", xalign=0.08, yalign=1.0))
define ltl_wa01 = Character(_('？？？'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/ltl_warry01.png", xalign=0.08, yalign=1.0))
define ltl_happy01 = Character(_('相马廉太郎'), who_outlines=[(2,"#ffffff")], color="#d1864c", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/ltl_happy01.png", xalign=0.08, yalign=1.0))
define ltl_su02 = Character(_('相马廉太郎'), who_outlines=[(2,"#ffffff")], color="#d1864c", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/ltl_su01.png", xalign=0.08, yalign=1.0))
define ltl_no02 = Character(_('相马廉太郎'), who_outlines=[(2,"#ffffff")], color="#d1864c", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/ltl_normal01.png", xalign=0.08, yalign=1.0))
define ltl_sad02 = Character(_('相马廉太郎'), who_outlines=[(2,"#ffffff")], color="#d1864c", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/ltl_sad01.png", xalign=0.08, yalign=1.0))
define ltl_warry02 = Character(_('相马廉太郎'), who_outlines=[(2,"#ffffff")], color="#d1864c", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/ltl_warry01.png", xalign=0.08, yalign=1.0))
define ltl_zihao01 = Character(_('相马廉太郎'), who_outlines=[(2,"#ffffff")], color="#d1864c", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/ltl_zihao01.png", xalign=0.08, yalign=1.0))
define together01 = Character(_('相马廉太郎·六连悠人'), who_outlines=[(2,"#ffffff")], color="#d1864c", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/ltl_happy01.png", xalign=0.08, yalign=1.0))
define together02 = Character(_('相马廉太郎·六连悠人'), who_outlines=[(2,"#ffffff")], color="#d1864c", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/ltl_normal01.png", xalign=0.08, yalign=1.0))
define together03 = Character(_('相马廉太郎·六连悠人'), who_outlines=[(2,"#ffffff")], color="#d1864c", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/ltl_sad01.png", xalign=0.08, yalign=1.0))
define y = Character(_('六连悠人'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define ltl = Character(_('相马廉太郎'), who_outlines=[(2,"#ffffff")], color="#d1864c", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define xnh = Character(_('小女孩'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define mother = Character(_('母亲'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define girl = Character(_('女孩'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define lr1 = Character(_('路人1'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define lr2 = Character(_('路人2'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define girl_anger01 = Character(_('女孩'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/mm_anger01.png", xalign=0.08, yalign=1.0))
define ltl_anger01 = Character(_('相马廉太郎'), who_outlines=[(2,"#ffffff")], color="#d1864c", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/ltl_anger01.png", xalign=0.08, yalign=1.0))
define girl_wunai01 = Character(_('女孩'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/mm_wunai01.png", xalign=0.08, yalign=1.0))
define dz = Character(_('店主'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define zh = Character(_('醉汉'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define ltl_hap01 = Character(_('相马廉太郎'),  who_outlines=[(2,"#ffffff")], color="#d1864c", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/ltl_happy01.png", xalign=0.08, yalign=1.0))
define ltl_sa01 = Character(_('相马廉太郎'),  who_outlines=[(2,"#ffffff")], color="#d1864c", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/ltl_sad01.png", xalign=0.08, yalign=1.0))
define ltl_nor01 = Character(_('相马廉太郎'),  who_outlines=[(2,"#ffffff")], color="#d1864c", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/ltl_normal01.png", xalign=0.08, yalign=1.0))
define ltl_sa02 = Character(_('相马廉太郎'),  who_outlines=[(2,"#ffffff")], color="#d1864c", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/ltl_sad02.png", xalign=0.08, yalign=1.0))
define ltl_sup01 = Character(_('相马廉太郎'),  who_outlines=[(2,"#ffffff")], color="#d1864c", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/ltl_su01.png", xalign=0.08, yalign=1.0))
define ltl_war01 = Character(_('相马廉太郎'),  who_outlines=[(2,"#ffffff")], color="#d1864c", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/ltl_warry01.png", xalign=0.08, yalign=1.0))
define ltl_sa03 = Character(_('相马廉太郎'),  who_outlines=[(2,"#ffffff")], color="#d1864c", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/ltl_sad03.png", xalign=0.08, yalign=1.0))
define tsy = Character(_('提示音'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define nz = Character(_('神秘男子'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define jc = Character(_('警察'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define sc = Character(_('矢吹美羽'), who_outlines=[(2,"#ffffff")], color="#c1535f", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define nf = Character(_('女诱拐犯'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define dh_normal04 = Character(_('相神野大和'), who_outlines=[(2,"#b14234")], color="#652118", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/dh_normal04.png", xalign=0.08, yalign=1.0))
define sc_surprise02 = Character(_('矢吹美羽'), who_outlines=[(2,"#ffffff")], color="#c1535f", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/mm_surprise02.png", xalign=0.08, yalign=1.0))
define sc_anger01 = Character(_('矢吹美羽'), who_outlines=[(2,"#ffffff")], color="#c1535f", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/mm_anger01.png", xalign=0.08, yalign=1.0))
define hs = Character(_('护士'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define ys = Character(_('医生'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define shs = Character(_('扇和树'), who_outlines=[(2,"#ffffff")], color="#6b8070", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define sc_warry02 = Character(_('矢吹美羽'), who_outlines=[(2,"#ffffff")], color="#c1535f", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/mm_warry02.png", xalign=0.08, yalign=1.0))
define sc_wunai03 = Character(_('矢吹美羽'), who_outlines=[(2,"#ffffff")], color="#c1535f", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/mm_wunai03.png", xalign=0.08, yalign=1.0))
define sj = Character(_('司机'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define nx = Character(_('女性'), color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define lh = Character(_('相马芦花'), who_outlines=[(2,"#ffffff")], color="#a1576e", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define lh_surprise02 = Character(_('相马芦花'), who_outlines=[(2,"#ffffff")], color="#a1576e", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/lh_surprise02.png", xalign=0.08, yalign=1.0))
define syl_normal01 = Character(_('神野凉'), who_outlines=[(2,"#ffffff")], color="#ffffff", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/syl_normal01.png", xalign=0.08, yalign=1.0))
define xm = Character(_('小埋'), who_outlines=[(2,"#ffffff")], color="#ffb1b5", ctc="ctc_animation", ctc_position="fixed", show_two_window=True)
define by_sad02 = Character(_('白羽'), who_outlines=[(2,"#30362c")], color="#687460", ctc="ctc_animation", ctc_position="fixed", show_two_window=True, show_side_image=Image("face/side/by_sad02.png", xalign=0.08, yalign=1.0))

$ snow = Snow("ui/snowflake2.png")
image snow = Snow("ui/snowflake2.png")
image Spring = "images/Spring.png"
image charxuzhang = "images/logo-xuzhang.png"
image chardiyizhang = "images/logo-diyizhang.png"
image jingtanhao = "images/jingtanhao.png"
image chardierzhang = "images/logo-dierzhang.png"
image things saoba = "images/saoba.bmp"
image things hbook = "images/hbook.bmp"
image meng02 = "images/meng02.bmp"
image meng03 = "images/meng03.bmp"
image meng04 = "images/meng04.bmp"
image chardisanzhang = "images/logo-disanzhang.png"
image ishengqi = "images/ishengqi.png"
image dunqiangjiao = "images/dunqiangjiao.png"
image Summer = "images/Summer.png"
image chardisizhang = "images/logo-disizhang.png"
image things bag = "images/bag.bmp"
image things banpai = "images/banpai.bmp"
image chardiwuzhang = "images/logo-diwuzhang.png"
image things biandang = "images/biandang.bmp"
image things shouji = "images/shouji.bmp"
image chardiliuzhang = "images/logo-diliuzhang.png"
image things zhihe = "images/zhihe.bmp"
image chardiqizhang = "images/logo-diqizhang.png"
image things xiangji = "images/xiangji.bmp"
image Autumn = "images/Autumn.png"
image chardibazhang = "images/logo-dibazhang.png"
image chardijiuzhang = "images/logo-dijiuzhang.png"
image chardishizhang = "images/logo-dishizhang.png"
image chardishiyizhang = "images/logo-dishiyizhang.png"
image Winter = "images/Winter.png"
image charzuizhongzhang = "images/logo-zuizhongzhang.png"
image charzuizhongzhang2 = "images/logo-zuizhongzhang2.png"
image title_logo2 = "images/title_logo2.png"
image logo_dierji = "images/logo_dierji.png"
image logo_dierji0 = "images/logo_dierji0.png"
image day01 = "images/day01.png"
image fan31 = "images/fan31.bmp"
image day02 = "images/day02.png"
image fan96 = "images/fan96.png"
image day03 = "images/day03.png"
image day04 = "images/day04.png"
image day05 = "images/day05.png"
image day06 = "images/day06.png"
image day07 = "images/day07.png"
image day08 = "images/day08.png"
image day09 = "images/day09.png"
image day10 = "images/day10.png"
image day11 = "images/day11.png"
image day12 = "images/day12.png"
image day13 = "images/day13.png"
image day14 = "images/day14.png"
image day15 = "images/day15.png"
image day15_2 = "images/day15_2.png"
image day15_3 = "images/day15_3.png"
image day15_4 = "images/day15_4.png"
image day16 = "images/day16.png"
image day17 = "images/day17.png"
image day18 = "images/day18.png"
image yinliao = "images/yinliao.bmp"
image caomei = "images/caomei.bmp"
image guanzi = "images/guanzi.bmp"
image qian = "images/qian.bmp"
image fan317 = "images/fan317.png"
image fan318 = "images/fan318.png"
image fan319 = "images/fan319.png"
image fan320 = "images/fan320.png"
image fan321 = "images/fan321.png"
image fan322 = "images/fan322.png"
image fan323 = "images/fan323.png"
image xingxing = "images/BG081_105_parts1.bmp"
image day19 = "images/day19.png"
image day20 = "images/day20.png"
image day21 = "images/day21.png"
image day22 = "images/day22.png"
image day23 = "images/day23.png"
image fin = "images/fin1.png"
image cut_one = "images/cut_one.png"
image cut_two = "images/cut_two.png"

image SD01 = "images/SD105A.bmp"
image SD02 = "images/SD105B.bmp"
image SD03 = "images/SD105C.bmp"

image jizhong = "ui/jizhongxian.png"

image ctc = Animation("ani/ctc/prompt1.png", .13, "ani/ctc/prompt2.png", .13, "ani/ctc/prompt3.png", .13, "ani/ctc/prompt4.png", .13, "ani/ctc/prompt5.png", .13,  "ani/ctc/prompt6.png", .13,  "ani/ctc/prompt20.png", .13,  "ani/ctc/prompt21.png", .13,  "ani/ctc/prompt22.png", .13,  "ani/ctc/prompt23.png", .13,  "ani/ctc/prompt24.png", .13,)
image hanshui = Animation("ani/hanshui/bu_effect6_N_1.bmp", .5, "ani/hanshui/bu_effect6_N_2.bmp", .5,)
image ciyan = Animation("images/SD105B2.bmp", .25, "images/SD105B3.bmp", .25,)
image ciyan2 = Animation("images/SD105C.bmp", .25, "images/SD105C1.bmp", .25,)

image syl normal01 = "face/nz/syl_normal01.png"

image xiangzi shame01 = "face/xz_wunv/xz_shame01.png"
image xiangzi nervous01 = "face/xz_wunv/xz_nervous01.png"
image xiangzi shame02 = "face/xz_wunv/xz_shame02.png"
image xiangzi anger01 = "face/xz_wunv/xz_anger01.png"
image xiangzi happy01 = "face/xz_wunv/xz_happy01.png"
image xiangzi happy02 = "face/xz_wunv/xz_happy02.png"
image xiangzi happy03 = "face/xz_wunv/xz_happy03.png"
image xiangzi happy04 = "face/xz_wunv/xz_happy04.png"
image xiangzi sad01 = "face/xz_wunv/xz_sad01.png"
image xiangzi sad02 = "face/xz_wunv/xz_sad02.png"
image xiangzi surprise01 = "face/xz_wunv/xz_surprise01.png"
image xiangzi disappointed = "face/xz_wunv/xz_disappointed.png"
image xiangzi surprise11 = "face/xz_zhongxue/xz_surprise11.png"
image xiangzi anger111 = "face/xz_zhongxue/xz_anger111.png"
image xiangzi anger112 = "face/xz_zhongxue/xz_anger112.png"
image xiangzi sad111 = "face/xz_zhongxue/xz_sad111.png"
image xiangzi sad112 = "face/xz_zhongxue/xz_sad112.png"
image xiangzi sad113 = "face/xz_zhongxue/xz_sad113.png"
image xiangzi happy111 = "face/xz_zhongxue/xz_happy111.png"
image xiangzi happy112 = "face/xz_zhongxue/xz_happy112.png"
image xiangzi surprise112 = "face/xz_zhongxue/xz_surprise112.png"
image xiangzi cry111 = "face/xz_zhongxue/xz_cry111.png"
image xiangzi xsf_sad01 = "face/xz_xsf/xz_sad01.png"
image xiangzi xsf_cry01 = "face/xz_xsf/xz_cry01.png"
image xiangzi xsf_happy01 = "face/xz_xsf/xz_happy01.png"
image xiangzi xsf_shame01 = "face/xz_xsf/xz_shame01.png"
image xiangzi xsf_surprise01 = "face/xz_xsf/xz_surprise01.png"
image xiangzi xsf_shame02 = "face/xz_xsf/xz_shame02.png"
image xiangzi xsf_happy02 = "face/xz_xsf/xz_happy02.png"
image xiangzi xsf_shame03 = "face/xz_xsf/xz_shame03.png"
image xiangzi xsf_anger01 = "face/xz_xsf/xz_anger01.png"
image xiangzi xsf_happy03 = "face/xz_xsf/xz_happy03.png"
image xiangzi xsf_smile01 = "face/xz_xsf/xz_smile01.png"
image xiangzi xsf_smile02 = "face/xz_xsf/xz_smile02.png"
image xiangzi xsf_ganga01 = "face/xz_xsf/xz_ganga01.png"
image xiangzi xsf_surprise02 = "face/xz_xsf/xz_surprise02.png"
image xiangzi xsf_sad02 = "face/xz_xsf/xz_sad02.png"
image xiangzi xsf_warry01 = "face/xz_xsf/xz_warry01.png"
image xiangzi xsf_nanshou01 = "face/xz_xsf/xz_nanshou01.png"
image xiangzi xsf_wunai01 = "face/xz_xsf/xz_wunai01.png"
image xiangzi xsf_happy04 = "face/xz_xsf/xz_happy04.png"
image xiangzi xsf_surprise03 = "face/xz_xsf/xz_surprise03.png"
image xiangzi xf_warry01 = "face/xz_xf/xz_warry01.png"
image xiangzi xf_warry02 = "face/xz_xf/xz_warry02.png"
image xiangzi xf_anger01 = "face/xz_xf/xz_anger01.png"
image xiangzi xf_anger02 = "face/xz_xf/xz_anger02.png"
image xiangzi xf_ganga01 = "face/xz_xf/xz_ganga01.png"
image xiangzi xf_surprise01 = "face/xz_xf/xz_surprise01.png"
image xiangzi xf_happy01 = "face/xz_xf/xz_happy01.png"
image xiangzi xf_anger03 = "face/xz_xf/xz_anger03.png"
image xiangzi xf_ganga02 = "face/xz_xf/xz_ganga02.png"
image xiangzi xf_anger04 = "face/xz_xf/xz_anger04.png"
image xiangzi xf_shame01 = "face/xz_xf/xz_shame01.png"
image xiangzi xf_normal01 = "face/xz_xf/xz_normal01.png"
image xiangzi xf_happy02 = "face/xz_xf/xz_happy02.png"
image xiangzi xf_surprise02 = "face/xz_xf/xz_surprise02.png"
image xiangzi yz_normal01 = "face/xz_yz/xz_normal01.png"
image xiangzi yz_surprise01 = "face/xz_yz/xz_surprise01.png"
image xiangzi yz_happy01 = "face/xz_yz/xz_happy01.png"
image xiangzi yz_shame01 = "face/xz_yz/xz_shame01.png"
image xiangzi yz_normal02 = "face/xz_yz/xz_normal02.png"
image xiangzi yz_happy02 = "face/xz_yz/xz_happy02.png"
image xiangzi yz_happy03 = "face/xz_yz/xz_happy03.png"
image xiangzi yz_warry01 = "face/xz_yz/xz_warry01.png"
image xiangzi yz_anger01 = "face/xz_yz/xz_anger01.png"
image xiangzi yz_anger02 = "face/xz_yz/xz_anger02.png"
image xiangzi yz_anger03 = "face/xz_yz/xz_anger03.png"
image xiangzi dsf_smile01 = "face/xz_dsf/xz_smile01.png"
image xiangzi dsf_surprise01 = "face/xz_dsf/xz_surprise01.png"
image xiangzi dsf_warry01 = "face/xz_dsf/xz_warry01.png"
image xiangzi dsf_normal01 = "face/xz_dsf/xz_normal01.png"
image xiangzi dsf_anger01 = "face/xz_dsf/xz_anger01.png"
image xiangzi dsf_shame01 = "face/xz_dsf/xz_shame01.png"
image xiangzi dsf_smile02 = "face/xz_dsf/xz_smile02.png"
image xiangzi dsf_anger02 = "face/xz_dsf/xz_anger02.png"
image xiangzi dsf_sad02 = "face/xz_dsf/xz_sad02.png"
image xiangzi dsf_cry01 = "face/xz_dsf/xz_cry01.png"
image xiangzi dsf_sad03 = "face/xz_dsf/xz_sad03.png"
image xiangzi dsf_happy01 = "face/xz_dsf/xz_happy01.png"
image xiangzi dsf_surprise02 = "face/xz_dsf/xz_surprise02.png"
image xiangzi dsf_normal02 = "face/xz_dsf/xz_normal02.png"
image xiangzi dsf_warry02 = "face/xz_dsf/xz_warry02.png"
image xiangzi dsf_anger03 = "face/xz_dsf/xz_anger03.png"
image xiangzi dsf_anger03b = "face/xz_dsf/xz_anger03b.png"
image xiangzi dsf_surprise03 = "face/xz_dsf/xz_surprise03.png"
image xiangzi dsf_shame01b = "face/xz_dsf/xz_shame01b.png"
image xiangzi dsf_bishi01 = "face/xz_dsf/xz_bishi01.png"
image xiangzi xf_ganga03 = "face/xz_xf/xz_ganga03.png"
image xiangzi xf_wunai01 = "face/xz_xf/xz_wunai01.png"

image cl1 class01 = "face/class/class01.png"
image cl2 class02 = "face/class/class02.png"
image cl3 class03 = "face/class/class03.png"
image cl1 class011 = "face/class/class011.png"
image cl1 class001 = "face/class/class001.png"

image bg sel = "ui/sel.bmp"

image yc normal = "face/yc/yc000.png"
image yc happy01 = "face/yc/yc_happy01.png"
image yc wunai = "face/yc/yc_wunai.png"
image yc warry01 = "face/yc/yc_warry01.png"
image yc normal02 = "face/yc/yc_normal02.png"
image ycxf normal01 = "face/yc_xf/ycxf_normal01.png"
image ycxf happy01 = "face/yc_xf/ycxf_happy01.png"
image ycxf happy02 = "face/yc_xf/ycxf_happy02.png"
image ycxf warry01 = "face/yc_xf/ycxf_warry01.png"
image ycxf sad01 = "face/yc_xf/ycxf_sad01.png"
image ycxf warry02 = "face/yc_xf/ycxf_warry02.png"
image ycxf happy03 = "face/yc_xf/ycxf_happy03.png"
image ycxf wunai01 = "face/yc_xf/ycxf_wunai01.png"
image ycyz normal01 = "face/yc_yz/ycyz_normal01.png"
image ycyz warry01 = "face/yc_yz/ycyz_warry01.png"
image ycyz happy01 = "face/yc_yz/ycyz_happy01.png"
image ycyz ganga01 = "face/yc_yz/ycyz_ganga01.png"
image ycyz happy02 = "face/yc_yz/ycyz_happy02.png"
image ycsf wunai01 = "face/yc_sf/ycsf_wunai01.png"
image ycsf happy01 = "face/yc_sf/ycsf_happy01.png"
image ycsf sad01 = "face/yc_sf/ycsf_sad01.png"
image ycsf warry01 = "face/yc_sf/ycsf_warry01.png"

image rx wunai = "face/rx/rx_wunai.png"
image rx anger01 = "face/rx/rx_anger01.png"
image rx surprise01 = "face/rx/rx_surprise01.png"
image rx anger02 = "face/rx/rx_anger02.png"
image rx happy01 = "face/rx/rx_happy01.png"
image rx anger03 = "face/rx/rx_anger03.png"
image rx surprise02 = "face/rx/rx_surprise02.png"
image rx warry01 = "face/rx/rx_warry01.png"
image rx huachi = "face/rx/rx_huachi.png"
image rxxf happy01 = "face/rx_xf/rxxf_happy01.png"
image rxxf anger01 = "face/rx_xf/rxxf_anger01.png"
image rxxf surprise01 = "face/rx_xf/rxxf_surprise01.png"
image rxxf ganga01 = "face/rx_xf/rxxf_ganga01.png"
image rxxf anger02 = "face/rx_xf/rxxf_anger02.png"
image rxxf ganga02 = "face/rx_xf/rxxf_ganga02.png"
image rxxf surprise02 = "face/rx_xf/rxxf_surprise02.png"
image rxxf cry01 = "face/rx_xf/rxxf_cry01.png"
image rxxf huachi01 = "face/rx_xf/rxxf_huachi01.png"
image rxxf happy02 = "face/rx_xf/rxxf_happy02.png"
image rxxf wunai01 = "face/rx_xf/rxxf_wunai01.png"
image rxyz happy01 = "face/rx_yz/rxyz_happy01.png"
image rxyz ganga01 = "face/rx_yz/rxyz_ganga01.png"
image rxyz anger01 = "face/rx_yz/rxyz_anger01.png"
image rxyz anger02 = "face/rx_yz/rxyz_anger02.png"
image rxyz huachi01 = "face/rx_yz/rxyz_huachi01.png"
image rxyz warry01 = "face/rx_yz/rxyz_warry01.png"
image rxxf happy03 = "face/rx_xf/rxxf_happy03.png"

image rxsf anger01 = "face/rx_sf/rxsf_anger01.png"
image rxsf anger02 = "face/rx_sf/rxsf_anger02.png"
image rxsf happy01 = "face/rx_sf/rxsf_happy01.png"
image rxsf happy02 = "face/rx_sf/rxsf_happy02.png"
image rxsf smile01 = "face/rx_sf/rxsf_smile01.png"
image rxsf smile02 = "face/rx_sf/rxsf_smile02.png"
image rxsf surprise01 = "face/rx_sf/rxsf_surprise01.png"
image rxsf surprise02 = "face/rx_sf/rxsf_surprise02.png"
image rxsf happy03 = "face/rx_sf/rxsf_happy03.png"
image rxsf wunai01 = "face/rx_sf/rxsf_wunai01.png"
image rxsf ganga01 = "face/rx_sf/rxsf_ganga01.png"
image rxsf surprise03 = "face/rx_sf/rxsf_surprise03.png"
image rxsf wunai02 = "face/rx_sf/rxsf_wunai02.png"
image rxsf ganga02 = "face/rx_sf/rxsf_ganga02.png"
image rxsf anger03 = "face/rx_sf/rxsf_anger03.png"
image rxsf smile03 = "face/rx_sf/rxsf_smile03.png"
image rxsf happy04 = "face/rx_sf/rxsf_happy04.png"

image xzm normal01 = "face/family/xzm_normal01.png"
image xzm surprise01 = "face/family/xzm_surprise01.png"
image xzm anger01 = "face/family/xzm_anger01.png"
image xzm happy01 = "face/family/xzm_happy01.png"
image xzm sad01 = "face/family/xzm_sad01.png"
image xzm tield01 = "face/family/xzm_tield01.png"
image xzf normal01 = "face/family/xzf_normal01.png"
image xzf happy01 = "face/family/xzf_happy01.png"
image xzf sad01 = "face/family/xzf_sad01.png"
image xzf anger01 = "face/family/xzf_anger01.png"
image xzf surprise01 = "face/family/xzf_surprise01.png"

image my surprise01 = "face/lisite/my_surprise01.png"
image my sad01 = "face/lisite/my_sad01.png"
image my normal01 = "face/lisite/my_normal01.png"
image my anger01 = "face/lisite/my_anger01.png"
image my anger02 = "face/lisite/my_anger02.png"
image my shame01 = "face/lisite/my_shame01.png"
image my shame02 = "face/lisite/my_shame02.png"
image my surprise02 = "face/lisite/my_surprise02.png"
image my sad02 = "face/lisite/my_sad02.png"
image my happy01 = "face/lisite/my_happy01.png"
image my normal02 = "face/lisite/my_normal02.png"
image my surprise03 = "face/lisite/my_surprise03.png"
image my anger03 = "face/lisite/my_anger03.png"
image my wunai01 = "face/lisite/my_wunai01.png"
image my wunai02 = "face/lisite/my_wunai02.png"
image my sad03 = "face/lisite/my_sad03.png"
image my cry02 = "face/lisite/my_cry02.png"
image my surprise04 = "face/lisite/my_surprise04.png"
image my bishi01 = "face/lisite/my_bishi01.png"
image my myxf_sad00 = "face/lisite_xf/myxf_sad00.png"
image my myxf_sad01 = "face/lisite_xf/myxf_sad01.png"
image my myxf_surprise01 = "face/lisite_xf/myxf_surprise01.png"
image my myxf_ganga01 = "face/lisite_xf/myxf_ganga01.png"
image my myxf_normal01 = "face/lisite_xf/myxf_normal01.png"
image my myxf_warry01 = "face/lisite_xf/myxf_warry01.png"
image my myxf_small = "face/lisite_xf/myxf_small.png"
image my myxf_anger01 = "face/lisite_xf/myxf_anger01.png"
image my myxf_sad02 = "face/lisite_xf/myxf_sad02.png"
image my myxf_cry01 = "face/lisite_xf/myxf_cry01.png"
image my myxf_sad03 = "face/lisite_xf/myxf_sad03.png"
image my myxf_happy01 = "face/lisite_xf/myxf_happy01.png"
image my surprise05 = "face/lisite/my_surprise05.png"
image my bishi02 = "face/lisite/my_bishi02.png"
image my normal03 = "face/lisite/my_normal03.png"
image my normal04 = "face/lisite/my_normal04.png"
image my shame03 = "face/lisite/my_shame03.png"
image my shame04 = "face/lisite/my_shame04.png"
image my anger04 = "face/lisite/my_anger04.png"
image my sad04 = "face/lisite/my_sad04.png"
image my wunai03 = "face/lisite/my_wunai03.png"
image my warry01 = "face/lisite/my_warry01.png"

image xfe normal01 = "face/xfe/xfe_normal01.png"
image xfe happy01 = "face/xfe/xfe_happy01.png"
image xfe smile01 = "face/xfe/xfe_smile01.png"
image xfe smile02 = "face/xfe/xfe_smile02.png"
image xfe happy02b = "face/xfe/xfe_happy02b.png"
image xfe surprise01b = "face/xfe/xfe_surprise01b.png"
image xfe smile01b = "face/xfe/xfe_smile01b.png"
image xfe warry01b = "face/xfe/xfe_warry01b.png"
image xfe sad01b = "face/xfe/xfe_sad01b.png"
image xfe sad02b = "face/xfe/xfe_sad02b.png"
image xfe sad03b = "face/xfe/xfe_sad03b.png"
image xfe happy03b = "face/xfe/xfe_happy03b.png"
image xfe smile02b = "face/xfe/xfe_smile02b.png"
image xfe normal01b = "face/xfe/xfe_normal01b.png"
image xfe surprise02b = "face/xfe/xfe_surprise02b.png"
image xfe surprise03b = "face/xfe/xfe_surprise03b.png"
image xfe surprise04b = "face/xfe/xfe_surprise04b.png"
image xfe happy04b = "face/xfe/xfe_happy04b.png"
image xfe happy05b = "face/xfe/xfe_happy05b.png"
image xfe smile03b = "face/xfe/xfe_smile03b.png"
image xfe smile04b = "face/xfe/xfe_smile04b.png"
image xfe happy06b = "face/xfe/xfe_happy06b.png"
image xfe warry02b = "face/xfe/xfe_warry02b.png"
image xfe sad04b = "face/xfe/xfe_sad04b.png"
image xfe anger01b = "face/xfe/xfe_anger01b.png"
image xfe surprise05b = "face/xfe/xfe_surprise05b.png"
image xfe sad05b = "face/xfe/xfe_sad05b.png"
image xfe smile05b = "face/xfe/xfe_smile05b.png"
image xfe chixue01 = "face/xfe/xfe_chixue01.png"
image xfe shame01 = "face/xfe/xfe_shame01.png"
image xfe happy07 = "face/xfe/xfe_happy07.png"
image xfe cry01 = "face/xfe/xfe_cry01.png"
image xfe warry03 = "face/xfe/xfe_warry03.png"
image xfe anger02b = "face/xfe/xfe_anger02b.png"
image xfe surprise06 = "face/xfe/xfe_surprise06.png"
image xfe sad01s = "face/xfe/xfe_sad01s.png"
image xfe sad02s = "face/xfe/xfe_sad02s.png"
image xfe chixue02 = "face/xfe/xfe_chixue02.png"
image xfe smile06 = "face/xfe/xfe_smile06.png"
image xfe surprise07 = "face/xfe/xfe_surprise07.png"
image xfe happy08 = "face/xfe/xfe_happy08.png"
image xfe normal02 = "face/xfe/xfe_normal02.png"
image xfe normal03 = "face/xfe/xfe_normal03.png"
image xfe sad06 = "face/xfe/xfe_sad06.png"
image xfe sad07 = "face/xfe/xfe_sad07.png"
image xfe surprise08 = "face/xfe/xfe_surprise08.png"
image xfe anger02 = "face/xfe/xfe_anger02.png"
image xfe surprise09 = "face/xfe/xfe_surprise09.png"
image xfe warry04 = "face/xfe/xfe_warry04.png"
image xfe warry05 = "face/xfe/xfe_warry05.png"
image xfe warry06 = "face/xfe/xfe_warry06.png"
image xfe cry02 = "face/xfe/xfe_cry02.png"
image xfe anger03 = "face/xfe/xfe_anger03.png"
image xfe smile07 = "face/xfe/xfe_smile07.png"
image xfe anger04 = "face/xfe/xfe_anger04.png"
image xfe sad08 = "face/xfe/xfe_sad08.png"
image xfe ganga01 = "face/xfe/xfe_ganga01.png"
image xfe surprise10 = "face/xfe/xfe_surprise10.png"
image xfe wunai01 = "face/xfe/xfe_wunai01.png"
image xfe happy09 = "face/xfe/xfe_happy09.png"

image xing surprise01 = "face/jishenxing/xing_surprise01.png"
image xing smile01 = "face/jishenxing/xing_smile01.png"
image xing normal01 = "face/jishenxing/xing_normal01.png"
image xing sad01 = "face/jishenxing/xing_sad01.png"
image xing anger01 = "face/jishenxing/xing_anger01.png"
image xing warry01 = "face/jishenxing/xing_warry01.png"
image xing smile02 = "face/jishenxing/xing_smile02.png"
image xing bishi01 = "face/jishenxing/xing_bishi01.png"
image xing sad02 = "face/jishenxing/xing_sad02.png"
image xing sad03 = "face/jishenxing/xing_sad03.png"

image aiyi normal01 = "face/aiyi/ay_normal01.png"
image aiyi surprise01 = "face/aiyi/ay_surprise01.png"
image aiyi smile01 = "face/aiyi/ay_smile01.png"
image aiyi sad01 = "face/aiyi/ay_sad01.png"
image aiyi shame01 = "face/aiyi/ay_shame01.png"
image aiyi sad02 = "face/aiyi/ay_sad02.png"
image aiyi surprise02 = "face/aiyi/ay_surprise02.png"
image aiyi sad02b = "face/aiyi/ay_sad02b.png"
image aiyi kun01 = "face/aiyi/ay_kun01.png"
image aiyi normal02 = "face/aiyi/ay_normal02.png"
image aiyi smile02 = "face/aiyi/ay_smile02.png"
image aiyi anger01 = "face/aiyi/ay_anger01.png"
image aiyi surprise03 = "face/aiyi/ay_surprise03.png"
image aiyi sad03 = "face/aiyi/ay_sad03.png"
image aiyi sad04 = "face/aiyi/ay_sad04.png"
image aiyi wunai01 = "face/aiyi/ay_wunai01.png"
image aiyi warry01 = "face/aiyi/ay_warry01.png"
image aiyi nengli01 = "face/aiyi/ay_nengli01.png"
image aiyi nengli02 = "face/aiyi/ay_nengli02.png"

image qianbo tucao01 = "face/qb/qb_tucao01.png"
image qianbo anger01 = "face/qb/qb_anger01.png"
image qianbo normal01 = "face/qb/qb_normal01.png"
image qianbo bishi01 = "face/qb/qb_bishi01.png"
image qianbo shame01 = "face/qb/qb_shame01.png"
image qianbo youhuo01 = "face/qb/qb_youhuo01.png"
image qianbo surprise01 = "face/qb/qb_surprise01.png"
image qianbo anger02 = "face/qb/qb_anger02.png"
image qianbo surprise02 = "face/qb/qb_surprise02.png"
image qianbo cry01 = "face/qb/qb_cry01.png"
image qianbo zihao01 = "face/qb/qb_zihao01.png"
image qianbo surprise03 = "face/qb/qb_surprise03.png"
image qianbo zihao02 = "face/qb/qb_zihao02.png"
image qianbo tucao01b = "face/qb/qb_tucao01b.png"
image qianbo sad01 = "face/qb/qb_sad01.png"
image qianbo sad02 = "face/qb/qb_sad02.png"
image qianbo anger03 = "face/qb/qb_anger03.png"
image qianbo happy01 = "face/qb/qb_happy01.png"
image qianbo tucao02 = "face/qb/qb_tucao02.png"
image qianbo normal02 = "face/qb/qb_normal02.png"
image qianbo zihao03 = "face/qb/qb_zihao03.png"
image qianbo sad03 = "face/qb/qb_sad03.png"
image qianbo normal03 = "face/qb/qb_normal03.png"
image qianbo bishi02 = "face/qb/qb_bishi02.png"
image qianbo anger04 = "face/qb/qb_anger04.png"
image qianbo surprise04 = "face/qb/qb_surprise04.png"
image qianbo happy02 = "face/qb/qb_happy02.png"
image qianbo smile01 = "face/qb/qb_smile01.png"
image qianbo shame02 = "face/qb/qb_shame02.png"
image qianbo surprise05 = "face/qb/qb_surprise05.png"
image qianbo sad04 = "face/qb/qb_sad04.png"
image qianbo cry02 = "face/qb/qb_cry02.png"
image qianbo zihao04 = "face/qb/qb_zihao04.png"
image qianbo smile02 = "face/qb/qb_smile02.png"

image hz anger01 = "face/hz/hz_anger01.png"
image hz surprise01 = "face/hz/hz_surprise01.png"
image hz normal01 = "face/hz/hz_normal01.png"
image hz sad01 = "face/hz/hz_sad01.png"
image hz smile01 = "face/hz/hz_smile01.png"
image hz wunai01 = "face/hz/hz_wunai01.png"
image hz anger02 = "face/hz/hz_anger02.png"
image hz surprise02 = "face/hz/hz_surprise02.png"
image hz normal02 = "face/hz/hz_normal02.png"
image hz sad02 = "face/hz/hz_sad02.png"
image hz smile02 = "face/hz/hz_smile02.png"
image hz wunai02 = "face/hz/hz_wunai02.png"
image hz warry01 = "face/hz/hz_warry01.png"
image hz wunai03 = "face/hz/hz_wunai03.png"

image xiaotao normal01 = "face/xiaotao/xt_normal01.png"
image xiaotao sad01 = "face/xiaotao/xt_sad01.png"
image xiaotao cry01 = "face/xiaotao/xt_cry01.png"
image xiaotao surprise01 = "face/xiaotao/xt_surprise01.png"
image xiaotao shame01 = "face/xiaotao/xt_shame01.png"
image xiaotao smile01 = "face/xiaotao/xt_smile01.png"
image xiaotao sikao01 = "face/xiaotao/xt_sikao01.png"
image xiaotao chimi01 = "face/xiaotao/xt_chimi01.png"
image xiaotao normal02 = "face/xiaotao/xt_normal02.png"
image xiaotao sad02 = "face/xiaotao/xt_sad02.png"
image xiaotao sikao02 = "face/xiaotao/xt_sikao02.png"
image xiaotao surprise02 = "face/xiaotao/xt_surprise02.png"
image xiaotao cry02 = "face/xiaotao/xt_cry02.png"
image xiaotao cry02b = "face/xiaotao/xt_cry02b.png"

image yey normal01 = "face/yeylaoshi/yey_normal01.png"
image yey sad01 = "face/yeylaoshi/yey_sad01.png"
image yey happy01 = "face/yeylaoshi/yey_happy01.png"
image yey surprise01 = "face/yeylaoshi/yey_surprise01.png"
image yey sad02 = "face/yeylaoshi/yey_sad02.png"
image yey surprise02 = "face/yeylaoshi/yey_surprise02.png"
image yey happy02 = "face/yeylaoshi/yey_happy02.png"
image yey anger01 = "face/yeylaoshi/yey_anger01.png"
image yey normal02 = "face/yeylaoshi/yey_normal02.png"
image yey nengli01 = "face/yeylaoshi/nengli.png"
image yey normal03 = "face/yeylaoshi/yey_normal03.png"
image yey sad03 = "face/yeylaoshi/yey_sad03.png"
image yey sad04 = "face/yeylaoshi/yey_sad04.png"
image yey surprise03 = "face/yeylaoshi/yey_surprise03.png"
image yey sad05 = "face/yeylaoshi/yey_sad05.png"
image yey nengli01 = "face/yeylaoshi/yey_nengli01.png"
image yey nengli02 = "face/yeylaoshi/yey_nengli02.png"
image yey happy03 = "face/yeylaoshi/yey_happy03.png"
image yey normal04 = "face/yeylaoshi/yey_normal04.png"
image yey happy04 = "face/yeylaoshi/yey_happy04.png"
image yey normal05 = "face/yeylaoshi/yey_normal05.png"
image yey nengli03 = "face/yeylaoshi/yey_nengli03.png"

image yj happy01 = "face/yj/yj_happy01.png"
image yj ganga01 = "face/yj/yj_ganga01.png"
image yj shame01 = "face/yj/yj_shame01.png"
image yj surprise01 = "face/yj/yj_surprise01.png"
image yj normal01 = "face/yj/yj_normal01.png"
image yj smile01 = "face/yj/yj_smile01.png"
image yj surprise02 = "face/yj/yj_surprise02.png"
image yj bishi01 = "face/yj/yj_bishi01.png"
image yj cry01 = "face/yj/yj_cry01.png"
image yj shame02 = "face/yj/yj_shame02.png"
image yj anger01 = "face/yj/yj_anger01.png"
image yj happy02 = "face/yj/yj_happy02.png"
image yj surprise03 = "face/yj/yj_surprise03.png"
image yj smile03 = "face/yj/yj_smile03.png"
image yj smile02 = "face/yj/yj_smile02.png"
image yj warry01 = "face/yj/yj_warry01.png"
image yj surprise04 = "face/yj/yj_surprise04.png"
image yj warry02 = "face/yj/yj_warry02.png"
image yj smile04 = "face/yj/yj_smile04.png"
image yj happy03 = "face/yj/yj_happy03.png"
image yj ganga02 = "face/yj/yj_ganga02.png"
image yj normal02 = "face/yj/yj_normal02.png"
image yj shame03 = "face/yj/yj_shame03.png"
image yj sad01 = "face/yj/yj_sad01.png"
image yj surprise05 = "face/yj/yj_surprise05.png"
image yj smile05 = "face/yj/yj_smile05.png"
image yj wunai01 = "face/yj/yj_wunai01.png"
image yj anger02 = "face/yj/yj_anger02.png"
image yj chaoxiao01 = "face/yj/yj_chaoxiao01.png"
image yj happy04 = "face/yj/yj_happy04.png"
image yj sad02 = "face/yj/yj_sad02.png"
image yj wunai02 = "face/yj/yj_wunai02.png"
image yj sad03 = "face/yj/yj_sad03.png"
image yj shame04 = "face/yj/yj_shame04.png"
image yj sad04 = "face/yj/yj_sad04.png"
image yj cry02 = "face/yj/yj_cry02.png"
image yj nengli1 = "face/yj/yj_nengli1.png"
image yj cry03 = "face/yj/yj_cry03.png"
image yj nengli2 = "face/yj/yj_nengli2.png"
image yj sad05 = "face/yj/yj_sad05.png"
image yj shame05 = "face/yj/yj_shame05.png"
image yj cry04 = "face/yj/yj_cry04.png"
image yj smile06 = "face/yj/yj_smile06.png"
image yj anger03 = "face/yj/yj_anger03.png"
image yj wunai03 = "face/yj/yj_wunai03.png"
image yj wunai04 = "face/yj/yj_wunai04.png"
image yj normal03 = "face/yj/yj_normal03.png"
image yj wunai05 = "face/yj/yj_wunai05.png"
image yj happy05 = "face/yj/yj_happy05.png"
image yj surprise06 = "face/yj/yj_surprise06.png"
image yj warry03 = "face/yj/yj_warry03.png"
image yj happy06 = "face/yj/yj_happy06.png"
image yj surprise07 = "face/yj/yj_surprise07.png"
image yj nengli3 = "face/yj/yj_nengli3.png"
image yj smile07 = "face/yj/yj_smile07.png"
image yj shame06 = "face/yj/yj_shame06.png"
image yj normal04 = "face/yj/yj_normal04.png"
image yj zihao01 = "face/yj/yj_zihao01.png"
image yj normal05 = "face/yj/yj_normal05.png"
image yj anger04 = "face/yj/yj_anger04.png"
image yj sad06 = "face/yj/yj_sad06.png"
image yj anger05 = "face/yj/yj_anger05.png"
image yj normal06 = "face/yj/yj_normal06.png"

image szl surprise01 = "face/szl/szl_surprise01.png"
image szl sad01 = "face/szl/szl_sad01.png"
image szl normal01 = "face/szl/szl_normal01.png"
image szl wunai01 = "face/szl/szl_wunai01.png"
image szl surprise02 = "face/szl/szl_surprise02.png"
image szl wunai02 = "face/szl/szl_wunai02.png"
image szl normal02 = "face/szl/szl_normal02.png"
image szl surprise03 = "face/szl/szl_surprise03.png"
image szl bishi01 = "face/szl/szl_bishi01.png"
image szl normal03 = "face/szl/szl_normal03.png"
image szl happy01 = "face/szl/szl_happy01.png"
image szl smile01 = "face/szl/szl_smile01.png"
image szl wunai03 = "face/szl/szl_wunai03.png"
image szl warry01 = "face/szl/szl_warry01.png"
image szl shame01 = "face/szl/szl_shame01.png"
image szl anger01 = "face/szl/szl_anger01.png"
image szl bishi02 = "face/szl/szl_bishi02.png"
image szl anger02 = "face/szl/szl_anger02.png"
image szl wunai04 = "face/szl/szl_wunai04.png"
image szl normal04 = "face/szl/szl_normal04.png"
image szl sad02 = "face/szl/szl_sad02.png"
image szl shame02 = "face/szl/szl_shame02.png"
image szl sad03 = "face/szl/szl_sad03.png"
image szl warry02 = "face/szl/szl_warry02.png"
image szl anger03 = "face/szl/szl_anger03.png"
image szl sad04 = "face/szl/szl_sad04.png"
image szl anger04 = "face/szl/szl_anger04.png"
image szl anger05 = "face/szl/szl_anger05.png"
image szl normal05 = "face/szl/szl_normal05.png"
image szl wunai05 = "face/szl/szl_wunai05.png"
image szl bishi03 = "face/szl/szl_bishi03.png"
image szl shame03 = "face/szl/szl_shame03.png"
image szl cry01 = "face/szl/szl_cry01.png"
image szl anger06 = "face/szl/szl_anger06.png"
image szl smile02 = "face/szl/szl_smile02.png"
image szl anger07 = "face/szl/szl_anger07.png"
image szl normal06 = "face/szl/szl_normal06.png"
image szl shame04 = "face/szl/szl_shame04.png"
image szl sad05 = "face/szl/szl_sad05.png"
image szl normal07 = "face/szl/szl_normal07.png"
image szl normal08 = "face/szl/szl_normal08.png"
image szl anger08 = "face/szl/szl_anger08.png"
image szl normal09 = "face/szl/szl_normal09.png"
image szl anger09 = "face/szl/szl_anger09.png"
image szl happy02 = "face/szl/szl_happy02.png"
image szl wunai06 = "face/szl/szl_wunai06.png"
image szl surprise04 = "face/szl/szl_surprise04.png"
image szl happy03 = "face/szl/szl_happy03.png"
image szl shame05 = "face/szl/szl_shame05.png"
image szl shame06 = "face/szl/szl_shame06.png"
image szl anger10 = "face/szl/szl_anger10.png"
image szl surprise05 = "face/szl/szl_surprise05.png"
image szl shame07 = "face/szl/szl_shame07.png"
image szl wunai07 = "face/szl/szl_wunai07.png"
image szl normal10 = "face/szl/szl_normal10.png"
image szl sad06 = "face/szl/szl_sad06.png"
image szl bishi04 = "face/szl/szl_bishi04.png"
image szl surprise06 = "face/szl/szl_surprise06.png"
image szl surprise07 = "face/szl/szl_surprise07.png"
image szl normal11 = "face/szl/szl_normal11.png"
image szl happy04 = "face/szl/szl_happy04.png"
image szl wunai08 = "face/szl/szl_wunai08.png"
image szl sad07 = "face/szl/szl_sad07.png"
image szl warry03 = "face/szl/szl_warry03.png"
image szl shame08 = "face/szl/szl_shame08.png"
image szl sad08 = "face/szl/szl_sad08.png"
image szl anger11 = "face/szl/szl_anger11.png"
image szl wunai09 = "face/szl/szl_wunai09.png"
image szl anger12 = "face/szl/szl_anger12.png"
image szl anger13 = "face/szl/szl_anger13.png"
image szl wunai10 = "face/szl/szl_wunai10.png"
image szl normal12 = "face/szl/szl_normal12.png"
image szl happy05 = "face/szl/szl_happy05.png"
image szl happy06 = "face/szl/szl_happy06.png"
image szl anger14 = "face/szl/szl_anger14.png"
image szl surprise08 = "face/szl/szl_surprise08.png"
image szl bishi05 = "face/szl/szl_bishi05.png"
image szl wunai11 = "face/szl/szl_wunai11.png"
image szl normal13 = "face/szl/szl_normal13.png"
image szl anger15 = "face/szl/szl_anger15.png"
image szl anger16 = "face/szl/szl_anger16.png"
image szl wunai12 = "face/szl/szl_wunai12.png"
image szl bishi06 = "face/szl/szl_bishi06.png"
image szl wunai13 = "face/szl/szl_wunai13.png"
image szl anger17 = "face/szl/szl_anger17.png"
image szl surprise09 = "face/szl/szl_surprise09.png"
image szl bishi07 = "face/szl/szl_bishi07.png"
image szl bishi08 = "face/szl/szl_bishi08.png"
image szl normal14 = "face/szl/szl_normal14.png"
image szl shame09 = "face/szl/szl_shame09.png"
image szl surprise10 = "face/szl/szl_surprise10.png"
image szl shame10 = "face/szl/szl_shame10.png"
image szl anger18 = "face/szl/szl_anger18.png"
image szl shame11 = "face/szl/szl_shame11.png"

image kls normal01 = "face/kls/kls_normal01.png"
image kls sad01 = "face/kls/kls_sad01.png"
image kls happy01 = "face/kls/kls_happy01.png"
image kls smile01 = "face/kls/kls_smile01.png"
image kls wunai01 = "face/kls/kls_wunai01.png"
image kls shame01 = "face/kls/kls_shame01.png"
image kls happy02 = "face/kls/kls_happy02.png"
image kls warry01 = "face/kls/kls_warry01.png"
image kls bishi01 = "face/kls/kls_bishi01.png"
image kls surprise01 = "face/kls/kls_surprise01.png"

image dh normal01 = "face/dahe/dh_normal01.png"
image dh surprise01 = "face/dahe/dh_surprise01.png"
image dh sad01 = "face/dahe/dh_sad01.png"
image dh normal02 = "face/dahe/dh_normal02.png"
image dh happy01 = "face/dahe/dh_happy01.png"
image dh shame01 = "face/dahe/dh_shame01.png"
image dh normal03 = "face/dahe/dh_normal03.png"
image dh normal04 = "face/dahe/dh_normal04.png"
image dh anger01 = "face/dahe/dh_anger01.png"

image wyh happy01 = "face/jswyh/wyh_happy01.png"
image wyh sad01 = "face/jswyh/wyh_sad01.png"
image wyh surprise01 = "face/jswyh/wyh_surprise01.png"
image wyh normal01 = "face/jswyh/wyh_normal01.png"
image wyh happy02 = "face/jswyh/wyh_happy02.png"
image wyh sad02 = "face/jswyh/wyh_sad02.png"
image wyh ganga01 = "face/jswyh/wyh_ganga01.png"

image shy surprise01 = "face/shy/shy_surprise01.png"
image shy wunai01 = "face/shy/shy_wunai01.png"
image shy normal01 = "face/shy/shy_normal01.png"
image shy wunai02 = "face/shy/shy_wunai02.png"
image shy happy01 = "face/shy/shy_happy01.png"
image shy smile01 = "face/shy/shy_smile01.png"
image shy normal02 = "face/shy/shy_normal02.png"
image shy happy02 = "face/shy/shy_happy02.png"

image by smile01 = "face/baiyu/by_smile01.png"
image by wunai01 = "face/baiyu/by_wunai01.png"
image by sad01 = "face/baiyu/by_sad01.png"
image by warry01 = "face/baiyu/by_warry01.png"
image by normal01 = "face/baiyu/by_normal01.png"
image by normal02 = "face/baiyu/by_normal02.png"
image by anger01 = "face/baiyu/by_anger01.png"
image by surprise01 = "face/baiyu/by_surprise01.png"
image by sad02 = "face/baiyu/by_sad02.png"
image by sad03 = "face/baiyu/by_sad03.png"
image by anger02 = "face/baiyu/by_anger02.png"

image ll normal01 = "face/liuli/ll_normal01.png"
image ll smile01 = "face/liuli/ll_smile01.png"
image ll surprise01 = "face/liuli/ll_surprise01.png"
image ll normal02 = "face/liuli/ll_normal02.png"
image ll surprise02 = "face/liuli/ll_surprise02.png"
image ll happy01 = "face/liuli/ll_happy01.png"
image ll sad01 = "face/liuli/ll_sad01.png"
image ll happy02 = "face/liuli/ll_happy02.png"
image ll smile02 = "face/liuli/ll_smile02.png"
image ll warry01 = "face/liuli/ll_warry01.png"
image ll sad02 = "face/liuli/ll_sad02.png"
image ll surprise03 = "face/liuli/ll_surprise03.png"
image ll sad03 = "face/liuli/ll_sad03.png"
image ll shame01 = "face/liuli/ll_shame01.png"
image ll ganga01 = "face/liuli/ll_ganga01.png"
image ll warry02 = "face/liuli/ll_warry02.png"
image ll warry03 = "face/liuli/ll_warry03.png"
image ll shame02 = "face/liuli/ll_shame02.png"
image ll happy03 = "face/liuli/ll_happy03.png"
image ll smile03 = "face/liuli/ll_smile03.png"
image ll happy04 = "face/liuli/ll_happy04.png"
image ll normal03 = "face/liuli/ll_normal03.png"
image ll smile04 = "face/liuli/ll_smile04.png"
image ll surprise04 = "face/liuli/ll_surprise04.png"
image ll shame03 = "face/liuli/ll_shame03.png"
image ll surprise05 = "face/liuli/ll_surprise05.png"
image ll normal04 = "face/liuli/ll_normal04.png"
image ll shame04 = "face/liuli/ll_shame04.png"
image ll sad04 = "face/liuli/ll_sad04.png"
image ll surprise06 = "face/liuli/ll_surprise06.png"
image ll sad05 = "face/liuli/ll_sad05.png"
image ll anger01 = "face/liuli/ll_anger01.png"
image ll smile05 = "face/liuli/ll_smile05.png"
image ll normal05 = "face/liuli/ll_normal05.png"
image ll surprise07 = "face/liuli/ll_surprise07.png"
image ll smile06 = "face/liuli/ll_smile06.png"
image ll sad06 = "face/liuli/ll_sad06.png"
image ll shame05 = "face/liuli/ll_shame05.png"
image ll surprise08 = "face/liuli/ll_surprise08.png"
image ll ganga02 = "face/liuli/ll_ganga02.png"
image ll warry04 = "face/liuli/ll_warry04.png"
image ll warry05 = "face/liuli/ll_warry05.png"
image ll normal06 = "face/liuli/ll_normal06.png"
image ll sad07 = "face/liuli/ll_sad07.png"
image ll anger02 = "face/liuli/ll_anger02.png"
image ll anger03 = "face/liuli/ll_anger03.png"
image ll normal07 = "face/liuli/ll_normal07.png"
image ll normal08 = "face/liuli/ll_normal08.png"
image ll normal09 = "face/liuli/ll_normal09.png"
image ll anger04 = "face/liuli/ll_anger04.png"
image ll normal10 = "face/liuli/ll_normal10.png"
image ll sad08 = "face/liuli/ll_sad08.png"
image ll surprise09 = "face/liuli/ll_surprise09.png"
image ll shame06 = "face/liuli/ll_shame06.png"
image ll sad09 = "face/liuli/ll_sad09.png"
image ll cry01 = "face/liuli/ll_cry01.png"
image ll anger05 = "face/liuli/ll_anger05.png"
image ll warry06 = "face/liuli/ll_warry06.png"
image ll ganga03 = "face/liuli/ll_ganga03.png"
image ll warry07 = "face/liuli/ll_warry07.png"
image ll kongzhi01 = "face/liuli/ll_kongzhi01.png"
image ll kongzhi02 = "face/liuli/ll_kongzhi02.png"
image ll kongzhi03 = "face/liuli/ll_kongzhi03.png"
image ll kongzhi04 = "face/liuli/ll_kongzhi04.png"
image ll kongzhi05 = "face/liuli/ll_kongzhi05.png"

image ly normal01 = "face/lingyin/ly_normal01.png"
image ly happy01 = "face/lingyin/ly_happy01.png"
image ly sad01 = "face/lingyin/ly_sad01.png"
image ly sad02 = "face/lingyin/ly_sad02.png"
image ly surprise01 = "face/lingyin/ly_surprise01.png"
image ly sad03 = "face/lingyin/ly_sad03.png"
image ly sad04 = "face/lingyin/ly_sad04.png"
image ly normal01 = "face/lingyin/ly_normal01.png"
image ly anger01 = "face/lingyin/ly_anger01.png"
image ly sad05 = "face/lingyin/ly_sad05.png"
image ly anger02 = "face/lingyin/ly_anger02.png"
image ly sad06 = "face/lingyin/ly_sad06.png"
image ly surprise02 = "face/lingyin/ly_surprise02.png"
image ly normal02 = "face/lingyin/ly_normal02.png"
image ly smile01 = "face/lingyin/ly_smile01.png"
image ly surprise03 = "face/lingyin/ly_surprise03.png"
image ly cry01 = "face/lingyin/ly_cry01.png"

image lnn normal01 = "face/laonainai/lnn_normal01.png"
image lnn sad01 = "face/laonainai/lnn_sad01.png"
image lnn happy01 = "face/laonainai/lnn_happy01.png"

image tyt normal01 = "face/tyt/tyt_normal01.png"
image tyt normal02 = "face/tyt/tyt_normal02.png"
image tyt surprise01 = "face/tyt/tyt_surprise01.png"
image tyt happy01 = "face/tyt/tyt_happy01.png"
image tyt sad01 = "face/tyt/tyt_sad01.png"
image tyt shame01 = "face/tyt/tyt_shame01.png"
image tyt anger01 = "face/tyt/tyt_anger01.png"
image tyt sad02 = "face/tyt/tyt_sad02.png"
image tyt anger02 = "face/tyt/tyt_anger02.png"

image lhx normal01 = "face/lux/lhx_normal01.png"
image lhx shame01 = "face/lux/lhx_shame01.png"
image lhx normal02 = "face/lux/lhx_normal02.png"
image lhx sad01 = "face/lux/lhx_sad01.png"
image lhx wunai01 = "face/lux/lhx_wunai01.png"
image lhx normal03 = "face/lux/lhx_normal03.png"
image lhx ganga01 = "face/lux/lhx_ganga01.png"
image lhx surprise01 = "face/lux/lhx_surprise01.png"
image lhx ganga02 = "face/lux/lhx_ganga02.png"
image lhx wunai02 = "face/lux/lhx_wunai02.png"
image lhx sad02 = "face/lux/lhx_sad02.png"
image lhx wunai03 = "face/lux/lhx_wunai03.png"
image lhx normal04 = "face/lux/lhx_normal04.png"
image lhx anger01 = "face/lux/lhx_anger01.png"
image lhx surprise02 = "face/lux/lhx_surprise02.png"
image lhx ganga03 = "face/lux/lhx_ganga03.png"
image lhx ganga04 = "face/lux/lhx_ganga04.png"
image lhx wunai04 = "face/lux/lhx_wunai04.png"
image lhx zihao01 = "face/lux/lhx_zihao01.png"
image lhx sad03 = "face/lux/lhx_sad03.png"
image lhx normal05 = "face/lux/lhx_normal05.png"
image lhx wunai05 = "face/lux/lhx_wunai05.png"
image lhx smile01 = "face/lux/lhx_smile01.png"
image lhx zihao02 = "face/lux/lhx_zihao02.png"
image lhx fangsong01 = "face/lux/lhx_fangsong01.png"
image lhx normal06 = "face/lux/lhx_normal06.png"
image lhx wunai06 = "face/lux/lhx_wunai06.png"
image lhx wunai07 = "face/lux/lhx_wunai07.png"
image lhx smile02 = "face/lux/lhx_smile02.png"
image lhx wunai08 = "face/lux/lhx_wunai08.png"
image lhx wunai09 = "face/lux/lhx_wunai09.png"
image lhx sad04 = "face/lux/lhx_sad04.png"
image lhx sad05 = "face/lux/lhx_sad05.png"
image lhx kun01 = "face/lux/lhx_kun01.png"
image lhx surprise03 = "face/lux/lhx_surprise03.png"
image lhx anger02 = "face/lux/lhx_anger02.png"
image lhx anger03 = "face/lux/lhx_anger03.png"
image lhx anger04 = "face/lux/lhx_anger04.png"
image lhx wunai10 = "face/lux/lhx_wunai10.png"
image lhx smile03 = "face/lux/lhx_smile03.png"
image lhx shame02 = "face/lux/lhx_shame02.png"
image lhx sad06 = "face/lux/lhx_sad06.png"
image lhx sad07 = "face/lux/lhx_sad07.png"
image lhx sad08 = "face/lux/lhx_sad08.png"
image lhx fangsong02 = "face/lux/lhx_fangsong02.png"
image lhx surprise04 = "face/lux/lhx_surprise04.png"
image lhx anger05 = "face/lux/lhx_anger05.png"
image lhx kun01 = "face/lux/lhx_kun01.png"
image lhx warry01 = "face/lux/lhx_warry01.png"
image lhx surprise05 = "face/lux/lhx_surprise05.png"
image lhx shame03 = "face/lux/lhx_shame03.png"
image lhx kun02 = "face/lux/lhx_kun02.png"
image lhx wunai11 = "face/lux/lhx_wunai11.png"
image lhx sad09 = "face/lux/lhx_sad09.png"
image lhx anger06 = "face/lux/lhx_anger06.png"
image lhx surprise06 = "face/lux/lhx_surprise06.png"
image lhx normal07 = "face/lux/lhx_normal07.png"
image lhx wunai12 = "face/lux/lhx_wunai12.png"
image lhx deyi01 = "face/lux/lhx_deyi01.png"
image lhx deyi02 = "face/lux/lhx_deyi02.png"
image lhx zihao03 = "face/lux/lhx_zihao03.png"
image lhx surprise07 = "face/lux/lhx_surprise07.png"
image lhx normal08 = "face/lux/lhx_normal08.png"
image lhx wunai13 = "face/lux/lhx_wunai13.png"
image lhx sad10 = "face/lux/lhx_sad10.png"
image lhx shame04 = "face/lux/lhx_shame04.png"
image lhx normal09 = "face/lux/lhx_normal09.png"
image lhx sad11 = "face/lux/lhx_sad11.png"
image lhx shame05 = "face/lux/lhx_shame05.png"
image lhx sad12 = "face/lux/lhx_sad12.png"
image lhx shame06 = "face/lux/lhx_shame06.png"
image lhx surprise08 = "face/lux/lhx_surprise08.png"
image lhx normal10 = "face/lux/lhx_normal10.png"
image lhx smile04 = "face/lux/lhx_smile04.png"
image lhx surprise09 = "face/lux/lhx_surprise09.png"
image lhx sad13 = "face/lux/lhx_sad13.png"

image al normal01 = "face/albo/al_normal01.png"
image al normal02 = "face/albo/al_normal02.png"
image al smile01 = "face/albo/al_smile01.png"
image al normal03 = "face/albo/al_normal03.png"
image al normal04 = "face/albo/al_normal04.png"
image al smile02 = "face/albo/al_smile02.png"
image al anger01 = "face/albo/al_anger01.png"
image al surprise01 = "face/albo/al_surprise01.png"
image al sad01 = "face/albo/al_sad01.png"
image al happy01 = "face/albo/al_happy01.png"
image al wunai01 = "face/albo/al_wunai01.png"
image al happy02 = "face/albo/al_happy02.png"
image al anger02 = "face/albo/al_anger02.png"
image al anger03 = "face/albo/al_anger03.png"
image al sad02 = "face/albo/al_sad02.png"
image al happy03 = "face/albo/al_happy03.png"
image al ganga01 = "face/albo/al_ganga01.png"
image al penhuo01 = "face/albo/al_penhuo01.png"
image al smile03 = "face/albo/al_smile03.png"
image al smile04 = "face/albo/al_smile04.png"

image bg new01 = "images/BG010_020.bmp"
image bg new02 = "images/BG010_020b.bmp"

image bg ssel_bg = "images/ssel_bg.bmp"

image bg end2 = "images/end2.bmp"

image bg MARE_e11a = "images/MARE_e11a.bmp"
image bg MARE_e11b = "images/MARE_e11b.bmp"
image bg MARE_e11c = "images/MARE_e11c.bmp"
image bg MARE_e11d = "images/MARE_e11d.bmp"

image bg lsth01 = "images/H1/MARE_e08a.bmp"
image bg lsth02 = "images/H1/MARE_e08b.bmp"
image bg lsth03 = "images/H1/MARE_h01a.bmp"
image bg lsth04 = "images/H1/MARE_h01b.bmp"
image bg lsth05 = "images/H1/MARE_h01c.bmp"
image bg lsth06 = "images/H1/MARE_h01d.bmp"
image bg lsth07 = "images/H1/MARE_h01e.bmp"
image bg lsth08 = "images/H1/MARE_h01f.bmp"
image bg lsth09 = "images/H1/MARE_h01g.bmp"
image bg lsth10 = "images/H1/MARE_h01h.bmp"
image bg lsth11 = "images/H1/MARE_h01i.bmp"
image bg lsth12 = "images/H1/MARE_h01j.bmp"
image bg lsth13 = "images/H1/MARE_h01k.bmp"

image bg lsth14 = "images/H1/MARE_h02a.bmp"
image bg lsth15 = "images/H1/MARE_h02b.bmp"
image bg lsth16 = "images/H1/MARE_h02c.bmp"
image bg lsth17 = "images/H1/MARE_h02d.bmp"
image bg lsth18 = "images/H1/MARE_h02e.bmp"
image bg lsth19 = "images/H1/MARE_h02g.bmp"
image bg lsth20 = "images/H1/MARE_h02h.bmp"
image bg lsth21 = "images/H1/MARE_h02i.bmp"
image bg lsth22 = "images/H1/MARE_h02j.bmp"

image bg MARE_e03o = "images/MARE_e03o.bmp"
image bg MARE_e07a = "images/MARE_e07a.bmp"
image bg MARE_e07b = "images/MARE_e07b.bmp"

image bg MARE_e05g = "images/MARE_e05g.bmp"
image bg MARE_e05h = "images/MARE_e05h.bmp"
image bg MARE_e05i = "images/MARE_e05i.bmp"

image bg xzh01 = "images/H/KOMOMO_h03a.bmp"
image bg xzh02 = "images/H/KOMOMO_h03f.bmp"
image bg xzh03 = "images/H/KOMOMO_h03d.bmp"
image bg xzh04 = "images/H/KOMOMO_h03e.bmp"
image bg xzh05 = "images/H/KOMOMO_h04a.bmp"
image bg xzh06 = "images/H/KOMOMO_h04b.bmp"
image bg xzh07 = "images/H/KOMOMO_h04c.bmp"
image bg xzh08 = "images/H/KOMOMO_h04d.bmp"
image bg xzh09 = "images/H/KOMOMO_h04e.bmp"
image bg xzh10 = "images/H/KOMOMO_h04g.bmp"
image bg xzh11 = "images/H/KOMOMO_h04f.bmp"
image bg xzh12 = "images/H/KOMOMO_h04h.bmp"
image bg xzh13 = "images/H/KOMOMO_h04i.bmp"
image bg xzh14 = "images/H/KOMOMO_h04j.bmp"
image bg xzh15 = "images/H/KOMOMO_h04l.bmp"
image bg xzh16 = "images/H/KOMOMO_h04k.bmp"

image bg xzh17 = "images/H/KOMOMO_h05a.bmp"
image bg xzh18 = "images/H/KOMOMO_h05b.bmp"
image bg xzh19 = "images/H/KOMOMO_h05c.bmp"
image bg xzh20 = "images/H/KOMOMO_h05d.bmp"
image bg xzh21 = "images/H/KOMOMO_h05e.bmp"
image bg xzh22 = "images/H/KOMOMO_h05f.bmp"
image bg xzh23 = "images/H/KOMOMO_h05g.bmp"
image bg xzh24 = "images/H/KOMOMO_h05h.bmp"
image bg xzh25 = "images/H/KOMOMO_h05l.bmp"
image bg xzh26 = "images/H/KOMOMO_h05j.bmp"
image bg xzh27 = "images/H/KOMOMO_h05k.bmp"
image bg xzh28 = "images/H/KOMOMO_h05m.bmp"

image bg MARE_e03f = "images/MARE_e03k.bmp"
image bg MARE_e03h = "images/MARE_e03m.bmp"
image bg MARE_e03n = "images/MARE_e03n.bmp"
image bg MARE_e06a = "images/MARE_e06a.bmp"

image bg sel = "ui/sel.bmp"

image ltl tucao01 = "face/ltl/ltl_tucao01.png"
image ltl happy01 = "face/ltl/ltl_happy01.png"
image ltl tucao02 = "face/ltl/ltl_tucao02.png"
image ltl ganga01 = "face/ltl/ltl_ganga01.png"
image ltl tucao03 = "face/ltl/ltl_tucao03.png"
image ltl surprise01 = "face/ltl/ltl_su01.png"
image ltl sad01 = "face/ltl/ltl_sad01.png"
image ltl sad02 = "face/ltl/ltl_sad02.png"
image ltl zihao02 = "face/ltl/ltl_zihao02.png"
image ltl anger01 = "face/ltl/ltl_anger01.png"
image ltl sad03 = "face/ltl/ltl_sad03.png"
image ltl shame01 = "face/ltl/ltl_shame01.png"
image ltl normal01 = "face/ltl/ltl_normal01.png"
image ltl huachi01 = "face/ltl/ltl_huachi01.png"
image ltl surprise02 = "face/ltl/ltl_su02.png"
image ltl sad04 = "face/ltl/ltl_sad04.png"

image mm normal01 = "face/my/mm_normal01.png"
image mm normal02 = "face/my/mm_normal02.png"
image mm wunai01 = "face/my/mm_wunai01.png"
image mm normal03 = "face/my/mm_normal03.png"
image mm zihao01 = "face/my/mm_zihao01.png"
image mm happy01 = "face/my/mm_happy01.png"
image mm tucao01 = "face/my/mm_tucao01.png"
image mm zihao02 = "face/my/mm_zihao02.png"
image mm smile01 = "face/my/mm_smile01.png"
image mm surprise01 = "face/my/mm_surprise01.png"
image mm shame01 = "face/my/mm_shame01.png"
image mm shame02 = "face/my/mm_shame02.png"
image mm sad01 = "face/my/mm_sad01.png"
image mm shame03 = "face/my/mm_shame03.png"
image mm anger01 = "face/my/mm_anger01.png"
image mm shame04 = "face/my/mm_shame04.png"
image mm surprise02 = "face/my/mm_surprise02.png"
image mm shame05 = "face/my/mm_shame05.png"
image mm wunai02 = "face/my/mm_wunai02.png"
image mm anger02 = "face/my/mm_anger02.png"
image mm wunai03 = "face/my/mm_wunai03.png"
image mm anger03 = "face/my/mm_anger03.png"
image mm smile02 = "face/my/mm_smile02.png"
image mm anger04 = "face/my/mm_anger04.png"
image mm sad02 = "face/my/mm_sad02.png"
image mm smile03 = "face/my/mm_smile03.png"
image mm warry01 = "face/my/mm_warry01.png"
image mm anger05 = "face/my/mm_anger05.png"
image mm wunai04 = "face/my/mm_wunai04.png"
image mm shame06 = "face/my/mm_shame06.png"
image mm sad03 = "face/my/mm_sad03.png"
image mm normal04 = "face/my/mm_normal04.png"
image mm warry02 = "face/my/mm_warry02.png"
image mm happy02 = "face/my/mm_happy02.png"
image mm warry03 = "face/my/mm_warry03.png"
image mm normal05 = "face/my/mm_normal05.png"
image mm shame07 = "face/my/mm_shame07.png"
image mm anger06 = "face/my/mm_anger06.png"
image mm tucao02 = "face/my/mm_tucao02.png"

image shs normal01 = "face/shs/shs_normal01.png"
image shs smile01 = "face/shs/shs_smile01.png"
image shs happy01 = "face/shs/shs_happy01.png"
image shs smile02 = "face/shs/shs_smile02.png"
image shs normal02 = "face/shs/shs_normal02.png"
image shs anger01 = "face/shs/shs_anger01.png"
image shs sad01 = "face/shs/shs_sad01.png"
image shs normal03 = "face/shs/shs_normal03.png"
image shs smile03 = "face/shs/shs_smile03.png"
image shs anger02 = "face/shs/shs_anger02.png"
image shs surprise01 = "face/shs/shs_surprise01.png"
image shs sad02 = "face/shs/shs_sad02.png"
image shs surprise02 = "face/shs/shs_surprise02.png"
image shs normal04 = "face/shs/shs_normal04.png"
image shs anger03 = "face/shs/shs_anger03.png"

image nlx smile01 = "face/nlx/nlx_smile01.png"
image nlx happy01 = "face/nlx/nlx_happy01.png"
image nlx warry01 = "face/nlx/nlx_warry01.png"
image nlx surprise01 = "face/nlx/nlx_surprise01.png"
image nlx surprise02 = "face/nlx/nlx_surprise02.png"

image lh surprise01 = "face/xmlh/lh_surprise01.png"
image lh surprise02 = "face/xmlh/lh_surprise02.png"
image lh surprise03 = "face/xmlh/lh_surprise03.png"
image lh happy01 = "face/xmlh/lh_happy01.png"
image lh happy02 = "face/xmlh/lh_happy02.png"
image lh normal01 = "face/xmlh/lh_normal01.png"
image lh smile01 = "face/xmlh/lh_smile01.png"
image lh tucao01 = "face/xmlh/lh_tucao01.png"
image lh smile02 = "face/xmlh/lh_smile02.png"
image lh tucao02 = "face/xmlh/lh_tucao02.png"
image lh wunai01 = "face/xmlh/lh_wunai01.png"
image lh smile03 = "face/xmlh/lh_smile03.png"
image lh normal02 = "face/xmlh/lh_normal02.png"
image lh smile04 = "face/xmlh/lh_smile04.png"
image lh surprise04 = "face/xmlh/lh_surprise04.png"
image lh warry01 = "face/xmlh/lh_warry01.png"
image lh tucao03 = "face/xmlh/lh_tucao03.png"
image lh smile05 = "face/xmlh/lh_smile05.png"
image lh shame01 = "face/xmlh/lh_shame01.png"
image lh ganga01 = "face/xmlh/lh_ganga01.png"
image lh anger01 = "face/xmlh/lh_anger01.png"
image lh anger02 = "face/xmlh/lh_anger02.png"
image lh sad01 = "face/xmlh/lh_sad01.png"
image lh wunai02 = "face/xmlh/lh_wunai02.png"
image lh sad02 = "face/xmlh/lh_sad02.png"
image lh sad03 = "face/xmlh/lh_sad03.png"
image lh surprise05 = "face/xmlh/lh_surprise05.png"
image lh anger03 = "face/xmlh/lh_anger03.png"
image lh smile06 = "face/xmlh/lh_smile06.png"

image xm surprise01 = "face/xm/xm_surprise01.png"
image xm happy01 = "face/xm/xm_happy01.png"
image xm normal01 = "face/xm/xm_normal01.png"
image xm happy02 = "face/xm/xm_happy02.png"
image xm wunai01 = "face/xm/xm_wunai01.png"
image xm wunai02 = "face/xm/xm_wunai02.png"
image xm surprise02 = "face/xm/xm_surprise02.png"
image xm smile01 = "face/xm/xm_smile01.png"
# image bg p1_surprise01 = "images/event cg/01/surprise01.bmp"
# image bg p1_anger01 = "images/event cg/01/anger01.bmp"
# image bg p1_normal01 = "images/event cg/01/normal01.bmp"
# image bg p1_smile01 = "images/event cg/01/smile01.bmp"
# image bg p1_linggan = "images/event cg/01/linggan.bmp"
# image bg p1_happy01 = "images/event cg/01/happy01.bmp"
# image bg p1_shame01 = "images/event cg/01/shame01.bmp"
# image bg p1_shame02 = "images/event cg/01/shame02.bmp"

# image bg p2_my_haibian = "images/event cg/02/my_haibian.bmp"
# image bg p2_my_huanghun2 = "images/event cg/02/my_huanghun2.bmp"

# image bg p5_my_huiyi_xinwei = "images/event cg/05/huiyi_xinwei.bmp"
# image bg p5_my_huiyi_sad = "images/event cg/05/huiyi_sad.bmp"

# image bg p3_wunv_anger01 = "images/event cg/03/wunv_anger01.bmp"
# image bg p3_wunv_happy01 = "images/event cg/03/wunv_happy01.bmp"
# image bg p3_wunv_normal01 = "images/event cg/03/wunv_normal01.bmp"
# image bg p3_wunv_shame01 = "images/event cg/03/wunv_shame01.bmp"
# image bg p3_wunv_smile01 = "images/event cg/03/wunv_smile01.bmp"
# image bg p3_wunv_surprise01 = "images/event cg/03/wunv_surprise01.bmp"
# image bg p3_wunv_wunai01 = "images/event cg/03/wunv_wunai01.bmp"

# image bg p4_xz_shenshe01 = "images/event cg/04/xz_shenshe01.bmp"

# image bg p7_KOMOMO_e06a = "images/event cg/07/KOMOMO_e06a.bmp"
# image bg p7_KOMOMO_e06b = "images/event cg/07/KOMOMO_e06b.bmp"
# image bg p7_KOMOMO_e06c = "images/event cg/07/KOMOMO_e06c.bmp"
# image bg p7_KOMOMO_e06d = "images/event cg/07/KOMOMO_e06d.bmp"
# image bg p7_KOMOMO_e06e = "images/event cg/07/KOMOMO_e06e.bmp"

# image bg p8_KOMOMO_h03a = "images/event cg/08/KOMOMO_h03a.bmp"
# image bg p8_KOMOMO_h03d = "images/event cg/08/KOMOMO_h03d.bmp"
# image bg p8_KOMOMO_h03e = "images/event cg/08/KOMOMO_h03e.bmp"
# image bg p8_KOMOMO_h03f = "images/event cg/08/KOMOMO_h03f.bmp"

# image bg p9_KOMOMO_h04a = "images/event cg/09/KOMOMO_h04a.bmp"
# image bg p9_KOMOMO_h04b = "images/event cg/09/KOMOMO_h04b.bmp"
# image bg p9_KOMOMO_h04c = "images/event cg/09/KOMOMO_h04c.bmp"
# image bg p9_KOMOMO_h04d = "images/event cg/09/KOMOMO_h04d.bmp"
# image bg p9_KOMOMO_h04e = "images/event cg/09/KOMOMO_h04e.bmp"
# image bg p9_KOMOMO_h04f = "images/event cg/09/KOMOMO_h04f.bmp"
# image bg p9_KOMOMO_h04g = "images/event cg/09/KOMOMO_h04g.bmp"
# image bg p9_KOMOMO_h04h = "images/event cg/09/KOMOMO_h04h.bmp"
# image bg p9_KOMOMO_h04i = "images/event cg/09/KOMOMO_h04i.bmp"
# image bg p9_KOMOMO_h04j = "images/event cg/09/KOMOMO_h04j.bmp"
# image bg p9_KOMOMO_h04k = "images/event cg/09/KOMOMO_h04k.bmp"
# image bg p9_KOMOMO_h04l = "images/event cg/09/KOMOMO_h04l.bmp"

# image bg p10_KOMOMO_h05a = "images/event cg/10/KOMOMO_h05a.bmp"
# image bg p10_KOMOMO_h05b = "images/event cg/10/KOMOMO_h05b.bmp"
# image bg p10_KOMOMO_h05c = "images/event cg/10/KOMOMO_h05c.bmp"
# image bg p10_KOMOMO_h05d = "images/event cg/10/KOMOMO_h05d.bmp"
# image bg p10_KOMOMO_h05e = "images/event cg/10/KOMOMO_h05e.bmp"
# image bg p10_KOMOMO_h05f = "images/event cg/10/KOMOMO_h05f.bmp"
# image bg p10_KOMOMO_h05g = "images/event cg/10/KOMOMO_h05g.bmp"
# image bg p10_KOMOMO_h05h = "images/event cg/10/KOMOMO_h05h.bmp"
# image bg p10_KOMOMO_h05j = "images/event cg/10/KOMOMO_h05j.bmp"
# image bg p10_KOMOMO_h05k = "images/event cg/10/KOMOMO_h05k.bmp"
# image bg p10_KOMOMO_h05l = "images/event cg/10/KOMOMO_h05l.bmp"
# image bg p10_KOMOMO_h05m = "images/event cg/10/KOMOMO_h05m.bmp"

# image bg p11_MARE_e02a = "images/event cg/11/MARE_e02a.bmp"
# image bg p11_MARE_e02b = "images/event cg/11/MARE_e02a.bmp"
# image bg p11_MARE_e02c = "images/event cg/11/MARE_e02a.bmp"
# image bg p11_MARE_e02d = "images/event cg/11/MARE_e02a.bmp"
# image bg p11_MARE_e02e = "images/event cg/11/MARE_e02a.bmp"
# image bg p11_MARE_e02f = "images/event cg/11/MARE_e02a.bmp"
# image bg p11_MARE_e02g = "images/event cg/11/MARE_e02a.bmp"
# image bg p11_MARE_e02h = "images/event cg/11/MARE_e02a.bmp"

# image bg p12_MARE_e09a = "images/event cg/12/MARE_e09a.bmp"
# image bg p12_MARE_e09b = "images/event cg/12/MARE_e09b.bmp"
# image bg p12_MARE_e09c = "images/event cg/12/MARE_e09c.bmp"
# image bg p12_MARE_e09d = "images/event cg/12/MARE_e09d.bmp"
# image bg p12_MARE_e09e = "images/event cg/12/MARE_e09e.bmp"
# image bg p12_MARE_e09i = "images/event cg/12/MARE_e09i.bmp"
# image bg p12_MARE_e09j = "images/event cg/12/MARE_e09j.bmp"
# image bg p12_MARE_e09l = "images/event cg/12/MARE_e09l.bmp"
# image bg p12_MARE_e09m = "images/event cg/12/MARE_e09m.bmp"

# image bg p6_a1 = "images/event cg/06/a1.bmp"
# image bg p6_a2 = "images/event cg/06/a2.bmp"
# image bg p6_a3 = "images/event cg/06/a3.bmp"

# image bg p13_lisite = "images/event cg/13/lisite.bmp"
# image bg p13_lisite02 = "images/event cg/13/lisite02.bmp"

# image bg p14_xiangzi_a = "images/event cg/14/xiangzi_a.bmp"
# image bg p14_xiangzi_s = "images/event cg/14/xiangzi_s.bmp"

# image bg p15_MARE_e03k = "images/event cg/15/MARE_e03k.bmp"
# image bg p15_MARE_e03m = "images/event cg/15/MARE_e03m.bmp"
# image bg p15_MARE_e03n = "images/event cg/15/MARE_e03n.bmp"
# image bg p15_MARE_e03o = "images/event cg/15/MARE_e03o.bmp"

# image bg p16_MARE_e08a = "images/event cg/16/MARE_e08a.bmp"
# image bg p16_MARE_e08b = "images/event cg/16/MARE_e08b.bmp"

# image bg p17_MARE_h01a = "images/event cg/17/MARE_h01a.bmp"
# image bg p17_MARE_h01b = "images/event cg/17/MARE_h01b.bmp"
# image bg p17_MARE_h01c = "images/event cg/17/MARE_h01c.bmp"
# image bg p17_MARE_h01d = "images/event cg/17/MARE_h01d.bmp"
# image bg p17_MARE_h01e = "images/event cg/17/MARE_h01e.bmp"
# image bg p17_MARE_h01f = "images/event cg/17/MARE_h01f.bmp"
# image bg p17_MARE_h01g = "images/event cg/17/MARE_h01g.bmp"
# image bg p17_MARE_h01h = "images/event cg/17/MARE_h01h.bmp"
# image bg p17_MARE_h01i = "images/event cg/17/MARE_h01i.bmp"
# image bg p17_MARE_h01j = "images/event cg/17/MARE_h01j.bmp"
# image bg p17_MARE_h01k = "images/event cg/17/MARE_h01k.bmp"

# image bg p18_MARE_h02a = "images/event cg/18/MARE_h02a.bmp"
# image bg p18_MARE_h02b = "images/event cg/18/MARE_h02b.bmp"
# image bg p18_MARE_h02c = "images/event cg/18/MARE_h02c.bmp"
# image bg p18_MARE_h02d = "images/event cg/18/MARE_h02d.bmp"
# image bg p18_MARE_h02e = "images/event cg/18/MARE_h02e.bmp"
# image bg p18_MARE_h02g = "images/event cg/18/MARE_h02g.bmp"
# image bg p18_MARE_h02h = "images/event cg/18/MARE_h02h.bmp"
# image bg p18_MARE_h02i = "images/event cg/18/MARE_h02i.bmp"
# image bg p18_MARE_h02j = "images/event cg/18/MARE_h02j.bmp"

# image bg p19_MARE_e05g = "images/event cg/19/MARE_e05g.bmp"
# image bg p19_MARE_e05h = "images/event cg/19/MARE_e05h.bmp"
# image bg p19_MARE_e05i = "images/event cg/19/MARE_e05i.bmp"

# image bg p20_MARE_e07a = "images/event cg/20/MARE_e07a.bmp"
# image bg p20_MARE_e07b = "images/event cg/20/MARE_e07b.bmp"

# image bg p21_MARE_e11a = "images/event cg/21/MARE_e11a.bmp"
# image bg p21_MARE_e11b = "images/event cg/21/MARE_e11b.bmp"
# image bg p21_MARE_e11c = "images/event cg/21/MARE_e11c.bmp"
# image bg p21_MARE_e11d = "images/event cg/21/MARE_e11d.bmp"

# image bg p22_MARE_e06a = "images/event cg/22/MARE_e06a.bmp"

image bg xuzhang01 = "images/xuzhang01.bmp"
image bg xuzhang02 = "images/xuzhang02.bmp"
image bg xuzhang = "images/xuzhang.bmp"
image bg shenshe = "images/shenshe.bmp"
image bg weilan = "images/weilan.bmp"
image bg ssjd01 = "images/ssjd01.bmp"
image bg yinghuashu = "images/yinghuashu.bmp"
image bg guanjingtai = "images/guanjingtai.bmp"
image bg xingkong = "images/xingkong.bmp"
image bg white = "ui/white.png"
image bg diyizhang = "images/diyizhang.bmp"
image bg guanjingtai2 = "images/guanjingtai2.bmp"
image bg xuexiao = "images/xuexiao.bmp"
image bg dierzhang = "images/dierzhang.bmp"
image bg huanghun = "images/huanghun.bmp"
image bg xiangzijia = "images/xiangzijia.bmp"
image bg xiangzijia02 = "images/xiangzijia02.bmp"
image bg xuanguan = "images/xuanguan.bmp"
image bg myroom_before = "images/myroom_before.bmp"
image bg huanghun02 = "images/huanghun02.bmp"
image bg myroom_after = "images/myroom_after.bmp"
image bg meng01 = "images/meng01.bmp"
image bg disanzhang = "images/disanzhang.bmp"
image bg canting = "images/canting.bmp"
image bg keting = "images/keting.bmp"
image bg linggan = "images/linggan.bmp"
image bg jiedao01 = "images/jiedao01.bmp"
image bg jiedao02 = "images/jiedao02.bmp"
image bg jiedao03 = "images/jiedao03.bmp"
image bg jiedao04 = "images/jiedao04.bmp"
image bg xingkong02 = "images/xingkong02.bmp"
image bg disizhang = "images/disizhang.bmp"
image bg yun = "images/yun.bmp"
image bg xzj_morning = "images/xzj_morning.bmp"
image bg xg_morning = "images/xg_morning.bmp"
image bg chumen01 = "images/chumen01.bmp"
image bg chumen02 = "images/chumen02.bmp"
image bg chumen03 = "images/chumen03.bmp"
image bg jiaoxuelou = "images/jiaoxuelou.bmp"
image bg guodao = "images/guodao.bmp"
image bg jiaoshi = "images/jiaoshi.bmp"
image bg jiaoshi_mohu = "images/jiaoshi_mohu.bmp"
image bg jiaoshizhongwu = "images/jiaoshizhongwu.bmp"
image bg zoulangzhongwu = "images/zoulangzhongwu.bmp"
image bg loutizhongwu = "images/loutizhongwu.bmp"
image bg tiantai = "images/tiantai.bmp"
image bg shangke = "images/shangke.bmp"
image bg diwuzhang = "images/diwuzhang.bmp"
image bg shitang = "images/shitang.bmp"
image bg jiaoxuelou_huanghun = "images/jiaoxuelou_huanghun.bmp"
image bg louti_huanghun = "images/louti_huanghun.bmp"
image bg jiaoshi_huanghun = "images/jiaoshi_huanghun.bmp"
image bg xuexiao_huanghun = "images/xuexiao_huanghun.bmp"
image bg xuanguan_wanshang = "images/xuanguan_wanshang.bmp"
image bg xingkong_wan = "images/xingkong_wan.bmp"
image bg chuangtai = "images/chuangtai.bmp"
image bg huiyi = "images/huiyi.bmp"
image bg anger01 = "images/anger01.bmp"
image bg happy01 = "images/happy01.bmp"
image bg normal01 = "images/normal01.bmp"
image bg shame01 = "images/shame01.bmp"
image bg shame02 = "images/shame02.bmp"
image bg smile01 = "images/smile.bmp"
image bg surprise01 = "images/surprise01.bmp"
image bg guanjingtai03 = "images/guanjingtai03.bmp"
image bg xingkong04 = "images/xingkong04.bmp"
image bg yinghuashu02 = "images/nav_background.png"
image bg diliuzhang = "images/diliuzhang.bmp"
image bg xiaomen_mohu = "images/xiaomen_mohu.bmp"
image bg diqizhang = "images/diqizhang.bmp"
image bg haibian = "images/haibian.bmp"
image bg haitian = "images/haitian.bmp"
image bg shadi = "images/shadi.bmp"
image bg haitan_huanghun = "images/haitan_huanghun.bmp"
image bg my_haibian = "images/my_haibian.bmp"
image bg my_huanghun2 = "images/my_huanghun2.bmp"
image bg dibazhang = "images/dibazhang.bmp"
image bg jiedao1 = "images/jiedao1.bmp"
image bg shenshe_zao = "images/shenshe_zao.bmp"
image bg wunv_anger01 = "images/wunv_anger01.bmp"
image bg wunv_happy01 = "images/wunv_happy01.bmp"
image bg wunv_normal01 = "images/wunv_normal01.bmp"
image bg wunv_shame01 = "images/wunv_shame01.bmp"
image bg wunv_smile01 = "images/wunv_smile01.bmp"
image bg wunv_surprise01 = "images/wunv_surprise01.bmp"
image bg wunv_wunai01= "images/wunv_wunai01.bmp"
image bg shenshe_huanghun = "images/shenshe_huanghun.bmp"
image bg shenshe_daolu01 = "images/shenshe_daolu01.bmp"
image bg shenshe_daolu02 = "images/shenshe_daolu02.bmp"
image bg shenshe_wanjing = "images/shenshe_wanjing.bmp"
image bg dijiuzhang = "images/dijiuzhang.bmp"
image bg jidian01 = "images/jidian01.bmp"
image bg jidian03 = "images/jidian03.bmp"
image bg xz_shenshe01 = "images/xz_shenshe01.bmp"
image bg jitai = "images/jitai.bmp"
image bg shangke = "images/shangke.bmp"
image bg ssjd01 = "images/ssjd01.bmp"
image bg ssjd02 = "images/ssjd02.bmp"
image bg xingxiangyi = "images/xingxiangyi.bmp"
image bg huiyi_xinwei = "images/huiyi_xinwei.bmp"
image bg huiyi_sad = "images/huiyi_sad.png"
image bg dishizhang = "images/dishizhang.bmp"
image bg yinghuashu_zao = "images/yinghuashu_zao.bmp"
image bg shipin = "images/shipin.bmp"
image bg keting_huanghun = "images/keting_huanghun.bmp"
image bg canting_huanghun = "images/canting_huanghun.bmp"
image bg dishiyizhang = "images/dishiyizhang.bmp"
image bg zhuigan01 = "images/zhuigan01.bmp"
image bg zhuigan02 = "images/zhuigan02.bmp"
image bg xiaoshi_smile01 = "images/a3.bmp"
image bg xiaoshi_sad01 = "images/a2.bmp"
image bg xiaoshi_cry01 = "images/a1.bmp"
image bg MARE_e02a = "images/MARE_e02a.bmp"
image bg MARE_e02b = "images/MARE_e02b.bmp"
image bg MARE_e02c = "images/MARE_e02c.bmp"
image bg MARE_e02d = "images/MARE_e02d.bmp"
image bg MARE_e02e = "images/MARE_e02e.bmp"
image bg MARE_e02f = "images/MARE_e02f.bmp"
image bg MARE_e02g = "images/MARE_e02g.bmp"
image bg MARE_e02h = "images/MARE_e02h.bmp"
image bg KOMOMO_e06a = "images/KOMOMO_e06a.bmp"
image bg KOMOMO_e06b = "images/KOMOMO_e06b.bmp"
image bg KOMOMO_e06c = "images/KOMOMO_e06c.bmp"
image bg KOMOMO_e06d = "images/KOMOMO_e06d.bmp"
image bg KOMOMO_e06e = "images/KOMOMO_e06e.bmp"
image bg xing = "images/xing.bmp"
image bg chaqu = "images/chaqu.bmp"
image bg bg_end = "images/bg_end.bmp"
image bg zhaopian = "images/zhaopian.bmp"
image bg zuizhongzhang01 = "images/zuizhongzhang01.bmp"
image bg zuizhongzhang02 = "images/zuizhongzhang02.bmp"
image bg zuizhongzhang03 = "images/zuizhongzhang03.bmp"
image bg zuizhongzhang04 = "images/zuizhongzhang04.bmp"
image bg xue = "images/xue.bmp"
image bg yinghuashu_xue = "images/yinghuashu_xue.bmp"
image bg jiedao_xue = "images/jiedao_xue.bmp"
image bg shujian = "images/shujian.bmp"
image bg jiedao_xue02 = "images/jiedao_xue02.bmp"
image bg xue_huanghun = "images/xue_huanghun.bmp"
image bg yinghuashu_xue02 = "images/yinghuashu_xue02.bmp"
image bg jiedao_xue03 = "images/jiedao_xue03.bmp"
image bg MARE_e09a = "images/MARE_e09a.bmp"
image bg MARE_e09b = "images/MARE_e09b.bmp"
image bg MARE_e09c = "images/MARE_e09c.bmp"
image bg MARE_e09d = "images/MARE_e09d.bmp"
image bg MARE_e09e = "images/MARE_e09e.bmp"
image bg MARE_e09i = "images/MARE_e09i.bmp"
image bg MARE_e09j = "images/MARE_e09j.bmp"
image bg MARE_e09l = "images/MARE_e09l.bmp"
image bg MARE_e09m = "images/MARE_e09m.bmp"
image bg jieshu = "images/jieshu.bmp"
image bg lisite = "images/lisite.bmp"
image bg lisite02 = "images/lisite02.bmp"
image bg xiangzi_s = "images/xiangzi_s.bmp"
image bg xiangzi_a = "images/xiangzi_a.bmp"
image bg yugao = "images/yugao.bmp"
image bg xing01 = "images/xing01.bmp"
image bg xuexue01 = "images/YUKI_e03a6.bmp"
image bg xuexue02 = "images/YUKI_e03b6.bmp"
image bg xuexue03 = "images/YUKI_e03c6.bmp"
image bg xuexue04 = "images/YUKI_e03e6.bmp"
image bg xuexue05 = "images/YUKI_e03f6.bmp"
image bg xuetian = "images/xuetian.bmp"
image bg fan01 = "images/fan01.bmp"
image bg fan02 = "images/fan02.bmp"
image bg fan03 = "images/YUKI_e01a2.bmp"
image bg fan04 = "images/YUKI_e01b2.bmp"
image bg fan05 = "images/YUKI_e01c2.bmp"
image bg fan06 = "images/YUKI_e01d2.bmp"
image bg fan07 = "images/fan07.bmp"
image bg fan08 = "images/fan08.bmp"
image bg fan09 = "images/fan09.bmp"
image bg fan10 = "images/fan10.bmp"
image bg fan11 = "images/fan11.bmp"
image bg fan12 = "images/fan12.bmp"
image bg fan13 = "images/fan13.bmp"
image bg fan14 = "images/fan14.bmp"
image bg fan15 = "images/fan15.bmp"
image bg fan16 = "images/fan16.bmp"
image bg fan17 = "images/fan17.bmp"
image bg fan18 = "images/fan18.bmp"
image bg fan19 = "images/fan19.bmp"
image bg fan20 = "images/fan20.bmp"
image bg fan21 = "images/fan21.bmp"
image bg fan22 = "images/fan22.bmp"
image bg fan23 = "images/fan23.bmp"
image bg fan24 = "images/fan24.bmp"
image bg fan25 = "images/YUKI_e02a1.bmp"
image bg dayback = "images/dayback.bmp"
image bg fan26 = "images/fan26.bmp"
image bg fan27 = "images/ETC_e01a1.bmp"
image bg fan28 = "images/fan28.bmp"
image bg fan29 = "images/ETC_e01c1.bmp"
image bg fan30 = "images/fan30.bmp"
image bg fan32 = "images/fan32.bmp"
image bg fan33 = "images/fan33.bmp"
image bg fan34 = "images/fan34.bmp"
image bg fan35 = "images/fan35.bmp"
image bg fan36 = "images/fan36.bmp"
image bg fan37 = "images/fan37.bmp"
image bg fan38 = "images/fan38.bmp"
image bg fan39 = "images/fan39.bmp"
image bg fan40 = "images/fan40.bmp"
image bg fan41 = "images/fan41.bmp"
image bg fan42 = "images/fan42.bmp"
image bg fan43 = "images/YUKI_e01a4.bmp"
image bg fan44 = "images/YUKI_e01b4.bmp"
image bg fan45 = "images/fan45.bmp"
image bg fan46 = "images/YUKI_e02b1.bmp"
image bg fan47 = "images/fan47.bmp"
image bg fan48 = "images/ETC_e01b1.bmp"
image bg fan49 = "images/fan49.bmp"
image bg fan50 = "images/KORONA_e01a1.bmp"
image bg fan51 = "images/KORONA_e01b1.bmp"
image bg fan52 = "images/KORONA_e01d1.bmp"
image bg fan53 = "images/KORONA_e01c1.bmp"
image bg fan54 = "images/KORONA_e01f1.bmp"
image bg fan55 = "images/fan55.bmp"
image bg fan56 = "images/fan56.bmp"
image bg fan57 = "images/fan57.bmp"
image bg fan58 = "images/fan58.bmp"
image bg fan59 = "images/fan59.bmp"
image bg fan60 = "images/ICHIKA_e01a3.bmp"
image bg fan61 = "images/fan61.bmp"
image bg fan62 = "images/ICHIKA_e01c3.bmp"
image bg fan63 = "images/ICHIKA_e01b3.bmp"
image bg fan64 = "images/ICHIKA_e01d2.bmp"
image bg fan65 = "images/fan65.bmp"
image bg fan66 = "images/fan66.bmp"
image bg fan67 = "images/fan67.bmp"
image bg fan68 = "images/fan68.bmp"
image bg fan69 = "images/ETC_e100a.bmp"
image bg fan70 = "images/fan70.bmp"
image bg fan71 = "images/ETC_e102a.bmp"
image bg fan72 = "images/fan72.bmp"
image bg fan73 = "images/ETC_e02a.bmp"
image bg fan74 = "images/fan74.bmp"
image bg fan75 = "images/fan75.bmp"
image bg fan76 = "images/ETC_e02b.bmp"
image bg fan77 = "images/ETC_e02c.bmp"
image bg fan78 = "images/fan78.bmp"
image bg fan79 = "images/fan79.bmp"
image bg fan80 = "images/fan80.bmp"
image bg fan81 = "images/ETC_e03a1.bmp"
image bg fan82 = "images/ETC_e03a2.bmp"
image bg fan83 = "images/ETC_e03a3.bmp"
image bg fan84 = "images/ETC_e03b2.bmp"
image bg fan85 = "images/ETC_e03c3.bmp"
image bg fan86 = "images/ETC_e03d3.bmp"
image bg fan87 = "images/fan87.bmp"
image bg fan88 = "images/fan88.bmp"
image bg fan89 = "images/fan89.bmp"
image bg fan90 = "images/fan90.bmp"
image bg fan91 = "images/ETC_e04a.bmp"
image bg fan92 = "images/ETC_e04d.bmp"
image bg fan93 = "images/ETC_e04b.bmp"
image bg fan94 = "images/ETC_e04e.bmp"
image bg fan95 = "images/ETC_e101b.bmp"
image bg fan96 = "images/YUKI_e02c1.bmp"
image bg fan97 = "images/KORONA_e01a2.bmp"
image bg fan98 = "images/KORONA_e01e2.bmp"
image bg fan99 = "images/KORONA_e01c2.bmp"
image bg fan100 = "images/KORONA_e01d2.bmp"
image bg fan101 = "images/KORONA_e01b2.bmp"
image bg fan102 = "images/KORONA_e01f2.bmp"
image bg fan103 = "images/ETC_e01d1.bmp"
image bg fan104 = "images/ETC_e01e1.bmp"
image bg fan105 = "images/fan105.bmp"
image bg fan106 = "images/fan106.bmp"
image bg fan107 = "images/KORONA_e02a2.bmp"
image bg fan108 = "images/KORONA_e02c2.bmp"
image bg fan109 = "images/KORONA_e02b2.bmp"
image bg fan110 = "images/fan110.bmp"
image bg fan111 = "images/fan111.bmp"
image bg fan112 = "images/fan112.bmp"
image bg fan113 = "images/fan113.bmp"
image bg fan114 = "images/fan114.bmp"
image bg fan115 = "images/YUKI_e03b5.bmp"
image bg fan116 = "images/fan116.bmp"
image bg fan117 = "images/KOSAME_e02b.bmp"
image bg fan118 = "images/KOSAME_e02d.bmp"
image bg fan119 = "images/KOSAME_e02c.bmp"
image bg fan120 = "images/fan120.bmp"
image bg fan121 = "images/KOSAME_e03a.bmp"
image bg fan122 = "images/KOSAME_e03b.bmp"
image bg fan123 = "images/KOSAME_e03g.bmp"
image bg fan124 = "images/KOSAME_e03h.bmp"
image bg fan125 = "images/KOSAME_e02g.bmp"
image bg fan126 = "images/KOSAME_e02f.bmp"
image bg fan127 = "images/KOMOMO_e04a.bmp"
image bg fan128 = "images/KOMOMO_e04b.bmp"
image bg fan129 = "images/KOMOMO_e04d.bmp"
image bg fan130 = "images/KOMOMO_e04c.bmp"
image bg fan131 = "images/KOMOMO_e04e.bmp"
image bg fan132 = "images/KOMOMO_e04f.bmp"
image bg fan133 = "images/KOMOMO_e05a.bmp"
image bg fan134 = "images/KOMOMO_e05b.bmp"
image bg fan135 = "images/KOMOMO_e05d.bmp"
image bg fan136 = "images/KOMOMO_e05c.bmp"
image bg fan137 = "images/fan137.bmp"
image bg fan138 = "images/SD_012a.bmp"
image bg fan139 = "images/SD_012b.bmp"
image bg fan140 = "images/SD_012c.bmp"
image bg fan141 = "images/SD_012d.bmp"
image bg fan142 = "images/SD_012e.bmp"
image bg fan143 = "images/fan143.bmp"
image bg fan144 = "images/ICHIKA_e01a1.bmp"
image bg fan145 = "images/ICHIKA_e03a1.bmp"
image bg fan146 = "images/ICHIKA_e03b1.bmp"
image bg fan147 = "images/ICHIKA_e03c1.bmp"
image bg fan148 = "images/ICHIKA_e03d2.bmp"
image bg fan149 = "images/ICHIKA_e03a2.bmp"
image bg fan150 = "images/ICHIKA_e03b2.bmp"
image bg fan151 = "images/ICHIKA_e03e2.bmp"
image bg fan152 = "images/fan152.bmp"
image bg fan153 = "images/ICHIKA_e06a1.bmp"
image bg fan154 = "images/ICHIKA_e06a2.bmp"
image bg fan155 = "images/ICHIKA_e06b2.bmp"
image bg fan156 = "images/ICHIKA_e06c2.bmp"
image bg fan157 = "images/ICHIKA_e06d2.bmp"
image bg fan158 = "images/ICHIKA_e06e3.bmp"
image bg fan159 = "images/fan159.bmp"
image bg fan160 = "images/SD_011a.bmp"
image bg fan161 = "images/SD_011b.bmp"
image bg fan162 = "images/SD_011c.bmp"
image bg fan163 = "images/SD_011d.bmp"
image bg fan164 = "images/SD_011e.bmp"
image bg fan165 = "images/fan165.bmp"
image bg fan166 = "images/fan166.bmp"
image bg fan167 = "images/fan167.bmp"
image bg fan168 = "images/SD_100a.bmp"
image bg fan169 = "images/SD_100b.bmp"
image bg fan170 = "images/SD_100c.bmp"
image bg fan171 = "images/SD_100d.bmp"
image bg fan172 = "images/SD_100e.bmp"
image bg fan173 = "images/SD_100f.bmp"
image bg fan174 = "images/SD_101a.bmp"
image bg fan175 = "images/SD_101b.bmp"
image bg fan176 = "images/SD_101c.bmp"
image bg fan177 = "images/SD_101d.bmp"
image bg fan178 = "images/SD_101e.bmp"
image bg fan179 = "images/ETC_e200a.bmp"
image bg fan180 = "images/KOTORI_e02a1.bmp"
image bg fan181 = "images/KOTORI_e02a2.bmp"
image bg fan182 = "images/KOTORI_e02c2.bmp"
image bg fan183 = "images/KOTORI_e02c3.bmp"
image bg fan184 = "images/KOTORI_e02b2.bmp"
image bg fan185 = "images/KOTORI_e02a3.bmp"
image bg fan186 = "images/KOTORI_e02c1.bmp"
image bg fan187 = "images/KOTORI_e02d1.bmp"
image bg fan188 = "images/KOTORI_e05a.bmp"
image bg fan189 = "images/KOTORI_e05b.bmp"
image bg fan190 = "images/KOTORI_e05c.bmp"
image bg fan191 = "images/KOTORI_e05d.bmp"
image bg fan192 = "images/SD_601a.bmp"
image bg fan193 = "images/SD_601b.bmp"
image bg fan194 = "images/SD_601c.bmp"
image bg fan195 = "images/SD_601d.bmp"
image bg fan196 = "images/SD_601e.bmp"
image bg fan197 = "images/SD_601f.bmp"
image bg fan198 = "images/SD_601g.bmp"
image bg fan199 = "images/KOTORI_e03d3.bmp"
image bg fan200 = "images/KOTORI_e03a1.bmp"
image bg fan201 = "images/KOTORI_e03b1.bmp"
image bg fan202 = "images/KOTORI_e03b2.bmp"
image bg fan203 = "images/KOTORI_e03c2.bmp"
image bg fan204 = "images/KOTORI_e03d2.bmp"
image bg fan205 = "images/KOTORI_e03a3.bmp"
image bg fan206 = "images/KOTORI_e03b3.bmp"
image bg fan207 = "images/KOTORI_e03e1.bmp"
image bg fan208 = "images/KOTORI_e03c3.bmp"
image bg fan209 = "images/KOTORI_e03c6.bmp"
image bg fan210 = "images/KOTORI_e03c4.bmp"
image bg fan211 = "images/KOTORI_e03e4.bmp"
image bg fan212 = "images/KOTORI_e03e7.bmp"
image bg fan213 = "images/KOTORI_e03e9.bmp"
image bg fan214 = "images/KOTORI_e03e6.bmp"
image bg fan215 = "images/KOTORI_e03ea.bmp"
image bg fan216 = "images/KOTORI_e03b4.bmp"
image bg fan217 = "images/KOTORI_e03a4.bmp"
image bg fan218 = "images/KOTORI_e03a7.bmp"
image bg fan219 = "images/KOTORI_e03a8.bmp"
image bg fan220 = "images/KOTORI_e03b8.bmp"
image bg fan221 = "images/KOTORI_e03e8.bmp"
image bg fan222 = "images/KOTORI_e03e5.bmp"
image bg fan223 = "images/KOTORI_e03eb.bmp"
image bg fan224 = "images/fan224.bmp"
image bg fan225 = "images/fan225.bmp"
image bg fan226 = "images/SD_104a.bmp"
image bg fan227 = "images/SD_104b.bmp"
image bg fan228 = "images/SD_104c.bmp"
image bg fan229 = "images/fan229.bmp"
image bg fan230 = "images/SD_104d.bmp"
image bg fan231 = "images/fan231.bmp"
image bg fan232 = "images/fan232.bmp"
image bg fan233 = "images/KORONA_e02d2.bmp"
image bg fan234 = "images/SD_501a.bmp"
image bg fan235 = "images/SD_501b.bmp"
image bg fan236 = "images/SD_501c.bmp"
image bg fan237 = "images/SD_501d.bmp"
image bg fan238 = "images/KORONA_e08a.bmp"
image bg fan239 = "images/KORONA_e08b.bmp"
image bg fan240 = "images/KORONA_e08c.bmp"
image bg fan241 = "images/KORONA_e08d.bmp"
image bg fan242 = "images/fan242.bmp"
image bg fan243 = "images/KORONA_e03a.bmp"
image bg fan244 = "images/KORONA_e03d.bmp"
image bg fan245 = "images/KORONA_e03b.bmp"
image bg fan246 = "images/fan246.bmp"
image bg fan247 = "images/fan247.bmp"
image bg fan248 = "images/ETC_FD_e02c.bmp"
image bg fan249 = "images/ETC_FD_e02a.bmp"
image bg fan250 = "images/ETC_FD_e02e.bmp"
image bg fan251 = "images/ETC_FD_e02d.bmp"
image bg fan252 = "images/ETC_FD_e02f.bmp"
image bg fan253 = "images/KOTORI_e01c3.bmp"
image bg fan254 = "images/KOTORI_e01a3.bmp"
image bg fan255 = "images/ETC_FD_e02k.bmp"
image bg fan256 = "images/ETC_FD_e02m.bmp"
image bg fan257 = "images/ETC_FD_e02l.bmp"
image bg fan258 = "images/ETC_FD_e02p.bmp"
image bg fan259 = "images/ETC_e03c.bmp"
image bg fan260 = "images/cut_FD_e05_30.bmp"
image bg fan261 = "images/ETC_e03d.bmp"
image bg fan262 = "images/cut_FD_e05_10.bmp"
image bg fan263 = "images/cut_FD_e05_20.bmp"
image bg fan264 = "images/fan264.bmp"
image bg fan265 = "images/fan265.bmp"
image bg fan266 = "images/fan266.bmp"
image bg fan267 = "images/fan267.bmp"
image bg fan268 = "images/ETC_e115a.bmp"
image bg fan269 = "images/fan269.bmp"
image bg fan270 = "images/fan270.bmp"
image bg fan271 = "images/ICHIKA_e05a.bmp"
image bg fan272 = "images/ICHIKA_e05b.bmp"
image bg fan273 = "images/ICHIKA_e05c.bmp"
image bg fan274 = "images/fan274.bmp"
image bg fan275 = "images/ICHIKA_e05d.bmp"
image bg fan276 = "images/fan276.bmp"
image bg fan277 = "images/ETC_e05a.bmp"
image bg fan278 = "images/ETC_FD_e01a.bmp"
image bg fan279 = "images/ETC_FD_e01b.bmp"
image bg fan280 = "images/fan280.bmp"
image bg fan281 = "images/ICHIKA_e04a.bmp"
image bg fan282 = "images/ICHIKA_e04b.bmp"
image bg fan283 = "images/fan283.bmp"
image bg fan284 = "images/ICHIKA_e04c.bmp"
image bg fan285 = "images/ICHIKA_e04d.bmp"
image bg fan286 = "images/ICHIKA_e04e.bmp"
image bg fan287 = "images/fan287.bmp"
image bg fan288 = "images/fan288.bmp"
image bg fan289 = "images/SD_401a.bmp"
image bg fan290 = "images/SD_401c.bmp"
image bg fan291 = "images/fan291.bmp"
image bg fan292 = "images/ETC_e113a.bmp"
image bg fan293 = "images/YUKI_e01c4.bmp"
image bg fan294 = "images/YUKI_e01d4.bmp"
image bg fan295 = "images/fan295.bmp"
image bg fan296 = "images/fan296.bmp"
image bg fan297 = "images/SD_401i.bmp"
image bg fan298 = "images/fan298.bmp"
image bg fan299 = "images/SD_401j.bmp"
image bg fan300 = "images/fan300.bmp"
image bg fan301 = "images/fan301.bmp"
image bg fan302 = "images/fan302.bmp"
image bg fan303 = "images/RINNE_e02a1.bmp"
image bg fan304 = "images/RINNE_e02b1.bmp"
image bg fan305 = "images/RINNE_e02c1.bmp"
image bg fan306 = "images/RINNE_e02d2.bmp"
image bg fan307 = "images/fan307.bmp"
image bg fan308 = "images/fan308.bmp"
image bg fan309 = "images/fan309.bmp"
image bg fan310 = "images/SD_103a.bmp"
image bg fan311 = "images/SD_103b.bmp"
image bg fan312 = "images/SD_103c.bmp"
image bg fan313 = "images/SD_103d.bmp"
image bg fan314 = "images/SD_103e.bmp"
image bg fan315 = "images/fan315.bmp"
image bg fan316 = "images/RINNE_e02d1.bmp"
image bg fan317 = "images/fan317.bmp"
image bg fan318 = "images/fan318.bmp"
image bg fan324 = "images/SD_103f.bmp"
image bg fan325 = "images/SD_103g.bmp"
image bg fan326 = "images/SD_103h.bmp"
image bg fan327 = "images/SD_103i.bmp"
image bg fan328 = "images/SD_602a.bmp"
image bg fan329 = "images/SD_602b.bmp"
image bg fan330 = "images/SD_602c.bmp"
image bg fan331 = "images/SD_602d.bmp"
image bg fan332 = "images/SD_602e.bmp"
image bg fan333 = "images/SD_602f.bmp"
image bg fan334 = "images/SD_602g.bmp"
image bg fan335 = "images/SD_602h.bmp"
image bg fan336 = "images/fan336.bmp"
image bg fan337 = "images/YUKI_e01e2.bmp"
image bg fan338 = "images/YUKI_e01e4.bmp"
image bg fan339 = "images/RINNE_e04a.bmp"
image bg fan340 = "images/RINNE_e04c.bmp"
image bg fan341 = "images/RINNE_e04b.bmp"
image bg fan342 = "images/RINNE_e04d.bmp"
image bg fan343 = "images/fan343.bmp"
image bg fan344 = "images/SD_403a.bmp"
image bg fan345 = "images/SD_403b.bmp"
image bg fan346 = "images/SD_404a.bmp"
image bg fan347 = "images/RINNE_e05a1.bmp"
image bg fan348 = "images/RINNE_e05b1.bmp"
image bg fan349 = "images/RINNE_e05c1.bmp"
image bg fan350 = "images/RINNE_e05a2.bmp"
image bg fan351 = "images/RINNE_e05d2.bmp"
image bg fan352 = "images/RINNE_e05b2.bmp"
image bg fan353 = "images/fan353.bmp"
image bg fan354 = "images/fan354.bmp"
image bg fan355 = "images/RINNE_e06a.bmp"
image bg fan356 = "images/RINNE_e06b.bmp"
image bg fan357 = "images/RINNE_e06c.bmp"
image bg fan358 = "images/RINNE_e03a.bmp"
image bg fan359 = "images/RINNE_e08a1.bmp"
image bg fan360 = "images/RINNE_e08b1.bmp"
image bg fan361 = "images/RINNE_e08c1.bmp"
image bg fan362 = "images/RINNE_e08d1.bmp"
image bg fan363 = "images/RINNE_e08a2.bmp"
image bg fan364 = "images/RINNE_e08b2.bmp"
image bg fan365 = "images/RINNE_e08d2.bmp"
image bg fan366 = "images/RINNE_e08e2.bmp"
image bg fan367 = "images/RINNE_e08f2.bmp"
image bg fan368 = "images/RINNE_e01c2.bmp"
image bg fan369 = "images/RINNE_e01a2.bmp"
image bg fan370 = "images/RINNE_e01b2.bmp"
image bg fan371 = "images/fan371.bmp"
image bg fan372 = "images/RINNE_e10a.bmp"
image bg fan373 = "images/RINNE_e10b.bmp"
image bg fan374 = "images/RINNE_e10c.bmp"
image bg fan375 = "images/RINNE_e10d.bmp"
image bg fan376 = "images/ETC_e03b.bmp"
image bg fan377 = "images/ETC_e03a.bmp"
image bg fan378 = "images/MARE_FD_e02a.bmp"
image bg fan379 = "images/MARE_FD_e02b.bmp"
image bg fan380 = "images/MARE_FD_e02c.bmp"
image bg fan381 = "images/MARE_FD_e03a.bmp"
image bg fan382 = "images/MARE_FD_e03b.bmp"
image bg fan383 = "images/MARE_FD_e03g.bmp"
image bg fan384 = "images/MARE_FD_e03e.bmp"
image bg fan385 = "images/MARE_FD_e03f.bmp"
image bg fan386 = "images/MARE_FD_e03c.bmp"
image bg fan387 = "images/MARE_FD_e03d.bmp"
image bg fan388 = "images/MARE_FD_e03k.bmp"
image bg fan389 = "images/MARE_FD_e03i.bmp"
image bg fan390 = "images/MARE_FD_e03j.bmp"
image bg fan391 = "images/fan391.bmp"
image bg fan392 = "images/fan392.bmp"
image bg fan393 = "images/KORONA_e04a1.bmp"
image bg fan394 = "images/KORONA_e04b1.bmp"
image bg fan395 = "images/KORONA_e04c1.bmp"
image bg fan396 = "images/KORONA_e04a3.bmp"
image bg fan397 = "images/KORONA_e04b3.bmp"
image bg fan398 = "images/KORONA_e04d3.bmp"
image bg fan399 = "images/fan399.bmp"
image bg fan400 = "images/fan400.bmp"
image bg fan401 = "images/KORONA_e04e1.bmp"
image bg fan402 = "images/KORONA_e04c3.bmp"
image bg fan403 = "images/KORONA_e05a.bmp"
image bg fan404 = "images/KORONA_e05b.bmp"
image bg fan405 = "images/KORONA_e05c.bmp"
image bg fan406 = "images/KORONA_e05d.bmp"
image bg fan407 = "images/KORONA_e05e.bmp"
image bg fan408 = "images/KORONA_e06a.bmp"
image bg fan409 = "images/KORONA_e06c.bmp"
image bg fan410 = "images/SD_103j.bmp"
image bg fan411 = "images/SD_103k.bmp"
image bg fan412 = "images/SD_103l.bmp"
image bg fan413 = "images/SD_103m.bmp"
image bg fan414 = "images/SD_103n.bmp"
image bg fan415 = "images/SD_103o.bmp"
image bg fan416 = "images/YUKI_e04a4.bmp"
image bg fan417 = "images/YUKI_e04b4.bmp"
image bg fan418 = "images/fan418.bmp"
image bg fan419 = "images/fan419.bmp"
image bg fan420 = "images/fan420.bmp"
image bg fan421 = "images/YUKI_e05a.bmp"
image bg fan422 = "images/YUKI_e05b.bmp"
image bg fan423 = "images/YUKI_e06a.bmp"
image bg fan424 = "images/YUKI_e06b.bmp"
image bg fan425 = "images/YUKI_e06c.bmp"
image bg fan426 = "images/YUKI_e06d.bmp"
image bg fan427 = "images/fan427.bmp"
image bg fan428 = "images/YUKI_e04c4.bmp"
image bg fan429 = "images/YUKI_e04d4.bmp"
image bg fan430 = "images/YUKI_e04e4.bmp"
image bg fan431 = "images/ETC_e101c.bmp"
image bg fan432 = "images/fan432.bmp"
image bg fan433 = "images/YUKI_e07a1.bmp"
image bg fan434 = "images/YUKI_e07d1.bmp"
image bg fan435 = "images/YUKI_e07b1.bmp"
image bg fan436 = "images/YUKI_e07c1.bmp"
image bg fan437 = "images/YUKI_e07e1.bmp"
image bg fan438 = "images/YUKI_e15a.bmp"
image bg fan439 = "images/YUKI_e15b.bmp"
image bg fan440 = "images/YUKI_e15c.bmp"
image bg fan441 = "images/YUKI_e15d.bmp"
image bg fan442 = "images/YUKI_e15e.bmp"
image bg fan443 = "images/fan443.bmp"
image bg fan444 = "images/fan444.bmp"
image bg fan445 = "images/fan445.bmp"
image bg fan446 = "images/YUKI_e04f4.bmp"
image bg fan447 = "images/YUKI_e04g4.bmp"
image bg fan448 = "images/fan448.bmp"
image bg fan449 = "images/YUKI_e08a1.bmp"
image bg fan450 = "images/YUKI_e08d1.bmp"
image bg fan451 = "images/YUKI_e08b1.bmp"
image bg fan452 = "images/ETC_e130a.bmp"
image bg fan453 = "images/YUKI_e08c1.bmp"
image bg fan454 = "images/ETC_e130b.bmp"
image bg fan455 = "images/YUKI_e16c.bmp"
image bg fan456 = "images/ETC_e131a.bmp"
image bg fan457 = "images/fan457.bmp"
image bg fan458 = "images/fan458.bmp"
image bg fan459 = "images/fan459.bmp"
image bg fan460 = "images/fan460.bmp"
image bg fan461 = "images/YUKI_e09b1.bmp"
image bg fan462 = "images/YUKI_e09a1.bmp"
image bg fan463 = "images/fan463.bmp"
image bg fan464 = "images/YUKI_e09d2.bmp"
image bg fan465 = "images/fan465.bmp"
image bg fan466 = "images/YUKI_e09e2.bmp"
image bg fan467 = "images/YUKI_e08a2.bmp"
image bg fan468 = "images/YUKI_e08d2.bmp"
image bg fan469 = "images/YUKI_e08e2.bmp"
image bg fan470 = "images/YUKI_e08f2.bmp"
image bg fan471 = "images/YUKI_e08b2.bmp"
image bg fan472 = "images/YUKI_e08c2.bmp"
image bg fan473 = "images/YUKI_e08g2.bmp"
image bg fan474 = "images/YUKI_e10a1.bmp"
image bg fan475 = "images/YUKI_e10b1.bmp"
image bg fan476 = "images/YUKI_e10b2.bmp"
image bg fan477 = "images/YUKI_e10d2.bmp"
image bg fan478 = "images/YUKI_e10c2.bmp"
image bg fan479 = "images/YUKI_e11a.bmp"
image bg fan480 = "images/YUKI_e11b.bmp"
image bg fan481 = "images/MARE_FD_e01a.bmp"
image bg fan482 = "images/MARE_FD_e01b.bmp"
image bg fan483 = "images/MARE_FD_e01c.bmp"
image bg fan484 = "images/MARE_FD_e01d.bmp"
image bg fan485 = "images/MARE_FD_e01e.bmp"
image bg fan486 = "images/MARE_FD_e01f.bmp"
image bg fan487 = "images/YUKI_e07b2.bmp"
image bg fan488 = "images/YUKI_e07e2.bmp"
image bg fan489 = "images/YUKI_e07d2.bmp"
image bg fan490 = "images/YUKI_e07c2.bmp"
image bg fan491 = "images/fan491.bmp"
image bg fan492 = "images/YUKI_e12a1.bmp"
image bg fan493 = "images/YUKI_e12b1.bmp"
image bg fan494 = "images/YUKI_e03e7.bmp"
image bg fan495 = "images/YUKI_e03f7.bmp"
image bg fan496 = "images/YUKI_e12c2.bmp"
image bg fan497 = "images/YUKI_e12d2.bmp"
image bg fan498 = "images/YUKI_e12d3.bmp"
image bg fan499 = "images/YUKI_e12d1.bmp"
image bg fan500 = "images/YUKI_e12c3.bmp"
image bg fan501 = "images/YUKI_e12a3.bmp"
image bg fan502 = "images/YUKI_e12b3.bmp"
image bg fan503 = "images/YUKI_e12e3.bmp"
image bg fan504 = "images/YUKI_e14a.bmp"
image bg fan505 = "images/YUKI_e14b.bmp"
image bg fan506 = "images/YUKI_e14c.bmp"
image bg fan507 = "images/YUKI_e12a4.bmp"
image bg fan508 = "images/YUKI_e13a.bmp"
image bg fan509 = "images/YUKI_e13b.bmp"
image bg fan509 = "images/YUKI_e13c.bmp"
image bg fan510 = "images/YUKI_e13d.bmp"
image bg fan511 = "images/YUKI_e13f.bmp"
image bg fan512 = "images/YUKI_e13e.bmp"
image bg fan513 = "images/endback1.bmp"
image bg fan514 = "images/fan514.bmp"
image bg fan515 = "images/ETC_e04c.bmp"
image bg fan516 = "images/fan516.bmp"
image bg fan517 = "images/EF_e08_B.bmp"
image bg fan518 = "images/fan518.bmp"
image bg fan519 = "images/fan519.bmp"
image bg fan520 = "images/fan520.bmp"
image bg fan521 = "images/SD_301a.bmp"
image bg fan522 = "images/SD_301b.bmp"
image bg fan523 = "images/SD_301c.bmp"
image bg fan524 = "images/SD_301d.bmp"
image bg fan525 = "images/SD_301e.bmp"
image bg fan526 = "images/SD_301f.bmp"
image bg fan527 = "images/fan527.bmp"
image bg fan528 = "images/KOTORI_e01a1.bmp"
image bg fan529 = "images/KOTORI_e01b1.bmp"
image bg fan530 = "images/KOTORI_e01c1.bmp"
image bg fan531 = "images/fan531.bmp"
image bg fan532 = "images/KOTORI_e04b.bmp"
image bg fan533 = "images/KOTORI_e04e.bmp"
image bg fan534 = "images/KOTORI_e04a.bmp"
image bg fan535 = "images/KOTORI_e04c.bmp"
image bg fan536 = "images/KOTORI_e04d.bmp"
image bg fan537 = "images/ETC_e300a.bmp"
image bg fan538 = "images/fan538.bmp"
image bg fan539 = "images/fan539.bmp"
image bg fan540 = "images/fan540.bmp"
image bg fan541 = "images/fan541.bmp"
image bg fan542 = "images/fan542.bmp"
image bg fan543 = "images/fan543.bmp"
image bg fan544 = "images/fan544.bmp"
image bg fan545 = "images/KOTORI_e01d1.bmp"
image bg fan546 = "images/fan546.bmp"
image bg fan547 = "images/fan547.bmp"
image bg fan548 = "images/sd_402_10.bmp"
image bg fan549 = "images/sd_402_20.bmp"
image bg fan550 = "images/sd_402_30.bmp"

image bg third02 = "images/third02.png"
image bg third01 = "images/third01.png"
image bg third03 = "images/third03.png"
image bg third04 = "images/third04.png"
image bg third05 = "images/third05.png"
image bg third06 = "images/third06.png"
image bg third07 = "images/third07.png"
image bg third08 = "images/third08.png"
image bg third09 = "images/third09.png"
image bg third10 = "images/third10.png"
image bg third11 = "images/third11.png"
image bg third12 = "images/third12.png"
image bg third13 = "images/third13.png"
image bg third14 = "images/third14.png"
image bg third15 = "images/third15.png"
image bg third16 = "images/third16.png"
image bg third17 = "images/third17.png"
image bg third18 = "images/third18.png"
image bg third19 = "images/third19.png"
image bg third20 = "images/third20.png"
image bg third21 = "images/third21.png"
image bg third22 = "images/third22.png"
image bg third23 = "images/third23.png"
image bg third24 = "images/third24.png"
image bg third25 = "images/third25.png"
image bg third26 = "images/third26.png"
image bg third27 = "images/third27.png"
image bg third28 = "images/third28.png"
image bg third29 = "images/third29.png"
image bg third30 = "images/third30.png"
image bg third31 = "images/third31.png"
image bg third32 = "images/third32.png"
image bg third33 = "images/third33.bmp"
image bg third34 = "images/third34.bmp"
image bg third35 = "images/third35.png"

image pic p01 = "images/p01.bmp"
image pic p02 = "images/p02.bmp"
image pic p03 = "images/p03.bmp"
image pic p04 = "images/p04.bmp"
image pic p05 = "images/p05.bmp"
image pic p06 = "images/p06.bmp"
image pic p07 = "images/p07.bmp"
image pic p08 = "images/p08.bmp"
image pic p09 = "images/p09.bmp"

image pic p11 = "images/p11.bmp"
image pic p12 = "images/p12.bmp"
image pic p13 = "images/p13.bmp"
image pic p14 = "images/p14.bmp"
image pic p15 = "images/p15.bmp"
image pic p16 = "images/p16.bmp"
image pic p17 = "images/p17.bmp"
image pic p18 = "images/p18.bmp"
image pic p19 = "images/p19.bmp"
image pic p20 = "images/p20.bmp"
image pic p21 = "images/p21.bmp"
image pic p22 = "images/p22.bmp"
image pic p23 = "images/p23.bmp"
image pic p24 = "images/p24.bmp"
image pic p25 = "images/p25.bmp"

image logo = "images/logo.png"
image logo01 = "images/logo01.png"
image logo02 = "images/logo02.png"
image logo03 = "images/logo03.png"
image logo04 = "images/logo04.png"
image logo05 = "images/logo05.png"
image logo06 = "images/logo06.png"
image logo07 = "images/logo07.png"
image logo08 = "images/logo08.png"
image logo09 = "images/logo09.png"
image logo10 = "images/logo10.png"

image log1 = "images/log1.png"
image log2 = "images/log2.png"
image log3 = "images/log3.png"
image log4 = "images/log4.png"
image log5 = "images/log5.png"
image log6 = "images/log6.png"
image log7 = "images/log7.png"
image log8 = "images/log8.png"
image log9 = "images/log9.png"
image log10 = "images/log10.png"
image log11 = "images/log11.png"
image log12 = "images/log12.png"
image log13 = "images/log13.png"
image log14 = "images/log14.png"
image log15 = "images/log15.png"


image txt1 = "images/txt1.png"
image txt2 = "images/txt2.png"
image txt3 = "images/txt3.png"
image txt4 = "images/txt4.png"
image txt5 = "images/txt5.png"
image txt6 = "images/txt6.png"
image txt7 = "images/txt7.png"
image txt8 = "images/txt8.png"
image txt9 = "images/txt9.png"
image txt10 = "images/txt10.png"
image txt11 = "images/txt11.png"
image txt12 = "images/txt12.png"

image last01 = "images/last01.bmp"
image last02 = "images/last02.bmp"
image last03 = "images/last03.bmp"
image last04 = "images/last04.bmp"
image last05 = "images/last05.bmp"

image wan01 = "images/wan01.png"
image wan02 = "images/wan02.png"

image bg gallery = "ui/a_cg_s1.bmp"

image wsblur:
    "ui/235blur.png"
image wsround:
    "ui/EF_e08_D.png"
image tri_black:
    "images/tri_black.png"
image tri_white:
    "images/tri_white.png"
image chain1:
    "images/chain_1.png"
image chain2:
    "images/chain_2.png"
image chain3:
    "images/chain_3.png"
image cut_pentblack:
    "images/cut_02_black.png"
image cut_pentwhite:
    "images/cut_02_white.png"
image bslash1:
    "images/slashb1.png"
    0.1
    "images/empty.png" with Dissolve(0.1, alpha=True)
image bslash2:
    "images/slashb2.png"
    0.1
    "images/empty.png" with Dissolve(0.1, alpha=True)
image bslash3:
    "images/slashb3.png"
    0.1
    "images/empty.png" with Dissolve(0.1, alpha=True)


image ctc_animation:
    xalign 0.92 yalign 0.92
    "ani/prompt1.png"
    0.1
    "ani/prompt2.png"
    0.1
    "ani/prompt3.png"
    0.1
    "ani/prompt4.png"
    0.1
    "ani/prompt5.png"
    0.1
    "ani/prompt6.png"
    0.1
    "ani/prompt7.png"
    0.1
    "ani/prompt8.png"
    0.1
    "ani/prompt9.png"
    0.1
    "ani/prompt10.png"
    0.1
    "ani/prompt11.png"
    0.1
    "ani/prompt12.png"
    0.1
    "ani/prompt13.png"
    0.1
    "ani/prompt14.png"
    0.1
    "ani/prompt15.png"
    0.1
    "ani/prompt16.png"
    0.1
    "ani/prompt17.png"
    0.1
    "ani/prompt18.png"
    0.1
    "ani/prompt19.png"
    0.1
    "ani/prompt20.png"
    0.1
    "ani/prompt21.png"
    0.1
    "ani/prompt22.png"
    0.1
    "ani/prompt23.png"
    0.1
    "ani/prompt24.png"
    repeat

image yangmu:
    "ani/yangmu/bu_effect22_U_3.bmp"
    0.35
    "ani/yangmu/bu_effect22_U_4.bmp"
    0.35
    repeat

image jian:
    "ani/jian/mag_ef300_01.png"
    0.02
    "ani/jian/mag_ef300_02.png"
    0.04
    "ani/jian/mag_ef300_03.png"
    0.06
    "ani/jian/mag_ef300_04.png"
    0.08
    repeat 1

image daokan:
    "ani/daokan/act_ef012_01.bmp"
    0.02
    "ani/daokan/act_ef012_02.bmp"
    0.02
    "ani/daokan/act_ef012_03.bmp"
    0.02
    "ani/daokan/act_ef012_04.bmp"
    0.02
    "ani/daokan/act_ef012_05.bmp"
    0.02
    "ani/daokan/act_ef012_04.bmp"
    0.02
    "ani/daokan/act_ef012_03.bmp"
    0.02
    "ani/daokan/act_ef012_02.bmp"
    0.02
    "ani/daokan/act_ef012_01.bmp"
    0.02
    repeat 1

image fennu:
    "ani/fennu/bu_effect7_F_1.bmp"
    0.02
    "ani/fennu/bu_effect7_F_2.bmp"
    0.02
    repeat 1

image daokan2:
    "ani/daokan/act_ef013_01.bmp"
    0.02
    "ani/daokan/act_ef013_02.bmp"
    0.02
    "ani/daokan/act_ef013_03.bmp"
    0.02
    "ani/daokan/act_ef013_04.bmp"
    0.02
    "ani/daokan/act_ef013_01.bmp"
    0.02
    "ani/daokan/act_ef013_04.bmp"
    0.02
    "ani/daokan/act_ef013_03.bmp"
    0.02
    "ani/daokan/act_ef013_02.bmp"
    0.02
    "ani/daokan/act_ef013_01.bmp"
    0.02
    repeat 1

image sanlianshe:
    "ani/sanlian/mag_ef310_03.bmp"
    0.06
    "ani/sanlian/mag_ef310_04.bmp"
    0.08
    "ani/sanlian/mag_ef310_11.bmp"
    0.02
    "ani/sanlian/mag_ef310_12.bmp"
    0.04
    "ani/sanlian/mag_ef310_13.bmp"
    0.06
    "ani/sanlian/mag_ef310_14.bmp"
    0.08
    "ani/sanlian/mag_ef310_21.bmp"
    0.02
    "ani/sanlian/mag_ef310_22.bmp"
    0.04
    "ani/sanlian/mag_ef310_23.bmp"
    0.06
    "ani/sanlian/mag_ef310_24.bmp"
    0.08
    repeat 1

image yangmu2:
    "ani/yangmu/bu_effect22_U_5.bmp"
    0.35
    "ani/yangmu/bu_effect22_U_6.bmp"
    0.35
    repeat

image han:
    "ani/han/bu_effect6_U_3.bmp"
    0.1
    "ani/han/bu_effect6_U_4.bmp"
    0.1
    repeat

image yun:
    "ani/yun/bu_effect25_U_1.bmp"
    0.1
    "ani/yun/bu_effect25_U_2.bmp"
    0.1
    repeat

image yun1:
    "ani/yun1/bu_effect16_U_1.bmp"
    0.1
    "ani/yun1/bu_effect16_U_2.bmp"
    0.1
    repeat


image liuxing:
    "ani/liuxing/cut_e17_10.bmp"
    0.1
    "ani/liuxing/cut_e17_11.bmp"
    0.1
    "ani/liuxing/cut_e17_12.bmp"
    0.1
    "ani/liuxing/cut_e17_13.bmp"
    0.1
    "ani/liuxing/cut_e17_14.bmp"
    0.1
    "ani/liuxing/cut_e17_15.bmp"
    0.1
    "ani/liuxing/cut_e17_16.bmp"
    0.1
    "ani/liuxing/cut_e17_17.bmp"
    0.1
    "ani/liuxing/cut_e17_18.bmp"
    0.1
    "ani/liuxing/cut_e17_19.bmp"
    0.1
    repeat 1

image wflash:
    "ui/flash.png"
    0.1
    "ui/empty.png" with Dissolve(0.5, alpha=True)

transform fei:
    yalign 0.4
    easein 2.0 yalign 0.35
    pause 0.2
    easein 2.0 yalign 0.4
    pause 0.2
    repeat

transform pageflip:
    "images/system/gallery/book/bg_1.png"
    0.1
    "images/system/gallery/book/bg_2.png"
    0.1
    "images/system/gallery/book/bg_3.png"
    0.1
    "images/system/gallery/book/bg_4.png"
    0.1
    "images/system/gallery/book/bg_5.png"
    0.1
    "images/system/gallery/book/bg_6.png"
    0.1
    "images/system/gallery/book/bg_7.png"
    0.1
    "images/system/gallery/book/bg_8.png"

transform pageflip2:
    "images/system/gallery/book/bg_8.png"
    0.1
    "images/system/gallery/book/bg_7.png"
    0.1
    "images/system/gallery/book/bg_6.png"
    0.1
    "images/system/gallery/book/bg_5.png"
    0.1
    "images/system/gallery/book/bg_4.png"
    0.1
    "images/system/gallery/book/bg_3.png"
    0.1
    "images/system/gallery/book/bg_2.png"
    0.1
    "images/system/gallery/book/bg_1.png"


transform galleryfade2:
    alpha 0
    1
    linear 0.5 alpha 1
    on hide:
        linear 0.5 alpha 0
        
transform galleryhide:
    on hide:
        ease 0.5 ycenter 2.0

transform vignettehide:
    on hide:
        linear 0.3 alpha 0.0

transform galleryfade:
    xcenter 0.5 ycenter 2.0
    ease 0.5 ycenter 0.5
    on hide:
        ease 0.5 ycenter 2.0

transform galleryfade2:
    alpha 0
    1
    linear 0.5 alpha 1
    on hide:
        linear 0.5 alpha 0

transform fpoverlay:
    alpha 0
    0.25
    ease 0.5 alpha 1.0
    on hide:
        ease 0.5 alpha 0

transform encyctitletext:
    xalign 0.05 yalign 0.05 alpha 0
    ease 0.5 alpha 1
    on hide:
        ease 0.5 alpha 0

transform shan:
    alpha 1.0
    easein 0.1 alpha 0.5
    pause 0.05
    easein 0.1 alpha 1.0
    pause 0.05
    repeat

transform mainlogoslide1:
    alpha 0.0 xalign 0.83 yalign 0.05
    easein 4.0 alpha 1.0 yalign 0.15


transform titleslide1:
    alpha 0.0 xalign 0.95 yalign 0.4
    easein 4.0 alpha 1.0 yalign 0.3


transform feizou:
    alpha 1.0 yalign 0.4
    easein 0.5 alpha 0.0 yalign 0.0


transform mainlogoslide:
    alpha 0.0 xalign 0.5 yalign 0.08
    easein 2.0 alpha 1.0 yalign 0.12



transform main:
    alpha 0.0 xalign 0.5 yalign 0.6
    easein 3.0 alpha 1.0 yalign 0.5

transform titleslide:
    alpha 0.0 xalign 0.08 yalign 0.2
    easein 2.0 alpha 1.0 yalign 0.16

transform titleslide2:
    alpha 0.0 xalign 0.08 yalign 0.1
    easein 2.0 alpha 1.0 yalign 0.06

transform quickfade:
    on show:
        alpha 0.0
        linear 0.1 alpha 1.0
    on hide:
        linear 0.1 alpha 0.0
        
transform basicfade:
    on show:
        alpha 0.0
        linear 0.3 alpha 1.0
    on hide:
        linear 0.3 alpha 0.0

transform basicfade_ctd:
    on show:
        alpha 0.0 yalign 1.8
        linear 0.6 alpha 1.0 yalign 1.0
    on hide:
        alpha 1.0 yalign 1.0
        linear 0.6 alpha 0.0 yalign 1.8

transform basicfade_ltc:
    on show:
        alpha 0.0 xalign 0.4 yalign 1.0
        easein .6 alpha 1.0 xalign 0.5
    on hide:
        easeout .6 alpha 0.0 xalign 0.4

transform basicfade_ltc1:
    on show:
        alpha 0.0 xalign 0.25 yalign 1.2
        easein .6 alpha 1.0 xalign 0.5
    on hide:
        easeout .6 alpha 0.0 xalign 0.25

transform basicfade_ltc2:
    on show:
        alpha 0.0 xalign 0.4 yalign 1.5
        easein .6 alpha 1.0 xalign 0.5
    on hide:
        easeout .6 alpha 0.0 xalign 0.4

transform basicfade_ltc3:
    on show:
        alpha 0.0 xalign 0.4 yalign 1.2
        easein .6 alpha 1.0 xalign 0.5
    on hide:
        easeout .6 alpha 0.0 xalign 0.4

transform basicfade_ltc4:
    on show:
        alpha 0.0 xalign 0.25 yalign 1.5
        easein .6 alpha 1.0 xalign 0.5
    on hide:
        easeout .6 alpha 0.0 xalign 0.25

transform basicfade_ctl:
    on show:
        alpha 0.0 xalign 0.5 yalign 1.0
        easein .6 alpha 1.0 xalign 0.35
    on hide:
        easeout .6 alpha 0.0 xalign 0.5

transform basicfade_ctl1:
    on show:
        alpha 0.0 xalign 0.5 yalign 1.2
        easein .6 alpha 1.0 xalign 0.35
    on hide:
        easeout .6 alpha 0.0 xalign 0.5

transform basicfade_ctl2:
    on show:
        alpha 0.0 xalign 0.5 yalign 1.5
        easein .6 alpha 1.0 xalign 0.35
    on hide:
        easeout .6 alpha 0.0 xalign 0.5

transform basicfade_ctl3:
    on show:
        alpha 0.0 xalign 0.5 yalign 1.2
        easein .6 alpha 1.0 xalign 0.25
    on hide:
        easeout .6 alpha 0.0 xalign 0.5

transform basicfade_ctu:
    on show:
        alpha 0.0 xalign 0.5 yalign 0.5
        easein 1.0 alpha 1.0 yalign 0.35
    on hide:
        easeout 1.0 alpha 0.0 yalign 0.5

transform basicfade_rtc:
    on show:
        alpha 0.0 xalign 0.6 yalign 1.0
        easein .6 alpha 1.0 xalign 0.5
    on hide:
        easeout .6 alpha 0.0 xalign 0.6

transform basicfade_rtc1:
    on show:
        alpha 0.0 xalign 0.75 yalign 1.2
        easein .6 alpha 1.0 xalign 0.5
    on hide:
        easeout .6 alpha 0.0 xalign 0.75

transform basicfade_rtc2:
    on show:
        alpha 0.0 xalign 0.6 yalign 1.2
        easein .6 alpha 1.0 xalign 0.5
    on hide:
        easeout .6 alpha 0.0 xalign 0.6

transform back:
    subpixel True
    align (.5, .5)
    zoom 1.2

transform backslide:
    subpixel True

transform basicfade_rtc3:
    on show:
        alpha 0.0 xalign 0.6 yalign 1.5
        easein .6 alpha 1.0 xalign 0.5
    on hide:
        easeout .6 alpha 0.0 xalign 0.6

transform basicfade_ctr:
    on show:
        alpha 0.0 xalign 0.5 yalign 1.0
        easein .6 alpha 1.0 xalign 0.65
    on hide:
        easeout .6 alpha 0.0 xalign 0.5

transform basicfade_otr:
    on show:
        alpha 0.0 xalign 1.0 yalign 0.2
        easein .6 alpha 1.0 xalign 0.9
    on hide:
        easeout .6 alpha 0.0 xalign 1.0

transform basicfade_otr1:
    on show:
        alpha 0.0 xalign 1.0 yalign 1.2
        easein .6 alpha 1.0 xalign 0.75
    on hide:
        easeout .6 alpha 0.0 xalign 1.0

transform basicfade_otr7:
    on show:
        alpha 0.0 xalign 0.9 yalign 1.0
        easein .6 alpha 1.0 xalign 0.75
    on hide:
        easeout .6 alpha 0.0 xalign 0.9

transform basicfade_otr8:
    on show:
        alpha 0.0 xalign 1.0 yalign 1.5
        easein .6 alpha 1.0 xalign 0.85
    on hide:
        easeout .6 alpha 0.0 xalign 1.0

transform basicfade_otr9:
    on show:
        alpha 0.0 xalign 1.0 yalign 1.2
        easein .6 alpha 1.0 xalign 0.95
    on hide:
        easeout .6 alpha 0.0 xalign 1.0

transform basicfade_otl:
    on show:
        alpha 0.0 xalign 0.0 yalign 0.2
        easein .6 alpha 1.0 xalign 0.1
    on hide:
        easeout .6 alpha 0.0 xalign 0.0

transform basicfade_otl1:
    on show:
        alpha 0.0 xalign 0.0 yalign 1.2
        easein .6 alpha 1.0 xalign 0.25
    on hide:
        easeout .6 alpha 0.0 xalign 0.0

transform basicfade_otr2:
    on show:
        alpha 0.0 xalign 1.0 yalign 1.0
        easein .6 alpha 1.0 xalign 0.85
    on hide:
        easeout .6 alpha 0.0 xalign 1.0

transform basicfade_otr3:
    on show:
        alpha 0.0 xalign 0.75 yalign 1.0
        easein .6 alpha 1.0 xalign 0.6
    on hide:
        easeout .6 alpha 0.0 xalign 1.0

transform basicfade_otl2:
    on show:
        alpha 0.0 xalign 0.0 yalign 1.0
        easein .6 alpha 1.0 xalign 0.15
    on hide:
        easeout .6 alpha 0.0 xalign 0.0

transform basicfade_otl7:
    on show:
        alpha 0.0 xalign 0.0 yalign 1.5
        easein .6 alpha 1.0 xalign 0.15
    on hide:
        easeout .6 alpha 0.0 xalign 0.0

transform basicfade_otl8:
    on show:
        alpha 0.0 xalign 0.0 yalign 1.5
        easein .6 alpha 1.0 xalign 0.25
    on hide:
        easeout .6 alpha 0.0 xalign 0.0

transform basicfade_otl0:
    on show:
        alpha 0.0 xalign 0.0 yalign 1.2
        easein .6 alpha 1.0 xalign 0.15
    on hide:
        easeout .6 alpha 0.0 xalign 0.0

transform basicfade_otl5:
    on show:
        alpha 0.0 xalign 0.0 yalign 1.0
        easein .6 alpha 1.0 xalign 0.1
    on hide:
        easeout .6 alpha 0.0 xalign 0.0

transform basicfade_otl6:
    on show:
        alpha 0.0 xalign 0.05 yalign 1.0
        easein .6 alpha 1.0 xalign 0.25
    on hide:
        easeout .6 alpha 0.0 xalign 0.05

transform basicfade_otl4:
    on show:
        alpha 0.0 xalign 0.0 yalign 1.0
        easein .6 alpha 1.0 xalign 0.35
    on hide:
        easeout .6 alpha 0.0 xalign 0.0

transform basicfade_otr4:
    on show:
        alpha 0.0 xalign 1.0 yalign 1.0
        easein .6 alpha 1.0 xalign 0.65
    on hide:
        easeout .6 alpha 0.0 xalign 1.0

transform basicfade_otr5:
    on show:
        alpha 0.0 xalign 1.3 yalign 1.0
        easein .6 alpha 1.0 xalign 1.0
    on hide:
        easeout .6 alpha 0.0 xalign 1.3

transform basicfade_otr6:
    on show:
        alpha 0.0 xalign 0.9 yalign 1.5
        easein .6 alpha 1.0 xalign 0.65
    on hide:
        easeout .6 alpha 0.0 xalign 0.9

transform basicfade_otl3:
    on show:
        alpha 0.0 xalign 0.0 yalign 1.0
        easein .6 alpha 1.0 xalign 0.1
    on hide:
        easeout .6 alpha 0.0 xalign 0.0

transform basicfade_otcr:
    on show:
        alpha 0.0 xalign 1.0 yalign 1.0
        easein .6 alpha 1.0 xalign 0.65
    on hide:
        easeout .6 alpha 0.0 xalign 1.0

transform basicfade_fei:
    on show:
        alpha 0.0 yalign 0.0
        easein .6 alpha 1.0 yalign 0.55
    on hide:
        linear .6 alpha 0.0 yalign 0.0

transform zoomin:
    ease 0.4 zoom 1.15

transform zoomout:
    zoom 1.15
    ease 0.4 zoom 1.0

transform basicfade_flu:
    yalign 1.0
    easein .25 yalign 1.5
    easein .25 yalign 1.0

transform basicfade_flu7:
    yalign 1.0
    easein .25 yalign 1.3
    easein .25 yalign 1.0

transform basicfade_flu8:
    yalign 1.2
    easein .25 yalign 1.5
    easein .25 yalign 1.2

transform basicfade_flu9:
    yalign 1.2
    easein .25 yalign 1.0
    easein .25 yalign 1.2

transform basicfade_flu10:
    yalign 1.2
    easein .25 yalign 1.0
    easein .25 yalign 1.2
    easein .25 yalign 1.0
    easein .25 yalign 1.2

transform basicfade_flu11:
    xalign 0.5
    easein .8 xalign 0.4
    easein .8 xalign 0.5
    easein .8 xalign 0.4
    easein .8 xalign 0.5

transform basicfade_flu12:
    yalign 1.2
    easein 0.1 yalign 1.0
    easein 0.1 yalign 1.2

transform basicfade_flu13:
    xalign 0.5
    easein .3 xalign 0.45
    easein .3 xalign 0.5
    easein .3 xalign 0.45
    easein .3 xalign 0.5

transform basicfade_flual:
    yalign 0.5
    easein .25 yalign 0.55
    easein .25 yalign 0.5

transform basicfade_flual3:
    yalign 0.6
    easein .25 yalign 0.7
    easein .25 yalign 0.6

transform basicfade_flual4:
    yalign 0.55
    easein .25 yalign 0.65
    easein .25 yalign 0.55

transform basicfade_flual2:
    yalign 0.55
    easein .25 yalign 0.6
    easein .25 yalign 0.55

transform basicfade_flud:
    yalign 1.0
    easein .25 yalign 1.5
    easein .25 yalign 1.0
    repeat 2

transform basicfade_flu4:
    yalign 1.2
    easein .25 yalign 1.6
    easein .25 yalign 1.2

transform basicfade_tiao:
    yalign 1.0
    easein .1 yalign 0.6
    easein .1 yalign 1.0

transform basicfade_tiao1:
    yalign 1.5
    easein .1 yalign 1.0
    easein .1 yalign 1.2

transform basicfade_tiao2:
    yalign 1.5
    easein .1 yalign 1.0
    easein .1 yalign 1.5

transform basicfade_tiao3:
    yalign 1.2
    easein .1 yalign 1.0
    easein .1 yalign 1.2

transform basicfade_flu2:
    yalign 1.0
    easein 0.4 yalign 1.6
    easein 0.4 yalign 1.0

transform basicfade_flu6:
    yalign 1.0
    easein 0.4 yalign 1.4
    easein 0.4 yalign 1.0

transform basicfade_flu3:
    yalign 1.5
    easein 0.3 yalign 1.8
    easein 0.3 yalign 1.5

transform basicfade_flu5:
    yalign 1.5
    easein 0.4 yalign 1.8
    easein 0.4 yalign 1.5

transform tan:
    xalign 0.35 yalign 0.23 alpha 1.0
    parallel:
        linear .6 xalign 0.3 yalign 0.2
    parallel:
        linear .6 alpha 0.0
    parallel:
        linear .6 zoom 1.15

transform tan2:
    xalign 0.35 yalign 0.1 alpha 1.0 xzoom -1
    parallel:
        linear .6 xalign 0.4 yalign 0.03
    parallel:
        linear .6 alpha 0.0
    parallel:
        linear .6 zoom 1.15

transform tan3:
    xalign 0.65 yalign 0.163 alpha 1.0
    parallel:
        linear .6 xalign 0.6 yalign 0.1
    parallel:
        linear .6 alpha 0.0
    parallel:
        linear .6 zoom 1.15

transform tan4:
    xalign 0.75 yalign 0.05 alpha 1.0 xzoom -1
    parallel:
        linear .6 xalign 0.8 yalign 0.0
    parallel:
        linear .6 alpha 0.0
    parallel:
        linear .6 zoom 1.15

transform tan5:
    xalign 0.65 yalign 0.05 alpha 1.0 xzoom -1
    parallel:
        linear .6 xalign 0.7 yalign 0.0
    parallel:
        linear .6 alpha 0.0
    parallel:
        linear .6 zoom 1.15

transform tan6:
    xalign 0.75 yalign 0.05 alpha 1.0 xzoom -1
    parallel:
        linear .6 xalign 0.65 yalign 0.0
    parallel:
        linear .6 alpha 0.0
    parallel:
        linear .6 zoom 1.15

transform tan7:
    xalign 0.78 yalign 0.05 alpha 1.0 xzoom -1
    parallel:
        linear .6 xalign 0.82 yalign 0.0
    parallel:
        linear .6 alpha 0.0
    parallel:
        linear .6 zoom 1.15

transform tan8:
    xalign 0.8 yalign 0.05 alpha 1.0 xzoom -1
    parallel:
        linear .6 xalign 0.82 yalign 0.0
    parallel:
        linear .6 alpha 0.0
    parallel:
        linear .6 zoom 1.15


transform show1:
    xalign 0.35 yalign 0.3 alpha 0.0
    easein .6 xalign 0.2 alpha 1.0

transform show2:
    xalign 0.85 yalign 0.3 alpha 0.0
    easein .6 xalign 0.7 alpha 1.0

transform basicfade_utc:
    on show:
        alpha 0.0 xalign 0.0 yalign 0.0
        easein .6 alpha 1.0 yalign 0.5
    on hide:
        easeout .6 alpha 0.0 yalign 1.0

transform otu:
    alpha 1.0 xalign 0.5 yalign 1.0
    linear 0.8 alpha 0.0 yalign 0.3

transform otu2:
    alpha 1.0 xalign 0.5 yalign 0.5
    linear 0.8 alpha 0.0 yalign 0.1

transform basicfade_dtc:
    on show:
        alpha 0.0 xalign 0.0 yalign 1.9
        easein 2.0 alpha 1.0 yalign 1.5
    on hide:
        easeout 2.0 alpha 0.0 yalign 1.9

transform basicfade_dtc1:
    on show:
        alpha 0.0 yalign 1.6
        easein .5 alpha 1.0 yalign 1.2
    on hide:
        easeout .5 alpha 0.0 yalign 1.6

transform basicfade_utc2:
    on show:
        alpha 0.0 xalign 0.5 yalign 0.0
        easein .6 alpha 1.0 yalign 0.6
    on hide:
        easeout .6 alpha 0.0 yalign 1.0

transform basicfade_utc3:
    on show:
        alpha 0.0 xalign 0.5 yalign 0.0 rotate 0.0
        easein .6 alpha 1.0 yalign 0.4
    on hide:
        parallel:
            linear 0.15 yalign 0.25
            pause 0.05
            easeout .5 alpha 0.0 yalign 1.0 
        parallel:
            linear 0.7 rotate 210

transform basicfade_ryrx:
    alpha 1.0
    linear 1.2 alpha 0.4
    linear 1.2 alpha 1.0
    repeat

transform centernozoom:
    xalign 0.5 yalign 0.5
    zoom 1.0
    ease 1.0 zoom 1.0

transform logo_slide01:
    alpha 0.0 xalign 0.75 yalign 0.8
    easein 2.0 alpha 1.0 yalign 0.83

transform logo_slide02:
    alpha 0.0 xalign 0.9 yalign 0.9
    easein 2.0 alpha 1.0 yalign 0.93

transform logo_slide03:
    alpha 0.0 xalign 0.85 yalign 0.8
    easein 2.0 alpha 1.0 yalign 0.83
