def pokerhand(p_kasi):
    temp = []
    kasi = []
    l = 0
    n = [0, 2, 4, 6, 8]
    number = []
    for i in p_kasi:
        if i == '0':
            kasi[-1] = '10'
        else:
            kasi.append(i.upper())
    for i in kasi:
        if l in n:
            if i == 'J':
                number.append(11)
            elif i == 'Q':
                number.append(12)
            elif i == 'K':
                number.append(13)
            elif i == 'A':
                number.append(14)
            else:
                number.append(int(i))
        l += 1
    number = sorted(number)
    if kasi.count('♥') == 5 or kasi.count('♦') == 5 or kasi.count('♣') == 5 or kasi.count('♠') == 5: # mast/mastirida/kuninglikmastirida
        if number.count('10') == 1 and number.count('11') == 1 and number.count('12') == 1 and number.count('13') == 1 and number.count('14') == 1: # kuninglik mastirida
            return(10 + number[-1] / 100 + number[-2] / 10000 + number[-3] / 1000000 + number[-4] / 100000000 + number[-5] / 10000000000)
        elif number == list(range(min(number), max(number)+1)): # mastirida
            return(9 + number[-1] / 100 + number[-2] / 10000 + number[-3] / 1000000 + number[-4] / 100000000 + number[-5] / 10000000000)
        else: # mast
            return(8 + number[-1] / 100 + number[-2] / 10000 + number[-3] / 1000000 + number[-4] / 100000000 + number[-5] / 10000000000)
    elif number[0] == number[1] and number[0] == number[2] and number[0] == number[3] or number[1] == number[2] and number[1] == number[3] and number[1] == number[4]: #  nelik
        return(7 + number[-1] / 100 + number[-2] / 10000 + number[-3] / 1000000 + number[-4] / 100000000 + number[-5] / 10000000000)
    elif number[0] == number[1] and number[2] == number[3] and number[2] == number[4] or number[0] == number[1] and number[0] == number[2] and number[3] == number[4]: # maja
        return(6 + number[-1] / 100 + number[-2] / 10000 + number[-3] / 1000000 + number[-4] / 100000000 + number[-5] / 10000000000)
    elif number == list(range(min(number), max(number)+1)): # rida
        return(5 + number[-1] / 100 + number[-2] / 10000 + number[-3] / 1000000 + number[-4] / 100000000 + number[-5] / 10000000000)
    elif number[2] == number[3] and number[2] == number[4]  or number[0] == number[1] and number[0] == number[2]: # kolmik
        return(4 + number[-1] / 100 + number[-2] / 10000 + number[-3] / 1000000 + number[-4] / 100000000 + number[-5] / 10000000000)
    elif number[3] == number[4] and number[0] == number[1] or number[3] == number[4] and number[1] == number[2] or number[0] == number[1] and number[2] == number[3] or number[0] == number[1] and number[3] == number[4]: # 2 paar
        return(3 + number[-1] / 100 + number[-2] / 10000 + number[-3] / 1000000 + number[-4] / 100000000 + number[-5] / 10000000000)
    elif number[0] == number[1] or number[1] == number[2] or number[2] == number[3] or number[3] == number[4]: # 1 paar
        return(2 + number[-1] / 100 + number[-2] / 10000 + number[-3] / 1000000 + number[-4] / 100000000 + number[-5] / 10000000000)
    else: #suurim kaart
        return(1 + number[-1] / 100 + number[-2] / 10000 + number[-3] / 1000000 + number[-4] / 100000000 + number[-5] / 10000000000)

print(pokerhand('2♥3♥4♥5♥6♥'))
