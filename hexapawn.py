# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 08:59:44 2020

@author: lawfr
"""
import pandas as pd
import random

def drawgrid(board):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[0][0], board[0][1], board[0][2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[1][0], board[1][1], board[1][2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(board[2][0], board[2][1], board[2][2]))
    print("\t     |     |")
    print("\n")

def isvalidmove(board,i0,j0,i1,j1):
    if (board[i0][j0] != 'O'):
        return 0
    
    if (abs(i1-i0)==1 and j1==j0 and (board[i1][j1]==' ')):
        return 1
    elif ((board[i1][j1]=='X') and abs(j1-j0)==1 and abs(i1-i0)==1):
        return 1
    else:
        return 0
    
data=(
      [2, (['X', 'X', 'X'], ['O', ' ', ' '], [' ', 'O', 'O']), [[0,1,1,0],[0,1,1,1],[0,2,1,2]]],
      [2, (['X', 'X', 'X'], [' ', 'O', ' '], ['O', ' ', 'O']), [[0,0,1,0],[0,0,1,1]]],
      [2, (['X', 'X', 'X'], [' ', ' ', 'O'], ['O', 'O', ' ']), [[0,1,1,2],[0,1,1,1],[0,0,1,0]]],
      
      [4, (['X', ' ', 'X'], ['O', ' ', 'X'], [' ', 'O', ' ']), [[1,2,2,1],[1,2,2,2]]],
      [4, (['X', ' ', 'X'], [' ', 'O', 'X'], ['O', ' ', ' ']), [[0,0,1,0],[0,0,1,1],[0,2,1,1],[1,2,2,2]]],
      [4, (['X', ' ', 'X'], [' ', ' ', 'O'], ['O', ' ', ' ']), [[0,0,1,0]]],
      [4, (['X', ' ', 'X'], ['X', 'O', ' '], [' ', ' ', 'O']), [[0,0,1,1],[0,2,1,1],[1,0,2,0],[0,2,1,2]]],
      [4, (['X', ' ', 'X'], ['O', ' ', ' '], [' ', ' ', 'O']), [[0,2,1,2]]],
      [4, (['X', ' ', 'X'], ['X', ' ', 'O'], [' ', 'O', ' ']), [[1,0,2,0],[1,0,2,1]]],
      [4, (['X', ' ', 'X'], ['O', 'O', ' '], [' ', 'O', ' ']), [[0,2,1,2],[0,2,1,1]]],
      [4, (['X', ' ', 'X'], [' ', 'O', 'O'], [' ', 'O', ' ']), [[0,0,1,1],[0,0,1,0],[0,2,1,1]]],
      [4, (['X', 'X', ' '], ['O', 'O', 'X'], [' ', ' ', 'O']), [[0,0,1,1],[0,1,1,0]]],
      [4, (['X', 'X', ' '], ['O', ' ', 'O'], [' ', ' ', 'O']), [[0,1,1,0],[0,1,1,1],[0,1,1,2]]],
      [4, ([' ', 'X', 'X'], [' ', 'O', ' '], ['O', ' ', ' ']), [[0,2,1,2],[0,2,1,1]]],
      [4, ([' ', 'X', 'X'], ['X', 'O', 'O'], ['O', ' ', ' ']), [[0,1,1,2],[0,2,1,1]]],
      [4, ([' ', 'X', 'X'], ['O', 'X', ' '], [' ', ' ', 'O']), [[0,1,1,0],[1,1,2,1],[1,1,2,2],[0,2,1,2]]],
      [4, ([' ', 'X', 'X'], [' ', 'O', ' '], [' ', ' ', 'O']), [[0,2,1,2],[0,2,1,1]]],
      [4, ([' ', 'X', 'X'], [' ', 'X', 'O'], ['O', ' ', ' ']), [[0,1,1,2],[1,1,2,0],[1,1,2,1]]],
      [4, ([' ', 'X', 'X'], ['O', ' ', 'O'], ['O', ' ', ' ']), [[0,1,1,0],[0,1,1,1],[0,1,1,2]]],
      
      [6, ([' ', ' ', 'X'], ['O', 'X', 'X'], [' ', ' ', ' ']), [[1,1,2,1],[1,2,2,2]]],
      [6, ([' ', ' ', 'X'], [' ', 'O', 'X'], [' ', ' ', ' ']), [[1,2,2,2]]],
      [6, ([' ', ' ', 'X'], ['X', 'X', ' '], [' ', ' ', 'O']), [[1,0,2,0],[1,1,2,1],[1,1,2,2],[0,2,1,2]]],
      [6, (['X', ' ', ' '], ['O', 'O', 'O'], [' ', ' ', ' ']), [[0,0,1,1]]],
      [6, ([' ', ' ', 'X'], ['O', 'O', 'O'], [' ', ' ', ' ']), [[0,2,1,1]]],
      [6, (['X', ' ', 'X'], [' ', 'O', 'O'], [' ', ' ', ' ']), [[0,0,1,0],[0,0,1,1],[0,2,1,1]]],
      [6, (['X', ' ', ' '], [' ', 'O', 'O'], [' ', ' ', ' ']), [[0,0,1,0],[0,0,1,1]]],
      [6, ([' ', 'X', 'X'], ['O', 'O', ' '], [' ', ' ', ' ']), [[0,1,1,0],[0,2,1,2],[0,2,1,1]]],
      [6, ([' ', 'X', 'X'], ['O', 'X', 'O'], [' ', ' ', ' ']), [[0,1,1,0],[0,1,1,2],[1,1,2,1]]],
      [6, (['X', ' ', ' '], ['O', 'O', 'X'], [' ', ' ', ' ']), [[1,2,2,2],[0,0,1,1]]],
      [6, ([' ', 'X', ' '], ['O', 'O', 'X'], [' ', ' ', ' ']), [[1,2,2,2],[0,1,1,0]]],
      [6, ([' ', 'X', ' '], ['O', 'X', ' '], [' ', ' ', ' ']), [[0,1,1,0],[1,1,2,1]]],
      [6, ([' ', 'X', ' '], ['O', 'O', 'X'], [' ', ' ', ' ']), [[0,1,1,0],[1,2,2,2]]],
      [6, ([' ', 'X', ' '], ['X', 'O', 'O'], [' ', ' ', ' ']), [[1,0,2,0],[0,1,1,2]]],
      [6, ([' ', ' ', 'X'], ['X', 'O', ' '], [' ', ' ', ' ']), [[1,0,2,0],[0,2,1,1],[0,2,1,2]]],
      [6, ([' ', ' ', 'X'], ['X', 'X', 'O'], [' ', ' ', ' ']), [[1,0,2,0],[1,1,2,1]]],
      [6, ([' ', 'X', ' '], [' ', 'X', 'O'], [' ', ' ', ' ']), [[0,1,1,2],[1,1,2,1]]],
      [6, (['X', ' ', ' '], ['X', 'O', ' '], [' ', ' ', ' ']), [[0,0,1,1],[1,0,2,0]]]
      
      # [6, ([' ', ' ', 'X'], ['X', 'X', 'O'], [' ', ' ', ' ']), ([1,0,2,0],[1,1,2,1])],
      # [6, ([' ', ' ', 'X'], ['X', 'O', ' '], [' ', ' ', ' ']), ([1,0,2,0],[0,2,1,1],[0,2,1,2])],
      # [6, ([' ', ' ', 'X'], ['X', 'O', 'X'], [' ', ' ', ' ']), ([1,0,2,0],[1,2,2,2],[0,2,1,1])],
      # [6, (['X', ' ', 'X'], ['X', 'O', 'O'], [' ', ' ', ' ']), ([1,0,2,0],[0,0,1,1],[0,2,1,1])],
      # [6, (['X', ' ', 'X'], ['O', 'O', 'X'], [' ', ' ', ' ']), ([1,0,2,0],[0,0,1,1],[0,2,1,1])],
      # [6, ([' ', 'X', 'X'], [' ', 'O', 'O'], [' ', ' ', ' ']), ([0,1,1,2],[0,2,1,1])]      
)
     
moves = pd.DataFrame(data=data, columns=['turn', 'state', 'moves'])

def checkwin(board, symbol):
    count = 0
    for i in range(3):
        if (symbol == 'X' and board[0][i] == 'O'):
            return 1
        elif (symbol == 'O' and board[2][i] == 'X'):
            return 1
        for j in range(3):
            if (board[i][j] == symbol):
                count = count + 1
    
    if(count == 0):
        return 1
        
    for i in range(3):
        for j in range(3):
            if (board[i][j] == 'O'):
                for a in range(-i,i+1):
                    for b in range (-j,j+1):
                        if (isvalidmove(board, i, j, a, b)):
                            return 0
    return 1

def makemove(board,i0,j0,i1,j1):
    if (board[i1][j1]==' '):
        board[i0][j0], board[i1][j1] = board[i1][j1], board[i0][j0]
    else:
        board[i1][j1] = board[i0][j0]
        board[i0][j0] = ' '
    return board

def partita():
    board = ['X' for x in range(3)],[' ' for x in range(3,6)],['O' for x in range(6,9)]
    drawgrid(board)
    global moves
    turn = 1
    while(True):
        if (turn%2==1):   
            try:
                i0,j0 = input("Which O do you want to move (row and column)? ").split()
            except(ValueError):
                print("You did insert the data in the wrong way. Try typing 'row column'")
                i0,j0 = input("Which O do you want to move (row and column)? ").split()
            
            try:
                i1,j1 = input("Where do you want to move it to (row and column)? ").split()
            except(ValueError):
                print("You did insert the data in the wrong way. Try typing 'row column'")
                i1,j1 = input("Where do you want to move it to (row and column)? ").split()
            i0 = int(i0)
            j0 = int(j0)
            i1 = int(i1)
            j1 = int(j1)
            while (not(isvalidmove(board, i0, j0, i1, j1))):
                print("That's an invalid move: try again.")
                i0,j0 = input("Which O do you want to move (row and column)? ").split()
                i1,j1 = input("Where do you want to move it to (row and column)? ").split()
                i0 = int(i0)
                j0 = int(j0)
                i1 = int(i1)
                j1 = int(j1)
            board = makemove(board,i0,j0,i1,j1)
            if(checkwin(board, 'X')):
                print("You won!")
                drawgrid(board)
                moves['moves'][moveindex].remove(todomove)
                return
            drawgrid(board)
            turn = turn + 1
        elif (turn%2==0):
            for a in range(len(moves)):
                if (moves['turn'][a] == turn and moves['state'][a] == board):
                    moveindex = a
                    if (len(moves['moves'][a]) > 0):
                        bead = random.randint(0, len(moves['moves'][a])-1)
                        todomove = moves['moves'][a][bead]
                    elif (len(moves['moves'][a]) == 0):
                        todomove = moves['moves'][a]
                    if (type(todomove)==list):
                        i0 = todomove[0]
                        j0 = todomove[1]
                        i1 = todomove[2]
                        j1 = todomove[3]
                    board = makemove(board, i0, j0, i1, j1)
            
            if(checkwin(board, 'O')):
                print("The computer won!")
                drawgrid(board)
                return
            drawgrid(board)
            turn = turn + 1

for i in range(0,5):
    partita()