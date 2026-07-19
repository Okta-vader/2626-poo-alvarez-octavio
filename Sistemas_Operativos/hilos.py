#
# import threading
# import time
# import os
#
# # Función que simula una tarea para un hilo
# def tarea_hilo(identificador, delay):
#     # Incrementamos a 15 iteraciones para dar tiempo a capturar los datos en el Sistema Operativo
#     for i in range(15):
#         print(f'Hilo {identificador}: Realizando tarea {i}')
#         time.sleep(delay)
#
# # Mostrar el PID del proceso actual para identificarlo fácilmente en el Administrador de Tareas
# pid_actual = os.getpid()
# print(f"=== PROCESO PYTHON INICIADO ===")
# print(f"PID del Proceso: {pid_actual}")
# print(f"Busca este número (PID) o el nombre 'Python' en tu Monitor de Actividad / Administrador de Tareas.")
# print(f"================================\n")
#
# # Crear instancias de hilos personalizados (Modificados en identificadores y delays)
# hilo1 = threading.Thread(target=tarea_hilo, args=("Servidor-A", 1.0))
# hilo2 = threading.Thread(target=tarea_hilo, args=("BaseDatos-B", 0.8))
# hilo3 = threading.Thread(target=tarea_hilo, args=("API-C", 1.2))
#
# # Iniciar los hilos (Planificación y concurrencia)
# hilo1.start()
# hilo2.start()
# hilo3.start()
#
# # Esperar a que todos los hilos terminen (Sincronización)
# hilo1.join()
# hilo2.join()
# hilo3.join()
#
# print('\nPrograma principal: Todas las tareas concurrentes han sido completadas.')

import threading
import time

# Función que simula una tarea para un hilo
def tarea_hilo(identificador, delay):
    for i in range(5):
        print(f'Hilo {identificador}: Realizando tarea {i}')
        time.sleep(delay)

# Crear instancias de hilos
hilo1 = threading.Thread(target=tarea_hilo, args=(1, 1))
hilo2 = threading.Thread(target=tarea_hilo, args=(2, 0.8))
hilo3 = threading.Thread(target=tarea_hilo, args=(3, 1.2))

# Iniciar los hilos
hilo1.start()
hilo2.start()
hilo3.start()

# Esperar a que todos los hilos terminen
hilo1.join()
hilo2.join()
hilo3.join()

print('Programa principal: Todas las tareas han sido completadas.')
