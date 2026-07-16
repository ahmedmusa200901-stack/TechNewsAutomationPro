from datetime import datetime


def generate_report(analysis_results):

    high_risk = 0

    for result in analysis_results:
        if "Threat Level:\nHIGH" in result:
            high_risk += 1

    report = f"""
==================================================
TECH NEWS AUTOMATION PRO
DAILY CYBERSECURITY REPORT
==================================================

Generated:
{datetime.now().strftime("%d %B %Y %H:%M")}

Articles Analysed:
{len(analysis_results)}

High Risk Threats:
{high_risk}

==================================================

"""

    for result in analysis_results:
        report += result
        report += "\n"

    return report
