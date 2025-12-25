#!/usr/bin/env python3
"""
Hormiguita 3 - Nodo de práctica
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

def nodo_estudiante_loop(interval=10): # Más lenta, simulando tarea pesada
    while True:
        timestamp = time.strftime("%H:%M:%S")
        print(f"🐜 [{timestamp}] Hormiguita 3: validando entorno seguro...")
        emit_pheromone("Hormiguita3")
        time.sleep(interval)

if __name__ == "__main__":
    nodo_estudiante_loop()
