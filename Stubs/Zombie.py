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
    def __init__(self, speed, position):
        self.surfaces = []
        self.surfaces += [pygame.image.load("rsc/zombie/zombie.png")]
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.speed = speed
        self.place(position)
        self.unDead = True
        #if pygame.mixer:
        #    self.zombieNoise = pygame.mixer.sound("zombie.wav")
    
    
    def __str__(self):
        return "I am the Undead" + str(self.rect.center) + str(self.speed) + str(self.living)
    
    def place(self, position):
        print "I've moved to", position
    
    def move(self):
        print "I've moved", self.speed
        #if pygame.mixer
        #   self.zombieNoise.play()
        
    def chase(self, other):
        print "I am chasing, at a faster speed,", other
        
    def sight(self, other):
        print "I have seen", other
    
    def distToPoint(self):
        print "I can see", str(distToPoint)
        
    def collideWall(self, screenWidth, screenHeight):
        print "Trying to hit screen walls", screenWidth, screenHeight
        
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
        
        