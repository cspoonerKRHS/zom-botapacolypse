#-------------------------------------------------------------------
# Project:     Zom-botapacolyse
# Name:        Projectile.py
# Purpose:     A Projectile
# 
# Authors:     Michael Simon, Matt Hahn, Tim Richter
# Main Author: Tim Richter
#
# Created:     12/10/12
# Copyright:   (c) Tim Richter 2012
# License:     GSL
#-------------------------------------------------------------------
import pygame, math

class Projectile():
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
        self.surfaces += [pygame.image.load("rsc/projectile/projectile.png")]
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.speed = speed
        self.place(position)
        self.notBroken = True
    
    
    def __str__(self):
        return "I am a Projecile" + str(self.rect.center) + str(self.notBroken)
    
    def place(self, position):
        self.rect.center = position
        print "I've moved to", position
    
    def move(self):
        self.rect = self.rect.move(self.speed)
        print "I've moved", self.speed
    
    def distToPoint(self):
        print "I can see", str(distToPoint)
        
    def collideWall(self, screenWidth, screenHeight):
        print "Trying to hit screen walls", screenWidth, screenHeight
    
    def collideAttackMan(self, man):
        print "Trying to hit man"
    
    def collideMazeWall(self, mazeWall):
        print "Trying to hit the maze wall"
        
    def collideAttackRobot(self, robot):
        print "Trying to collide with the robot"
        
    def collideAttackZomie(self, other):
        print "Trying to collide with the zombie"
   
    def remove(self):
        print "I am being removed from the game", str(self)
                    
        #return True
        
        
        #return False
        
        