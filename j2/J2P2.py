file = open("input.txt", "r").read()
tab = file.split(',')

invalid = []

def est_invalide(num):
    for i in range(1, len(num)//3):
        if len(num)%i==0:
            motif=num[:i]
            if motif * (len(num)//i)==num:
                return True
    return False

for i in range(len(tab)):
    indice = tab[i].split('-')
    for j in range(int(indice[0]), int(indice[1])+1):
        num=str(j)
        if est_invalide(num):
            invalid.append(j)

print(sum(invalid)) 