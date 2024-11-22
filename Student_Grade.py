Grade = input("Enter Your Grade: ")

if not Grade:
    print("Please Enter a Number")
    exit()
Grade = int(Grade)
if Grade < 0 or Grade > 100:
    print("Please Enter a correct grade")
if 90 <= Grade <= 100:
    print("Your Grade is A")
elif 80 <= Grade <= 89:
    print("Your Grade is B")
elif 70 <= Grade <= 79:
    print("Your Grade is C")
elif 60 <= Grade <= 69:
    print("Your Grade is D")
elif 50 <= Grade <= 59:
    print("Your Grade is E")
elif 0 <= Grade <= 49:
    print("Your Grade is F")