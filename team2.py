####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'The name the team gives to itself' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
global globbest
globbest = ['b', 'b', 'b', 'b', -2000]
global globrev
globrev = 0 

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
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    c7 = 0
    c8 = 0
    c9 = 0
    c10 = 0
    c11 = 0
    c12 = 0
    c13 = 0
    c14 = 0
    c15 = 0
    c16 = 0
    c17 = 0
    c18 = 0
    c19 = 0
    c20 = 0
    c21 = 0
    global globbest
    global globrev
    
    if len(my_history)==0:
        return 'b'
    elif len(my_history)==1:
        return 'b'
    elif len(my_history)==2:
        return 'b'
    elif len(my_history)==3:
        return 'b'
    elif len(my_history)==4:
        return 'c'
    elif len(my_history)==5:
        return 'c'
    elif len(my_history)==6:
        return 'b'
    elif len(my_history)==7:
        return 'c'
    elif len(my_history)==8:
        return 'b'
    elif len(my_history)==9:
        return 'b'
    elif len(my_history)==10:
        return 'c'
    elif len(my_history)==11:
        return 'c'
    elif len(my_history)==12:
        return 'c'
    elif len(my_history)==13:
        return 'c'
    elif len(my_history)==14:
        return 'b'
    elif len(my_history)==15:
        return 'b'
    elif len(my_history)==16:
        return 'b'
    elif len(my_history)==17:
        return 'c'
    elif len(my_history)==18:
        return 'b'
    elif len(my_history)==19:
        return 'c'
    elif len(my_history)==20:
        return 'c'
    elif len(my_history)>20:
        if globrev == 0:
            if my_history[-21]=='c' and their_history[-21]=='c':
                c1 += 0
            elif my_history[-21]=='c' and their_history[-21]=='b':
                c1 -= 500
            elif my_history[-21]=='b' and their_history[-21]=='c':
                c1 += 100
            elif my_history[-21]=='b' and their_history[-21]=='b':
                c1 -= 250
                
            if my_history[-20]=='c' and their_history[-20]=='c':
                c2 += 0
            elif my_history[-20]=='c' and their_history[-20]=='b':
                c2 -= 500
            elif my_history[-20]=='b' and their_history[-20]=='c':
                c2 += 100
            elif my_history[-20]=='b' and their_history[-20]=='b':
                c2 -= 250
            
            if my_history[-19]=='c' and their_history[-19]=='c':
                c3 += 0
            elif my_history[-19]=='c' and their_history[-19]=='b':
                c3 -= 500
            elif my_history[-19]=='b' and their_history[-19]=='c':
                c3 += 100
            elif my_history[-19]=='b' and their_history[-19]=='b':
                c3 -= 250
            
            if my_history[-18]=='c' and their_history[-18]=='c':
                c4 += 0
            elif my_history[-18]=='c' and their_history[-18]=='b':
                c4 -= 500
            elif my_history[-18]=='b' and their_history[-18]=='c':
                c4 += 100
            elif my_history[-18]=='b' and their_history[-18]=='b':
                c4 -= 250
                
            if my_history[-17]=='c' and their_history[-17]=='c':
                c5 += 0
            elif my_history[-17]=='c' and their_history[-17]=='b':
                c5 -= 500
            elif my_history[-17]=='b' and their_history[-17]=='c':
                c5 += 100
            elif my_history[-17]=='b' and their_history[-17]=='b':
                c5 -= 250
                
            if my_history[-16]=='c' and their_history[-16]=='c':
                c6 += 0
            elif my_history[-16]=='c' and their_history[-16]=='b':
                c6 -= 500
            elif my_history[-16]=='b' and their_history[-16]=='c':
                c6 += 100
            elif my_history[-16]=='b' and their_history[-16]=='b':
                c6 -= 250
                
            if my_history[-15]=='c' and their_history[-15]=='c':
                c7 += 0
            elif my_history[-15]=='c' and their_history[-15]=='b':
                c7 -= 500
            elif my_history[-15]=='b' and their_history[-15]=='c':
                c7 += 100
            elif my_history[-15]=='b' and their_history[-15]=='b':
                c7 -= 250
            
            if my_history[-14]=='c' and their_history[-14]=='c':
                c8 += 0
            elif my_history[-14]=='c' and their_history[-14]=='b':
                c8 -= 500
            elif my_history[-14]=='b' and their_history[-14]=='c':
                c8 += 100
            elif my_history[-14]=='b' and their_history[-14]=='b':
                c8 -= 250
                
            if my_history[-13]=='c' and their_history[-13]=='c':
                c9 += 0
            elif my_history[-13]=='c' and their_history[-13]=='b':
                c9 -= 500
            elif my_history[-13]=='b' and their_history[-13]=='c':
                c9 += 100
            elif my_history[-13]=='b' and their_history[-13]=='b':
                c9 -= 250
                
            if my_history[-12]=='c' and their_history[-12]=='c':
                c10 += 0
            elif my_history[-12]=='c' and their_history[-12]=='b':
                c10 -= 500
            elif my_history[-12]=='b' and their_history[-12]=='c':
                c10 += 100
            elif my_history[-12]=='b' and their_history[-12]=='b':
                c10 -= 250
                
            if my_history[-11]=='c' and their_history[-11]=='c':
                c11 += 0
            elif my_history[-11]=='c' and their_history[-11]=='b':
                c11 -= 500
            elif my_history[-11]=='b' and their_history[-11]=='c':
                c11 += 100
            elif my_history[-11]=='b' and their_history[-11]=='b':
                c11 -= 250
                
            if my_history[-10]=='c' and their_history[-10]=='c':
                c12 += 0
            elif my_history[-10]=='c' and their_history[-10]=='b':
                c12 -= 500
            elif my_history[-10]=='b' and their_history[-10]=='c':
                c12 += 100
            elif my_history[-10]=='b' and their_history[-10]=='b':
                c12 -= 250
                
            if my_history[-9]=='c' and their_history[-9]=='c':
                c13 += 0
            elif my_history[-9]=='c' and their_history[-9]=='b':
                c13 -= 500
            elif my_history[-9]=='b' and their_history[-9]=='c':
                c13 += 100
            elif my_history[-9]=='b' and their_history[-9]=='b':
                c13 -= 250
                
            if my_history[-8]=='c' and their_history[-8]=='c':
                c14 += 0
            elif my_history[-8]=='c' and their_history[-8]=='b':
                c14 -= 500
            elif my_history[-8]=='b' and their_history[-8]=='c':
                c14 += 100
            elif my_history[-8]=='b' and their_history[-8]=='b':
                c14 -= 250
                
            if my_history[-7]=='c' and their_history[-7]=='c':
                c15 += 0
            elif my_history[-7]=='c' and their_history[-7]=='b':
                c15 -= 500
            elif my_history[-7]=='b' and their_history[-7]=='c':
                c15 += 100
            elif my_history[-7]=='b' and their_history[-7]=='b':
                c15 -= 250
                
            if my_history[-6]=='c' and their_history[-6]=='c':
                c16 += 0
            elif my_history[-6]=='c' and their_history[-6]=='b':
                c16 -= 500
            elif my_history[-6]=='b' and their_history[-6]=='c':
                c16 += 100
            elif my_history[-6]=='b' and their_history[-6]=='b':
                c16 -= 250
                
            if my_history[-5]=='c' and their_history[-5]=='c':
                c17 += 0
            elif my_history[-5]=='c' and their_history[-5]=='b':
                c17 -= 500
            elif my_history[-5]=='b' and their_history[-5]=='c':
                c17 += 100
            elif my_history[-5]=='b' and their_history[-5]=='b':
                c17 -= 250
            
            if my_history[-4]=='c' and their_history[-4]=='c':
                c18 += 0
            elif my_history[-4]=='c' and their_history[-4]=='b':
                c18 -= 500
            elif my_history[-4]=='b' and their_history[-4]=='c':
                c18 += 100
            elif my_history[-4]=='b' and their_history[-4]=='b':
                c18 -= 250
                
            if my_history[-3]=='c' and their_history[-3]=='c':
                c19 += 0
            elif my_history[-3]=='c' and their_history[-3]=='b':
                c19 -= 500
            elif my_history[-3]=='b' and their_history[-3]=='c':
                c19 += 100
            elif my_history[-3]=='b' and their_history[-3]=='b':
                c19 -= 250
                
            if my_history[-2]=='c' and their_history[-2]=='c':
                c20 += 0
            elif my_history[-2]=='c' and their_history[-2]=='b':
                c20 -= 500
            elif my_history[-2]=='b' and their_history[-2]=='c':
                c20 += 100
            elif my_history[-2]=='b' and their_history[-2]=='b':
                c20 -= 250
                
            if my_history[-1]=='c' and their_history[-1]=='c':
                c21 += 0
            elif my_history[-1]=='c' and their_history[-1]=='b':
                c21 -= 500
            elif my_history[-1]=='b' and their_history[-1]=='c':
                c21 += 100
            elif my_history[-1]=='b' and their_history[-1]=='b':
                c21 -= 250
            
            pattern1 = [my_history[-21], my_history[-20], my_history[-19], my_history[-18], c1 + c2 + c3 + c4]
            pattern2 = [my_history[-20], my_history[-19], my_history[-18], my_history[-17], c2 + c3 + c4 + c5]
            pattern3 = [my_history[-19], my_history[-18], my_history[-17], my_history[-16], c3 + c4 + c5 + c6]
            pattern4 = [my_history[-18], my_history[-17], my_history[-16], my_history[-15], c4 + c5 + c6 + c7]
            pattern5 = [my_history[-17], my_history[-16], my_history[-15], my_history[-14], c5 + c6 + c7 + c8]
            pattern6 = [my_history[-16], my_history[-15], my_history[-14], my_history[-13], c6 + c7 + c8 + c9]
            pattern7 = [my_history[-15], my_history[-14], my_history[-13], my_history[-12], c7 + c8 + c9 + c10]
            pattern8 = [my_history[-14], my_history[-13], my_history[-12], my_history[-11], c8 + c9 + c10 + c11]
            pattern9 = [my_history[-13], my_history[-12], my_history[-11], my_history[-10], c9 + c10 + c11 + c12]
            pattern10 = [my_history[-12], my_history[-11], my_history[-10], my_history[-9], c10 + c11 + c12 + c13]
            pattern11 = [my_history[-11], my_history[-10], my_history[-9], my_history[-8], c11 + c12 + c13 + c14]
            pattern12 = [my_history[-10], my_history[-9], my_history[-8], my_history[-7], c12 + c13 + c14 + c15]
            pattern13 = [my_history[-9], my_history[-8], my_history[-7], my_history[-6], c13 + c14 + c15 + c16]
            pattern14 = [my_history[-8], my_history[-7], my_history[-6], my_history[-5], c14 + c15 + c16 + c17]
            pattern15 = [my_history[-7], my_history[-6], my_history[-5], my_history[-4], c15 + c16 + c17 + c18]
            pattern16 = [my_history[-6], my_history[-5], my_history[-4], my_history[-3], c16 + c17 + c18 + c19]
            pattern17 = [my_history[-5], my_history[-4], my_history[-3], my_history[-2], c17 + c18 + c19 + c20]
            pattern18 = [my_history[-4], my_history[-3], my_history[-2], my_history[-1], c18 + c19 + c20 + c21]
    
            reslist = [pattern1[4], pattern2[4], pattern3[4], pattern4[4], pattern5[4], pattern6[4], pattern7[4], pattern8[4], pattern9[4], pattern10[4], pattern11[4], pattern12[4], pattern13[4], pattern14[4], pattern15[4], pattern16[4], pattern17[4], pattern18[4], globbest[4]]
            if pattern1[4] == max(reslist):
                globbest = pattern1
            if pattern2[4] == max(reslist):
                globbest = pattern2
            if pattern3[4] == max(reslist):
                globbest = pattern3
            if pattern4[4] == max(reslist):
                globbest = pattern4
            if pattern5[4] == max(reslist):
                globbest = pattern5
            if pattern6[4] == max(reslist):
                globbest = pattern6
            if pattern7[4] == max(reslist):
                globbest = pattern7
            if pattern8[4] == max(reslist):
                globbest = pattern8
            if pattern9[4] == max(reslist):
                globbest = pattern9
            if pattern10[4] == max(reslist):
                globbest = pattern10
            if pattern11[4] == max(reslist):
                globbest = pattern11
            if pattern12[4] == max(reslist):
                globbest = pattern12
            if pattern13[4] == max(reslist):
                globbest = pattern13
            if pattern14[4] == max(reslist):
                globbest = pattern14
            if pattern15[4] == max(reslist):
                globbest = pattern15
            if pattern16[4] == max(reslist):
                globbest = pattern16
            if pattern17[4] == max(reslist):
                globbest = pattern17
            if pattern18[4] == max(reslist):
                globbest = pattern18
        
            globrev = 1
            return globbest[0]
        
        else:
            if globrev == 1:
                globrev = 2
                return globbest[1]
            elif globrev == 2:
                globrev = 3
                return globbest[2]
            elif globrev == 3:
                globrev = 0
                return globbest[3]
    return 'c'
    
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