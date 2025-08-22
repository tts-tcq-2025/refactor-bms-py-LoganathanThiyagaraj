from typing import Tuple # <--- ADD THIS LINE

# --- Configuration ---
# Simplified thresholds for adult vitals.
ADULT_VITAL_THRESHOLDS = {
    'temperature': {'min': 95.0, 'max': 102.0, 'unit': 'F', 'display_name': 'Temperature'},
    'pulseRate': {'min': 60, 'max': 100, 'unit': 'bpm', 'display_name': 'Pulse Rate'},
    'spo2': {'min': 90, 'max': 100, 'unit': '%', 'display_name': 'Oxygen Saturation'},
}

# --- Core Logic ---
def is_value_critical(value: float, vital_type_name: str, thresholds_config: dict) -> Tuple[bool, str]: # <--- USE Tuple here

    thresholds = thresholds_config.get(vital_type_name)
    if not thresholds:

        return False, f"Unknown vital sign type: {vital_type_name}."

    min_val = thresholds['min']
    max_val = thresholds['max']
    display_name = thresholds['display_name']
    unit = thresholds['unit']

    if value < min_val or value > max_val:
        # The message is still part of the pure function's return for potential debugging/logging
        return True, f"{display_name} is out of range!"
    
    return False, "Normal"


def vitals_ok(
    temperature: float,
    pulseRate: float,
    spo2: float
) -> bool:
 
    vital_readings = [
        ('temperature', temperature),
        ('pulseRate', pulseRate),
        ('spo2', spo2)
    ]

    # No need to collect messages or call an alert function.
    for vital_type_name, value in vital_readings:
        is_critical, _ = is_value_critical(value, vital_type_name, ADULT_VITAL_THRESHOLDS)
        if is_critical:
            # If any vital is critical, the overall status is not OK.
            return False # Exit early as soon as one critical vital is found
            
    # If the loop completes, no critical vitals were found.
    return True
