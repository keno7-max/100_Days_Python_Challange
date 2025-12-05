import random
import os
from art import logo
clear = lambda: os.system('cls')

def deal_card() :
   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
   card = random.choice(cards)
   return card



def calculate_score(cardS) :
   
   if len(cardS) == 2 and sum(cardS) == 21:
      return 0
   
   if 11 in cardS and sum(cardS) > 21 :
      cardS.remove(11)
      cardS.append(1)

   return sum(cardS)


def compare(user, computer):
   if user == computer :
      return "Draw"
   elif computer == 0 :
      return "Lose, opponent has Blackjack."
   elif user == 0 :
      return "Win with a Blackjack."
   elif user > 21 :
      return "You went over. You lose"
   elif computer > 21 :
      return "Opponent went over. You win"
   elif user > computer :
      return "You win"
   else:
      return "You lose"
   

def play_the_game() :
   print(logo)

   user_card = []
   computer_card = []
   is_game_over = False

   for i in range(0, 2):
      user_card.append(deal_card())
      computer_card.append(deal_card())
   while not is_game_over :
      user_score = calculate_score(user_card)
      computer_score = calculate_score(computer_card)

      print(F"Your cards: {user_card}, current score: {user_score}")
      print(f"computer's first card: {computer_card[0]}")

      if computer_score == 0 or user_score == 0 or user_score > 21:
         is_game_over = True


      else: 
         another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
         if another_card == 'y' :
            user_card.append(deal_card())
         elif another_card == 'n' :
            is_game_over = True


   while computer_score != 0 and computer_score < 17 :
      computer_card.append(deal_card())
      computer_score = calculate_score(computer_card)


   print(F"Your final hand: {user_card}, final score: {user_score}")
   print(f"computer's final hand: {computer_card}, final score: {computer_score}")
   print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == 'y' :
   clear()
   play_the_game()
      


   


   



    




















































































