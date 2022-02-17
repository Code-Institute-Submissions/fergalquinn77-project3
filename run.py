import random
import gspread
from google.oauth2.service_account import Credentials

"""
    Battleships

    How it works:

    1. User inputs the grid size (min-max of 10 & 15)
    2. There will be 5 types of ships (10 ships in total)
        - Carrier (Size 5 squares) x 1
        - Battleship (Size 4 squares) x 2
        - Destroyer (Size 3 squares) x 3
        - Patrol Boat (Size 2 squares) x 4
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
grid_display=[[]]
grid_hide=[[]]
num_ships_sunk=0


def get_grid_size():
    
    pass

def print_grid():
    pass

def position_ships():
    pass

def throw_bomb():
    pass

def check_ship_sunk():
    pass

def check_game_over():
    pass

def record_game_stats():
    pass



