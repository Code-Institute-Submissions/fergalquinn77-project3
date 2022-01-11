
game_size=int(input("Enter grid size (8-15):"))
"""
Get game size - give option of 8-15 rows
"""
user_board = [[' '*game_size for x in range(game_size)]]
computer_board = [[' '*game_size for x in range(game_size)]]

def user_ship_locations():
    for i in range(game_size):
        print(f"Enter co-orderinates of ship number {i+1}")
        co_ord=input("Enter x,y co-ordinates of ship separated by a comma")
        print(co_ord)

def check_grid_input():
    pass

def check_ship_input():
    pass

def computer_ship_locations():
    pass

def user_move():
    pass

def adjust_scores():
    pass

user_ship_locations()



