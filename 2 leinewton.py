print('2 lei de newton')
print('F = m * a')
print('oque você quer calcular?')
print('1-Força')
print('2-Massa')
print('3-Aceleração')
op=int(input('Digite o número da opção desejada: '))
def forca():
    massa = float(input("Digite o valor da massa (em kg):"))  
    aceleracao = float(input("Digite o valor da aceleração (em m/s²):"))
    forca = massa * aceleracao
    return forca
def massa():
    forca = float(input("Digite o valor da força (em N):"))
    aceleracao = float(input("Digite o valor da aceleração (em m/s²):"))
    massa = forca / aceleracao
    return massa
def aceleracao():
    massa = float(input("Digite o valor da massa (em kg):"))
    forca = float(input("Digite o valor da força (em N):"))
    aceleracao = forca / massa
    return aceleracao

if op==1:
    print(f'A força resultante é: {forca()} newtons')
elif op==2:
    print(f'A massa é: {massa()} kg')
elif op==3:
    print(f'A aceleração é: {aceleracao()} m/s²')