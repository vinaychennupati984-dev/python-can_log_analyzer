def build_validation_rules(db):
    
    rules = {}

    for message in db.messages:

        for signal in message.signals:

            rules[signal.name] = {
                "min": signal.minimum,
                "max": signal.maximum
            }

    return rules


def validate_signals(signals, rules):

    errors = []

    for signal, value in signals.items():

        if signal in rules:

            min_val = rules[signal]["min"]
            max_val = rules[signal]["max"]

            if min_val is not None and value < min_val:
                errors.append(f"{signal} below min: {value}")

            if max_val is not None and value > max_val:
                errors.append(f"{signal} above max: {value}")

    return errors