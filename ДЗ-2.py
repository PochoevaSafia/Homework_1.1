import math
# a = 5
# b = 3
# c = (-26)
# D = b**2 - 4*a*c
# print(D)
# x1 =(-b + math.sqrt(D))/(2*a)
# x2 =(-b - math.sqrt(D))/(2*a)
# print(x1, x2)

a = int(input())
b = int(input())
c = int(input())
D = b**2 - 4*a*c
print(D)
if D > 0:
   x1 =(-b + math.sqrt(D))/(2*a)
   x2 =(-b - math.sqrt(D))/(2*a)
   print("Дискриминант имеет два корня:",x1, x2)
elif D == 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    print("Один корень:", x1)
else:
   print ('Дискриминант не имеет корня!')



