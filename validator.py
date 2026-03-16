def validate_signals(signals, rules):
    
    results = {}

    for signal, value in signals.items():

        rule = rules.get(signal)

        if not rule:
            continue

        min_v = rule.get("min")
        max_v = rule.get("max")

        if min_v <= value <= max_v:
            results[signal] = "PASS"
        else:
            results[signal] = "FAIL"

    return results