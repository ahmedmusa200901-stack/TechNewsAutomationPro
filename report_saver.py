from datetime import datetime
import os


def save_report(report):

    folder = "Reports"

    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = (
        f"{folder}/Cyber_Report_"
        f"{datetime.now().strftime('%d-%m-%Y_%H-%M')}.txt"
    )

    with open(filename, "w", encoding="utf-8") as file:
        file.write(report)

    return filename