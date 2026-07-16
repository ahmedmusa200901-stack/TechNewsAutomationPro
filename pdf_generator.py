from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os


def create_pdf(report):

    folder = "Reports"

    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = (
        f"{folder}/Cybersecurity_Report_"
        f"{datetime.now().strftime('%d-%m-%Y_%H-%M')}.pdf"
    )

    pdf = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "TECH NEWS AUTOMATION PRO - CYBERSECURITY REPORT",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    for line in report.split("\n"):
        content.append(
            Paragraph(line, styles["Normal"])
        )
        content.append(Spacer(1, 5))

    pdf.build(content)

    return filename