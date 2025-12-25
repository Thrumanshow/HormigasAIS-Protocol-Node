#!/bin/bash
# 🐜 HormigasAIS - Iniciador Real-Time (v2.1)
echo "🚀 Despertando colonia con escritura inmediata..."

# Detenemos cualquier residuo previo para limpieza total
pkill -f scripts/education/hormiguita > /dev/null 2>&1

# Lanzamos con -u para evitar el retraso en logs (Buffering)
nohup python3 -u scripts/education/hormiguita1.py > logs/education/hormiguita1.log 2>&1 &
nohup python3 -u scripts/education/hormiguita2.py > logs/education/hormiguita2.log 2>&1 &
nohup python3 -u scripts/education/hormiguita3.py > logs/education/hormiguita3.log 2>&1 &

echo "✨ Enjambre sincronizado. Verifique actividad en 5 segundos."
