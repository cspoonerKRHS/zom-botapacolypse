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

from MazeWall import MazeWall
from Zombie import Zombie

from Electricity import Electricity
from Projectile import Projectile

class Robot():
    def __init__(self, speed = [2,2], position):
        self.surfaces = []
        self.surfaces += [pygame.image.load("rsc/Robot/robotright1.png")]
        self.surfaces += [pygame.image.load("rsc/Robot/robotright2.png")]
        self.surfaces += [pygame.image.load("rsc/Robot/robotshoot2.png")]
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.speed = speed
        self.place(position)
        self.living = True 
        #if pygame.mixer:
        #    self.robotSound = pygame.mixer.Sound("Robot.wav")
        
    def  __str__(self):
        return "I'm a Robot " + str(self.rect.center) + str(self.speed) + str(self.living)
     
    def place(self, position):
        print "I've moved to", position
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        print "I've moved", self.speed
        
    def shootElect(self):
        if self.frame > 1:
            screen.blit(Electricity.surface, Electricity.rect)
        print "I'm shooting Electricity "
            
        
    def hurt(self):
        if self.living:
            if Electricity.collideAttackRobot:
                self.living = False
            if Projectile.collideAttackRobot:
                
        print "I'm hurt"
        
    def distToPoint(self, pt):
        x1 = self.rect.center[0]
        x2 = pt[0]
        y1 = self.rect.center[1]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
        print "I'm near something ", str(other.rect.center)
        
    def sight(self, other):
        if (self.distToPoint(Man.rect.center)):
            self.shootElect()
        print "I can see ", other
        
    def dropItem(self):
        print "I drop this" 
         
      
    def collideWall(self, screenWidth, screenHeight):
        if (self.rect.left < 0 
            or self.rect.right > self.screenWidth):
            self.speed[0] = self.speed[0]*-1
        if (self.rect.top < 0 
            or self.rect.bottom >self.screenHeight):
            self.speed[1] = self.speed[1]*-1
        print "trying to hit edges of screen", screenWidth, screenHeight
        
    def collideMazeWall(self, MazeWall):
        if (self.rect.right > MazeWall.rect.left 
                and self.rect.left < MazeWall.rect.right):
                if (self.rect.bottom > MazeWall.rect.top and 
                    self.rect.top < MazeWall.rect.bottom):
                    if (self.distToPoint(MazeWall.rect.center)
                        < self.radius + MazeWall.radius):  
                        self.speed[0] = self.speed[0] * -1
                        self.speed[1] = self.speed[1] * -1

        print "trying to hit ", str(MazeWall)
        #if pygame.mixer:
        #   self.bounceSound.play()
        
    def collideElectricity(self, Electricity):
        if self.living and Electricity.living:
            if (self.rect.right > Electricity.rect.left 
                and self.rect.left < Electricity.rect.right):
                if (self.rect.bottom > Electricity.rect.top and 
                    self.rect.top < Electricity.rect.bottom):
                    if (self.distToPoint(Electricity.rect.center)
                        < self.radius + Electricity.radius):  
                        self.speed[0] = self.speed[0] * -1
                        self.speed[1] = self.speed[1] * -1
                        Electricity.speed[0] = Electricity.speed[0] * -1
                        Electricity.speed[1] = Electricity.speed[1] * -1
        print "trying to hit ", str(Electricity)
        
    def collideProjectile(self, Projectile):
        if self.living and Projectile.living:
            if (self.rect.right > Projectile.rect.left 
                and self.rect.left < Projectile.rect.right):
                if (self.rect.bottom > Projectile.rect.top and 
                    self.rect.top < Projectile.rect.bottom):
                    if (self.distToPoint(Projectile.rect.center)
                        < self.radius + Projectile.radius):  
                        self.speed[0] = self.speed[0] * -1
                        self.speed[1] = self.speed[1] * -1
                        Projectile.speed[0] = Projectile.speed[0] * -1
                        Projectile.speed[1] = Projectile.speed[1] * -1
        print "I'm being shot by", projectile
        
    def collideRobot (self, other):
        if self.living and other.living:
            if (self.rect.right > other.rect.left 
                and self.rect.left < other.rect.right):
                if (self.rect.bottom > other.rect.top and 
                    self.rect.top < other.rect.bottom):
                    if (self.distToPoint(other.rect.center)
                        < self.radius + other.radius):  
                        self.speed[0] = self.speed[0] * -1
                        self.speed[1] = self.speed[1] * -1
                        other.speed[0] = other.speed[0] * -1
                        other.speed[1] = other.speed[1] * -1
                        return True
        return False
        
        
        print "trying to hit ", str(other)  
    