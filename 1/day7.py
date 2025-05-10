import random
stages = ['''
O

==========
''','''
2
==========
''','''
3
==========
''','''
4
==========
''','''
5
==========
''','''
6
==========
''','''
''']


world_list = ["aardvark", "baboon", "camel"]

lives = 6
chosen_word = random.choice(world_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("guess a letter: ").lower()


    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("you lose")

    if "_" not in display:
        print("Your win")
        game_over = True

    print(stages[lives])