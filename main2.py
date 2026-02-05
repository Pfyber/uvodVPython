# spremenljivke

x = 10
ime = "Luka"

# izhode - print()

print(x)
print(x, ime)

# pogojne stavke - if stavki

if x > 10:
    print("ne bo mrzlo")
    print(" še neki ")
else:
    print("mrzlo je")

# seznami - list

# izračuna povprečno višino dijaka
# altgr + f
visine = [160, 170, 185, 167, 195, 210]
print(visine)
# izpiši prvo vrednost/element
print(visine[0])
print(visine[5])

# negativne indekse

print(visine[-1])


ime = "Aleksandar Pajić"
# ime = ["A", "l", "e",....]
print(ime[0])
print(ime[-1])

# izračunaj povprečno višino dijakov


# zanke 
print(list(range(10)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




visine = [160, 170, 185, 167, 195, 210]
vsota = 0
stevec = 0
for i in visine:
    #vsota = vsota + i
    vsota += i
    stevec += 1

print(vsota, stevec)
print(vsota / stevec)
print( vsota / len(visine))


# seštej števila od 1 - 1000000 (milijon)

vsota = 0
for i in range(1000001):
    vsota += i
print(vsota)