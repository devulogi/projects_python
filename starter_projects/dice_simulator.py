'''A simple dice roll game'''
from random import randint

def dice_roll():
    '''This game will roll the dice and give you the result each roll'''
    try:
        # get dice roll times
        rolls: int = int(input("How many times would you like to roll? "))
    except ValueError:
        print('Please enter a valid number')
        
    # list result of each dice roll
    result = []
    
    # roll the dice and insert into the result list
    for _ in range(rolls):
        result.append(randint(1, 6))
    
    print(*result, sep=', ')
