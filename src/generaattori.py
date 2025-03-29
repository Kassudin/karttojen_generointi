import pygame
import random
import sys
from bowyerwatson import BowyerWatson

def satunnaiset_pisteet(n=250):
    return [(random.randint(0,800),random.randint(0,600)) for _ in range(n)] 

def generoi_kuva(): # pragma: no cover 
    pygame.init()
    naytto = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Bowyer-Watson")
    naytto.fill((255, 255, 255))
    pygame.display.flip()
    pisteet = satunnaiset_pisteet()
    kolmiot = BowyerWatson(pisteet)  
    for p in pisteet:
        pygame.draw.circle(naytto, (0,0,0), p, 2)
    for kolmio in kolmiot:
        pygame.draw.polygon(naytto,(0,0,0),[kolmio.A, kolmio.B, kolmio.C], 1)
    pygame.display.flip()
    running = True
    while running:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                running = False
            elif tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_RETURN:
                    naytto.fill((255, 255, 255)) #tyhjennetään
                    pisteet = satunnaiset_pisteet()
                    kolmiot = BowyerWatson(pisteet)  
                    for p in pisteet:
                        pygame.draw.circle(naytto, (0,0,0), p, 2)
                    for kolmio in kolmiot:
                        pygame.draw.polygon(naytto,(0,0,0),[kolmio.A, kolmio.B, kolmio.C], 1)
                    pygame.display.flip()
    pygame.quit()
    sys.exit
            
if __name__ == "__main__": # pragma: no cover
    generoi_kuva()








