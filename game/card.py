import random


class Card:
    """A deck of cards with face values ranging from 1 to 13.

    The responsibility of Card is to deal a card and identify the face value of that card
   
    Attributes:
        value (int): The face value of the card.
    """

    def __init__(self):
        """Constructs a new instance of Card. Possible values will range from 1 to 13.

            Args:
                self (Card): An instance of Card. 
            """

        # the initial value of the card
        self.value = 0 # not sure if we really need this? We can delete if we end up not needing it.
        

    def create_card(self):
        """Generates a new random face value of the card ranging from 1 to 13.
        
        Args:
            self (Card): An instance of Card.
        """
        # Setting self.value to be some random integer between 1 and 13.
        self.value = random.randint(1, 13)
       
        

        
        