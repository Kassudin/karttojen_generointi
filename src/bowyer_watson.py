import math

class Kolmio:
    #tähän kolmion tiedot
    #pisteet sekä reunat
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        self.reunat = {(A,B),(B,C),(A,C)}

def superkolmio(pisteet):
    #"add super-triangle to triangulation // must be large enough to completely contain all the points in pointList"
    #muodostetaan annetuista pisteistä aluksi mahdollisimman pieni suorakulmio, kuitenkin, että kaikki pisteet ovat tämän sisällä
    #tämä auttaa meitä muodostamaan tarpeeksi suuren superkolmion tämän ympärille
    #https://bit-101.com/blog/posts/2024-02-11/supertriangle/
    #tarkastellaan annettuja pisteitä, ja etsitään sieltä x ja y koordinaattien minimi ja maksimi arvot
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
    #suorakulmion leveys ja korkeus
    leveys = max_x - min_x
    korkeus = max_y-min_y
    #olkoon superkolmion pohjan korkeus 3*suorakulmion korkeus
    pohja= korkeus*3
    keskipiste = (min_y + max_y) /2
    #siirretään superkolmion pohjaa hieman irti suorakulmion vasemmasta reunasta 
    offset = leveys / 5
    pohjan_keskipiste = pohja / 2
    A =(min_x - offset, keskipiste-pohjan_keskipiste)
    B =(min_x - offset, keskipiste+pohjan_keskipiste)
    #kolmion kärki on suorakulmion korkeuden keskipiste, ja oikeasta reunasta etäällä.
    C = (3 * leveys, keskipiste)
    return Kolmio(A, B, C)

def kehaympyrän_keskipiste(A,B,C): 
    #kolmion kehäympyrän laskemiseen tarvittavat kaavat 
    #https://en.wikipedia.org/wiki/Circumcircle#Circumcenter_coordinates 
    Ax,Ay = A
    Bx,By = B
    Cx,Cy = C
    D = 2*(Ax*(By-Cy)+Bx*(Cy-Ay)+Cx*(Ay-By))
    if D == 0: #ei voida jakaa nollalla
        return None
    #nyt voimme laskea ux ja uy, jotta voidaan muodostaa keskipiste U
    Ux = 1/D*((Ax*Ax+Ay*Ay)*(By-Cy)+(Bx*Bx+By*By)*(Cy-Ay)+(Cx*Cx+Cy*Cy)*(Ay-By))
    Uy = 1/D*((Ax*Ax+Ay*Ay)*(Cx-Bx)+(Bx*Bx+By*By)*(Ax-Cx)+(Cx*Cx+Cy*Cy)*(Bx-Ax))
    #palautetaan keskipiste U
    return (Ux,Uy)

def onko_piste_kehaympyrän_sisällä(A,B,C,P):
    #tarkistetaan onko piste P kolmion ABC kehäympyrän sisällä
    U = kehaympyrän_keskipiste(A,B,C)
    if U == None:
        return False
    #lasketaan etäisyys keskipisteestä pisteeseen A ympyrän eli ympyrän säde r
    r = math.sqrt((U[0]-A[0])**2+(U[1]-A[1])**2)
    #lasketaan pisteestä P etäisyys keskipisteeseen
    d = math.sqrt((U[0]-P[0])**2+(U[1]-P[1])**2)
    #jos etäisyys on pienempi tai yhtäsuuri kuin säde, on piste kehäympyrän sisällä
    return d<=r    

def BowyerWatson(pisteet):
    #seurataan pseudokoodia https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm
    #muodostetaan superkolmio
    sk = superkolmio(pisteet) 
    #lisätään superkolmio kolmioiden listaan
    kolmiot = [sk]
    #käydään pisteet läpi   
    for piste in pisteet:
        #huonot kolmiot omaan listaan
        huonot_kolmiot = []
        for kolmio in kolmiot:
            #tarkistetaan onko piste kolmion kehäympyrän sisällä
            if onko_piste_kehaympyrän_sisällä(kolmio.A, kolmio.B, kolmio.C, piste):
                #jos on, lisätään kolmio huonojen kolmioiden listaan
                huonot_kolmiot.append(kolmio)
        monikulmiot = set()
        #käydään huonot kolmiot läpi
        for huonot in huonot_kolmiot:
            for reuna in huonot.reunat:
                #jos reuna ei ole jaettu minkään muun huonon kolmion kanssa
                if reuna not in monikulmiot: 
                    monikulmiot.add(reuna) #lisätään se 
                else:
                    monikulmiot.remove(reuna) #poistetaan, reuna tuli vastaan toisessa huonossa kolmiossa
        for huono_kolmio in huonot_kolmiot:
            kolmiot.remove(huono_kolmio)#poistetaan huonot kolmiot kolmioiden listasta
        #olkoon piste p yksi kolmion koordinaateista
        for A,B in monikulmiot:
            kolmiot.append(Kolmio(A,B,piste)) #lisätään kolmio kolmioiden listaan
    deluaunay = [] #nyt muodostetaan lopullinen triangulaatio
    for kolmio in kolmiot: #käydään  kolmiolista läpi
        sk_karjet=(sk.A,sk.B,sk.C) #superkolmion kärjet
        if kolmio.A in sk_karjet or kolmio.B in sk_karjet or kolmio.C in sk_karjet: #jos kolmio jakaa superkolmion kärjen niin ei oteta sitä mukaan
            continue
        deluaunay.append(kolmio) #muut lisätään listaan
    #palautetaan lista kolmioista, jotka toteuttavat Deluaunay triangulaation
    return deluaunay
