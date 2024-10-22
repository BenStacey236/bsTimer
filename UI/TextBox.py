import pygame

from AppAssets.AppPresets import *
from AppAssets.KeyDict import KeyDict


class TextBox:
    def __init__(self, x:int, y:int, saved_text:str):
        # Initialises variables for later use
        self.saved_text = saved_text
        self.input_text = saved_text
        self.selected = False
        self.x, self.y = x, y
        self.__WIDTH, self.__HEIGHT = 203, 26
        self.cursor_count = 0
    

    def select(self):
        'Selects the text box'
        
        self.selected = True

    
    def deselect(self):
        'Deselects the text box'
        
        self.selected = False
        self.saved_text = self.input_text


    def is_clicked(self):
        'Returns a boolean value corresponding if the text box is clicked'
        
        mouse_pos = pygame.mouse.get_pos()
        
        if pygame.mouse.get_pressed()[0] and self.text_rect.collidepoint(mouse_pos):
            self.select()
            return True
        
        else:
            self.deselect()
            return False


    def input_key(self, key:pygame.key, shift:bool):
        'Inputs the character corresponding to the passed pygame key into the text box'
        
        # Removes the last character from the text box when backspace pressed
        if key == pygame.K_BACKSPACE:
            self.input_text = self.input_text[:-1]
        
        # Deselects the text box if enter is pressed
        elif key == pygame.K_RETURN: self.deselect()
        
        else:
            try: 
                # If shift is held, input the capital form of the letter
                if shift and ord(KeyDict[key])>96: self.input_text += chr(ord(KeyDict[key])-32)
                # Otherwise inputs the pressed key
                else: self.input_text += KeyDict[key]
            except:
                print('This character can not be inputted')
    

    def draw(self, surface:pygame.surface):
        'Method that draws the text box and contents to the passed surface'
        
        # Logic for the flashing of the cursor in text box
        if self.selected: self.cursor_count += 1
        if self.cursor_count == 120: self.cursor_count = 0

        # Renders text ready for drawing to screen
        self.drawing_text = SOLVES_TITLE_FONT.render(self.input_text, True, BASICALLY_WHITE)
        self.text_rect = self.drawing_text.get_rect(midleft=(self.x+2, self.y+15))
        
        # If text overfills the text box, then text is scrolled to fit
        if self.text_rect.right > self.x+self.__WIDTH:
            offset = (self.text_rect.right-(self.x+self.__WIDTH))//9
            self.drawing_text = SOLVES_TITLE_FONT.render(self.input_text[offset:], True, BASICALLY_WHITE)
            self.text_rect = self.drawing_text.get_rect(midleft=(self.x+2, self.y+15))

        # Draw Box and cursor
        pygame.draw.polygon(surface, (110, 110, 110) if self.selected else VV_LIGHT_GREY, [(self.x, self.y), (self.x+self.__WIDTH, self.y), (self.x+self.__WIDTH, self.y+self.__HEIGHT), (self.x, self.y+self.__HEIGHT)])
        pygame.draw.polygon(surface, LIGHT_GREY, [(self.x-2, self.y-2), (self.x+self.__WIDTH+2, self.y-2), (self.x+self.__WIDTH+2, self.y+self.__HEIGHT+2), (self.x-2, self.y+self.__HEIGHT+2)], width=2)
        if self.selected and self.cursor_count <= 60: pygame.draw.line(surface, BASICALLY_WHITE, (self.text_rect.right+1, self.y+2), (self.text_rect.right+1, self.y+24), 2)

        # Draws text to the screen
        surface.blit(self.drawing_text, self.text_rect)