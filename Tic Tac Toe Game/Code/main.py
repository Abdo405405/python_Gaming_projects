from tabulate import tabulate
import shutil
import os 
import pyfiglet
from termcolor import colored


def clear_screen () : 
    os.system('cls' if os.name == 'nt' else "clear")

class Player : 
    def __init__(self ) -> None:
        self.__name = "" 
        self.__symbol = ""

    def choose_name(self,PlayerNumber):
        name = input(f"Player{PlayerNumber} , Enter Your Name (only Letters ): ").strip()
        while True : 
            if name.isalpha() : 
                self.__name = name
                break  
            else : 
                name=input("Erorr , Enter valid Name with only Letters : ")

    def choose_symbol (self) : 
        symbol = input(f"{self.__name} , Choose Your Symbol (Only 1 char ) :  ")
        while True : 
            if len(symbol) == 1 and not symbol.isnumeric() : 
                self.__symbol = symbol.upper() 
                break 
            else : 
                symbol=input("Erorr , Enter valid Symbol like x , o ,@ : ")
    @property
    def name(self) :
        return self.__name
    @name.setter
    def name (self ,value):
        self.__name = value
    @name.deleter 
    def name (self) :
        del self.__name
    
    @property
    def symbol(self) :
        return self.__symbol
    @name.setter
    def name (self ,value):
        self.__symbol = value
    @name.deleter 
    def name (self) :
        del self.__symbol

class Menu : 
    @staticmethod
    def display_start_menu () : 
         print("Welcome To Tec Tac Teo Game")
         print("1 - Start Game ")
         print("2 - Quit Game ")
         while True : 
            try : 
             choice = int(input("Enter Your Choice (1 or 2 ) : ").strip())
             while True : 
                 if choice == 1 or choice == 2 :
                     return choice
                 else : 
                     choice = input("Enter Valid Choice (1 or 2 ) : ")
            except ValueError : 
             print("Error : Invalid Input")
     
    @staticmethod
    def display_end_menu()  : 
         print("1 - restart Game ")
         print("2 - Quit Game ")
         choice = int(input("Enter Your Choice (1 or 2 ) : ").strip())
         while True : 
            if choice == 1 or choice == 2 :
                 return choice
            else : 
                choice = input("Enter Valid Choice (1 or 2 ) : ")

class Board : 
    def __init__(self) -> None:
        self.board = [ [f'{i}' , f'{i+1}' , f'{i+2}' ] for i in range(1 , 10 , 3 ) ]
        self.boardNumbers = set(range(1,10))

    def show_board(self) -> None:
        """Displays the current state of the board, centered in the terminal
        For Example 
        let say numbers represent terminal size and -- represent board to center board  we calculate terminal_size = 10 and board size = 2
        padding that suppose to add left = (10 -2 ) // 2 = 4 spaces
        1 2 3 4 5 6 7 8 9 10
        --
        ."""
        board_str = tabulate(self.board, tablefmt="heavy_grid")
        board_lines = board_str.split('\n')

        # Get terminal width
        terminal_width = shutil.get_terminal_size().columns

        # Calculate the maximum width of the board (longest line)
        max_board_width = max(len(line) for line in board_lines)

        # Calculate padding on the left to center the board               
        padding = (terminal_width - max_board_width) // 2

        # Print each line of the board with the padding
        for line in board_lines:
            print(' ' * padding + line) 
    
    def get_position (self , num) : 
        row = (num - 1) // 3
        col = (num-1) % 3 
        return row , col 
    
    def is_valid_choice (self , num) : 
        return num in self.boardNumbers and num > 0 
    
    def update_board (self ,name ,symbol):
        try : 
            num = int(input(f"{name} , Choose a cell (1-9) : ").strip())
            while True : 
                if self.is_valid_choice(num) : 
                    row , col = self.get_position(num)
                    self.board[row][col] =symbol 
                    self.boardNumbers.remove(num)
                    break 
                else : 
                    num = int(input("Invalid Number , Enter only A number from The Board : ").strip())
        except ValueError : 
            print("Please ,Enter A Valid Number")

    def reset_board (self) : 
        self.board = [ [f'{i}' , f'{i+1}' , f'{i+2}' ] for i in range(1 , 10 , 3 ) ]
        print(self.board)
        self.boardNumbers = set(range(1,10))

class GameLogic : 
    def __init__(self) -> None:
        self.players = [Player() , Player()]
        self.player_index = 0
        self.game_board = Board()
        self.menu = Menu()

    def setup_players (self): 
        print('-'*50,'\n')
        for idx,player in enumerate(self.players) :
            player.choose_name(PlayerNumber=idx+1)
            print("\n")
            player.choose_symbol()
            clear_screen()
    
    def play_turn(self ,player_index) :
        self.game_board.show_board()
        playerName = self.players[player_index].name
        symbol = self.players[player_index].symbol
        self.game_board.update_board(playerName ,symbol)
        clear_screen()


    def check_win (self) :
        symbol = (self.players[self.player_index].symbol)*3
        board = self.game_board.board
        size = len(board)
        vertical_pattern = ""
        horzintal_pattern=""
        for col in range(size) :  
            horzintal_pattern="".join(board[col])
            if horzintal_pattern ==symbol : 
                return True
                
            for row in range(size) : 
                vertical_pattern += board[row][col]
                if vertical_pattern ==symbol :
                    return True
                    
        vertical_pattern=""
        left_Diagonally  = board[0][0] + board[1][1] + board[2][2] 
        right_Diagonally = board[0][2] + board[1][1] + board[2][0]
        if left_Diagonally ==symbol or right_Diagonally ==symbol : 
            return True
        
        return False    
         
    def check_draw(self) : 
        return not self.game_board.boardNumbers
    
    def switch_player (self) : 
        self.player_index = 1 - self.player_index
    def play_game(self) : 
        while True : 
            self.play_turn(self.player_index)
            if self.check_win() or self.check_draw() : 
                if self.check_draw() :
                    print("No Winner !")
                else : 
                     print( colored(pyfiglet.figlet_format(f"{self.players[self.player_index].name} is winner" , font='slant'),color='red')) 
                     print("\n")

                choice=self.menu.display_end_menu()
                if choice == 1 : 
                    self.restart_game()
                else : 
                    self.Quit()
            self.switch_player()
    def restart_game(self) : 
        clear_screen()
        self.game_board.reset_board()
        self.player_index = 0
        self.start_game()

    def start_game (self) : 
        choice =self.menu.display_start_menu()
        if choice == 1 : 
            clear_screen()
            self.setup_players()
            self.play_game()

        else : 
            self.Quit()

    def Quit (self) : 
        clear_screen()
        print( colored(pyfiglet.figlet_format("Thank You For Gaming ! " , font='slant'),color='green')) 
        exit()

    


g = GameLogic () 
g.start_game()





         







