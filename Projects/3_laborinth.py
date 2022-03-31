map = [
    [5, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 1, 1, 10]
]

start_pos_x = 0
start_pos_y = 0

def get_next_free_position(1):
    if map[start_pos_y][start_pos_x + 1] == 1:
        print("You are able to go right")
        return [start_pos_y, start_pos_x + 1]

    if map [start_pos_y + 1][start_pos_x] == 1:
        print("You are able to go down")
        return [start_pos_y + 1, start_pos_x]

next_free_position = get_next_free_position()
print("Next free position is:", next_free_position)
