
import random

HANGMAN_PICS = [""" 
 +===+
     |
     |
     |
    ===
""", """
 +===+
 O   |
     |
     |
    ===
""", """
 +===+
 O   |
 |   |
     |
    ===
""", """
 +===+
 O   |
/|   |
     |
    ===
""", """
 +===+
 O   |
/|\  |
     |
    ===
""", """
 +===+
 O   |
/|\  |
/    |
    ===
""", """
 +===+
 O   |
/|\  |
/ \  |
    ===
"""]

words = ["rhino", "porsche", "quill", "haemoglobin", "hello"]

def getRandomWord(wordList):
    wordIndex = random.randint(0,len(wordList)-1)
    return wordList[wordIndex]
    

def displayBoard(missedLetters, correctLetters, secretWord, hangman_pics):
    print(hangman_pics[len(missedLetters)])
    print("\n")
    print(f"Missed letters: {missedLetters}")
    print("\n")

    blanks = ''

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks + secretWord[i]
        else:
            blanks = blanks + '_'

    for character in blanks:
        print(character + ' ', end = '')
    print("\n")
          

def getGuess(alreadyGuessed):
    
    while True:
        guess = input("Guess a letter: ")
        guess = guess.lower()

        if guess in alreadyGuessed:
            print("You have already guessed this letter.")

        elif len(guess) != 1:
            print("Please enter a single letter...")

        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a letter...")
        
        else:
            return guess

def playAgain():
    print("Do you wanna play again? | y/n")

    response = input()
    response.lower()

    while response != 'y' and response != 'n':
        print("Do you wanna play again? | y/n")

        response = input()
        response.lower()

    if response == 'y':
        return True
    elif response == 'n':
        return False

    

##################### M A I N #######################

print("H A N G M A N")

missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)

gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord, HANGMAN_PICS)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False

        if foundAllLetters == True:
            print("Yes! The secret word is " +secretWord + ". You have won!")
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord, HANGMAN_PICS)
            print("You've run out of guesses!")
            print(f"The word was {secretWord}")
            gameIsDone = True

        


    if gameIsDone == True:

        if playAgain() == True:
            missedLetters = ''
            correctLetters = ''
            secretWord = getRandomWord(words)

            gameIsDone = False
            
        else:
            break





























