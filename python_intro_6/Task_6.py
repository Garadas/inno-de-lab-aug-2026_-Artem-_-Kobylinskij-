first = float(input("Введите первое число:"))
second = float(input("Введите второе число:"))
op = input("Введите символ операции (+, -, *, /): ")
if op == "+":
    print("Результат:", first, op, second, "=", first + second)
elif op == "-":
    print("Результат:", first, op, second, "=", first - second)
elif op == "*":
    print("Результат:", first, op, second, "=", first * second)
elif op == "/":
    if second != 0:
        print("Результат:", first, op, second, "=", first / second)
    else:
        print("Делить на ноль нельзя!")
else:
    print("Неверная операция!")
