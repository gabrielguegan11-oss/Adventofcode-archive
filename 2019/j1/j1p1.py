file = open("input.txt", "r").read()
tab0 = file.splitlines()
tab=[]

for val in tab0:
    tab.append(int(val))

total=0

for val in tab:
    result=val // 3
    result -=2
    total+=result

print(total)