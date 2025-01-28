import time

def temporizador(segundos):
    while segundos:
        mins = segundos // 60
        secs = segundos % 60
        tiempo_restante = f'{mins:02d}:{secs:02d}'
        print(tiempo_restante, end='\r')  # Muestra el tiempo en la misma línea
        time.sleep(1)  # Espera un segundo
        segundos -= 1  # Resta un segundo

    print("\n¡Tiempo finalizado!")  # Mensaje al terminar el temporizador

# Solicita el tiempo al usuario
tiempo_ingresado = int(input("Ingrese la cantidad de segundos: "))
temporizador(tiempo_ingresado)
