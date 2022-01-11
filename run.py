
game_size=0
def get_grid_size():
    global game_size
    while True:
        game_size=int(input("Enter grid size (8-15):"))
        if check_grid_input(game_size):
            print("Data is valid!")
            break
    return game_size

"""
Get game size - give option of 8-15 rows
"""
user_board = [[' '*game_size for x in range(game_size)]]
computer_board = [[' '*game_size for x in range(game_size)]]

def user_ship_locations():
    for i in range(5):
        print(f"Enter co-orderinates of ship number {i+1}")
        co_ord=input("Enter x,y co-ordinates of ship separated by a comma")
        

def check_grid_input(data):
    
    try:
        if data <8 or data >15:
            raise ValueError(
                f"Value needs to be between 8 & 15"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return data
    

def check_ship_input():
    pass

def computer_ship_locations():
    pass

def user_move():
    pass

def adjust_scores():
    pass

def main():
    get_grid_size()
    check_grid_input(game_size)

main()



