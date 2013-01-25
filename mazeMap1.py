import pygame, math, sys
from MazeWall import MazeWall

class level():
    def __init__(self, level, screenSize):
        self.load(level)
        
        
    def load(self, level)
        geofile="/rsc/maps/"+ level +".lvl"
        thingfile="/rsc/maps/"+ level +".tng"
        self.mazeWall = []
        geofile = open(geoMap, "r")
        lines = geofile.readlines()
        geofile.close()
        newlines = []
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
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
                    self.mazeWalls += [MazeWall([(x*10)+5, (y*10)+5], screenSize,"rcs/MazeWall/MazeWall.png",(10,10))]
  
        #----Done with file---
        
        thingfile = open(thingMap, "r")
        lines = thingfile.readlines()
        thingfile.close() 
        
        newlines = []
        
        for line in lines:
            newline = ""
            for character in line:
                if character != "\n":
                    newline += character
            newlines += [newline]
            
        for y, line in enumerate(newlines):
            for x, c in enumerate(line):
                if c == "p":
                    self.dblocks += [Block([(x*10)+5, (y*10)+5], screenSize,"rcs/imgs/block/spawnspace.png",(10,10))]
                    

                    
