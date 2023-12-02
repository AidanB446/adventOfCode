
data = open("input.txt", "r").read()

data = data.split("\n")
numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

numberList = []

for line in data :
    
    nums = "" 

    for i, letter in enumerate(line) :

        for x, number in enumerate(numbers) :

            if number in line[i:i + len(number)] :
                nums = nums + str(x)


        if letter.isnumeric() :
            nums = nums + letter

    
    if len(nums) == 0 :
        continue

    numberList.append(nums[0] + nums[len(nums) - 1])

print(sum([int(num) for num in numberList]))


