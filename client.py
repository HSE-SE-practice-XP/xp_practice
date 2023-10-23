import socket

import pygame
import sys
import selectors
import types
import Dice

class Client:
    def __init__(self, name):
        self.name = name
        self.s = None
        clicked = False
        dices = []


    def start_connection(self):
        server_addr = (self.host, self.port)
        print(f"Starting connection to {server_addr}")
        s = socket.socket()
        s.connect((self.host, self.port))

    def start_game(self):
        pygame.init()
        screen = pygame.display.set_mode([1000, 600])
        pygame.display.set_caption('Yahtzee')

        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

                if event.type == pygame.MOUSEBUTTONDOWN:








            pygame.display.flip()








if __name__ == "__main__":
    host, port = sys.argv[0], sys.argv[1]
    name = sys.argv[2]
    client = Client(host, port, name)
    client.start_connection()
    client.start_game()






