def convertir_entre_bases(numero, base_original):
    try:
        # Convertir a decimal
        decimal = int(numero, base_original)

        # Convertir a binario
        binario = bin(decimal)[2:]

        # Convertir a hexadecimal
        hexadecimal = hex(decimal)[2:]

        return decimal, binario, hexadecimal

    except ValueError:
        return None, None, None

def main():
    print("Programa de conversión entre bases numéricas")
    print("Ingrese un número y su base original")

    while True:
        numero = input("Número: ")

        if numero.lower() == 'exit':
            break

        try:
            base_original = int(input("Base (2 para binario, 10 para decimal, 16 para hexadecimal): "))
        except ValueError:
            print("Por favor, ingrese una base válida.")
            continue

        decimal, binario, hexadecimal = convertir_entre_bases(numero, base_original)

        if decimal is not None:
            print(f"\nEn Decimal: {decimal}")
            print(f"En Binario: {binario}")
            print(f"En Hexadecimal: {hexadecimal}\n")
        else:
            print("Error: Número o base no válidos. Intente nuevamente.\n")

if __name__ == "__main__":
    main()
