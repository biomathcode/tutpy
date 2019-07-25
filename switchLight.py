market_2nd = {'ns':'green', 'ew':'red'}
## assert has to be too is a programmer error
## whereas We should raise an exception
## use assert statement for the
## assertion are insanity checks and should never be raised. 

def swithclight(intersection):
    for key in intersection.keys():
        if intersection[key] =='green':
            intersection[key] ='yellow'
        elif intersection[key] =='yellow':
            intersection[key] ='red'
        elif intersection[key] == 'red':
            intersection[key] ='green'

    assert 'red' in intersection.values(),'Neither light is red' + str(intersection)

print(market_2nd)



swithclight(market_2nd)

print(market_2nd)

    
