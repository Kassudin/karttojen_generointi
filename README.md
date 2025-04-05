# Karttojen generointi
[![codecov](https://codecov.io/gh/Kassudin/karttojen_generointi/branch/main/graph/badge.svg)](https://app.codecov.io/gh/Kassudin/karttojen_generointi)

# Dokumentaatio
[määrittelydokumentti](https://github.com/Kassudin/karttojen_generointi/blob/main/dokumentaatio/m%C3%A4%C3%A4rittelydokumentti.md)

[testausdokumentti](https://github.com/Kassudin/karttojen_generointi/blob/main/dokumentaatio/testausdokumentti.md)

# Viikkoraportit
[viikko 1](https://github.com/Kassudin/karttojen_generointi/blob/main/dokumentaatio/viikkoraportit/viikko1.md)

[viikko 2](https://github.com/Kassudin/karttojen_generointi/blob/main/dokumentaatio/viikkoraportit/viikko2.md)

[viikko 3](https://github.com/Kassudin/karttojen_generointi/blob/main/dokumentaatio/viikkoraportit/viikko3.md)

# Käynnistysohjeet (Linux ympäristö)

- Kloonaa projekti tai lataa zip-pakattu projekti:
  ```
  git clone git@github.com:Kassudin/karttojen_generointi.git
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
