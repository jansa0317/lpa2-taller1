# R1: pedir el número de porciones
def pedir_datos():
    try:
        porciones = int(input("Ingrese el número de porciones (múltiplo de 4): "))
        return porciones
    except ValueError:
        return -1


# R2: calcular la cantidad de los ingredientes
def calcular_ingredientes(porciones):
    if porciones <= 0 or porciones % 4 != 0:
        return (0.0, 0.0, 0.0, 0.0)

    factor = porciones / 4
    harina = 225.0 * factor
    huevos = 1.0 * factor
    leche = 100.0 * factor
    mantequilla = 200.0 * factor
    return (harina, huevos, leche, mantequilla)


# R3: mostrar los ingredientes necesarios
def mostrar_resultados(porciones, ingredientes):
    print(f"\nIngredientes necesarios para {porciones} porciones:")
    print(f"- Harina: {ingredientes[0]} gramos")
    print(f"- Huevos: {ingredientes[1]} unidades")
    print(f"- Leche: {ingredientes[2]} mililitros")
    print(f"- Mantequilla: {ingredientes[3]} gramos")
