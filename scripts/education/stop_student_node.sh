#!/bin/bash
# 🐜 HormigasAIS - Finalizador de Nodo Estudiante
# Autor: Cristhiam Quiñonez

echo "🛑 Retirando enjambre estudiantil..."

# Buscamos los procesos de las hormiguitas y los terminamos
pkill -f "python3 scripts/education/hormiguita"

echo "💤 Todas las hormigas han regresado a la colmena. Nodo en reposo."
