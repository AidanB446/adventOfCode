
data = open("input.txt", "r").read()
data = data.split("\n")

numberList = []

for line in data :
    
    if len(line) == 0 :
        continue

    numString = ""

    for letter in line :
        if letter.isnumeric() :
            numString = numString + letter
    
    numberList.append(numString[0] + numString[len(numString) - 1])

print(sum([int(num) for num in numberList]))
 

