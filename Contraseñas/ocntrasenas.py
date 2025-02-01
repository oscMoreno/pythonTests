import string
import random

longitud = int(input('Ingrese el tanaño de la contraseña: '))

caracteres = string.ascii_letters + string.digits + string.punctuation

contrasena = "".join(random.choice(caracteres) for i in range(longitud))
print('La contraseña generada es: ' + contrasena)