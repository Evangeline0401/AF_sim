import pyxel
import random


# Windowのサイズ（これ以上はデカくなりません）
WINDOW_H = 256
WINDOW_W = 256

# OffとDefの初期アライン
off_init_align = [[121, 121], [169, 121], [75, 121], [121, 137], [121, 169]]
def_init_align = []


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
    def __init__(self, img_id):
        self.pos = Vec2(0, 0)
        self.vec = 0
        self.img_def = img_id

    def update(self, x, y, dx):
        self.pos.x = x
        self.pos.y = y
        self.vec = dx


class App:
    def __init__(self):
        #self.IMG_ID0_X = 121
        #self.IMG_ID0_Y = 121
        self.IMG_ID0 = 0
        self.left_click_flag = 0

        pyxel.init(WINDOW_W, WINDOW_H, caption="SHIMANO sample", fps=30)
        pyxel.load("my_resource.pyxres")

        pyxel.mouse(True)

        # make instance
        self.Offenses = []
        for align in off_init_align:
            self.Offenses.append(Offense(self.IMG_ID0, align[0], align[1]))
        self.Defenses = []

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.left_click_flag = 1
        
        # ここの + or - の値を持ってるデータに上手くアジャストさせて更新すれば
        # それっぽいシミュレータになるはず？
        if self.left_click_flag == 1:
            self.Offenses[0].update(self.Offenses[0].pos.x+0.2,
                                    self.Offenses[0].pos.y-0.5,
                                    self.Offenses[0].vec)

    def draw(self):
        pyxel.cls(0)
        self.tilemap_draw()

        for Off in self.Offenses:
            pyxel.blt(Off.pos.x, Off.pos.y, Off.img_off, 18, 10, 4, 4, 0)
    
    def tilemap_draw(self):
        base_x = 0
        base_y = 0
        tm = 0
        u = 0
        v = 0
        w = 32
        h = 32
        # 指定したtm(template)番号の(u,v)座標から
        # サイズ(w,h)の大きさを(base_x,base_y)座標に描画する
        pyxel.bltm(base_x, base_y, tm, u, v, w, h)


App()