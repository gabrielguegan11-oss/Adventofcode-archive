file = open("input.txt", "r").read()
tab0 = file.splitlines()
tab=[]

total=0

for val in tab0:
    tab.append(int(val))

indexprev=0
indexcurr=1

for i in range(len(tab)-1):
    prev = tab[indexprev]
    current=tab[indexcurr]

    if current>prev:
        total+=1

    indexcurr+=1
    indexprev+=1
    
print(total)