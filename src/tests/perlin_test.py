import unittest
import math
import random
from perlin import sulautus, lineaarinen_interpolointi, gradientti, kohina_2d
from generaattori import satunnaiset_pisteet


class TestPerlin(unittest.TestCase):
    def test_sulautus(self):
        # 6t^5-15t^4+10t^3
        # Kun t(0) pitäisi palautua 0.
        self.assertEqual(sulautus(0.0), 0.0)
        # t(1) palauttaa 1.
        self.assertEqual(sulautus(1.0),1.0)
        # t(0.5) palauttaa 0.5.
        self.assertEqual(sulautus(1.0), 1.0)
    
    def test_lineaarinen_interpolointi(self):
        # a+t*(b-a)
        # lerp(a,b,t) = lerp(5,12,7)
        # 5+7*(12-5)=54
        self.assertEqual(lineaarinen_interpolointi(5,12,7), 54)
    
    def test_gradientti_h_0(self):
        # h=0 eli x+y
        self.assertEqual(gradientti(0, 3, 4), 3 + 4)
    
    def test_gradientti_h_1(self):
        # h=1 eli -x+y
        self.assertEqual(gradientti(1, 3, 4), -3 + 4)
    
    def test_gradientti_h_2(self):
        # h=2 eli x-y
        self.assertEqual(gradientti(2, 3, 4), 3 - 4)

    def test_gradientti_h_3(self):
        # h=3 eli -x-y
        self.assertEqual(gradientti(3, 3, 4), -3 - 4)

    def test_perlin_100_pistetta(self):
        # Perlin-kohinan tuottamat arvot #ovat teoreettisesti välillä [-sqrt(N)/4, sqrt(N)/4],
        # missä N ulottuvuuksien määrä  #https://digitalfreepen.com/2017/06/20/range-perlin-noise.html.
        # Kaksiulotteinen eli N=2
        pisteet = satunnaiset_pisteet(1000)
        for x, y in pisteet:
            self.assertTrue(-math.sqrt(2)/4 <= kohina_2d(x, y) <= math.sqrt(2)/4)
    
    def test_perlin_jatkuvuus(self):
        # Pieni siirto aiheuttaa vain pienen muutoksen.
        for _ in range(1000):
            x, y = random.random(), random.random()
            # Testatessa ero oli 0.00176293846534481 eli sallitaan 0.01 ero.
            self.assertAlmostEqual(kohina_2d(x, y), kohina_2d(x + 0.001, y ), delta=0.01)

    def test_perlin_eri_arvot(self):
        # Eri koordinaatit tuottavat eri arvoja.
        for _ in range(1000):
            x, y = random.random(), random.random()
            self.assertNotEqual(kohina_2d(x, y), kohina_2d(x + 0.0001, y + 0.0001))
    
    def test_kohinan_jakauma(self):
        # Kohinan tulisi olla jakautunut lähelle nollaa, kun  välillä [-sqrt(N)/4, sqrt(N)/4].
        pisteet = satunnaiset_pisteet(1000)
        arvot = []
        for piste in pisteet:
            x, y = piste
            arvot.append(kohina_2d(x, y))
        keskiarvo = sum(arvot) / len(arvot)
        self.assertAlmostEqual(keskiarvo, 0.0, delta=0.01)

    def test_jakauman_arvot(self):
        # Ainakin 50% tuloksista pitäisi olla lähellä nollaa.
        pisteet = satunnaiset_pisteet(1000)
        arvot = []
        for piste in pisteet:
            x, y = piste
            arvot.append(kohina_2d(x, y))
        osuus = sum(-0.1 <= arvo <= 0.1 for arvo in arvot) / len(arvot)
        self.assertGreater(osuus, 0.5)

    def test_kohinan_sileys(self):
        # Kohinan tulisi olla jokaisessa x,y pisteessä derivoituva.
        # Pienillä siirroilla derivaatan arvo ei pitäisi muuttua kovinkaan paljon.
        # Hyvin pieni muutos = sileä.
        pisteet = satunnaiset_pisteet(1000)
        h = 1e-3
        for piste in pisteet:
            x, y = piste
            # Olkoon f(x) = kohinan tuottava arvo pisteessä (x,y).
            # Tällöin f'(x) ≈ [f(x+h,y) – f(x–h,y)] / (2h).
            df1 = (kohina_2d(x + h, y) - kohina_2d(x - h, y)) / (2 * h)
            # Ja hyvin lähellä yllä olevaa.
            df2 = (kohina_2d(x + 0.0001 + h, y) - kohina_2d(x + 0.0001 - h, y)) / (2 * h)
            # Varmistetaan, että ovat lähes samat.
            self.assertAlmostEqual(df1, df2, delta=0.01)

    def test_solmukohdat(self):
        # Perlin-kohinassa 2D-solmukohdissa (kokonaiskoordinaateissa) arvo on nolla
        for _ in range(1000):
            x = random.randint(0, 1920) # Leveys.
            y = random.randint(0, 1080) # Korkeus.
            arvo = kohina_2d(x, y)
            self.assertEqual(arvo, 0.0)
