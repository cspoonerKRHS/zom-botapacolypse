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

class HealthBar():
    def __init__(self, position):
        self.surfaces = []
        self.surfaces += [pygame.image.load("rsc/HealthBar/healthbar100.png")]
        self.surfaces += [pygame.image.load("rsc/HealthBar/healthbar90.png")]
        self.surfaces += [pygame.image.load("rsc/HealthBar/healthbar80.png")]
        self.surfaces += [pygame.image.load("rsc/HealthBar/healthbar70.png")]
        self.surfaces += [pygame.image.load("rsc/HealthBar/healthbar60.png")]
        self.surfaces += [pygame.image.load("rsc/HealthBar/healthbar50.png")]
        self.surfaces += [pygame.image.load("rsc/HealthBar/healthbar40.png")]
        self.surfaces += [pygame.image.load("rsc/HealthBar/healthbar30.png")]
        self.surfaces += [pygame.image.load("rsc/HealthBar/healthbar20.png")]
        self.surfaces += [pygame.image.load("rsc/HealthBar/healthbar10.png")]
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.place(position)
        #if pygame.mixer:
        #    self.healthSound = pygame.mixer.Sound("health.wav")
        
    def  __str__(self):
        return "I'm a Health Bar " + str(self.rect.center) + str(self.speed) + str(self.living)
     
    def place(self, position):
        print "I'm in place", position
        self.rect = self.rect.move(position)
        
    def downHealth(self, man):
        if man.life == 100:
            self.surface = pygame.image.load("rsc/HealthBar/healthbar100.png")
        elif man.life == 90:
            self.surface = pygame.image.load("rsc/HealthBar/healthbar90.png")
        elif man.life == 80:
            self.surface = pygame.image.load("rsc/HealthBar/healthbar80.png")
        elif man.life == 70:
            self.surface = pygame.image.load("rsc/HealthBar/healthbar70.png")
        elif man.life == 60:
            self.surface = pygame.image.load("rsc/HealthBar/healthbar60.png")
        elif man.life == 50:
            self.surface = pygame.image.load("rsc/HealthBar/healthbar50.png")
        elif man.life == 40:
            self.surface = pygame.image.load("rsc/HealthBar/healthbar40.png")
        elif man.life == 30:
            self.surface = pygame.image.load("rsc/HealthBar/healthbar30.png")
        elif man.life == 20:
            self.surface = pygame.image.load("rsc/HealthBar/healthbar20.png")
        elif man.life == 10:
            self.surface = pygame.image.load("rsc/HealthBar/healthbar10.png")
        
        print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
           
    
