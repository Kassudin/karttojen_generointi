import unittest
from bowyerwatson import Kolmio, superkolmio, kehäympyrän_keskipiste, onko_piste_kehäympyrän_sisällä, BowyerWatson
from generaattori import satunnaiset_pisteet

class TestBowyerWatson(unittest.TestCase):

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
        u = kehäympyrän_keskipiste(a,b,c)
        #tämän ymypyrän kehäpiste on 1,1
        self.assertAlmostEqual(u[0], 1)
        self.assertAlmostEqual(u[1], 1)

    def test_onko_piste_kehäympyrän_sisällä(self):
        a = (0,0)
        b = (0,2)
        c = (2,0)
        #tämän ympyrän säde on 1.41
        self.assertTrue(onko_piste_kehäympyrän_sisällä(a,b,c,(1,1))) #sisäpuolella
        self.assertTrue(onko_piste_kehäympyrän_sisällä(a,b,c,(0,0))) #reunalla
        self.assertFalse(onko_piste_kehäympyrän_sisällä(a,b,c,(0,3))) #ulkopuolella
    
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
        pisteet = satunnaiset_pisteet(10)
        kolmiot = BowyerWatson(pisteet)
        self.assertTrue(10 <= len(kolmiot) <= 13)

    def test_satunnaiset_pisteet_oikea_maara(self):
        pisteet = satunnaiset_pisteet(n=25)
        self.assertEqual(len(pisteet),25)
        