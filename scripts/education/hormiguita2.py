#!/usr/bin/env python3
"""
Hormiguita 2 - Nodo de práctica
Protocolo: LBH-Education | Autor: Cristhiam Quiñonez
"""
import time
import sys
sys.path.append('.') 

try:
    from pheromone_bus import emit_pheromone
except ImportError:
    def emit_pheromone(name):
        print(f"[SIMULACIÓN] Feromona emitida por: {name}")

def nodo_estudiante_loop(interval=7): # Intervalo diferente para variar el bus
    while True:
        timestamp = time.strftime("%H:%M:%S")
        print(f"🐜 [{timestamp}] Hormiguita 2: procesando datos educativos...")
        emit_pheromone("Hormiguita2")
        time.sleep(interval)

if __name__ == "__main__":
    nodo_estudiante_loop()
