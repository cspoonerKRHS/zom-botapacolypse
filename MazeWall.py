#---------------------------------------------------------------
# Project:     Zom-botapacolyse
# Name:        MazeWall.py
# Purpose:     The Inner Walls
# 
# Authors:     Michael Simon, Matt Hahn, Tim Richter
# Main Author: Michael Simon
#
# Created:     12/10/12
# Copyright:   (c) Michael Simon 2012
# License:     BSD
#-------------------------------------------------------------------
import pygame, math

class MazeWall():
    # Attributes or Variables
    # surface
    # rect
    # distToCenter
    # screenWidth
    # screenHeight
    
    # Methods or Functions
    def __init__(self, blockSize, position):
        self.blockSize = blockSize
        self.surface = pygame.image.load("rsc/MazeWall/block4.png")
        self.surface = pygame.transform.scale(self.surface, [self.blockSize,self.blockSize])
        self.rect = self.surface.get_rect()
        self.radius = self.rect.width/2
        self.place(position)
        self.living = True
    
    def __str__(self):
        return "I am a wall" + str(self.rect.center)
    
    def place(self, position):
        self.rect.center = position
    
    def distToPoint(self, pt):
        x1 = self.rect.center[0]
        x2 = pt[0]
        y1 = self.rect.center[1]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
        #print "I'm near something ", str(other.rect.center)
    
        #return True
        
        
        #return False
        
        