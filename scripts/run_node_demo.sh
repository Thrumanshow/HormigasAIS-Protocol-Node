#!/usr/bin/env bash
set -e
echo "🐜 HORMIGASAIS NODE DEMO — LBH-2025"
echo "----------------------------------"
if [ ! -f contracts/config/config.human ]; then
  echo "❌ AUTHORITY CONTRACT MISSING"
  exit 1
fi
echo "✅ Authority contract validated"
python3 tools/health_check.py
STATUS=$(grep "FINAL STATUS" logs/node_health_report.txt | grep -o "NOMINAL" || true)
if [ "$STATUS" != "NOMINAL" ]; then
  echo "🛑 NODE LOCKED — Health gate failed"
  exit 1
fi
echo "🟢 Node health: NOMINAL"
export NODE_MODE=OBSERVER
echo "🚀 Starting API in Observer Mode..."
python3 -m uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
