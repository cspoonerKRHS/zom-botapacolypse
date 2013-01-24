#-------------------------------------------------------------------
# Project:     Zom-botapacolyse
# Name:        Man.py
# Purpose:     The Player Object
# 
# Authors:     Michael Simon, Matt Hahn, Tim Richter
# Main Author: Michael Simon
#
# Created:     12/11/12
# Copyright:   (c) Michael Simon 2012
# License:     GSL
#-------------------------------------------------------------------
import pygame, math
from Zombie import Zombie
from Robot import Robot
from MazeWall import MazeWall
screenWidth = 800
screenHeight = 600

screenSize = screenWidth, screenHeight
screen = pygame.display.set_mode(screenSize)

class Man():
    # Attributes or Variables
    # surface
    # rect
    # distToCenter
    # speed
    # screenWidth
    # screenHeight
    # living
    
    # Methods or Functions
    def __init__(self, maxSpeed, position):
        self.surfaces = []
        self.surfaces += [pygame.image.load("rsc\man\man.png")]
        self.surfaces += [pygame.image.load("rsc\man\mann.png")]
        self.surfaces += [pygame.image.load("rsc\man\mane.png")]
        self.surfaces += [pygame.image.load("rsc\man\manw.png")]
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.radius = self.rect.width/2
        self.maxSpeed = maxSpeed
        self.speed = [0,0]
        self.place(position)
        self.living = True
    
    
    def __str__(self):
        return "I am the Man" + str(self.rect.center) + str(self.speed) + str(self.living)
    
    def place(self, position):
        #print "I've moved to", position
        self.rect = self.rect.move(position)
    
    def move(self):
        print "I've moved", self.speed
        self.rect = self.rect.move(self.speed)
    
    def direction(self, dir):
        #print "I am trying to move", dir
        if dir == "up":
            self.surface = pygame.image.load("rsc\man\mann.png")
            self.speed[1] = -self.maxSpeed
        elif dir == "down":
            self.surface = pygame.image.load("rsc\man\man.png")
            self.speed[1] = self.maxSpeed
        elif dir == "stop up":
            self.speed[1] = 0
        elif dir == "stop down":
            self.speed[1] = 0
            
        if dir == "right":
            self.surface = pygame.image.load("rsc\man\mane.png")
            self.speed[0] = self.maxSpeed
        elif dir == "left":
            self.surface = pygame.image.load("rsc\man\manw.png")
            self.speed[0] = -self.maxSpeed
        elif dir == "stop right":
            self.speed[0] = 0
        elif dir == "stop left":
            self.speed[0] = 0
        
        
    def distToPoint(self, pt):
        x1 = self.rect.center[0]
        x2 = pt[0]
        y1 = self.rect.center[1]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
        #print "I'm near something ", str(other.rect.center)

        
    def collideWall(self):
        if (self.rect.left < 0 
            or self.rect.right > screenWidth):
            self.speed[0] = self.speed[0]*0
        if (self.rect.top < 0 
            or self.rect.bottom > screenHeight):
            self.speed[1] = self.speed[1]*0
        
        if (self.rect.top < 0):
            self.speed = [0, 1]
            if (self.rect.top > 0):
                self.speed = [0, 0]
        if (self.rect.left < 0):
            self.speed = [1, 0]
            if (self.rect.left > 0):
                self.speed = [0, 0]
        if (self.rect.right > screenWidth):
            self.speed = [-1, 0]
            if (self.rect.right < screenWidth):
                self.speed = [0, 0]
        if (self.rect.bottom > screenHeight):
            self.speed = [0, -1]
            if (self.rect.bottom < screenHeight):
                self.speed = [0, 0]
        #print "Trying to hit screen walls", screenWidth, screenHeight    
    
    def collideMazeWall(self, MazeWall):
        if (self.rect.right > MazeWall.rect.left 
                and self.rect.left < MazeWall.rect.right):
                if (self.rect.bottom > MazeWall.rect.top and 
                    self.rect.top < MazeWall.rect.bottom):
                    if (self.distToPoint(MazeWall.rect.center)
                        < self.radius + MazeWall.radius):  
                        self.speed[0] = self.speed[0] * 0
                        self.speed[1] = self.speed[1] * 0
        #print "Trying to hit the maze wall", str(MazeWall)
        
    def collideRobot(self, other):
        pass
        #print "Trying to collide with the robot", str(Robot)
        
    def collideZombie(self, other):
        pass
        #print "Trying to collide zombie", str(Zombie)
                            
    def collideStick(self, stick):
        pass
        #print "I have collided with", stick
        
    def collideStunGun(self, stunGun):
        pass
        #print "I have collided with", stunGun
    
    def collideTaser(self, taser):
        pass
        #print "I have collided with", taser
    
    def collidePistol(self, pistol):
        pass
        #print "I have collided with", pistol
        
    def collideElectricity(self, electricity):
        pass
        #print "I'm being electricuted by", electricity
    
    def pickUpStick(self, stick):
        pass
        #print "I have picked up", stick
    
    def pickUpStunGun(self, stunGun):
        pass
        #print "I have picked up", stunGun
    
    def pickUpTaser(self, taser):
        pass
        #print "I have picked up", taser
    
    def pickUpPistol(self, pistol):
        pass
        #print "I have picked up", pistol
    
    def attackWithStick(self, stick, other):
        pass
        #print "I have attacked with", str(stick), other
    
    def attackWithStunGun(self, stunGun, other):
        pass
        #print "I have attacked with", str(stunGun), other
    
    def attackWithTaser(self, taser, other):
        pass
        #print "I have attacked with", str(taser), other
    
    def attackWithPistol(self, pistol, other):
        pass
        #print "I have attacked", str(pistol), other
    
    def hurt(self, other):
        pass
        #print "I've been hurt by", str(other)
    
    def die(self):
        pass
        #print "I have died"
    
    def remove(self):
        pass
        #print "I am being removed from the game", self
                    
        #return True
        
        
        #return False
        
        