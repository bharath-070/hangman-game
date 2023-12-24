#import random module for the choice operation
import random
#get the ascii art for the title
logo="""
   _                                             
  | |                                            
  | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
  | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
  | | | | (_| | | | | (_| | | | | | | (_| | | | |
  |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/                       
"""
print(logo)
#get the asscii art into lists
hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
#get the list of words
word_list=["red","orange","yellow","green","blue","purple","black","white"]
#get the random word from the list
chosen_word=random.choice(word_list)
#print(chosen_word)
length=len(chosen_word)
#create a list of dashes the length of the word
display=[]
for letter in chosen_word:
  display+="_"
print(display)
#declare the life as 1
life=1
hint_times=1
#create a while loop to run the game
while "_" in display and life<7:
  #get the user input
  guess=input("guess the letter: ").lower()
  #create a for loop to check if the letter is in the word
  if guess in display:
    print("you alredy chosen this letter")
    #if the letter is in the word, print the letter in the display list
  for i in range(len(chosen_word)):
    if guess == chosen_word[i]:
       display[i] = guess
       print(display)
  #if the letter is not in the word, print the hangman and decrease the life
  if guess not in chosen_word and life<7:
    print(f"You guessed {guess}, that's not in the word. You lose a life\n")
    print(hangman[life])
    #ask for the hint only once
    while hint_times>0:
      hint=input("Do you want a hint? (y/n)").lower()
      if hint == "y":
        print("The word is one of the color!")
      hint_times=0
    life+=1
#if the user guessed the word, print the ascii art for the winner
if life>6:
  print("""                      _                
                             | |               
          _   _  ___  _   _  | | ___  ___  ___ 
         | | | |/ _ \| | | | | |/ _ \/ __|/ _ \
         | |_| | (_) | |_| | | | (_) \__ \  __/
          \__, |\___/ \__,_| |_|\___/|___/\___|
           __/ |                               
          |___/                                
""")
  #if the user didn't guess the word, print the ascii art for the loser
else:
  print("""                               _       
                              (_)      
  _   _  ___  _   _  __      ___ _ __  
 | | | |/ _ \| | | | \ \ /\ / / | '_ \ 
 | |_| | (_) | |_| |  \ V  V /| | | | |
  \__, |\___/ \__,_|   \_/\_/ |_|_| |_|
   __/ |                               
  |___/                                
""")  
      