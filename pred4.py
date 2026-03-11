# predavanje 4
# stringi

ime = "Andrej Brtoncelj"
# upper
print(ime.upper())
# lower
print(ime.lower())
# strip
print(ime.strip())
# split
print(ime.split())
spl = ime.split()
print(spl[0])
print(spl[1])

# slicanje stringov
ime = "Andrej Brtoncelj"
#print(ime[0])
#ime = ['A', 'n', 'd', 'r', 'e', 'j', ' ', 'B', 'r', 't', 'o', 'n', 'c', 'e', 'l', 'j']
print(ime[0])
print(ime[-1])
print(ime[:9])
print(ime[0:9:3])
print(ime[::-1])
spl = ime.split()
print(spl)
print(spl[1][0])

#f- string
ime = "Boštjan"
pri = "Lončar"
# Moje ime je Luka in pišem se Cola
print(f"Moje ime je {ime}. in pišem se {pri}.")