numbers = [1,2,3,4,5,6,7,8,9]

grouped_numbers = []

size = 2

for i in range(0,len(numbers), size):
    grouped_numbers.append(numbers[i:i+size])
    
print(grouped_numbers)