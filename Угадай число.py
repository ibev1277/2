import random

def game():
    number_to_guess = random.randint(1, 100)
    guess = None
    tries = 0
    max_tries = 5
    print(f"У тебя есть {max_tries} попыток, чтобы угадать число от 1 до 100.")

    while guess != number_to_guess and tries < max_tries:
        guess = int(input("Введи число от 1 до 100: "))
        tries += 1
        if guess < number_to_guess:
            print("Слишком мало! Попробуй снова.")
        elif guess > number_to_guess:
            print("Слишком много! Попробуй снова.")
        
        tries_left = max_tries - tries
        print(f"Оставшееся количество попыток - {tries_left}.")

    if guess == number_to_guess:
        print(f"Поздравляю! Ты угадал число {number_to_guess} с {tries} раза.")
    else:
        print(f"Игра окончена, ты проиграл. Загаданное число было {number_to_guess}.")

if __name__ == "__main__":
    game()
