def enforce_health_gate(report_path="logs/node_health_report.txt"):
    try:
        with open(report_path) as f:
            content = f.read()
        if "FINAL STATUS: NOMINAL" not in content:
            raise SystemExit("NODE_LOCKED: Health gate violation")
    except FileNotFoundError:
        raise SystemExit("NODE_LOCKED: Health report missing")
