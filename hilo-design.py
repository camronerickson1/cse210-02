"""Classes needed and possible methods: (new file for each class)

Camron: Director attributes, start_game, get_inputs, README file.
Monika: do_outputs, change_score.
Jonathan: keep_playing, Card(), main file

Director

    Attributes:
        is_playing=boolean
        score=int
        current_card
        new_card


    Methods:
        start game:
            call:
                get_inputs
                do_outputs

        get_inputs:
            display current_card
            player_guess
            
            
        do_outputs:
            new_card = Card()
            display new_card value
            call "change_score()"
            call "keep_playing()"
            

        change_score:
            update the score
            display score

        keep_playing:
            ask question
            change "is_playing" if needed
            set new card to current card

Card
    create_card  # changed this to be one word create_card
"""