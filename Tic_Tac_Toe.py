#!/usr/bin/env python
# coding: utf-8


# Below is a set of steps for you to follow to try to create the Tic Tac Toe Milestone Project game!

# #### Some suggested tools before you get started:
# To take input from a user:
# 
#     player1 = input("Please pick a marker 'X' or 'O'")
#     
# Note that input() takes in a string. If you need an integer value, use
# 
#     position = int(input('Please enter a number'))
#     
# <br>To clear the screen between moves:
# 
#     from IPython.display import clear_output
#     clear_output()
#     
# Note that clear_output() will only work in jupyter. To clear the screen in other IDEs, consider:
# 
#     print('\n'*100)
#     
# This scrolls the previous board up out of view. Now on to the program!

# **Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.**

# In[1]:


from IPython.display import clear_output

def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-'+' - '+'-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-'+' - '+'-')
    print(board[1]+'|'+board[2]+'|'+board[3])


# **TEST Step 1:** run your function on a test version of the board list, and make adjustments as necessary

# In[2]:


test_board = ['#','x','x','x','x','x','x','x','x','o']
display_board(test_board)


# **Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using *while* loops to continually ask until you get a correct answer.**

# In[3]:


def player_input():
    marker = ''
    while  marker!= 'x' and marker!= 'o':
        marker = input('choose a marker x or o :')
    player1 = marker    
    if player1 == 'x':
        player2 ='o' 
    else :
        player2 = 'x'
    return (player1 , player2)
        


# **TEST Step 2:** run the function to make sure it returns the desired output

# In[4]:


player1_marker, player2_marker = player_input()
print(player1_marker)


# **Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.**

# In[ ]:


def place_marker(board,marker,position):
    board[position] = marker


place_marker(test_board,'x',7)
display_board(test_board)


# **Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won. **

# In[ ]:


def win_check(board, mark):
    return ((board[7]==mark and board[8]==mark and board[9]==mark) or #across the top
    (board[4]==mark and board[5]==mark and board[6]==mark) or #across the middle
    (board[1]==mark and board[2]==mark and board[3]==mark) or #across the bottom
    (board[7]==mark and board[4]==mark and board[1]==mark) or #down the left
    (board[8]==mark and board[5]==mark and board[2]==mark) or #down the middle
    (board[9]==mark and board[6]==mark and board[3]==mark) or #down the right
    (board[7]==mark and board[5]==mark and board[3]==mark) or #diagonal
    (board[9]==mark and board[5]==mark and board[1]==mark))   
        


# **TEST Step 4:** run the win_check function against our test_board - it should return True

# In[ ]:


win_check(test_board,'x')


# **Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.**

# In[7]:


import random

def choose_first():
    if random.randint(0,1)==0:
        return 'player2'
    else:
        return 'player1'

choose_first()


# **Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.**

# In[8]:


def space_check(board, position):
    return board[position]==' '
space_check(test_board,1)


# In[9]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
        return True
    
full_board_check(test_board)


# **Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.**

# In[ ]:


def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('choose your next number (1-9): '))
    return position
    
    
        
player_choice(test_board)
    


# **Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.**

# In[ ]:


def replay():
    
    while True:
        a = input('Do you want to play again, Yes or No : ').lower()
        if a == 'yes':
            return True
            break
        elif a == 'no':
            return False
            break
        else:
            a = 'invalid input'
            continue
    
    #return input('Do you want to play again, Yes or No :').lower().startswith('y')
        
replay()
    


# **Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!**

# In[ ]:


print('Welcome to Tic Tac Toe!')

while True:
    
    game_board = [' ']*10
    player1_marker , player2_marker = player_input()
    print('player1 is {} and player2 is  {}'.format(player1_marker , player2_marker))
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play the game, Yes or No: ').lower()
    if play_game == 'yes' :
        game_on = True
    else :
        game_on = False
    
    while game_on:
        #Player 1 Turn
        if turn == 'player1':
            
            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board,player1_marker,position)
            
            if win_check(game_board, player1_marker):
                display_board(game_board)
                print('Player 1 won the game')
                game_on = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print('Its a Tie')
                    break
                else:
                    turn = 'player2'
                    
                           
        # Player2's turn.
        else:
            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board,player2_marker,position)
            
            if win_check(game_board, player2_marker):
                display_board(game_board)
                print('Player 2 won the game')
                game_on = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print('Its a Tie')
                    break
                else:
                    turn = 'player1'
            
    if not replay():
        break









