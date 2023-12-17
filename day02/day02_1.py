from aocd import get_data

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

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
        valid_game = True
        for r in rounds:
            counts = r.split(', ')
            for c in counts:
                c_color = c.split(' ')
                if c_color[1] == 'blue':
                    if int(c_color[0]) > BLUE_MAX:
                        valid_game = False
                if c_color[1] == 'red':
                    if int(c_color[0]) > RED_MAX:
                        valid_game = False
                if c_color[1] == 'green':
                    if int(c_color[0]) > GREEN_MAX:
                        valid_game = False
        if valid_game:
            game_id_sum += int(game_id)
    print(game_id_sum)
                    

if __name__ == "__main__":
    main()
