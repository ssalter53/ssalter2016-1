# -*- coding: utf-8 -*-
import random
team_name = 'Brown Town'
strategy_name = 'Random'
strategy_description = 'randomly picks C and B'

def move(my_history, their_history, my_score, their_score):
    if random.randint(0,2) == 0:
        return "c"
    else:
        return "b"
