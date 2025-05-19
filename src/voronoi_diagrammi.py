import math
from bowyer_watson import kehaympyran_keskipiste


def kulma_suhteessa_pisteeseen(kolmionkärki, piste): 
    # atan2 palauttaa kulman radiaaneina kahden pisteen välillä.
    # Lasketaan kulma kolmion kärjen ja pisteen välillä.
    # https://stackoverflow.com/questions/42258637/how-to-know-the-angle-between-two-vectors
    return math.atan2(piste[1]-kolmionkärki[1], piste[0]-kolmionkärki[0])
    # Tämän avulla voimme järjestää myöhemmin kolmion kärjen ympärillä olevat kehäympyrän keskipisteet järjestykseen.

def voronoi(deluaunay):
    # https://stackoverflow.com/questions/85275/how-do-i-derive-a-voronoi-diagram-given-its-point-set-and-its-delaunay-triangula.
    # Jotta voimme piirtää ja värittää pygamella voronoin monikulmiot, meidän pitää määritellä monikulmioiden kaikki pisteet.
    # Tarvitsemme deluaunay kolmion kärkipisteen. Voronoi-diagrammissa kärkeä ympäröivät kehäympyröiden keskipisteet muodostavat monikulmion.
    # Eli lasketaan niiden kolmioioden kehäympyröiden keskipisteet, jotka jakavat pisteen yhtenä kolmion kärkenä.
    # Nämä lasketut kehäympyrän keskipisteet muodostavat monikulmion kolmion kärjen A ympärille.
    karki_pisteena = {}
    for kolmio in deluaunay:
        for piste in (kolmio.A, kolmio.B, kolmio.C):
            if piste not in karki_pisteena:
                karki_pisteena[piste] = []
            karki_pisteena[piste].append(kolmio)
    # Nyt meillä on sanakirja pisteistä, joiden arvoina on kolmiot johon piste kuuluu.
    voronoi_diagrammi = {} # Avaimena kolmion kärki (piste).
    # Arvona niiden kolmioiden kehäympyröiden keskipisteet, jotka jakavat tämän kärjen.
    for piste, kolmiot in karki_pisteena.items():
        kehaympyran_keskipisteet = []
        for kolmio in kolmiot: # Pisteen jakamat kolmiot.
            keskipiste = kehaympyran_keskipiste(kolmio.A, kolmio.B, kolmio.C)
            if keskipiste is not None: 
                kehaympyran_keskipisteet.append(keskipiste)
        # Kehäympyröiden keskipisteet on nyt listassa, mutta ei järjestyksessä.
        # Tämä on ongelma, sillä jos jätämme nämä tällä tavalla, niin monikulmiota ei synny.

        def kulmat(kehaympyran_keskipiste): # Apufunktio.
            return kulma_suhteessa_pisteeseen(piste, kehaympyran_keskipiste) # Lasketaan radiaanit kaikille kehäympyröiden keskipisteille.
        
        kehaympyran_keskipisteet.sort(key=kulmat) # Järjestetään nousevaan järjestyksen.
        # Tätä voi ajatella yksikköympyränä, jossa kolmion kärki (keskipiste) on origossa.
        voronoi_diagrammi[piste] = kehaympyran_keskipisteet 
        # Nyt sanakirja sisältää kärjen ja sen ympärillä olevat kehäympyröiden keskipisteet järjestyksessä.
    return voronoi_diagrammi
