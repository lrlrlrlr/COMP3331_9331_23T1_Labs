import re


incoming_message = "hello, my name is Kate, I am 23 years old."

match_name = re.search(r'my name is (\w+),',incoming_message).group(1)
print(match_name)

match_age = re.search(r'\d+',incoming_message).group()
print(match_age)