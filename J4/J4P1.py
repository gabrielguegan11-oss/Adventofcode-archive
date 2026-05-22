file=open("input.txt", "r").read()
tab=file.splitlines()

tab_temp=[]
for lignes in tab:
    ligne=[str(ch) for ch in lignes]
    tab_temp.append(ligne)

tab=tab_temp

accessible = 0

for i in range(len(tab)):
    for j in range(len(tab[0])):
        if tab[i][j] == '@':
            voisins=0

            if i-1 >= 0 and tab[i-1][j]== '@':
                voisins+=1

            if i+1 < len(tab[0]) and tab[i+1][j]== '@':
                voisins+=1

            if j-1 >= 0 and tab[i][j-1]== '@':
                voisins+=1

            if j+1 < len(tab) and tab[i][j+1]== '@':
                voisins+=1
                
            if i-1 >= 0 and j-1 >= 0 and tab[i-1][j-1]== '@':
                voisins+=1
            if i-1 >= 0 and j+1 < len(tab) and tab[i-1][j+1]== '@':
                voisins+=1
            if i+1 < len(tab) and j-1 >= 0 and tab[i+1][j-1]== '@':
                voisins+=1
            if i+1 < len(tab) and j+1 < len(tab) and tab[i+1][j+1]== '@':
                voisins+=1

            if voisins < 4:
                accessible+=1

print(accessible)