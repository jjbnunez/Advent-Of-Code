"""
Day 2: Rock Paper Scissors

Solution written by JJ Nunez.
"""

import sys

def translateOpponentChoice(symbol):
    if symbol == 'A':
        return 'rock'
    if symbol == 'B':
        return 'paper'
    if symbol == 'C':
        return 'scissors'

def translatePlayerChoice(symbol):
    if symbol == 'X':
        return 'rock'
    if symbol == 'Y':
        return 'paper'
    if symbol == 'Z':
        return 'scissors'

def getChoiceScore(playerChoice):
    pc = playerChoice
    if pc == 'rock':
        return 1
    if pc == 'paper':
        return 2
    if pc == 'scissors':
        return 3

def getOutcomeScore(opponentChoice, playerChoice):
    oc = opponentChoice
    pc = playerChoice
    if oc == 'rock':
        if pc == 'scissors':
            return 0
        elif pc == 'rock':
            return 3
        elif pc == 'paper':
            return 6
    if oc == 'paper':
        if pc == 'rock':
            return 0
        elif pc == 'paper':
            return 3
        elif pc == 'scissors':
            return 6
    if oc == 'scissors':
        if pc == 'paper':
            return 0
        if pc == 'scissors':
            return 3
        if pc == 'rock':
            return 6

def findRequiredChoice(opponentChoice, desiredOutcomeSymbol):
    oc = opponentChoice
    dos = desiredOutcomeSymbol
    if dos == 'X':
        if oc == 'rock':
            return 'scissors'
        if oc == 'paper':
            return 'rock'
        if oc == 'scissors':
            return 'paper'
    if dos == 'Y':
        return opponentChoice
    if dos == 'Z':
        if oc == 'rock':
            return 'paper'
        if oc == 'paper':
            return 'scissors'
        if oc == 'scissors':
            return 'rock'

def solve1(data):
    totalScore = 0
    for line in data:
        opponentSymbol = line[0]
        playerSymbol = line[2]
        opponentChoice = translateOpponentChoice(opponentSymbol)
        playerChoice = translatePlayerChoice(playerSymbol)
        totalScore += getChoiceScore(playerChoice)
        totalScore += getOutcomeScore(opponentChoice, playerChoice)
    print("Problem 1 total score is", totalScore)

def solve2(data):
    totalScore = 0
    for line in data:
        opponentSymbol = line[0]
        desiredOutcomeSymbol = line[2]
        opponentChoice = translateOpponentChoice(opponentSymbol)
        playerChoice = findRequiredChoice(opponentChoice, desiredOutcomeSymbol)
        totalScore += getChoiceScore(playerChoice)
        totalScore += getOutcomeScore(opponentChoice, playerChoice)
    print("Problem 2 total score is", totalScore)

def main():
    # Get arg from command line
    args = sys.argv[1:]
    
    # Get list of lines from file
    with open(args[0], 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Trim newline characters off the ends
    data = []
    for line in lines:
        data.append(line.replace('\n', ''))
    
    # Get your answers
    solve1(data)
    solve2(data)
# Allows execution only from command line
# and not from import statements
if __name__ == '__main__':
    main()
