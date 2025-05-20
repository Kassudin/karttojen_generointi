import random

#https://en.wikipedia.org/wiki/Perlin_noise
#https://rtouti.github.io/graphics/perlin-noise-algorithm
#https://mrl.cs.nyu.edu/~perlin/noise/

# Tässä tiedostossa implementoidaan paranneltu Perlin-kohinan toteuttava algoritmi seuraten ylläolevia linkkejä.
# Tämä toteutus on kaksiulotteinen.

# Luodaan permutaatiotaulukko, jotta saamme pseudosatunnaisia arvoja.
permutaatio = list(range(256))
random.shuffle(permutaatio)
p = permutaatio*2 # Kerrotaan kahdella, jotta kulmahashien laskennassa ei ylitetä listan pituutta.

# Määritellään aluksi funktiot kohinan tuottamiseksi.

def lineaarinen_interpolointi(a,b,t): # Interpolaatio #https://en.wikipedia.org/wiki/Linear_interpolation.
    return a+t*(b-a)

def sulautus(t): # https://en.wikipedia.org/wiki/Smoothstep
    # Jotta interpolointi olisi sujuva.
    return t ** 3 * (t * (t * 6 - 15) + 10)

def gradientti(hash_arvo, x, y): 
    # "For a point in a two-dimensional grid,
    # this will require the computation of four offset vectors and dot products"
    # https://en.wikipedia.org/wiki/Perlin_noise
    # neljä eri suuntaa
    h = hash_arvo % 4  # Koska kaksiulotteinen, tarvitsemme vain tapaukset h={0,1,2,3}.
    # Nyt h saa aina arvon 0,1,2,3.
    if h == 0:
        return x + y
    if h == 1:
        return -x + y
    if h == 2:
        return x - y
    return -x - y

def kohina_2d(x, y): # Kaksiulotteinen xy.
    # x = ⌊x⌋+xf
    # Ruudun indeksit.
    xi = int(x) & 255  #⌊x⌋
    yi = int(y) & 255
    # Murto-osat.
    x_murto = x - int(x) #xf
    y_murto = y - int(y)
    # Nyt indeksit ovat välillä 0-255.
    # Sulautetaan murto-osat myöhempää varten.
    x_smooth = sulautus(x_murto)
    y_smooth = sulautus(y_murto)

    # Kulmahashit valitaan permutaatio-taulukosta.
    # Jokainen kulmapiste saa siis hash-arvon.
    # (0,0) = (xi,yi), (1,0) = (xi+1,yi), (0,1) = (xi,yi+1), (1,1) = (xi+1,yi+1).
    vasen_ala = p[p[xi] + yi]
    vasen_yla = p[p[xi] + yi+1]
    oikea_ala = p[p[xi+1] + yi]
    oikea_yla = p[p[xi+1] + yi+1]
 
    # Ylläolevista kulmahasheista valitaan gradientin suunta (neljä suuntaa).
    # Eli muodostetaan gradienttivektorit.
    # xf = x - ⌊x⌋
    # v_00 = (xf,yf),  v_10 = (xf-1,yf), v_01 = (xf,yf-1), v_11 = (xf-1,yf-1).
    grad_vasen_ala = gradientti(vasen_ala, x_murto, y_murto)
    grad_vasen_yla = gradientti(vasen_yla, x_murto, y_murto-1)
    grad_oikea_ala = gradientti(oikea_ala, x_murto-1, y_murto)
    grad_oikea_yla = gradientti(oikea_yla, x_murto-1, y_murto-1) 
   
    # Interpoloidaan ensiksi x-suunnassa.
    x1 = lineaarinen_interpolointi(grad_vasen_ala, grad_oikea_ala, x_smooth)
    x2 = lineaarinen_interpolointi(grad_vasen_yla, grad_oikea_yla, x_smooth)
    # Nyt meillä on alareunan ja yläreunan arvot.
    # Lopuksi interpoloidaan näiden arvojen väliltä y-suunnassa.
    return lineaarinen_interpolointi(x1, x2, y_smooth)
    