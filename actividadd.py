def validar_lista_num(lista:list) -> int:
    for i in lista:
        if i %2 == 0:
            pares.append(i)
        else:
            inpares.append(i)

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
pares = []
inpares = []

print(lista)
print(pares)
print(inpares)