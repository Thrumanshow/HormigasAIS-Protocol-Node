#!/usr/bin/env bash
set -e

echo "🐜 HORMIGASAIS - INICIANDO NODO SOBERANO [LBH-2025]"
echo "---------------------------------------------------"

# 1. Validación de Entorno
if [ ! -d "venv_xoxo" ]; then
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv_xoxo
fi
source venv_xoxo/bin/activate
pip install -q fastapi uvicorn

# 2. Ejecutar Health Check previo
python3 tools/health_check.py

# 3. Lanzar API
echo "🚀 Nodo activo en: http://127.0.0.1:8000"
echo "🩺 Salud pública: http://127.0.0.1:8000/v1/health"
python3 -m uvicorn api.main:app --host 127.0.0.1 --port 8000 --log-level warning
