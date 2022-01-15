#Ariel Rosenthal
#11/27/2021
#Portfolio Project

#Note for TA: Sorry that my halfway point Google Doc explaining what I was planning to do was not
#very good... I decided to delete everything I had and restart from scratch because it was not
#working as expected. Thankfully I was able to get it to work now-- though it is much more complicated
#than before!

class HasamiShogiGame:
    def __init__(self):
        '''Constructor for the game hasami shogi. It will intialize the board with 0 and initialize the first player as BLACK'''

        # Initialize a 9x9 board with 0s
        self.board = [[0 for x in range(9)] for x in range(9)]
        # Initialize turn as BLACk
        self.turn = "BLACK"


    def initiate_board(self):
        '''This function will set the reds and blacks in respective rows and columns. Column 0 being red and Column 8 being blacks'''

        # Row 0 set to Reds and 8 set to blacks
        self.board[0] = ["R", "R", "R", "R", "R", "R", "R", "R", "R"]
        self.board[8] = ["B", "B", "B", "B", "B", "B", "B", "B", "B"]

    def print_board(self):
        '''This function will print the board on the console'''


        # Loops through the board to print 10 rows
        for x in range(10):
            # Checks if the row is 0, then prints numbers for first row
            if x==0:
                print(" ", end="  ")
                for y in range(9):
                    print(f"{y+1}",end="  ")
            # Else it will print the board
            else:
                # Prints alphabet for the first column to refer the board
                alpha = " abcdefghi"[x]
                print(f"{alpha}", end="  ")

                for z in range(9):
                    if self.board[x-1][z]==0:
                        print(f".", end="  ")
                    else:
                        print(f"{self.board[x-1][z]}", end="  ")
            print("")
        print("\n\n")

    def get_game_state(self):
        '''Returns game state as UNFINISHED, BLACK_WON or RED_WON.'''
        reds = 0
        blacks = 0

        # Loops through each portion of the board to count the players remaining
        for row in self.board:
            for col in row:
                if col=='R':
                    reds+=1
                elif col=='B':
                    blacks+=1

        # Returns the game state according to the game logic
        if blacks>reds:
            if reds<=1:
                return "BLACK_WON"
        elif reds>blacks:
            if blacks<=1:
                return "RED_WON"

        return "UNFINISHED"

    def get_active_player(self):
        '''Returns current active player'''
        return self.turn

    def change_player(self):
        '''Changes the player from black to red or from red to black'''


        if self.turn=="BLACK":
            self.turn="RED"
        elif self.turn=="RED":
            self.turn="BLACK"


    def get_num_captured_pieces(self,player):
        '''This function will get the number of captured pieces of the given player'''

        reds = 0
        blacks = 0
        # Following loop counts the number of reds and blacks remaining
        for row in self.board:
            for col in row:
                if col == 'R':
                    reds += 1
                elif col == 'B':
                    blacks += 1

        # Following lines will subtract the sum from 9 to get remaining players
        captured_reds = 9-reds
        captured_blacks = 9-blacks

        # Return according to parameter
        if player=="BLACK":
            return captured_blacks
        else:
            return captured_reds

    def make_move(self,from_loc,to_loc):
        '''This is the function that makes a move from a location to a given location for the current player'''


        # Following line converts the input string to proper row-col indexes for from location
        from_row_i = list("abcdefghi").index(from_loc[0].lower())
        from_col_i = int(from_loc[1])-1


        # Following line converts the input string to proper row-col indexes for to location
        to_row_i = list("abcdefghi").index(to_loc[0].lower())
        to_col_i = int(to_loc[1])-1

        # Gets current player
        current_player = self.get_active_player()[0]


        # Following lines check if the from and two have a same col/row to check whether the move is valid or not
        same_col_check = False
        same_row_check = False

        if from_row_i==to_row_i:
            same_row_check=True
        if from_col_i==to_col_i:
            same_col_check=True


        # Get game status
        game_status = self.get_game_state()


        # Following loop checks if there is a blocking piece between the from and to location
        check_valid_move = False
        direction_move  = ''
        if same_row_check:
            from_ = from_col_i
            to_ = to_col_i
            if to_<from_:
                for i in range(from_-1,to_,-1):
                    if self.board[from_row_i][i] != 0:
                        check_valid_move = True
                        break
                direction_move='L'
            else:
                for i in range(from_+1,to_+1):
                    if self.board[from_row_i][i] != 0:
                        check_valid_move = True
                        break
                direction_move='R'
        elif same_col_check:
            from_ = from_row_i
            to_ = to_row_i
            if to_<from_:
                for i in range(from_-1,to_,-1):
                    if self.board[i][from_col_i] != 0:
                        check_valid_move = True
                        break
                direction_move='U'
            else:
                for i in range(from_+1,to_+1):
                    if self.board[i][from_col_i] != 0:
                        check_valid_move = True
                        break
                direction_move='D'

        # Following lines would return false if any of the condition doesn't comply for the valid move
        if game_status != 'UNFINISHED':
            return game_status

        if self.board[from_row_i][from_col_i]!=current_player:
            return False
        elif self.board[to_row_i][to_col_i]!=0:
            return False
        elif same_col_check==False and same_row_check==False:
            return False

        elif check_valid_move!=False:
            return False
        else:

            # Following is the code if the move is valid

            # Following code is divided into two core logics
            # The first part of the following code will work if the movement is in the middle locations
            # The second part of the following code will work if the movement is in the sides/corners

            self.board[from_row_i][from_col_i] = 0
            self.board[to_row_i][to_col_i] = current_player

            # Following line calculates who the opponent is for future use
            if current_player=='B':
                opponent = 'R'
            else:
                opponent = 'B'
            # Logic to remove captured
            # check if corners
            if to_row_i!=0 and to_row_i!=8 and to_col_i!=0 and to_col_i!=8:
                # If the to location is not a corner row/column then following code will execute
                # The following code will check 4 directions for closures, up down left and right and then it will remove the pieces in between

                # Check left  line for closures
                found_opp = False
                if to_col_i!=0:
                    if self.board[to_row_i][to_col_i-1]==opponent:
                        found_opp=True
                    if found_opp:
                        found_closure = False
                        closure_index_row = -1
                        closure_index_col = -1
                        # Loops through the board to check if there is a closure with the same player letter
                        for i in range(to_col_i-1,-1,-1):
                            if self.board[to_row_i][i]==0:
                                break
                            elif self.board[to_row_i][i]==current_player:
                                found_closure=True
                                closure_index_row=to_row_i
                                closure_index_col=i
                                break
                        if found_closure:
                            self.capture(to_row_i,to_col_i,closure_index_row,closure_index_col)

                # Check right line for closures
                found_opp = False
                if to_col_i!=8:
                    if self.board[to_row_i][to_col_i + 1] == opponent:
                        found_opp = True
                    if found_opp:
                        found_closure = False
                        closure_index_row = -1
                        closure_index_col = -1
                        # Loops through the board to check if there is a closure with the same player letter
                        for i in range(to_col_i + 1, 9):
                            if self.board[to_row_i][i] == 0:
                                break
                            elif self.board[to_row_i][i] == current_player:
                                found_closure = True
                                closure_index_row = to_row_i
                                closure_index_col = i
                                break
                        if found_closure:
                            self.capture(to_row_i, to_col_i, closure_index_row, closure_index_col)

                # Check up line for closures
                found_opp = False
                if to_row_i!=0:
                    if self.board[to_row_i-1][to_col_i] == opponent:
                        found_opp = True
                    if found_opp:
                        found_closure = False
                        closure_index_row = -1
                        closure_index_col = -1
                        # Loops through the board to check if there is a closure with the same player letter
                        for i in range(to_row_i - 1, -1, -1):
                            if self.board[i][to_col_i] == 0:
                                break
                            elif self.board[i][to_col_i] == current_player:
                                found_closure = True
                                closure_index_row = i
                                closure_index_col = to_col_i
                                break
                        if found_closure:
                            self.capture(to_row_i, to_col_i, closure_index_row, closure_index_col)

                # Check down line for closures
                found_opp = False
                if to_row_i!=8:
                    if self.board[to_row_i+1][to_col_i] == opponent:
                        found_opp = True
                    if found_opp:
                        found_closure = False
                        closure_index_row = -1
                        closure_index_col = -1
                        # Loops through the board to check if there is a closure with the same player letter
                        for i in range(to_row_i + 1, 9):
                            if self.board[i][to_col_i] == 0:
                                break
                            elif self.board[i][to_col_i] == current_player:
                                found_closure = True
                                closure_index_row = i
                                closure_index_col = to_col_i
                                break
                        if found_closure:
                            self.capture(to_row_i, to_col_i, closure_index_row, closure_index_col)




            else:
                # Following is the code for the corners
                # Following code is divided into 4 parts where the location
                # can be the top row, bottom row, left most column or the right most column

                # Top row
                if to_row_i==0:
                    # Check down
                    found_opp = False
                    if self.board[to_row_i + 1][to_col_i] == opponent:
                        found_opp = True
                    if found_opp:
                        found_closure = False
                        closure_index_row = -1
                        closure_index_col = -1
                        # Loops through the board to check if there is a closure with the same player letter
                        for i in range(to_row_i + 1, 9):
                            if self.board[i][to_col_i] == 0:
                                break
                            elif self.board[i][to_col_i] == current_player:
                                found_closure = True
                                closure_index_row = i
                                closure_index_col = to_col_i
                                break
                        if found_closure:
                            self.capture(to_row_i, to_col_i, closure_index_row, closure_index_col)

                    # Check left

                    found_opp = False
                    try:
                        if self.board[to_row_i][to_col_i - 1] == opponent:
                            found_opp = True
                    except IndexError:
                        found_opp = True
                    if found_opp:
                        found_closure = False
                        found_break = False
                        closure_index_row = -1
                        closure_index_col = -1
                        # Loops through the board to check if there is a closure with the same player letter
                        for i in range(to_col_i - 1, -1, -1):
                            if self.board[to_row_i][i] == 0:
                                found_break=True
                                break
                            elif self.board[to_row_i][i] == current_player:
                                found_closure = True
                                closure_index_row = to_row_i
                                closure_index_col = i
                                break


                        if found_closure:
                            self.capture(to_row_i, to_col_i, closure_index_row, closure_index_col)
                        elif found_break==False:
                            # Loops through the board to check if there is a closure with the same player letter
                            for i in range(0,9):
                                if self.board[i][0] == 0:
                                    found_break = True
                                    break
                                elif self.board[i][0] == current_player:
                                    found_closure = True
                                    closure_index_row = i
                                    closure_index_col = 0
                                    break
                            if found_closure:
                                self.capture(to_row_i, to_col_i, closure_index_row, closure_index_col)

                    # Check right

                    found_opp = False
                    try:
                        if self.board[to_row_i][to_col_i + 1] == opponent:
                            found_opp = True
                    except IndexError:
                        found_opp = True
                    if found_opp:
                        found_closure = False
                        found_break = False
                        closure_index_row = -1
                        closure_index_col = -1
                        # Loops through the board to check if there is a closure with the same player letter
                        for i in range(to_col_i + 1, 9):
                            if self.board[to_row_i][i] == 0:
                                found_break = True
                                break
                            elif self.board[to_row_i][i] == current_player:
                                found_closure = True
                                closure_index_row = to_row_i
                                closure_index_col = i
                                break

                        if found_closure:
                            self.capture(to_row_i, to_col_i, closure_index_row, closure_index_col)
                        elif found_break == False:
                            # Loops through the board to check if there is a closure with the same player letter
                            for i in range(0, 9):
                                if self.board[i][8] == 0:
                                    found_break = True
                                    break
                                elif self.board[i][8] == current_player:
                                    found_closure = True
                                    closure_index_row = i
                                    closure_index_col = 8
                                    break
                            if found_closure:
                                self.capture(to_row_i, to_col_i, closure_index_row, closure_index_col)


                # Bottom row
                elif to_row_i==8:
                    # Check up
                    found_opp = False
                    if self.board[to_row_i - 1][to_col_i] == opponent:
                        found_opp = True
                    if found_opp:
                        found_closure = False
                        closure_index_row = -1
                        closure_index_col = -1
                        # Loops through the board to check if there is a closure with the same player letter
                        for i in range(to_row_i - 1, -1, -1):
                            if self.board[i][to_col_i] == 0:
                                break
                            elif self.board[i][to_col_i] == current_player:
                                found_closure = True
                                closure_index_row = i
                                closure_index_col = to_col_i
                                break
                        if found_closure:
                            self.capture(to_row_i, to_col_i, closure_index_row, closure_index_col)


                    # Check left

                    found_opp = False
                    try:
                        if self.board[to_row_i][to_col_i - 1] == opponent:
                            found_opp = True
                    except IndexError:
                        found_opp = True
                    if found_opp:
                        found_closure = False
                        found_break = False
                        closure_index_row = -1
                        closure_index_col = -1
                        # Loops through the board to check if there is a closure with the same player letter
                        for i in range(to_col_i - 1, -1, -1):
                            if self.board[to_row_i][i] == 0:
                                found_break = True
                                break
                            elif self.board[to_row_i][i] == current_player:
                                found_closure = True
                                closure_index_row = to_row_i
                                closure_index_col = i
                                break

                        if found_closure:
                            self.capture(to_row_i, to_col_i, closure_index_row, closure_index_col)
                        elif found_break == False:

                            for i in range(8,-1,-1):
                                if self.board[i][0] == 0:
                                    found_break = True
                                    break
                                elif self.board[i][0] == current_player:
                                    found_closure = True
                                    closure_index_row = i
                                    closure_index_col = 0
                                    break
                            if found_closure:
                                self.capture(to_row_i, to_col_i, closure_index_row, closure_index_col)

                    # Check right
                    found_opp = False
                    try:
                        if self.board[to_row_i][to_col_i + 1] == opponent:
                            found_opp = True
                    except IndexError:
                        found_opp = True
                    if found_opp:
                        found_closure = False
                        found_break = False
                        closure_index_row = -1
                        closure_index_col = -1
                        # Loops through the board to check if there is a closure with the same player letter
                        for i in range(to_col_i + 1, 9):
                            if self.board[to_row_i][i] == 0:
                                found_break = True
                                break
                            elif self.board[to_row_i][i] == current_player:
                                found_closure = True
                                closure_index_row = to_row_i
                                closure_index_col = i
                                break

                        if found_closure:
                            self.capture(to_row_i, to_col_i, closure_index_row, closure_index_col)
                        elif found_break == False:
                            # Loops through the board to check if there is a closure with the same player letter
                            for i in range(8,-1,-1):
                                if self.board[i][8] == 0:
                                    found_break = True
                                    break
                                elif self.board[i][8] == current_player:
                                    found_closure = True
                                    closure_index_row = i
                                    closure_index_col = 0
                                    break
                            if found_closure:
                                self.capture(to_row_i, to_col_i, closure_index_row,
                                             closure_index_col)

                # Top column
                elif to_col_i==0:
                    # Check right
                    found_opp = False
                    if self.board[to_row_i][to_col_i + 1] == opponent:
                        found_opp = True
                    if found_opp:
                        found_closure = False
                        closure_index_row = -1
                        closure_index_col = -1
                        # Loops through the board to check if there is a closure with the same player letter
                        for i in range(to_col_i + 1, 9):
                            if self.board[to_row_i][i] == 0:
                                break
                            elif self.board[to_row_i][i] == current_player:
                                found_closure = True
                                closure_index_row = to_row_i
                                closure_index_col = i
                                break
                        if found_closure:
                            self.capture(to_row_i, to_col_i, closure_index_row, closure_index_col)


                    #Check Up

                    found_opp = False
                    try:
                        if self.board[to_row_i - 1][to_col_i] == opponent:
                            found_opp = True
                    except IndexError:
                        found_opp = True
                    if found_opp:
                        found_break = False
                        found_closure = False
                        closure_index_row = -1
                        closure_index_col = -1
                        # Loops through the board to check if there is a closure with the same player letter
                        for i in range(to_row_i - 1, -1, -1):
                            if self.board[i][to_col_i] == 0:
                                found_break=True
                                break
                            elif self.board[i][to_col_i] == current_player:
                                found_closure = True
                                closure_index_row = i
                                closure_index_col = to_col_i
                                break
                        if found_closure:
                            self.capture(to_row_i, to_col_i, closure_index_row, closure_index_col)
                        elif found_break == False:

                            for i in range(0, 9):
                                if self.board[0][i] == 0:
                                    found_break = True
                                    break
                                elif self.board[0][i] == current_player:
                                    found_closure = True
                                    closure_index_row = 0
                                    closure_index_col = i
                                    break
                            if found_closure:
                                self.capture(to_row_i, to_col_i, closure_index_row,
                                             closure_index_col)

                    #Check Down
                    found_opp = False
                    try:
                        if self.board[to_row_i + 1][to_col_i] == opponent:
                            found_opp = True
                    except IndexError:
                        found_opp = True
                    if found_opp:
                        found_break = False
                        found_closure = False
                        closure_index_row = -1
                        closure_index_col = -1
                        # Loops through the board to check if there is a closure with the same player letter
                        for i in range(to_row_i + 1,9):
                            if self.board[i][to_col_i] == 0:
                                found_break = True
                                break
                            elif self.board[i][to_col_i] == current_player:
                                found_closure = True
                                closure_index_row = i
                                closure_index_col = to_col_i
                                break
                        if found_closure:
                            self.capture(to_row_i, to_col_i, closure_index_row, closure_index_col)
                        elif found_break == False:

                            for i in range(0, 9):
                                if self.board[8][i] == 0:
                                    found_break = True
                                    break
                                elif self.board[8][i] == current_player:
                                    found_closure = True
                                    closure_index_row = 8
                                    closure_index_col = i
                                    break
                            if found_closure:
                                self.capture(to_row_i, to_col_i, closure_index_row,closure_index_col)

                # Bottom column
                elif to_col_i==8:
                    # Check Left
                    found_opp = False
                    if self.board[to_row_i][to_col_i - 1] == opponent:
                        found_opp = True
                    if found_opp:
                        found_closure = False
                        closure_index_row = -1
                        closure_index_col = -1
                        # Loops through the board to check if there is a closure with the same player letter
                        for i in range(to_col_i - 1, -1, -1):
                            if self.board[to_row_i][i] == 0:
                                break
                            elif self.board[to_row_i][i] == current_player:
                                found_closure = True
                                closure_index_row = to_row_i
                                closure_index_col = i
                                break
                        if found_closure:
                            self.capture(to_row_i, to_col_i, closure_index_row, closure_index_col)

                    # Check Up
                    found_opp = False
                    try:
                        if self.board[to_row_i - 1][to_col_i] == opponent:
                            found_opp = True
                    except IndexError:
                        found_opp = True
                    if found_opp:
                        found_break = False
                        found_closure = False
                        closure_index_row = -1
                        closure_index_col = -1
                        # Loops through the board to check if there is a closure with the same player letter
                        for i in range(to_row_i - 1, -1, -1):
                            if self.board[i][to_col_i] == 0:
                                found_break = True
                                break
                            elif self.board[i][to_col_i] == current_player:
                                found_closure = True
                                closure_index_row = i
                                closure_index_col = to_col_i
                                break
                        if found_closure:
                            self.capture(to_row_i, to_col_i, closure_index_row, closure_index_col)
                        elif found_break == False:

                            for i in range(8,-1,-1):
                                if self.board[0][i] == 0:
                                    found_break = True
                                    break
                                elif self.board[0][i] == current_player:
                                    found_closure = True
                                    closure_index_row = 0
                                    closure_index_col = i
                                    break
                            if found_closure:
                                self.capture(to_row_i, to_col_i, closure_index_row,
                                             closure_index_col)

                    # Check Down
                    found_opp = False
                    try:
                        if self.board[to_row_i + 1][to_col_i] == opponent:
                            found_opp = True
                    except IndexError:
                        found_opp = True
                    if found_opp:
                        found_break = False
                        found_closure = False
                        closure_index_row = -1
                        closure_index_col = -1
                        for i in range(to_row_i + 1, 9):
                            if self.board[i][to_col_i] == 0:
                                found_break = True
                                break
                            elif self.board[i][to_col_i] == current_player:
                                found_closure = True
                                closure_index_row = i
                                closure_index_col = to_col_i
                                break
                        if found_closure:
                            self.capture(to_row_i, to_col_i, closure_index_row, closure_index_col)
                        elif found_break == False:

                            for i in range(8,-1,-1):
                                if self.board[8][i] == 0:
                                    found_break = True
                                    break
                                elif self.board[8][i] == current_player:
                                    found_closure = True
                                    closure_index_row = 8
                                    closure_index_col = i
                                    break
                            if found_closure:
                                self.capture(to_row_i, to_col_i, closure_index_row, closure_index_col)


        self.change_player()

    def capture(self,from_row_i,from_col_i,to_row_i,to_col_i):
        '''This function will capture the pieces of the opponent between the from location to the to location and remove the pieces from the board'''

        # Following code is divided into two main logics
        # The first logic is for straight row or straight column capture
        # The second logic deals with the corners where it removes the players from the corners

        if from_row_i==to_row_i:
            # Following is the logic for the case when row is same

            if to_col_i<from_col_i:
                for i in range(to_col_i+1,from_col_i):
                    self.board[from_row_i][i]=0
            else:
                for i in range(from_col_i + 1, to_col_i):
                    self.board[from_row_i][i] = 0
        elif from_col_i==to_col_i:
            # Following is the logic for the case when col is same

            if to_row_i<from_row_i:
                for i in range(to_row_i+1,from_row_i):
                    self.board[i][from_col_i]=0

            else:
                for i in range(from_row_i+1,to_row_i):
                    self.board[i][from_col_i]=0
        else:
            # Corners part
            # Following code is divided into 4 parts
            # One for the top row
            # One for the bottom row
            # One for the left column
            # One for the right Columns


            # for the top row
            if from_row_i==0:
                if to_col_i==0:
                    for i in range(from_col_i-1,-1,-1):
                        self.board[0][i]=0
                    for i in range(0,to_row_i):
                        self.board[i][0]=0
                elif to_col_i==8:
                    for i in range(from_col_i+1,9):
                        self.board[0][i] = 0
                    for i in range(0, to_row_i):
                        self.board[i][8] = 0
            # for the bottom row
            elif from_row_i==8:
                if to_col_i==0:
                    for i in range(from_col_i-1,-1,-1):
                        self.board[8][i]=0
                    for i in range(8,to_row_i,-1):
                        self.board[i][0]=0

                elif to_col_i==8:
                    for i in range(from_col_i+1,9):
                        self.board[8][i] = 0
                    for i in range(8, to_row_i,-1):
                        self.board[i][8] = 0

            # for the left column
            elif from_col_i==0:
                if to_row_i==0:
                    for i in range(from_row_i-1,-1,-1):
                        self.board[i][0]=0
                    for i in range(0,to_col_i):
                        self.board[0][i]=0
                elif to_row_i==8:
                    for i in range(from_row_i+1, 9):
                        self.board[i][0] = 0
                    for i in range(0, to_col_i):
                        self.board[8][i] = 0

            # for the right Columns
            elif from_col_i==8:
                if to_row_i == 0:
                    for i in range(from_row_i-1,-1,-1):
                        self.board[i][8]=0
                    for i in range(8,to_col_i,-1):
                        self.board[0][i]=0

                elif to_row_i == 8:
                    for i in range(from_row_i+1,9):
                        self.board[i][8]=0
                    for i in range(8,to_col_i,-1):
                        self.board[8][i]=0


    def get_square_occupant(self,loc):
        '''This function will return the occupant of the given location'''


        row_i = list("abcdefghi").index(loc[0].lower())
        col_i = int(loc[1]) - 1
        if self.board[row_i][col_i]=='R':
            return "RED"
        elif self.board[row_i][col_i]=='B':
            return "BLACK"
        else:
            return "NONE"

