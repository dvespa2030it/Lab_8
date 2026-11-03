"""
Reservar y liberar puestos

DATOS
puestos = [[1, 0, 1], [0, 0, 1]]

IMPLEMENTA
1. reservar_puesto(puestos, coordenada): si la coordenada es valida y el puesto
   esta disponible, cambia su estado a 1 y devuelve True. En otro caso, False.
2. liberar_puesto(puestos, coordenada): si la coordenada es valida y el puesto
   esta ocupado, cambia su estado a 0 y devuelve True. En otro caso, False.
Rechaza indices negativos y coordenadas fuera del tablero.
Supone que coordenada es una tupla de dos enteros y el tablero es rectangular,
no vacio y contiene solo 0 y 1. Estas funciones SI modifican el tablero.

COMPROBACIONES CON PRINT
Realiza en orden, sobre el mismo tablero:
- Reservar (0, 1): True.
- Reservar otra vez (0, 1): False.
- Liberar (1, 2): True.
- Liberar otra vez (1, 2): False.
- Reservar (5, 0): False.
- Reservar (-1, 0): False.
Muestra el tablero final y agrega una comprobacion propia.

ANALISIS EN COMENTARIOS
Es necesario recorrer todo el tablero para reservar una coordenada conocida?
Justifica la complejidad de reservar, sin contar la impresion del tablero.

COMMIT SUGERIDO
Completa ejercicio 3: reservas y liberaciones
"""

def reservar_puesto(puestos, coordenada):
    fila, columna = coordenada
    if fila < 0 or fila >= len(puestos):
        return False
    if columna < 0 or columna >= len(puestos[0]):
        return False
    if puestos[fila][columna] != 0:
        return False

    puestos[fila][columna] = 1
    return True


def liberar_puesto(puestos, coordenada):
    fila, columna = coordenada
    if fila < 0 or fila >= len(puestos):
        return False
    if columna < 0 or columna >= len(puestos[0]):
        return False
    if puestos[fila][columna] != 1:
        return False

    puestos[fila][columna] = 0
    return True


if __name__ == "__main__":
    puestos = [[1, 0, 1], [0, 0, 1]]

    print("Reservar (0, 1):", reservar_puesto(puestos, (0, 1)))
    print("Reservar otra vez (0, 1):", reservar_puesto(puestos, (0, 1)))
    print("Liberar (1, 2):", liberar_puesto(puestos, (1, 2)))
    print("Liberar otra vez (1, 2):", liberar_puesto(puestos, (1, 2)))
    print("Reservar (5, 0):", reservar_puesto(puestos, (5, 0)))
    print("Reservar (-1, 0):", reservar_puesto(puestos, (-1, 0)))
    print("Reservar (1, 1), caso propio:", reservar_puesto(puestos, (1, 1)))
    print("Tablero final:", puestos)

# ANALISIS
# No hace falta recorrer el tablero: se accede directamente a la coordenada.
# Validar indices y consultar/modificar un elemento toma tiempo O(1).
