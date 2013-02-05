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
    def __init__(self, position):
        self.surface = pygame.image.load("rsc/MazeWall/block4.png")
        self.surface = pygame.transform.scale(self.surface, [25,25])
        self.rect = self.surface.get_rect()
        self.radius = self.rect.width/2
        self.place(position)
    
    def __str__(self):
        return "I am a wall" + str(self.rect.center)
    
    def place(self, position):
        print "I'm staying at", position
        self.rect.center = position
    
    def distToPoint(self):
        print "I can see", str(distToPoint)
    
        #return True
        
        
        #return False
        
        