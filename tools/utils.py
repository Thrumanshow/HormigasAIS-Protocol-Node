import datetime
import yaml
import os

CONFIG_PATH = "contracts/config/config.human"

class LBH_Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    INFO = "\033[94m"        # Azul
    WARNING = "\033[93m"     # Amarillo
    CRITICAL = "\033[91m"    # Rojo
    SECURITY = "\033[41m"    # Fondo Rojo
    SUCCESS = "\033[92m"     # Verde
    CORP = "\033[1;34m"      # Azul Negrita
    PREM = "\033[1;36m"      # Cian Negrita
    FREE = "\033[0;32m"      # Verde

def log_event(message, level="INFO"):
    COLORS = {
        "INFO": LBH_Colors.INFO,
        "WARNING": LBH_Colors.WARNING,
        "CRITICAL": LBH_Colors.CRITICAL,
        "SECURITY": LBH_Colors.SECURITY,
        "SUCCESS": LBH_Colors.SUCCESS,
        "CORP": LBH_Colors.CORP,
        "PREM": LBH_Colors.PREM,
        "FREE": LBH_Colors.FREE
    }
    color = COLORS.get(level, LBH_Colors.RESET)
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"{color}[{timestamp}] [{level}] {message}{LBH_Colors.RESET}")

def get_contract_config():
    try:
        if not os.path.exists(CONFIG_PATH): return None
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except: return None

def print_contract_summary():
    config = get_contract_config()
    if not config:
        print(f"\n{LBH_Colors.WARNING}--- ESPERANDO CONFIG.HUMAN ---{LBH_Colors.RESET}")
        return

    print(f"\n{LBH_Colors.BOLD}--- PANEL DE CONTROL HORMIGASAIS LBH ---{LBH_Colors.RESET}")
    for node in config.get('nodes_registry', []):
        ntype = node.get('type')
        level = "CORP" if ntype == "Corporativo" else "PREM" if ntype == "Premium" else "FREE"
        log_event(f"ID: {node['id']} | {node['name']} ({ntype})", level=level)
    print(f"{LBH_Colors.BOLD}---------------------------------------{LBH_Colors.RESET}\n")

