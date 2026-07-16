def summarize_news(article):

    title = article["title"]
    source = article["source"]

    url = article.get(
        "url",
        "No URL Available"
    )

    image = article.get(
        "image",
        ""
    )

    news_category = article.get(
        "category",
        "Cybersecurity"
    )


    title_lower = title.lower()


    # Default values
    cve_detected = "No CVE identified"
    attack_method = "Unknown"
    security_area = "General Cybersecurity"


    # CVE Detection
    if "cve-" in title_lower:
        cve_detected = "CVE vulnerability identified"



    # High risk threats
    if any(word in title_lower for word in [
        "ransomware",
        "malware",
        "data theft",
        "stolen",
        "breach",
        "leak"
    ]):

        threat = "HIGH"

        category = "Cyber Attack / Data Compromise"

        attack_method = "Malware or unauthorised access"

        security_area = "Endpoint Security / Data Protection"

        mitre = (
            "T1486 - Data Encrypted for Impact\n"
            "T1078 - Valid Accounts"
        )

        impact = (
            "This article indicates possible malicious activity "
            "including malware infections, unauthorised access, "
            "or sensitive data exposure."
        )

        summary = (
            "This article covers a significant cybersecurity event "
            "which may involve threats such as malware, data exposure "
            "or unauthorised access. Organisations should review "
            "security controls and monitor for related activity."
        )

        recommendation = (
            "- Review security logs\n"
            "- Enable multi-factor authentication\n"
            "- Monitor indicators of compromise\n"
            "- Isolate affected systems if required"
        )



    # Medium risk threats
    elif any(word in title_lower for word in [
        "attack",
        "phishing",
        "scam",
        "security issue",
        "vulnerability",
        "exploit"
    ]):

        threat = "MEDIUM"

        category = "Security Threat / Vulnerability"

        attack_method = "Potential exploitation or social engineering"

        security_area = "Identity Security / Vulnerability Management"

        mitre = (
            "T1566 - Phishing\n"
            "T1190 - Exploit Public-Facing Application"
        )

        impact = (
            "The issue may present a security weakness "
            "that requires investigation and monitoring."
        )

        summary = (
            "This article discusses a potential cybersecurity risk "
            "that may affect systems, users or organisations. "
            "Further investigation and monitoring is recommended."
        )

        recommendation = (
            "- Review affected systems\n"
            "- Apply security patches\n"
            "- Monitor suspicious activity"
        )



    # Low risk updates
    elif any(word in title_lower for word in [
        "update",
        "patch",
        "authentication",
        "passkey"
    ]):

        threat = "LOW"

        category = "Security Improvement"

        attack_method = "Defensive technology enhancement"

        security_area = "Identity and Access Management"

        mitre = (
            "No active attack technique identified"
        )

        impact = (
            "This relates to defensive security improvements "
            "or protection enhancements."
        )

        summary = (
            "This article covers a technology or security improvement "
            "designed to strengthen protection, improve user security "
            "or enhance digital systems."
        )

        recommendation = (
            "- Review the update\n"
            "- Consider implementation where suitable"
        )



    # Unknown/general
    else:

        threat = "MEDIUM"

        category = "General Technology Development"

        attack_method = "Requires investigation"

        security_area = "General Technology"

        mitre = (
            "No MITRE technique identified"
        )

        impact = (
            "Requires further cybersecurity investigation "
            "to determine potential risk."
        )

        summary = (
            "This article covers a technology development that "
            "may impact the cybersecurity or technology landscape. "
            "Further analysis may be required."
        )

        recommendation = (
            "- Monitor developments\n"
            "- Review relevant security controls"
        )



    report = f"""
========================================
AI CYBERSECURITY ANALYSIS
========================================

Title:
{title}

Source:
{source}

Technology Category:
{news_category}

Article URL:
{url}

Image:
{image}

Summary:
{summary}

Attack Category:
{category}

Attack Method:
{attack_method}

Security Area:
{security_area}

Vulnerability Detection:
{cve_detected}

MITRE ATT&CK Mapping:
{mitre}

Security Impact:
{impact}

Threat Level:
{threat}

Recommended Actions:
{recommendation}

"""

    return report