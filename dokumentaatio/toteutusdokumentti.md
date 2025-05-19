# Yleisrakenne
Tällä ohjelmalla voidaan muodostaa proseduraalisia karttoja. Aluksi ohjelma sijoittaa n määrän pisteitä satunnaisesti koordinaatein x,y. Pisteitä yhdistämällä muodostetaan Delaunay triangulaatio Bowyer-Watson algoritmilla. Syntyvä triangulaatio muutetaan sen duaalisuuden ansiosta Voronoi-diagrammiksi, etsimällä kunkin kolmion kärjen ympärillä olevat kehäympyröiden keskipisteet, jotka yhdistetään monikulmioiksi.

Lisäksi ohjelmma toteutettaa Perlin-kohinan satunnaisesta permutaatiotaulusta. Tästä saadaan jokaiselle yllämainitulle kolmion kärjelle oma kohina-arvo. Kohina on sulavaa, joten arvot muuttuvat lähekkäin tasaisesti. Nämä arvot väritetään, jolloin saadaan realistista maaston vaihtelua.

# Saavutetut aika- ja tilavaativuudet
Bowyer-Watson algoritmi toimii pseudokoodin mukaisesti O(n^2). Perlin-kohina taas (2^d), missä d=2.

# Puutteet ja parannusehdotukset
Bowyer-Watson algoritmi vaatisi optimointia. Useampi piste hidastaa ohjelmaa paljon, sekä esimerkiksi 5000 pistettä saattaa kaataa koko ohjelman. Lisäksi käyttöliittymään voisi lisätä tietyille parametreille säätöpainikkeet, jolloin ohjelmaa ajaessa voisi vaikuttaa esimerkiksi pisteiden määrään sekä syntyvään kuvioon/värikarttaan.

# Laajojen kielimallien käyttö.
Tässä työssä on käytetty ChatGPT:tä (o1, o3-mini sekä 4o) aiheiden selittämisessä sekä artikkelien suomentamisessa. 

# Lähteet
- https://en.wikipedia.org/wiki/Delaunay_triangulation
- https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm
- https://en.wikipedia.org/wiki/Perlin_noise
- http://www-cs-students.stanford.edu/~amitp/game-programming/polygon-map-generation/
- https://www.redblobgames.com/maps/terrain-from-noise/
- https://stackoverflow.com/questions/85275 
- https://stackoverflow.com/questions/85275/how-do-i-derive-a-voronoi-diagram-given-its-point-set-and-its-delaunay-triangula
- https://www.baeldung.com/cs/sort-points-clockwise
- https://www.pygame.org/docs/
- https://bit-101.com/blog/posts/2024-02-11/supertriangle/
- https://en.wikipedia.org/wiki/Circumcircle#Circumcenter_coordinates
- https://rtouti.github.io/graphics/perlin-noise-algorithm
