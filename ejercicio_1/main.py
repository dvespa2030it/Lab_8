"""
Mapa de puestos

DATOS
puestos = [[1, 0, 1], [0, 0, 1]]
0: disponible. 1: ocupado. Las coordenadas son tuplas (fila, columna), desde cero.

IMPLEMENTA
1. crear_mapa(puestos): devuelve un diccionario {(fila, columna): estado}.
   Utiliza una comprension de diccionarios.
2. obtener_disponibles(puestos): devuelve un set de coordenadas disponibles.
   Utiliza una comprension de conjuntos.
No modifiques el tablero.

COMPROBACIONES CON PRINT
- Muestra el mapa completo y los disponibles.
- Consulta el estado de (1, 2) en el mapa: debe ser 1.
- Disponibles esperados: {(0, 1), (1, 0), (1, 1)}. El orden no importa.
- Agrega y comprueba otro tablero propio.

ANALISIS EN COMENTARIOS
- Cuantas celdas se revisan al obtener los disponibles en el ejemplo?
- Cuantas se revisan para f filas y c columnas? Y para n filas y n columnas?

COMMIT SUGERIDO
Completa ejercicio 1: mapa y puestos disponibles
"""

def crear_mapa(puestos):
    return {(i, j): puestos[i][j] for i in range(len(puestos)) for j in range(len(puestos[i]))}


def obtener_disponibles(puestos):
    return {
        (i, j)
        for i in range(len(puestos))
        for j in range(len(puestos[i]))
        if puestos[i][j] == 0
    }


if __name__ == "__main__":
    puestos = [[1, 0, 1], [0, 0, 1]]

    mapa = crear_mapa(puestos)
    disponibles = obtener_disponibles(puestos)

    print("Mapa completo:", mapa)
    print("Puestos disponibles:", disponibles)
    print("Estado de (1, 2):", mapa[(1, 2)])

    puestos_propios = [[0, 1], [1, 0], [0, 0]]
    mapa_propio = crear_mapa(puestos_propios)
    disponibles_propios = obtener_disponibles(puestos_propios)

    print("Mapa del tablero propio:", mapa_propio)
    print("Disponibles del tablero propio:", disponibles_propios)

# ANALISIS
# En el ejemplo se revisan 2 * 3 = 6 celdas.
# Para f filas y c columnas se revisan f * c celdas.
# Para un tablero cuadrado de n filas y n columnas se revisan n ** 2 celdas.
