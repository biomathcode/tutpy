import re

message ='Call me at 415-555-1011 tomorrow, or at 415-555-9999'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall(message))

# regular expression are the mini-language for specifying text patterns. Writing code to do pattern matching without regular expressions is a huge pain.
