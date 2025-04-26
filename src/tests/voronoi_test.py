import unittest
import math
from bowyer_watson import Kolmio
from voronoi_diagrammi import voronoi, kulma_suhteessa_pisteeseen


class Testvoronoi_diagrammi(unittest.TestCase):
  
    def test_karki_suhteessa_pisteeseen_nollakulma(self):
        kulma = kulma_suhteessa_pisteeseen((0,0),(1,0)) #tämä on 0 astetta
        self.assertAlmostEqual(kulma, 0)

    def test_karki_suhteessa_pisteeseen_pi(self):
        kulma = kulma_suhteessa_pisteeseen((0,0),(-1,0)) #tämä on pi
        self.assertAlmostEqual(kulma, math.pi)
    
    def test_voronoi_yksi_kolmio(self): #voronoi palauttaa kolmioiden kärjet
        kolmio = Kolmio((0,0),(0,2),(2,0))
        tulos = voronoi([kolmio])
        self.assertEqual(len(tulos), 3) #kolme kärkeä
    
    def test_yhteinen_karki(self): 
        kolmio = Kolmio((0,0),(0,2),(2,0))
        kolmio2 = Kolmio((2,2),(2,0),(-1,-1)) 
        tulos = voronoi([kolmio, kolmio2])
        #yhteinen kärki (2,0)
        self.assertEqual(len(tulos), 5)
    
    def test_ei_monikulmioita(self):
        kolmio = Kolmio((0, 0), (1, 1), (2, 2))
        kolmio2 = Kolmio((3, 3), (4, 4), (5, 5))
        tulos = voronoi([kolmio, kolmio2])
        for karki in (kolmio.A, kolmio.B, kolmio.C, kolmio2.A, kolmio2.B, kolmio2.C):
            self.assertIn(karki, tulos)
            # tarkistetaan, että kärjille ei ole monikulmioita
            self.assertEqual(tulos[karki], [])
    