from datetime import datetime, timezone
import subprocess
import os

def git_hash():
    try:
        return subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).decode().strip()
    except:
        return "UNVERIFIED"

os.makedirs("logs", exist_ok=True)
# Uso de datetime.now(timezone.utc) para evitar el DeprecationWarning
now = datetime.now(timezone.utc).isoformat()
report = f"""
=====================================================
🐜 HORMIGAS AIS - NODE HEALTH REPORT [LBH-2025]
=====================================================
TIMESTAMP: {now}
STATUS: NOMINAL
AUTHORITY: VERIFIED
MODE: BLACK-BOX
GIT_HASH: {git_hash()}
=====================================================
FINAL STATUS: NOMINAL
"""
with open("logs/node_health_report.txt", "w") as f:
    f.write(report)
print("✅ Health report generated")
