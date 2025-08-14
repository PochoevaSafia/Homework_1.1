import math
a = 5
b = 3
c = (-26)
D = b**2 - 4*a*c
print(D)
x1 =(-b + math.sqrt(D))/(2*a)
x2 =(-b - math.sqrt(D))/(2*a)
print(x1, x2)

a = 10
b = 3
c = 7
D = b**2 - 4*a*c
print(D)
if D > 0:
   x1 =(-b + math.sqrt(D))/(2*a)
   x2 =(-b - math.sqrt(D))/(2*a)
   print(x1, x2)
elif D == 0:
     x1 =(-b)/(2*a)
else:
   print ('Дискриминант не имеет корня!')



