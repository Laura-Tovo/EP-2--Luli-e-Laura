def normaliza(dic):
    dados_paises= {}
    for cont, dic_paises in dic.items():
        for pais, dic_dados in dic_paises.items():
            dic_dados['continente']= cont
            dados_paises[pais]= dic_dados
    return (dados_paises)

from random import*
def sorteia_pais(dic):
    lista= []
    for i in dic.keys():
        lista.append(i)
    pais= choice(lista)
    return pais

from math import*
def haversine(raio, latitude1, longitude1, latitude2, longitude2):
    latitude_1= (latitude1*pi)/180
    latitude_2= (latitude2*pi)/180
    longitude_1= (longitude1*pi)/180
    longitude_2= (longitude2*pi)/180
    funcao= ((sin((latitude_2 - latitude_1)/2))**2 + (cos(latitude_1))*(cos(latitude_2))*((sin((longitude_2-longitude_1)/2))**2))**0.5 
    distancia= 2*raio*(asin(funcao))
    return distancia


import random
def sorteia_letra(string,lista_restritas):
    #deixar tudo minusculo
    palavra=''
    string = string.lower()
    for c in string:
        if c.isalnum():
            palavra+=c
    
    sorteio=[]
    letras=[]

    for l in palavra:
        letras.append(l)
        
    sorteada=random.choice(letras)
    
    if sorteada in lista_restritas:
        i=0
        while i < len(letras):
            sorteada=random.choice(letras)
            i+=1
    if sorteada in lista_restritas:
        sorteada=''
    lista_restritas.append(sorteada)
    return sorteada

def esta_na_lista(pais,lista):
    cond=True
    lista_limpa=[]
    for item in lista:
        lista_limpa.extend(item)

    if pais not in lista_limpa:
        cond=False
    if pais in lista_limpa:
        cond=True
    return cond

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

escolhidas=['outras']
def sorteia_cor(bandeira):
    cores=[]
    for cor, quantidade in bandeira.items():
        if quantidade > 0:
            cores.append(cor)
    for c in escolhidas:
        cores.remove(c)
    escolha = choice(cores)
    escolhidas.append(escolha)
    return escolha

def done(bandeira):
    n= 0
    for cor, quantidade in bandeira.items():
        if cor == 'outras':
            False
        if quantidade>0:
            n+=1
    return n

lista_dicas=[]
def dicas(lista_dicas, numeros):
    if 1 in numeros:
        lista_dicas.append('1. Área   -   vale 6 tentativas')
    if 2 in numeros:
        lista_dicas.append('2. Letra da capital   -   vale 2 tentativa')
    if 3 in numeros:
        lista_dicas.append('3. Cor da bandeira   -   vale 4 tentativas')
    if 4 in numeros:
        lista_dicas.append('4. População   -   vale 5 tentativas')
    if 5 in numeros:
        lista_dicas.append('5. Continente   -   vale 7 tentativas')
    lista_dicas= str(lista_dicas)
    lista_dicas= lista_dicas.strip('[]')
    lista_dicas= lista_dicas.strip('')
    lista_dicas= lista_dicas.replace(',', '\n')
    return (lista_dicas)
    


        
        