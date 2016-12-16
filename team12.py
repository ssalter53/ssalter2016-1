team_name = 'Harambae'
strategy_name = 'Passive Aggressive'
strategy_description = 'Collude until some one betrayes then betray'
    
def move(my_history, their_history, my_score, their_score):

    if len(their_history) > 1:
    
        if their_history[-1] == 'c':
            return 'c'
        elif their_history[-1] == 'b':
            return 'b'
    
    return 'c'

def test_move(my_history, their_history, my_score, their_score, result):
   
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
     
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
    test_move(my_history='bbb',
              their_history='ccc', 
              my_score=0, 
              their_score=0,
              result='b')             