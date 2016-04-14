#This code produces an interactive graph for the nitrogene code using pygame.

import pygame
import time
from random import choice
Example_Genome = [(0, 19), (0, 25), (.15, 30), (0, 40), (.60, 40)]
Example_Genome2 = [(0, 15), (0, 40), (.35, 30), (0, 40), (.60, 100)]
Genome_List = [Example_Genome, Example_Genome2]
Genome_Bar_Height = 0
a = 0
b = 0

#Code to determine variables

#Model

#Changing variables
#Initializing objects:

class Nitrogene_Graph_Model(object):
    def __init__(self, size):
        """Initialize within the specialized model"""
        self.screen = pygame.display.set_mode(size)

#View - draw functions

#Adapted from PolkaDots game from the previous project.
class Nitrogene_Graph_View (object):
    def __init__(self, model):
        self.model = model

    def draw(self):
        """Draws the gene image onto the window."""

        self.screen.fill(pygame.Color('white'))
        background = pygame.Surface(screen.get_size()) #This is just making a surface because we have to use blitting to make things show up.
        background = background.convert() #This increases speed
        background.fill((255, 255, 255)) #This needs to match color

        font = pygame.font.Font(None, 36)
        text = font.render("Nitrogene Matches:", 1, (0, 0, 0))
        textpos = text.get_rect()
        textpos.centerx = WIDTH - 270
        background.blit(text, textpos)
        screen.blit(background, (0,0))

        for Genome in Genome_List:
            #Creating the stacking elements that build the bar graph for false values
            if 0 <= Genome[0][0] <= .15:
                pygame.rect(screen, (255, 0, 0, 0),Genome[b], Genome_Bar_Height)

                #Iterate through the rest of the sequence.

                b + 1

            elif i[a] in Genome_List <= .15: #and => 0:
                color_match = (0, i[a]*255 , 0, 0)
                pygame.rect(screen, (color_match), left + i[b], top - Genome_Bar_Height)

                #Iterate through the rest of the

                b + 1

            i + 1

#Running the Code (Adapted from the in class brick breaker code.)
if __name__ == '__main__':

    pygame.init()
    size = (640, 480)
    model = Nitrogene_Graph_Model(size)
    view = Nitrogene_Graph_View(model)
    screen = pygame.display.set_mode(size) #This is the surface you want to draw to.
    running = True
    while running:
        view.draw()
        time.sleep(.001)
