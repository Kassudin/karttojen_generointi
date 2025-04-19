import unittest
from bowyer_watson import Kolmio, superkolmio, kehaympyrän_keskipiste, onko_piste_kehaympyrän_sisällä, BowyerWatson
from generaattori import satunnaiset_pisteet
import math

class TestBowyer_Watson(unittest.TestCase):

    def test_kolmio(self):
        a = (0,0)
        b = (0,2)
        c = (2,0)
        k = Kolmio(a,b,c)
        self.assertEqual(k.A, a)
        self.assertEqual(k.B, b)
        self.assertEqual(k.C, c)
        self.assertEqual(k.reunat, {(a,b),(b,c),(a,c)})

    def test_superkolmio(self):
        pisteet = [(1,1),(0,0),(2,2)] #alue on 2x2 (0,0)(0,2)(2,0)(2,2)
        result = superkolmio(pisteet)
        self.assertEqual(result.A, (-0.4, -2))
        self.assertEqual(result.B, (-0.4, 4))
        self.assertEqual(result.C, (6,1))

    def test_kehäympyrän_keskipiste(self):
        a = (0,0)
        b = (0,2)
        c = (2,0)
        u = kehaympyrän_keskipiste(a,b,c)
        #tämän ymypyrän kehäpiste on 1,1
        self.assertAlmostEqual(u[0], 1)
        self.assertAlmostEqual(u[1], 1)

    def test_onko_piste_kehäympyrän_sisällä(self):
        a = (0,0)
        b = (0,2)
        c = (2,0)
        #tämän ympyrän säde on 1.41
        self.assertTrue(onko_piste_kehaympyrän_sisällä(a,b,c,(1,1))) #sisäpuolella
        self.assertTrue(onko_piste_kehaympyrän_sisällä(a,b,c,(0,0))) #reunalla
        self.assertFalse(onko_piste_kehaympyrän_sisällä(a,b,c,(0,3))) #ulkopuolella
    
    def test_pisteet_kollineaarisia(self):
        a = (0, 0)
        b = (1, 1)
        c = (2, 2)
        #U palauttaa None vaikka piste on sisällä
        self.assertFalse(onko_piste_kehaympyrän_sisällä(a, b, c, (1,1)))
     
    def test_bowyer_watson_yksi_kolmio(self):
        pisteet = [(4,2),(0,0),(2,2)]
        result = BowyerWatson(pisteet)
        self.assertEqual(len(result), 1)

    def test_bowyer_watson_pisteet_kollineaarisia(self):
        pisteet = [(0,0),(1,1),(2,2)]
        kolmiot = BowyerWatson(pisteet)
        self.assertEqual(len(kolmiot), 0)

    def test_bowyer_watson_liian_vahan_pisteita(self):
        pisteet = [(1,1),(0,0)]
        kolmiot = BowyerWatson(pisteet)
        self.assertEqual(len(kolmiot), 0)

    def test_bowyer_watson_10_satunnaista_pistetta(self):
        #kolmioiden määrä voidaan laskea kaavalla = 2n-2-h
        #missä n= pisteiden määrä ja h=konveksisen hilan reunapisteiden määrä
        pisteet = [
        (0,0), (3,0), (4,2), (3,4), (0,3), (-1,3),  #reunapisteet 6kpl
        (1,1), (2,1), (2,1), (2,2)                    
        ]
        kolmiot = BowyerWatson(pisteet)
        #pisteitä yhteensä 10 eli kolmioita muodostuu 2*10-2-6=12
        self.assertTrue(len(kolmiot), 12)
    
    def test_bowyer_watson_ei_superkolmiota(self):
        #testataan, että yksikään kolmio ei jaa kärkeä superkolmion kanssa
        pisteet = [(0,0), (3,0), (4,2), (3,4), (0,3), (-1,3)]
        sk = superkolmio(pisteet)
        kolmiot = BowyerWatson(pisteet)
        for kolmio in kolmiot:
            self.assertNotEqual(kolmio, sk)
