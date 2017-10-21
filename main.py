import random
player_one_input = None
player_two_input = None


print('Both players will guess a number between 1 and 100, whoever is closest to THE NUMBER is the winner!!!')
print('To exit enter 0')


def difference(player,rand):
    if player > rand:
        return player - rand
    else:
        return rand - player


while player_one_input != 0 and player_two_input != 0:
    random_number = random.randint(1,100)
    player_one_input = int(input('Player one\'s guess: '))
    player_two_input = int(input('Player two\'s guess: '))

    player_one_diff = difference(player_one_input, random_number)
    player_two_diff = difference(player_two_input, random_number)

    if player_one_diff == player_two_diff:
        print(f'Both player choose the same number! Try again!')
    elif player_one_diff > player_two_diff:
        print(f'Player two wins! THE NUMBER was {random_number}!!!')
        print(f'Player one was {player_one_diff} away from THE NUMBER')
        print(f'Player two was {player_two_diff} away from THE NUMBER')
    else:
        print(f'Player one wins! THE NUMBER was {random_number}!!!')
        print(f'Player one was {player_one_diff} away from THE NUMBER')
        print(f'Player two was {player_two_diff} away from THE NUMBER')


def difference(player,rand):
    if player > rand:
        return player - rand
    else:
        return rand - player

