def pokerhand(p_kasi):
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
    if kasi.count('♥') == 5 or kasi.count('♦') == 5 or kasi.count('♣') == 5 or kasi.count('♠') == 5:
        if kasi.count('10') == 1 and kasi.count('J') == 1 and kasi.count('Q') == 1 and kasi.count('K') == 1 and kasi.count('A') == 1:
            return('Kuninglik mastirida')
            quit()
        elif number == list(range(min(number), max(number)+1)):
            return('Mastirida')
            quit()
        else:
            return('Mast')
            quit()
    if number[0] == number[1] and number[0] == number[2] and number[0] == number[3]:
        return('Nelik')
        quit()
    if number[1] == number[2] and number[1] == number[3] and number[1] == number[4]:
        return('Nelik')
        quit()
    if number[0] == number[1] and number[0] == number[2] and number[3] == number[4]:
        return('Maja')
        quit()
    if number[0] == number[1] and number[2] == number[3] and number[2] == number[4]:
        return('Maja')
        quit()
    if number == list(range(min(number), max(number)+1)):
        return('Rida')
        quit()
    if number[0] == number[1] and number[0] == number[2]:
        return('Kolmik')
        quit()
    if number[2] == number[3] and number[2] == number[4]:
        return('Kolmik')
        quit()
    if number[0] == number[1] and number[2] == number[3] or number[0] == number[1] and number[3] == number[4]:
        return('Kaks paari')
        quit()
    if number[3] == number[4] and number[0] == number[1] or number[3] == number[4] and number[1] == number[2]:
        return('Kaks paari')
        quit()
    if number[0] == number[1] or number[1] == number[2] or number[2] == number[3] or number[3] == number[4]:
        return('Üks paar')
    else:
        return('Kõrge kaart')
