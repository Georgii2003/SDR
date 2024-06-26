# Алгоритм для нахождения наибольшего общего делителя (НОД) двух чисел

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
print("Наибольший общий делитель чисел", num1, "и", num2, "равен", gcd(num1, num2))