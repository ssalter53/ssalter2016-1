####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Best Crew' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'

import random
        
#betray every turn
def straight_bs():
    return 'b'

    #c-b-b

def cbb(my_history):
    if len(my_history)==0:
        return 'c'
    elif len(my_history)%3==0:
        return 'c'
    else:
        return 'b'         

    #retaliate

def retaliate(my_history, their_history):
    if len(my_history)==0: # It's the first round; collude.
        return 'c'
    elif my_history[-1]=='c' and their_history[-1]=='b':
        return 'b' # Betray if severely punished last time,
    else:
        return 'c' # otherwise collude.

        #alternate

def alt(my_history):
    if len(my_history)==0:
        return 'c'
    elif my_history[-1]=='c':
        return 'b'
    else:
        return 'c'

    #random

def randim():       
    to_do = random.choice([2,3,4])
    if to_do == 2:
        randim2()
    if to_do == 3:
        randim3()
    if to_do == 4:
        randim4()
       
def randim2():
    return random.choice(['c','b'])

def randim3():
    return random.choice(['c','b','b'])

def randim4():
    return random.choice(['c','c','b'])
    
    #copy previous

def copy(my_history, their_history):
    if len(my_history)==0:
        return random.choice(['c','b'])
    else:
        return their_history[-1]


    #betray if winning
def winning(my_score, their_score):
    if my_score >= their_score:
        return 'b'
        

    #if score > -1000, perform last strategy


    #betray if tie


    #adapt; pick new strategy

def adapt(my_score, their_score):
    if my_score <= (their_score - 1000):
        change = 1
    else:
        change = 0

def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    change = 0
   
    
    if len(my_history)==0:
        strategy = random.choice(['winning', 'copy', 'straight_bs', 'cbb', 'retaliate', 'alt', 'randim'])
        if strategy == 'winning':
            winning(my_score, their_score)
        if strategy == 'copy':
            copy(my_history, their_history)
        if strategy == 'straight_bs':
            straight_bs()
        if strategy == 'cbb':
            cbb(my_history)
        if strategy == 'retaliate':
            retaliate(my_history, their_history)
        if strategy == 'alt':
            alt(my_history)
        if strategy == 'randim':
            randim()
        if len(my_history)%3==0:
            adapt(my_score, their_score)
            if change == 1:
                strategy = random.choice(['winning', 'copy', 'straight_bs', 'cbb', 'retaliate', 'alt', 'randim'])
       
        
    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             