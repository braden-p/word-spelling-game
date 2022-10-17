Word Spelling Game
Created by Braden Piper, bradenpiper.com
Created on Fri Oct 14, 2022
Version = 1.1
------------------------------------------
DESCRIPTION:
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
The variable HAND_SIZE determines the number of letters dealt to the player.
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