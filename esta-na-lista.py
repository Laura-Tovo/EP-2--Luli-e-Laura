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