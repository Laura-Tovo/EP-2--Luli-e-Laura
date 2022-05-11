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
    return sorteada
