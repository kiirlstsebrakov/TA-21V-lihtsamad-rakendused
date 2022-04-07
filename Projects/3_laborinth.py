import random

START = 12
FINISH = 24
ROAD = 1
WALL = 0

map = [
    [START, ROAD, ROAD, ROAD, ROAD],
    [WALL, WALL, WALL, WALL, ROAD],
    [WALL, FINISH, ROAD, WALL, ROAD],
    [WALL, WALL, ROAD, WALL, ROAD],
    [WALL, WALL, ROAD, ROAD, ROAD]
]

start_pos_x = 0 
start_pos_y = 0

y_rows = 5
x_columns = 5

def get_next_free_position(current_position_y, current_position_x):
    random_number = random.random()


    can_go_right = current_position_x+1 < x_columns and map[current_position_y][current_position_x+1] == ROAD
    can_go_left = current_position_x-1 > 0 and map[current_position_y][current_position_x-1] == ROAD
    can_go_bottom = current_position_y+1 < y_rows and map[current_position_y+1][current_position_x] == ROAD
    can_go_top = current_position_y-1 > 0 and map[current_position_y-1][current_position_x] == ROAD

    finish_on_right = current_position_x+1 < x_columns and map[current_position_y][current_position_x+1] == FINISH
    finish_on_left = current_position_x-1 > 0 and map[current_position_y][current_position_x-1] == FINISH
    finish_on_bottom = current_position_y+1 < y_rows and map[current_position_y+1][current_position_x] == FINISH
    finish_on_top = current_position_y-1 > 0 and map[current_position_y-1][current_position_x] == FINISH

    available_next_positions = []


    if can_go_right:
        print("can go right")
        position_on_right = [current_position_y, current_position_x+1]
        available_next_positions.append(position_on_right)

    if can_go_bottom:
        print("can go bottom")
        position_on_left = [current_position_y+1, current_position_x]
        available_next_positions.append(position_on_left)

    if can_go_left:
        print("can go left")
        position_on_bottom = [current_position_y, current_position_x-1]
        available_next_positions.append(position_on_bottom)

    if can_go_top:
        print("can go top")
        position_on_top = [current_position_y-1, current_position_x]
        available_next_positions.append(position_on_top)

    if finish_on_bottom:
        print("The end")
        print("[", current_position_y + 1, "]", "[", current_position_x, "]")
        quit()

    if finish_on_top:
        print("The end")
        print("[", current_position_y - 1, "]", "[", current_position_x, "]")
        quit()

    if finish_on_right:
        print("The end")
        print("[", current_position_y, "]", "[", current_position_x + 1, "]")
        quit()

    if finish_on_left:
        print("The end")
        print("[", current_position_y, "]", "[", current_position_x - 1, "]")
        quit()

    return random.choice(available_next_positions)

next_free_position = get_next_free_position(start_pos_y, start_pos_x)
print("Next free position is: ", next_free_position)

while next_free_position:
    print("Next free position is: ", next_free_position)
    next_free_position = get_next_free_position(next_free_position[0], next_free_position[1])