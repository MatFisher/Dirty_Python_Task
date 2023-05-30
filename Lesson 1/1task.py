# На вход подается число с плавающей точкой, выведите первую цифру дробной части

import math

a = float(input("Enter number: "))
print(math.trunc(a*10%10))

