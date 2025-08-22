

# --- Configuration ---
# Simplified thresholds for adult vitals.
ADULT_VITAL_THRESHOLDS = {
    'temperature': {'min': 95.0, 'max': 102.0, 'unit': 'F', 'display_name': 'Temperature'},
    'pulseRate': {'min': 60, 'max': 100, 'unit': 'bpm', 'display_name': 'Pulse Rate'},
    'spo2': {'min': 90, 'max': 100, 'unit': '%', 'display_name': 'Oxygen Saturation'},
}

# --- Core Logic ---
def is_value_critical(value: float, vital_type_name: str, thresholds_config: dict) -> tuple[bool, str]:
    """
    Checks if a vital sign value is critical.
    """
    thresholds = thresholds_config.get(vital_type_name)
    if not thresholds:
        # In a no-alert scenario, an unknown vital just means it's not critical.
        # Could also raise an error if an unknown vital is considered a programming mistake.
        return False, f"Unknown vital sign type: {vital_type_name}."

    min_val = thresholds['min']
    max_val = thresholds['max']
    display_name = thresholds['display_name']
    unit = thresholds['unit']

    if value < min_val or value > max_val:
        # The message is still part of the pure function's return for potential debugging/logging
        return True, f"{display_name} out of range!"
    
    return False, "Normal"

# --- Main Monitoring Function ---
# No alert_critical_vitals or _alert_placeholder functions needed anymore.
def vitals_ok(
    temperature: float,
    pulseRate: float,
    spo2: float
) -> bool:
    """
    Monitors a patient's vital signs and returns True if all are OK, False otherwise.
    This function performs no external alerts or I/O.
    Assumes adult patient thresholds.
    """
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
