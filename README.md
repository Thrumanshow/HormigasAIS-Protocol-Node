# 🐜 HormigasAIS Protocol Node (LBH-2025)

**Infraestructura de Inteligencia Distribuida y Soberana.**

## 🎯 ¿Qué hace?
- **Auto-Validación Determinista:** El nodo se auto-audita antes de iniciar.
- **Soberanía de Datos:** Implementa el Lenguaje Binario HormigasAIS (LBH).
- **Gate de Seguridad:** Bloquea la API si la integridad de salud no es NOMINAL.

## 🛑 ¿Qué NO hace?
- **Fuga de Datos:** No expone IPs, tokens o rutas internas.
- **Voz no Autorizada:** El endpoint `/voice` está bloqueado sin token HVT.
- **Dependencia de Nube:** Operación 100% Edge/Local.

## 🛠️ Cómo se valida (Repetibilidad)
1. Instalar dependencias: `pip install -r requirements.txt`
2. Ejecutar Demo: `./scripts/run_node_demo.sh`
3. Verificar Salud: `curl http://localhost:8000/v1/health`

**Estado: v1.0.0-mvp | Autoridad: Cristhiam Hernández**
