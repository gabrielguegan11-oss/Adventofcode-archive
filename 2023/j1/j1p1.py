file=open("input.txt").read()
tab0=file.splitlines()

nbs=['0','1','2','3','4','5','6','7','8','9']

tab2=[]
for i in range(len(tab0)):
    char=''
    for val in tab0[i]:
        if val in nbs:
            char=char+val
    tab2.append(char)

somme = 0

for char in tab2:
    val = int(char[0] + char[-1])
    somme += val

print(somme)
