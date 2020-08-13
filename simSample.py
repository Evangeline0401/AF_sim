import pyxel
import random

WINDOW_H = 256
WINDOW_W = 256
CAT_H = 16
CAT_W = 16
ENEMY_H = 12
ENEMY_W = 12

off_init_align = [[121, 121], [169, 121], [75, 121], [121, 137], [121, 169]]


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

class cat:
    def __init__(self, img_id):
        self.pos = Vec2(0, 0)
        self.vec = 0
        self.img_cat = img_id

    def update(self, x, y, dx):
        self.pos.x = x
        self.pos.y = y
        self.vec = dx

class Ball:
    def __init__(self):
        self.pos = Vec2(0, 0)
        self.vec = 0
        self.size = 2
        self.speed = 3
        self.color = 10 # 0~15

    def update(self, x, y, dx, size, color):
        self.pos.x = x
        self.pos.y = y
        self.vec = dx
        self.size = size
        self.color = color


class App:
    def __init__(self):
        self.IMG_ID0_X = 121
        self.IMG_ID0_Y = 121
        self.IMG_ID0 = 0
        self.IMG_ID1 = 1
        self.IMG_ID2 = 2

        pyxel.init(WINDOW_W, WINDOW_H, caption="SHIMANO sample", fps=30)
        pyxel.load("my_resource.pyxres")

        pyxel.mouse(True)

        # make instance
        self.mcat = cat(self.IMG_ID1)
        self.Balls = []
        self.Offenses = []
        for align in off_init_align:
            self.Offenses.append(Offense(0, align[0], align[1]))
        self.Defenses = []

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        #if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
        self.Offenses[0].update(self.Offenses[0].pos.x+0.2,
                                self.Offenses[0].pos.y-0.5,
                                self.Offenses[0].vec)

        # ====== ctrl cat ======
        dx = pyxel.mouse_x - self.mcat.pos.x  # x軸方向の移動量(マウス座標 - cat座標)
        dy = pyxel.mouse_y - self.mcat.pos.y  # y軸方向の移動量(マウス座標 - cat座標)
        if dx != 0:
            self.mcat.update(pyxel.mouse_x, pyxel.mouse_y, dx) # 座標と向きを更新
        elif dy != 0:
            self.mcat.update(pyxel.mouse_x, pyxel.mouse_y, self.mcat.vec) # 座標のみ更新（真上or真下に移動）

    def draw(self):
        pyxel.cls(0)
        for Off in self.Offenses:
            pyxel.blt(Off.pos.x, Off.pos.y, Off.img_off, 0, 16, 16, 16, 1)

        # ======= draw cat ========
        if self.mcat.vec > 0:
            pyxel.blt(self.mcat.pos.x, self.mcat.pos.y, self.IMG_ID0, 0, 0, -CAT_W, CAT_H, 5)
        else:
            pyxel.blt(self.mcat.pos.x, self.mcat.pos.y, self.IMG_ID0, 0, 0, CAT_W, CAT_H, 5)


App()