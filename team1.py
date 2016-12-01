####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Jaysen and Collin' # Only 10 chars displayed.
strategy_name = 'Revenge'
strategy_description = 'This strategy will begin with a betrayal. It will then collude in the remaining moves UNLESS the opponent betrays twice in a row. If the opponent consecutively betrays twice at anytime past the first move, the user will betray as well for the remainder of the round.'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
 
    if (my_history)==0:
        return 'b'
    if (my_history)==1:
        return 'c'
    if (my_history) == 3:
        if 'b' in their_history:
            return 'b'
        else:
            return 'c'
    

