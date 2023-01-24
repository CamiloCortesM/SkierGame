import os
import sys
import cfg
import pygame
import random

class SkierClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.direction = 0
        self.imagpaths = cfg.SKIER_IMAGES_PATHS[:-1]
        self.image = pygame.image.load(self.imagpaths[self.direction])
        self.rect = self.image.get_rect()
        self.rect.center = [320,100]
        self.speed = [self.direction, 6-abs(self.direction)*2]