
#MENU
print("1. Sumatoria ")
print("2. Factorial ")
print("3. Tablas de multiplicar")
print("4. Numero perfecto")
op = int(input("Ingrese una opcion del menu: "))


def sum():
    n = int(input("Ingresa un número para calcular su sumatoria: "))
    s= 0
    for i in range(1, n + 1):
        s += i

    print(f"La sumatoria de {n} es {s}")
    
def fct():
    n = int(input("Ingresa un número para calcular su factorial: "))
    fac= 1
    for i in range(1, n + 1):
        fac *= i
    print(f"El factorial de {n} es {fac}")
    
def mul():
    n = int(input("Ingresa un número para ver su tabla de multiplicar: "))
    print(f"Tabla de multiplicar del {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
        
def perf():
    n = int(input("Ingresa un número para verificar si es un número perfecto: "))
    sd = 0

    for i in range(1, n):
        if n % i == 0:
            sd += i

    if sd == n:
        print(f"{n} es un número perfecto.")
    else:
        print(f"{n} no es un número perfecto.")

if op == 1:
    sum()
elif op == 2:
    fct()
elif op == 3:
    mul()
elif op == 4:
    perf()
else:
    print("Ingrese una opcion que se encuentre en el menu")
    