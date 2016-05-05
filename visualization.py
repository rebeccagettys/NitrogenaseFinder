

#This code creates a visualization for the nitrogenase_finder.py code, which finds nitrogenase matches from the gene_finder.py code. Bars in this simulation are contigs,
#and the bars drawn on top of them. Hover the mouse over one of these bars to find the percentage match.
#Type the threshold for DNA accuracy for a match in the command window.

#Importing everything.

import pygame
import pickle
import time
import sys
from pickle import dump
from random import choice


#Model - Creates lists with information about the forward and complementary strands.

class Nitrogene_Graph_Model(object):

    """ Loads and sorts pickle file information."""

    def __init__(self, size):
        """Initialize within the specialized model"""

        self.sorter_code(self.code_loader()) # Initializes the "code loader."
    def code_loader (self):
        return pickle.load(open('genes_found.pickle')) #This "code loader" loads the pickle file produced by nitrogenase_finder.py.

    def sorter_code (self, list_of_orfs_imported): #This sorter code sorts information for the forward and reverse complement strands into separate lists.

        self.forward_only_orf = [] #Creates the list for the forward orf
        self.complement_only_orf = [] #Creates a list for the reverse complement.
        for item in list_of_orfs_imported:
            if item["rev_flag"] == 0:
                self.forward_only_orf.append(item) #Adds the information to the forward strand list.
            elif item["rev_flag"] == 1:
                self.complement_only_orf.append(item) #Adds information to the complement list.

#View - Draw functions adapted from the POLKADOTS project and Pygame documentation.

