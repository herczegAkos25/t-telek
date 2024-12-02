megadott_szo=[]

while True:
    szavak=input("Adj meg egy szót: ")
    if szavak == "":
        break
    megadott_szo.append(szavak)
    
    
    legrovidebb_szo = megadott_szo[0]
    leghosszabb_szo = megadott_szo[0]

    for szavak in megadott_szo:    
        if len(szavak) < len(legrovidebb_szo):
            legrovidebb_szo = szavak
        if len(szavak) > len(leghosszabb_szo):
            leghosszabb_szo = szavak
        
print(szavak)
print("Legrövidebb szó: ", legrovidebb_szo)
print("Leghosszabb szó: ", leghosszabb_szo)


