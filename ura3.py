"""
# spremenljivke
# številske spremenljivke
starost = 30 # int
pi = 3.14 # float

# nizi znakov - string
ime = "Luka"

# boolean vrednost (True/False  1/0 )
resnica = True


# seznami altgr +f / list

imena = ["Luka", "Bine", "Cene"]
itm = [[60, 160], [80, 180]]
#print(starost[0])
#print(starost[-1])

# zanke - for
#izračunaj povprečno starost
starost = [22, 12, 66, 54, 18]
sest_let = 0
n = 0
for s in starost:
    #sest_let = sest_let + s
    sest_let += s
    #n = n + 1
    n += 1

print(sest_let / n)
print(sum(starost) / len(starost))

# seštej števila od 0 - 1000
# range()
#print(list(range(101)))
# pastebin.com/M7A4B6MX

sest = 0
for i in range(1001):
    sest += i
    # sest = sest + i
print(sest)

# zmnoži (*) števila od 0 - 1000
zmnoz = 1
for i in range(1, 1001):
    zmnoz *= i
    # sest = sest + i
print(zmnoz)
"""

# funkcije
# def ime_funkcije(par1, par2):

def sestej(a, b):
    return a + b

#sestej(8, 19)
#sestej(81, 19)

s = sestej(20, 30)
print(s + 10)

# pogoji/vejitve ali if stavki

# funkcija, ki prejme parameter n
# in vrne 0, če je n negativen
# in vrne 1, če je n pozitiven

def predznak(n):
    if n < 0:
        return 0
    else:
        return 1

print(predznak(10)) # 1
print(predznak(-10)) # 0