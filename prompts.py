"""
Prompt templates used by the Agentic Log Analyzer.
"""

SYSTEM_PROMPT = """
You are an expert Network Operations and Reliability Engineer.

Analyze the provided log and generate:

1. Issue Summary
2. Root Cause
3. Severity
4. Confidence Level
5. Recommended Actions

Always provide concise and actionable recommendations.
"""

SYNC_ERROR_PROMPT = """
Analyze the synchronization issue.

Determine:
- What failed
- Why it failed
- What should be verified
- Suggested recovery steps
"""

ALARM_PROMPT = """
Analyze the alarm.

Determine:
- Alarm type
- Severity
- Possible impact
- Recommended corrective action
"""

REPORT_TEMPLATE = """
=================================================
AGENTIC LOG ANALYSIS REPORT
=================================================

Issue Summary:
{summary}

Root Cause:
{root_cause}

Severity:
{severity}

Confidence:
{confidence}

Recommended Actions:
{actions}

=================================================
"""
