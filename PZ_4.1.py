# Дано целое число N (>0).Если оно является степенью числа 3, то вывести True, если не является - вывести False.

a = int(input("Введите целое число"))
while a % 3 == 0:
    a = a // 3
if a == 1:
    print("True")
else:
    print("False")
