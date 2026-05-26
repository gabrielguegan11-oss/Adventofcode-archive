file=open("input.txt", "r").read()
tab=file.splitlines()

tab_intervalles=[]
tab_id=[]
cp=0

for valeur in tab:
    if '-'  in valeur:
        valeurs=valeur.split('-')
        valeur1=int(valeurs[0])
        valeur2=int(valeurs[1])
        tab_intervalles.append([valeur1, valeur2])
    elif valeur != "":
        tab_id.append(int(valeur))

for id in tab_id:
    for intervale in tab_intervalles:
        if id >= intervale[0] and id <= intervale[1]: #est dans l'intervalle
            cp+=1
            break

print(cp)