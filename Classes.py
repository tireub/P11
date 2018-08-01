import pygame
from pygame.locals import *

import random

#Definition of Labyrinth
class Labyrinth:
#Game level class

#def Initialisation of the level
    def __init__(self , file):
        self.file = file
        self.grid = []
        self.char_init_pos = (0, 0)
        self.char_init_sprite = (0, 0)


#def Read the file Level1 to import the level structure
    def create(self):
        # save into list within a list (main list for lines, secondary list for columns
        with open(self.file, "r") as file:
            self.grid = []

            for line in file:
                grid_line = []
                # for loop over the lines to define the sprites values
                for sprite in line:
                    grid_line.append(sprite)

                self.grid.append(grid_line)

#def display the level
    def display(self, level, window):

        background = pygame.image.load("img/background5.jpg")
        wall = pygame.image.load("img/wall2.jpg")
        finish = pygame.image.load("img/murdoc.png")
        y_pos = 0
        for lines in level.grid:
            # for each line we set the line position (sprite size = 31*31

            x_pos = 0
            for sprites in lines:
                # for each sprite we calculate the position
                x = x_pos * 45
                y = y_pos * 45
                # switch between the different types of sprites
                if sprites == "w" or sprites == "g":
                    window.blit(background, (x, y))
                    #Generate init position informations for the hero
                    if sprites == "g":
                        self.char_init_pos = (x + 7, y)
                        self.char_init_sprite = (y_pos, x_pos)
                if sprites == "b":
                    window.blit(wall, (x, y))
                if sprites == "r":
                    window.blit(finish, (x, y))
                x_pos += 1

            y_pos += 1


#Definition of our hero
class Character:

    #def initialisation of the character
    def __init__(self, char_pos, char_sprite):
        self.pos = char_pos
        self.sprite = char_sprite
        self.img = pygame.image.load("img/mcgiver.png").convert()
        self.bag_content = 0


    def move(self, direction, level, needle, tube, ether, sound, coin_sound):

        #while receiving a direction, check if it's not a wall or the border, then move and update position
        if direction == "up":
            if self.sprite[0] > 0:
                if level.grid[self.sprite[0] - 1][self.sprite[1]] != "b":
                    self.pos = [(self.pos[0]),(self.pos[1] - 45)]
                    self.sprite = [(self.sprite[0] - 1), (self.sprite[1])]
        if direction == "down":
            if self.sprite[0] < 14:
                if level.grid[self.sprite[0] + 1][self.sprite[1]] != "b":
                    self.pos = [(self.pos[0]), (self.pos[1] + 45)]
                    self.sprite = [(self.sprite[0] + 1), (self.sprite[1])]
        if direction == "right":
            if self.sprite[1] < 14:
                if level.grid[self.sprite[0]][self.sprite[1] + 1] != "b":
                    self.pos = [(self.pos[0] + 45), (self.pos[1])]
                    self.sprite = [(self.sprite[0]), (self.sprite[1] + 1)]
        if direction == "left":
            if self.sprite[1] > 0:
                if level.grid[self.sprite[0]][self.sprite[1] - 1] != "b":
                    self.pos = [(self.pos[0] - 45), (self.pos[1])]
                    self.sprite = [(self.sprite[0]), (self.sprite[1] - 1)]

        #check if there is an object to collect
        if self.sprite == needle.sprite:
            #update bag comp and remove object from lab
            needle.location = "bag"
            needle.sprite = ()
            needle.bag_position = self.bag_content
            self.bag_content += 1
            if sound.state == 0:
                coin_sound.play()

        if self.sprite == tube.sprite:
            #update bag comp and remove object from lab
            tube.location = "bag"
            tube.sprite = ()
            tube.bag_position = self.bag_content
            self.bag_content += 1
            if sound.state == 0:
                coin_sound.play()

        if self.sprite == ether.sprite:
            #update bag comp and remove object from lab
            ether.location = "bag"
            ether.sprite = ()
            ether.bag_position = self.bag_content
            self.bag_content += 1
            if sound.state == 0:
                coin_sound.play()


#Definition of the objects
class Object:

    #initialisation
    def __init__(self, type):
        self.name = type
        self.img = pygame.image.load("img/" + type + ".png").convert()
        self.location = "labyrinth"
        self.sprite = [0, 0]
        self.bag_position = 0

    #Object generation randomly on a w sprite
    def generate(self, level):
        x = random.randint(0, 14)
        y = random.randint(0, 14)

        while level.grid[x][y] != "w":
            x = random.randint(0, 14)
            y = random.randint(0, 14)


        self.sprite = [x, y]


    #Display the object
    def display(self, window, perso):
        #separate depending if the object has been collected or not
        if self.location == "labyrinth":
            x_pos = self.sprite[0] * 45 + 5
            y_pos = self.sprite[1] * 45 + 5

        if self.location == "bag":
            y_pos = 700 + self.bag_position * 45
            x_pos = 250

        window.blit(self.img, (y_pos, x_pos))

#Definition of sound_button
class Sound_button:
    button_images = (pygame.image.load("img/buttonon.jpg"), pygame.image.load("img/buttononoff.jpg"))
    sound_text = pygame.image.load("img/sound_text.png")

    #Init
    def __init__(self, initialvalue):

        self.state = initialvalue
        self.position = (900 , 600)
        self.img = self.button_images[initialvalue]



    def value_switch(self):
        self.state = not self.state
        self.img = self.button_images[self.state]

    def display(self, window):
        window.blit(self.sound_text, (self.position[0] - 85, self.position[1] - 12))
        window.blit(self.img, self.position)



