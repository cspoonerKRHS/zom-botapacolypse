import pygame, sys, math

class Button:
    
    def __init__(self, text, location, color, highlighted = False):
        self.surfaces = []
        pygame.font.init()
        self.font = pygame.font.Font(None, 60)
        self.text = text
        self.normalText = self.text
        self.selectedText = self.text + " (-)"
        self.color = color
        self.surface = self.font.render(str(self.text), 1, self.color)
        self.frame = 0
        self.rect = self.surface.get_rect()
        self.clicked = False
        self.highlighted = highlighted
        self.location = location
        self.place(self.location)
        
    def place(self, pt):
        self.rect.center = pt   

    def select(self):
        self.text = self.selectedText
        self.surface = self.font.render(str(self.text), 1, self.color)
        self.rect = self.surface.get_rect()
        self.place(self.location)
        
    def deselect(self):
        self.text = self.normalText
        self.surface = self.font.render(str(self.text), 1, self.color)
        self.rect = self.surface.get_rect()
        self.place(self.location)

        
        
    def update(self, color):
        if self.highlighted:
            self.frame = 1
        else:
            self.frame = 0
            self.surface = self.font.render(str(self.text), 1, (color))
        
    def collidePt(self, pt):
        if (pt[0] > self.rect.left and pt[0] < self.rect.right):
            if (pt[1] > self.rect.top and pt[1] < self.rect.bottom):
                return True       
