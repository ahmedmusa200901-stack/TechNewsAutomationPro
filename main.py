import time

print("=" * 60)
print("        TECH NEWS AUTOMATION PRO")
print("        CYBER THREAT INTELLIGENCE SYSTEM")
print("=" * 60)

print()

print("[+] Collecting cybersecurity news...")
time.sleep(1)

print("[+] Analysing security threats...")
time.sleep(1)

print("[+] Generating reports...")
time.sleep(1)

print("[+] Preparing email delivery...")
time.sleep(1)

print()

from news_fetcher import get_news
from ai_summarizer import summarize_news
from report_generator import generate_report
from report_saver import save_report
from pdf_generator import create_pdf
from email_sender import send_email


news = get_news()

analysis_results = []

for article in news:
    analysis = summarize_news(article)
    analysis_results.append(analysis)


final_report = generate_report(analysis_results)

saved_file = save_report(final_report)

pdf_file = create_pdf(final_report)

send_email(
    "Daily Cybersecurity Report",
    final_report,
    pdf_file
)

print(f"Text report saved as: {saved_file}")
print(f"PDF report created as: {pdf_file}")