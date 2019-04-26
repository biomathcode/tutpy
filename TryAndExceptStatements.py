print('How many cats do you have?')
numcats = input()
try:
    if int(numcats)>= 4:
        print('that a lot of cats')
    else:
        print('that not a lot of cats')
except ValueError:
    print('You did not enter a number')
