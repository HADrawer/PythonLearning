import re
def isEmail(email):
    is_email = re.search(r"^[A-z0-9]+[\.-]?[A-z0-9]+@\w{3,}\.\w{2,3}$",email)

    if is_email:
        print(f'the {email} is a valid Email')
    else:
        print(f"the {email} is not a valid Email")

email = input("Enter your email: ")

print(f'Is {email} a email?')
isEmail(email)