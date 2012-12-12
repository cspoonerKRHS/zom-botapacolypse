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
    def __init__(self, speed, position):
        self.surfaces = []
        self.surfaces += [pygame.image.load("")]
        self.surfaces += [pygame.image.load("")]
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.place(position)
        self.notBroken = True
        if pygame.mixer:
            self.gunshotSound = pygame.mixer.Sound("gunshot.wav")
        
    def  __str__(self):
        return "I'm a ball " + str(self.rect.center) + str(self.speed) + str(self.living)
     
    def place(self, position):
        print "I've moved to", position
        
    def shoot(self):
     print "I shot", str(self)
        
    def createProjectile(self):
        print "I created a Projectile"
        
    def useDown(self):
        print "I've been used", str(self)
        
    def broken(self):
        print "I'm broken", str(self)
        
    def remove(self):
        print "I'm gone" str(self)
        