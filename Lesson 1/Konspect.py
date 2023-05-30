print("Hello World")

numb_1 = 1
numb_2 = "1"
numb_3 = 0.1
numb_4 = True

print(type(numb_1))
print(type(numb_2))
print(type(numb_3))
print(type(numb_4))

number_1 = 10
number_2 = 5

print (number_1 + number_2)
print (number_1 - number_2)
print (number_1 * number_2)
print (number_1 / number_2)
print (number_1 // number_2) #Целочисленное деление
print (number_1 % number_2) #Деление с остатком
print (number_1 ** number_2) #Возведение в степень
print (number_1 == number_2)

from decimal import Decimal

a = Decimal('0.56')
print(a)
print (a*100)

# Основные методы для работы со строками

text = "iaue 443 rhgi 2345 p ao eф4456hn"
print(f"Исходный текст: {text}")
print(text.split())   # Разделяет строку на список. В скобках вставляется разделительный символ (пробел по ум.)
print(text.replace())  # замена символов в строке. Первым вводим что менять, вторым - на что менять
print(text.isdigit()) # проверяет, является ли строка числом
print(text.isalpha()) # проверяет, только ли буквы в строке
print(text.lower())   # переводит всё в нижний регистр
print(text.upper())   # переводит всё в верхний регистр
print(text.title())   # делает первые буквы слов заглавными
print(text.capitalize())   # делает первые буквы предложений заглавными
print(text.index())   # выдать индекс элемента. Если ввести второе число - будет искать с указанной позиции
print(text.find())   # выдать индекс элемента. Если ввести второе число - будет искать с указанной позиции
print(text.count())   # число повторений элемента в строке
