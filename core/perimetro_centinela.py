import json
import time
import sys

SENTINEL_ID = "centinela_alfa"
LBH_AUTH_KEY = "01001100" 
MAX_INTENTOS = 3

def ejecutar_lockdown():
    """Acción de defensa extrema: Bloquea el nodo"""
    print("\n[!!!] 🚨 EJECUTANDO PROTOCOLO DE AUTO-BLOQUEO 🚨 [!!!]")
    print("🔒 Cerrando puertos... Encriptando logs de XOXO... Notificando a la Colonia...")
    # Aquí se dispararía el script físico de desconexión
    time.sleep(2)
    print("🌑 Nodo en MODO SOMBRA. Sistema de defensa activo.")
    sys.exit(1) # El proceso se detiene por seguridad

def emitir_feromona_alerta(intento_num):
    alerta = {
        "timestamp": time.time(),
        "origin": SENTINEL_ID,
        "type": "INTRUSION_DETECTED",
        "severity": "HIGH",
        "intentos": f"{intento_num}/{MAX_INTENTOS}",
        "lbh_sign": LBH_AUTH_KEY
    }
    print(f"📡 [XOXO-BUS] 🚨 ALERTA: {json.dumps(alerta)}")

def validar_acceso(paquete_binario):
    return paquete_binario.startswith(LBH_AUTH_KEY)

if __name__ == "__main__":
    print(f"🛡️ Guardián {SENTINEL_ID} iniciado. Umbral de bloqueo: {MAX_INTENTOS} intentos.")
    intentos_fallidos = 0
    
    try:
        while True:
            intento = "11110000" # Simulación de ataque persistente
            
            if not validar_acceso(intento):
                intentos_fallidos += 1
                emitir_feromona_alerta(intentos_fallidos)
                
                if intentos_fallidos >= MAX_INTENTOS:
                    ejecutar_lockdown()
            
            time.sleep(5) # Escaneo más rápido para defensa activa
    except KeyboardInterrupt:
        print("\n🛑 Guardián desactivado por el Arquitecto.")
