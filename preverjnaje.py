"""
Napiši program, ki:
1. Ustvari seznam besed: besede = ["jabolko", "banana", "češnja", "dinja", "figa"]
2. S for zanko pregleduje vsako besedo
3. Izpiše samo tiste besede, ki imajo več kot 5 črk
4. Na koncu izpiše: Dolgih besed: [število]


besede = ["jabolko", "banana", "banana", "banana", "figa"]

st = 0
for b in besede:
    if len(b) == "banana":
        st += 1 # st = st +1
        #print(b)
print(st)



Ustvari seznam: temperature = [22, 35, 18, 41, 29, 12, 38, 25]
2. S for zanko pregleda vse temperature
3. Šteje vroče (≥30°C) in hladne dni (<30°C)
4. Poišče najvišjo temperaturo
5. Izpiše

temperature = [22, 35, 18, 41, 29, 12, 38, 25]

vroce = 0
hladne = 0
maksimalno = -9999999999
for t in temperature:
    if t >= 30:
        vroce += 1
    else:
        hladne += 1

    if t > maksimalno:
        maksimalno = t

print(vroce, hladne, maksimalno)

 Ustvari seznam: stevilke = [3, 7, 2, 8, 4, 6, 1, 9, 5]
2. S for zanko pregleda vsa števila
3. Sešteje posebej soda in posebej liha števila
4. Prešteje, koliko je sodih in koliko lihih
5. Izpiše:



stevilke = [3, 7, 2, 8, 4, 6, 1, 9, 5]

vs_sodih = 0
vs_lihih = 0
ses_sodih = 0
ses_lihih = 0
for s in stevilke:
    if s % 2 == 0:
        vs_sodih += s
        ses_sodih += 1
    else:
        vs_lihih += s
        ses_lihih += 1

print(vs_sodih, vs_lihih, ses_lihih, ses_sodih)




Ustvari seznam: ocene = [8, 4, 9, 5, 7, 3, 10, 6]
2. S for zanko pregleda vse ocene
3. Šteje pozitivne (≥6) in negativne (<6) ocene
4. Izračuna povprečje vseh ocen
5. Poišče najboljšo oceno


"""
ocene = [8, 4, 9, 5, 7, 3, 10, 6]
poz = 0
neg = 0
sestevek = 0
st_elem = 0
max_ocena = 0

for o in ocene:
    sestevek += o
    st_elem += 1

    if o >= 6:
        poz += 1
    else:
        neg += 1

    if o > max_ocena:
        max_ocena = 0

poprecje = sestevek/st_elem
print(poz, neg, max_ocena, poprecje)