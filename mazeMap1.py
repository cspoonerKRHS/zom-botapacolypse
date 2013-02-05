import pygame, math, sys
from MazeWall import MazeWall

class level():
    def __init__(self, level, screenSize):
        self.screenSize = screenSize
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.load(level)
        
        
    def load(self, level):
        self.mazeWalls = []
        mazeWallSize = 25
        
        geoMap="rsc/maps/"+ level
        geofile = open(geoMap, "r")
        lines = geofile.readlines()
        geofile.close()
        newlines = []
        self.nspawn = False
        
        for line in lines:
            newline = ""
            for character in line:
                if character != "\n":
                    newline += character
            newlines += [newline]
            
        for y, line in enumerate(newlines):
            for x, c in enumerate(line):
                if c == "m":
                    self.mazeWalls += [MazeWall([(x*mazeWallSize)+mazeWallSize/2, (y*mazeWallSize)+mazeWallSize/2])]
            