from random import randint

number = randint(1,100)
print('Угадай число от 1 до 100')

while True:
    guess = int(input('Введите число '))
    if guess < number:
        print('Ваше число меньше')
    elif guess > number:
        print('Ваше число больше')
    elif guess == number:
        break
print('Молодец!')