class PlayGame:
    def __init__(self):
        pass

    def game(self):
        '''This function will allow the user to play the game by inputting the locations in the console. It will use the class HasamiShogiGame'''

        b = HasamiShogiGame()
        b.initiate_board()
        valid_moves = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7', 'i8', 'i9']

        game_state = b.get_game_state()
        while game_state=='UNFINISHED':
            b.print_board()
            print(f"TURN       : {b.get_active_player()}")
            print(f"GAME STATE : {b.get_game_state()}")

            from_loc = input("Enter from location : ")
            while from_loc not in valid_moves:
                print("Incorrect input! Enter correct location.")
                from_loc = input("Enter from location : ")

            to_loc = input("Enter to location   : ")
            while to_loc not in valid_moves:
                print("Incorrect input! Enter correct location.")
                to_loc = input("Enter to location   : ")

            b.make_move(from_loc,to_loc)
            game_state = b.get_game_state()

    def test_case(self):
        '''This function is the Test case for HasamiShogiGame class'''


        game = HasamiShogiGame()
        move_result = game.make_move('i6', 'e3')
        print("Move Result   : ",move_result)
        print("Active Player : ",game.get_active_player())
        print("Occupant (a4) : ",game.get_square_occupant('a4'))
        print("Game State    : ",game.get_game_state())


if __name__ == '__main__':

    # Main code block that runs the game and the test case

    game = PlayGame()

    print("TEST CASE :")
    print("---------------")
    game.test_case()
    print("---------------")

    print()

    game.game()