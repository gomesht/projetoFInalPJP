def validarCpf(cpf):

    
    listacpf = []
    if len(cpf) == 11:
        for i in cpf:
            if i.isnumeric():
                listacpf.append(int(i))
            else:
                return False
        
        mult =0
        for j in range (9):
            
            mult += listacpf[j]*(10-(j))
        divs1 = (mult*10)//11
        res1 = (mult*10)% 11
        mult2=0
        for k in range (10):   
            mult2 += listacpf[k]*(11-(k))
        divs2 = (mult2*10)//11
        res2 = (mult2*10)% 11
        
    
        if res1 == 10:
            res1 = 0
        if res2 == 10:
            res2 = 0
        if res1 == listacpf[9] and res2 == listacpf[10]: 
            return True  
        else:
            return False 
    else:
        return False                 