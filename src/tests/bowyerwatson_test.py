import unittest
from bowyerwatson import Kolmio, superkolmio, kehäympyrä, onko_piste_kehäympyrän_sisällä

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

    def test_kehäympyrä(self):
        a = (0,0)
        b = (0,2)
        c = (2,0)
        u = kehäympyrä(a,b,c)
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

