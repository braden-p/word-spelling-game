# Word Spelling Game
#### Created by Braden Piper, bradenpiper.com
#### Created on Fri Oct 14, 2022
#### Version = 1.1
---
## DESCRIPTION
A word spelling game similar to Scrabble. The program will provide the player with
a specified number of letters. The player attempts to spell words using the provided
letters, and each word is assigned a score. Each letter has its own score value,
and longer words score more points. If the player is able to spell a word using
all of the letters on the fist turn, they get a bonus score of 50 points.
Play continues until the player uses all of the letters, or they give up because
they can no longer spell any words, and a final score is awarded.
After the game is over, the player can opt to play again using the same set of
letters, or a new set of letters.

## SCORING
The score for a word is the sum of the points for letters in the word, multiplied
by the length of the word, PLUS 50 points if all n letters are used on the first turn.

### Letter Values
| Letter | Score |
| ------ | ------ |
|a|1|
|a|1|
|b|3|
|c|3|
|d|2|
|e|1|
|f|4|
|g|2|
|h|4|
|i|1|
|j|8|
|k|5|
|l|1|
|m|3|
|n|1|
|o|1|
|p|3|
|q|10|
|r|1|
|s|1|
|t|1|
|u|1|
|v|4|
|w|4|
|x|8|
|y|4|
|z|10|

## HOW TO PLAY
- Set the variable `HAND_SIZE` to the desired amount of letters for the game.
- Run the program

##### NOTE:
This program was completed as part of the course MITx 6.00.1x - Introduction
to Computer Science and Programming using Python. The general framework, and some
of the functions were provided materials. The majority of the implementation is
my own work.
The provided functions include:
- `loadwords()`
- `getFrequencyDict(sequence)`

The remainder of the function names were provided with pseudocode descriptions,
but the implementations are my own.