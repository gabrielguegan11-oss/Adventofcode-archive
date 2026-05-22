file = open("input.txt", "r").read()
tab = file.splitlines()

table_finale=[]
total=0

for lignes in tab:
    ligne=[int(ch) for ch in lignes]
    print(ligne)
    maxi=-1
    for i in range(len(ligne)):
        for j in range(i+1, len(ligne)):
            nombre = int(str(ligne[i]) + str(ligne[j]))
            if nombre > maxi:
                maxi=nombre
    
    table_finale.append(maxi)
    total+=maxi

print(table_finale)
print(total)