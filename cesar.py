def cifrar_cesar(texto, llave):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            if caracter.isupper():
                base = ord('A')
            else:
                base = ord('a')
            nuevo_caracter = chr((ord(caracter) - base + llave) % 26 + base)
            resultado += nuevo_caracter
        else:
            resultado += caracter
    return resultado

def descifrar_cesar(texto, llave):
    return cifrar_cesar(texto, -llave)

def main():
    print("=== CIFRADO CÉSAR ===")
    opcion = input("¿Desea (1) Cifrar o (2) Descifrar?: ")
    texto = input("Ingrese el texto: ")
    llave = int(input("Ingrese la llave numérica: "))
    if opcion == "1":
        resultado = cifrar_cesar(texto, llave)
        print("Texto cifrado:", resultado)
    elif opcion == "2":
        resultado = descifrar_cesar(texto, llave)
        print("Texto descifrado:", resultado)
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
