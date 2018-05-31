import socket

host = socket.gethostname() 
port = 12345 
s = socket.socket() 
s.connect((host, port))
print('connected') 


choices = []

for x in range (0, 9) :
    choices.append(str(x + 1))


winner = 0


def printBoard() :
    print( '\n -----')
    print( '|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
    print( ' -----')
    print( '|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
    print( ' -----')
    print( '|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
    print( ' -----\n')
 
def check():
    if(choices[0]=='X' and choices[4]=='X' and choices[8]=='X' or
        choices[2]=='X' and choices[4]=='X' and choices[6]=='X' or
        choices[0]=='X' and choices[1]=='X' and choices[2]=='X' or
        choices[0]=='X' and choices[3]=='X' and choices[6]=='X' or
        choices[2]=='X' and choices[5]=='X' and choices[8]=='X' or
        choices[3]=='X' and choices[4]=='X' and choices[5]=='X' or
        choices[6]=='X' and choices[7]=='X' and choices[8]=='X' or
        choices[1]=='X' and choices[4]=='X' and choices[7]=='X' ):
            winner=1
            return winner
            
    elif(choices[0]=='O' and choices[4]=='O' and choices[8]=='O' or
        choices[2]=='O' and choices[4]=='O' and choices[6]=='O' or
        choices[0]=='O' and choices[1]=='O' and choices[2]=='O' or
        choices[0]=='O' and choices[3]=='O' and choices[6]=='O' or
        choices[2]=='O' and choices[5]=='O' and choices[8]=='O' or
        choices[3]=='O' and choices[4]=='O' and choices[5]=='O' or
        choices[6]=='O' and choices[7]=='O' and choices[8]=='O' or
        choices[1]=='O' and choices[4]=='O' and choices[7]=='O'):
            winner=2
            return winner
            
    elif(choices[0]!='1' and choices[1]!='2' and choices[2]!='3' and
        choices[3]!='4' and choices[4]!='5' and choices[5]!='6' and
        choices[6]!='7' and choices[7]!='8' and choices[8]!='9'):
            winner=3
            return winner

    
printBoard()

while winner<=0 :
    
    print( 'Player 1: its Your Turn:')
    
    try:
        choice = int(input('>> '))
        choices[choice - 1] = 'X'
        s.send(bytes([choice]))
        printBoard()
        win=check()
        if(win==1):
            print('Player 1 won')
            break
        elif(win==2):
            print('Player 2 won')
            break
        elif(win==3):
            print('Match Draw')
            break

        
    except:
        print('Illegal Value')
        continue
    
    
    data = s.recv(1024)
    data=int.from_bytes(data, byteorder='big') 
    choices[data - 1] = 'O'
    printBoard()
    win=check()
    if(win==1):
        print('Player 1 won')
        break
    elif(win==2):
        print('Player 2 won')
        break
    elif(win==3):
        print('Match Draw')
        break

s.close()
