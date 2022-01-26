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

        

    def create_card(self):
        """Generates a new random face value of the card ranging from 1 to 13.
        Returns the number to the source the called it.
        
        Args:
            self (Card): An instance of Card.
        """
        return random.randint(1,13)
       
        

        
        