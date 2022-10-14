"""
Word Spelling Game
Created by Braden Piper, bradenpiper.com
Created on Fri Oct 14, 2022
Version = 1.1
------------------------------------------
A word spelling game similar to Scrabble. The program will provide the player with
a specified number of letters. The player attempts to spell words using the provided
letters, and each word is assigned a score. Each letter has its own score value,
and longer words score more points. If the player is able to spell a word using
all of the letters on the fist turn, they get a bonus score of 50 points.
Play continues until the player uses all of the letters, or they give up because
they can no longer spell any words, and a final score is awarded.
After the game is over, the player can opt to play again using the same set of
letters, or a new set of letters.
------------------------------------------
NOTE: This program was completed as part of the course MITx 6.00.1x - Introduction
to Computer Science and Programming using Python. The general framework, and some
of the functions were provided materials. The majority of the implementation is
my own work.
The provided functions include:
    loadwords()
    getFrequencyDict(sequence)
The remainder of the function names were provided with pseudocode descriptions,
but the implementations are my own.
"""

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 12

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    base_score = 0
    for letter in word: # iterate through each letter in the word
        base_score += SCRABBLE_LETTER_VALUES[letter] # look up the value of the letter in the SCRABBLE_LETTER_VALUES dict, += the values to a variable called base_score
    score = base_score * len(word)   # multiply base_score times the length of the word and store in score
    if len(word) == n:   # if all letters were used, add 50 to score
        score += 50
        return score
    else:
        return score


#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    tempHand = hand.copy()   # copy hand into a tempHand
    for letter in word: # for each letter in word, update the corresponding value in tempHand to value-1
        tempHand[letter] -= 1
    return tempHand


#
# Problem #3: Test word validity
#

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    isValid = True
    tempHand = hand.copy()
    if word not in wordList:
        isValid = False
    for letter in word:
        if letter not in tempHand:
            isValid = False
        else:
            tempHand[letter] -= 1
    tempHandValues = tempHand.values()
    for value in tempHandValues:
        if value < 0:
            isValid = False
    return isValid
            

#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    values = list(hand.values())
    length = 0
    for value in values:
        length += value
    return length
    

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    score = 0  # Keep track of the total score
    
    while calculateHandlen(hand) > 0: # As long as there are still letters left in the hand:
        print('Current Hand: ', end = ' ')
        displayHand(hand)   # Display the hand
        word = input('Enter word, or a "." to indicate that you are finished: ')   # Ask user for input
        if word == '.':   # If the input is a single period:
            print('Goodbye!', end = ' ')
            break   # End the game (break out of the loop)
        else:   # Otherwise (the input is not a single period):
            if not isValidWord(word, hand, wordList):   # If the word is not valid:
                print('Invalid word, please try again.')   # Reject invalid word (print a message followed by a blank line)
                print()
            else:   # Otherwise (the word is valid):
                score += getWordScore(word,n)
                print('"'+word+'"','earned',getWordScore(word,n),'points. Total:',score,'points')   # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                print()
                hand = updateHand(hand,word)   # Update the hand
        if calculateHandlen(hand) == 0:
            print('Run out of letters.', end = ' ')
    print('Total score:', score,'points.')   # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    

#
# Problem #5: Playing a game
# 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    gameCounter = 0
    gameOver = False
    while gameOver == False:
        userInput = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if userInput == 'n':
            gameCounter += 1
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
        elif userInput == 'r' and gameCounter == 0:
            print('You have not played a hand yet. Please play a new hand first!')
        elif userInput == 'r' and gameCounter > 0:
            playHand(hand, wordList, HAND_SIZE)
        elif userInput == 'e':
            gameOver = True
        else:
            print('Invalid command.')



#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
