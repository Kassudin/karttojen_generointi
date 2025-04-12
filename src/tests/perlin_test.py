import unittest
from perlin import sulautus, lineaarinen_interpolointi, gradientti, kohina_2d
from generaattori import satunnaiset_pisteet
import math

class TestPerlin(unittest.TestCase):

    def test_sulautus(self):
        #6t^5-15t^4+10t^3
        #kun t(0) pitäisi palautua 0
        self.assertEqual(sulautus(0.0), 0.0)
        #t(1) palauttaa 1
        self.assertEqual(sulautus(1.0),1.0)
    
    def test_lineaarinen_interpolointi(self):
        #a+t*(b-a)
        #lerp(a,b,t) = lerp(5,12,7)
        #5+7*(12-5)=54
        self.assertEqual(lineaarinen_interpolointi(5,12,7), 54)
    
    def test_gradientti_h_0(self):
        #h=0 eli x+y
        self.assertEqual(gradientti(0, 3, 4), 3 + 4)
    
    def test_gradientti_h_1(self):
        #h=1 eli -x+y
        self.assertEqual(gradientti(1, 3, 4), -3 + 4)
    
    def test_gradientti_h_2(self):
        #h=2 eli x-y
        self.assertEqual(gradientti(2, 3, 4), 3 - 4)

    def test_gradientti_h_3(self):
        #h=3 eli -x-y
        self.assertEqual(gradientti(3, 3, 4), -3 - 4)

    def test_perlin_100_pistettä(self):
        #Perlin-kohinan tuottamat arvot #ovat teoreettisesti välillä [-sqrt(N)/4, sqrt(N)/4] 
        #missä N ulottuvuuksien määrä  #https://digitalfreepen.com/2017/06/20/range-perlin-noise.html
        #kaksiulotteinen eli N=2
        pisteet = satunnaiset_pisteet(1000)
        for i in range(len(pisteet)):
            x, y = pisteet[i]
            self.assertTrue(-math.sqrt(2)/4 <= kohina_2d(x, y) <= math.sqrt(2)/4)