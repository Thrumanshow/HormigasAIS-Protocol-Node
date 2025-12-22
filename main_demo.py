import time
import os
# --- NUEVA IMPORTACIÓN ---
from scripts.solar_engine import simulate_energy_cycle
# -------------------------

# Intentar cargar las herramientas de color de HormigasAIS
try:
    from tools.utils import log_event, print_contract_summary
except ImportError:
    def log_event(m, level="INFO"):
        colors = {"SUCCESS": "\033[92m", "WARNING": "\033[93m", "INFO": "\033[94m", "RESET": "\033[0m"}
        c = colors.get(level, colors["INFO"])
        print(f"{c}[{level}] {m}{colors['RESET']}")
    def print_contract_summary():
        print("\033[1m--- PANEL DE CONTROL HORMIGASAIS (CARGANDO...) ---\033[0m")

def run_protocol_demo():
    print_contract_summary()
    time.sleep(1)
    
    log_event("INICIANDO PROTOCOLO LBH ENERGY SOLAR", level="SUCCESS")
    time.sleep(1)
    
    # 1. Validación de Integridad
    log_event("PASO 1: Verificando integridad del contrato .human...", level="INFO")
    time.sleep(1)
    
    # 2. Identificación de Nodos
    log_event("PASO 2: Nodo 'Main-Grid' detectado - Nivel Corporativo", level="INFO")
    time.sleep(1)
    
    # 3. Gobernanza
    log_event("PASO 3: Aplicando reglas de gobernanza solar...", level="WARNING")
    time.sleep(1)
    
    # --- NUEVA LÓGICA: EJECUCIÓN DEL MOTOR ---
    log_event("PASO 4: Iniciando ciclo de distribución de carga...", level="INFO")
    time.sleep(1)
    simulate_energy_cycle()
    # -----------------------------------------
    
    log_event("SISTEMA LISTO Y ESPERANDO VOLUNTAD HUMANA (HVT).", level="SUCCESS")

if __name__ == "__main__":
    run_protocol_demo()

