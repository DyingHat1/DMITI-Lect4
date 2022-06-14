from random import random

def Generator(p):
    if random() < p:
        return 0
    else:
        return 1
    
Mas1 = [10,10]
Mas2 = [10,10] 
p1 = Mas1[0]/(Mas1[0]+Mas1[1])
p2 = Mas2[1]/(Mas2[0]+Mas2[1])
arr = [[2, -3], [-1, 2]]
rez_array = [[0, 0] for i in range (0,100)]
Mx = 0
Mx2 = 0
a=b=0
s=0;
D=0
sko=0

for i in range (0,100):
    f = Generator(p1)
    g = Generator(p2)
    if f == 0 and g ==0:
        Mas1[0]+=2
    elif f == 1 and g == 1:
        Mas1[1]+=2
    elif f == 1 and g == 0:
        Mas2[0]+=1
    else:
        Mas2[1]+=3
    p1 = Mas1[0]/(Mas1[0]+Mas1[1])
    p2 = Mas2[1]/(Mas2[0]+Mas2[1])
for i in range(0, 100):
    rez_array[i][0] = Generator(p1)
    rez_array[i][1] = Generator(p2)

for i in range(0, 100):
    if rez_array[i][0] == rez_array[i][1]:
        a+=2
    elif arr[rez_array[i][0]][rez_array[i][1]] == -1:
        b+=1
    else:
        b+=3
    s+=(abs(arr[rez_array[i][0]][rez_array[i][1]])-(a-b)/100)**2

sko = (s/99)**0.5
Mx = 2*p1*p2 + 2*(1-p1)*(1-p2) + (-1)*p2*(1-p1) + (-3)*p1*(1-p2)
Mx2 = 4*p1*p2 + 4*(1-p1)*(1-p2) + 1*p2*(1-p1) + 9*p1*(1-p2)
D = Mx2 - Mx**2

print("Cчет игрока А:", a)
print("Cчет игрока В:", b)
print("Среднее значение A и В", a/100, b/100)
print("Мат ожидание", Mx)
print("Среднее квадратическое отклонение", sko)
print("Дисперсия", D)
print("Теоретическое среднее квадратичное отклонение", D**0.5)
