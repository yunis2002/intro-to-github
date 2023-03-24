fileName = input("Enter the file name: ") #GUEVARRA
f = open(fileName, 'r')

numbers = []
for line in f:
    words = line.split()
    for word in words:
        numbers.append(float(word))

size: int = len(numbers)
sum_: int = 0

for i in numbers:
    sum_ = sum_ + i
    MEAN = sum_ / size
print("The mean is ", MEAN)
