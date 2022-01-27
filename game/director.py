from game.card import Card   # Imports the Card class in the game directory, in the card.py file


class Director:
    # This class runs the Hi/Lo game. It gathers input from the user, outputs information to the user,
    # processes the input to make decisions such as whether the game should continue.
    # This class also calls the Card class.
    
    
    def __init__(self):
        """Initial method to set needed attributes"""

        self.is_playing= True  # Start off with the user wanting to keep playing
        self.score= 300  # According to specs of the game, the user starts with 300 points
        self.current_card= Card().create_card() # Uses the Card class to get an initial card value between 1 and 13
        self.new_card= 0
        self.players_guess = ""

    def start_game(self):
        """Starts game by running the main loop."""
        # While is_playing is True, keep gathering inputs from the user and doing outputs to the user

        while self.is_playing:
            self.get_inputs()
            self.do_outputs()

    def get_inputs(self):
        """Displays the current and gets user input"""
        cond=1
        #Display the current card
        print(f"The card is: {self.current_card}")
        # Ask user for their guess, if they think the next card will be higher or lower
        guess = input("Higher or lower? [h/l] ")
        while cond==1:
            if (guess.lower() == "h" or guess.lower() == "l"):
                self.players_guess = guess
                cond=0   
            else:
                guess = input("Please enter h for higher or l for lower. ")
                cond=1




    def do_outputs(self):
        """Displays new_card's value.  Calls the change_score method.  Determines if the score has dropped to 0 and calls keep_playing method if >0.
        
            Args: self (Director): an instance of Director.
        """
        # Get new card value by using the Card class
        self.new_card = Card().create_card()
        #Display new_card value
        print(f'The next card is: {self.new_card}') 
        #Display new score
        print(f'Your score is: {self.change_score()}')
        self.is_playing == (self.score > 0)
        if self.is_playing:
            #Call "keep_playing()"
            self.keep_playing()
        else:
            # End the game if the score has reached 0
            print("Sorry your score has reached 0.  Game Over.")
        

            
    def change_score(self):
        """Calculates and displays the current score based the players last guess.
        
            Args: self (Director): an instance of Director.
        """
        # If they guessed correctly, give them 100 points
        if (self.players_guess.lower() == 'h' and self.new_card > self.current_card) or(self.players_guess.lower() == 'l' and self.new_card < self.current_card):
            self.score+=100
        
        # If they didn't guess correctly, subtract 75 points
        else:
            self.score -=75
        return self.score

    def keep_playing(self):
        # This method asks player if they want to play again
        # if they want to play again then set self.is_playing to be True, else set it False
        # This also has a loop to keep asking if they want to play again until they give us a valid y or n
        
        # If their score is 0 or less don't bother asking them if they want to keep playing and end the game

        if self.score <=0:
            print(f"Thanks for playing! Your final score is {self.score}")
            self.is_playing = False
            return

        # Initialize player_input to allow us to get into the player input loop
        player_input = ""
        # Keep looping to gather player input until they give us a valid answer of y or n
        while player_input.lower != "y": 
            # Ask question if they want to keep playing and put into a temp variable
            player_input = input("Do you want to play again? [y/n]: ")
            print()

            # if the player wants to quit, end the game with a nice message and the final score
            if player_input.lower() == "n":
                self.is_playing = False
                print(f"Thanks for playing! Your final score is {self.score}")
                # exit the loop by returning since they don't want to play anymore 
                return

            # if the player wants to keep going, set is_playing to True and retain the latest card value in current_card
            elif player_input.lower() == "y":
                self.is_playing = True
                self.current_card = self.new_card
                return
            
            # Since they didn't give us a y or n, tell the user to use a valid response and keep looping until we get a
            # valid response
            else:
                print("Please enter a valid option.")
