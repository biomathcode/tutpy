##local variables can not be use in another scope 
def spam ():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()
## Code in the global scope can not use the local variables
##Code in a funtion's local scope can not use variables in another function's local scope
## if there's an assignment statement for a variable in a function, that is a local variable
##Global variables can be used in local scopes
def spam():
    print(eggs)
eggs = 42
spam()

## how to change the global variables

def spam():
    global eggs
    eggs= 'hello'
    print(eggs)

eggs = 42
spam()
print(eggs)
