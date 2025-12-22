# LBH Validator – EnergySolar
# Verifica existencia del contrato humano (HAP)

import os
import sys

CONTRACT_PATH = "contracts/config/config.human"

def validate():
    if not os.path.exists(CONTRACT_PATH):
        print("✖ CONTRATO HUMANO NO ENCONTRADO")
        sys.exit(1)

    print("✔ CONTRATO HUMANO VALIDADO")
    print("✔ AUTORIDAD HUMANA PRESENTE")
    print("🔒 EJECUCIÓN PERMANECE BLOQUEADA")
    return True

if __name__ == "__main__":
    validate()
