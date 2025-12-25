#!/usr/bin/env python3
"""
Hormiguita 1 - Nodo de práctica
Protocolo: LBH-Education
Autor: Cristhiam Quiñonez
"""
import time
import sys
# Aseguramos que pueda encontrar el bus de feromonas
sys.path.append('.') 

try:
    from pheromone_bus import emit_pheromone
except ImportError:
    # Mock para pruebas si el bus no está presente
    def emit_pheromone(name):
        print(f"[SIMULACIÓN] Feromona emitida por: {name}")

def nodo_estudiante_loop(interval=5):
    while True:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"🐜 [{timestamp}] Hormiguita 1: simulando tarea segura...")
        emit_pheromone("Hormiguita1")
        time.sleep(interval)

if __name__ == "__main__":
    nodo_estudiante_loop()
