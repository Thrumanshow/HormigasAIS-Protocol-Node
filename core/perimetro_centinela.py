import json
import time

SENTINEL_ID = "centinela_alfa"
LBH_AUTH_KEY = "01001100" 

def emitir_feromona_alerta(tipo, severidad, detalle):
    alerta = {
        "timestamp": time.time(),
        "origin": SENTINEL_ID,
        "type": "PERIMETRAL_ALERT",
        "severity": severidad,
        "status": "active",
        "detail": detalle,
        "lbh_sign": LBH_AUTH_KEY
    }
    print(f"📡 [XOXO-BUS] 🚨 ALERTA: {json.dumps(alerta)}")

def validar_acceso(paquete_binario):
    return paquete_binario.startswith(LBH_AUTH_KEY)

if __name__ == "__main__":
    print(f"🛡️ Centinela {SENTINEL_ID} iniciado. Vigilando el Borde...")
    try:
        while True:
            # Simulación de escaneo de tráfico en el puerto de video/datos
            intento = "11110000" 
            if not validar_acceso(intento):
                emitir_feromona_alerta("NON_LBH_TRAFFIC", "CRITICAL", f"Protocolo intruso: {intento}")
            time.sleep(10)
    except KeyboardInterrupt:
        print("\n🛑 Centinela desactivado por el Arquitecto.")
