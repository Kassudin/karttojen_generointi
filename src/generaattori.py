import pygame
import random
import sys
from voronoi_diagrammi import BowyerWatson, voronoi

def satunnaiset_pisteet(n=80):
    return [(random.randint(0, 1920), random.randint(0, 1080)) for _ in range(n)] 

def generoi_kuva(): #pragma no cover
    pygame.init()
    naytto = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("Proseduraalinen kartta")
    naytto.fill((100, 149, 237, 255))
    pygame.display.flip()
    pisteet = satunnaiset_pisteet()
    kolmiot = BowyerWatson(pisteet)
    voronoi_kuva = voronoi(kolmiot)
    for kolmio in kolmiot:
        pygame.draw.polygon(naytto, (0, 0, 0), [kolmio.A, kolmio.B, kolmio.C], 1)
        pygame.display.flip() #päivitetään näyttö
        pygame.time.wait(20) 
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    pygame.time.wait(30)  
    for _, monikulmiot in voronoi_kuva.items():
        if len(monikulmiot) >= 3: #tarvitaan kolme pistettä, jotta voidaan piirtää monikulmio 
            pygame.draw.polygon(naytto, (0, 255, 0), monikulmiot, 1)
            pygame.display.flip()
            pygame.time.wait(20)
            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    pygame.time.wait(1000)
    naytto.fill((100, 149, 237, 255))  
    sininen = (100, 149, 237, 255)
    vihrea = (69, 139, 0, 255)
    for _, monikulmiot in voronoi_kuva.items():
        if len(monikulmiot) >= 3:
            valittu_vari = random.choice([sininen, vihrea, vihrea, vihrea])
            pygame.draw.polygon(naytto, valittu_vari, monikulmiot, 0)
            pygame.display.flip()
            pygame.time.wait(20)
            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    running = True
    while running:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                running = False
    pygame.quit()
    sys.exit()
if __name__ == "__main__": #pragma no cover
    generoi_kuva()
