from .card import Card  # Jonathan put the dot in front of card, we can remove it if it causes problems
                        # but for me it was needed to see that it is in the same directory


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
        # Jonathan working on this one, still have to add to this
        # Need to put comments here

        return # this will be removed later
