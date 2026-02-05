# seznami
stevila = [1, 2, 3, 4, 5, 6, 7, 8]
# zmnožek vseh števil
sum = 1
for s in stevila:
    sum = sum * s
    print(sum)

# iz seznama izpiši negativna števila

# preštej negativna in preštej pozitivna števila
st = [1, -10, 20, 30, 20, -20, 30]

neg = 0
poz = 0

for s in st:
    if s > 0:
        poz = poz + 1
    else:
        neg = neg + 1
print(poz, neg)


sez = [1, 0, 1, 0, 1, 0, 1, 1, 1]
# preštej kolikokrat se ponovi 1

en = 0
for s in sez:
    if s == 1:
        en = en +1
print(en)

# seštej vsa negativna števila


