import time
from tools.utils import log_event, get_contract_config

def simulate_energy_cycle():
    config = get_contract_config()
    if not config:
        log_event("No se pudo cargar la configuración para el ciclo solar.", level="CRITICAL")
        return

    nodes = config.get('nodes_registry', [])
    # Ordenar nodos por prioridad (Mayor a menor)
    nodes.sort(key=lambda x: x.get('priority', 0), reverse=True)

    total_available_kw = 100  # Simulación de entrada solar total
    log_event(f"CICLO SOLAR INICIADO: {total_available_kw}kW disponibles.", level="SUCCESS")
    
    for node in nodes:
        name = node.get('name')
        max_kw = node.get('max_output_kw')
        ntype = node.get('type')
        
        # Lógica de asignación
        allocated = min(total_available_kw, max_kw)
        total_available_kw -= allocated
        
        level = "CORP" if ntype == "Corporativo" else "PREM" if ntype == "Premium" else "FREE"
        
        if allocated > 0:
            log_event(f"ASIGNADO: {allocated}kW a {name} [{ntype}]", level=level)
        else:
            log_event(f"CORTE: {name} en espera de excedente.", level="WARNING")
        
        time.sleep(0.5)

    log_event("CICLO DE DISTRIBUCIÓN FINALIZADO.", level="SUCCESS")

if __name__ == "__main__":
    simulate_energy_cycle()

