__author__ = 'dugging'
import os


class Inputting():
    @staticmethod
    def map(name, extension):
        #########NOT DONE
        filepath = os.path.join("Maps", name, ".", extension)
        file = open(filepath, "r")
        data = file.readlines()
        file.close()
        mapx = int(data[0])
        mapy = int(data[1])
        mapnums = []
        for x in range(mapx):
            mapnums.append([])
            for y in range(mapy):
                mapnums[x].append()
        for n in range(len(data) - 2):
            pass


class Outputting():
    @staticmethod
    def map(name, extension, mapdim, map):
        filepath = os.path.join("Maps", name, ".", extension)
        file = open(filepath, "w")
        file.write(mapdim[0])
        file.write("\n")
        file.write(mapdim[1])
        file.write("\n")
        for x in range(len(map)):
            for y in range(len(map[x])):
                file.write(map[x][y].ID)
                file.write("\n")
        file.close()