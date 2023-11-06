#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Spielfeld erzeugen

def draw_board(position):

    print(f"  {position[0]}  |  {position[1]}  |  {position[2]}  \n-----|-----|-----\n  {position[3]}  |  {position[4]}  |  {position[5]}  \n-----|-----|-----\n  {position[6]}  |  {position[7]}  |  {position[8]}  ")

# Möglichkeit Spielzug

def check_if_valid (position, move):
    
    for i in range(len(position)):
        
        if i  == move and position[i] == " " :
            return True
        
    return False

# Gewonnen oder nicht

def check_win_condition(position):
    
    #Reihen
    if position[0] == position[1] ==  position[2] and position[0] != " ":
        return True
    if position[3] == position[4] == position[5] and position[3] != " ":
        return True
    if position[6] == position[7] == position[8] and position[6] != " ":
         return True
        
    #Spalten
    if position[0] == position[3] == position[6] and position[0] != " ":
        return True
    if position[1] == position[4] == position[7] and position[1] != " ":
        return True
    if position[2] == position[5] == position[8] and position[2] != " ":
         return True
    
    #Diagonal
    if position[0] == position[4] == position[8] and position[0] != " ":
        return True
    if position[2] == position[4] == position[6] and position[2] != " ":
        return True

# Unentschieden

def check_if_draw(position):
    if not " " in position:
        return False
    return True  
    

position = [" "] * 9                                           # Erzeugt ein leeres Spielfeld

player1 = (input("Player 1\nYour name: "))
player2 = (input("Player 2\nYour name: "))

score_spieler1 = 0
score_spieler2 = 0

active = True

while active:
    draw_board(position)
    
    valid_move = False
    while not valid_move:
    
        # Zug von Spieler1
        player1zug = int(input(f"{player1}, where do you want to play? [0 - 8] "))
        
        # Zug spielbar?
        valid_move = check_if_valid(position, player1zug)
        
    position [player1zug] = "X"         # Spieler Zug

    draw_board(position)
    if not check_if_draw(position):
        print("No one has won!")
        print(f"--------------------\n-----SCOREBOARD-----\n--------------------\n{player1}       {score_spieler1}\n{player2}       {score_spieler2}\n--------------------")
        quit = input("If you want to quit, press [q], else [y]: ")
        if quit == "q":
            active = False
        position = [" "] * 9  
        continue
    
    # Hat Spieler1 gewonnen?
    if check_win_condition(position):
        score_spieler1 += 1
        print(f"Player {player1} has won!")
        print(f"--------------------\n-----SCOREBOARD-----\n--------------------\n{player1}       {score_spieler1}\n{player2}       {score_spieler2}\n--------------------")
        
        quit = input("If you want to quit, press [q], else [y]: ")
        if quit == "q":
            active = False
        position = [" "] * 9  
        continue
        
    valid_move = False
    while not valid_move:
        
    # Zug von Spieler2
        player2zug = int(input(f"{player2}, where do you want to play? [0 - 8] "))
        
        # Zug spielbar ?
        valid_move = check_if_valid(position, player2zug)
        
    position [player2zug] = "O"        #Spieler Zug
    
    if not check_if_draw(position):
        print("No one has won!")
        print(f"--------------------\n-----SCOREBOARD-----\n--------------------\n{player1}       {score_spieler1}\n{player2}       {score_spieler2}\n--------------------")
        quit = input("If you want to quit, press [q], else [y]: ")
        if quit == "q":
            active = False
        position = [" "] * 9  
        continue
    
    # Hat Spieler2 gewonnen?
    if check_win_condition (position):
        score_spieler2 += 1
        print(f"Player {player2} has won!")
        print(f"--------------------\n-----SCOREBOARD-----\n--------------------\n{player1}       {score_spieler1}\n{player2}       {score_spieler2}\n--------------------")

        quit = input("If you want to quit, press [q], else [y]: ")
        if quit == "q":
            active = False
        position = [" "] * 9  
        continue


# In[ ]:




