#-------------------------------------------------------------------
# Project:     Zom-botapacolyse
# Name:        gameover.py
# Purpose:     After death, game over
# 
# Authors:     Michael Simon, Matt Hahn, Tim Richter
# Main Author: Michael Simon
#
# Created:     02/14/13
# Copyright:   (c) Michael Simon 2012
# License:     GSL
#-------------------------------------------------------------------
import pygame, math


class GameOver():
    # Attributes or Variables
    # surface
    # rect
    # screenWidth
    # screenHeight

   
    
    # Methods or Functions
    def __init__(self, image, position, screenSize):
        self.surface = pygame.image.load(image)
        self.rect = self.surface.get_rect()
        self.radius = self.rect.width/2
        self.place(position)
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1] 
    
    def __str__(self):
        pass
    
    def place(self, position):
        self.rect = self.rect.move(position)
        

            
        
        