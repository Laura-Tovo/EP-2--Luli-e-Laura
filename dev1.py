from paises import dados
from paises import raio 
from random import*
from math import*
from funcoes import normaliza, sorteia_letra
from funcoes import sorteia_pais, esta_na_lista
from funcoes import haversine
from funcoes import sorteia_cor, dicas
from funcoes import adiciona_em_ordem, done

dic_paises= normaliza(dados)

lista_paises_= []
for i in dic_paises.keys():
    x= [i]
    lista_paises_.append(x)

print('ACERTE O PAÍS')
print('Como funciona:\n O computador sorteia um país e você tem que tentar adivinhar em 20 tentativas\n Se estiver muito difícil pode comprar dicas')
print('Opções:\n -dica\n -desisto\n')
Jogar= input('Vamos jogar?[s/n]')

if Jogar!= 's' and Jogar!='n':
    print('resposta não esperada')
    Jogar= input('Vamos jogar?[s/n]')
elif Jogar== 's':
    pais= sorteia_pais(dic_paises)
    print ('O país já foi sorteado\nPode começar')
    tentativa= 20
    while tentativa>-1:
        if tentativa== 20:
            numeros= [1, 2, 3, 4, 5, 6]
            escolhidas=['outras']
            lista_restritas=[]
            lista_sorteadas=[]
            lista_cores=[]
            paises_d= []
    
        print('você tem {} tentativas'.format(tentativa))
        chute= input('Qual o país?')
        chute= chute.lower()
        cond= esta_na_lista(chute, lista_paises_)
        if chute== pais:
            tentativa= 0
            print('Você acertou!!')
        elif chute != 'dica' and chute!= 'desisto' and cond== False:
            print('inválido')
            tentativa= tentativa
        elif chute== 'dica':
            lista_dicas= []
            area= dic_paises[pais]['area']
            populacao= dic_paises[pais]['populacao']
            bandeira=dic_paises[pais]['bandeira']
            cor_bandeira=sorteia_cor(bandeira)
            lista_cores.append(cor_bandeira)
            capital=dic_paises[pais]['capital']
            letra_capital=sorteia_letra(capital,lista_restritas)
            lista_sorteadas.append(letra_capital)
            continente=dic_paises[pais]['continente']
            n= done(bandeira)
            dica= dicas(lista_dicas, numeros)
            print(('Opções de dica:\n{}\n 6. Voltar').format(dica))
            opcao= int(input(('Escolha sua opção: {}').format(numeros)))
            if opcao not in numeros:
                print('opção inválida')
                opcao= int(input(('Escolha sua opção: {}').format(numeros)))
            if opcao== 1 or opcao== 4 or opcao== 5:
                numeros.remove(opcao)
            if opcao== 1:
                print('A área é{}km²'.format(area))
                tentativa-=6
            elif opcao== 2:
                print('Letra da capital {}'.format(lista_sorteadas))
                if len(lista_sorteadas) == len(capital):
                    numeros.remove(2)
                tentativa-= 2
            elif opcao== 3:
                print('Cores da bandeira {}'.format(lista_cores))
                if n == len(lista_cores):
                    numeros.remove(3)
                tentativa-= 4
            elif opcao== 4:
                print('A população é de {} pessoas'.format(populacao))
                tentativa-= 5
            elif opcao==5:
                print('Fica na {}'.format(continente))
                tentativa-= 7
            elif opcao== 6:
                tentativa=tentativa
        elif chute== 'desisto':
            tentativa= 0
        else:  
            tentativa-= 1
            latitude_p= dic_paises[pais]['geo']['latitude']
            longitude_p= dic_paises[pais]['geo']['longitude']
            latitude= dic_paises[chute]['geo']['latitude']
            longitude= dic_paises[chute]['geo']['longitude']
            distancia= haversine(raio, latitude, longitude, latitude_p, longitude_p)
            print(('{:.2f} km').format(distancia))
            lista_ordem= adiciona_em_ordem(chute, distancia, paises_d)
            paises_d= lista_ordem
            lista_ordem=str(lista_ordem)
            lista_ordem=lista_ordem.strip('[]')
            lista_ordem=lista_ordem.replace(',','')
            lista_ordem=lista_ordem.replace('[','')
            lista_ordem=lista_ordem.replace(']','\n')
            print(lista_ordem)    
        if tentativa== 0:
            print('A resposta era {}'.format(pais))
            Jogar= (input('Quer jogar?[s/n]'))
            if Jogar!= 's' and Jogar!='n':
                print('resposta não esperada')
                Jogar= (input('Quer jogar?[s/n]'))
                tentativa= 0
            elif Jogar== 'n':
                tentativa= -1
            elif Jogar== 's':
                pais= sorteia_pais(dic_paises)
                print ('O país já foi sorteado\nPode começar')
                tentativa= 20
        

    
    

