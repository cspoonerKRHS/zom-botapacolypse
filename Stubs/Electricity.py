#-------------------------------------------------------------------
# Project:     Zom-botapacolyse
# Name:        Electricity.py
# Purpose:     A Projectile
# 
# Authors:     Michael Simon, Matt Hahn, Tim Richter
# Main Author: Michael Simon
#
# Created:     12/10/12
# Copyright:   (c) Michael Simon 2012
# License:     GSL
#-------------------------------------------------------------------
import pygame, math

class Electricity():
    # Attributes or Variables
    # surface
    # rect
    # distToCenter
    # speed
    # screenWidth
    # screenHeight
    # living
    
    # Methods or Functions
    def __init__(self, speed, position):
        self.surfaces = []
        self.surfaces += [pygame.image.load("rsc/electricity/electricity.png")]
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.speed = speed
        self.place(position)
        self.notBroken = True
    
    
    def __str__(self):
        return "I am electricity" + str(self.rect.center) + str(self.notBroken)
    
    def place(self, position):
        print "I've moved to", position
    
    def move(self):
        print "I've moved", self.speed
    
    def distToPoint(self):
        print "I can see", str(distToPoint)
        
    def collideWall(self, screenWidth, screenHeight):
        print "Trying to hit screen walls", screenWidth, screenHeight
    
    
    def collideMazeWall(self, mazeWall):
        print "Trying to hit the maze wall"
        
    def collideAttackRobot(self, robot):
        print "Trying to collide with the robot"
        
    def collideAttackZomie(self, other):
        print "Trying to collide with the zombie"
   
    def remove(self):
        print "I am being removed from the game", self
                    
        #return True
        
        
        #return False
        
        