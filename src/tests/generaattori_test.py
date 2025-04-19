import unittest

from generaattori import satunnaiset_pisteet, biomin_vari

class TestGeneraattori(unittest.TestCase):

    def test_satunnaiset_pisteet_oikea_maara(self):
        pisteet = satunnaiset_pisteet(n=25)
        self.assertEqual(len(pisteet),25)

    def test_syva_vesi(self):
        x = -0.6
        self.assertEqual(biomin_vari(x), (25, 50, 80)) 

    def test_rantavesi(self):
        x = -0.4
        self.assertEqual(biomin_vari(x), (80, 120, 150)) 
    
    def test_hiekkaranta(self):
        x = -0.2
        self.assertEqual(biomin_vari(x), (210, 200, 160)) 
    
    def test_laakso(self):
        x = 0.0
        self.assertEqual(biomin_vari(x), (170, 190, 140))
    
    def test_metsa(self):
        x = 0.2
        self.assertEqual(biomin_vari(x), (140, 170, 120))

    def test_kukkulat(self):
        x = 0.4
        self.assertEqual(biomin_vari(x), (120, 100, 80))

    def test_vuori(self):
        x = 0.6
        self.assertEqual(biomin_vari(x), (160, 140, 120))
    
    def test_lumi(self):
        x = 0.8
        self.assertEqual(biomin_vari(x), (230, 230, 230))
    
    def test_raja(self):
        x = 1.0
        self.assertEqual(biomin_vari(x), (230, 230, 230))
