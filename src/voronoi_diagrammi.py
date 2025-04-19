import math
from bowyer_watson import kehaympyrän_keskipiste, BowyerWatson
def kulma_suhteessa_pisteeseen(kolmionkärki, piste): #atan2 palauttaa kulman radiaaneina kahden pisteen välillä. 
    #lasketaan kulma kolmion kärjen ja pisteen välillä
    #https://stackoverflow.com/questions/42258637/how-to-know-the-angle-between-two-vectors
    return math.atan2(piste[1]-kolmionkärki[1], piste[0]-kolmionkärki[0])
    #tämän avulla voimme järjestää myöhemmin kolmion kärjen ympärillä olevat kehäympyrän keskipisteet järjestykseen
    
def voronoi(deluaunay):
    #https://stackoverflow.com/questions/85275/how-do-i-derive-a-voronoi-diagram-given-its-point-set-and-its-delaunay-triangula
    #jotta voimme piirtää ja värittää pygamella voronoin monikulmiot, meidän pitää määritellä monikulmioiden kaikki pisteet
    #tarvitsemme deluaunay kolmion kärkipisteen. Voronoi-diagrammissa kärkeä ympäröivät kehäympyröiden keskipisteet muodostavat monikulmion
    #eli lasketaan niiden kolmioioden kehäympyröiden keskipisteet, jotka jakavat pisteen yhtenä kolmion kärkenä
    #nämä lasketut kehäympyrän keskipisteet muodostavat monikulmion kolmion kärjen A ympärille.
    karki_pisteena = {}
    for kolmio in deluaunay:
        for piste in (kolmio.A, kolmio.B, kolmio.C):
            if piste not in karki_pisteena:
                karki_pisteena[piste] = []
            karki_pisteena[piste].append(kolmio)
    #nyt meillä on sanakirja pisteistä, joiden arvoina on kolmiot johon piste kuuluu
    voronoi_diagrammi = {} #avaimena kolmion kärki (piste), arvona niiden kolmioiden kehäympyröiden keskipisteet, jotka jakavat tämän kärjen
    for piste, kolmiot in karki_pisteena.items():
        kehaympyran_keskipisteet = []
        for kolmio in kolmiot: #pisteen jakamat kolmiot
            keskipiste = kehaympyrän_keskipiste(kolmio.A, kolmio.B, kolmio.C)
            if keskipiste is not None: 
                kehaympyran_keskipisteet.append(keskipiste)
        #kehäympyröiden keskipisteet on nyt listassa, mutta ei järjestyksessä
        #Tämä on ongelma, sillä jos jätämme nämä tällä tavalla, niin monikulmiota ei synny
        def kulmat(kehaympyran_keskipiste): #apufunktio
            return kulma_suhteessa_pisteeseen(piste, kehaympyran_keskipiste) #lasketaan radiaanit kaikille kehäympyröiden keskipisteille
        kehaympyran_keskipisteet.sort(key=kulmat) #järjestetään nousevaan järjestyksen
        #tätä voi ajatella yksikköympyränä, jossa kolmion kärki (keskipiste) on origossa.
        voronoi_diagrammi[piste]= kehaympyran_keskipisteet #nyt sanakirja sisältää kärjen ja sen ympärillä olevat kehäympyröiden keskipisteet järjestyksessä.
    return voronoi_diagrammi
