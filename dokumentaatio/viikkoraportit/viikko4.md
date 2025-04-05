#Viikko 4

Neljännellä viikolla toteutin Voronoi-diagrammin luovan ohjelmiston loppuun. Sovellus on siis nyt saatu siihen pisteeseen, että kartan pohja on proseduraalisesti tuotettavissa.

Ohjelmalla voidaan nyt muuntaa Deluanay triangulaatio Voronoi-diagrammiksi. Lisäksi Voronoi-diagrammista muodostuvat monikulmiot voidaan värittää pygamen avulla. Tämän avulla voidaan luoda proseduraalinen kartta, joka sisältää vettä ja maata.

Tällä viikolla opin lisää Voronoi-diagrammeista. Lisäksi opin, miten lasketaan radiaani keskipisteen ja monikulmion kulman välillä ja miten tätä hyödynnetään, jotta voidaan järjestää kulmat myötäpäivään https://www.baeldung.com/cs/sort-points-clockwise. 

Hankaluuksia tuotti pygamea ajatellen oikeanlaisen Voronoi-diagrammin muodostaminen. Alkuperäinen suunnitelma yhdistää kolmion reunan jakavat pisteet oli kyllä visuaalisesti toimiva ratkaisu, mutta tällöin monikulmiot syntyivät vain visuaalisesti (monikulmiolla ei ollut kulmia eli pygame ei voinut värittää monikulmioiden sisälle syntyvää alaa). Ohjelmaa piti muokata siten, että voronoi funktio palauttaa kärkien ympärille syntyvien kehäympyröiden keskipisteiden koordinaatit, jotta ne voidaan yhdistää. Tästä muodostui uusi ongelma, sillä pisteet piti vielä järjestää jotenkin, jotta pygame piirtäisi ne oikein (ilman järjestystä kuvio hajoili pahasti).  

Ensi viikolla aloitan satunnaisen kohinan luomisen. Lisäksi täydennän testejä.

Työhön käytetty aika: 19h