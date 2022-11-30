import os
def find_player(player):

     a = 0
     for i in player:
         if player[a] == "@":
            player = a
            break
         a = a + 1
     return(a)

def move_(move, displaylevel): 
     p = find_player(displaylevel)
     if move == "w":    
         move = -20
     if move == "s":
         move = 20
     if move == "a":
         move = -1
     if move == "d":
         move = 1
     if displaylevel[p + move] == "o" or displaylevel[p + move] == "+":
         if displaylevel[p + move + move] == " ":
             displaylevel[p + move] = "@"
             displaylevel[p] = " "
             displaylevel[p + move + move] = "o"
         elif displaylevel[p + move + move] == ".":
             displaylevel[p + move + move] = "+"
             displaylevel[p] = " "
             displaylevel[p + move] = "@"
     elif displaylevel[p + move] == " " or ".":
         displaylevel[p + move] = "@"
         displaylevel[p] = " "
     return(displaylevel)


def can_move(move, displaylevel): 
     p = find_player(displaylevel)
     if move == "w":    
         move = -20
     if move == "s":
         move = 20
     if move == "a":
         move = -1
     if move == "d":
         move = 1
     if displaylevel[p + move] == "#":
         print("Can't move forward")
         return(False)
     elif displaylevel[p + move] == "o" or displaylevel[p + move] == "+":
         if displaylevel[p + move + move] == "o":
             print("There is a box try different path")
             return(False)
         if displaylevel[p + move + move] == "#":
             print("Can't move forward")
             return(False)
     return(True)

def move_player(level, displaylevel):



     move = input(" Up(w), Down(s), Left(a) or Right(d) ")
     os.system('clear')
     if len(move) > 1 or len(move) == 0:
          print('      ')
          print(' ')
          print(' ')
          return(displaylevel)
     d = can_move(move, displaylevel)
     if d == False:
          print(' ')
          print(' ')
          return(displaylevel)
     elif d == True:
          print('                                  ')
          print(' ')
          print(' ')
          return(move_(move, displaylevel))
         

