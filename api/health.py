from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/health")
def health():
    """
    Endpoint de observabilidad pública.
    Solo expone metadatos de salud, nunca secretos internos.
    """
    return {
        "status": "OPERATIONAL",
        "sovereignty": "ENFORCED",
        "version": "LBH-2025",
        "last_check": datetime.utcnow().isoformat() + "Z",
        "origin": "San Miguel, SV"
    }
