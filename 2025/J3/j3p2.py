file=open("input.txt", "r").read()
tab=file.splitlines()

table_finale=[]
total=0

for lignes in tab:
    ligne = [int(ch) for ch in lignes]
    resultat=[]
    debut=0
    for k in range(12):
        maxi=-1
        indice_max=debut
        reste = 12-k
        fin = len(ligne) - reste
        for i in range(debut, fin+1):
            if ligne[i] > maxi:
                maxi = ligne[i]
                indice_max=i
        resultat.append(maxi)
        debut=indice_max+1
    nombre = int("".join(str(x) for x in resultat))
    table_finale.append(nombre)
    total+=nombre

print(table_finale)
print(total)
