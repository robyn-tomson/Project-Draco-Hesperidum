import random
def vaenlane(punktid, round, sinuraha, vaenlaseraha, panus):
    a=0
    if round==0:
        if punktid<2 and panus>5 and random.randint(1,100)<75:
            return "fold"
        elif panus>vaenlaseraha:
            return "call"
        elif punktid>2 and random.randint(1,100)>60 :
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
        elif punktid<1 and panus>15 and random.randint(1,100)<50:
            return "fold"
        elif panus>vaenlaseraha:
            return "call"
        elif punktid>2 and random.randint(1,100)>70:
            a=panus+random.randint(3,15)
            if vaenlaseraha>=a:
                return a
            else:
                return "call"
        elif punktid>3 and random.randint(1,100)>35:
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
        if punktid<2 and panus>5 and random.randint(1,100)<80:
            return "fold"
        elif punktid<2 and panus>15 and random.randint(1,100)<70:
            return "fold"
        elif punktid<1 and panus>5 and random.randint(1,100)<60:
            return "fold"
        elif punktid<1 and panus>15 and random.randint(1,100)<50:
            return "fold"
        elif panus>vaenlaseraha:
            return "call"
        elif punktid>3 and random.randint(1,100)>75:
            a=panus+random.randint(10,20)
            if vaenlaseraha>=a:
                return a
            else:
                return "call"
        elif punktid>2 and random.randint(1,100)>85:
            a=panus+random.randint(10,20)
            if vaenlaseraha>=a:
                return a
            else:
                return "call"
        elif punktid>3 and random.randint(1,100)>70:
            a=panus+random.randint(10,20)
            if vaenlaseraha>=a:
                return a
            else:
                return "call"
        elif random.randint(1,100)>90:
            a=panus+random.randint(5,10)
            if vaenlaseraha>=a:
                return a
            else:
                return "call"
        else:
            return "call"
    if round==3:
        if punktid<2 and panus>5 and random.randint(1,100)<75:
            return "fold"
        elif punktid<2 and panus>15 and random.randint(1,100)<65:
            return "fold"
        elif punktid<1 and panus>5 and random.randint(1,100)<55:
            return "fold"
        elif punktid<1 and panus>5 and random.randint(1,100)<45:
            return "fold"
        elif panus>vaenlaseraha:
            return "call"
        elif punktid>3 and random.randint(1,100)>50:
            a=panus+random.randint(3,10)
            if vaenlaseraha>=a:
                return a
            else:
                return "call"
        elif punktid>2 and random.randint(1,100)>90:
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