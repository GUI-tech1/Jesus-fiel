print('formula da dilatação linear')
print('ΔL = L0 * α * ΔT')
print('oque você quer calcular?')
print('1-variação de comprimento')
print('2-Coeficiente de dilatação linear')
print('3-Variação de temperatura')
op=int(input('Digite o número da opção desejada: '))
def Vcomprimento():
    icomprimento=float(input('Digite o comprimento inicial: '))
    Coeficiente=float(input('Digite o coeficiente de dilatação linear: '))
    Vtemperatura=float(input('Digite a variação de temperatura: '))
    Vcomprimento= icomprimento*Coeficiente*Vtemperatura
    return Vcomprimento
def coeficiente():
    Vcomprimento=float(input('Digite o variação de comprimento'))
    icomprimento=float(input('Digite o comprimento inicial: '))
    Vtemperatura=float(input('Digite a variação de temperatura: '))
    coeficiente= Vcomprimento/(icomprimento*Vtemperatura)
    return coeficiente
def Vtemperatura():
    Fcomprimento=float(input('Digite o variação de comprimento'))
    icomprimento=float(input('Digite o comprimento inicial: '))
    Coeficiente=float(input('Digite o coeficiente de dilatação linear: '))
    Vtemperatura= Fcomprimento/(icomprimento*Coeficiente)
    return Vtemperatura
if op==1:
    
    print(f'A variação de comprimento é {Vcomprimento()}')
elif op==2:
    
    print(f'O coeficiente de dilatação linear é {coeficiente()}')
elif op==3:
    
    print(f'A variação de temperatura é {Vtemperatura()}')
else:
    print('Opção inválida')
    exit()