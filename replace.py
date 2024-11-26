asd = input()
asd = asd.split(" ")
print(asd)
asd1 = []

#i use for but you can use asd.reverse directly
for i in range(len(asd)):
    asd1.append(asd[len(asd)-i-1])

asd = " ".join(asd1)

print(asd)