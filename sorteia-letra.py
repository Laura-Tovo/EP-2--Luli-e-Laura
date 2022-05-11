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