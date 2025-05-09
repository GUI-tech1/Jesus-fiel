print('formula da Densidade')
print('D=M/V')
print('oque você quer calcular?')
print('1-densidade')
print('2-massa')
print('3-volume')
op=int(input('Digite o número da opção desejada: '))
def densidade():
    massa = float(input("Digite a massa (em gramas ou kg): "))
    volume = float(input("Digite o volume (em cm³ ou m³): "))
    densidade = massa / volume
    return densidade
def massa():
    densidade = float(input("Digite a densidade (em g/cm³ ou kg/m³): "))
    volume = float(input("Digite o volume (em cm³ ou m³): "))
    massa = densidade * volume
    return massa
def volume():   
    densidade = float(input("Digite a densidade (em g/cm³ ou kg/m³): "))
    massa = float(input("Digite a massa (em gramas ou kg): "))
    volume = massa / densidade
    return volume
if op==1:
    print(f"A densidade é {densidade()} unidades de massa/volume")
elif op==2:
    print(f"A massa é {massa()} unidades de massa")
elif op==3:
    print(f"O volume é {volume()} unidades de volume")