from aocd import get_data

def main():
    my_data = get_data(day=2, year=2023)
    # print(my_data)
    lines = my_data.split("\n")
    print(len(lines))
    game_id_sum = 0
    for line in lines:
        # print(line)
        game_info = line.split(': ')
        game_id = game_info[0].split(' ')[1]
        rounds = game_info[1].split('; ')
        max_green = 0
        max_blue = 0
        max_red = 0
        for r in rounds:
            counts = r.split(', ')
            for c in counts:
                c_color = c.split(' ')
                if c_color[1] == 'blue':
                    if int(c_color[0]) > max_blue:
                        max_blue = int(c_color[0])
                if c_color[1] == 'red':
                    if int(c_color[0]) > max_red:
                        max_red = int(c_color[0])
                if c_color[1] == 'green':
                    if int(c_color[0]) > max_green:
                        max_green = int(c_color[0])
        game_power = max_blue * max_red * max_green
        if game_power == 0:
            print(f'Game {game_id} had 0 power')
        game_id_sum += game_power
    print(game_id_sum)
                    

if __name__ == "__main__":
    main()
