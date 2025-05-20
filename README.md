# Karttojen generointi
[![codecov](https://codecov.io/gh/Kassudin/karttojen_generointi/branch/main/graph/badge.svg)](https://app.codecov.io/gh/Kassudin/karttojen_generointi)

Proseduraalisten kaksiulotteisten karttojen luomiseen soveltuva ohjelma.

![Delaunay+Voronoi](Delaunay+Voronoi.png)
![kartta](kartta.png)

# Dokumentaatio
[määrittelydokumentti](https://github.com/Kassudin/karttojen_generointi/blob/main/dokumentaatio/m%C3%A4%C3%A4rittelydokumentti.md)

[testausdokumentti](https://github.com/Kassudin/karttojen_generointi/blob/main/dokumentaatio/testausdokumentti.md)

[toteutusdokumentti](https://github.com/Kassudin/karttojen_generointi/blob/main/dokumentaatio/toteutusdokumentti.md)

# Viikkoraportit
[viikko 1](https://github.com/Kassudin/karttojen_generointi/blob/main/dokumentaatio/viikkoraportit/viikko1.md)

[viikko 2](https://github.com/Kassudin/karttojen_generointi/blob/main/dokumentaatio/viikkoraportit/viikko2.md)

[viikko 3](https://github.com/Kassudin/karttojen_generointi/blob/main/dokumentaatio/viikkoraportit/viikko3.md)

[viikko 4](https://github.com/Kassudin/karttojen_generointi/blob/main/dokumentaatio/viikkoraportit/viikko4.md)

[viikko 5](https://github.com/Kassudin/karttojen_generointi/blob/main/dokumentaatio/viikkoraportit/viikko5.md)

[viikko 6](https://github.com/Kassudin/karttojen_generointi/blob/main/dokumentaatio/viikkoraportit/viikko6.md)

# Ohje käyttöönottoon ja ohjelman suorittamiseen (Linux ympäristö)

- Kloonaa projekti tai lataa zip-pakattu projekti:
  ```
  git clone git@github.com:Kassudin/karttojen_generointi.git
  ```
- Siirry juurihakemistoon 
  ```
  cd karttojen_generointi
  ```
  
- Lataa tarvittavat riippuuvuudet:
  ```
  poetry install
  ```
- Aktivoi virtuaaliympäristö:
   ```
  poetry shell
   ```
- Luo proseduraalinen kartta (pygame):
   ```
  python3 src/generaattori.py
   ```
- Yksikkötestit:
   ```
  coverage run --branch -m pytest src
   ```
