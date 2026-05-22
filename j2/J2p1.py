file=open("input.txt", "r").read()
tab= file.split(',')

invalid=[]

for i in range(len(tab)):
    indice=tab[i].split('-')
    for j in range(int(indice[0]), int(indice[1])):
        liste=[int(c) for c in str(j)]
        listep1=liste[:len(liste)//2]
        listep2=liste[len(liste)//2:]
        if listep1==listep2:
            result = int("".join(map(str, liste)))
            invalid.append(result)


print(sum(invalid))