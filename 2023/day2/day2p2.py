
data = open("input.txt", "r").read()

data = data.split("\n")

sum = 0
for i, line in enumerate(data) :

    if len(line) == 0 :
        continue

    line = line.split(':')[1].split(';') 
    
    possible = True

    red = 0
    green = 0
    blue = 0

    for games in line :
        
        games = games.strip().split(',')
        
        for game in games :

            game = game.strip().split(' ')
            
            if game[1] == 'red' and int(game[0]) > red :
                red = int(game[0])
            
            if game[1] == 'green' and int(game[0]) > green :
                green = int(game[0])

            if game[1] == 'blue' and int(game[0]) > blue :
                blue = int(game[0])
            
    sum = sum + (red * green * blue)  

print(sum)

