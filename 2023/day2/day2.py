
data = open("input.txt", "r").read()

data = data.split("\n")

sum = 0
for i, line in enumerate(data) :

    if len(line) == 0 :
        continue

    line = line.split(':')[1].split(';') 
    
    possible = True
    
    for games in line :

        games = games.strip().split(',')

        for game in games :

            game = game.strip().split(' ')

            if ((game[1] == 'red' and int(game[0]) > 12) or
                (game[1] == 'green' and int(game[0]) > 13) or
                (game[1] == 'blue' and int(game[0]) > 14)) : 
                
                possible = False

    if possible :
        sum = sum + i + 1

print(sum)

