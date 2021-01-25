from pythonping import ping
from time import sleep
import pygame
import sys


class Programm:
    def __init__(self):

        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((600,300))
        pygame.display.set_caption("Ping")

        self.ypings = [0]
        self.mean_ping = sum(self.ypings)/len(self.ypings)

    def get_ping(self)->None:
    	x = ping('8.8.8.8', count=1)
    	self.ypings.append(int(round(float(str(x).split("\n")[2].split("/")[-2]),0)))

    def _draw_ping(self)->None:
    	j = 10
    	mult = 580/len(self.ypings)
    	for i in range(len(self.ypings)-1):
    		if self.mean_ping < self.ypings[i]:
    			color = (255,0,0)
    		else:
    			color = (0,0,255)
    		pygame.draw.line(self.screen, color,(10+mult*i, 240-self.ypings[i]), (10+mult*(i+1), 240-self.ypings[i+1]), 1)
    
    def _draw_text(self, ping: str)->None:
        font = pygame.font.SysFont('Comic Sans MS', 30)
        ping_text = font.render(ping + "ms", False, (255, 255, 255))
        
        self.screen.blit(ping_text, (290, 50))
        
    def _update_screen(self)->None:
        self.mean_ping = sum(self.ypings)/len(self.ypings)
        self.screen.fill((255, 255, 255))
        self.get_ping()
        self._draw_ping()
        self._draw_text(str(self.ypings[-1]))
        if len(self.ypings) > 30:
            del self.ypings[0]
        pygame.display.flip()
        sleep(.05)

    def run(self)->None:
    	while True:
    		self._update_screen()


s = Programm()
s.run()

	

