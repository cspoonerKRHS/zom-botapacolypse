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
    def __init__(self, speed, position):
        self.surfaces = []
        self.surfaces += [pygame.image.load("rsc\man\man.png")]
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.speed = speed
        self.place(position)
        self.living = True
    
    
    def __str__(self):
        return "I am the Man" + str(self.rect.center) + str(self.speed) + str(self.living)
    
    def place(self, position):
        print "I've moved to", position
    
    def move(self):
        print "I've moved", self.speed
    
    def direction(self, direction):
        print "I am trying to move", direction
    
    def distToPoint(self):
        print "I can see", str(distToPoint)
        
    def collideWall(self):
        print "Trying to hit screen walls", screenWidth, screenHeight    
    
    def collideMazeWall(self, MazeWall):
        print "Trying to hit the maze wall", str(MazeWall)
        
    def collideRobot(self, robot):
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
        
        