#Tic-Tac-Toe
''' Example boards
 -----------
| x | x | x |
|--- --- ---|
| x | x | x |
|--- --- ---|
| x | x | x |
 ----------- 
 
 x | x | x
--- --- ---
 x | x | x 
--- --- ---
 x | x | x
'''




def intro(keyword):
    '''
    starts the game
    returns output based on input
    starts game then not talked to again
    '''
    keyword.lower()
    if keyword == 'beginning':
        print 'Welcome to Tic-Tac-Toe!'
        print 'Type \'start\' to start, \'help\' for help, or \'rules\' for the game rules'
    elif keyword == 'help':
        print 'follow the directions on the screen!'
    elif keyword == 'rules':
        print 'The goal of the game is to get three of your letter in a row, Xs or Os'
        print 'Write in the two letter combination of any untaken square, such as tm for top middle,'
        print 'and br for bottom right. (b=bottom,m=middle,t=top,l=left,r=right) Firs to three in a row wins!'
    elif keyword == 'start' or keyword == 'start game' or keyword == 'startgame':
        print 'Starting game now!'
        return main()
    else:
        print 'That input is not understood.'
        print 'Type \'start\' to start, \'help\' for help, or \'rules\' for the game rules'
    userKeyword = raw_input('Where would you like to go?')
    return intro(userKeyword)

        
def board(moves):
    '''
    returns game board
    '''
    print (' ' + str(moves.get('tl')) + ' | ' + str(moves.get('tm')) + ' | ' + str(moves.get('tr')))
    print '--- --- ---'
    print (' ' + str(moves.get('ml')) + ' | ' + str(moves.get('mm')) + ' | ' + str(moves.get('mr')))
    print '--- --- ---'
    print (' ' + str(moves.get('bl')) + ' | ' + str(moves.get('bm')) + ' | ' + str(moves.get('br')))
    return
    
   
    
def winner(who):
    print 'Winner is: ' + str(who)
 
def checkIfWin(turn,moves):
    '''
    checks for three in a row
    '''
    player = ''
    if moves != turn%2:
        player == 'X'
    else:
        player == 'O'
        
    print('Checking for a win...')

    if moves.get('tr') == moves.get('tm') == moves.get('tl') == player:
        return True
    elif moves.get('mr') == moves.get('mm') == moves.get('ml') == player:
        return True
    elif moves.get('br') == moves.get('bm') == moves.get('bl') == player:
        return True
    elif moves.get('tr') == moves.get('mr') == moves.get('br') == player:
        return True
    elif moves.get('bm') == moves.get('mm') == moves.get('tm') == player:
        return True
    elif moves.get('bl') == moves.get('ml') == moves.get('tl') == player:
        return True
    elif moves.get('br') == moves.get('mm') == moves.get('tl') == player:
        return True
    elif moves.get('bl') == moves.get('mm') == moves.get('tr') == player:
        return True
    else:
        return False
            


def main():
    '''
    runs the game
    '''
    turn = 1
    remainingSquares = ['tr','tm','tl','mr','mm','ml','br','bm','bl']
    moves = {'tr':' ','tm':' ','tl':' ','mr':' ','mm':' ','ml':' ','br':' ','bl':' ','bm':' '} #holds moves
    gameOver = False
    while gameOver == False: #Runs until game is over :)
        print
        print
        print
        print ('It is turn #' + str(turn))
        print
        board(moves)
        print
        print 'Available moves: ' + str(remainingSquares)
        if turn%2 != 0: #Player 1's turn
            player = 'player one'
        else:
            player = 'player two'
        print 'It is %s\'s turn' % (player)
        newMove = raw_input('Please enter your next move: ')
        if newMove in remainingSquares:
            turn += 1
            if player == 'player one':
                moves.update({newMove:'X'})
            else:
                moves.update({newMove:'O'})
            remainingSquares.remove(newMove)
            if checkIfWin(turn,moves):
                gameOver = True
                winner(player) 
                continue
            else:
                print 'Next Turn!'
        else:
            print str(newMove) + ' is not a valid move! Please enter a vaild move!'
            print remainingSquares
        if turn == 10:
            print 'Cat\'s Game! Game Over!'
            gameOver = True
            continue
    print
    print
    print
    print 'Starting new game...'
    return main()
                
                
            
    
intro('beginning') #starts the game