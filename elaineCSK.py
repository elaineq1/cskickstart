import random
import sys
import time
from art import *

typing_speed = 350
def slow_type(msg):
    for letter in msg:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')

print()
slow_type('Hello! What is your name?')
name = input()
slow_type('Hi {}. Welcome to the game selector!'.format(name))
decor("love_music")
print()

slow_type('What game would you like to play?')
slow_type('Please select from the following:')
print()
slow_type('1: Blackjack')
slow_type('2: Rock Paper Scissors')
slow_type('3: Trivia')
print()
slow_type('Enter a number to make your selection:')

choice = input()
answers = ['1', '2', '3']
while choice not in answers:
  slow_type('Invalid input. Enter a number (1-3):')
  choice = input()
print()

user_win = 0
user_lose = 0
user_tie = 0

def blackjack():
    user_score = 0
    user_cards = []
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    points = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    global user_win
    global user_lose
    global user_tie

    ran1 = random.randint(0,12)
    ran2 = random.randint(0,12)
    user_score += points[ran1] + points[ran2]
    user_cards.append(cards[ran1])
    user_cards.append(cards[ran2])

    slow_type('Your turn!')
    slow_type('Your first card is a {}.'.format(cards[ran1]))
    slow_type('Your second card is a {}.'.format(cards[ran2]))
    slow_type('Your total score is {}.'.format(user_score))
    print()

    valid = ['hit', 'stand']
    slow_type('Hit or stand?')
    ans = input().lower()
    while ans not in valid:
        slow_type('Not a valid input. Enter hit or stand:')
        ans = input().lower()
    
    while ans == 'hit':
        ran = random.randint(0, 12)
        user_score += points[ran]
        user_cards.append(cards[ran])
        slow_type('You chose: hit')
        slow_type('Your next card is a {}.'.format(cards[ran]))
        slow_type('Your total score is {}.'.format(user_score))
        if user_score > 21:
            slow_type('You have busted!')
            break
        print()
        slow_type('Hit or stand?')
        ans = input().lower()
        while ans not in valid:
            slow_type('Invalid input. Enter hit or stand:')
            ans = input().lower()
    
    if ans == 'stand':
        slow_type('You chose: stand')
    print()

    slow_type("Dealer's turn!")
    comp_score = 0
    comp_cards = []

    c_ran1 = random.randint(0,12)
    c_ran2 = random.randint(0,12)
    comp_score += points[c_ran1] + points[c_ran2]
    comp_cards.append(cards[c_ran1])
    comp_cards.append(cards[c_ran2])
    
    while comp_score < 17:
        c_ran = random.randint(0, 12)
        comp_score += points[c_ran]
        comp_cards.append(cards[c_ran])
        slow_type('Dealer has chosen to hit.')
    
    if comp_score <= 21:
        slow_type('Dealer has chosen to stand.')
    else:
        slow_type('Dealer has busted!')
    print()

    slow_type("Dealer's score: {}".format(comp_score))
    slow_type("Dealer's cards:")
    print(comp_cards)
    print()

    slow_type('Your score: {}'.format(user_score))
    slow_type('Your cards:')
    print(user_cards)
    print()

    if user_score > 21:
        slow_type('You lost. Better luck next time!')
        user_lose += 1
    else:
        if comp_score > 21:
            slow_type('You won. Congratulations!')
            user_win += 1
        else :
            if user_score > comp_score:
                slow_type('You won. Congratulations!')
                user_win += 1
            elif comp_score > user_score:
                slow_type('You lost. Better luck next time!')
                user_lose += 1
            else:
                slow_type('You tied!')
                user_tie += 1
    print()

def bj_rules():
    slow_type('Rules for Blackjack:')
    slow_type('Objective: score the best possible hand without going over 21. Note: in this version, aces are worth 1 point and all face cards are worth 10 points. \
You will first be dealt two cards. You can then decide to hit (receive another card) or stand (stay at current score). \
You can hit as many times as you want, but be careful not to bust. To help you keep count, your score will be shown after each card. \
The dealer will then play. The dealer will keep hitting until their score is at least 17. They will then reveal their cards and their score. \
If you have busted, you lose (even if the dealer also busts). If the dealer has busted and you have not, you win. Otherwise, whoever has the higher score wins.')
    slow_type('Have fun and good luck!')
    print()

def rock_paper_scissors():
    pos = ['rock', 'paper', 'scissors']
    comp = ''
    global user_win
    global user_lose
    global user_tie

    slow_type('Ready?')
    slow_type('Rock, paper, scissors...')
    slow_type('Make your selection:')

    user = input().lower()
    while user not in pos:
        slow_type('Invalid input. Enter rock, paper, or scissors:')
        user = input().lower()
    print()
    slow_type('You selected: {}'.format(user))

    rand = random.randint(0, 2)
    if rand == 0:
        comp = 'rock'
    elif rand == 1:
        comp = 'paper'
    else:
        comp = 'scissors'
    
    slow_type('Computer selected: {}'.format(comp))

    if user == comp:
        slow_type('You tied!')
        user_tie += 1
    else:
        if (user == 'rock' and comp == 'scissors') or (user == 'paper' and comp == 'rock') or (user == 'scissors' and comp == 'paper'):
            slow_type('You won. Congratulations!')
            user_win += 1
        else:
            slow_type('You lost. Better luck next time!')
            user_lose += 1
    print()

def rps_rules():
    slow_type('Rules for Rock Paper Scissors:')
    slow_type("I sincerely hope that you don't need instructions for rock paper scissors. But just in case... Rock beats scissors. Paper beats rock. Scissors beats paper.")
    slow_type('Have fun and good luck!')
    print()

again = ['yes', 'no']
if choice == '1':
    slow_type('You have chosen to play Blackjack.')
    print()
    bj_rules()
    blackjack()
    slow_type('Play again?')
    play = input().lower()

    while play not in again:
        slow_type('Invalid input. Enter yes or no:')
        play = input().lower()

    while play == 'yes':
        slow_type('You chose: yes.')
        print()
        blackjack()
        slow_type('Play again?')
        play = input().lower()
        while play not in again:
            slow_type('Invalid input. Enter yes or no:')
            play = input().lower()

    if play == "no":
        print()
        slow_type('You have exited Blackjack.')

elif choice == '2':
    slow_type('You have chosen to play Rock Paper Scissors.')
    print()
    rps_rules()
    rock_paper_scissors()
    slow_type('Play again?')
    play = input().lower()

    while play not in again:
        slow_type('Invalid input. Enter yes or no:')
        play = input().lower()

    while play == 'yes':
        slow_type('You chose: yes.')
        print()
        rock_paper_scissors()
        slow_type('Play again?')
        play = input().lower()
        while play not in again:
            slow_type('Invalid input. Enter yes or no:')
            play = input().lower()

    if play == "no":
        print()
        slow_type('You have exited Rock Paper Scissors.')

elif choice == '3':
  slow_type('You have chosen to play Trivia.')
  print()

slow_type('Thank you for playing, {}!'.format(name))
print()

if user_win == 1:
    slow_type('You won 1 time :)')
else:
    slow_type('You won {} times :)'.format(user_win))
if user_tie == 1:
    slow_type('You tied 1 time :|')
else:
    slow_type('You tied {} times :|'.format(user_tie))
if user_lose == 1:
    slow_type('You lost 1 time :(')
else: 
    slow_type('You lost {} times :('.format(user_lose))
print()

slow_type('And remember...')
text2art('Go Bears!')
text2art(name, font = 'bear')