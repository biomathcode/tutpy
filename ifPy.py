name = input()
def NameChecker(name):
    if name == 'Pratik':
        print('Hi ' + name)
        return True
    elif name == '':
        print('You didn\'t type your name.')
    else:
        print('fuck you bastard')
        return False
NameChecker(name)
print('DOne')
