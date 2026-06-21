def analyze_log(log):

    if "out of sync" in log.lower():
        return {
            "issue": "Synchronization Failure",
            "severity": "Medium"
        }

    return {
        "issue": "Unknown",
        "severity": "Low"
    }
