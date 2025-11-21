
from  cuadrado import Cuadrado
from rectangulo import Rectangulo


def sumar_areas(figuras: list):
    total = 0
    for figura in figuras:
        total += figura.area()
    return total


def sumar_perimetros(figuras: list):
    total = 0
    for figura in figuras:
        total += figura.perimetro()
    return total


def main():

    # ========== CREACIÓN DE CUADRADOS ==========
    print("\n" + "=" * 70)
    print("1. CREACIÓN DE CUADRADOS")
    print("=" * 70)

    cuadrado1 = Cuadrado(5)
    print(f"\nCuadrado 1 creado: {cuadrado1}")
    print(f"  Área: {cuadrado1.area()}")
    print(f"  Perímetro: {cuadrado1.perimetro()}")

    cuadrado2 = Cuadrado(8)
    print(f"\nCuadrado 2 creado: {cuadrado2}")
    print(f"  Área: {cuadrado2.area()}")
    print(f"  Perímetro: {cuadrado2.perimetro()}")

    # ========== CREACIÓN DE RECTÁNGULOS ==========
    print("\n" + "=" * 70)
    print("2. CREACIÓN DE RECTÁNGULOS")
    print("=" * 70)

    rectangulo1 = Rectangulo(4, 6)
    print(f"\nRectángulo 1 creado: {rectangulo1}")
    print(f"  Área: {rectangulo1.area()}")
    print(f"  Perímetro: {rectangulo1.perimetro()}")

    rectangulo2 = Rectangulo(10, 3)
    print(f"\nRectángulo 2 creado: {rectangulo2}")
    print(f"  Área: {rectangulo2.area()}")
    print(f"  Perímetro: {rectangulo2.perimetro()}")

    # ========== MODIFICACIÓN DE VALORES VÁLIDOS ==========
    print("\n" + "=" * 70)
    print("3. MODIFICACIÓN DE VALORES VÁLIDOS")
    print("=" * 70)

    print(f"\nAntes: {cuadrado1}")
    cuadrado1.ancho = 10
    cuadrado1.alto = 10
    print(f"Después de modificar el lado a 10: {cuadrado1}")
    print(f"  Nueva área: {cuadrado1.area()}")
    print(f"  Nuevo perímetro: {cuadrado1.perimetro()}")

    print(f"\nAntes: {rectangulo1}")
    rectangulo1.ancho = 7
    rectangulo1.alto = 9
    print(f"Después de modificar a ancho=7, alto=9: {rectangulo1}")
    print(f"  Nueva área: {rectangulo1.area()}")
    print(f"  Nuevo perímetro: {rectangulo1.perimetro()}")

    # ========== VALIDACIÓN DE ERRORES ==========
    print("\n" + "=" * 70)
    print("4. VALIDACIÓN DE VALORES INVÁLIDOS)")
    print("=" * 70)

    print("\n--- Intento 1: Crear cuadrado con lado 0 ---")
    try:
        cuadrado_invalido = Cuadrado(0)
        print("Se creó el cuadrado con valores invalidos")
    except ValueError as e:
        print(f" Error capturado: {e}")

    print("\n--- Intento 2: Crear cuadrado con lado negativo ---")
    try:
        cuadrado_invalido = Cuadrado(-5)
        print("Se creó el cuadrado con valores invalidos")
    except ValueError as e:
        print(f" Error capturado: {e}")

    print("\n--- Intento 3: Crear rectángulo con ancho negativo ---")
    try:
        rectangulo_invalido = Rectangulo(-3, 5)
        print("Se creó el rectángulo con valores invalidos")
    except ValueError as e:
        print(f" Error capturado: {e}")

    print("\n--- Intento 4: Modificar ancho de cuadrado a valor inválido ---")
    try:
        cuadrado2.ancho = -2
        print("Se modificó el cuadrado con valores invalidos")
    except ValueError as e:
        print(f" Error capturado: {e}")
        print(f"   El cuadrado mantiene su valor: {cuadrado2}")
    # Lista con todas las figuras
    figuras = [cuadrado1, cuadrado2, rectangulo1, rectangulo2]

    print("\nLista de figuras:")
    for i, figura in enumerate(figuras, 1):
        print(f"  {i}. {figura}")

    # Sumar áreas usando polimorfismo
    total_areas = sumar_areas(figuras)
    print(f"\n✓ Suma total de áreas: {total_areas}")

    # Sumar perímetros usando polimorfismo
    total_perimetros = sumar_perimetros(figuras)
    print(f"✓ Suma total de perímetros: {total_perimetros}")



if __name__ == "__main__":
    main()


