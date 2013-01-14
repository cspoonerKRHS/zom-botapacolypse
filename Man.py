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
        print "I am trying to move", dir
        if dir == "up":
            self.speed[1] = -self.maxSpeed
        elif dir == "down":
            self.speed[1] = self.maxSpeed
        elif dir == "stop up":
            self.speed[1] = 0
        elif dir == "stop down":
            self.speed[1] = 0
            
        if dir == "right":
            self.speed[0] = self.maxSpeed
        elif dir == "left":
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
        print "Trying to hit screen walls", screenWidth, screenHeight    
    
    def collideMazeWall(self, MazeWall):
        print "Trying to hit the maze wall", str(MazeWall)
        
    def collideRobot(self, other):
        print "Trying to collide with the robot", str(Robot)
        
    def collideZombie(self, other):
        print "Trying to collide zombie", str(Zombie)
                            
    def collideStick(self, stick):
        print "I have collided with", stick
        
    def collideStunGun(self, stunGun):
        print "I have collided with", stunGun
    
    def collideTaser(self, taser):
        print "I have collided with", taser
    
    def collidePistol(self, pistol):
        print "I have collided with", pistol
        
    def collideElectricity(self, electricity):
        print "I'm being electricuted by", electricity
    
    def pickUpStick(self, stick):
        print "I have picked up", stick
    
    def pickUpStunGun(self, stunGun):
        print "I have picked up", stunGun
    
    def pickUpTaser(self, taser):
        print "I have picked up", taser
    
    def pickUpPistol(self, pistol):
        print "I have picked up", pistol
    
    def attackWithStick(self, stick, other):
        print "I have attacked with", str(stick), other
    
    def attackWithStunGun(self, stunGun, other):
        print "I have attacked with", str(stunGun), other
    
    def attackWithTaser(self, taser, other):
        print "I have attacked with", str(taser), other
    
    def attackWithPistol(self, pistol, other):
        print "I have attacked", str(pistol), other
    
    def hurt(self, other):
        print "I've gotten hurt by", str(other)
    
    def die(self):
        print "I have died"
    
    def remove(self):
        print "I am being removed from the game", self
                    
        #return True
        
        
        #return False
        
        