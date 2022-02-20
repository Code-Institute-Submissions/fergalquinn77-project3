import random
import gspread
from google.oauth2.service_account import Credentials

"""
    Battleships

    How it works:

    1. User inputs the grid size (min-max of 10 & 15)
    2. There will be 5 types of ships (10 ships in total)
        - Carrier (Size 5 squares) x 1 [C1]
        - Battleship (Size 4 squares) x 2 [B1, B2]
        - Destroyer (Size 3 squares) x 3 [D1, D2, D3]
        - Patrol Boat (Size 2 squares) x 4 [P1, P2, P3, P4]
    3. Fixed number of bombs - 50 
    4. User gives grid co-ordinates to drop bomb
    5. Object of game is to destroy all ships before running out of bombs

    Legend
    '~' = Water
    'S' = Part of ship
    '#' = Water hit by bomb
    'X' = Part of ship hit by bomb

"""

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("project-3-battleships")

num_ships = 10
bombs_left = 50
grid=[]
num_ships_sunk=0
grid_size = 10


def get_grid_size():
    global grid_size

    while True:
        try:
            grid_size = int(input("Please enter the grid size between 8 & 15: "))
            if grid_size <8 or grid_size > 15:
                continue
            print(grid_size)
            break
        except ValueError:
            print('\nYou did not enter a valid integer')

def create_initial_grid():
    
    for r in range(grid_size):
        row = []
        for c in range(grid_size):
            row.append("~")
        grid.append(row)
    

create_initial_grid()

def print_grid():
    pass

def position_ships(length,quatity):
    direction=random.choice(('north','south','east','west'))
    start_x=random.randint(0,grid_size-1)
    start_y=random.randint(0,grid_size-1)
    print(start_x)
    print(start_y)
    """ if check_if_position_possible(length,start_point,direction)==True:
        {
            pass
        } """

def check_if_position_possible(length,start_x,start_y,direction):

    """ check_ship_fits(length,start_x,start_y,direction)
    check_clear_water(length,start_x,start_y,direction)

    print('yes')
 """

def check_ship_fits(length,start_row,start_col,direction):
    if direction=='North':
        if(start_col-length>=-1):
            return True
        else:
            return False

    if direction=='South':
        if(start_col+length<=grid_size):
            return True
        else:
            return False

    if direction=='East':
        if(start_row+length<=grid_size):
            return True
        else:
            return False

    if direction=='West':
        if(start_row-length>=-1):
            return True
        else:
            return False
        

def check_clear_water(length,start_row,start_col,direction):
    
    if direction=='North':
        non_water=0
        for position in range(length):
            if grid[start_row-position][start_col]!='~':
                non_water+=1
        if non_water==0:
            return True
        else:
            return False
    
    if direction=='South':
        non_water=0
        for position in range(length):
            if grid[start_row+position][start_col]!='~':
                non_water+=1
        if non_water==0:
            return True
        else:
            return False
        

    if direction=='West':
        non_water=0
        for position in range(length):
            if grid[start_row][start_col-position]!='~':
                non_water+=1
        if non_water==0:
            return True
        else:
            return False

    if direction=='East':
        non_water=0
        for position in range(length):
            if grid[start_row][start_col+position]!='~':
                non_water+=1
        if non_water==0:
            return True
        else:
            return False
        

grid[9][9]='0'
x=check_clear_water(2,8,9,'South')
print(x)

def throw_bomb():
    pass

def check_ship_sunk():
    pass

def check_game_over():
    pass

def record_game_stats():
    pass



