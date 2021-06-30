import random

def generateRandomNumber():
    randomNumber = random.randint(1, 100)
    return randomNumber

def results( numberOfEvenNumbers, numberOfOddNumbers ):
    print( "Out of 100, there were", numberOfEvenNumbers, \
           "even numbers and", numberOfOddNumbers, "odd numbers" )

def isEven(randomNumber):
    if (randomNumber % 2) == 0:
        return True
    return False

def main():
    numberOfEvenNumbers = 0
    numberOfOddNumbers = 0
    for count in range (1, 101):
        randomNumber = generateRandomNumber()
        print (randomNumber)
        if (isEven(randomNumber)):
            numberOfEvenNumbers +=1
        else:
            numberOfOddNumbers = numberOfOddNumbers + 1
    results( numberOfEvenNumbers, numberOfOddNumbers )
main()
