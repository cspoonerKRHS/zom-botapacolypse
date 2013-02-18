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
        self.hitCount = 10
        #if pygame.mixer:
        #    self.stickSound = pygame.mixer.Sound("stick.wav")
           
    def  __str__(self):
        return "I'm a Stick " + str(self.rect.center) + str(self.notBroken)
     
    def place(self, position):
        self.rect.center = position
        #print "I've moved to", position
      
    def collideZombie(self, zombie):
        if (self.rect.right > zombie.rect.left 
            and self.rect.left < zombie.rect.right):
            if (self.rect.bottom > zombie.rect.top and 
                self.rect.top < zombie.rect.bottom):
                if (self.distToPoint(zombie.rect.center)
                    < self.radius + zombie.radius):  
                    self.hitCount = self.hitCount -1
                    zombie.life = zombie.life-10
        print "I've hit the zombie", str(other)
        
    def collideRobot(self, robot):
        if (self.rect.right > robot.rect.left 
                and self.rect.left < robot.rect.right):
                if (self.rect.bottom > robot.rect.top and 
                    self.rect.top < robot.rect.bottom):
                    if (self.distToPoint(robot.rect.center)
                        < self.radius + robot.radius):  
                        self.hitCount = self.hitCount -1
                        robot.life = robot.life-10
        print "I've hit the Robot", str(other)
        
    def collideMazeWall(self, Mazewall):
        if (self.rect.right > MazeWall.rect.left and
                self.rect.left < MazeWall.rect.right):
                    if (self.rect.bottom > MazeWall.rect.top and 
                        self.rect.top < MazeWall.rect.bottom):
                            if (self.distToPoint(MazeWall.rect.center) < 
                                self.radius + MazeWall.radius): 
                                    self.notBroken = False
        print "I've hit the MazeWall", str(other)
            
    def broken(self):
        print "I'm broken"
        
    def remove(self):
        print "I'm gone"
        
    