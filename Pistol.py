#------------------------------------------------------------------------------
# Project:     Zom-botapacolypse
# Name:        Pistol.py
# Purpose:     Pistol Object
# 
# Authors:     Matt Hahn, Michael Simon, Tim Richter
# Main Author: Matt Hahn
#
# Created:     12/10/2012
# Copyright:   (c) Matthew Hahn 2012
# Licence:     GSL
#------------------------------------------------------------------------------
import pygame, math, sys, random

class Pistol():
    def __init__(self, speed, position, screenSize):
        self.surfaces = []
        self.surfaces += [pygame.image.load("rsc/Pistol/pistol.png")]
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.radius = self.rect.width/2
        self.place(position)
        self.ammo = 20
        self.notBroken = True
        if pygame.mixer:
            self.gunshotSound = pygame.mixer.Sound("gunshot.wav")
        
    def  __str__(self):
        return "I'm a Pistol " + str(self.rect.center) + str(self.notBroken)
        
    def distToPoint(self, pt):
        x1 = self.rect[0]
        x2 = pt[0]
        y1 = self.rect[1]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
     
    def place(self, position):
        self.rect.center = position
        
    def checkLiving(self, projectile):       
        if projectile.ammo == 0:
            self.notBroken = False
           
    def collideMazeWall(self, mazeWall):
        if (self.rect.right > mazeWall.rect.left 
            and self.rect.left < mazeWall.rect.right):
            if (self.rect.bottom > mazeWall.rect.top and 
                self.rect.top < mazeWall.rect.bottom):
                (self.distToPoint(mazeWall.rect.center)
                    < self.radius + mazeWall.radius)

   
    def useDown(self):
        print "I've been used", str(self)
        
    def broken(self):
        print "I'm broken", str(self)
        
    def remove(self):
        print "I'm gone", str(self)
        