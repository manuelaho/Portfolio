#!/usr/bin/env python
# coding: utf-8

import Tic_Tac_Toe_02_board as board
import Tic_Tac_Toe_02_KI as KI

position = board.clear_board()


player1 = (input("Player 1\nYour name: "))
print("Player 2\nYour name: Computer")

score_spieler1 = 0
score_computer = 0

active = True

while active:
    board.draw_board(position)
    
    valid_move = False
    while not valid_move:
    
        # Zug von Spieler1
        player1zug = int(input(f"{player1}, where do you want to play? [0 - 8] "))
        
        # Zug spielbar?
        valid_move = board.check_if_valid(position, player1zug)
        
    position [player1zug] = "X"         # Spieler Zug

    board.draw_board(position)
    
    if not board.check_if_draw(position):
        print("No one has won!")
        print("No one has won!")
        print(f"--------------------\n-----SCOREBOARD-----\n--------------------\n{player1}       {score_spieler1}\nComputer   {score_computer}\n--------------------")
        quit = input("If you want to quit, press [q], else [y]: ")
        if quit == "q":
            active = False
        
        position = board.clear_board()     
        continue
    
    # Hat Spieler1 gewonnen?
    if board.check_win_condition(position):
        score_spieler1 += 1
        print(f"Player {player1} has won!")
        print(f"--------------------\n-----SCOREBOARD-----\n--------------------\n{player1}       {score_spieler1}\nComputer   {score_computer}\n--------------------")
        
        quit = input("If you want to quit, press [q], else [y]: ")
        if quit == "q":
            active = False
        
        position = board.clear_board()     
        continue
        
    valid_move = False
    while not valid_move:
        
    # Zug von Computer
        print("Computer is playing: ")
        computer = KI.make_good_move(position)
        
        # Zug spielbar ?
        valid_move = board.check_if_valid(position, computer)
        
    position [computer] = "O"        # Computer Zug
    
    if not board.check_if_draw(position):
        print("No one has won!")
        print(f"--------------------\n-----SCOREBOARD-----\n--------------------\n{player1}       {score_spieler1}\nComputer   {score_computer}\n--------------------")
        quit = input("If you want to quit, press [q], else [y]: ")
        if quit == "q":
            active = False
        
        position = board.clear_board() 
        continue
    
    # Hat Computer gewonnen?
    if board.check_win_condition(position):
        score_computer += 1
        print("Player Computer has won!")
        print(f"--------------------\n-----SCOREBOARD-----\n--------------------\n{player1}       {score_spieler1}\nComputer   {score_computer}\n--------------------")

        quit = input("If you want to quit, press [q], else [y]: ")
        if quit == "q":
            active = False
        
        position = board.clear_board() 
        continue
