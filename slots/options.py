def result():
    from random import randint
    a = randint(1, 3)
    if a == 1:
        b = randint(1,6)
        return([b, b, b])
    elif a == 2:
        b = randint(1, 6)
        c = randint(1, 6)
        while c == b:
            c = randint(1, 6)
        d = randint(0, 2)
        if d == 0:
            return([c, b, b])
        elif d == 1:
            return([b, c, b])
        elif d == 2:
            return([b, b, c])
    elif a == 3:
        b = randint(1, 6)
        c = randint(1, 6)
        while c == b:
            c = randint(1, 6)
        e = randint(1, 6)
        while e == b or e == c:
            e = randint(1, 6)
        d = randint(0, 2)
        if d == 0:
            return([b, c, e])
        elif d == 1:
            return([c, e, b])
        elif d == 2:
            return([e, b, c])

