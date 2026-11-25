# Problema 4 - Videoteca digital (Fase 5 - 213022)
# Formato por fila: [Título, Año de lanzamiento, Calificación (1 a 10), Género]
catalogo = [
    ["Dune: Parte Dos", 2024, 8.6, "Ciencia Ficción"],
    ["Parásitos", 2019, 8.5, "Suspenso"],
    ["Oppenheimer", 2023, 8.3, "Biografía"],
    ["Interestelar", 2014, 8.7, "Ciencia Ficción"],
    ["Spider-Man: Un nuevo universo", 2018, 8.4, "Animación"],
    ["El Padrino", 1972, 9.2, "Drama"],
    ["Atrapado en el tiempo", 1993, 8.0, "Comedia"],
]
def contar_titulos(matriz, umbral_calificacion, anio_limite):
    """Cuenta cuántos títulos cumplen simultáneamente calificación y año mínimos."""
    total = 0
    for _titulo, anio, calificacion, _genero in matriz:
        if calificacion >= umbral_calificacion and anio >= anio_limite:
            total += 1
    return total
def main():
    umbral_calificacion = 8.5
    anio_limite = 2015
    resultado = contar_titulos(catalogo, umbral_calificacion, anio_limite)
    print(f"Total de títulos que cumplen ambos criterios: {resultado}")
if __name__ == "__main__":
    main()
# 
# 