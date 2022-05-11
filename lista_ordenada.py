def adiciona_em_ordem(pais,distancia,lista):
    pais_novo=[pais,distancia]
    if pais_novo in lista:
        condicao = len(lista)-1
    else:
        condicao = len(lista)
    if lista == []:
        lista_nova = [pais_novo]
    else:
        if len(lista)>1:
            if pais_novo not in lista:
                lista_nova=[0]*(len(lista)+1)
            if pais_novo in lista:
                lista_nova=[0]*len(lista)
            i=0
            while i < condicao:
                if pais_novo[1] >= lista[i][1]:
                    lista_nova[i]=lista[i]
                if pais_novo not in lista_nova:
                    if pais_novo[1] < lista[i][1]:
                        lista_nova[i]=pais_novo
                        i-=1
                elif pais_novo in lista_nova:
                    if pais_novo not in lista:
                        lista_nova[i+1]=lista[i]
                    else:
                        lista_nova[i]=lista[i]
                i+=1
            if pais_novo not in lista_nova:
                lista_nova[i]=pais_novo
        if len(lista)==1:
            lista_nova = [0]*2
            if pais_novo[1] < lista[0][1]:
                lista_nova[0] = pais_novo
                lista_nova[1] = lista[0]
            else:
                lista_nova[0] = lista[0]
                lista_nova[1] = pais_novo                
                
            
    return lista_nova