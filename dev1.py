from paises import dados
from paises import raio 
from random import*
from math import*
from funcoes import normaliza
from funcoes import sorteia_pais
from funcoes import haversine
dic_paises= normaliza(dados)

print('ACERTE O PAÍS')
print('Como funciona:\n O computador sorteia um país e você tem que tentar adivinhar em 20 tentativas\n Se estiver muito difícil pode comprar dicas')
print('Opções:\n -dica\n -desisto\n')
Jogar= input('Vamos jogar?[s/n]')
#perguntar se pode while ou for, jogar== True
if Jogar!= 's' and Jogar!='n':
    print('resposta não esperada')
    Jogar= input('Vamos jogar?[s/n]')
elif Jogar== 's':
    pais= sorteia_pais(dic_paises)
    print ('O país já foi sorteado\nPode começar')
    tentativa= 20
    while tentativa>0:
        chute= input('Qual o país?')
        if chute== pais:
            tentativa== 0
            print('Você acertou!!')
        if chute not in dic_paises.keys() and chute != 'dica' and chute!= 'desisto':
            print('inválido')
            tentativa= tentativa
        else:
            tentativa-= 1
            latitude_p= dic_paises[pais]['geo']['latitude']
            longitude_p= dic_paises[pais]['geo']['longitude']
            latitude= dic_paises[chute]['geo']['latitude']
            longitude= dic_paises[chute]['geo']['longitude']
            distancia= haversine(raio, latitude, longitude, latitude_p, longitude_p)
            print(('{:.2f} km').format(distancia))



    
            

    
        
    
    

