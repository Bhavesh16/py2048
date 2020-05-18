# py2048

# Taking an input
Using argparse library , take 2 inputs n and w for board_size and win resp.

# Getting started
z is n*n square matrix containing all zeros, created using mat function and add two 2's at random position 

# Working of game 
Take key input using keyboard library. Main function contains all 4 shifts up,down,left,right. After every move, add 2 at position containing zero using add_two function. Print result using display function after every move 

# Result of game
Win or lose is checked using game_state function and if result comes, print and exit

# Special imports
os.system('cls') clears screen before every display call to display new one, keyboard library is used so that after every key input, no need to press enter, as keboard.read_only() works very fast, there is time.sleep() of 1 sec. 
