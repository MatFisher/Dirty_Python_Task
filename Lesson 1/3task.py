from decimal import Decimal

num = Decimal(input('enter any num : '))
digits = num.as_tuple().digits
print(sum(digits))


