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
grid_size = 12
ship_sizes = {'c1':5,'b1':4,'b2':4,'d1':3,'d2':3,'d3':3,'p1':2,'p2':2,'p3':2,'p4':2}
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
test_mode=False

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



def print_grid(grid):
    for i in range(grid_size):
            print(i+1, grid[i])

def print_grid_display(grid):
    global alphabet
    alphabet = alphabet[0: grid_size]

    for row in range(grid_size):
        print(alphabet[row], end=") ")
        for col in range(len(grid[row])):
            if len(grid[row][col]) > 1:
                if test_mode:
                    print(grid[row][col], end=" ")
                else:
                    print("~", end=" ")
            else:
                print(grid[row][col], end=" ")
        print("")

    print("  ", end=" ")
    for i in range(len(grid[0])):
        print(str(i), end=" ")
    print("")


    
def check_ship_fits(length,start_row,start_col,direction):

    if direction=='north':
        if(start_row-(length-1)>=0):
            return check_clear_water(length,start_row,start_col,direction)
        else:
            return False

    if direction=='south':
        if(start_row+(length-1)<=grid_size-1):
            return check_clear_water(length,start_row,start_col,direction)
        else:
            return False

    if direction=='east':
        if(start_col+(length-1)<=grid_size-1):
            return check_clear_water(length,start_row,start_col,direction)
        else:
            return False

    if direction=='west':
        if(start_col-(length-1)>=0):
            return check_clear_water(length,start_row,start_col,direction)
        else:
            return False
        

def check_clear_water(length,start_row,start_col,direction):

    
    if direction=='north':
        non_water=0
        for position in range(length):
            if grid[start_row-position][start_col]!='~':
                non_water+=1
        if non_water==0:
            return True
        else:
            return False
    
    if direction=='south':
        non_water=0
        for position in range(length):
            if grid[start_row+position][start_col]!='~':
                non_water+=1
        if non_water==0:
            return True
        else:
            return False
    
    if direction=='west':
        non_water=0
        for position in range(length):
            if grid[start_row][start_col-position]!='~':
                non_water+=1        
        if non_water==0:
            return True
        else:
            return False

    if direction=='east':
        non_water=0
        for position in range(length):
            if grid[start_row][start_col+position]!='~':
                non_water+=1
        if non_water==0:
            return True
        else:
            return False

def position_ships(length,boat):
    
    position_ship_possible=False

    while position_ship_possible==False:
        direction=random.choice(('north','south','east','west'))
        start_row=random.randint(0,grid_size-1)
        start_col=random.randint(0,grid_size-1)
        position_ship_possible=check_ship_fits(length,start_row,start_col,direction)
    
    place_ship(length,start_row,start_col,direction,boat)
    

def place_ship(length,start_row,start_col,direction,boat):
    if(direction=='north'):
        for position in range(length):
            grid[start_row-position][start_col]=boat
    elif(direction=='south'):
        for position in range(length):
            grid[start_row+position][start_col]=boat
    elif(direction=='east'):
        for position in range(length):
            grid[start_row][start_col+position]=boat
    elif(direction=='west'):
        for position in range(length):
            grid[start_row][start_col-position]=boat        


def position_ships_on_grid():
    for key,value in ship_sizes.items():
        position_ships(value,key)

position_ships_on_grid()
print_grid_display(grid)


def get_bomb():
    global alphabet
    alphabet = alphabet[0: grid_size]
    within_grid=False
    while within_grid==False:
        position_bomb = input("Enter row (A-J) and column (0-9) such as G7: ")
        position_bomb = position_bomb.upper()
        if len(position_bomb) <= 0 or len(position_bomb) > 2:
            print("Error: Please enter only one row and column such as A3")
            continue
        row = position_bomb[0]
        col = position_bomb[1]
        if (not row.isalpha() or not col.isnumeric()):
            print("Error: Invalid entry")
        col=int(col)
        if (row not in alphabet) or (not 0<=col<=grid_size-1):
            print("Error: Your choice was off the grid")
            continue
        row = alphabet.find(row)
        if (grid[row][col]=="#" or grid[row][col]=="X"):
            print("Error: You have already thrown a bomb here")
            continue
        if (grid[row][col]=="~" or len(grid[row][col])==2):
            within_grid=True
        
    print(row, col)

get_bomb()

def check_ship_sunk():
    pass

def check_game_over():
    pass

def record_game_stats():
    pass



