import logging
logging.basicConfig(filename='myprogramlog.txt', level= logging.DEBUG, format='%(asctime)s -%(levelname)s -%(message)s')
## why can we use print
##because with the log we will get time and other parameters
## we can pretty easily stop the log messsages
## logging can be done in five levels:-
# list is in the order form lowest to the highest
# logging.debug()
# logging.info()
# logging.warning()
# logging.error()
# logging.critical()
logging.disable(logging.CRITICAL)
logging.debug('Start of program')
def factorial(n):
    logging.debug('First step is complete, the factorial (%s)' % (n))
    
    total = 1
    logging.debug('The variable "total" is set up to be 1')
    
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
    return total
    logging.debug('The for loop has been excecuted')
print(factorial(5))

logging.debug('End of the program')
