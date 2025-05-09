A=float(input("a:"))
B=float(input("b:"))
C=float(input("c:"))
delta= (B**2) - (4*A*C)
raiz= delta**(1/2)
if A==0:
    X1= (-B+raiz)
    X2= (-B+raiz)
else:
    X1= (-B+raiz)/(2*A)
    X2= (-B-raiz)/(2*A)
print(f'(Delta é igual a {delta}')
print(f'(X1 é igual a {X1} e X2 é igual a {X2})')
