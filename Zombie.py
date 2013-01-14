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
from Robot import Robot


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
        self.surfaces += [pygame.image.load("rsc/zombie/zombie2.png")]
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.radius = self.rect.width/2
        speed = [2, 2]
        self.maxSpeed = 3
        self.speed = speed
        self.detectionRadius = 100
        self.biteRadius = 10
        self.noSpeed = 0
        self.place(position)
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.unDead = True
        self.life = 100
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
        
    def distToPoint(self, pt):
        x1 = self.rect.center[0]
        x2 = pt[0]
        y1 = self.rect.center[1]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
        #print "I'm near something ", str(other.rect.center)
        
    def chase(self, man):
        if self.distToPoint(man.rect.center) < self.detectionRadius:
            pX = man.rect.center[0]
            pY = man.rect.center[1]
            zX = self.rect.center[0]
            zY = self.rect.center[1]
            
            if pX > zX:
                self.speed[0] = self.maxSpeed
            elif pX < zX:
                self.speed[0] = -self.maxSpeed
            else:
                self.speed[0] = 0
        
            if pY > zY:
                self.speed[1] = self.maxSpeed
            elif pY < zY:
                self.speed[1] = -self.maxSpeed
            else:
                self.speed[1] = 0
        
    def collideWall(self, screenWidth, screenHeight):
        if (self.rect.left < 0 
            or self.rect.right > self.screenWidth):
            self.speed[0] = self.speed[0]*-1
        if (self.rect.top < 0 
            or self.rect.bottom >self.screenHeight):
            self.speed[1] = self.speed[1]*-1
    
    def collideMazeWall(self, mazeWall):
        #print "Trying to hit the maze wall", str(mazeWall)
        if (self.rect.right > mazeWall.rect.left 
            and self.rect.left < mazeWall.rect.right):
            if (self.rect.bottom > mazeWall.rect.top and 
                self.rect.top < mazeWall.rect.bottom):
                if (self.distToPoint(mazeWall.rect.center)
                    < self.radius + mazeWall.radius):  
                    self.speed[0] = self.speed[0] * -1
                    self.speed[1] = self.speed[1] * -1
                    return True
        
    def collideRobot(self, robot):
        #print "Trying to collide with the robot", str(robot)
        if (self.rect.right > robot.rect.left 
            and self.rect.left < robot.rect.right):
            if (self.rect.bottom > robot.rect.top and 
                self.rect.top < robot.rect.bottom):
                if (self.distToPoint(robot.rect.center)
                    < self.radius + robot.radius):  
                    self.speed[0] = self.speed[0] * -1
                    self.speed[1] = self.speed[1] * -1
                    robot.speed[0] = robot.speed[0] * -1
                    robot.speed[1] = robot.speed[1] * -1
                    return True
        
    def collideZombie(self, other):
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
                    
    def collideZombie2(self, other):
        if (self.rect.right > other.rect.left 
            and self.rect.left < other.rect.right):
            if (self.rect.bottom > other.rect.top and 
                self.rect.top < other.rect.bottom):
                if (self.distToPoint(other.rect.center)
                    < self.radius + other.radius):  
                    self.speed[0] = self.speed[0] * 0
                    self.speed[1] = self.speed[1] * 0
                    other.speed[0] = other.speed[0] * 0
                    other.speed[1] = other.speed[1] * 0
                    return True

    
    def biteMan(self, man):
        if self.distToPoint(man.rect.center) < self.biteRadius:
            pX = man.rect.center[0]
            pY = man.rect.center[1]
            zX = self.rect.center[0]
            zY = self.rect.center[1]
            
            if pX > zX:
                self.speed[0] = self.noSpeed
            elif pX < zX:
                self.speed[0] = -self.noSpeed
            else:
                self.speed[0] = 0
        
            if pY > zY:
                self.speed[1] = self.noSpeed
            elif pY < zY:
                self.speed[1] = -self.noSpeed
            else:
                self.speed[1] = 0        
        #print "Trying to bite", man
        
    def dropItem(self):
        if self.unDead == False:
            screen.blit(pistol.surface, pistol.rect)
        #print "I've droped", (Taser or stunGun or stick or pistol)
    
        if self.life == 0:
            self.unDead = False
                    
        #return True
        
        
        #return False
        
        