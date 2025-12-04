import random
import hangman_art
import hangman_words


print(hangman_art.logo)
lives = 6
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for i in range(0, word_length):
    placeholder += "_"
print(f"Word to guess: {placeholder}")

game_over = False
correct_letter = []
while not game_over :
    
    guess = input("Guess a letter: ").lower()
    

    if guess in correct_letter :
       print(f"You've already guessed {guess}")

    display = ""
    for i in range(0,word_length):
        letter = chosen_word[i]
        if letter == guess :
           correct_letter.append(letter)
           display += letter
        elif letter in correct_letter :
            display += letter
        else:
           display += "_"

    print("Word to guess: " + display)
    
    if guess not in display :
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
    
        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")
    
    

    if "_" not in display  :
       game_over = True
       print("You Win!.")
    
    print(hangman_art.stages[lives])

    print(f"****************************{lives}/6 LIVES LEFT****************************")
   
    