class Nitrogene_Graph_View (object):

    """ Creates all of the visible items on the screen."""

    def __init__(self, model, forward_only_orf, complement_only_orf): #Initializes the attributes for the view class.

        #Attributes to do with the scrolling window.

        self.screen = pygame.display.set_mode(size)
        self.lscreen = pygame.surface.Surface(lsize)

        #Attributes used to draw the genes and matches onto the screen.

        self.model = model
        self.threshold = float(raw_input("Please type a two digit number representing the DNA accuracy threshold percentage."))
        self.Genome_Bar_Height = 15
        self.forward_only_orf = forward_only_orf
        self.complement_only_orf = complement_only_orf
        self.comp_fact = 10 # compression factor
        self.scroll_y = 0


    def draw(self):
        """Draws the contigs, matches, and percent values onto the screen."""

        self.lscreen.fill((0,0,0,0)) #This updates the surface so that past percentage symbols (to be drawn later) don't stay on the screen.

        for orf_num, orf in enumerate(self.forward_only_orf):

        #This makes sure that lengths of the contigs are oriented in the right direction.

            if orf["start"] > orf["end"]:
                orf["start"], orf["end"] = orf["end"], orf["start"]


            #This code draws the blue bars that represent the contigs of the forward strand.

            contig_length_rectangle = pygame.Rect(0,
                                   (self.Genome_Bar_Height + 10)*(orf_num*2),
                                    orf["length_item"]/self.comp_fact,
                                    self.Genome_Bar_Height
                                    )

            pygame.draw.rect(self.lscreen, (0,0,200,100), contig_length_rectangle, 0)

           #This code draws the matches onto the contigs.

            match_rectangle = pygame.Rect(float(orf["start"])/self.comp_fact,
                                        (self.Genome_Bar_Height + 10)*(orf_num*2),
                                        float(orf["end"]- orf["start"])/self.comp_fact,
                                        self.Genome_Bar_Height)

            #This code ensures that no orfs too short to be nitrogenase are used as such.

            if orf["end"] - orf["start"] < .8*orf["length_nitrogenase"]:
                continue

            #This code defines the color and draws the false matches.

            if 0 <= orf["percent_match"] <= self.threshold:

                pygame.draw.rect(self.lscreen, (150, 150, 150, 150), match_rectangle, 0)

            #This code defines the color and draws the matches.

            elif orf["percent_match"]  > self.threshold:
                color_match = (0, orf["percent_match"] , 0, 0)
                pygame.draw.rect(self.lscreen, color_match, match_rectangle, 0)

            #This code draws the percent matches when the cursor hovers over the matches.

            percent_match = orf["percent_match"]

            Mouse_Position = pygame.mouse.get_pos()
            if match_rectangle.collidepoint(Mouse_Position[0], Mouse_Position[1]-self.scroll_y):
                font = pygame.font.Font(None, 14)
                text = font.render(("   " + str(int(percent_match)) + " %"), 1, (250, 250, 210))
                self.lscreen.blit(text, (Mouse_Position[0], Mouse_Position[1]-self.scroll_y))

            #For comp values

            for comp_num, comp in enumerate(self.complement_only_orf):

                 #This makes sure that lengths of the contigs are oriented in the right direction.

                if comp["start"] > comp["end"]:
                    comp["start"], comp["end"] = comp["end"], comp["start"]
                    percent_match = comp["percent_match"]
                    #print 'start', start, 'end', end

                #This code draws the lighter blue bars that represent the contigs of the complement strand.

                comp_contig_length_rectangle = pygame.Rect(0,
                                       (self.Genome_Bar_Height + 10)*(comp_num*2+1),
                                        comp["length_item"]/self.comp_fact,
                                        self.Genome_Bar_Height
                                        )

                pygame.draw.rect(self.lscreen, (0,100,200,100), comp_contig_length_rectangle, 0)

                #This code draws the matches onto the contigs.

                comp_match_rectangle = pygame.Rect(float(comp["start"])/self.comp_fact,
                                            (self.Genome_Bar_Height + 10)*(comp_num*2+1),
                                            float(comp["end"]- comp["start"])/self.comp_fact,
                                            self.Genome_Bar_Height)

                #This code ensures that no orfs too short to be nitrogenase are used as such.

                if comp["end"] - comp["start"] < .8*comp["length_nitrogenase"]:
                    continue

                #This code defines the color and draws the false matches.

                if 0 <= comp["percent_match"] <= self.threshold:

                    pygame.draw.rect(self.lscreen, (150, 150, 150, 150), comp_match_rectangle, 0)

                #This code defines the color and draws the matches.

                elif comp["percent_match"]  > self.threshold:
                    color_match = (0, comp["percent_match"] , 0, 0)
                    pygame.draw.rect(self.lscreen, color_match, comp_match_rectangle, 0)

                #This code draws the percent matches when the cursor hovers over the matches.

                if comp_match_rectangle.collidepoint(Mouse_Position[0], Mouse_Position[1]-self.scroll_y):
                    font = pygame.font.Font(None, 14)
                    text = font.render(("   " + str(int(comp["percent_match"]) + " %"), 1, (250, 250, 210)) #
                    self.lscreen.blit(text, (Mouse_Position[0], Mouse_Position[1]-self.scroll_y))


    def update(self):

            self.screen.blit(self.lscreen, (0, self.scroll_y)) #This code updates the scrolling and screen.

            font = pygame.font.Font(None, 36) #This code creates the title and keeps it centered on the screen.
            text = font.render("Nitrogene Visualization", 1, (255, 255, 255))
            textpos = text.get_rect()
            self.screen.blit(text, textpos)
            self.screen.blit(self.screen, (0,0))

            img = pygame.image.load('Key.png') #This code draws the key onto the upper right corner of the screen.
            self.screen.blit(img,(513,0))

            pygame.display.flip()

class Nitrogenase_Controller(object):

    """ Initializes and executes scrolling through the up and down arrows."""

    def __init__(self, view):
        """Initialize view within the specialized model"""
        self.view = view

    def Key_Press (self): #Allows the up and down arrows to be used for scrolling.

        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 4:
                    self.view.scroll_y = min(self.view.scroll_y + 15, 0) #Allows the up arrow to be used.
                if e.button == 5:
                    self.view.scroll_y = max(self.view.scroll_y - 15, -6000) #Allows the down arrow to be used.


#Running the Code (Adapted from the in class brick breaker code.)

if __name__ == '__main__':

    pygame.init()
    lsize = (600, 6000) #W,L
    size = (600, 640)

    model = Nitrogene_Graph_Model(size)  #Initializes the model.
    view = Nitrogene_Graph_View(model, model.forward_only_orf, model.complement_only_orf) #Initializes the view.
    screen = pygame.display.set_mode(size) #Initializes the screen.
    running = True
    controller = Nitrogenase_Controller(view) #Initializes the controller.
    while running:
        view.draw() #Updates draw.
        view.update() #Updates the scrolling, screen, title, and key.
        controller.Key_Press() #updates the scrolling function.

