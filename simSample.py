import pyxel
import random


# Windowのサイズ（これ以上はデカくなりません）
WINDOW_H = 256
WINDOW_W = 256

# OffとDefの初期アライン
off_init_align = [[126, 180], [131, 181], [136, 181], [121, 181], [116, 181],
                  [126, 185], [126, 206],
                  [182, 181], [144, 185], [70, 181], [108, 185]]
def_init_align = [[124, 175], [138, 175], [112, 175],
                  [133, 156], [146, 156], [121, 156], [106, 156],
                  [184, 170], [68, 170],
                  [154, 136], [98, 136]]


class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Offense:
    def __init__(self, img_id, x, y):
        self.pos = Vec2(x, y)
        self.vec = 0
        self.img_off = img_id

    def update(self, x, y, dx):
        self.pos.x = x
        self.pos.y = y
        self.vec = dx


class Defense:
    def __init__(self, img_id, x, y):
        self.pos = Vec2(x, y)
        self.vec = 0
        self.img_def = img_id

    def update(self, x, y, dx):
        self.pos.x = x
        self.pos.y = y
        self.vec = dx


class App:
    def __init__(self):
        self.IMG_ID0 = 0
        self.left_click_flag = 0

        pyxel.init(WINDOW_W, WINDOW_H, caption="SHIMANO sample", fps=30)
        pyxel.load("my_resource.pyxres")

        pyxel.mouse(True)

        # make instance
        self.Offenses = []
        for align_o in off_init_align:
            self.Offenses.append(Offense(self.IMG_ID0, align_o[0], align_o[1]))
        self.Defenses = []
        for align_d in def_init_align:
            self.Defenses.append(Defense(self.IMG_ID0, align_d[0], align_d[1]))

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.left_click_flag = 1
        
        # ここの + or - の値を持ってるデータに上手くアジャストさせて更新すれば
        # それっぽいシミュレータになるはず？
        if self.left_click_flag == 1:
            for i in range(7, 11):
                self.Offenses[i].update(self.Offenses[i].pos.x,
                                        self.Offenses[i].pos.y-0.5,
                                        self.Offenses[i].vec)

    def draw(self):
        pyxel.cls(0)
        self.tilemap_draw()

        for Off in self.Offenses:
            pyxel.blt(Off.pos.x, Off.pos.y, Off.img_off, 18, 10, 4, 4, 0)
        for Def in self.Defenses:
            pyxel.blt(Def.pos.x, Def.pos.y, Def.img_def, 26, 10, 4, 4, 0)
    
    def tilemap_draw(self):
        # 指定したtm(template)番号の(u,v)座標から
        # サイズ(w,h)の大きさを(base_x,base_y)座標に描画する
        base_x = 0
        base_y = 0
        tm = 0
        u = 0
        v = 0
        w = 32
        h = 32
        pyxel.bltm(base_x, base_y, tm, u, v, w, h)


App()