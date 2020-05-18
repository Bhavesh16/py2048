from numpy import *
import random
import argparse
import os
import keyboard
import time



parser = argparse.ArgumentParser()
parser.add_argument('-n','--board_size',type=int,help='Size of board')
parser.add_argument('-w','--winpoint',type=int,help='value for win')
args = parser.parse_args()
n = args.board_size
w = args.winpoint


p = 2
z = []

def mat(n = 5):
    for i in range(n):
        a = []
        for j in range(n):
            a.append(0)
        z.append(a)
    return

def display(n,z):
    for i in range(n):
        for j in range(n):
            print(z[i][j], end=" ")
        print()
    return

def game_state(mat,w = 2048):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == w:
                print("you win")
                exit()
    for i in range(len(mat)-1):
        for j in range(len(mat[0])-1):
            if mat[i][j] == mat[i+1][j] or mat[i][j+1] == mat[i][j]:
                return
    for i in range(len(mat)):  # check for any zero entries
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                return
    for k in range(len(mat)-1):  # to check the left/right entries on the last row
        if mat[len(mat)-1][k] == mat[len(mat)-1][k+1]:
            return
    for j in range(len(mat)-1):  # check up/down entries on last column
        if mat[j][len(mat)-1] == mat[j+1][len(mat)-1]:
            return
    print("game over, you lose")
    exit()

def add_two(mat):
    a = random.randint(0, n-1)
    b = random.randint(0, n-1)
    while(mat[a][b] != 0):
        a = random.randint(0, n-1)
        b = random.randint(0, n-1)
    mat[a][b] = 2
    return mat

def main(n,z):
    key = keyboard.read_key()
    flag = 0
    #upward shift
    if key in ['w', 'W']:
        for j in range(n):
            for i in range(n):
                check = z[i][j]
                for k in range(i + 1, n):
                    if z[k][j] == check or z[k][j] == 0 or check == 0:
                        if z[i][j] == z[k][j] and z[i][j] != 0:
                            z[i][j] = z[i][j] + z[k][j]
                            z[k][j] = 0
                            check = z[i][j]
                            break
                        else:
                            z[i][j] = z[i][j] + z[k][j]
                            z[k][j] = 0
                            check = z[i][j]
                    else:
                        break

    # downward shift
    elif key in ['s', 'S']:
        for j in range(n):
            for i in reversed(range(n)):
                check = z[i][j]
                for k in range(i - 1, -1, -1):
                    if z[k][j] == check or z[k][j] == 0 or check == 0:
                        if z[i][j] == z[k][j] and z[i][j] != 0:
                            z[i][j] = z[i][j] + z[k][j]
                            z[k][j] = 0
                            check = z[i][j]
                            break
                        else:
                            z[i][j] = z[i][j] + z[k][j]
                            z[k][j] = 0
                            check = z[i][j]
                    else:
                        break

    # left shift
    elif key in ['a', 'A']:
        for i in range(n):
            for j in range(n):
                check = z[i][j]
                for k in range(j + 1, n):
                    if z[i][k] == check or z[i][k] == 0 or check == 0:
                        if z[i][j] == z[i][k] and z[i][j] != 0:
                            z[i][j] = z[i][j] + z[i][k]
                            z[i][k] = 0
                            check = z[i][j]
                            break
                        else:
                            z[i][j] = z[i][j] + z[i][k]
                            z[i][k] = 0
                            check = z[i][j]
                    else:
                        break

    # right shift
    elif key in ['d', 'D']:
        for i in range(n):
            for j in reversed(range(n)):
                check = z[i][j]
                for k in range(j - 1, -1, -1):
                    if z[i][k] == check or z[i][k] == 0 or check == 0:
                        if z[i][j] == z[i][k] and z[i][j] != 0:
                            z[i][j] = z[i][j] + z[i][k]
                            z[i][k] = 0
                            check = z[i][j]
                            break
                        else:
                            z[i][j] = z[i][j] + z[i][k]
                            z[i][k] = 0
                            check = z[i][j]
                    else:
                        break
    else:
        print("invalid input")


    for i in range(n):
        for j in range(n):
            if z[i][j] == 0:
                flag = 1
                break

    if flag == 1:
        add_two(z)

    os.system('cls')
    display(n,z)
    time.sleep(1)

    if flag == 0:
        print("Try another move")

    game_state(z,w)
    main(n,z)


mat(n)

for i in range(p):
    a = random.randint(0, n-1)
    b = random.randint(0, n-1)
    if (z[a][b] == 0):
        z[a][b] = 2
    else:
        p = p+1

os.system('cls')
display(n,z)
time.sleep(1)

main(n,z)








