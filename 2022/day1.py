def organizeData(data) :
    elfData = {}  
    
    elves = data.split("\n\n") 

    elves = [list(map(int, elf.strip().split("\n"))) for elf in elves]

    incrementationNum = 1
    for calories in [sum(elf) for elf in elves] : 
        elfData['elf' + str(incrementationNum)] = int(calories)
        incrementationNum = incrementationNum + 1

    return elfData

greatestElf = ""
greatest = 0

elfData = organizeData(open("input.txt", "r").read())
for elf in elfData :
    if elfData[elf] > greatest :
        greatest = elfData[elf]
        greatestElf = elf

print(greatestElf, greatest)

