import Sokoboard
import moveplayer
import os

os.system('clear')
level = int(input("Which level do you want to play on? (1 - 10): "))
success = False
os.system('clear')
displaylevel = Sokoboard.board(level)
goal = []
b = 0
x = 0
for i in displaylevel:
 if displaylevel[b] == ".":
  goal.append(b)
 b = b + 1
x = 0
while success == False:
 displaylevel = moveplayer.move_player(level, displaylevel)
 x += 1
 for i in goal:
  if displaylevel[i] == " ":
   displaylevel[i] = "."
 w = 0
 for i in goal:
  if displaylevel[i] == "+":
   w = w + 1
 print("".join(displaylevel))
 print("Boxes placed:", w, "/", len(goal))
 print("MOVES ", x, "times!")
 if w == len(goal):
  print("Congratulations!!!!! You have successfully placed all the boxes")
  success = True
 else:
  w = 0
