szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']
a_betus_szavak=0


for a_betu in szavak:
    if a_betu[0] == "A" or a_betu[0] == "a":
        a_betus_szavak += 1
        print(a_betu)
print("Ennyi a vagy A betűvel kezdődő szó van a listában: ", a_betus_szavak)