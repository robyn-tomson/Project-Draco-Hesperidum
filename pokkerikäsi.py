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
                number.append('11')
            elif i == 'Q':
                number.append(12)
                number.append('12')
            elif i == 'K':
                number.append(13)
                number.append('13')
            elif i == 'A':
                number.append(14)
                number.append('14')
            else:
                number.append(int(i))
                number.append(i)
        l += 1
    number = sorted(number)
    if kasi.count('♥') == 5 or kasi.count('♦') == 5 or kasi.count('♣') == 5 or kasi.count('♠') == 5:
        if number.count('10') == 1 and number.count('11') == 1 and number.count('12') == 1 and number.count('13') == 1 and number.count('14') == 1:
            z = [temp[temp.index('10')]+temp[temp.index('10') + 1], temp[temp.index('11')]+temp[temp.index('11') + 1], temp[temp.index('12')]+temp[temp.index('12') + 1], temp[temp.index('13')]+temp[temp.index('13') + 1],  temp[temp.index('14')]+temp[temp.index('14') + 1]]
            return(z)
        elif number == list(range(min(number), max(number)+1)):
            z = [] 
            lin = 0
            while lin < 5:
                z.append(temp[temp.index(str(min(number)))] + temp[temp.index(str(min(number))) + 1])
                temp.pop(temp[temp.index(str(min(number))) + 1], temp[temp.index(str(min(number)))])
                lin += 1
            return(z)
        else:
            return('Mast')
    elif number[0] == number[1] and number[0] == number[2] and number[0] == number[3]:
        return('Nelik')
    elif number[1] == number[2] and number[1] == number[3] and number[1] == number[4]:
        return('Nelik')
    elif number[0] == number[1] and number[0] == number[2] and number[3] == number[4]:
        return('Maja')
    elif number[0] == number[1] and number[2] == number[3] and number[2] == number[4]:
        return('Maja')
    elif number == list(range(min(number), max(number)+1)):
        return('Rida')
    elif number[0] == number[1] and number[0] == number[2]:
        return('Kolmik')
    elif number[2] == number[3] and number[2] == number[4]:
        return('Kolmik')
    elif number[0] == number[1] and number[2] == number[3] or number[0] == number[1] and number[3] == number[4]:
        return('Kaks paari')
    elif number[3] == number[4] and number[0] == number[1] or number[3] == number[4] and number[1] == number[2]:
        return('Kaks paari')
    elif number[0] == number[1] or number[1] == number[2] or number[2] == number[3] or number[3] == number[4]:
        return('Üks paar')
    else:
        return('Kõrge kaart')
