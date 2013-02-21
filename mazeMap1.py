import pygame, math, sys
from MazeWall import MazeWall

class level():
    def __init__(self, level, screenSize):
        self.screenSize = screenSize
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.mazeWallSize = 25
        self.load(level)
        
    def load(self, level):
        self.mazeWalls = []
        
        
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
                    self.mazeWalls += [MazeWall(self.mazeWallSize, 
                                                [(x*self.mazeWallSize)+self.mazeWallSize/2, 
                                                 (y*self.mazeWallSize)+self.mazeWallSize/2])
                                                ]
            