"""
*******






"""



def boxprint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to a string to length 1.')
    if (width <2) or (height<2):
        raise Exception('"width" and "height" should be greater than 2. ')
    print(symbol * width)
    for i in range(height -2):
        print(symbol + (' ' * (width-2)) + symbol)

    print(symbol * width)

boxprint('*', 15, 5)
boxprint('0', 3, 30)

boxprint('))))', 2, 2)


