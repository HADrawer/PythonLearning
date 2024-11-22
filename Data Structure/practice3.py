numbers = [1,2,2,2,4,4,5,6,7,8,8]

seen = {}

dups = []

for number in numbers:
    if number not in seen:
        seen[number] = 1
    else:
        if seen[number] == 1:
            dups.append(number)
        seen[number] += 1
    
print(dups)