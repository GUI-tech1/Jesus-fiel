from listas import teste01, teste02
def calculo (teste01=teste01, teste02=teste02):
    SomaX=sum(teste01)
    SomaY=sum(teste02)
    r1 = []
    r4= []
    r8=[]
    for i in range(len(teste01)):
        r1.append(teste01[i] * teste02[i])
    r2=sum(r1)
    r3=(SomaX*SomaY)/len(teste01)
    rcima=r2-r3
    for i in range(len(teste01)):
        r4.append(teste01[i]**2)
    r5=sum(r4)
    r6=SomaX**2/len(teste01)
    r7=r5-r6
    for i in range(len(teste02)):
        r8.append(teste02[i]**2)
    r9=sum(r8)
    r10=SomaY**2/len(teste02)
    r11=r9-r10
    r12=r11*r7
    rbaixo=r12**(1/2)
    Resultado=rcima/rbaixo
    print(Resultado)

calculo()
[29,23,32,43,38] 
400,350,430,505,480