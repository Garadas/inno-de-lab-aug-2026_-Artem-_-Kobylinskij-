from random import randint

print("Я загадал число от 1 до 20. У тебя 5 попыток!")
attempts = 0
answer = randint(1, 20)
while attempts < 5:
    attempts += 1
    guess = int(input("Попытка " + str(attempts) + ". Введите число: "))
    if guess > answer:
        print("Слишком много! осталось попыток", 5 - attempts)
    elif guess < answer:
        print("Слишком мало! осталось попыток", 5 - attempts)
    else:
        print("Ты угадал! Отличная работа.")
        break
