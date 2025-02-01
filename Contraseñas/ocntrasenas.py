import string
import random

def generar_contrasena(longitud, usar_letras=True, usar_numeros=True, usar_simbolos=True):
    caracteres = ""
    if usar_letras:
        caracteres += string.ascii_letters
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Debes seleccionar al menos un tipo de carácter.")

    contrasena = "".join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def validar_longitud(longitud):
    if longitud < 8:
        print("La longitud mínima recomendada es 8 caracteres.")
        return False
    if longitud > 128:
        print("La longitud máxima recomendada es 128 caracteres.")
        return False
    return True

def main():
    try:
        longitud = int(input('Ingrese el tamaño de la contraseña: '))
        if not validar_longitud(longitud):
            return

        usar_letras = input('¿Incluir letras? (s/n): ').lower() == 's'
        usar_numeros = input('¿Incluir números? (s/n): ').lower() == 's'
        usar_simbolos = input('¿Incluir símbolos? (s/n): ').lower() == 's'

        cantidad = int(input('¿Cuántas contraseñas deseas generar?: '))

        for i in range(cantidad):
            contrasena = generar_contrasena(longitud, usar_letras, usar_numeros, usar_simbolos)
            print(f'Contraseña {i+1}: {contrasena}')

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()