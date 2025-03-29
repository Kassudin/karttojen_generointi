#Viikko 3

Kolmannella viikolla toteutin Bowyer-Watson algoritmin loppuun ja sen piirtämisen. Lisäksi aloitin Voronoi-diagrammiksi muuntavan funktion toteuttamisen

Ohjelmalla voidaan nyt muodostaa satunnaisista pisteistä delunay triangulaatio(n>=3). Lisäksi syntyvä kuvio voidaan visualisoida (pygame). Yksikkötestit kirjoitettu testaamaan palautuvien kolmioiden määrää eri tilanteissa. 

Tällä viikolla opin, miten Bowyer-Watson algoritmi totetutetaan. Lisäksi tutustuin logiikkaan, miten muunnetaan saatu triangulaatio Voronoi-diagrammiksi #https://stackoverflow.com/questions/85275/how-do-i-derive-a-voronoi-diagram-given-its-point-set-and-its-delaunay-triangula. 

Hankaluuksia tuotti algoritmin sopiva testaaminen. Tällä hetkellä testitapauksissa on n:n arvot, jotka eivät vastaa realisista suoritusta. Tarvitaan siis jokin tapa laskea kolmioiden määrä suurilla n:n määrillä (esim. n=500). Lisäksi nykyisessä koodissa on ongelmana, että harvoin satunnaisissa tapauksissa funktio kehäympyrän_keskipiste(A,B,C): yrittää jakaa nollalla, jolloin ohjelma kaatuu. Sitä suurempi n määrä, sitä useammin tämä tapahtuu.

Ensi viikolla toteutan Voronoi-diagrammin muodostavan funktion loppuun. Lisäksi aloitan Perlin-kohinaan tutustumisen. Korjaan myös kehäympyrän keskipisteen laskevan funktion toimimaan kaikissa tapauksissa ja parantelen yksikkötestejä.

Työhön käytetty aika: 15h

