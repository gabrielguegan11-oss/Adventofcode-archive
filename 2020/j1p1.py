file = open("input.txt", "r").read()
tab0 = file.splitlines()

tab = []
for val in tab0:
    tab.append(int(val))


for i in range(len(tab)):
    for j in range(len(tab)):
        for d in range(len(tab)):

            if tab[i]+tab[j]+tab[d]==2020:
                print(tab[i],tab[j],tab[d], tab[i]*tab[j]*tab[d])