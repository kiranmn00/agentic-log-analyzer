"""
Agentic Log Analyzer

Rule-based log analysis engine with verification support.
"""

from prompts import REPORT_TEMPLATE


def classify_severity(log_text):

    log_text = log_text.lower()

    if "critical" in log_text:
        return "Critical"

    if "los" in log_text:
        return "High"

    if "out of sync" in log_text:
        return "Medium"

    return "Low"


def identify_root_cause(log_text):

    log_text = log_text.lower()

    if "controller not found" in log_text:
        return "Inventory mismatch between management system and device"

    if "out of sync" in log_text:
        return "Synchronization failure"

    if "los" in log_text:
        return "Loss of Signal detected on interface"

    return "Unknown issue"
    

def generate_recommendation(log_text):

    log_text = log_text.lower()

    if "controller not found" in log_text:
        return (
            "- Verify controller exists on device\n"
            "- Verify device-resource-name mapping\n"
            "- Trigger inventory synchronization"
        )

    if "out of sync" in log_text:
        return (
            "- Verify device connectivity\n"
            "- Review synchronization logs\n"
            "- Re-run sync operation"
        )

    if "los" in log_text:
        return (
            "- Verify optical power levels\n"
            "- Check fiber connectivity\n"
            "- Inspect transceiver status"
        )

    return "- Manual investigation required"


def verify_analysis(log_text, root_cause):

    log_text = log_text.lower()

    verification_rules = {

        "Inventory mismatch between management system and device":
            "controller not found" in log_text,

        "Synchronization failure":
            "out of sync" in log_text,

        "Loss of Signal detected on interface":
            "los" in log_text
    }

    return verification_rules.get(root_cause, False)


def analyze_log(log_text):

    severity = classify_severity(log_text)

    root_cause = identify_root_cause(log_text)

    recommendation = generate_recommendation(log_text)

    verified = verify_analysis(log_text, root_cause)

    report = {
        "summary": root_cause,
        "root_cause": root_cause,
        "severity": severity,
        "confidence": "Verified" if verified else "Needs Review",
        "actions": recommendation
    }

    return report


def generate_report(report):

    return REPORT_TEMPLATE.format(
        summary=report["summary"],
        root_cause=report["root_cause"],
        severity=report["severity"],
        confidence=report["confidence"],
        actions=report["actions"]
    )
