import re

txt = "My name is Hashem"

search = re.search("[A-Z]", txt)

print(search)
# print(search.group())


test = "Call me at 414-555-1011 tomorrow. 415-555-9999 is my office"

search1 = re.search(r"\d{3}-\d{3}-\d{4}", test)
print(search1)

search2 = re.findall(r"\d{3}-\d{3}-\d{4}", test)
print(search2)
search3 = re.findall(r"A", test)
print(search3)


phone_number = input("here: ")
