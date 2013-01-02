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
        if self.sight(other)
            self.rect = self.rect.move(self.speed + self.speed)
        
    def sight(self, other, pt):
        x1 = self.rect.center[0]
        x2 = pt[0]
        y1 = self.rect.center[1]
        y2 = pt[1]
        x1 = other.rect.center[0]
        x2 = pt[0]
        y1 = other.rect.center[1]
        y2 = p1[0]
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
        print "I'm near something ", str(other.rect.center)
        
        
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
        if (self.rect.right > mazeWall.rect.left 
            and self.rect.left < mazeWall.rect.right):
            if (self.rect.bottom > mazeWall.rect.top and 
                self.rect.top < mazeWall.rect.bottom):
                if (self.distToPoint(mazeWall.rect.center)
                    < self.radius + mazeWall.radius):  
                    self.speed[0] = self.speed[0] * 0
                    self.speed[1] = self.speed[1] * 0
                    return True
        
    def collideRobot(self, robot):
        print "Trying to collide with the robot", str(robot)
        if (self.rect.right > robot.rect.left 
            and self.rect.left < robot.rect.right):
            if (self.rect.bottom > robot.rect.top and 
                self.rect.top < robot.rect.bottom):
                if (self.distToPoint(robot.rect.center)
                    < self.radius + robot.radius):  
                    self.speed[0] = self.speed[0] * 0
                    self.speed[1] = self.speed[1] * 0
                    robot.speed[0] = robot.speed[0] * 0
                    robot.speed[1] = robot.speed[1] * 0
                    return True
        
    def collideZombie(self, other):
        print "Trying to collide with my comrade", str(zombie)
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
        print "Trying to bite", str(man)
    
    def hurt(self, other):
        print "I've gotten hurt by", str(other)
        
    def dropItem(self):
        print "I've droped", (Taser or stunGun or stick or pistol)
    
    def remove(self):
        print "I am being removed from the game", self
                    
        #return True
        
        
        #return False
        
        