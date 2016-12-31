import math
import random

def moon():
#####################################################################
##  DEFINISANJE PARAMETARA
#####################################################################
    masa_projektila = 1000 #kg
    poluprecnik_projektila = 1 #m
    pocetna_sila = 4*10**6 #N
    vreme = 30 #s
    #pocetna sila deluje na projektil 30 s
    orbita_meseca = 384405000 #m (to je zapravo udaljenost od zemlje)
    poluprecnik_zemlje = 6378000 #m
    masa_zemlje = random.gauss(6*10**24, 0.1) #kg
    poluprecnik_meseca = 1738000 #m
    masa_meseca = random.gauss(7.3*10**22,0.1) #kg
   
    #da li da napisemo u posebnoj funkciji izracunavanje sile otpora vazduha?
    # u random.gauss prvi parametar je srednja vrednost a drugi standardna devijacija. Ubacila sam standardnu devijaciju
    # u procentima, nisam sigurna da li je to dobro.
    
    C_d = 0.5 #drag coefficient za sferu
    povrsina_projektila = 4 * poluprecnik_projektila**2 * math.pi
    alfa1 = random.uniform(2, 2.5)#uniformna raspodela od 2 do 2.5
    alfa = random.gauss(alfa1, 0.1)
    ro = 1
    if visina >= 0 and visina < 5000:
        ro = random.gauss(1.22500, 0.1) #kg/m^3
    elif visina >= 5000 and visina < 10000:
        ro = random.gauss(0.736116, 0.1) #kg/m^3
    elif visina >= 10000 and visina < 15000:
        ro = random.gauss(0.412707, 0.1) #kg/m^3
    elif visina >= 15000 and visina < 20000:
        ro = random.gauss(0.193674, 0.1) #kg/m^3
    elif visina >= 20000 and visina < 25000:
        ro = random.gauss(0.0880349, 0.1) #kg/m^3
    elif visina >= 25000 and visina < 30000:
        ro = random.gauss(0.0394658, 0.1) #kg/m^3
    elif visina >= 30000 and visina < 35000:
        ro = random.gauss(0.0180119, 0.1) #kg/m^3
    elif visina >= 35000 and visina < 40000:
        ro = random.gauss(0.00821392, 0.1) #kg/m^3
    elif visina >= 40000 and visina < 45000:
        ro = random.gauss(0.00385101, 0.1) #kg/m^3
    elif visina >= 45000 and visina < 50000:
        ro = random.gauss(0.00188129, 0.1) #kg/m^3
    elif visina = 50000:
        ro = random.gauss(0.0009777525, 0.1)
    else:
        ro = 1
    # brzina_projektila = ?
    # visina = ?

    # treba jos ubaciti i uncertainty oko pozicije meseca u trenutku ispaljivanja
    F_otpora = 1/2 * ro * brzina_projektila**alfa * C_d * povrsina_projektila
    
#####################################################################
##  RACUNANJE SILA KOJE DELUJU NA SISTEM
#####################################################################
    
