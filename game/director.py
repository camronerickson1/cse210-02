from card import Card


class Director:
    # We need to put comments here
    
    
    def __init__(self):
        """Initial method to set needed attributes"""

        self.is_playing= True
        self.score= 0
        self.current_card= Card()
        self.new_card= Card()

    def start_game(self):
        """Starts game by running the main loop."""
        while self.is_playing:
            self.get_inputs()
            self.do_outputs()



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
