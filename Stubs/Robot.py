#------------------------------------------------------------------------------
# Project:     Zomb-botapacolypse
# Name:        Robot.py
# Purpose:     Robot Object
# 
# Authors:     Matt Hahn, Michael Simon, Tim Richter
# Main Author: Matt Hahn
#
# Created:     12/5/12
# Copyright:   (c) Matthew Hahn 2012
# Licence:     GSL
#------------------------------------------------------------------------------
import pygame, math, sys, random

class Robot():
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
        self.living = True
        self.sight(distToPoint) 
        if pygame.mixer:
            self.robotSound = pygame.mixer.Sound("Robot.wav")
        
    def  __str__(self):
        return "I'm a Robot " + str(self.rect.center) + str(self.speed) + str(self.living)
     
    def place(self, position):
        print "I've moved to", position
        
    def move(self):
        print "I've moved", self.speed
        
    def shootElect():
        print "I'm shooting Electricity " 
        
    def hurt():
        print "I'm hurt"
        
    def distToPoint(self, man or zombie or other or MazeWall or Wall):
        print "I'm near something ", str(position)
        
    def sight(distToPoint):
        print "I can see ", str(distToPoint)
        
    def dropItem(self):
        print "I drop this" 
        
    def remove(self)
        print "I'm gone" 
      
    def collideWall(self, screenWidth, screenHeight):
        print "trying to hit edges of screen", screenWidth, screenHeight
        
    def collideMazeWall(self, MazeWall):
        print "trying to hit paddle", str(MazeWall)
        #if pygame.mixer:
        #   self.bounceSound.play()
        
    def collideElectricity(self, Electricity):
        print "trying to hit ", str(Electricity)
        
    def collideRobot (self, other):
        print "trying to hit ", str(other)  
    