
def bubble_sort(lista):  # função com nome bubble-sort(ordenação por troca), recebe lista como argumento

    for i in range(0, len(lista) - 1):      # loop itera lista completa
        for j in range(len(lista) - 1):     # loop itera lista e compara dois elementos em cada iteração
            if lista[j] > lista[j + 1]:     # se posição j na lista for maior que j+1
                temp = lista[j]             # valor da posição j pasa para temp(temporario)
                lista[j] = lista[j + 1]     # então posição j rece o valor da posição j+1
                lista[j + 1] = temp         # e posição j+1 recebe o valor da variavel temp
                                            # repetira o loop até que j não seja maior que j+1
    return lista
    # retorna a lista

lista = [9, 7, 8, 6, 12, 22, 5, 3, 1, 23]

print("Lista sem ordenação: ", lista)

# chamando a função bubble_sorte

print("Lista ordenada: ", bubble_sort(lista))



