import re

def fewest_color(game_desc):
    largest_blue = 0
    largest_red = 0
    largest_green = 0
    sets = [s.strip() for s in game_desc.split(';')]
    for set_desc in sets:
        cubes = re.findall(r'(\d+) (\w+)', set_desc)
        for count, color in cubes:
            match color:
                case 'blue':
                    if int(count) > largest_blue:
                        largest_blue = int(count)
                case 'red':
                    if int(count) > largest_red:
                        largest_red = int(count)
                case 'green':
                    if int(count) > largest_green:
                        largest_green = int(count)
    return (largest_blue * largest_red * largest_green)
            
def is_game_possible(game_desc, bag):
    sets = [s.strip() for s in game_desc.split(';')]
    for set_desc in sets:
        cubes = re.findall(r'(\d+) (\w+)', set_desc)
        for count, color in cubes:
            if color in bag and bag[color] < int(count):
                return False
    return True

bag = {'red': 12, 'green': 13, 'blue': 14}
games = {}
possible_games = []
power_total = 0;

with open('input.txt', 'r') as file:
    for line in file:
        match = re.match(r'Game (\d+): (.+)', line)
        if match:
            game_id = int(match.group(1))
            game_desc = match.group(2)
            games[game_id] = game_desc

for game_id, game_desc in games.items():
    power_total += fewest_color(game_desc)
    if is_game_possible(game_desc, bag):
        possible_games.append(game_id)
    
total = sum(possible_games)

print(f"The sum of the IDs of possible games is: {total}")
print(f"The power total of the cubes of possible games is: {power_total}")