import pygame
import random
import sys
from voronoi_diagrammi import BowyerWatson, voronoi
from perlin import kohina_2d

def satunnaiset_pisteet(n=2000):
    return [(random.randint(0, 1920), random.randint(0, 1080)) for _ in range(n)] 

def biomin_vari(x):
    normalisoitu = (x + 1.0) / 2.0 #normalisoidaan arvo välille [0,1]
    #https://en.wikipedia.org/wiki/Feature_scaling
    #helpottaa värien valintaa
    if normalisoitu < 0.25:
        return (25, 50, 80)    # Syvä vesi
    elif normalisoitu < 0.40:
        return (80, 120, 150)  # Rantavesi
    elif normalisoitu < 0.45:
        return (210, 200, 160) # Hiekkaranta
    elif normalisoitu < 0.60:
        return (170, 190, 140) # Laakso
    elif normalisoitu < 0.70:
        return (140, 170, 120) # Metsä
    elif normalisoitu < 0.80:
        return (120, 100, 80)  # Kukkula
    elif normalisoitu < 0.90:
        return (160, 140, 120) # Vuori
    else:
        return (230, 230, 230) # Lumi

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
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    pygame.time.wait(10)  
    for _, monikulmiot in voronoi_kuva.items():
        if len(monikulmiot) >= 3: #tarvitaan kolme pistettä, jotta voidaan piirtää monikulmio 
            pygame.draw.polygon(naytto, (0, 255, 0), monikulmiot, 1)
            pygame.display.flip()
            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    pygame.time.wait(1000) 
    pygame.time.wait(500)
    naytto.fill((80, 120, 150))  
    for karki, monikulmiot in voronoi_kuva.items():
        if len(monikulmiot) >= 3:
            #ilman /300 jakoa tulisi vain yhtä väriä
            perlin_arvo = kohina_2d(karki[0]/300, karki[1]/300) #kohinan arvo kolmion kärjessä
            biomi = biomin_vari(perlin_arvo)
            pygame.draw.polygon(naytto, biomi, monikulmiot, 0)
            pygame.display.flip()
            pygame.time.wait(5)
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
