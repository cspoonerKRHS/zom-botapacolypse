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


from Electricity import Electricity
from Projectile import Projectile

class Robot():
    def __init__(self, speed, position, screenSize):
        self.surfaces = []
        self.surfaces += [pygame.image.load("rsc/Robot/robot2.png")]
        self.surfaces += [pygame.image.load("rsc/Robot/robotright2.png")]
        self.surfaces += [pygame.image.load("rsc/Robot/robotshoot2.png")]
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.radius = self.rect.width/2
        speed = [0, 0]
        self.maxSpeed = 1
        self.speed = speed
        self.detectionRadius = 100
        self.place(position)
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.living = True
        self.life = 100
        #if pygame.mixer:
        #    self.robotSound = pygame.mixer.Sound("Robot.wav")
        
    def  __str__(self):
        return "I'm a Robot " + str(self.rect.center) + str(self.speed) + str(self.living)
     
    def place(self, position):
        self.rect.center = position
        #print "I've moved to", position
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        #print "I've moved", self.speed
                
        
    def distToPoint(self, pt):
        x1 = self.rect.center[0]
        x2 = pt[0]
        y1 = self.rect.center[1]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
        #print "I'm near something ", str(other.rect.center)
        
    def see(self, man):
        if self.distToPoint(man.rect.center) < self.detectionRadius:
            self.speed = [0,0]
            return True
        else:
            if self.speed == [0,0]:
                self.randomDirection()
                return False
            
    
    def checkLiving(self):       
        if self.life == 0:
            self.living = False
        #print "I can see You"
    
    def randomDirection(self):
        while self.speed == [0,0]:
            xmult = random.randint(-1,1)
            ymult = random.randint(-1,1)
            self.speed = [self.maxSpeed * xmult, self.maxSpeed * ymult]     
      
    def collideWall(self, screenWidth, screenHeight):
        if (self.rect.left < 0 
            or self.rect.right > screenWidth):
            self.speed[0] = self.speed[0]*-1
        if (self.rect.top < 0 
            or self.rect.bottom > screenHeight):
            self.speed[1] = self.speed[1]*-1
        #print " robot trying to hit edges of screen", screenWidth, screenHeight
        
    def collideMazeWall(self, mazeWall):
        if (self.rect.right > mazeWall.rect.left 
            and self.rect.left < mazeWall.rect.right):
            if (self.rect.bottom > mazeWall.rect.top and 
                self.rect.top < mazeWall.rect.bottom):
                if (self.distToPoint(mazeWall.rect.center)
                    < self.radius + mazeWall.radius):  
                    self.speed[0] = self.speed[0] * -1
                    self.speed[1] = self.speed[1] * -1
                    
                    dir = random.choice([-1,1])
                    
                    print self.rect.top, mazeWall.rect.bottom, ",", self.rect.bottom, mazeWall.rect.top, ",", self.rect.right, mazeWall.rect.left, ",", self.rect.left, mazeWall.rect.right
                    
                    if (self.rect.top < mazeWall.rect.bottom and self.speed[1] != 0):
                        print "hit top"
                        self.move()
                        self.move()
                        self.speed[0] = self.maxSpeed * dir
                        self.speed[1] = 0
                    elif (self.rect.bottom > mazeWall.rect.top and self.speed[1] != 0):
                        print "hit bottom"
                        self.move()
                        self.move()
                        self.speed[0] = self.maxSpeed * dir
                        self.speed[1] = 0
                    elif (self.rect.right > mazeWall.rect.left and self.speed[0] != 0):
                        print "hit right"
                        self.move()
                        self.move()
                        self.speed[0] = 0
                        self.speed[1] = self.maxSpeed * dir
                    elif (self.rect.left < mazeWall.rect.right and self.speed[0] != 0):
                        print "hit left"
                        self.move()
                        self.move()
                        self.speed[0] = 0
                        self.speed[1] = self.maxSpeed * dir
                    print self.speed

                    return True
        return False
        #print "trying to hit ", str(MazeWall)
        #if pygame.mixer:
        #   self.bounceSound.play()
           
    def collideRobot (self, other):
        #print "trying to hit ", str(other)
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
    
    def dead(self):
        if self.life <= 0:
            self.living = False

       
  
    