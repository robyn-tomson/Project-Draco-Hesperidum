def pokerhand(kasi):
    number = []
    paarid=[]
    rida=[]
    mast=[]
    paaridenumbrid=[]
    a=0
    c=0
    for i in kasi:
        number.append(int(i[:-1]))
        mast.append(i[-1])
    if number[0]<number[1]:
        c=number[0]
        number[0]=number[1]
        number[1]=c
    rida=number[:]
    rida.sort
    if mast.count('♥') >= 5 or mast.count('♦') >= 5 or mast.count('♣') >= 5 or mast.count('♠') >= 5: # mast/mastirida/kuninglikmastirida
        if number.count('10') >= 1 and number.count('11') >= 1 and number.count('12') >= 1 and number.count('13') >= 1 and number.count('14') >= 1: # kuninglik mastirida
            return(10 + number[0] / 100 + number[1] /10000)
        for i in range(len(rida)-1):
            if rida[i]==rida[i+1]-1:
                a+=1
                if a==4:
                    return(9 + number[0] / 100 + number[1] /10000)
            elif rida[i]!=rida[i+1]:
                a=0
        return(8 + number[0] / 100 + number[1] /10000)
    for el in number:
        if number.count(el)>1:
            if el not in paaridenumbrid:
                paarid.append(number.count(el))
                paaridenumbrid.append(el)
    if len(paarid)>3:
        return (7 + number[0] / 100 + number[1] /10000)
    if len(paarid)>0:
        if max(paarid)>2 and len(paarid)>1:
            return (6 + number[0] / 100 + number[1] /10000)
    for i in range(len(rida)-1):
        if rida[i]+1==rida[i+1]:
            a+=1
            if a==4:
                return(5 + number[0] / 100 + number[1] /10000)
        elif rida[i]!=rida[i+1]:
            a=0  
    if len(paarid)>0: 
        if max(paarid)==3:
            return (4 + number[0] / 100 + number[1] /10000)
        if max(paarid)==2:
            return (2 + number[0] / 100 + number[1] /10000)
    else:
        return 1 + number[0] / 100 + number[1] /10000
