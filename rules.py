def rule_based_decision(ticket):
    summary = ticket.summary.lower()
    severity = ticket.severity.lower()

    code_issue_keywords = ["error", "crash", "bug", "timeout", "exception", "failure", "stack trace"]
    workflow_issue_keywords = ["login", "configuration", "setup", "connection"]
    
    for word in code_issue_keywords:
        if word in summary:
            return "AI_CODE_PATCH", "Detected technical error keywords suggesting code-level issue."
        
    for word in workflow_issue_keywords:
        if word in summary:
            return "VIBE_CODED_WORKFLOW", "Detected configuration or setup issue suitable for scripted troubleshooting."


    if severity == "critical" or severity == "high":
        return "AI_CODE_PATCH", "High severity implies potential production impact needing AI code remediation."

    return "UNCERTAIN", "Unable to classify confidently; requires deeper semantic understanding."
