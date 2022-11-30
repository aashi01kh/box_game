def create_level_1(level):
    x = 0
    y = 0
    check = []  
    with open("first_level.sokoban") as f:
        for rad in f:
            for tecken in rad:
                x = x + 1
                if tecken == '\n':
                 y = y + 1
                 x = 0
                if tecken != " ":
                   check.append({'symb': tecken, 'posy': y, 'posx': x})
 
        return(check)

def display_level(check): 
 rad1 = [                    ]
 rad2 = []
 displaylevel = rad1 + rad2
 i = 0
 for l in check:
  while i < check[i]['posx']:
   rad1.append(" ")
   i = i + 1
  if check[i]['posy'] == 0:
    
    rad1.append([check[i]['symb'], check[i]['posx']])
  else: 
   rad2.append({'symb', 'posx'})
  i = i + 1
 return(rad1)
 return(rad2)
 return(displaylevel)

level = 1
check = create_level_1(level)
check = display_level(check)
print(check)

