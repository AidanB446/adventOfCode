def organizeData(data) :
    elves = data.split("\n\n")

    elves = [list(map(int, elf.strip().split("\n"))) for elf in elves]

    return [sum(calorie) for calorie in elves]

totalCal = organizeData(open("input.txt", "r").read())
totalCal.sort(reverse=True)

print(totalCal[0] + totalCal[1] + totalCal[2])
