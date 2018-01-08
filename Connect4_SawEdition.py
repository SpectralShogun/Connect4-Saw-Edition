import sys
import random

with open('WallofSurvivers.txt', 'w') as f:
    read_data = f.read()
    f.closed


print ("     *Billy*\n==================")
print ("I want to play a game. As you can see, there is a automated contraption with metal spikes attached to your head.")
print ("The table in front of you is a stationary advanced super computer known as the Spectral Atlas F0-E")
print ("I know that you are one with an incredible mind, if you can beat SAFE in Connect4 the contraption will automatically deactivate and can safely be removed")
print ("But do be careful, if you lose then you'll be one less genius to care about.")

def winner(board):
    """This function accepts the Connect 4 board as a parameter.  
If there is no winner, the function will return the empty string "".  
If the user has won, it will return 'X', and if the computer has
won it will return 'O'."""

# Check rows for winner
    for row in range(6):
        for col in range(3):
            if (board[row][col] == board[row][col + 1] == board[row][col + 2] ==\
                board[row][col + 3]) and (board[row][col] != " "):
                    return board[row][col]

# Check columns for winner
    for col in range(6):
        for row in range(3):
            if (board[row][col] == board[row + 1][col] == board[row + 2][col] ==\
                board[row + 3][col]) and (board[row][col] != " "):
                    return board[row][col]
    
    # Check diagonal (top-left to bottom-right) for winner
    
    for row in range(3):
        for col in range(4):
            if (board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] ==\
                board[row + 3][col + 3]) and (board[row][col] != " "):
                    return board[row][col]
    
    
    # Check diagonal (bottom-left to top-right) for winner
    
    for row in range(5, 2, -1):
        for col in range(3):
            if (board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] ==\
                board[row - 3][col + 3]) and (board[row][col] != " "):
                    return board[row][col]
    
   # No winner: return the empty string
        return ""

def display_board(board):

    print ("   1   2   3   4    5   6   7")
    print ("1: " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " | " + board[0][3] + " | " + board[0][4] + " | " + board[0][5] + " | " + board[0][6] + " | " + board[0][7])
    print ("  ---+---+---+---+---+---+---")
    print ("2: " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " | " + board[1][3] + " | " + board[1][4] + " | " + board[1][5] + " | " + board [1][6] + " | " + board [1][7]) 
    print ("  ---+---+---+---+---+---+---+")
    print ("3: " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " | " + board[2][3] + " | " + board [2][4] + " | " + board [2][5] + " | " + board [2][6] + " | " + board [2][7])
    print ("  ---+---+---+---+---+---+---+")
    print ("4: " + board[3][0] + " | " + board[3][1] + " | " + board[3][2] + " | " + board[3][3] + " | " + board [3][4] + " | " + board [3][5] + " | " + board [3][6] + " | " + board [3][7])
    print ("  ---+---+---+---+---+---+---+")
    print ("5: " + board[4][0] + " | " + board[4][1] + " | " + board[4][2] + " | " + board[4][3] + " | " + board [4][4] + " | " + board [4][5] + " | " + board [4][6] + " | " + board [4][7])
    print ("  ---+---+---+---+---+---+---+")
    print ("6: " + board[5][0] + " | " + board[5][1] + " | " + board[5][2] + " | " + board[5][3] + " | " + board [5][4] + " | " + board [5][5] + " | " + board [5][6] + " | " + board [5][7])
    print 



def make_user_move(board):

    try:    
        valid_move = False
        while not valid_move:
            col = eval(input("What col would you like to move to (1-7):"))
            for row in range (6,0,-1):
                if (1 <= row <= 6) and (1 <= col <= 7) and (board[row-1][col-1] == " "):
                    board[row-1][col-1] = 'X'
                    valid_move = True
                    break
        else:
            print ("Sorry, invalid square. Please try again!\n")

    except NameError:
        print ("Only numbers are allowed.")

    except IndexError:
        print ("You can only select columns from (1-7), and rows from (1-6).")

def make_computer_move(board):

        valid_move = False
        while not valid_move:
            col = random.randint(1,7)
            for row in range (6,0,-1):
                if (1 <= row <= 6) and (1 <= col <= 7) and (board[row-1][col-1] == " "):
                    board[row-1][col-1] = 'O'
                    valid_move = True
                    break
        if sys.hexversion < 0x3000000:
            inp = raw_input
        else:
            inp = input

def get_int(prompt):
    while True:
        try:
            return int(prompt)
        except ValueError:
            pass

        HEIGHT = get_int(6)
        WIDTH  = get_int(6)


def main():


    free_cells = 42
users_turn = True
count = 1
ttt_board = [ [ " ", " ", " ", " ", " ", " "," ", " "], [ " ", " ", " ", " ", " "," ", " ", " "], [ " ", " ", " ", " ", " ", " ", " ", " "], [ " ", " ", " ", " ", " ", " ", " ", " "], [ " ", " ", " ", " ", " ", " ", " ", " "], [ " ", " ", " ", " ", " ", " ", " ", " "] ]

print ("")
print ("--SAFE--")
print ("Hello, I am a Spectral Atlas Type F0-E. You can call me SAFE for short, I will be your opponent. ")
print ("I am fully aware what you are capable of, but I am an ASC and this will be your trial of life and death\n")

choice = input("Would you like to go first?" +' y or n')

if (choice == 'y' or choice =='Y'):
    users_turn = True


elif (choice == 'n' or choice =='N') :
    users_turn = False        

              

else:
    print ('invalid input')

free_cells=42

while not winner(ttt_board) and (free_cells > 0):
    display_board(ttt_board)
    if users_turn:
        make_user_move(ttt_board)
        users_turn = not users_turn
    else:
        make_computer_move(ttt_board)
        users_turn = not users_turn
    free_cells -= 1

print ("\n(List of who survived) \n")


class wall_of_survivers:
    def out(self):


        s = wall_of_survivers()
        s.close()

        wall_of_survivers = open("WallofSurvivers.txt", 'a')

        name = input("Enter your name: ")
        wall_of_survivers.write(name+ '\n')
        print ("Your name has been added to the Wall of Survivers!")
        
        wall_of_survivers.close()

wall_of_survivers=open("WallofSurvivers.txt", 'r')
for name in wall_of_survivers:
    print (str(count) + ".", name)
    print ()
    count += 1
    
wall_of_survivers.close()    



    #display_board(ttt_board)
if (winner(ttt_board) == 'X'):
    print ("Good game, you have proven that your a force to be reckoned with.")
    print ("\n*CLICK CLICK* \n ")
    print ("I have disabled the locking mechanism as well as the fail-safe of the contraption, you may leave unscathed")
    print ("**Your name will now be added to the Wall of Survivers!**")

    wall_of_survivers = open("WallofSurvivers.txt", 'a')
    name = input("Enter your name: ")
    wall_of_survivers.write(name+ '\n')
    print ("Your name has been added to the Wall of Survivers!")

    wall_of_survivers.close()


    if (winner(ttt_board) == 'O'):
        print ("NO, NOOOOO! *Crunch*")
        print ("\nGAME OVER")
    else:
        print ("Stalemate!")
        print ("\nGAME OVER \n")

#start the game

main()
    
    
