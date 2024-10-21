# Write your code here
import random
letter = []
wins = 0
loses = 0
def computer():
    lis = ['python', 'java', 'swift', 'javascript']
    num = random.randint(0, 3)
    return lis[num]
def dash(comp):
    global letter
    for i in range(len(comp)):
        letter.append('-')
def hide(st):
    new_str = []
    count = 0
    for i in st:
        if count < 3:
            new_str.append(i)
            count += 1
        else:
            new_str.append('-')
    return ''.join(new_str)
def letter_replace(word, comp):
    global letter
    for i in range(len(comp)):
        if word == comp[i]:
            letter[i] = word

def invalid(word):
    if len(word) > 1 or word == '' or word == ' ':
        print("Please, input a single letter.")
        return True
    elif word.isupper() or not word.isalpha():
        print("Please, enter a lowercase letter from the English alphabet.")
        return True
def play():
    global wins, loses
    comp = computer()
    count = 7
    dash(comp)
    uncovered = []
    while count >= 0:
        print()
        x = ''.join(letter)
        
        if x == comp:
            break
        print(x)
        word = input("Input a letter: ")
        if invalid(word):
            continue
        if word in uncovered:
            print("You've already guessed this letter.") 
            continue
        if word in comp:
            uncovered.append(word)
            letter_replace(word, comp)
        else:
            print("That letter doesn't appear in the word.")
            uncovered.append(word)
            count -= 1
    print()
    o = x.replace('-', '')
    if o == comp:
        print(f"You guessed the word {comp}!")
        print("You survived!")
        wins += 1
    else:
        print("You lost!")
        loses += 1
def main_menu():
    global letter
    print('H A N G M A N')
    while True:
        print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
        user_input = input()
        if user_input == 'play':
            play()
            print()
            letter = []
        elif user_input == 'results':
            print(f"You won: {wins} times.")
            print(f"You lost: {loses} times.")
            pass
        elif user_input == 'exit':
            break
        else:
            print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
            continue
main_menu()