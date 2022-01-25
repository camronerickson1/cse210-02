from game.card import Card


class Director:
    # We need to put comments here
    
    
    def __init__(self):
        """Initial method to set needed attributes"""

        self.is_playing= True
        self.score= 300
        self.current_card= Card()
        self.new_card= 0
        self.players_guess = ""

    def start_game(self):
        """Starts game by running the main loop."""
        while self.is_playing:
            self.get_inputs()
            self.do_outputs()

    def get_inputs(self):
        """Displays the current and gets user input"""

        #display the current card
        print(f"The card is: {self.current_card}")
        #ask user for their guess
        self.players_guess = input("Higher or lower? [h/l] ")

    def do_outputs(self):
        """Displays new_card's value.  Calls the change_score method.  Determines if the score has dropped to 0 and calls keep_playing method if >0.
        
            Args: self (Director): an instance of Director.
        """
        #get new card
        self.new_card = Card()
        #display new_card value
        print(f'The next card is: {self.new_card}') 
        #display new score
        print(f'Your score is: {self.change_score()}')
        self.is_playing == (self.score > 0)
        if self.is_playing:
            #call "keep_playing()"
            self.keep_playing()
        else:
            print("Sorry your score has reached 0.  Game Over.")
        

            
    def change_score(self):
        """Calculates and displays the current score based the players last guess.
        
            Args: self (Director): an instance of Director.
        """
        if (self.players_guess.lower() == 'h' and self.new_card > self.current_card) or(self.players_guess.lower() == 'l' and self.new_card < self.current_card):
            self.score+=100
        else:
            self.score -=75
        return self.score

    def keep_playing(self):
        # This method asks player if they want to play again
        # if they want to play again then set self.is_playing to be True, else set it False
        
        # Ask question if they want to keep playing and put into a temp variable
        player_input = input("Do you want to play again? [y/n]: ")

        # Set self.is_playing to be True or False based upon the y or n answer
        if player_input.lower() == "y":
            self.is_playing = True
        else:
            self.is_playing = False  # since they answer wasn't "y" assume it is "n" or an invalid response
            return # skip the last line in this method since they won't be playing anymore
       
        # If they want to play again, then the next round's "current_card" will be equal to
        # the current round's "new_card"
        self.current_card = self.new_card
