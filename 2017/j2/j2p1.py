file = open("input.txt", "r").read()
tab = file.splitlines()


tabfinal =[]
for val in tab:
    minitab= val.split("\t")
    tabfinal.append(minitab)

tabint=[]
for i in range(len(tabfinal)):
    minitabint=[]
    for j in range(len(minitab)):
        minitabint.append(int(tabfinal[i][j]))
    tabint.append(minitabint)

tabecart=[]
for i in range(len(tabint)):
    mini=tabint[i][0]
    maxi=tabint[i][0]
    for j in range(len(tabint[0])):
        
        if tabint[i][j]<mini:
            mini=tabint[i][j]
    for j in range(len(tabint[0])):
        
        if tabint[i][j]>maxi:
            maxi=tabint[i][j]
    ecart =[maxi,  mini]
    tabecart.append(ecart)

print(tabecart)
total =0

for i in range(len(tabecart)):
    ecart = tabecart[i][0]-tabecart[i][1]
    total+=ecart

print(total)

