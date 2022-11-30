def create_level():
    teck = []
    with open("first_level.sokoban") as f:
        for rad in f:
            for i in rad:
                teck.append(i)
    return(teck)

def find_player(level):
    a = 0
    for i in displaylevel:
     if displaylevel[a] == "@":
      player = a
      break
     a = a + 1
    return(a)

def move_up(): #w
    a = find_player(displaylevel)
    can_move("w")
    if displaylevel[a - 20] == "o":
                 displaylevel[a - 20] = "@"
                 displaylevel[a] = " "
                 displaylevel[a - 40] = "o"
    elif displaylevel[a - 20] == " " or ".":
             displaylevel[a - 20] = "@"
             displaylevel[a] = " "
    return(displaylevel)

def move_left(): #a
     a = find_player(displaylevel)
     if displaylevel[a - 1] == "o":
             displaylevel[a - 2] = "o"
             displaylevel[a - 1] = "@"
             displaylevel[a] = " "
     elif displaylevel[a - 1] == " " or ".":
             displaylevel[a - 1] = "@"
             displaylevel[a] = " "
     return(displaylevel)

def move_down():
     a = find_player(displaylevel)
     if displaylevel[a + 20] == "o":
             displaylevel[a] = " "
             displaylevel[a + 20] = "@"
             displaylevel[a + 40] = "o"
     elif displaylevel[a + 20] == " " or ".":
             displaylevel[a + 20] = "@"
             displaylevel[a] = " "
     return(displaylevel)

def move_right(): #d
     a = find_player(displaylevel)
     if displaylevel[a + 1] == "o" or displaylevel[a + 1] == "+":
        if displaylevel[a + 2] == ".":
             displaylevel[a] = " "
             displaylevel[a + 1] = "@"
             displaylevel[a + 2] = " +"
        else:
             displaylevel[a] = " "
             displaylevel[a + 1] = "@"
             displaylevel[a + 2] = "o"
     elif displaylevel[a + 1] == " " or ".":
             displaylevel[a + 1] = "@"
             displaylevel[a] = " "
     return(displaylevel)

def can_move(direction):
    a = find_player(displaylevel)
    if direction == "w":
         if displaylevel[a - 20] == "#":
             print("There's a Trump wall in the way, try again")
             return(False)
         elif displaylevel[a - 20] == "o" or displaylevel[a - 20] == "+":
            if displaylevel[a - 40] == "o":
              print("There's an object in the way, try again")
              return(False)
            if displaylevel[a - 40] == "#":
              print("There's a Trump wall in the way, try again")
              return(False)
    elif direction == "d":
        if displaylevel[a + 1] == "#":
          print("There's a Trump  wall in the way, try again")
          return(False)
        elif displaylevel[a + 1] == "o" or displaylevel[a + 1] == "+":
          if displaylevel[a + 2] == "o":
            print("There's an object in the way, try again")
            return(False)
          elif displaylevel[a + 2] == "#":
            print("There's a Trump wall in the way, try again")
            return(False)
    elif direction == "a":
        if displaylevel[a - 1] == "#":
             print("There's a Trump wall in the way, try again")
             return(False)
        elif displaylevel[a - 1] == "o" or displaylevel[a - 1] == "+":
          if displaylevel[a - 2] == "o":
            print("There's an object in the way, try again")
            return(False)
          if displaylevel[a - 2] == "#":
              print("There's a Trump wall in the way, try again")
              return(False)
    elif direction == "s":
        if displaylevel[a + 20] == "#":
             print("There's a wall in the way, try again")
             return(False)
        elif displaylevel[a + 20] == "o" or displaylevel[a + 20] == "+":
          if displaylevel[a + 40] == "o":
            print("There's an object in the way, try again")
            return(False)
          if displaylevel[a + 40] == "#":
              print("There's a Trump wall in the way, try again")
              return(False)

def move_player(level):
     move = input("Which direction do you want to go? Up(w), Down(s), Left(a) or Right(d)? ")
     d = can_move(move)
     print(d)
     #for d in displaylevel:
     if d == False:
            return(level)
     if d == None:
           if move == "w":# UPP
                return(move_up())
           elif move == "d": #d HÖGER
                return(move_right())
           elif move == "a": #a VÄNSTER
                return(move_left())
           elif move == "s": #s NER
                return(move_down())

    #if not d == None:
    #    print(d)
displaylevel = create_level()
print("".join(displaylevel))
win = False
while win == False:
 displaylevel = move_player(displaylevel)
 print("".join(displaylevel))
