import math


class Kolmio:
    # Kolmion tiedot (pisteet sekä reunat).
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        self.reunat = {(A,B),(B,C),(A,C)}

def superkolmio(pisteet):
    # "Add super-triangle to triangulation
    # Must be large enough to completely contain all the points in pointList"
    # Muodostetaan annetuista pisteistä aluksi mahdollisimman pieni suorakulmio.
    # Kuitenkin, että kaikki pisteet ovat tämän sisällä.
    # Tämä auttaa meitä muodostamaan tarpeeksi suuren superkolmion tämän ympärille.
    # https://bit-101.com/blog/posts/2024-02-11/supertriangle/.
    # Tarkastellaan annettuja pisteitä ja etsitään sieltä (x,y) koordinaattien minimi ja maksimi arvot.
    min_x = pisteet[0][0]
    max_x = pisteet[0][0]
    min_y = pisteet[0][1]
    max_y = pisteet[0][1]
    for (x, y) in pisteet:
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y
    # Suorakulmion leveys ja korkeus.
    leveys = max_x - min_x
    korkeus = max_y-min_y
    # Olkoon superkolmion pohjan korkeus 3*suorakulmion korkeus.
    pohja= korkeus*3
    keskipiste = (min_y + max_y) /2
    # Siirretään superkolmion pohjaa hieman irti suorakulmion vasemmasta reunasta.
    offset = leveys / 5
    pohjan_keskipiste = pohja / 2
    A =(min_x - offset, keskipiste-pohjan_keskipiste)
    B =(min_x - offset, keskipiste+pohjan_keskipiste)
    # Kolmion kärki on suorakulmion korkeuden keskipiste, ja oikeasta reunasta etäällä.
    C = (3 * leveys, keskipiste)
    return Kolmio(A, B, C)

def kehaympyran_keskipiste(A,B,C): 
    # Kolmion kehäympyrän laskemiseen tarvittavat kaavat
    # https://en.wikipedia.org/wiki/Circumcircle#Circumcenter_coordinates.
    Ax, Ay = A
    Bx, By = B
    Cx, Cy = C
    D = 2*(Ax*(By-Cy)+Bx*(Cy-Ay)+Cx*(Ay-By))
    if D == 0: # Ei voida jakaa nollalla.
        return None
    # Nyt voimme laskea ux ja uy, jotta voidaan muodostaa keskipiste U.
    Ux = 1/D*((Ax*Ax+Ay*Ay)*(By-Cy)+(Bx*Bx+By*By)*(Cy-Ay)+(Cx*Cx+Cy*Cy)*(Ay-By))
    Uy = 1/D*((Ax*Ax+Ay*Ay)*(Cx-Bx)+(Bx*Bx+By*By)*(Ax-Cx)+(Cx*Cx+Cy*Cy)*(Bx-Ax))
    # Palautetaan keskipiste U.
    return (Ux,Uy)

def onko_piste_kehaympyran_sisalla(A,B,C,P):
    # Tarkistetaan onko piste P kolmion ABC kehäympyrän sisällä.
    U = kehaympyran_keskipiste(A,B,C)
    if U is None:
        return False
    # Lasketaan etäisyys keskipisteestä pisteeseen A ympyrän eli ympyrän säde r.
    r = math.sqrt((U[0]-A[0])**2+(U[1]-A[1])**2)
    # Lasketaan pisteestä P etäisyys keskipisteeseen.
    d = math.sqrt((U[0]-P[0])**2+(U[1]-P[1])**2)
    # Jos etäisyys on pienempi tai yhtäsuuri kuin säde, on piste kehäympyrän sisällä.
    return d<=r

def BowyerWatson(pisteet):
    # Seurataan pseudokoodia https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm.
    # Muodostetaan superkolmio.
    sk = superkolmio(pisteet) 
    # Lisätään superkolmio kolmioiden listaan.
    kolmiot = [sk]
    # Käydään pisteet läpi.
    for piste in pisteet:
        # Huonot kolmiot omaan listaan.
        huonot_kolmiot = []
        for kolmio in kolmiot:
            # Tarkistetaan onko piste kolmion kehäympyrän sisällä.
            if onko_piste_kehaympyran_sisalla(kolmio.A, kolmio.B, kolmio.C, piste):
                # Jos on, lisätään kolmio huonojen kolmioiden listaan.
                huonot_kolmiot.append(kolmio)
        monikulmiot = set()
        # Käydään huonot kolmiot läpi.
        for huonot in huonot_kolmiot:
            for reuna in huonot.reunat:
                # Jos reuna ei ole jaettu minkään muun huonon kolmion kanssa,
                if reuna not in monikulmiot: # Lisätään se.
                    monikulmiot.add(reuna)
                else:
                    monikulmiot.remove(reuna)
                    # Poistetaan. Reuna tuli vastaan toisessa huonossa kolmiossa.
        for huono_kolmio in huonot_kolmiot:
            kolmiot.remove(huono_kolmio) # Poistetaan huonot kolmiot kolmioiden listasta.
        # Olkoon piste p yksi kolmion koordinaateista.
        for A,B in monikulmiot:
            kolmiot.append(Kolmio(A,B,piste)) # Lisätään kolmio kolmioiden listaan.
    deluaunay = [] # Nyt muodostetaan lopullinen triangulaatio.
    for kolmio in kolmiot: # Käydään kolmiolista läpi.
        sk_karjet=(sk.A,sk.B,sk.C) # Superkolmion kärjet.
        if kolmio.A in sk_karjet or kolmio.B in sk_karjet or kolmio.C in sk_karjet:
            # Jos kolmio jakaa superkolmion kärjen, niin ei oteta sitä mukaan.
            continue
        deluaunay.append(kolmio) # Muut lisätään listaan.
    # Palautetaan lista kolmioista, jotka toteuttavat Deluaunay triangulaation.
    return deluaunay
