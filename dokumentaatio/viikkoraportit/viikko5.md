# Viikko 5

Viidennellä viikolla toteutin Perlin-kohina algoritmin.

Ohjelmalla voidaan nyt muodostaa satunnaista kohinaa (perlin.py). Tämän avuksi on määritelty funktiot "gradientti" (grad), "sulautus" (fade) ja lineaarinen interpolointi (lerp). Näitä tarvitaan, jotta saadan toteutettua halutunlainen kohina https://adrianb.io/2014/08/09/perlinnoise.html.

Tällä viikolla opin, miten tuotetaan Perlin-kohinaa ja mitä matematiikkaa tarvitaan sen tuottamiseksi. Lisäksi tutustuin erilaisiin algoritmeihin, joilla voidaan tuottaa kohinaa.

Hankaluuksia tuotti Perlin-kohinan ymmärtäminen ja tuottaminen. Vaadittavat funktiot oli helppo toteutta, mutta niiden käyttäminen tuotti hankaluuksia (erityisesti vektorien muodostus). Lisäksi oli hankalaa tarkastaa, toimiiko ohelma, ilman visuaalista tulosta. Pygamella ei ole mielekästä piirtää kohinaa.

Ensi viikolla yhdistän Voronoi-soluihin Perlin-kohinan tuottamia arvoja (generaattori.py). Lisäksi parantelen ja lisäilen testejä.

Työhön käytetty aika: 15h
