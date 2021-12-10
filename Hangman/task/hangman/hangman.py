import random
import string

alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)

print('H A N G M A N')


def main():
    lives = 8
    all_letters = []
    words = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(words)

    word_on_screen = len(word) * '-'

    print()

    while lives > 0:
        print()
        print(word_on_screen)

        if '-' not in word_on_screen:
            print('''You guessed the word!
You survived!''')
            break

        user_input = input('Input a letter: ')
        if len(user_input) > 1:
            print('You should input a single letter')
            continue

        if user_input not in alphabet_list:
            print('Please enter a lowercase English letter')
            continue

        if user_input in all_letters:
            print("You've already guessed this letter")
            continue
        else:
            all_letters.append(user_input)

        if user_input in word:
            x = [i for i in range(len(word)) if word.startswith(user_input, i)]

            for i in x:
                word_on_screen = list(word_on_screen)
                word_on_screen[i] = user_input
                word_on_screen = ''.join(word_on_screen)
        else:
            print("That letter doesn't appear in the word")
            lives -= 1
    else:
        print('You lost!')


while input('Type "play" to play the game, "exit" to quit: ') == 'play':
    main()
