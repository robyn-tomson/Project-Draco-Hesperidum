import random
def vaenlane(punktid, round, raha, vaenlaseraha, panus):
    if round==0:
        if vaenlaseraha<panus:
            return "call"
        if punktid>1 and random.randint(1,100)>75 :
          return 10
        elif randint(1,100)>95:
            return 15
        elif punktid>1 and panus>5 and random.randint(1,100)<80:
            return "fold"
        else:
            return "call"
    if round==1:
        if punktid>1 and random.randint(1,100)>50:
          return 15
        elif random.randint(1,100)>95:
            if vaenlaseraha<15:
                return vaenlaseraha
            else:
                return 15
        elif(panus>10 and random.randint(1,100)<75 and punktid<1):
            return "fold"
        else:
            return "call"
    
    if round==2:
        if punktid>2 and random.randint(1,100)>75:
          return 20
        elif randint(1,100)>95:
            return 15
        elif(panus>15 and random.randint(1,100)<70 and punktid<1):
            return "fold"
        else:
            return "call"
    if round==3:
        if punktid>2 and random.randint(1,100)>50:
          return 25
        elif randint(1,100)>95:
            return 15
        elif(panus>20 and random.randint(1,100)<65 and punktid<1):
            return "fold"
        else:
            return "call"
print(vaenlane(2,1,100,100,5))