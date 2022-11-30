def create_level(level): 
    x = 0
    y = 0
    d = 0
    t = [] 
    teck = [] 
    levellist = ["first_level.sokoban", "second_level.sokoban", "third_level.sokoban", "fourth_level.sokoban", "fifth_level.sokoban", "sixth_level.sokoban", "seventh_level.sokoban", "eighth_level.sokoban", "ninth_level.sokoban", "tenth_level.sokoban"]
    with open(levellist[level - 1]) as f: 
        for rad in f: 
            for tecken in rad: 
                x = x + 1
                d = d + 1
                if tecken == '\n':
                    y = y + 1
                    x = 0
                if tecken != " ":
                    teck.append({'symb': tecken, 'posy': y, 'posx': x + 1})
                    t.append(d)
    return(teck, t, level)
  
def check(level):
    x = 0
    y = 0
    ll = []
    levellist = ["first_level.sokoban", "second_level.sokoban", "third_level.sokoban", "fourth_level.sokoban", "fifth_level.sokoban", "sixth_level.sokoban", "seventh_level.sokoban", "eighth_level.sokoban", "ninth_level.sokoban", "tenth_level.sokoban"]
    with open(levellist[level - 1]) as f:
        for rad in f:
            for tecken in rad:
                x = x + 1
                ll.append({'symb': tecken, 'posy': y, 'posx': x})
    al = len(ll) 
    return(al) 

def display_level(teck, teckin, al): 
    displaylevel = []
    y = 0
    for i in range(al):
        displaylevel.append(" ")
    for i in teckin: 
        displaylevel[i - 1] = teck[y]['symb']
        y = y + 1
    print("".join(displaylevel)) 
    return(displaylevel)
def board(level):
    create_level(level) 
    teck = create_level(level)[0]
    teckin = create_level(level)[1]
    print("Level:", level)
    print("Good luck! \n")
    goal = []
    check(level)
    al = check(level)
    displaylevel = display_level(teck, teckin, al)
    return(displaylevel)
