#!/usr/bin/env bash
set -e

echo "🐜 HORMIGASAIS - INICIANDO NODO SOBERANO [LBH-2025]"
echo "---------------------------------------------------"

# 1. Validación de Entorno Virtual
if [ ! -d "venv_xoxo" ]; then
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv_xoxo
fi
source venv_xoxo/bin/activate
pip install -q fastapi uvicorn

# 2. Ejecutar Health Gate previo
python3 tools/health_check.py

# 3. Selección dinámica de puerto (Resiliencia Total)
# Si PORT no está definido, usa 0 para que el sistema asigne uno libre.
TARGET_PORT=${PORT:-0}

echo "🚀 Iniciando Nodo en puerto dinámico..."
echo "🩺 Salud pública activa en: /v1/health"

# 4. Lanzamiento con Uvicorn
python3 -m uvicorn api.main:app \
  --host 127.0.0.1 \
  --port $TARGET_PORT \
  --log-level info
