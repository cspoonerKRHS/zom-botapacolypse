#-------------------------------------------------------------------
# Project:     Zom-botapacolyse
# Name:        Zombie.py
# Purpose:     An Enemy Object
# 
# Authors:     Michael Simon, Matt Hahn, Tim Richter
# Main Author: Michael Simon
#
# Created:     12/10/12
# Copyright:   (c) Michael Simon 2012
# License:     GSL
#-------------------------------------------------------------------
import pygame, math
from Taser import Taser



class Zombie():
    # Attributes or Variables
    # surface
    # rect
    # distToCenter
    # speed
    # maxSpeed
    # screenWidth
    # screenHeight
    # unDead

   
    
    # Methods or Functions
    def __init__(self, speed, position, screenSize):
        self.surfaces = []
        self.surfaces += [pygame.image.load("rsc/zombie/zombie.png")]
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.speed = speed
        speed = [2, 2]
        self.place(position)
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.unDead = True
        #if pygame.mixer:
        #    self.zombieNoise = pygame.mixer.sound("zombie.wav")   
    
    def __str__(self):
        return "I am the Undead" + str(self.rect.center) + str(self.speed) + str(self.living)
    
    def place(self, position):
        self.rect = self.rect.move(position)
    
    def move(self):
        self.rect = self.rect.move(self.speed)
        #if pygame.mixer
        #   self.zombieNoise.play()
        
    def chase(self, speed):
        self.rect = self.rect.move(self.speed + self.speed)
        
    def sight(self, other):
        
        def distToPoint(self, pt):
            x1 = self.rect.center[0]
            x2 = pt[0]
            y1 = self.rect.center[1]
            y2 = pt[1]
            return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
            print "I'm near something ", str(other.rect.center)
        
    def collideWall(self, screenWidth, screenHeight):
        if (self.rect.left < 0 
            or self.rect.right > self.screenWidth):
            self.speed[0] = self.speed[0]*-0.2
        if (self.rect.top < 0 
            or self.rect.bottom >self.screenHeight):
            self.speed[1] = self.speed[1]*-0.2
    def collideMazeWall(self, mazeWall):
        print "Trying to hit the maze wall", str(mazeWall)
        
    def collideRobot(self, robot):
        print "Trying to collide with the robot", str(robot)
        
    def collideZombie(self, other):
        print "Trying to collide with my comrade", str(zombie)
        
    def collideElectricity(self, electricity):
        print "I'm being electricuted by", electricity
       
    def collideProjectile(self, projectile):
        print "I'm being shot by", projectile
        
    def biteMan(self, man):
        print "Trying to bite", str(man)
    
    def hurt(self, other):
        print "I've gotten hurt by", str(other)
    
    def dropItem(self):
        print "I've droped", (Taser or stunGun or stick or pistol)
    
    def remove(self):
        print "I am being removed from the game", self
                    
        #return True
        
        
        #return False
        
        