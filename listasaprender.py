variavellista=[4,5,4]
variavellista2=[1,2,3]
print(variavellista)
#printar a classe da variavel
print(type(variavellista))
#printar a soma da lista
print(sum(variavellista))
#printar o tamanho da lista
print(len(variavellista))
#adcionar um elemento na lista
variavellista.append(7)
print(variavellista)
#remover um elemento da lista
variavellista.remove(4)
print(variavellista)
#mostrar conteudo da lista com for
for i in variavellista:
    print(i)
#somar conteudo de duas listas
RESULTADO=sum(variavellista)+sum(variavellista2)
print(RESULTADO)
#somar cada elemento da lista
for i in range(len(variavellista)):
    RESULTADO=variavellista[i]+variavellista2[i]
    print(RESULTADO)
#modificar um elemento da lista
variavellista[0]=10
print(variavellista)
#modificar um elemento da lista com for
for i in range(len(variavellista)):
    variavellista[i]=variavellista[i]+1
    print(variavellista[i])
#limpar a lista
variavellista.clear()
print(variavellista)
