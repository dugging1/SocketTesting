__author__ = 'dugging'


class Map():
    map = []

    def creategrid(self, mapx=8, mapy=8):
        for x in range(mapx):
            self.map.append([])
            for y in range(mapy):
                self.map[x].append(Tile())


class Tile():
    def __init__(self, initial="Bl", tileid=0):
        self.Initial = initial
        self.ID = tileid