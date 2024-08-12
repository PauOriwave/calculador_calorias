# Base de datos de calorías por 100 gramos
calorias_ingredientes = {
    "manzana": 52,
    "banana": 89,
    "arroz": 130,
    "pollo": 239,
    "brocoli": 34,
    "pasta": 131,
    "leche": 42,  # por 100 ml
}

def obtener_ingredientes():
    ingredientes = {}
    while True:
        nombre = input("Ingrese el nombre del ingrediente (o 'salir' para terminar): ").lower()
        if nombre == 'salir':
            break
        if nombre not in calorias_ingredientes:
            print("Ingrediente no encontrado en la base de datos. Inténtelo de nuevo.")
            continue
        
        cantidad = float(input(f"Ingrese la cantidad de {nombre} en gramos: "))
        ingredientes[nombre] = cantidad
    return ingredientes


def calcular_calorias(ingredientes):
    calorias_totales = 0
    for nombre, cantidad in ingredientes.items():
        calorias_por_100g = calorias_ingredientes[nombre]
        calorias = (calorias_por_100g / 100) * cantidad
        calorias_totales += calorias
        print(f"{cantidad}g de {nombre} aportan {calorias:.2f} calorías.")
    return calorias_totales

def main():
    print("Calculadora de Calorías")
    ingredientes = obtener_ingredientes()
    calorias_totales = calcular_calorias(ingredientes)
    print(f"\nCalorías totales: {calorias_totales:.2f} calorías")

if __name__ == "__main__":
    main()