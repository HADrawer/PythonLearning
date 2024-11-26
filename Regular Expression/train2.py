import re

string = "Hello my number is 415-555-1011 and my friend's number is 658-984-2165"
replace = re.sub(r"-"," ", string) 
print(replace)
# r"\d{3}\s\d{3}\s\d{4}"