import sys,os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from validator import validate_signals

def test_signal_validation():

    signals = {
        "VehicleSpeed": 80,
        "EngineRPM": 3000
    }

    rules = {
        "VehicleSpeed": {"min": 0, "max": 120},
        "EngineRPM": {"min": 0, "max": 6000}
    }

    result = validate_signals(signals, rules)

    assert result["VehicleSpeed"] == "PASS"
    assert result["EngineRPM"] == "PASS"