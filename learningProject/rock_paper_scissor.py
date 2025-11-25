import random

Rock = 'r'
Scissors = 's'
Papper = 's'
emojis = {Rock: '🪨' , Scissors : '✂️', Papper : '📃'}
choices = ('r','p','s')

def get_user_choose():
    while True:
        user_input = input('Play the Game Rock , scissors or paper? (r/s/p): ').lower()
        if user_input not in choices :
            print('Invalid Choice 😡😡, Please Enter valid Choice 😍😍😍')
        else: 
            return user_input
            
def user_computer_inputs(user_choose,computer_input):
    print(f'👱 You Chose {emojis[user_choose]}')
    print(f'🖥️ computer_input {emojis[computer_input]}')

def winner_result(user_choose,computer_input):
    if (user_choose==computer_input):
        print('Tie!')
    elif ((user_choose == Scissors and computer_input == Papper) or 
        (user_choose == Rock and computer_input == Scissors) or 
        (user_choose == Papper and computer_input == Rock)):
        print(f'You Win 👑 {emojis[user_choose]}' )
    else :
        print('You lose 😞')

def play_game(): 
    while True :

        user_choose = get_user_choose()

        computer_input = random.choice(choices)

        user_computer_inputs(user_choose,computer_input)

        winner_result(user_choose,computer_input)

        should_continue = input('Continue? (Y/n): ').lower()
        if should_continue == 'n':
            break
        else :
            continue
play_game()