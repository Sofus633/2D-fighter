


class Attackhitbox:
    def __init__(self):
        self.hitboxes = []
    def frametodisplay(self):
        lst = []
        for hitbox in self.hitboxes:
            hitbox[1]  -= 1
            lst.append(hitbox[0])
        return lst