def detect_category(subject, description):

    text = f"{subject} {description}".lower()

    hardware = [
        "printer", "laptop", "desktop",
        "keyboard", "mouse", "monitor",
        "cpu", "scanner"
    ]

    network = [
        "wifi", "network", "internet",
        "lan", "router"
    ]

    account = [
        "login", "password",
        "account", "username"
    ]

    email = [
        "email", "outlook",
        "gmail", "mail"
    ]

    security = [
        "virus", "malware",
        "hack", "phishing"
    ]

    software = [
        "software", "application",
        "app", "install", "update",
        "crash", "error"
    ]

    for word in hardware:
        if word in text:
            return "Hardware"

    for word in network:
        if word in text:
            return "Network"

    for word in account:
        if word in text:
            return "Account"

    for word in email:
        if word in text:
            return "Email"

    for word in security:
        if word in text:
            return "Security"

    for word in software:
        if word in text:
            return "Software"

    return "Other"
def detect_priority(subject, description):

    text = (subject + " " + description).lower()

    high_keywords = [
        "urgent",
        "critical",
        "immediately",
        "server",
        "production",
        "down",
        "crash",
        "not working",
        "failed",
        "error",
        "failure",
        "cannot login",
        "blocked"
    ]

    medium_keywords = [
        "slow",
        "issue",
        "problem",
        "bug",
        "unable",
        "delay",
        "warning",
        "printer",
        "network"
    ]

    for word in high_keywords:

        if word in text:

            return "High"

    for word in medium_keywords:

        if word in text:

            return "Medium"

    return "Low"
def generate_reply(subject, description):

    text = (subject + " " + description).lower()

    if "login" in text or "password" in text:

        return (
            "Please verify your username and password. "
            "If the issue continues, reset your password or contact the administrator."
        )

    elif "network" in text or "internet" in text:

        return (
            "Please check your network connection and restart your router. "
            "If the problem continues, contact the Network Team."
        )

    elif "printer" in text:

        return (
            "Please ensure the printer is powered on and connected properly. "
            "Restart the printer and try again."
        )

    elif "email" in text:

        return (
            "Please verify your email configuration and internet connection. "
            "If the issue continues, contact the Email Support Team."
        )

    elif "software" in text:

        return (
            "Please reinstall the software or update it to the latest version. "
            "If the issue persists, contact Software Support."
        )

    elif "hardware" in text or "laptop" in text:

        return (
            "Please restart the device and check all hardware connections. "
            "If the hardware is damaged, contact the Hardware Team."
        )

    return (
        "Thank you for reporting the issue. "
        "Our support team will investigate and resolve it as soon as possible."
    )