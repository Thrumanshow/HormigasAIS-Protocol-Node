from fastapi import APIRouter, HTTPException
from datetime import datetime, timezone
import os

router = APIRouter()

@router.get("/health")
def public_health():
    """Observabilidad Pública - Sanitizada"""
    return {
        "status": "OPERATIONAL",
        "sovereignty": "ENFORCED",
        "version": "LBH-2025-MVP",
        "origin": "San Miguel, SV"
    }

@router.get("/status")
def internal_status():
    """Estado Interno - Solo si hay Salud Nominal"""
    if not os.path.exists("logs/node_health_report.txt"):
        raise HTTPException(status_code=503, detail="Health report missing")
    return {"mode": "BLACK-BOX", "gate": "LOCKED", "auth": "VERIFIED"}

@router.get("/voice")
def voice_endpoint():
    """Bloqueado por HVT - Requiere Firma Humana"""
    raise HTTPException(status_code=403, detail="VOICE_LOCKED: Human Validation Token (HVT) Required")
