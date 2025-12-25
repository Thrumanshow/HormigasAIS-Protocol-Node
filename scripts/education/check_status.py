#!/usr/bin/env python3
"""
HormigasAIS - Monitor de Estado
Lógica: Validación de Feromonas y PIDs
"""
import os
import subprocess

def check_colony():
    print("🔍 [HormigasAIS] Escaneando estado de la colonia...")
    print("-" * 45)
    
    # Lista de hormigas a monitorear
    ants = ["hormiguita1.py", "hormiguita2.py", "hormiguita3.py"]
    
    active_count = 0
    for ant in ants:
        # Buscamos si el proceso está corriendo
        cmd = f"ps aux | grep {ant} | grep -v grep"
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = process.communicate()
        
        status = "🟢 ACTIVA (Emitiendo Feromonas)" if stdout else "🔴 INACTIVA (En Reposo)"
        if stdout: active_count += 1
        
        print(f"🐜 {ant.capitalize().split('.')[0]}: {status}")

    print("-" * 45)
    # Aplicando el Glosario LBH
    if active_count > 0:
        print(f"📊 Resumen M2M: {active_count} nodos coordinados en el borde.")
        print("💡 Tip LBH: Recuerde que los 'Logs Educativos' están en logs/education/")
    else:
        print("⚠️ Alerta: La colonia está en reposo. Use start_student_node.sh")

if __name__ == "__main__":
    check_colony()
