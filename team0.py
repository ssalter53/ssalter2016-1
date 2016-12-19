# -*- coding: utf-8 -*-
import random
team_name = 'Brown Town'
strategy_name = 'B and C for x amount of sets”'
strategy_description = 'Alternating b and c for 1 set of 10 iterations(ex.ccbbccbbcc)'

def move(my_history, their_history, my_score, their_score):
    if random.randint(0,2) == 0:
        return "c"
    else:
        return "b"
