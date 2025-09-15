"""
# komentar
# spremenljivke

# int (Integer) - celo število
# spremenljivka - ime = vrednost
# Starost Človeka
#StarostČloveka = 15
#camel case
starostCloveka = 30
#snake case
starost_cloveka = 30

# string - niz znakov
# "" = shift + 2
ime = "Luka7887@@@"

# float - decimalna števila
pi = 3.14

# boolean - logične vrednosti
# True ali False

pridenDijak = True


# print() - funkcija
print("Brina")
print(starost_cloveka)



# izračun površine sobe
sirina = 6
dolzina = 8

povrsina = dolzina * sirina # * = množenje
print(povrsina)


# pretvorba tipov spremenljivk

x = "22"
# type()
print(type(x))

# parsing
xInt = int(x)  # int(string)
print(type(xInt))

# input("Koliko si star?")
"""
# površina sobe
# inputi programa
sirina = input("Širina tvoje sobe?")
dolzina = input("Dolžina tvoje sobe?")

sInt = int(sirina)
dInt = int(dolzina)

print(sInt * dInt) 

# vprašajte uporabnika po širini in dolžini sobe
# izračunajte obseg sobe


sirina = input("Širina tvoje sobe?")
dolzina = input("Dolžina tvoje sobe?")

sInt = int(sirina)
dInt = int(dolzina)
print((2 * sInt)  + (2 * dInt)) 


# Program vpraša po številu kepic sladoleda
# in po ceni kepice
# Izračunaj ceno na računu

kepica = int(input("Koliko kepic želiš?"))
cena = int(input("Cena ene kepice?"))

print(kepica * cena)



# Program vpraša po trenutni uri in minuti
# Program vrne koliko sekund je minilo od polnoči (24 urni čas)

#https://github.com/Pfyber/uvodVPython