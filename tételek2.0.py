szamok=[]
összesen=0

while True:  
    szam=int(input("Adj meg egy számot! "))  
    if szam >= -5 and szam <= 5:
        szamok.append(szam)
        összesen+=szam
    else:
        break        

print("A megadott számok [-5;5] intervallumban: ", szamok)
print("A megadott számok öszzege: ", összesen)