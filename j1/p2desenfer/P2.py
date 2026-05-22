file=open("input.txt").read()
tab=file.splitlines()

cp_f=0

def tourner(valeur, ajout):
    cp = 0
    if ajout > 0:
        for i in range(ajout):
            valeur+=1
            if valeur==100:
                valeur=0
            if valeur==0:
                cp+=1
    if ajout < 0:
        for i in range(ajout*-1):
            valeur-=1
            if valeur==-1:
                valeur=99 
            if valeur==0:
                cp+=1
    
    return valeur, cp

rotation=50

for i in range(len(tab)):
    nombre=int(tab[i][1:])
    orientation=tab[i][:1]
    if orientation=="L":
        nombre=nombre*-1
    rotation=tourner(rotation,nombre)
    print(rotation)
    cp_f+=rotation[1]
    rotation=rotation[0]

print(cp_f)
