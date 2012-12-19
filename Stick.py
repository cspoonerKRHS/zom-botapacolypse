#------------------------------------------------------------------------------
# Project:     Zom-Botapocalypse
# Name:        Stick.py
# Purpose:     Player Object
# 
# Authors:     Mathew Hahn, Michael Simon, Tim Richter
# Main Author: Tim Richter
#
# Created:     12/10/2012
# Copyright:   (c) Tim Richter 2012
# Licence:     New BSD
#------------------------------------------------------------------------------
import pygame, math, sys, random

class Stick():
    def __init__(self, position):
        self.surfaces = []
        self.surfaces += [pygame.image.load("rsc/stick/stick.png")]
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.place(position)
        self.notBroken = True
        #if pygame.mixer:
        #    self.stickSound = pygame.mixer.Sound("stick.wav")
           
    def  __str__(self):
        return "I'm a Stick " + str(self.rect.center) + str(self.notBroken)
     
    def place(self, position):
        print "I've moved to", position
        
    def attack(self, other):
        print "I've attacked", str(other)
        
    def collideZombie(self, other):
        print "I've hit the zombie", str(other)
        
    def collideRobot(self, other):
        print "I've hit the Robot", str(other)
        
    def collideMazeWall(self, other):
        print "I've hit the MazeWall", str(other)
        
    def useDown(self):
        print "I've been used"
    
    def broken(self):
        print "I'm broken"
        
    def remove(self):
        print "I'm gone"
        
    