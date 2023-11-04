import random
def vaenlane(punktid, round, sinuraha, vaenlaseraha, panus):
    a=0
    if round==0:
        if punktid<1 and panus>5 and random.randint(1,100)<75:
            return "fold"
        elif panus>vaenlaseraha:
            return "call"
        elif punktid>1 and random.randint(1,100)>75 :
            a=panus+random.randint(1,10)
            if vaenlaseraha>=a:
                return a
            else:
                return "call"
        elif random.randint(1,100)>95:
            a=panus+random.randint(3,15)
            if vaenlaseraha>=a:
                return a
        else:
                return "call"
    if round==1:
        if punktid<1 and panus>5 and random.randint(1,100)<85:
            return "fold"
        elif panus>vaenlaseraha:
            return "call"
        elif punktid>1 and random.randint(1,100)>50:
            a=panus+random.randint(3,15)
            if vaenlaseraha>=a:
                return a
            else:
                return "call"
        elif random.randint(1,100)>95:
            a=panus+random.randint(5,17)
            if vaenlaseraha>=a:
                return a
            else:
                return "call"
        else:
            return "call"
    
    if round==2:
        if punktid<1 and panus>5 and random.randint(1,100)<80:
            return "fold"
        elif panus>vaenlaseraha:
            return "call"
        elif punktid>2 and random.randint(1,100)>75:
            a=panus+random.randint(10,20)
            if vaenlaseraha>=a:
                return a
            else:
                return "call"
        elif random.randint(1,100)>95:
            a=panus+random.randint(5,10)
            if vaenlaseraha>=a:
                return a
            else:
                return "call"
        else:
            return "call"
    if round==3:
        if punktid<1 and panus>5 and random.randint(1,100)<50:
            return "fold"
        elif panus>vaenlaseraha:
            return "call"
        elif punktid>2 and random.randint(1,100)>50:
            a=panus+random.randint(3,10)
            if vaenlaseraha>=a:
                return a
            else:
                return "call"
        elif random.randint(1,100)>95:
            a=panus+random.randint(3,15)
            if vaenlaseraha>=a:
                return a
            else:
                return "call"
        else:
            return "call"
print(vaenlane(0.5,0,100,100,10))