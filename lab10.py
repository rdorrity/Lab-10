# Ryan Dorrity , Nathan Warren-Acord
# Lab 10
# 11/16/2018

######## Warm Up #####################

#while True:
  #word = requestString("Enter word")
 # if word == 'stop':
   # break
    



#######################################
########### Hangman game ##############

# Output a brief description of the game of hangman and how to play
# The word to guess can be hard-coded in your program, but it should be easy to change the word
#########################################################################################
def hangman():
  printNow("Welcome to Hangman! Try to guess what the secret word is one letter at a time.")
  answer = "banana" 
  test = ""
  win = false
  k = 6
  solution = []
  for i in range(0, len(answer)):
    solution.append("-")
    
    
#Continuously read guesses of a letter from the user and fill in the corresponding blanks 
#if the letter is in the word, otherwise report that the user has made an incorrect guess. 

  while k > 0:    
    correct = False
    guess = checkGuess()
    correct = find(answer, guess)
    if correct == false:
      k = k - 1
      print "Incorrect guess"
      print "You only have " + repr(k) + " missed attempts left"
    else:
      for index in range(0, len(answer)):
        if guess == answer[index]:
          solution[index] = guess
        letter = solution[index]
        print letter,  
      print "Correct"
          
    win = checkWin(answer, solution)
    if win == true:
      print "You win!!"
      break
    if k == 0:
      print "You lose. Please try again"
      
#########################################################################################             
# error checks input      
def checkGuess():
  guess = requestString("Guess a letter")
  guess.lower()
  temp = ""
  if len(guess) > 1:
    print "Please enter only one letter"
    temp = checkGuess()
  elif ord(guess) < 65 or ord(guess) > 122:
    print "Please enter only letters A-Z"
    temp = checkGuess()    
  elif ord(guess) >= 65 and ord(guess) <=122 and len(guess) < 2:  
    return guess
  return temp
#########################################################################################    
# looks for letter in answer    
def find(answer, guess):
  index = 0
  count = 0
  while index < len(answer):
    if answer[index] == guess:
      count = count + 1
    index = index + 1 
  if count > 0:
    return true
  else:
    return false
    
#########################################################################################    
# Checks for win    
def checkWin(answer, solution):
  count = 0
  for i in range(0, len(answer)):
    if solution[i] != '-':
      count = count + 1
  if count == len(answer):
    return true
  else:
    return false
