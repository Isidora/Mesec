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
    alfa = random.gauss(alfa1, 0.1) #Zasto dva puta racunamo alpha?? Zar nije dovoljno da koristimo samo uniform razpodelu?

    # brzina_projektila = ?
    # visina = ?
    # treba jos ubaciti i uncertainty oko pozicije meseca u trenutku ispaljivanja

#Mozda da napisemo funkciju koja odvojeno odredjuje sile ovako?#
##########################FUNKCIJA ZA OTPOR########################
def silaOtpora(visina, C_d, poluprecnik_projektila, brzina projektila):
    '''Funkcija ce primiti visinu i brzinu projektila u svakom trenutku kao argumente, to cemo racunati u nekoj drugoj funkciji.
    Kod je isti kao ovo sto si ti napisala samo nisam siguran za ovo alfa dal treba uniform pa opet Gauss ili samo ovako??'''
    povrsina_projektila = 4 * poluprecnik_projektila**2 * math.pi
    alfa = random.uniform(2, 2.5)#uniformna raspodela od 2 do 2.5
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
    F_otpora = 1/2 * ro * brzina_projektila**alfa * C_d * povrsina_projektila
    return F_otpora

#########GRAVITACIONALNA SILA OD PLANETE I MESECA NA PROJEKTIL##########################

def distanca(Dict1, Dict2):
    '''Racuna daljinu izmedju dva Dicta za polazaj
    '''
    xDistance = (Dict1['xPoz'] - Dict2['xPoz']) 
    yDistance = (Dict1['yPoz'] - Dict2['yPoz'])  
    daljina = math.sqrt(xDistance**2 + yDistance**2)                    
    return daljina

def silaPlanete(gamma, masa_zemlje, masa_projektila, pozicija_zemlje, pozicija_projektila):
    '''Ako radimo u dve dimenzije, trebace nam polazaji i brzine (verovatno i sile) u x-y koordinatima, mislim da je najbolje 
    uraditi to u dict tipa {'xSila':broj, 'ySila': drugi broj}. Predpostavicu da cemo tako raditi za sada ali mozemo izmeniti
    prozicija_zemlje onda moze biti dict {xPoz:broj, yPoz: drugi broj} i isto tako pozicija projektila
    Zamislimo ih kao vektore u 2-D prostoru - pozicija Zemlje ce biti (0, 0) a pozicija projektila njegov polazaj u tom sistemu
    '''
    daljina = distanca(pozicija_zemlje, pozicija_projektila)
    #Ovo je vektorska verzija onog zakona F =Gmm/r^2 
    xF_planete = gamma*masa_zemlje*masa_projektila*pozicija_projektila['xPoz']/daljina^3
    yF_planete = xF_planete = gamma*masa_zemlje*masa_projektila*pozicija_projektila['yPoz']/daljina^3
    return {'xSila':xF_planete, 'ySila':yF_planete}

#Istu foru uradimo za mesec. Jel se slazes sa ovom implementacijom u Diktu? i jel ti jasno kako racunamo silu u x-y koordinatima       
    
#####################################################################
##  RACUNANJE SILA KOJE DELUJU NA SISTEM
#####################################################################

gamma = 6.674*10**(-11) # N(m/kg)^2 - da li ovo treba nekako da korigujemo?
gravitaciona_sila = gamma * masa_zemlje * masa_meseca / orbita_meseca**2
    
