#------------------------------------------------------------------------------
# Project:     Zom-botapacolypse
# Name:        HealthBar.py
# Purpose:     Health Bar Object
# 
# Authors:     Matt Hahn, Michael Simon, Tim Richter
# Main Author: Matt Hahn
#
# Created:     12/11/2012
# Copyright:   (c) Matthew Hahn 2012
# Licence:     GSL
#------------------------------------------------------------------------------
import pygame, math, sys, random

class Ball():
    def __init__(self, speed, position):
        self.surfaces = []
        self.surfaces += [pygame.image.load("")]
        self.surfaces += [pygame.image.load("")]
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.speed = speed
        self.place(position)
        self.maxHealth = maxHealth
        if pygame.mixer:
            self.healthSound = pygame.mixer.Sound("health.wav")
        
    def  __str__(self):
        return "I'm a Health Bar " + str(self.rect.center) + str(self.speed) + str(self.living)
     
    def place(self, position):
        print "I'm in place", position
        
    def maxHealth(self, maxHealth)
        print "This how much health you have to start", str(maxHealth)
           
    
