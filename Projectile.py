#-------------------------------------------------------------------
# Project:     Zom-botapacolyse
# Name:        Projectile.py
# Purpose:     A Projectile
# 
# Authors:     Michael Simon, Matt Hahn, Tim Richter
# Main Author: Matthew Hahn
#
# Created:     12/10/12
# Copyright:   (c) Matthew Hahn 2012
# License:     GSL
#-------------------------------------------------------------------
import pygame, math

class Projectile():
    # Attributes or Variables
    # surface
    # rect
    # distToCenter
    # speed
    # screenWidth
    # screenHeight
    # living
    
    # Methods or Functions
    def __init__(self, speed, position, heading, screenSize):
        self.surfaces = []
        self.surfaces += [pygame.image.load("rsc/projectile/projectile.png")]
        self.frame = 0
        self.maxFrame = len(self.surfaces)-1
        self.surface = self.surfaces[self.frame]
        self.surface = pygame.transform.scale(self.surface, [5, 5])
        self.rect = self.surface.get_rect()
        if heading == "n":
            self.speed = [0, -speed]
        elif heading == "s":
            self.speed = [0, speed]
        elif heading == "e":
            self.speed = [speed, 0]
        elif heading == "w":
            self.speed = [-speed, 0]
        self.place(position)
        self.notBroken = True
        self.damage = 10
        self.ammo = 20
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.radius = self.rect.width/2     
    
    def __str__(self):
        return "I am a Projecile" + str(self.rect.center) + str(self.notBroken)
    
    def place(self, position):
        self.rect.center = position
        
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        
        
    def distToPoint(self, pt):
        x1 = self.rect.center[0]
        x2 = pt[0]
        y1 = self.rect.center[1]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
                
    def collideWall(self, screenSize):
        if (self.rect.left < 0 
            or self.rect.right > screenSize):
            self.speed[0] = self.speed[0]*-1
        if (self.rect.top < 0 
            or self.rect.bottom > screenSize):
            self.speed[1] = self.speed[1]*-1
            
        
    def collideAttackMan(self, man):
        if (self.rect.right > man.rect.left 
            and self.rect.left < man.rect.right):
            if (self.rect.bottom > man.rect.top and 
                self.rect.top < man.rect.bottom):
                if (self.distToPoint(man.rect.center)
                    < self.radius + man.radius):
                    self.notBroken = False

    def collideMazeWall(self, MazeWall):
        if (self.rect.right > MazeWall.rect.left and
            self.rect.left < MazeWall.rect.right):
                if (self.rect.bottom > MazeWall.rect.top and 
                    self.rect.top < MazeWall.rect.bottom):
                        if (self.distToPoint(MazeWall.rect.center) < 
                            self.radius + MazeWall.radius): 
                                self.notBroken = False
        
    def collideAttackRobot(self, robot):
        if (self.rect.right > robot.rect.left 
            and self.rect.left < robot.rect.right):
            if (self.rect.bottom > robot.rect.top and 
                self.rect.top < robot.rect.bottom):
                if (self.distToPoint(robot.rect.center)
                    < self.radius + robot.radius):  
                    self.notBroken = False
                    robot.life = robot.life-20
            
    def collideAttackZombie(self, zombie):
        if (self.rect.right > zombie.rect.left 
            and self.rect.left < zombie.rect.right):
            if (self.rect.bottom > zombie.rect.top and 
                self.rect.top < zombie.rect.bottom):
                if (self.distToPoint(zombie.rect.center)
                    < self.radius + zombie.radius):  
                    self.notBroken = False
                    zombie.life = zombie.life-20
        
        