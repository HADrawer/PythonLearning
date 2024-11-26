import re
def isPhoneNumber(text):
    search = re.search(r"\d{3}-\d{3}-\d{4}",text)
    
    if search:
        return True
    else:
        return False

number = input("Add the number :")

print(isPhoneNumber(number))