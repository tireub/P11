import pygame
from pygame.locals import *

from Classes import *

'''
MAIN
'''

#Pygame part to display
pygame.init()

#Window generation
window = pygame.display.set_mode((1000, 675))

#import  images
background = pygame.image.load("img/background5.jpg")
wall = pygame.image.load("img/wall2.jpg")
finish = pygame.image.load("img/murdoc.png")
congrats_message = pygame.image.load("img/winner.jpg")
intro_message = pygame.image.load("img/intro.png")
bag_message = pygame.image.load("img/bag.png")
defeat_message = pygame.image.load("img/game_over.png")


#import sounds
theme_sound = pygame.mixer.Sound("Sound/themesong.wav")
coin_sound = pygame.mixer.Sound("Sound/coin.wav")
defeat_sound = pygame.mixer.Sound("Sound/failure_2.wav")
victory_sound = pygame.mixer.Sound("Sound/victory.wav")

#Create the level
level = Labyrinth('Level1')
level.create()

#display the level
level.display(level, window)

#Initialise character
mcgiver = Character(level.char_init_pos, level.char_init_sprite)

#insert character
window.blit(mcgiver.img, (mcgiver.pos[0], mcgiver.pos[1]))

#Initialise objects
needle = Object("needle")
needle.generate(level)
needle.display(window, mcgiver)

tube = Object("tube")
tube.generate(level)
#Check if it is on the same sprite than the needle. If yes reroll
while tube.sprite == needle.sprite:
    tube.generate(level)
tube.display(window, mcgiver)

ether = Object("ether")
ether.generate(level)
#check if not on the needle or tube sprite. If so, reroll
while ether.sprite == needle.sprite or ether.sprite == tube.sprite:
    ether.generate(level)
ether.display(window, mcgiver)

#Initialise sound button
sound = Sound_button(1)

#Screen refresh
pygame.display.flip()

#Initiate theme song
theme_sound.play()
pygame.mixer.pause()

#Infinite loop to keep the window open
loop = 1
while loop:
    for event in pygame.event.get():
        #Manages the movement orders
        if event.type == KEYDOWN:
            if event.key == K_UP:
                mcgiver.move("up", level, needle, tube, ether, sound, coin_sound)
            if event.key == K_DOWN:
                mcgiver.move("down", level, needle, tube, ether, sound, coin_sound)
            if event.key == K_LEFT:
                mcgiver.move("left", level, needle, tube, ether, sound, coin_sound)
            if event.key == K_RIGHT:
                mcgiver.move("right", level, needle, tube, ether, sound, coin_sound)
        #Takes a push on the sound button into account
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if event.pos[0] > 900 and event.pos[0] < 985 and event.pos[1] > 600 and event.pos[1] < 636:
                    sound.value_switch()
                    if sound.state == 1:
                        pygame.mixer.pause()
                    if sound.state == 0:
                        pygame.mixer.unpause()
        if event.type == QUIT:
            loop = 0

    # refresh everything
    level.display(level, window)
    needle.display(window, mcgiver)
    tube.display(window, mcgiver)
    ether.display(window, mcgiver)
    window.blit(mcgiver.img, (mcgiver.pos[0], mcgiver.pos[1]))
    window.blit(intro_message, (690, 0))
    window.blit(bag_message, (690, 200))
    sound.display(window)


    # Screen refresh
    pygame.display.flip()

    if level.grid[mcgiver.sprite[0]][mcgiver.sprite[1]] == "r":
        break

#Stop theme song
theme_sound.stop()

#Play sound according to result
if mcgiver.bag_content == 3:
    if sound.state == 0:
        victory_sound.play()
if mcgiver.bag_content != 3:
    if sound.state == 0:
        defeat_sound.play()

#Display message according to the result
while loop:
    if mcgiver.bag_content == 3:
        window.blit(congrats_message,(0, 0))
    if mcgiver.bag_content != 3:
        window.blit(defeat_message, (0, 0))


    #2 different end conditions : close the window or push escape
    for event in pygame.event.get():
        if event.type == QUIT:
            loop = 0
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                loop = 0


    pygame.display.flip()