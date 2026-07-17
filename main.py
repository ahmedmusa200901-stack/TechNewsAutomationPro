import time
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("NEWS_API_KEY"))

from news_fetcher import get_news
from ai_article_writer import create_article
from article_database import save_article


print("=" * 60)
print("        TECH NEWS AUTOMATION PRO")
print("        AI NEWS PUBLISHING SYSTEM")
print("=" * 60)

print()

print("[+] Collecting technology news...")
time.sleep(1)


news = get_news()


if not news:

    print("[-] No news articles found")
    exit()


print(f"[+] Found {len(news)} articles")


published = 0


for article in news:

    print()
    print("[+] Rewriting article:")

    print(
        article["title"]
    )


    rewritten_article = create_article(
        article
    )

    if rewritten_article:
        save_article(
            rewritten_article
        )
        published += 1
    else:
        print("❌ Article skipped")


print()

print(
    f"[+] Successfully published {published} articles"
)


print(
    "[+] Website database updated"
)