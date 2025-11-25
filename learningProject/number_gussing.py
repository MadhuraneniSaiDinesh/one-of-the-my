import random

while True:
    random_number = random.randint(1, 100)
    try:
        guess = int(input('Guess the number between 1 to 100: '))
        if guess < random_number:
            print('Too Low')
        elif guess > random_number:
            print('Too High')
        else:
            print('You got it 👍👍')
            break
    except ValueError:
        print('Please Enter a Valid number')