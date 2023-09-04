chislo = int(input('Введите число: '))
strk=input('Введите строку: ')
mass=[]
for i in range(0,chislo):
    if i%2 == 0:
        i=strk
        mass.append(strk)
    else:
        mass.append(i)
print(mass)