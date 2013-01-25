import pygame, math, sys
from Block import Block

class level():
    def __init__(self, level, screenSize):
        self.screenSize = screenSize
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.load(level)
        
        
    def load(self, level):
        geoMap="rcs/maps/"+ level +".lvl"
        thingMap="rcs/maps/"+ level +".tng"
        self.blocks = []
        self.fblocks = []
        self.wblocks = []
        self.dblocks = []
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
                if c == "w":
                    self.blocks += [MazeWall([(x*10)+5, (y*10)+5], self.screenSize,"rcs/mazeWall/mazeWall.png",(10,10))]
                
                    
        #----Done with file---
        
        thingfile = open(thingMap, "m")
        lines = thingfile.readlines()
        thingfile.close() 
        
        newlines = []
        
        for line in lines:
            newline = ""
            for character in line:
                if character != "\n":
                    newline += character
            newlines += [newline]
            