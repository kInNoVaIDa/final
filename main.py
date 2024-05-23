from funciones import char_to_byte
from funciones import word_to_bytes
from funciones import byte_to_ascii

def main():
    opcion = int(input("1. [cosa 1]\n2. [COSA2]\n3. [COSA3]\n"))
    if opcion == 1:
        a = input("Ingrese una caracter: ")
        binario = char_to_byte(a)
        print(binario)
    elif opcion == 2:
        a = input("Ingrese una palabra: ")
        binario = word_to_bytes(a)
        print(binario)
    elif opcion == 3:
        a = input("Ingresa un binario: ")
        binario = byte_to_ascii(a)
        print (binario)


if __name__ == "__main__":
    main()