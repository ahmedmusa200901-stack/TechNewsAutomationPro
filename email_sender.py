import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

sender_email = os.getenv("EMAIL_ADDRESS")
sender_password = os.getenv("EMAIL_PASSWORD")
receiver_email = os.getenv("RECIPIENT_EMAIL")


def send_email(subject, body, pdf_file=None):

    msg = EmailMessage()

    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.set_content(body)

    # Attach PDF if available
    if pdf_file:
        with open(pdf_file, "rb") as file:
            pdf_data = file.read()

        msg.add_attachment(
            pdf_data,
            maintype="application",
            subtype="pdf",
            filename=os.path.basename(pdf_file)
        )

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()

        server.login(
            sender_email,
            sender_password
        )

        server.send_message(msg)

        server.quit()

        print("Email sent successfully!")

    except Exception as error:
        print("Email failed:")
        print(error)