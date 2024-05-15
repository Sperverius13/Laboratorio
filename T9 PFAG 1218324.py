# Función para calcular las conversiones
def conv(mts):
    mi = mts / 1609.34
    k = mts / 1000
    p = mts * 3.28084
    pu = p * 12
    y = p / 3

    return y, p, pu, mi, k

# Función para mostrar el resultado
def res(y, p, pu, mi, k):
    print("Equivalencia en yardas: "+str(y) +" yd")
    print("Equivalencia en pies: "+str(p)+" pies")
    print("Equivalencia en pulgadas: "+str(pu)+" inch")
    print("Equivalencia en millas: "+str(mi)+" mll")
    print("Equivalencia en kilometros: "+str(k)+" km")

# Programa principal
if __name__ == "__main__":
    # Solicitar al usuario la cantidad en metros
    mts = float(input("Ingrese una cantidad en metros: "))

    # Calcular las conversiones
    y, p, pu, mi, k = conv(mts)

    # Mostrar el resultado
    res(y, p, pu, mi, k)
