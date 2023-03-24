fileName = input("Enter the file name: ")
f = open(fileName, 'r')

numbers = []
for line in f:
    words = line.split()
    for word in words:
        numbers.append(float(word))

theDictionary = {}
for word in words:
    number = theDictionary.get(word, None)
    if number == None:
        # word entered for the first time
        theDictionary[word] = 1
    else:
        # word already seen, increment its number
        theDictionary[word] = number + 1

size: int = len(numbers)
sum_: int = 0

for i in numbers:
    sum_ = sum_ + i
    MEAN = sum_ / size
print("The mean is ", MEAN)
