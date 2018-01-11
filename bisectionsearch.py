#secret number

low1 = 0
high1 = 100
lastGuessWas = ''

print 'Please think of a number between 0 and 100!'

while lastGuessWas != 'c':
    guess = (high+low1)/2
    print "Is your secret number {}?".format(guess)
    lastGuessWas = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if lastGuessWas not in ('l', 'h', 'c'):
        print 'Sorry, I did not understand your input.'
    elif lastGuessWas == 'l':
        low1 = guess
    elif lastGuessWas == 'h':
        high1 = guess
    elif lastGuessWas == 'c':
        print "Game over. Your secret number was: {}".format(guess)

#minimum to pay off debt in 1 year

monthlyInterestRate = annualInterestRate/12.0
high2 = (balance * (1 + monthlyInterestRate)**12)/12.0
low2 = balance/12
fixedPayment = (high2 + low2)/2

def adequatePayment(balance,monthlyInterestRate,fixedPayment):
    '''
    balance - the outstanding balance on the credit card
    monthlyInterestRate -  monthly interest rate as a decimal
    '''
    for month in range(1, 12)
        balance -=  fixedPayment #Update the outstanding balance by removing the payment,
        balance += monthlyInterestRate*balance #then charging interest on the result.
    return balance

while True:
    z = adequatePayment(balance,monthlyInterestRate,fixedPayment)
    if  round(z) < 0:
        high2 = fixedPayment
        fixedPayment = (high2 + low2)/2
    elif round(z) > 0:
        low2 = fixedPayment
        fixedPayment = (high2 + low2)/2
    elif round(z) == 0:
        print 'Lowest Payment:',round(fixedPayment,2)
        break

#check if a character is in a string with recursion

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    high = len(aStr)-1
    middle = high/2
    if aStr == "" :
        return False
    elif len(aStr) == 1:
        return aStr == char
    elif aStr[middle] == char:
        return True
    elif char < aStr[middle]:
        return isIn(char, aStr[:middle-1])
    else:
        return isIn(char, aStr[middle+1:])
