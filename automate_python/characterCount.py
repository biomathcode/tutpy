import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}## 'r': 12
## we can use string in for loop because string is a list like data stucture
## this also mean that the variable will be counted singularly

for character in message.upper():
    ##making sure that it start at a 0 
    count.setdefault(character, 0)
    count[character] = count[character] + 1 

pretty_text = pprint.pformat(count)
print(pretty_text)
